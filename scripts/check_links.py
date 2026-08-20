#!/usr/bin/env python3
"""Check every link in the Markdown files of this repository.

A dead link in a reference list is worse than a missing row, so this runs
weekly in CI and opens an issue when something rots.

Statuses:
  ok            2xx or a redirect chain ending in 2xx
  needs-review  401, 403, 405, 429 - almost always bot filtering, not rot
  dead          404, 410, 5xx after retries, DNS failures, timeouts

Writes link-report.md and link-results.json. Exits 1 if anything is dead.

Usage: python3 scripts/check_links.py [--files README.md ...]
"""

from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BROWSER_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)
HEADERS = {
    "User-Agent": BROWSER_UA,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

# Hosts that answer an automated client with a challenge no matter what.
# Their links are still checked; failures are reported as needs-review.
SOFT_BLOCK_CODES = {401, 403, 405, 429}

INLINE_LINK = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")
BARE_URL = re.compile(r"(?<![(<\w])(https?://[^\s<>)\"'`]+)")

CTX = ssl.create_default_context()


def extract(paths: list[Path]) -> dict[str, list[str]]:
    """Map each URL to the files it appears in."""
    found: dict[str, list[str]] = {}
    for path in paths:
        text = path.read_text(encoding="utf-8")
        # Skip fenced code blocks; examples in them are illustrative.
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        urls = set(INLINE_LINK.findall(text))
        for url in BARE_URL.findall(text):
            urls.add(url.rstrip(".,;:"))
        for url in urls:
            found.setdefault(url, []).append(str(path.relative_to(ROOT)))
    return found


def probe(url: str, method: str) -> tuple[int | None, str, str]:
    req = urllib.request.Request(url, method=method, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=45, context=CTX) as resp:
            return resp.status, resp.url, ""
    except urllib.error.HTTPError as exc:
        return exc.code, getattr(exc, "url", url), ""
    except Exception as exc:  # noqa: BLE001 - any transport failure is a failure
        return None, url, f"{type(exc).__name__}: {exc}"


def check(url: str) -> dict:
    status, final, error = None, url, ""
    for attempt in range(2):
        # HEAD first; many servers reject it, so fall back to GET.
        status, final, error = probe(url, "HEAD")
        if status is None or status >= 400:
            status, final, error = probe(url, "GET")
        if status is not None and status < 400:
            break
        if attempt == 0:
            time.sleep(3)

    if status is not None and status < 400:
        state = "ok"
    elif status in SOFT_BLOCK_CODES:
        state = "needs-review"
    else:
        state = "dead"

    return {
        "url": url,
        "status": status if status is not None else "error",
        "final_url": final,
        "error": error,
        "state": state,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="*", default=None)
    args = parser.parse_args()

    if args.files:
        paths = [ROOT / f for f in args.files]
    else:
        paths = sorted(
            p for p in ROOT.glob("*.md")
        ) + sorted(ROOT.glob(".github/*.md"))

    targets = extract([p for p in paths if p.exists()])
    print(f"Checking {len(targets)} unique links across {len(paths)} files.")

    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(check, sorted(targets)))

    for r in results:
        r["files"] = sorted(set(targets[r["url"]]))

    dead = [r for r in results if r["state"] == "dead"]
    review = [r for r in results if r["state"] == "needs-review"]
    checked_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        f"Checked {len(results)} links on {checked_at}.",
        "",
        f"- {len(results) - len(dead) - len(review)} resolved",
        f"- {len(review)} refused an automated client",
        f"- {len(dead)} dead",
        "",
    ]
    if dead:
        lines += ["## Dead links", "", "These returned 404, 410, a server error, or did not resolve at all.", ""]
        for r in dead:
            detail = r["error"] or f"HTTP {r['status']}"
            lines.append(f"- [ ] `{detail}` {r['url']} (in {', '.join(r['files'])})")
        lines.append("")
    if review:
        lines += [
            "## Needs a human check",
            "",
            "These refused an automated client with 401, 403, 405, or 429. That is",
            "usually bot filtering rather than rot, so open each one in a browser",
            "before changing anything.",
            "",
        ]
        for r in review:
            lines.append(f"- [ ] `{r['status']}` {r['url']}")
        lines.append("")

    report = "\n".join(lines)
    (ROOT / "link-report.md").write_text(report, encoding="utf-8")
    (ROOT / "link-results.json").write_text(
        json.dumps({"checked_at": checked_at, "results": results}, indent=2) + "\n",
        encoding="utf-8",
    )
    print(report)
    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
