"""Control-flow integration tests using an explicitly synthetic batch backend."""
from pathlib import Path
import importlib
import sys
import pytest
sys.path.insert(0,str(Path(__file__).parent))

def api():
    assert (Path(__file__).parent/'m3_postidle.py').exists(), 'opt-in driver absent'
    return importlib.import_module('m3_postidle')

def sample():
    return dict(all_exact=True, active_worker_count=32, worker_cpu_parallelism=20,
                nr_throttled_delta=0, effective_cpu_parallelism=21)

def test_three_measured_calls_not_memoized():
    count=[];checks=[];emitted=[]
    def measured():count.append(1);return sample()
    rows=api().perform_measured_batches(measured,lambda:checks.append(1),emitted.append,32)
    assert len(count)==3 and len(checks)==6 and len(emitted)==3 and len(rows)==3

def test_readonly_precheck_blocks_before_batch():
    def reject():raise ValueError('grant drift')
    def forbidden():raise AssertionError('native work called before admission')
    with pytest.raises(ValueError):api().perform_measured_batches(forbidden,reject,lambda x:None,32)

def test_exactness_failure_is_not_pass():
    def wrong():return dict(sample(),all_exact=False)
    with pytest.raises(RuntimeError):api().perform_measured_batches(wrong,lambda:None,lambda x:None,32)

def test_throttled_sample_rejected():
    def throttled():return dict(sample(),nr_throttled_delta=1)
    with pytest.raises(RuntimeError):api().perform_measured_batches(throttled,lambda:None,lambda x:None,32)

def test_failed_second_batch_leaves_first_checkpoint():
    events=[];calls=[]
    def batch():
        calls.append(1)
        if len(calls)==2:raise RuntimeError('interruption')
        return sample()
    with pytest.raises(RuntimeError):api().perform_measured_batches(batch,lambda:None,events.append,32)
    assert len(events)==1 and len(calls)==2

def test_numeric_context_is_path_independent(tmp_path):
    import types
    import numpy as np
    import controls
    m=api();a=tmp_path/'a';b=tmp_path/'b';a.mkdir();b.mkdir()
    for folder in (a,b):
        (folder/'seed.py').write_text('# same source\n')
        (folder/'ref.so').write_bytes(b'reference');(folder/'cand.so').write_bytes(b'candidate')
    h0=types.SimpleNamespace(manifest={'binary_sha256':'123','spec':{'flags':['strict']}})
    h0mod=types.SimpleNamespace(verify_sources=lambda:{'input':'456'})
    def context(folder):
        built={'libraries':{'reference':{'path':str(folder/'ref.so')},'candidate':{'path':str(folder/'cand.so')}}}
        return m._numeric_context(controls,types.SimpleNamespace(np=np),h0mod,h0,
            types.SimpleNamespace(__file__=str(folder/'seed.py')),built,(np.eye(2),))
    assert context(a)==context(b)
    (b/'cand.so').write_bytes(b'changed')
    assert context(a)!=context(b)
