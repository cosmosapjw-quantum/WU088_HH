import pytest
from wu088_hh.hardware import select_resources


def topology():
    return {i:(0,i%4) for i in range(8)}


def test_affinity_and_physical_core_selection():
    r=select_resources(topology(),{1,2,5,6},None,requested_workers=12)
    assert r['cpus']==[1,2]
    assert r['workers']==2
    assert r['logical_allowed']==4


def test_fractional_quota_caps_total_workers_times_threads():
    r=select_resources(topology(),set(range(8)),2.5,requested_workers=12)
    assert r['workers']==2
    with pytest.raises(ValueError,match='budget'):
        select_resources(topology(),set(range(8)),2.5,requested_workers=2,kernel_threads=2)


def test_package_core_pair_avoids_multisocket_collision():
    r=select_resources({0:(0,0),1:(1,0)},{0,1},None,requested_workers=12)
    assert r['workers']==2


def test_subcore_quota_keeps_one_worker_and_reports_limit():
    r=select_resources(topology(),set(range(8)),0.5,requested_workers=12)
    assert r['workers']==1
    assert r['quota_cores']==0.5


def test_smt_only_when_explicit_and_no_empty_affinity():
    r=select_resources(topology(),set(range(8)),None,requested_workers=8,use_smt=True)
    assert r['workers']==8
    with pytest.raises(ValueError):
        select_resources(topology(),set(),None)
