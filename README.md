# Awesome Answer Engine Optimization (AEO) and Generative Engine Optimization (GEO) [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Official documentation, crawler user agents, specifications, research, and tools for Answer Engine Optimization (AEO) and Generative Engine Optimization (GEO) in 2026.

Answer Engine Optimization (AEO) and Generative Engine Optimization (GEO) are the practice of making web content discoverable, retrievable, and citable by answer engines such as ChatGPT, Google AI Overviews and AI Mode, Perplexity, Google Gemini, Claude, Microsoft Copilot, and Grok. The two terms are used interchangeably by most practitioners. Where a distinction is drawn, Answer Engine Optimization (AEO) emphasizes being cited in a direct answer, and Generative Engine Optimization (GEO) emphasizes influencing the generated text itself.

This is a reference index of primary sources, not a ranking and not a tutorial. Where a vendor publishes its own documentation, that documentation is the entry. Third-party blog posts and summaries are excluded, because the whole value of this list is that every claim traces back to the party that operates the crawler. Tools are listed alphabetically and are deliberately unranked.

**Disclosure:** this list is maintained by [Jared Rhizor](https://github.com/jrhizor) and published under the [Elmo](https://github.com/elmohq) GitHub organization. Elmo is an open-source Answer Engine Optimization (AEO) and Generative Engine Optimization (GEO) platform, and it competes with many of the tools listed below. Elmo appears in the Tools section in alphabetical order, with the same one-line treatment as every other tool including its direct competitors. This list is maintained by an interested party, so verify anything that matters to you against the primary source. Every entry links to one.

Every link here resolved when it was added, and a scheduled job rechecks all of them weekly and opens an issue for anything that rots. Facts about crawlers and publisher controls come only from vendor documentation. Where a vendor documents nothing, this list says so instead of guessing.

## Contents

- [Official Engine Documentation](#official-engine-documentation)
  - [ChatGPT and OpenAI](#chatgpt-and-openai)
  - [Google AI Overviews and AI Mode](#google-ai-overviews-and-ai-mode)
  - [Google Gemini](#google-gemini)
  - [Perplexity](#perplexity)
  - [Claude and Anthropic](#claude-and-anthropic)
  - [Microsoft Copilot and Bing](#microsoft-copilot-and-bing)
  - [Grok and xAI](#grok-and-xai)
  - [Other Crawler Operators](#other-crawler-operators)
- [Crawler User Agents](#crawler-user-agents)
  - [Training Crawlers](#training-crawlers)
  - [Search Index Crawlers](#search-index-crawlers)
  - [User-Triggered Fetchers](#user-triggered-fetchers)
  - [Control Tokens Without a Crawler](#control-tokens-without-a-crawler)
  - [Verifying a Crawler Is Genuine](#verifying-a-crawler-is-genuine)
- [Specifications and Standards](#specifications-and-standards)
  - [Robots and Publisher Controls](#robots-and-publisher-controls)
  - [llms.txt](#llmstxt)
  - [Structured Data for Extraction](#structured-data-for-extraction)
  - [Measurement Standards](#measurement-standards)
- [Research Papers and Datasets](#research-papers-and-datasets)
- [Tools](#tools)
  - [Open Source and Self-Hostable](#open-source-and-self-hostable)
  - [Commercial Platforms](#commercial-platforms)
  - [Crawler Control and Bot Analytics](#crawler-control-and-bot-analytics)
- [Analytics and Measurement](#analytics-and-measurement)
  - [Vendor-Reported Visibility](#vendor-reported-visibility)
  - [Referral Traffic Attribution](#referral-traffic-attribution)

## Official Engine Documentation

Vendor-published documentation on crawling, citations, publisher controls, and attribution. Every entry is hosted on a domain the vendor itself controls.

### ChatGPT and OpenAI

- [Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots) - Official reference for every OpenAI crawler, with full user-agent strings, per-bot purposes, and links to IP range files.
- [GPTBot IP Ranges](https://openai.com/gptbot.json) - Machine-readable IP prefixes for the training crawler, for verifying that a request claiming to be GPTBot really is.
- [OAI-SearchBot IP Ranges](https://openai.com/searchbot.json) - Machine-readable IP prefixes for the crawler that builds the ChatGPT search index.
- [ChatGPT-User IP Ranges](https://openai.com/chatgpt-user.json) - Machine-readable IP prefixes for user-initiated fetches made from ChatGPT.
- [OAI-AdsBot IP Ranges](https://openai.com/adsbot.json) - Machine-readable IP prefixes for the crawler that validates advertiser landing pages.
- [Publishers and Developers FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq) - OpenAI's answers on how publisher content is surfaced, cited, and controlled.
- [ChatGPT Search](https://help.openai.com/en/articles/9237897-chatgpt-search) - How ChatGPT decides to search the web and how inline citations are presented to users.
- [Introducing ChatGPT Search](https://openai.com/index/introducing-chatgpt-search/) - Launch announcement describing the citation and attribution model for publishers.
- [Web Search Tool](https://developers.openai.com/api/docs/guides/tools-web-search) - API documentation for the web search tool, including the citation annotation format applications must display.

### Google AI Overviews and AI Mode

- [AI Features and Your Website](https://developers.google.com/search/docs/appearance/ai-features) - Google's statement of how AI Overviews and AI Mode source content, and exactly which preview controls apply to them.
- [Optimizing for Generative AI Features on Google Search](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) - Google's own optimization guide, including its rebuttals of common Answer Engine Optimization (AEO) and Generative Engine Optimization (GEO) claims.
- [A New Resource for Optimizing for Generative AI in Google Search](https://developers.google.com/search/blog/2026/05/a-new-resource-for-optimizing) - Search Central announcement introducing that guide.
- [Top Ways to Ensure Your Content Performs Well in Google's AI Experiences](https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search) - Earlier Search Central guidance that the optimization guide builds on.
- [Google Crawlers and Fetchers Overview](https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers) - Index of every Google crawler, fetcher, and robots.txt product token.
- [Google's Common Crawlers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) - Full user-agent strings for Googlebot, GoogleOther, Google-CloudVertexBot, and the Google-Extended token.
- [Google's Special-Case Crawlers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-special-case-crawlers) - Crawlers that operate for specific products and ignore the global robots.txt user-agent rules.
- [Search Generative AI Control](https://support.google.com/webmasters/answer/16908024) - Search Console setting that opts a site out of generative AI features in Google Search.
- [New Opportunities, Control and Insights for Website Owners](https://blog.google/products-and-platforms/products/search/new-controls-website-owners/) - Google's announcement of that opt-out control and the reporting that accompanies it.
- [AI Mode in Google Search](https://blog.google/products-and-platforms/products/search/ai-mode-search/) - Product announcement describing what AI Mode is and how it links out.

### Google Gemini

- [An Update on Web Publisher Controls](https://blog.google/innovation-and-ai/products/an-update-on-web-publisher-controls/) - Google's introduction of Google-Extended and a statement of which products it governs.
- [Grounding with Google Search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-search) - How Gemini grounds answers in Google Search results and returns grounding metadata and citations.
- [Grounding Overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/overview) - The grounding sources available to Gemini and how each attributes its sources.
- [GroundingMetadata Reference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/GroundingMetadata) - Exact response schema for grounding chunks and supports, which is what a citation is made of.

### Perplexity

- [Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers) - Official reference for PerplexityBot and Perplexity-User, with full user-agent strings and IP range files.
- [PerplexityBot IP Ranges](https://www.perplexity.ai/perplexitybot.json) - Machine-readable IP prefixes for the indexing crawler.
- [Perplexity-User IP Ranges](https://www.perplexity.ai/perplexity-user.json) - Machine-readable IP prefixes for user-initiated fetches.
- [Introducing the Perplexity Publishers' Program](https://www.perplexity.ai/hub/blog/introducing-the-perplexity-publishers-program) - The revenue-share and analytics program for publishers whose content is cited.
- [Understanding Source Labels](https://www.perplexity.ai/help-center/en/articles/20260806-understanding-source-labels) - How Perplexity labels and ranks the sources it cites in an answer.

### Claude and Anthropic

- [Does Anthropic Crawl Data From the Web, and How Can Site Owners Block the Crawler?](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) - The single official source for ClaudeBot, Claude-User, and Claude-SearchBot, and what blocking each one does.

### Microsoft Copilot and Bing

- [Which Crawlers Does Bing Use?](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0) - Bing's own list of the crawlers behind Bing search and Microsoft Copilot.
- [Announcing User-Agent Change for Bing Crawler Bingbot](https://blogs.bing.com/webmaster/april-2022/Announcing-user-agent-change-for-Bing-crawler-bingbot) - The announcement that carries the current bingbot user-agent strings verbatim.
- [Announcing New Options for Webmasters to Control Usage of Their Content in Bing Chat](https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat) - The `NOCACHE` and `NOARCHIVE` controls that govern whether Copilot may quote and link a page.
- [Bing Introduces Support for the data-nosnippet HTML Attribute](https://blogs.bing.com/webmaster/October-2025/Bing-Introduces-Support-for-the-data-nosnippet-HTML-Attribute) - Element-level control over which parts of a page Bing may show.
- [Introducing AI Performance in Bing Webmaster Tools](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview) - Launch announcement, and the definition of grounding queries and citations as Microsoft measures them.
- [New AI Visibility Insights in Bing Webmaster Tools](https://blogs.bing.com/search/June-2026/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare) - The expansion that added intents, topics, citation share, and competitive comparison.

### Grok and xAI

xAI publishes no crawler documentation. There is no vendor page listing Grok's user agents, no robots.txt guidance, and no published IP ranges, so this list has no entry to give you. Third-party crawler directories publish conflicting strings for xAI; because none of them is the operator, none is cited here. If xAI publishes documentation, [open an issue](https://github.com/elmohq/awesome-answer-engine-optimization/issues) and it will be added.

- [xAI Documentation](https://docs.x.ai/overview) - xAI's developer documentation, listed so you can confirm for yourself that it covers the API and not crawling or publisher controls.

### Other Crawler Operators

Not answer engines in their own right, but they crawl for AI systems and show up in the same access logs.

- [About Applebot](https://support.apple.com/en-us/119829) - Applebot user-agent formats plus Applebot-Extended, Apple's robots.txt opt-out for generative model training.
- [Amazonbot](https://developer.amazon.com/amazonbot) - Amazonbot's user-agent string and Amazon's statement that crawled data may train Amazon AI models.
- [Mistral Crawlers](https://docs.mistral.ai/robots) - One of the few vendors that separates training, indexing, and user-triggered fetching into three distinct user agents.
- [DuckAssistBot](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot) - DuckDuckGo's real-time fetcher for AI-assisted answers, with an explicit statement that it does not train models.
- [Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers) - Meta's list of crawler user agents, separating the training and indexing crawler from the user-request fetcher.
- [CCBot](https://commoncrawl.org/ccbot) - The Common Crawl crawler, whose archives are an input to many model training pipelines.

## Crawler User Agents

Every string below is quoted from the operator's own documentation linked in the section above. Where a vendor publishes only a robots.txt token and not a full user-agent string, that is stated rather than filled in from a third-party directory. Version numbers change without notice, so match on the token, never on the whole string.

The distinction that matters for Answer Engine Optimization (AEO) is the one between crawlers that build a corpus and fetchers that act for a user in real time. Blocking the first affects whether a model knows about you at all. Blocking the second affects whether you can be cited in an answer being generated right now. Several vendors state that user-triggered fetchers do not follow robots.txt.

### Training Crawlers

Collect content that may be used to train foundation models.

| Operator     | robots.txt token     | Full user-agent string as documented                                                                                      |
| ------------ | -------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | `GPTBot`             | `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.4; +https://openai.com/gptbot`                  |
| Anthropic    | `ClaudeBot`          | Not published                                                                                                             |
| Apple        | `Applebot-Extended`  | Control token only; see below                                                                                             |
| Amazon       | `Amazonbot`          | `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amazonbot/0.1) Chrome/W.X.Y.Z Safari/537.36`              |
| Mistral      | `MistralAI-Training` | `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; MistralAI-Training/1.0; +https://docs.mistral.ai/robots)` |
| Meta         | `meta-externalagent` | `meta-externalagent/1.1 (+/documentation/sharing/webmasters/web-crawlers)`                                                |
| Common Crawl | `CCBot`              | `CCBot/2.0`                                                                                                               |

### Search Index Crawlers

Build the retrieval index an answer engine draws on. These are the crawlers that determine whether you are eligible to be cited at all.

| Operator   | robots.txt token   | Full user-agent string as documented                                                                                                                                                  |
| ---------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI     | `OAI-SearchBot`    | `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.4; +https://openai.com/searchbot` |
| Perplexity | `PerplexityBot`    | `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)`                                                             |
| Anthropic  | `Claude-SearchBot` | Not published                                                                                                                                                                         |
| Google     | `Googlebot`        | `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/W.X.Y.Z Safari/537.36`                                         |
| Microsoft  | `bingbot`          | `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) Chrome/W.X.Y.Z Safari/537.36 Edg/W.X.Y.Z`                              |
| Mistral    | `MistralAI-Index`  | `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; MistralAI-Index/1.0; +https://docs.mistral.ai/robots)`                                                                |

Google's position is that "AI is built into Search and integral to how Search functions, which is why robots.txt directives for Googlebot is the control for site owners to manage access to how their sites are crawled for Search." There is no separate AI Overviews or AI Mode crawler to allow or block. Perplexity states that PerplexityBot is used to surface and link sites in Perplexity search results and is not used to crawl content for AI foundation models.

### User-Triggered Fetchers

Fetch a page in real time because a user asked a question right now. Several operators document that these fetchers do not honor robots.txt, because the request originates from a person rather than from an automated crawl.

| Operator   | robots.txt token       | Full user-agent string as documented                                                                                          |
| ---------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| OpenAI     | `ChatGPT-User`         | `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot`                   |
| Perplexity | `Perplexity-User`      | `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user)` |
| Anthropic  | `Claude-User`          | Not published                                                                                                                 |
| Mistral    | `MistralAI-User`       | `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; MistralAI-User/1.0; +https://docs.mistral.ai/robots)`         |
| DuckDuckGo | `DuckAssistBot`        | `DuckAssistBot/1.2; (+http://duckduckgo.com/duckassistbot.html)`                                                              |
| Meta       | `meta-externalfetcher` | `meta-externalfetcher/1.1 (+/documentation/sharing/webmasters/web-crawlers)`                                                  |

Perplexity documents that Perplexity-User generally ignores robots.txt rules because the fetch is user-initiated. Meta documents that meta-externalfetcher may bypass robots.txt for the same reason.

### Control Tokens Without a Crawler

These appear in robots.txt but never in an access log. They are opt-out switches, not user agents, and blocking them has no effect on search crawling.

| Token               | Operator | What disallowing it does, per the vendor                                                                                                                                          |
| ------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Google-Extended`   | Google   | Excludes the site from helping improve Gemini Apps and Vertex AI generative APIs. Google documents it as a standalone product token that uses existing Google user-agent strings. |
| `Applebot-Extended` | Apple    | Excludes the site's content from training Apple foundation models, without affecting Applebot's search crawling.                                                                  |

Google-Extended does not control AI Overviews or AI Mode. Google's AI features documentation points to `nosnippet`, `data-nosnippet`, `max-snippet`, and `noindex` for those, and Search Console carries a separate opt-out for generative AI features in Search.

### Verifying a Crawler Is Genuine

User-agent strings are trivially spoofed, so treat the string as a claim and verify it.

- [Verify Google Crawler Requests](https://developers.google.com/crawling/docs/crawlers-fetchers/verify-google-requests) - Reverse-DNS and IP-range verification for Google's crawlers and fetchers.
- [How to Verify Bingbot](https://www.bing.com/webmasters/help/how-to-verify-bingbot-3905dc26) - Reverse-DNS verification for Microsoft's crawler.

OpenAI and Perplexity both take the IP-range approach instead: each publishes a JSON file of the prefixes its bots crawl from, linked in their sections above. Match the requesting address against that file rather than trusting the user-agent header.

## Specifications and Standards

### Robots and Publisher Controls

- [RFC 9309: Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309) - The robots.txt standard itself, which every AI crawler control is layered on top of.
- [How Google Interprets the robots.txt Specification](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec) - The most detailed public description of real-world robots.txt parsing, including token matching and precedence.
- [Robots Meta Tags Specifications](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag) - The snippet-level controls that determine how much of a page an answer engine may quote.
- [IETF AI Preferences Working Group](https://datatracker.ietf.org/wg/aipref/about/) - The standards effort to replace today's incompatible per-vendor tokens with one vocabulary.
- [A Vocabulary for Expressing AI Usage Preferences](https://datatracker.ietf.org/doc/draft-ietf-aipref-vocab/) - The draft vocabulary of preference terms.
- [Attaching AI Preferences to Content](https://datatracker.ietf.org/doc/draft-ietf-aipref-attach/) - The companion draft for expressing those preferences in robots.txt and HTTP headers.
- [ai.robots.txt](https://github.com/ai-robots-txt/ai.robots.txt) - Community-maintained robots.txt blocklist of known AI crawler tokens, updated as vendors add agents.

### llms.txt

- [The llms.txt Proposal](https://llmstxt.org/) - Jeremy Howard's proposal for a Markdown file that gives models a curated map of a site. It is a community convention, not a standard, and no engine documented in this list commits to reading it.
- [llms-txt Repository](https://github.com/AnswerDotAI/llms-txt) - The reference implementation and specification source.
- [llms.txt Directory](https://directory.llmstxt.cloud/) - Directory of sites that publish an llms.txt file.
- [llms.txt Site Index](https://llmstxt.site/) - A second index of published llms.txt files, useful for seeing real-world formatting in practice.

Weigh the effort against what the engines say. Google's optimization guide addresses llms.txt by name and states that you do not need to create new machine-readable files, AI text files, markup, or Markdown to appear in Google Search including its generative AI capabilities, "as Google Search itself doesn't use them." No other engine in this list documents reading llms.txt either. That does not make publishing one harmful; it does mean nobody has documented a benefit.

### Structured Data for Extraction

Google's guidance is explicit that no special structured data is required for AI features. Structured data still earns rich results in classic search, still disambiguates entities, and is still the cheapest way to state facts unambiguously, which is why these types stay on the list.

- [Introduction to Structured Data Markup](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) - How search systems consume schema.org markup and which formats are accepted.
- [schema.org/Organization](https://schema.org/Organization) - Entity identity: names, logos, `sameAs` links, and the disambiguation an engine needs to know who you are.
- [schema.org/Article](https://schema.org/Article) - Authorship, publication date, and publisher, the provenance fields that citation-bearing answers lean on.
- [schema.org/FAQPage](https://schema.org/FAQPage) - Explicit question-and-answer pairs, the structure that most closely matches how an answer engine chunks a page.
- [schema.org/QAPage](https://schema.org/QAPage) - A single user-submitted question with answers, distinct from `FAQPage`.
- [schema.org/HowTo](https://schema.org/HowTo) - Ordered steps with tools and materials, for procedural answers.
- [schema.org/Product](https://schema.org/Product) - Product identity, offers, and reviews, the fields commercial answers are assembled from.
- [schema.org/Dataset](https://schema.org/Dataset) - Dataset descriptions, licensing, and distribution.
- [schema.org/BreadcrumbList](https://schema.org/BreadcrumbList) - Page position within a site, which supplies hierarchy an extractor would otherwise have to infer.

### Measurement Standards

- [IAB: Measuring Visibility in the AI Era](https://www.iab.com/guidelines/measuring-visibility-in-the-ai-era/) - The industry framework for measuring brand and publisher visibility in AI-powered discovery, published August 2026. It defines a common metrics hierarchy called the four P's, distinguishes decision-grade from directional measurement, and sets disclosure requirements for vendors. It is the closest thing this field has to an agreed vocabulary.

## Research Papers and Datasets

Peer-reviewed and preprint work, oldest first. Vendor benchmarks and agency studies are excluded.

- [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735) - Aggarwal et al., 2023, accepted to KDD 2024. The paper that named Generative Engine Optimization (GEO) and the origin of most of the field's vocabulary.
- [Evaluating Verifiability in Generative Search Engines](https://arxiv.org/abs/2304.09848) - Liu, Zhang, and Liang, 2023. Human evaluation of whether generative search engine citations actually support the sentences they are attached to.
- [CC-GSEO-Bench: A Content-Centric Benchmark for Measuring Source Influence in Generative Search Engines](https://arxiv.org/abs/2509.05607) - Chen et al., 2025. A benchmark for measuring how much an individual source shapes a generated answer.
- [Quantifying Uncertainty in AI Visibility: A Statistical Framework for Generative Search Measurement](https://arxiv.org/abs/2603.08924) - Sielinski, 2026. Treats answer-engine visibility as a sampling problem, which is the right frame for anyone reading a visibility dashboard.
- [From Citation Selection to Citation Absorption: A Measurement Framework for Generative Engine Optimization Across AI Search Platforms](https://arxiv.org/abs/2604.25707) - Zhang, He, and Yao, 2026. Separates being cited from actually influencing the answer text, and measures both across platforms.
- [Generative Engine Optimization at Scale: Measuring Brand Visibility Across AI Search Engines](https://arxiv.org/abs/2606.20065) - Kumar, 2026. A large-scale measurement of brand visibility across engines.
- [Optimizing Visibility in Generative Engines: A Critical Survey of Generative Engine Optimization, 2023-2026](https://arxiv.org/abs/2607.14035) - Martinez, 2026. A survey of the field to date and the best single starting point for the literature.

## Tools

Listed alphabetically within each subsection and deliberately unranked. Inclusion is not endorsement, and no entry here has been benchmarked by this list. Descriptions are drawn from each project's own materials. For an opinionated ranking of the same field, this list's maintainer keeps a separate, clearly partisan one at [answer-engine-optimization-tools-ranked](https://github.com/jrhizor/answer-engine-optimization-tools-ranked).

### Open Source and Self-Hostable

- [aeo-radar](https://github.com/hellowalt/aeo-radar) - Answer Engine Optimization monitor for tracking brand visibility across answer engines.
- [ansvisor](https://github.com/ansvisor/ansvisor) - AI visibility platform tracking citations, prompts, competitors, and content opportunities, self-hosted or managed.
- [aperture](https://github.com/anyin-ai/aperture) - AI visibility monitoring and analytics for tracking how a brand appears in answer engines.
- [canonry](https://github.com/Canonry/canonry) - Self-hosted Answer Engine Optimization (AEO) stack for tracking ChatGPT, Claude, Gemini, and Perplexity.
- [Elmo](https://github.com/elmohq/elmo) - Answer Engine Optimization (AEO) and Generative Engine Optimization (GEO) platform tracking how answer engines mention, cite, and describe a brand. Maintained by this list's maintainer.
- [gego](https://github.com/AI2HU/gego) - Generative Engine Optimization (GEO) tracking for a brand across multiple large language models.
- [geo-aeo-tracker](https://github.com/danishashko/geo-aeo-tracker) - Local-first AI visibility dashboard tracking a brand across six AI models.
- [geo-lint](https://github.com/IJONIS/geo-lint) - Linter applying Generative Engine Optimization (GEO), SEO, and content quality rules to pages.
- [GEORank](https://github.com/yaojingang/GEORank) - Generative Engine Optimization (GEO) ranking and optimization platform.
- [geolook](https://github.com/aigclink/geolook) - End-to-end Generative Engine Optimization (GEO) implementation covering analysis, diagnosis, and strategy.
- [GetCito](https://github.com/ai-search-guru/getcito-worlds-first-open-source-aio-aeo-or-geo-tool) - Brand and competitor benchmarking across multiple AI answer surfaces.
- [oneglanse](https://github.com/aryamantodkar/oneglanse) - Free Generative Engine Optimization (GEO) tracker for monitoring brand appearance in answer engines.
- [searchstack-aeo](https://github.com/alexpospekhov/searchstack-aeo) - Answer Engine Optimization (AEO), Generative Engine Optimization (GEO), and SEO stack aimed at small teams.

### Commercial Platforms

- [Ahrefs Brand Radar](https://ahrefs.com/brand-radar) - AI visibility measurement across six AI tools, built on Ahrefs' search-backed prompt data.
- [AthenaHQ](https://athenahq.ai/) - Answer Engine Optimization (AEO) and Generative Engine Optimization (GEO) platform for commercial and enterprise brands.
- [Authoritas](https://www.authoritas.com/) - SEO platform with AI search visibility tracking alongside classic rank tracking.
- [Botify](https://www.botify.com/) - AI search optimization platform focused on large-site crawling and indexing.
- [Brandlight](https://www.brandlight.ai/) - AI visibility platform aimed at enterprise brands.
- [BrightEdge](https://www.brightedge.com/) - Enterprise SEO and AI search platform covering Google Search, AI Overviews, and ChatGPT.
- [Conductor](https://www.conductor.com/) - Enterprise Answer Engine Optimization (AEO) and SEO intelligence with website monitoring and agents.
- [Evertune](https://www.evertune.ai/) - AI brand monitoring focused on how models represent a brand across the customer journey.
- [Goodie](https://higoodie.com/) - AI search visibility and Answer Engine Optimization (AEO) platform for monitoring and optimizing brand presence.
- [HubSpot AI Search Grader](https://www.hubspot.com/ai-search-grader) - Free one-time check of how ChatGPT, Perplexity, and Gemini describe a brand.
- [Knowatoa](https://knowatoa.com/) - AI search visibility tracking oriented toward recovering traffic lost to answer engines.
- [LLMrefs](https://llmrefs.com/) - Brand visibility, rank, and citation tracking across generative answer engines.
- [Nightwatch](https://nightwatch.io/) - Rank tracker unifying classic search positions with AI visibility in ChatGPT, Claude, Gemini, and Perplexity.
- [Otterly.AI](https://otterly.ai/) - AI search monitoring for ChatGPT, Perplexity, and Google AI Overviews.
- [Peec AI](https://peec.ai/) - AI search analytics for marketing teams, benchmarking brand performance against competitors.
- [Profound](https://www.tryprofound.com/) - Brand visibility measurement and optimization for answer engines.
- [Rankscale](https://rankscale.ai/) - AI visibility and ranking tracker across ChatGPT, Perplexity, Gemini, and Google AI Overviews.
- [Relixir](https://www.relixir.ai/rex) - Generative Engine Optimization (GEO) monitoring paired with automated content generation and deployment.
- [Scrunch AI](https://scrunch.com/) - AI search visibility monitoring, site optimization, and content delivery to AI agents.
- [SE Ranking AI Visibility Tool](https://seranking.com/ai-visibility-tracker.html) - Brand mention and link tracking in AI answers, with competitor comparison.
- [Semrush Enterprise](https://enterprise.semrush.com/) - Enterprise SEO and AI search platform.
- [seoClarity](https://www.seoclarity.net/) - Unified SEO and Answer Engine Optimization (AEO) platform for enterprise teams.
- [Similarweb](https://www.similarweb.com/) - Digital market intelligence, including traffic measurement for AI assistant referrals.
- [Superlines](https://superlines.io/) - AI search intelligence for brands and agencies.
- [Trakkr](https://trakkr.ai/) - Citation, perception, and competitor tracking across ChatGPT, Claude, and Gemini.
- [XFunnel](https://www.xfunnel.ai/) - Citation tracking and question discovery across AI search platforms.
- [Yext Scout](https://www.yext.com/platform/scout) - AI search visibility agent scanning multiple models with competitor comparison.
- [ZipTie.dev](https://ziptie.dev/) - Tracker for Google AI Overviews, ChatGPT, and Perplexity.
- [daydream](https://www.withdaydream.com/) - Full-service organic search combining SEO agents with human experts.

### Crawler Control and Bot Analytics

- [Cloudflare AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/) - Monitoring and control of how AI services access a site, at the network edge rather than by robots.txt convention.
- [Known Agents](https://knownagents.com/) - Directory and analytics for AI agents and bots, formerly Dark Visitors.
- [Known Agents Directory](https://knownagents.com/agents) - Continuously updated catalog of AI crawler user agents and their operators.

## Analytics and Measurement

Where each engine's activity actually shows up. Two different things get measured and they are easy to confuse: whether you were *cited* inside an answer, and whether a person *clicked through* to your site. Vendor consoles report the first. Your own analytics report the second, and only for the fraction of answers that produce a click at all.

### Vendor-Reported Visibility

- [Generative AI Performance Report for Search](https://support.google.com/webmasters/answer/16984139) - Search Console impressions for AI Overviews and AI Mode, broken down by page, country, device, and date.
- [Generative AI Performance Report for Discover](https://support.google.com/webmasters/answer/16983858) - The equivalent report for generative AI features in Google Discover.
- [Introducing Search Generative AI Performance Reports](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports) - Google's announcement of those reports and what the metrics do and do not include.
- [Bing Webmaster Tools AI Performance](https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c) - Citation counts, page-level performance, and the grounding queries Copilot generated internally to find your content.

Google reports impressions in generative AI features. Microsoft reports citations and grounding queries, and since June 2026 also intent labels, topic groups, and citation share; both Microsoft announcements are linked in the Copilot section above. Impressions and citations are not the same metric and should not be summed.

Neither Perplexity, OpenAI, Anthropic, nor xAI operates a public webmaster console reporting citations back to site owners. For those engines, referral traffic and third-party trackers are all there is.

### Referral Traffic Attribution

- [GA4 Default Channel Group](https://support.google.com/analytics/answer/9756891) - Google Analytics documents an `AI Assistants` channel for arrivals from sources like ChatGPT, Gemini, Copilot, and Grok, assigned when the medium is `ai-assistant` or the referrer matches Google's list of AI assistants. Google notes this channel excludes AI Overviews and AI Mode, which are reported as ordinary organic search.
- [Custom Channel Groups](https://support.google.com/analytics/answer/13051316) - How to build your own grouping if you need engines split individually rather than pooled.

Referral analytics only ever sees the answers that produced a click. To see the fetches that produced none, you need the server-side view from an edge tool such as Cloudflare AI Crawl Control, listed under Tools above.

Clicks from an answer engine arrive as ordinary referral traffic with that engine's hostname as the referrer. No vendor in this list publishes a specification of its referrer strings, so any fixed list of them is an observation rather than documentation, and this list does not publish one. Read the referrer hostnames out of your own logs and confirm them against your own traffic before hard-coding them into a report.

## Contributing

Contributions are welcome. Read the [contribution guidelines](contributing.md) first: every entry must link to a primary source, and no user-agent string is accepted unless the operator publishes it. See also the [code of conduct](code-of-conduct.md).
