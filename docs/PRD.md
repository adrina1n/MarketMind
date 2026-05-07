# MarketMind — Product Requirements Document

## Problem Statement

Les consultants en strategie (type KPMG, Deloitte) passent des heures a preparer des etudes de marche pour leurs propositions commerciales. Le travail est repetitif : chercher des donnees sur la taille du marche, les tendances, les concurrents, les M&A, les chiffres du client... a travers des dizaines de sources web, puis synthetiser le tout dans un document structure. Ce processus manuel est lent, sujet aux erreurs d'omission, et ne capitalise pas sur les recherches precedentes.

## Solution

MarketMind automatise la generation d'etudes de marche. L'utilisateur saisit 3 variables (client, secteur, geographie) et recoit un rapport structure en Markdown avec 11 sections sourcees, chacune accompagnee d'un score de confiance. Le systeme combine recherche web temps reel et base de connaissances personnalisable (RAG) pour produire des rapports fiables et reproductibles.

## User Stories

1. As a consultant, I want to enter a client name, sector, and geography, so that I can generate a market study without manual research.
2. As a consultant, I want to see the market size (value and volume) for a given sector and geography, so that I can quantify the opportunity.
3. As a consultant, I want to see market trends for a sector, so that I can identify growth drivers and headwinds.
4. As a consultant, I want to see macroeconomic factors affecting a sector, so that I can assess the broader context.
5. As a consultant, I want to see a list of competitors with market shares, so that I can map the competitive landscape.
6. As a consultant, I want to see market segmentation, so that I can identify the most relevant sub-segments.
7. As a consultant, I want to see recent M&A activity in a sector, so that I can understand consolidation dynamics.
8. As a consultant, I want to see the client's key financial figures, so that I can assess their current position.
9. As a consultant, I want to see the client's main business activities, so that I can understand their scope.
10. As a consultant, I want to see the client's position in the value chain, so that I can identify upstream/downstream dependencies.
11. As a consultant, I want to see the client's recent strategic operations, so that I can track their recent moves.
12. As a consultant, I want to see the client's future challenges and risks, so that I can anticipate threats.
13. As a consultant, I want every piece of information to cite its source, so that I can verify claims and build trust with my own clients.
14. As a consultant, I want a confidence score on each data point, so that I can prioritize which facts to double-check.
15. As a consultant, I want the system to tell me when information is unavailable, so that I know the gaps rather than getting fabricated data.
16. As a consultant, I want the system to detect ambiguities (e.g. "Orange" could be telecom or fruit), so that the report targets the right entity.
17. As a consultant, I want to choose between disambiguation options when the system detects ambiguity, so that I stay in control.
18. As a consultant, I want to upload my own documents (PDF, Word, Excel) to enrich the knowledge base, so that internal data appears in future reports.
19. As a consultant, I want to paste text or URLs to add to the knowledge base, so that I can quickly feed ad-hoc sources.
20. As a consultant, I want uploaded documents to be treated as high-confidence sources, so that internal data is prioritized.
21. As a consultant, I want to see loading progress while the report generates, so that I know the system is working.
22. As a consultant, I want sections to appear progressively as they complete, so that I can start reading before the full report is done.
23. As a consultant, I want to download the final report as a .md file, so that I can import it into my deliverables.
24. As a consultant, I want the full report generated in under 60 seconds, so that the tool fits into my workflow.
25. As a consultant, I want clear error messages when an API times out or hits a rate limit, so that I understand what happened and can retry.

## Implementation Decisions

### Deep Modules

The system is built around 8 deep modules with simple interfaces hiding significant internal complexity:

1. **LLM Gateway** — Single `complete(prompt, model?) -> str` interface wrapping Gemini 2.5 Flash (primary) and Mistral Small (fallback). Handles retry logic, rate limiting, model switching, and prompt formatting internally. Zero-budget constraint: uses free tiers only.

2. **Web Search** — `search(query, category) -> list[SourcedResult]` interface. Orchestrates Tavily (primary) and Serper (complement) internally. Expands query templates per category, deduplicates results, and extracts source metadata. Adding a new search provider = implementing one adapter.

3. **Synthesizer** — `synthesize(results, category) -> ReportSection` interface. Selects the right prompt per category, formats results for the LLM, injects citations into the Markdown output. Each category is a "plugin" (prompt template + query templates). Adding a category = adding one config file, zero changes to the synthesizer interface.

4. **Category Registry** — Plugin system for the 11 report categories. Each category defines its search query templates and synthesis prompt. The registry discovers categories automatically. This is the key extensibility point.

5. **Pipeline Orchestrator** — `generate_study(client, sector, geography) -> StudyReport`. Runs all registered categories through search + synthesize in parallel via asyncio. Assembles sections into a final structured report.

6. **Confidence Scorer** — Heuristic scoring with two signals: domain trustworthiness (curated list: Statista, Reuters, Bloomberg = high) and multi-source convergence (same fact from multiple sources = bonus). Outputs a badge (high/medium/low) per data point.

7. **RAG Store** — ChromaDB wrapper in embedded mode. Handles document ingestion (PDF/Word/Excel parsing + chunking), embedding (sentence-transformers or Mistral), and similarity search. Integrated into the Web Search module: search() queries both web APIs and ChromaDB, merging results.

8. **Disambiguator** — `disambiguate(client, sector, geography) -> Clarification | None`. Performs a quick pre-search (1-2 queries) to validate the client entity. Detects homonyms, unclear sectors, subsidiary vs. group ambiguities. Returns clarification options or None if unambiguous.

### Architecture Principles

- **Deep modules over shallow wrappers**: each module hides significant complexity behind a minimal interface. The interface surface area should be much smaller than the implementation.
- **Category = plugin**: the system is designed so that adding a new report category (e.g. "ESG factors") requires adding one config/prompt file and zero changes to the search, synthesis, or pipeline code.
- **Asyncio parallelism**: all 11 categories run their search+synthesis in parallel. The pipeline orchestrator uses `asyncio.gather()`.
- **No build step for frontend**: Jinja2 templates + TailwindCSS via CDN + HTMX for interactivity. FastAPI serves everything.
- **Mono-user, no auth**: simplifies the MVP. No sessions, no user management.

### Data Flow

```
Form (client, sector, geo)
  -> Disambiguator (pre-search)
    -> [Clarification UI if ambiguous]
  -> Pipeline Orchestrator
    -> For each category (in parallel):
      -> Category Registry (get query templates + prompt)
      -> Web Search (Tavily + Serper + RAG)
      -> Confidence Scorer (score each result)
      -> Synthesizer (LLM -> ReportSection)
    -> Assemble StudyReport
  -> Render Markdown in frontend (progressive, via HTMX)
```

### Key Data Models

- **SourcedResult**: a piece of raw data with its source URL, domain, and retrieval metadata
- **ReportSection**: a Markdown-formatted section with inline citations and per-fact confidence scores
- **StudyReport**: ordered collection of ReportSections + metadata (timestamp, inputs, generation time)
- **Clarification**: list of disambiguation options with labels and context

### Delivery Plan (Vertical Slices)

| # | Slice | Issues | Verifiable By |
|---|-------|--------|---------------|
| 1 | Setup + Hello World | #1 (CLOSED) | App starts, form displayed |
| 2 | Deep interfaces + Market Size E2E | #2 | "L'Oreal / Cosmetique / Europe" -> market size section with sources |
| 3 | Trends + Macro | #3 | 3 sections in report |
| 4 | Competitors + Segmentation + M&A | #4 | 6 sections in report |
| 5 | Client categories (5 modules) | #5 | Full 11-section report |
| 6 | Confidence scoring + missing data | #6 | Confidence badges visible, "unavailable" messages |
| 7 | Pre-search + disambiguation | #7 | "Orange" -> clarification prompt |
| 8 | RAG: ChromaDB + document upload | #8 | Uploaded PDF content appears in results |
| 9 | Polish: parallelization, UX, export | #9 | Full study < 60s, download button works |

## Testing Decisions

### Philosophy

Tests verify **external behavior through the module's public interface**, not implementation details. A test should break only when the module's contract changes, not when internals are refactored.

### Modules Under Test

The 3 foundational interfaces are tested in isolation:

1. **LLM Gateway** — Test that `complete()` returns a non-empty string for a valid prompt. Test fallback behavior: when the primary model fails, the fallback is used. Test retry on transient errors. Use dependency injection to swap real API calls for recorded responses in CI.

2. **Web Search** — Test that `search()` returns a list of `SourcedResult` with valid URLs and non-empty content. Test query template expansion per category. Test deduplication (same URL from Tavily and Serper = one result). Use recorded API responses for deterministic tests.

3. **Synthesizer** — Test that `synthesize()` returns a `ReportSection` with valid Markdown and at least one citation. Test that different categories produce different prompt structures. Use a fake LLM Gateway (returns canned responses) to test in isolation.

### Test Infrastructure

- pytest as the test runner
- Recorded API responses (cassettes or fixtures) for deterministic, offline testing
- Fake/stub implementations of external dependencies (LLM, search APIs) injected via constructor parameters
- No mocking of internal implementation details

## Out of Scope

- Authentication and multi-user support
- Automatic PowerPoint export
- Multi-agent architecture (prepared for, but not implemented in MVP)
- PDF or Word export (Markdown only)
- SSO or team management
- Search history or saved reports
- Custom report templates (fixed 11-section structure)
- Real-time collaboration
- Billing or usage tracking
- Mobile-responsive design (desktop-first)

## Further Notes

- **Zero-budget constraint**: all external services (Gemini, Tavily, Serper, Mistral) must use free tiers. The system must handle rate limits gracefully.
- **Language**: the UI and reports are in French. Code and documentation are in English (or unaccented French where practical).
- **Deployment**: local development with `uvicorn`. Cloud demo via Render or Railway with Docker. No production deployment planned for MVP.
- **Future evolution**: the modular architecture (category plugins, LLM abstraction, search abstraction) is designed to support a future migration to a multi-agent system where each category could be handled by an independent agent.
