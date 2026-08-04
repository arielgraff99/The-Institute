from collections import defaultdict
from pathlib import Path
from .common import load_json, load_csv, write_json

VALID={'MET','PARTIALLY_MET','NOT_MET','CONTRADICTED','NOT_ASSESSABLE'}

def validate_framework(fw, allowed=('0.2','0.2-H1')):
    if fw['framework_version'] not in allowed: raise ValueError('Unexpected framework version')

def core_criteria(spec):
    return [c['id'] for c in spec.get('criteria',[]) if c.get('role')=='CORE']

def gate_class(framework,class_name,payload):
    spec=framework['classification_specific_criteria'][class_name]
    needed=[]
    for c in list(spec.get('required',[]))+core_criteria(spec):
        if c not in needed: needed.append(c)
    crit=payload['criteria']
    status={c:crit.get(c,{'status':'NOT_ASSESSABLE'})['status'] for c in needed}
    if any(s in {'NOT_MET','CONTRADICTED'} for s in status.values()): gate='NOT_SUPPORTED_AS_GLOBAL_CLASS'
    elif all(s=='MET' for s in status.values()): gate='SUPPORTED'
    elif all(s in {'MET','PARTIALLY_MET'} for s in status.values()): gate='PARTIALLY_SUPPORTED'
    else: gate='INSUFFICIENT_EVIDENCE'
    return gate,status

def family_counts(rows):
    d=defaultdict(set)
    for r in rows:d[r['domain']].add(r['study_family_id'])
    return {k:len(v) for k,v in sorted(d.items())}

def run_gates(framework, judgments, track='HIGHER_CONFIDENCE_EVIDENCE'):
    out={}
    for cls,payload in judgments['tracks'][track].items():
        gate,req=gate_class(framework,cls,payload)
        out[cls]={'gate':gate,'required_and_core_criteria':req,'interpretation':payload['interpretation']}
    return out

def run(framework_path,holdout_path,config_path,ledger_path,judgments_path,outdir, analyses):
    fw=load_json(framework_path); hold=load_json(holdout_path); cfg=load_json(config_path); rows=load_csv(ledger_path); j=load_json(judgments_path)
    validate_framework(fw); validate_framework(hold)
    for tracks in j['tracks'].values():
        for p in tracks.values():
            for item in p['criteria'].values():
                if item['status'] not in VALID: raise ValueError(item['status'])
    all_gates=run_gates(fw,j,'ALL_RELEVANT_EVIDENCE')
    high_gates=run_gates(fw,j,'HIGHER_CONFIDENCE_EVIDENCE')
    hold_gates=run_gates(hold,j,'HIGHER_CONFIDENCE_EVIDENCE')
    support=[k for k,v in high_gates.items() if v['gate'] in {'SUPPORTED','PARTIALLY_SUPPORTED'}]
    summary={
      'module_version':cfg['version'],'parent_version':cfg['parent_version'],'historical_framework_version':fw['framework_version'],
      'holdout_framework_version':hold['framework_version'],'records':len(rows),'unique_study_families':len(set(r['study_family_id'] for r in rows)),
      'domains':family_counts(rows),'five_priority_modules':cfg['five_priority_modules'],'tracks':{'ALL_RELEVANT_EVIDENCE':all_gates,'HIGHER_CONFIDENCE_EVIDENCE':high_gates},
      'nonpsychiatric_holdout_gates':hold_gates,'holdout_changes_classification':hold_gates!=high_gates,
      'supported_or_partial_classes':support,'preferred_formulation':'COMPOSITE_MULTIAXIAL' if len(support)>=2 else (support[0] if support else 'INSUFFICIENT_EVIDENCE'),
      'mdd_endotype_structure':analyses['endotypes']['mdd_endotype_structure'],'global_trd_equals_single_endotype':analyses['endotypes']['global_trd_equals_single_endotype'],
      'pseudoresistance_R02_recomputed':analyses['pseudoresistance']['R02_recomputed_status']
    }
    Path(outdir).mkdir(parents=True,exist_ok=True); write_json(Path(outdir)/'run_summary_v2.json',summary)
    return summary
