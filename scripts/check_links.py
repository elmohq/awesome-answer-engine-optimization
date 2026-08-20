#!/usr/bin/env python3
"""Check every link in the Markdown files of this repository.

A dead link in a reference list is worse than a missing row, so this runs
weekly in CI and opens an issue when something rots.

Statuses:
  ok            2xx or a redirect chain ending in 2xx
  needs-review  401, 403, 405, 429, 5xx, timeouts, connection failures - all of
                which a healthy page produces from a CI runner often enough that
                failing the build on them would just train people to ignore it
  dead          404, 410, 451, or a domain that stopped resolving entirely

Only "dead" fails the build. That line is deliberate: this job is worth having
only if a red run means a genuinely broken link, so anything ambiguous is
reported for a human instead of shouting.

Writes link-report.md and link-results.json. Exits 1 if anything is dead.

Usage: python3 scripts/check_links.py [--files README.md ...]
"""

from __future__ import annotations

import argparse
import json
import re
import socket
import ssl
import sys
import time
import urllib.error
import urllib.parse
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

# Definitive rot. Everything else that fails is treated as ambiguous.
DEAD_CODES = {404, 410, 451}

# Hosts known to reject non-browser clients outright, sometimes with a 400.
# Their pages are real; verify them by hand rather than treating them as rot.
SOFT_BLOCK_HOSTS = {
    "developers.facebook.com",
    "www.facebook.com",
    "www.linkedin.com",
    "x.com",
    "twitter.com",
}

IGNORE_FILE = ROOT / "scripts" / "link-ignore.txt"

INLINE_LINK = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")
BARE_URL = re.compile(r"(?<![(<\w])(https?://[^\s<>)\"'`]+)")

CTX = ssl.create_default_context()


def load_ignored() -> set[str]:
    """URLs deliberately excluded from the check, one per line."""
    if not IGNORE_FILE.exists():
        return set()
    return {
        line.strip()
        for line in IGNORE_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    }


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


def probe(url: str, method: str) -> tuple[int | None, str, str, str]:
    """Return (status, final_url, error_text, failure_kind).

    failure_kind is "" on an HTTP response of any code, "dns" when the hostname
    itself stopped resolving, and "transport" for timeouts and connection
    errors, which are usually the network and not the site.
    """
    req = urllib.request.Request(url, method=method, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=45, context=CTX) as resp:
            return resp.status, resp.url, "", ""
    except urllib.error.HTTPError as exc:
        return exc.code, getattr(exc, "url", url), "", ""
    except urllib.error.URLError as exc:
        reason = getattr(exc, "reason", exc)
        kind = "dns" if isinstance(reason, socket.gaierror) else "transport"
        return None, url, f"{type(reason).__name__}: {reason}", kind
    except Exception as exc:  # noqa: BLE001 - any transport failure is ambiguous
        return None, url, f"{type(exc).__name__}: {exc}", "transport"


def check(url: str) -> dict:
    status, final, error, kind = None, url, "", ""
    # Three attempts with backoff. A CI runner sees transient timeouts that a
    # laptop never does, and one flaky request must not condemn a live page.
    for attempt in range(3):
        # HEAD first; many servers reject it, so fall back to GET.
        status, final, error, kind = probe(url, "HEAD")
        if status is None or status >= 400:
            status, final, error, kind = probe(url, "GET")
        if status is not None and status < 400:
            break
        if status in DEAD_CODES:
            break  # Definitive; retrying a 404 just wastes time.
        if attempt < 2:
            time.sleep(5 * (attempt + 1))

    host = urllib.parse.urlparse(url).hostname or ""
    if status is not None and status < 400:
        state = "ok"
    elif status in DEAD_CODES:
        state = "dead"
    elif kind == "dns":
        # The hostname stopped resolving through every attempt: the site is gone.
        state = "dead"
    else:
        # 5xx, timeouts, connection resets, and bot challenges all land here.
        state = "needs-review"

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
    ignored = load_ignored()
    skipped = sorted(set(targets) & ignored)
    for url in skipped:
        del targets[url]
    print(f"Checking {len(targets)} unique links across {len(paths)} files.")
    if skipped:
        print(f"Skipping {len(skipped)} ignored links.")

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
        f"- {len(review)} inconclusive (bot challenge, server error, or timeout)",
        f"- {len(dead)} dead",
        f"- {len(skipped)} skipped by scripts/link-ignore.txt",
        "",
    ]
    if dead:
        lines += [
            "## Dead links",
            "",
            "These returned 404, 410, or 451, or their domain stopped resolving.",
            "Treat them as real rot: fix the URL or delete the entry.",
            "",
        ]
        for r in dead:
            detail = r["error"] or f"HTTP {r['status']}"
            lines.append(f"- [ ] `{detail}` {r['url']} (in {', '.join(r['files'])})")
        lines.append("")
    if review:
        lines += [
            "## Needs a human check",
            "",
            "Bot challenges, server errors, and timeouts. A CI runner gets these",
            "from perfectly healthy pages far more often than a browser does, so",
            "open each one yourself before changing anything. If one persists for",
            "weeks, it is probably real.",
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
