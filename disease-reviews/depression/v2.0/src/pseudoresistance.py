from collections import Counter

def analyze_pseudoresistance(rows):
    c=Counter(r['pseudoresistance_vulnerability'] for r in rows)
    high=[r['record_id'] for r in rows if r['pseudoresistance_vulnerability']=='HIGH']
    adherence=[r['record_id'] for r in rows if r['adherence_assessed'] in {'YES','PARTIAL'}]
    adequate=[r['record_id'] for r in rows if r['adequacy_verified'] in {'YES','PARTIAL'}]
    r02='PARTIALLY_MET' if adherence and adequate else 'NOT_MET'
    alternatives=['INADEQUATE_EXPOSURE','NONADHERENCE','INTOLERANCE','PHARMACOKINETIC_VARIABILITY','MISDIAGNOSIS_OR_BIPOLARITY','MEDICAL_OR_SUBSTANCE_CAUSE','TREATMENT_UNAVAILABLE_OR_DELAYED','CLINICIAN_OR_HEALTH_SYSTEM_FACTOR']
    return {
      'vulnerability_counts':dict(sorted(c.items())),
      'high_vulnerability_records':high,
      'records_addressing_adherence':adherence,
      'records_addressing_treatment_adequacy':adequate,
      'R02_recomputed_status':r02,
      'alternative_cause_classes':alternatives,
      'interpretation':'Pseudoresistance is not a nuisance variable; it is a competing causal explanation. Current literature only partially verifies adequate exposure and adherence, so a treatment-resistance-state claim remains conditional on better exposure verification.'
    }
