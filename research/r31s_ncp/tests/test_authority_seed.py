from pathlib import Path
import importlib.util
import numpy as np

HERE=Path(__file__).resolve().parents[1]/'authority_seed'
spec=importlib.util.spec_from_file_location('grid_seed',HERE/'grid_seed.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

def test_authority_identity_chain():
    r=m.verify_authority()
    assert r['m2_model_seed_git_blob_sha1']=='43d5f2a79b8588e0844297dcf1c8ceb2df6b8ac0'
    assert r['source_frozen_inputs_sha256']=='8482d2854ab620c58bb1d7a7a45cf88eb71fd75081242263a9ef48927f0a282c'
    assert r['cp4_exact_weight_source_sha256']=='8ad5273551728a3608b5f8d43ea77f732aebeddc96bea767be0f79206fcc39eb'

def test_grid_shapes_for_m2_orders():
    for n in (160,192):
        d,t,W,gs,gw=m.grid(n,80)
        assert t.shape==(n,) and W.shape==(3,9,n,n)
        assert gs.shape==gw.shape==(80,)
        assert np.isfinite(t).all() and np.isfinite(W).all()
        assert d['exponents'].shape==(12,) and d['C'].shape==(9,9,9)

def test_seed_fields_are_binary64():
    d=m.inputs()
    assert d['exponents'].dtype==np.float64 and d['C'].dtype==np.float64 and d['v'].dtype==np.float64
