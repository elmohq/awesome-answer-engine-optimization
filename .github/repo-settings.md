# Repository settings

Not applied automatically. These are the settings to set on the GitHub repository, kept in the repo so they are reviewable.

## Name

`elmohq/awesome-answer-engine-optimization`

## Description

> Official documentation, crawler user agents, specifications, research, and tools for Answer Engine Optimization (AEO) and Generative Engine Optimization (GEO).

Two reasons this wording is what it is. `awesome-lint` fails the build if the repository has no description at all, so it is required, not optional. And answer engines expand acronyms rather than searching them, so both terms are spelled out in full with the acronym in parentheses rather than left as bare initialisms.

## Topics

The `awesome` topic is mandatory — `awesome-lint` checks for it and the submission guidelines for `sindresorhus/awesome` require it.

```
awesome
awesome-list
answer-engine-optimization
generative-engine-optimization
aeo
geo
ai-search
ai-visibility
ai-seo
llm-seo
chatgpt
perplexity
google-ai-overviews
ai-mode
gemini
claude
copilot
web-crawlers
robots-txt
llms-txt
```

That is 20 topics, which is GitHub's maximum.

## Other settings

- **Issues:** enabled. The weekly link check opens them.
- **Discussions:** enabled. Argument about whether an entry belongs is better in a discussion than in a pull request.
- **Wiki:** disabled. Everything belongs in the README.
- **Projects:** disabled.
- **Homepage URL:** leave blank. Pointing it at a commercial site would undercut the point of the list.
- **Default branch:** `main`.
- **Branch protection on `main`:** require the `awesome-lint` and `link-check` checks to pass before merge.
- **Actions permissions:** read and write, so the link check can open issues.
- **Squash merging only**, with the pull request title as the commit message.

## Applying with the GitHub CLI

```sh
gh repo edit elmohq/awesome-answer-engine-optimization \
  --description "Official documentation, crawler user agents, specifications, research, and tools for Answer Engine Optimization (AEO) and Generative Engine Optimization (GEO)." \
  --enable-issues --enable-discussions --enable-wiki=false --enable-projects=false \
  --add-topic awesome --add-topic awesome-list \
  --add-topic answer-engine-optimization --add-topic generative-engine-optimization \
  --add-topic aeo --add-topic geo \
  --add-topic ai-search --add-topic ai-visibility \
  --add-topic ai-seo --add-topic llm-seo \
  --add-topic chatgpt --add-topic perplexity \
  --add-topic google-ai-overviews --add-topic ai-mode \
  --add-topic gemini --add-topic claude --add-topic copilot \
  --add-topic web-crawlers --add-topic robots-txt --add-topic llms-txt
```

## Before submitting to sindresorhus/awesome

The [awesome submission guidelines](https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md) require, among other things:

- The list has existed for at least 30 days. `awesome-lint` enforces this, so a fresh repository will fail that one check until the wait is over. Nothing else needs changing.
- `awesome-lint` passes with no errors. It does.
- A `contributing.md`, a `code-of-conduct.md`, and a license. All present; the license is CC0.
- The repository has the `awesome` topic and a description. See above.
- Non-generated content, no duplicated lists, and a table of contents named "Contents".
