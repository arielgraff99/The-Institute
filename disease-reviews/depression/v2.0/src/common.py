import csv, json
from pathlib import Path

def load_json(path):
    with open(path,encoding='utf-8') as f: return json.load(f)

def write_json(path,obj):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    with open(path,'w',encoding='utf-8') as f: json.dump(obj,f,indent=2)

def load_csv(path):
    with open(path,newline='',encoding='utf-8') as f: return list(csv.DictReader(f))

def write_csv(path, rows, fieldnames=None):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    if fieldnames is None:
        fieldnames=list(rows[0].keys()) if rows else []
    with open(path,'w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fieldnames); w.writeheader(); w.writerows(rows)
