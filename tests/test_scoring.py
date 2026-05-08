from app.models.schemas import SourcedResult
from app.pipeline.scoring import _get_domain_trust, compute_confidence
from app.pipeline.synthesis.llm_synthesizer import _detect_data_unavailable


def _make_result(domain: str = "example.com", relevance: float = 0.8) -> SourcedResult:
    return SourcedResult(
        title="Test",
        snippet="Test snippet",
        url=f"https://{domain}/article",
        domain=domain,
        relevance_score=relevance,
    )


class TestComputeConfidence:
    def test_empty_results_returns_zero(self):
        assert compute_confidence([]) == 0.0

    def test_single_unknown_domain_is_low(self):
        results = [_make_result("random-blog.com", relevance=0.3)]
        score = compute_confidence(results)
        assert score < 0.4

    def test_trusted_domains_score_higher(self):
        trusted = [_make_result("reuters.com") for _ in range(5)]
        untrusted = [_make_result("random-blog.com") for _ in range(5)]
        assert compute_confidence(trusted) > compute_confidence(untrusted)

    def test_diverse_domains_score_higher(self):
        diverse = [
            _make_result("reuters.com"),
            _make_result("statista.com"),
            _make_result("forbes.com"),
        ]
        same = [_make_result("reuters.com") for _ in range(3)]
        assert compute_confidence(diverse) > compute_confidence(same)

    def test_high_relevance_scores_higher(self):
        high = [_make_result("example.com", relevance=0.95) for _ in range(3)]
        low = [_make_result("example.com", relevance=0.2) for _ in range(3)]
        assert compute_confidence(high) > compute_confidence(low)

    def test_five_trusted_diverse_sources_is_high(self):
        results = [
            _make_result("reuters.com", 0.9),
            _make_result("statista.com", 0.85),
            _make_result("bloomberg.com", 0.88),
            _make_result("ft.com", 0.82),
            _make_result("forbes.com", 0.8),
        ]
        score = compute_confidence(results)
        assert score >= 0.7

    def test_confidence_capped_at_one(self):
        results = [_make_result("reuters.com", 1.0) for _ in range(10)]
        assert compute_confidence(results) <= 1.0


class TestGetDomainTrust:
    def test_www_prefix_stripped(self):
        assert _get_domain_trust("www.reuters.com") == _get_domain_trust("reuters.com")

    def test_subdomain_matched(self):
        score = _get_domain_trust("data.worldbank.org")
        assert score > 0.5

    def test_unknown_domain_returns_default(self):
        assert _get_domain_trust("my-random-site.xyz") == 0.4


class TestDetectDataUnavailable:
    def test_no_markers(self):
        assert _detect_data_unavailable("Le marche est en croissance.") is False

    def test_one_marker_not_enough(self):
        assert _detect_data_unavailable("Donnee non disponible pour ce segment.") is False

    def test_two_markers_triggers(self):
        md = "Donnee non disponible. Aucune donnee publique trouvee."
        assert _detect_data_unavailable(md) is True

    def test_case_insensitive(self):
        md = "DONNEE NON DISPONIBLE. AUCUNE DONNEE trouvee."
        assert _detect_data_unavailable(md) is True
