#!/usr/bin/env python3
"""Bounded, read-only GitHub intake; never runs PR code or auto-merges."""
import argparse, datetime, fcntl, hashlib, json, os, pathlib, subprocess

REPO = 'cosmosapjw-quantum/WU088_HH'
FIELDS = 'number,title,author,headRefOid,headRefName,baseRefName,isCrossRepository,updatedAt,url'

def gh(*args):
    return subprocess.run(['gh',*args],check=True,capture_output=True,text=True,timeout=45).stdout

def atomic(path, obj):
    tmp=path.with_suffix('.tmp');tmp.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n');os.replace(tmp,path)

def update(prs, old, receipts):
    changed=[];records={}
    for pr in prs:
        key=str(pr['number']); prior=old.get(key,{})
        head_changed=prior.get('headRefOid')!=pr['headRefOid']
        metadata_changed=prior.get('updatedAt')!=pr.get('updatedAt')
        if head_changed or metadata_changed: changed.append(pr)
        records[key]={**pr,'disposition': prior.get('disposition','PENDING_REVIEW') if not (head_changed or metadata_changed) else 'PENDING_REVIEW'}
        receipt=receipts.get(key,{})
        if receipt.get('headRefOid')==pr['headRefOid']:
            records[key]['receipt']=receipt
            if receipt.get('disposition')=='ADOPTED_SCOPED_SOURCE_CONTRACT':
                records[key]['source_contract_adoption']=receipt
            if receipt.get('updatedAt')==pr.get('updatedAt'):
                records[key]['disposition']=receipt['disposition']
    return records,changed

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--state',default='/root/.local/state/wu088-pr-watch');a=parser.parse_args()
    state=pathlib.Path(a.state);state.mkdir(parents=True,exist_ok=True)
    with (state/'lock').open('a') as lock:
        try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError:return
        now=datetime.datetime.now(datetime.timezone.utc).isoformat()
        try:
            prs=json.loads(gh('pr','list','--repo',REPO,'--state','open','--limit','100','--json',FIELDS))
            if len(prs)==100:raise RuntimeError('100 PR intake limit reached; pagination required, snapshot not promoted')
            old=json.loads((state/'snapshot.json').read_text()).get('prs',{}) if (state/'snapshot.json').exists() else {}
            receipts=json.loads((state/'adoptions.json').read_text()) if (state/'adoptions.json').exists() else {}
            records,changed=update(prs,old,receipts)
            # Bound one polling batch to five changed heads; unprocessed heads keep pending status.
            evidence=state/'heads';evidence.mkdir(exist_ok=True)
            def capture_path(r):
                stamp=hashlib.sha256(r['updatedAt'].encode()).hexdigest()[:16]
                return evidence/(str(r['number'])+'-'+r['headRefOid'])/'updates'/stamp
            candidates=sorted([r for r in records.values() if r['disposition']=='PENDING_REVIEW' and not (capture_path(r)/'INTAKE.json').exists()],key=lambda r:r['updatedAt'],reverse=True)[:5]
            for pr in candidates:
                dest=capture_path(pr);dest.mkdir(parents=True,exist_ok=True)
                if (dest/'INTAKE.json').exists():continue
                detail=gh('pr','view',str(pr['number']),'--repo',REPO,'--json','body,files,commits,reviews')
                # Metadata only: never checkout or execute incoming content. Full diff is reviewed on demand.
                (dest/'metadata.json').write_text(detail)
                fresh=json.loads(gh('pr','view',str(pr['number']),'--repo',REPO,'--json','headRefOid'))
                if fresh['headRefOid']!=pr['headRefOid']:raise RuntimeError('PR head moved during intake; retry next poll')
                atomic(dest/'INTAKE.json',{'head':pr['headRefOid'],'metadata_sha256':hashlib.sha256(detail.encode()).hexdigest(),'captured_utc':now,'code_executed':False})
            atomic(state/'snapshot.json',{'captured_utc':now,'repository':REPO,'prs':records})
            atomic(state/'queue.json',{'captured_utc':now,'pending':[r for r in records.values() if r['disposition']=='PENDING_REVIEW'],'policy':'Astra xhigh source/diff review, then authorized scoped additive integration; no merge or science replay','model_calls':0})
            with (state/'history.jsonl').open('a') as f:f.write(json.dumps({'utc':now,'open_prs':len(prs),'changed_heads':len(changed),'model_calls':0})+'\n')
            print(json.dumps({'open':len(prs),'changed_heads':len(changed),'pending':sum(r['disposition']=='PENDING_REVIEW' for r in records.values()),'model_calls':0}))
        except Exception as exc:
            with (state/'errors.jsonl').open('a') as f:f.write(json.dumps({'utc':now,'error':str(exc)})+'\n')
            raise

if __name__=='__main__':main()
