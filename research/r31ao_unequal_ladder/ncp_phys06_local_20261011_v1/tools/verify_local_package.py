"""Hash/size verification only. No scientific module import or dispatch."""
from pathlib import Path
import json,hashlib,sys
root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parent.parent
m=json.loads((root/'MANIFEST.json').read_text());errors=[]
for name,entry in m['files'].items():
 p=(root/name).resolve()
 if root not in p.parents or not p.is_file():errors.append(name);continue
 if p.stat().st_size!=entry['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=entry['sha256']:errors.append(name)
actual={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and 'target' not in p.relative_to(root).parts and str(p.relative_to(root)) not in ('MANIFEST.json','SHA256SUMS')}
if actual!=set(m['files']):errors.extend(sorted(actual.symmetric_difference(m['files'])))
print(json.dumps(dict(status='PAYLOAD_HASHES_VERIFIED' if not errors else 'FAIL',files=len(m['files']),errors=errors,scientific_execution=False)))
sys.exit(bool(errors))

