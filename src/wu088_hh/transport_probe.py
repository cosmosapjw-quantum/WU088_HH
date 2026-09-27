from __future__ import annotations
from pathlib import Path
import hashlib

DROPBOX_BLOCK=4*1024*1024

def dropbox_content_hash(path:Path|str)->str:
    p=Path(path);outer=hashlib.sha256()
    with p.open('rb') as f:
        while True:
            block=f.read(DROPBOX_BLOCK)
            if not block:break
            outer.update(hashlib.sha256(block).digest())
    return outer.hexdigest()

def local_hashes(path:Path|str)->dict:
    p=Path(path);hs={'MD5':hashlib.md5(),'SHA-1':hashlib.sha1(),'SHA-256':hashlib.sha256()}
    with p.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):
            for h in hs.values():h.update(block)
    return {**{k:h.hexdigest() for k,h in hs.items()},'DropboxHash':dropbox_content_hash(p)}

def compare_hash_sets(local:dict,remote:dict)->dict:
    norm=lambda x:''.join(c for c in str(x).lower() if c.isalnum())
    l={norm(k):str(v).lower() for k,v in local.items()};r={norm(k):str(v).lower() for k,v in remote.items()}
    common=sorted(set(l)&set(r));matches={k:l[k]==r[k] for k in common}
    return {'common_algorithms':common,'matches':matches,'any_common':bool(common),
            'all_common_match':bool(common) and all(matches.values())}

def select_latest_acked_delta(queue_rows:list[dict],ack_rows:list[dict])->tuple[dict,dict]:
    amap={str(r['delta_sha256']):r for r in ack_rows}
    for q in reversed(queue_rows):
        h=str(q['delta_sha256'])
        if h in amap:return q,amap[h]
    raise ValueError('no acknowledged delta')
