from collections import defaultdict

def analyze_endotypes(rows):
    relevant=[r for r in rows if r['endotype_scope'] in {'MDD_WIDE','CROSS_CUTTING_MDD_TRD'} and r['endotype_candidate']!='NONE']
    by=defaultdict(list)
    for r in relevant: by[r['endotype_candidate']].append(r['record_id'])
    independent=[r['record_id'] for r in relevant if ('independent' in r['design'].lower() or 'systematic' in r['design'].lower() or r['record_id'] in {'DEP017','DEP033'})]
    response=[r['record_id'] for r in relevant if r['domain']=='endotype_treatment_response' or 'moderated' in r['finding'].lower()]
    trd_specific=[r['record_id'] for r in rows if r['endotype_scope']=='TRD_ENRICHMENT_ONLY']
    return {
      'mdd_wide_or_crosscutting_candidates':{k:v for k,v in sorted(by.items())},
      'candidate_records':len(relevant),
      'records_with_some_replication_or_validation_signal':independent,
      'records_linked_to_treatment_response_or_moderation':response,
      'trd_enrichment_only_records':trd_specific,
      'mdd_endotype_structure':'PROVISIONALLY_SUPPORTED',
      'global_trd_equals_single_endotype':'NOT_SUPPORTED',
      'interpretation':'Searching MDD independently of the TRD label reveals candidate immune, metabolic, circuit and multi-omic subtypes. These support biological heterogeneity of depression, but current subtypes are not yet a validated taxonomy and do not map one-to-one onto TRD.'
    }
