from collections import Counter, defaultdict

def analyze_trajectory(rows):
    states=Counter(r['trajectory_state'] for r in rows)
    by_family=defaultdict(set)
    for r in rows: by_family[r['trajectory_state']].add(r['study_family_id'])
    ordered={'PRE_TREATMENT':0,'FIRST_LINE':1,'SECOND_LINE':2,'MULTIPLE_FAILURES':3,'ADVANCED_INTERVENTION':4,'POST_ADVANCED_INTERVENTION':5}
    ordered_records=[r for r in rows if r['trajectory_state'] in ordered]
    evidence=[r['record_id'] for r in rows if r['domain'] in {'longitudinal','clinical_predictors'} and r['trajectory_state'] in {'MIXED_OR_UNKNOWN','MULTIPLE_FAILURES','ADVANCED_INTERVENTION'}]
    return {
      'state_record_counts':dict(sorted(states.items())),
      'state_study_family_counts':{k:len(v) for k,v in sorted(by_family.items())},
      'explicit_ordered_records':len(ordered_records),
      'longitudinal_stage_evidence_records':evidence,
      'interpretation':'The literature can be represented as a treatment-course trajectory rather than a binary label. Evidence spans pre-treatment, first-line, emerging resistance, established multiple failure, and advanced-intervention states, although many studies remain mixed/retrospective.'
    }
