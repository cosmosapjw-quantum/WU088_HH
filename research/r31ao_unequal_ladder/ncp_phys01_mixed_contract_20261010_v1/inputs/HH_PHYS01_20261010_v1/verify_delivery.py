"""Check the exact published payload set without evaluating scientific kernels."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def verify():
    manifest=json.loads((ROOT/'MANIFEST.json').read_text())['files']
    actual={str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
    if set(manifest)!=actual:raise ValueError(f'file-set mismatch missing={set(manifest)-actual},extra={actual-set(manifest)}')
    for path,record in manifest.items():
        b=(ROOT/path).read_bytes()
        if len(b)!=record['bytes'] or hashlib.sha256(b).hexdigest()!=record['sha256']:raise ValueError(f'payload mismatch: {path}')
    print(f'{len(manifest)} exact payloads verified')
    return len(manifest)
if __name__=='__main__':verify()
