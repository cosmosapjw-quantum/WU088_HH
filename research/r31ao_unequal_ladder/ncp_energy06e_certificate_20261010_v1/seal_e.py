from pathlib import Path
import json,shutil,hashlib,zipfile,subprocess
W=Path(__file__).parent;P=W/'repo/research/r31ao_unequal_ladder/ncp_energy06e_certificate_20261010_v1';R=W/'run'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
peers=json.loads((R/'PEER_RETURNS.json').read_text());peers[-1].update({'head':'eb692c19c7cef3e3721f1e044ca3d41151d9309d','branch':'research/cr-r17-recovery-r17b1-20261010','remote_return_byte_equal_local':subprocess.check_output(['git','show','eb692c19c7cef3e3721f1e044ca3d41151d9309d:research/cr_r17b1_20261010/RETURN.json'],cwd=W/'repo')==(R/'CR_LATEST_AVAILABLE_RETURN.json').read_bytes()});(R/'PEER_RETURNS.json').write_text(json.dumps(peers,indent=2)+'\n')
# Standalone candidate/source/ABI binding separate from original authority.
b={'authority':'FINAL_SOURCE_BINDING_V4.json unchanged','source_binding_sha256':sha(P/'FINAL_SOURCE_BINDING_V4.json'),'receipt_ABI_sha256':sha(P/'RECEIPT_ABI.json'),'candidate_sources':{str(p.relative_to(P)):sha(p)for p in (P/'src').glob('*')if p.is_file()},'generated_wrappers':{p.name:sha(p)for p in (W/'cargo').glob('*')if p.is_file()},'owner_dependency':{str(p.relative_to(W/'original_owner_dependency')):sha(p)for p in (W/'original_owner_dependency').rglob('*')if p.is_file()},'C1_binary_sha256':sha(W/'c1/energy06e_c1_identity_candidate'),'C1_source_sha256':sha(W/'c1/source/wide_domain_20261001_v1/log_native_driver/primitive_worker.cpp'),'new_native_science':0,'promotion':False};(R/'CANDIDATE_BINDING.json').write_text(json.dumps(b,indent=2)+'\n')
for p in R.iterdir():
 if p.is_file():shutil.copyfile(p,P/'evidence'/p.name)
for name in ['prepare_e.py','audit_e.py','verify_e.py','build_live.py','live_binding.py','return_e.py','seal_e.py']:shutil.copyfile(W/name,P/name)
# New candidate worker sources are additive; original C1 authority remains untouched.
shutil.copytree(W/'c1/source',P/'c1_source');shutil.copytree(W/'original_owner_dependency',P/'original_owner_dependency')
# Include original failure logs from ENERGY06D (already in inputs), plus new logs.
files={str(p.relative_to(P)):{'sha256':sha(p),'bytes':p.stat().st_size}for p in sorted(P.rglob('*'))if p.is_file() and '__pycache__' not in p.parts and p.name!='FILE_MANIFEST.json'}
(P/'FILE_MANIFEST.json').write_text(json.dumps({'files':files,'new_science_dispatch':0,'source_commit_base':'027395b3b66a87a24da8608038b1a5a20f66e507'},indent=2)+'\n')
print('MANIFEST',len(files),'files')
