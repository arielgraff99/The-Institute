import pytest
from pathlib import Path

from institute_search.config import RunConfig
from institute_search.engine import EvidenceSearchEngine


def config() -> RunConfig:
    return RunConfig.model_validate({
        "project_id": "demo",
        "research_question": "Reusable question?",
        "scientific_models": [{"id": "A"}, {"id": "B"}, {"id": "C"}],
    })


def test_requires_three_models():
    with pytest.raises(ValueError):
        RunConfig.model_validate({
            "project_id": "bad",
            "research_question": "x",
            "scientific_models": [{"id": "A"}, {"id": "B"}],
        })


def test_three_zero_insight_cycles_required():
    e = EvidenceSearchEngine(config())
    for generation in range(3):
        e.ingest_cycle({"generation_number": generation, "novel_insights": []})
    assert e.state.consecutive_zero_novel_insight_cycles == 3
    assert e.state.status == "SATURATION_CANDIDATE"


def test_new_insight_resets_counter():
    e = EvidenceSearchEngine(config())
    e.ingest_cycle({"generation_number": 0, "novel_insights": []})
    e.ingest_cycle({"generation_number": 1, "novel_insights": []})
    e.ingest_cycle({
        "generation_number": 2,
        "novel_insights": [{"category": "new_mechanism", "summary": "New pathway", "provenance": ["PMID:1"]}],
    })
    assert e.state.consecutive_zero_novel_insight_cycles == 0
    assert e.state.status == "CONTINUE"


def test_bibliographic_only_does_not_reset():
    e = EvidenceSearchEngine(config())
    e.ingest_cycle({
        "generation_number": 0,
        "novel_insights": [{"category": "bibliographic_only", "summary": "New citation", "provenance": ["x"]}],
    })
    assert e.state.consecutive_zero_novel_insight_cycles == 1


def test_multi_parent_graph_and_pruning(tmp_path: Path):
    e = EvidenceSearchEngine(config())
    e.ingest_cycle({
        "generation_number": 0,
        "nodes": [
            {"record_id": "a", "state": "included", "study_family_id": "f1"},
            {"record_id": "b", "state": "included", "study_family_id": "f2"},
            {"record_id": "c", "state": "excluded", "study_family_id": "f3"},
        ],
        "edges": [
            {"source": "a", "target": "c", "discovery_route": "forward_citation"},
            {"source": "b", "target": "c", "discovery_route": "backward_citation"},
        ],
        "pruning": [{"record_id": "c", "reason": "PR2"}],
    })
    assert e.graph.g.in_degree("c") == 2
    assert e.graph.g.nodes["c"]["pruned"] is True
    out = e.write_run(tmp_path)
    assert (out / "citation_graph.graphml").exists()
    assert (out / "growth_and_pruning.dot").exists()


def test_resource_stop_never_saturation():
    e = EvidenceSearchEngine(config())
    e.resource_limited_stop("API limit")
    assert e.state.status == "RESOURCE_LIMITED_NOT_SATURATED"
