from app.models.schemas import SourcedResult

TRUSTED_DOMAINS: dict[str, float] = {
    "statista.com": 1.0,
    "reuters.com": 1.0,
    "bloomberg.com": 1.0,
    "ft.com": 0.95,
    "wsj.com": 0.95,
    "mckinsey.com": 0.9,
    "bcg.com": 0.9,
    "bain.com": 0.9,
    "deloitte.com": 0.85,
    "pwc.com": 0.85,
    "ey.com": 0.85,
    "kpmg.com": 0.85,
    "worldbank.org": 0.9,
    "imf.org": 0.9,
    "oecd.org": 0.9,
    "ec.europa.eu": 0.85,
    "insee.fr": 0.85,
    "forbes.com": 0.75,
    "economist.com": 0.8,
    "hbr.org": 0.8,
    "techcrunch.com": 0.7,
    "crunchbase.com": 0.7,
}

_DEFAULT_DOMAIN_TRUST = 0.4


def _get_domain_trust(domain: str) -> float:
    domain = domain.lower().removeprefix("www.")
    if domain in TRUSTED_DOMAINS:
        return TRUSTED_DOMAINS[domain]
    for trusted, score in TRUSTED_DOMAINS.items():
        if domain.endswith("." + trusted):
            return score * 0.9
    return _DEFAULT_DOMAIN_TRUST


def compute_confidence(results: list[SourcedResult]) -> float:
    if not results:
        return 0.0

    quantity_score = min(len(results) / 5, 1.0)

    trust_scores = [_get_domain_trust(r.domain) for r in results]
    trust_score = sum(trust_scores) / len(trust_scores)

    relevance_scores = [r.relevance_score for r in results]
    relevance_score = (
        sum(relevance_scores) / len(relevance_scores)
        if any(relevance_scores)
        else 0.5
    )

    unique_domains = len({r.domain.lower().removeprefix("www.") for r in results})
    diversity_score = min(unique_domains / 3, 1.0)

    confidence = (
        0.25 * quantity_score
        + 0.30 * trust_score
        + 0.25 * relevance_score
        + 0.20 * diversity_score
    )

    return round(min(confidence, 1.0), 2)
