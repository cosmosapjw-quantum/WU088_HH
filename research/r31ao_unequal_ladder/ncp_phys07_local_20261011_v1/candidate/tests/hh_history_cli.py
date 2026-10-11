"""Black-box tests of the existing paired_history executable's HH route.

All commands and outputs are retained. No numerical solver is mocked.
"""
from pathlib import Path
import json,os,subprocess,unittest,hashlib,shutil,struct,sys
R=Path(__file__).resolve().parents[1]
# Run from the actual complete owner crate, no research-artifact layout required.
BINARY=Path(os.environ.get('HH_BINARY',str(Path(os.environ.get('CARGO_TARGET_DIR',str(R/'target')))/'debug/examples/paired_history')))
OUT=Path(os.environ['HH_CLI_TEST_OUTPUT']);OUT.mkdir(parents=True,exist_ok=False)
SCENARIO=R.parents[1]/'configs/rei_fastest_v1/science_scenario_v1.json'
commands=[]
def run(args):
    p=subprocess.run([str(BINARY),*map(str,args)],capture_output=True,timeout=30)
    i=len(commands); (OUT/f'command_{i:02}.stdout').write_bytes(p.stdout);(OUT/f'command_{i:02}.stderr').write_bytes(p.stderr)
    commands.append({'argv':[str(BINARY),*map(str,args)],'exit':p.returncode})
    (OUT/'COMMANDS.json').write_text(json.dumps(commands,indent=2)+'\n')
    return p

def digest_dir(d):
    return {str(p.relative_to(d)):hashlib.sha256(p.read_bytes()).hexdigest() for p in d.rglob('*') if p.is_file()}

class HHHistoryCli(unittest.TestCase):
    def command(self,d,mode='COMPARE',steps=1,extra=()):
        return run(['--hh',mode,'--hh-steps',steps,'--hh-grid','T0','--scenario',SCENARIO,'--output',d,*extra])
    def test_explicit_four_member_route_runs(self):
        d=OUT/'four';p=self.command(d);self.assertEqual(p.returncode,0,p.stderr.decode())
        s=json.loads((d/'summary.json').read_text());self.assertEqual(s['accepted_macros'],1);self.assertEqual(len(s['members']),4)
        self.assertEqual([m['mode'] for m in s['members']],['OFF','LCS','OFF','LCS'])
        self.assertTrue(all(m['hh_events_per_h']>0 for m in s['members'] if m['mode']=='LCS'))
        self.assertFalse(s['physical_admission'])
    def test_process_restart_matches_uninterrupted(self):
        d=OUT/'resume';u=OUT/'continuous'
        self.assertEqual(self.command(d).returncode,0)
        self.assertEqual(self.command(d,steps=2,extra=['--resume']).returncode,0)
        self.assertEqual(self.command(u,steps=2).returncode,0)
        for f in ('checkpoint.dat','trials.jsonl','summary.json'):
            self.assertEqual((d/f).read_bytes(),(u/f).read_bytes(),f)
    def test_unknown_provider_rejected_before_output(self):
        d=OUT/'badmode';p=self.command(d,mode='KS');self.assertNotEqual(p.returncode,0);self.assertIn(b'HH_CLI_MODE',p.stderr);self.assertFalse(d.exists())
    def test_full_campaign_not_silently_enabled(self):
        d=OUT/'full';p=self.command(d,extra=['--full']);self.assertNotEqual(p.returncode,0);self.assertIn(b'HH_FULL_NOT_QUALIFIED',p.stderr);self.assertFalse(d.exists())
    def test_duplicate_selection_rejected(self):
        d=OUT/'dupe';p=self.command(d,extra=['--hh','OFF']);self.assertNotEqual(p.returncode,0);self.assertIn(b'HH_CLI_DUPLICATE',p.stderr);self.assertFalse(d.exists())
    def test_nonfinite_or_out_of_range_budget_rejected(self):
        d=OUT/'badsteps';p=self.command(d,steps='NaN');self.assertNotEqual(p.returncode,0);self.assertIn(b'HH_CLI_STEPS',p.stderr);self.assertFalse(d.exists())
    def test_mutated_scenario_rejected_before_output(self):
        bad=OUT/'mutated.json';bad.write_bytes(SCENARIO.read_bytes()+b'\n');d=OUT/'badscenario'
        p=run(['--hh','LCS','--hh-steps',1,'--scenario',bad,'--output',d]);self.assertNotEqual(p.returncode,0);self.assertIn(b'HH_SCENARIO_IDENTITY',p.stderr);self.assertFalse(d.exists())
    def test_resume_mode_mismatch_preserves_evidence(self):
        d=OUT/'mode_resume';self.assertEqual(self.command(d,mode='LCS').returncode,0)
        before=digest_dir(d);p=self.command(d,mode='OFF',steps=2,extra=['--resume'])
        self.assertNotEqual(p.returncode,0);self.assertIn(b'HH_RUN_IDENTITY',p.stderr);self.assertEqual(digest_dir(d),before)


class HeaderIntegrity(HHHistoryCli):
    def test_header_change_is_rejected_without_evidence_change(self):
        d=OUT/'header';self.assertEqual(self.command(d,mode='LCS').returncode,0)
        p=d/'checkpoint.dat';text=p.read_text();lines=text.splitlines(keepends=True);v=lines[0].split();v[3]='41c2a05f20000000';lines[0]=' '.join(v)+'\n';p.write_text(''.join(lines))
        before=digest_dir(d);result=self.command(d,mode='LCS',extra=['--resume'])
        self.assertNotEqual(result.returncode,0);self.assertIn(b'HH_RUN_CHECKSUM',result.stderr);self.assertEqual(digest_dir(d),before)

class JournalRecovery(HHHistoryCli):
    def test_pending_transaction_four_write_boundaries(self):
        d=OUT/'origin';one=OUT/'snapshot_one'
        self.assertEqual(self.command(d,mode='LCS').returncode,0)
        shutil.copytree(d,one)
        self.assertEqual(self.command(d,mode='LCS',steps=2,extra=['--resume']).returncode,0)
        raw1=(one/'trials.jsonl').read_bytes();raw2=(d/'trials.jsonl').read_bytes();newraw=raw2[len(raw1):];cp2=(d/'checkpoint.dat').read_bytes()
        cases=[('before_append',0,False),('partial_append',len(newraw)//2,False),('after_append',len(newraw),False),('after_checkpoint',len(newraw),True)]
        for name,n,newcp in cases:
            with self.subTest(name=name):
                q=OUT/name;shutil.copytree(one,q)
                (q/'pending.transaction').write_bytes(struct.pack('<Q',len(newraw))+newraw+cp2)
                (q/'trials.jsonl').write_bytes(raw1+newraw[:n])
                if newcp:(q/'checkpoint.dat').write_bytes(cp2)
                p=self.command(q,mode='LCS',steps=2,extra=['--resume']);self.assertEqual(p.returncode,0,p.stderr.decode())
                self.assertEqual(json.loads(p.stdout)['computed_macros_this_process'],0)
                self.assertFalse((q/'pending.transaction').exists())
                for f in ('checkpoint.dat','trials.jsonl','summary.json'):self.assertEqual((q/f).read_bytes(),(d/f).read_bytes(),f)
    def test_unknown_log_suffix_preserved(self):
        q=OUT/'unknown';self.assertEqual(self.command(q,mode='OFF').returncode,0)
        p=q/'trials.jsonl';p.write_bytes(p.read_bytes()+b'unknown evidence\n');before=digest_dir(q)
        r=self.command(q,mode='OFF',steps=2,extra=['--resume']);self.assertNotEqual(r.returncode,0);self.assertIn(b'HH_RUN_LOG_OFFSET',r.stderr);self.assertEqual(digest_dir(q),before)
    def test_grid_identity_mismatch_preserved(self):
        q=OUT/'grid';self.assertEqual(self.command(q,mode='OFF').returncode,0);before=digest_dir(q)
        r=run(['--hh','OFF','--hh-grid','A0','--hh-steps',2,'--scenario',SCENARIO,'--output',q,'--resume']);self.assertNotEqual(r.returncode,0);self.assertIn(b'HH_RUN_IDENTITY',r.stderr);self.assertEqual(digest_dir(q),before)
    def test_corrupted_pending_preserved(self):
        q=OUT/'pendingbad';self.assertEqual(self.command(q,mode='OFF').returncode,0)
        (q/'pending.transaction').write_bytes(b'broken');before=digest_dir(q)
        r=self.command(q,mode='OFF',steps=2,extra=['--resume']);self.assertNotEqual(r.returncode,0);self.assertIn(b'HH_RUN_PENDING_SIZE',r.stderr);self.assertEqual(digest_dir(q),before)

if __name__=='__main__':
    suite=unittest.TestSuite()
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(HHHistoryCli))
    suite.addTest(HeaderIntegrity('test_header_change_is_rejected_without_evidence_change'))
    for n in ('test_pending_transaction_four_write_boundaries','test_unknown_log_suffix_preserved','test_grid_identity_mismatch_preserved','test_corrupted_pending_preserved'):
        suite.addTest(JournalRecovery(n))
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful())
