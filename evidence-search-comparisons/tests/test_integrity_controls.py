from institute_search.appraisal import (
    EpistemicAudit,
    EvidenceUnit,
    RiskOfBiasResult,
    independent_replication_count,
    publication_count,
    route_risk_of_bias_tool,
    validate_result_level_appraisal,
)
from institute_search.config import RunConfig
from institute_search.engine import EvidenceSearchEngine
from institute_search.missing_evidence import (
    MissingEvidenceSignal,
    NegativeEvidenceRecord,
    PublicationBiasAudit,
    PublicationRecord,
    RegistryRecord,
    compare_registration,
    completed_without_publication,
)


def test_funnel_null_does_not_mean_no_publication_bias():
    audit = PublicationBiasAudit(funnel_test_p_value=0.40)
    assert audit.interpret_funnel_test() == "no_detected_asymmetry_does_not_exclude_publication_bias"


def test_fail_safe_n_not_primary():
    assert PublicationBiasAudit(fail_safe_n=500).fail_safe_n_is_primary_evidence() is False


def test_registry_detects_missing_outcome():
    reg = RegistryRecord("NCT1", "completed", ("Cognition", "Agitation"), (), 100)
    pub = PublicationRecord("PMID1", "NCT1", ("Cognition",), 90)
    result = compare_registration(reg, pub)
    assert result["missing_registered_outcomes"] == ["agitation"]
    assert result["sample_size_delta"] == -10


def test_completed_unpublished_detected():
    reg = RegistryRecord("NCT2", "completed")
    assert completed_without_publication(reg, []) is True


def test_negative_evidence_can_be_novel():
    rec = NegativeEvidenceRecord("R1", "F1", "failed_replication", "C1", "Independent replication was null", True, ("PMID:1",))
    assert rec.qualifies_as_novel_insight is True


def test_replication_counts_study_families_not_publications():
    units = [EvidenceUnit("P1", "F1"), EvidenceUnit("P2", "F1"), EvidenceUnit("P3", "F2")]
    assert publication_count(units) == 3
    assert independent_replication_count(units) == 2


def test_result_level_appraisal_kept_separate():
    rows = [
        RiskOfBiasResult("S1", "primary", "randomized_trial", "RoB 2", overall_judgment="low"),
        RiskOfBiasResult("S1", "posthoc_subgroup", "randomized_trial", "RoB 2", overall_judgment="high"),
    ]
    assert validate_result_level_appraisal(rows) == []
    assert rows[0].overall_judgment != rows[1].overall_judgment


def test_design_routes_to_specific_tool():
    assert route_risk_of_bias_tool("diagnostic_accuracy") == "QUADAS-2"
    assert route_risk_of_bias_tool("prediction_model") == "PROBAST_or_successor"


def test_epistemic_dimensions_not_collapsed():
    audit = EpistemicAudit("C1", "direct", "some_concerns", 2, "high")
    dimensions = audit.dimensions()
    assert set(dimensions) >= {"directness", "risk_of_bias", "replication_count", "missing_evidence_concern"}
    assert "score" not in dimensions


def test_material_missing_evidence_sets_concern():
    audit = PublicationBiasAudit(signals=[MissingEvidenceSignal("completed_unpublished", "NCT3", "Completed but no result found", True, "moderate", ("NCT3",))])
    assert audit.concern_level == "high"


def _config() -> RunConfig:
    return RunConfig.model_validate({
        "project_id": "integrity-demo",
        "research_question": "Does the integrity engine work?",
        "scientific_models": [{"id": "A"}, {"id": "B"}, {"id": "C"}],
    })


def test_material_negative_evidence_resets_saturation_streak():
    engine = EvidenceSearchEngine(_config())
    engine.ingest_cycle({"generation_number": 0, "novel_insights": []})
    engine.ingest_cycle({"generation_number": 1, "novel_insights": []})
    assert engine.state.consecutive_zero_novel_insight_cycles == 2
    engine.ingest_cycle({
        "generation_number": 2,
        "negative_evidence": [{
            "source_id": "R1",
            "study_family_id": "F1",
            "finding_type": "failed_replication",
            "claim_id": "C1",
            "summary": "Independent replication was null",
            "material": True,
            "provenance": ["PMID:1"],
        }],
    })
    assert engine.state.consecutive_zero_novel_insight_cycles == 0
    assert engine.state.status == "CONTINUE"


def test_integrity_outputs_are_written(tmp_path):
    engine = EvidenceSearchEngine(_config())
    engine.ingest_cycle({
        "generation_number": 0,
        "risk_of_bias": [{"study_id": "S1", "result_id": "R1", "design": "observational", "overall_judgment": "some_concerns"}],
        "negative_evidence": [{"source_id": "P1", "study_family_id": "F1", "finding_type": "null", "claim_id": "C1", "summary": "Null result", "material": True, "provenance": ["P1"]}],
        "missing_evidence_signals": [{"signal_type": "completed_unpublished", "source_id": "NCT1", "description": "Completed without publication", "material": True, "provenance": ["NCT1"]}],
        "registry_publication_matches": [{"registry_id": "NCT2", "publication_id": "P2", "missing_registered_outcomes": ["agitation"]}],
        "replication_map": [{"publication_id": "P1", "study_family_id": "F1"}],
    })
    out = engine.write_run(tmp_path)
    for name in [
        "risk_of_bias.csv",
        "negative_evidence_ledger.csv",
        "publication_bias_audit.csv",
        "registry_publication_matches.csv",
        "missing_outcomes.csv",
        "replication_map.csv",
    ]:
        assert (out / name).exists()
