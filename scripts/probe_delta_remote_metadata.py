#!/usr/bin/env python3
"""Read-only capability probe for routine delta checksum verification.

No remote writes. Current durability semantics are unchanged by this probe.
"""
from __future__ import annotations
from pathlib import Path
import argparse,json,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from wu088_hh.transport_probe import local_hashes,compare_hash_sets,select_latest_acked_delta

def read_jsonl(path):return [json.loads(x) for x in Path(path).read_text().splitlines() if x.strip()]

def remote_stat(remote):
    t=time.perf_counter();p=subprocess.run(['rclone','lsjson','--stat','--hash',remote],capture_output=True,text=True,timeout=60);wall=time.perf_counter()-t
    if p.returncode:raise RuntimeError(f'rclone lsjson failed for {remote}: {p.stderr[-1200:]}')
    obj=json.loads(p.stdout);return {'wall_s':wall,'size':int(obj.get('Size',-1)),'hashes':obj.get('Hashes') or {},'raw':obj}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--folder',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
    if a.out.exists():raise FileExistsError('new output path required')
    folder=a.folder.resolve();q,ack=select_latest_acked_delta(read_jsonl(folder/'DURABLE_UPLOAD_QUEUE.jsonl'),read_jsonl(folder/'DURABLE_ACKS.jsonl'))
    src=Path(q['delta_path']).resolve()
    if not src.is_file():raise FileNotFoundError(src)
    lh=local_hashes(src);providers={}
    for name in ('drive','dropbox'):
        remote=str(ack[name]['id']);st=remote_stat(remote);match=compare_hash_sets(lh,st['hashes'])
        providers[name]={'remote':remote,'metadata_wall_s':st['wall_s'],'remote_size':st['size'],'local_size':src.stat().st_size,
                         'size_match':st['size']==src.stat().st_size,'remote_hashes':st['hashes'],'hash_match':match}
    report={'schema':'WU088_DELTA_REMOTE_METADATA_PROBE_V1','source':str(src),'source_sha256':q['delta_sha256'],'local_hashes':lh,
            'providers':providers,'metadata_verification_candidate':all(v['size_match'] and v['hash_match']['all_common_match'] for v in providers.values()),
            'remote_mutation_performed':False,'durability_policy_changed':False,
            'note':'Capability probe only. Final node seals remain candidates for full raw readback even if routine delta metadata verification is later approved.'}
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));return 0
if __name__=='__main__':raise SystemExit(main())
