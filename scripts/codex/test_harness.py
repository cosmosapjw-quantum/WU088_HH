import importlib.util, json, pathlib, unittest
ROOT=pathlib.Path(__file__).resolve().parents[2]
def load(name):
    s=importlib.util.spec_from_file_location(name,ROOT/'scripts/codex'/f'{name}.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
route=load('route');watch=load('pr_watch')
class HarnessTests(unittest.TestCase):
    def setUp(self):
        self.cache=json.loads(pathlib.Path('/root/.codex/models_cache.json').read_text())
    def test_requested_routes_and_escalation(self):
        self.assertEqual(route.resolve('routine',self.cache)['model'],'gpt-5.6-luna')
        self.assertEqual(route.resolve('code',self.cache)['model'],'gpt-5.6-terra')
        self.assertEqual(route.resolve('code',self.cache,2),route.resolve('blocker',self.cache))
    def test_no_silent_substitution(self):
        with self.assertRaises(ValueError):route.resolve('routine',{'models':[]})
    def test_ultra_must_be_supported(self):
        m={'slug':'gpt-6-astra','supported_reasoning_levels':[{'effort':'max'}]}
        with self.assertRaises(ValueError):route.resolve('blocker',{'models':[m]})
    def test_unchanged_head_keeps_adoption(self):
        pr={'number':7,'headRefOid':'abc'}
        records,changed=watch.update([pr],{'7':{**pr,'disposition':'ADOPTED'}},{})
        self.assertEqual(changed,[]);self.assertEqual(records['7']['disposition'],'ADOPTED')
    def test_changed_head_invalidates_adoption(self):
        records,changed=watch.update([{'number':7,'headRefOid':'new'}],{'7':{'headRefOid':'old','disposition':'ADOPTED'}},{'7':{'headRefOid':'old','disposition':'ADOPTED'}})
        self.assertEqual(len(changed),1);self.assertEqual(records['7']['disposition'],'PENDING_REVIEW')
    def test_updated_review_invalidates_previous_disposition(self):
        pr={'number':7,'headRefOid':'abc','updatedAt':'new'}
        records,changed=watch.update([pr],{'7':{**pr,'updatedAt':'old','disposition':'ADOPTED'}},{'7':{'headRefOid':'abc','updatedAt':'old','disposition':'ADOPTED'}})
        self.assertEqual(len(changed),1);self.assertEqual(records['7']['disposition'],'PENDING_REVIEW')
    def test_source_adoption_does_not_hide_new_review(self):
        receipt={'headRefOid':'abc','updatedAt':'old','disposition':'ADOPTED_SCOPED_SOURCE_CONTRACT'}
        pr={'number':7,'headRefOid':'abc','updatedAt':'new'}
        records,changed=watch.update([pr],{'7':{**pr,'updatedAt':'old','disposition':receipt['disposition']}},{'7':receipt})
        self.assertEqual(records['7']['disposition'],'PENDING_REVIEW')
        self.assertEqual(records['7']['source_contract_adoption'],receipt)
if __name__=='__main__':unittest.main()
