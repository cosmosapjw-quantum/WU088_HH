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
    events=[]
    def wrong():return dict(sample(),all_exact=False)
    with pytest.raises(RuntimeError):api().perform_measured_batches(wrong,lambda:None,events.append,32)
    assert len(events)==1 and events[0]['measurement_status']=='EXACTNESS_OR_THROTTLING_FAILED'

def test_throttled_sample_rejected():
    events=[]
    def throttled():return dict(sample(),nr_throttled_delta=1)
    with pytest.raises(RuntimeError):api().perform_measured_batches(throttled,lambda:None,events.append,32)
    assert len(events)==1 and events[0]['measurement_status']=='EXACTNESS_OR_THROTTLING_FAILED'


def test_postcheck_failure_keeps_completed_measurement():
    events=[]; checks=[]
    def recheck():
        checks.append(1)
        if len(checks)==2:raise ValueError('allocation changed')
    with pytest.raises(ValueError):api().perform_measured_batches(sample,recheck,events.append,32)
    assert len(events)==1 and events[0]['measurement_status']=='POSTCHECK_FAILED'

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


def test_existing_h0_cache_uses_authority_compiler_identity(tmp_path):
    import hashlib
    import json
    import shutil
    import subprocess
    import types
    m=api()
    compiler=shutil.which('g++')
    spec={'sources':{'source':'sha'}, 'flags':['-fno-fast-math'],
          'compiler_version':subprocess.run([str(Path(compiler).resolve()),'--version'],
                                          capture_output=True,text=True,check=True).stdout}
    key=hashlib.sha256(json.dumps(spec,sort_keys=True).encode()).hexdigest()
    folder=tmp_path/key
    folder.mkdir()
    (folder/'h0.so').write_bytes(b'binary')
    (folder/'BUILD.json').write_text(json.dumps({'spec':spec}))
    h0=types.SimpleNamespace(verify_sources=lambda:spec['sources'],FLAGS=spec['flags'])
    m._require_existing_h0_cache(h0,tmp_path)


def test_foreign_build_rejects_binary_drift(tmp_path, monkeypatch):
    import controls
    m=api()
    monkeypatch.setattr(m,'ROOT',tmp_path)
    source=tmp_path/'native/reference/source.cpp'
    source.parent.mkdir(parents=True)
    source.write_bytes(b'source')
    library=tmp_path/'reference.so'
    library.write_bytes(b'binary')
    built={'identity':{'sources':{'reference/source.cpp':controls.sha256(source)}},
           'libraries':{'reference':{'path':str(library),'sha256':controls.sha256(library)},
                        'candidate':{'path':str(library),'sha256':controls.sha256(library)}}}
    m._verify_foreign_build(controls,built)
    library.write_bytes(b'changed')
    with pytest.raises(RuntimeError,match='binary drift'):
        m._verify_foreign_build(controls,built)
