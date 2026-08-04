from .common import load_json

def validate_holdout(holdout_framework_path, support_map_path):
    fw=load_json(holdout_framework_path); sm=load_json(support_map_path)
    excluded=set(sm['excluded_historical_cases'])
    missing=[]; contaminated=[]
    for criterion,cases in sm['criterion_support'].items():
        if not cases: missing.append(criterion)
        bad=excluded.intersection(cases)
        if bad: contaminated.append({'criterion':criterion,'excluded_cases':sorted(bad)})
    return {
      'framework_version':fw['framework_version'],
      'excluded_cases':sorted(excluded),
      'all_promoted_scientific_criteria_retain_nonpsychiatric_support':not missing and not contaminated,
      'criteria_without_holdout_support':missing,
      'contaminated_support_entries':contaminated,
      'method':fw['holdout_method']
    }
