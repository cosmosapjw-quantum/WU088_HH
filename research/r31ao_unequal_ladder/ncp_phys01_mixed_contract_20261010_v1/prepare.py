from pathlib import Path
import json,hashlib,shutil
W=Path(__file__).parent;E=Path('/root/WU088_HH_ENERGY06E_20261010');P=W/'repo/research/r31ao_unequal_ladder/ncp_phys01_mixed_contract_20261010_v1';R=W/'run';D=W/'inputs/HH_PHYS01_20261010_v1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
records=json.loads((E/'run/INVENTORY_BEFORE.json').read_text())['files']
for x in records:assert sha(Path(x['path']))==x['sha256']
for root in [E/'run',E/'repo/research/r31ao_unequal_ladder/ncp_energy06e_certificate_20261010_v1',Path('/root/WU088_HH/native/reference'),Path('/root/WU088_HH/vendor/orchestration')]:
 for p in sorted(root.rglob('*')):
  if p.is_file()and '__pycache__' not in p.parts:records.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
for n,x in json.loads((D/'INPUT_IDENTITY.json').read_text())['selected_manifest_checked'].items():
 p=D/n;assert sha(p)==x['sha256'];other=E/'original_owner_dependency/src'/p.name
 if n.startswith('inputs/source/'):assert sha(other)==sha(p)
(R/'PRESERVATION_BEFORE.json').write_text(json.dumps({'files':records,'no_science_replay':True},indent=2)+'\n')
shutil.copytree(W/'inputs',P/'inputs');(P/'.gitignore').write_text('__pycache__/\n*.pyc\n')
for n in ['CERTIFICATE_PRECONDITIONER_AUDIT.json','BIRTH_SCHEME_LEDGER.json','BLOCKERS.json','CLAIM_LEDGER.json']:shutil.copyfile(E/'run'/n,R/('ENERGY06E_'+n))
(R/'PLAN.json').write_text(json.dumps({'scope':'frozen discrete mixed-family/corner contracts + synthetic proof only','D':'HH total at fixed S','I':'x(L,S)-x(L,0)-x(0,S)+x(0,0)','HH_defect':'D_twohalf-D_full','mixed_defect':'I_twohalf-I_full','source_time_error':'owner discrete minus true F0+lambdaH+SB flow; currently unresolved','corner_policy':'same gas/photon/guards/compensations/time/theta; S0 stops future birth only','native_dispatch':0,'native_authorization':None,'legacy_atomic_integration':0},indent=2)+'\n')
