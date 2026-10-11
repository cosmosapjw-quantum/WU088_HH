"""Pin candidate bytes and ABI descriptor before each concrete build repair."""
from pathlib import Path
import hashlib, json, subprocess, sys
P=Path(__file__).resolve().parents[1]
def sha(b):return hashlib.sha256(b).hexdigest()
def canonical(d):return json.dumps(d,sort_keys=True,separators=(',',':')).encode()
rows=[]
for f in sorted((P/'candidate').rglob('*')):
    if f.is_file() and 'target' not in f.relative_to(P).parts:
        rows.append(dict(path=str(f.relative_to(P)),bytes=f.stat().st_size,sha256=sha(f.read_bytes())))
candidate=sha(canonical(rows))
rustc=subprocess.check_output(['/root/WU088_HH_ON02_20261005/toolchain/prefix/bin/rustc','-vV'],text=True)
abi=dict(candidate_source_sha256=candidate,rustc=rustc,precision='binary64 signed 7-slot outward Jet; value[2],gradient[7][2],hessian[7][7][2]',
         flags='dev/unoptimized default IEEE; no fast-math; CARGO_BUILD_JOBS=1',
         metadata_fields='Phys04DerivativeExport q,sigma_leaves,heat_leaves,c_leaf,kb_leaf,ev_leaf; read-only PreBE captured words; trace/counters')
abi_sha=sha(canonical(abi))
(P/'src/bindings.rs').write_text(f'pub const SOURCE_SHA:&str="{candidate}";\npub const ABI_SHA:&str="{abi_sha}";\n')
run=sys.argv[1]
out=P/'evidence'/f'SOURCE_PINS_{run}.json'
assert not out.exists()
full=[]
for d in ('src','candidate/src','tools','inputs'):
    for f in sorted((P/d).rglob('*')):
        if f.is_file() and '__pycache__' not in f.parts:
            full.append(dict(path=str(f.relative_to(P)),bytes=f.stat().st_size,sha256=sha(f.read_bytes())))
record=dict(candidate_files=rows,candidate_source_sha256=candidate,abi_descriptor=abi,abi_sha256=abi_sha,
            full_source_input_files=full,full_source_input_sha256=sha(canonical(full)),canonicalization='sorted path rows; JSON sort_keys=True,separators=(comma,colon); UTF-8; SHA256; no timestamps',
            candidate_hash_scope='all candidate files except build target; full hash includes bindings so no self hash cycle')
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:record[k] for k in ('candidate_source_sha256','abi_sha256','full_source_input_sha256')}))
