from pathlib import Path
import subprocess,os,json,hashlib,sys
W=Path(__file__).parent;P=W/'repo/research/r31ao_unequal_ladder/ncp_energy06e_certificate_20261010_v1';R=W/'run'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
records=[]
def run(label,args,cwd=None,expected=0,env=None):
 r=subprocess.run(args,cwd=cwd or W,capture_output=True,env=env);(R/(label+'.stdout')).write_bytes(r.stdout);(R/(label+'.stderr')).write_bytes(r.stderr);records.append({'label':label,'argv':args,'exit':r.returncode,'expected':expected,'stdout_sha256':sha(R/(label+'.stdout')),'stderr_sha256':sha(R/(label+'.stderr'))});assert r.returncode==expected,(label,r.returncode)
e=dict(os.environ);e['PATH']='/root/WU088_HH_ON02_20261005/toolchain/prefix/bin:/root/BASS_HE_runtime/toolchain/cargo-1.94.1-x86_64-unknown-linux-gnu/cargo/bin:'+e['PATH'];e['RUSTFLAGS']='-C opt-level=3 -C target-cpu=x86-64';e['CARGO_TARGET_DIR']=str(W/'target');e['CARGO_BUILD_JOBS']='2';e['PYTHONDONTWRITEBYTECODE']='1'
run('FINAL_RECEIPT_TESTS',['cargo','test','--offline','--manifest-path',str(W/'cargo/Cargo.toml'),'--bin','receipt_contract','energy06e_tests'],env=e)
run('FINAL_PROOF_TESTS',['python3','-m','unittest','discover','-s',str(P/'tests'),'-v'],env=e)
D=W/'inputs/HH_ENERGY06D_20261010_v1'
run('ENERGY06D_MANIFEST',['python3',str(D/'verify_delivery.py')],env=e)
run('ENERGY06D_CONTRACT_TESTS',['python3','-m','unittest','discover','-s','tests','-v'],cwd=D,env=e)
run('FINAL_RECEIPT_BUILD',['cargo','build','--offline','--manifest-path',str(W/'cargo/Cargo.toml'),'--bin','receipt_contract'],env=e)
run('NO_DISPATCH_CLI',[str(W/'target/debug/receipt_contract')],expected=77)
run('C1_NO_DISPATCH_CLI',[str(W/'c1/energy06e_c1_identity_candidate')],expected=77)
run('RUST_COMPILER',['rustc','--version','--verbose'],env=e)
# Byte preservation is separate from numerical/scientific claims.
inv=json.loads((R/'INVENTORY_BEFORE.json').read_text())['files'];assert all(Path(x['path']).is_file() and sha(Path(x['path']))==x['sha256']for x in inv)
(R/'PRESERVATION_AFTER.json').write_text(json.dumps({'files_checked':len(inv),'mismatches':0,'original_worktree_status':subprocess.check_output(['git','status','--short'],cwd='/root/WU088_HH',text=True),'scientific_dispatch':0},indent=2)+'\n')
(R/'FINAL_VERIFICATION.json').write_text(json.dumps({'commands':records,'new_tests':{'Rust_synthetic_receipt':6,'Python_exact_contract':6},'ENERGY06D_contract_tests':18,'original_owner26_and_C1_8':'historical inventory only; not rerun','original_preservation_files':len(inv),'native_science_dispatch':0,'C1_integration_dispatch':0,'root_certified':False,'family_certified':False,'fullbox_certified':False,'promotion':False,'precision':'native binary64 owner; candidate C1 FLINT128; algebra exact Fraction','flags':e['RUSTFLAGS'],'CPU':next(l.split(':',1)[1].strip()for l in Path('/proc/cpuinfo').read_text().splitlines()if l.startswith('model name')),'compiler_sha256':sha(Path('/root/WU088_HH_ON02_20261005/toolchain/prefix/bin/rustc').resolve()),'binary_sha256':sha(W/'target/debug/receipt_contract'),'target_host_benchmark':False,'canonical_scalar_arrays_sumabs':'not new kernel optimization; no promotion/comparison claimed'},indent=2)+'\n')
print('FINAL_BOUNDED_VERIFICATION_PASS',len(records),'commands',len(inv),'preserved files')
