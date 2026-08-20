# Contributing

Thanks for helping. This list has exactly one thing going for it: every claim in it traces back to the party that operates the crawler or publishes the standard. A wrong user-agent string or a dead link destroys the only reason the list exists, so the bar for an entry is deliberately high.

## The rules

**Link to the primary source.** The entry for a crawler links to the operator's own documentation, not to a blog post summarizing it. The entry for a specification links to the specification. If the only source for a fact is a third-party crawler directory or an SEO agency's article, it does not go in.

**Never transcribe a user-agent string from a third party.** User-agent strings are only accepted when the operator publishes them. If a vendor documents a robots.txt token but not a full user-agent string, write "Not published" in that cell. That is a useful fact, and it is more useful than a plausible-looking string somebody reverse-engineered from access logs.

**Verify the link resolves before opening the pull request.** Open it in a browser. Check that the page actually says what your entry claims it says. Redirects are fine; use the URL you land on, not the one you started with.

**A missing row is fine.** If you cannot verify something, leave it out and say so in the pull request. Gaps get documented in the list itself, as the Grok and xAI section does.

## Format

Entries look like this:

```markdown
- [Name](https://example.com/page) - What it is, in one sentence ending in a period.
```

- Sort entries alphabetically within a section, except in Research Papers and Datasets, which is oldest first.
- Start the description with a capital letter and end it with a period.
- Do not use marketing language. "AI visibility monitoring for ChatGPT and Perplexity" is an entry; "the leading AI visibility platform" is not.
- Every URL may appear only once in the whole README. `awesome-lint` rejects duplicates.
- Run the linter before opening the pull request:

```sh
npx awesome-lint
```

Tables need their pipes aligned or `awesome-lint` will fail. If you edit one, the CI failure will tell you exactly which cells to pad.

## Adding a tool

Tools are listed alphabetically and unranked. Inclusion is not endorsement and there is no ordering to argue about, which is intentional.

To be listed, a tool needs a working public URL and a one-line description of what it does, drawn from its own materials. Open-source projects go in the open-source subsection and need a public repository. Commercial products go in the commercial subsection.

Rankings, benchmarks, and opinions belong in the maintainer's separate opinionated list, not here. Pull requests that reorder the tools section, add superlatives, or argue that one tool is better than another will be closed with a pointer to that list.

## Removing something

Removals are as welcome as additions. Open an issue if:

- A link is dead and has no obvious replacement.
- A user-agent string no longer matches what the vendor documents.
- A tool has been discontinued or its site has gone.
- An entry is a third-party source that slipped past review.

The weekly link check opens issues automatically for rot, but it cannot detect an entry that is merely wrong. That part needs people.

## Disclosure

This list is maintained by [Jared Rhizor](https://github.com/jrhizor), who also maintains [Elmo](https://github.com/elmohq), one of the tools listed in it. Pull requests that add competing tools are welcome and are held to the same standard as everything else. If you think an entry here is slanted, open an issue and say so plainly.
