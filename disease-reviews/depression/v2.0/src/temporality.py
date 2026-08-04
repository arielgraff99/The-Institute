from collections import Counter
BIO={'genetics','imaging','inflammation','omics','endotype_discovery','endotype_treatment_response'}

def analyze_temporality(rows):
    bio=[r for r in rows if r['domain'] in BIO]
    c=Counter(r['temporality_role'] for r in bio)
    pre=[r['record_id'] for r in bio if r['temporality_role'] in {'PREDISPOSING_OR_BASELINE','PRE_RESISTANCE_PREDICTOR'}]
    post=[r['record_id'] for r in bio if r['temporality_role'] in {'ESTABLISHED_TRD_CORRELATE','POST_TREATMENT_OR_CONSEQUENCE_UNCERTAIN'}]
    mixed=[r['record_id'] for r in bio if r['temporality_role']=='MIXED_OR_UNKNOWN']
    return {
      'biological_records':len(bio),
      'temporality_counts':dict(sorted(c.items())),
      'pre_resistance_or_baseline_records':pre,
      'post_resistance_or_consequence_uncertain_records':post,
      'mixed_or_unknown_records':mixed,
      'ontology_implication':'Pretreatment predictors receive greater weight for claims that resistance reflects a pre-existing disease/endotype. Established-TRD correlates are retained but cannot by themselves distinguish cause from consequence of illness or treatment.'
    }
