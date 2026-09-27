import pytest
from wu088_hh.fullpair_tuning import candidate_layouts, representative_pairs_from_events, select_exact_layout


def test_candidate_layouts_cover_serial_h0_friendly_and_current_baseline_without_oversubscription():
    cfg=candidate_layouts(physical_budget=12,logical_budget=24,pairs=12)
    assert (12,1,False) in cfg
    assert (6,2,False) in cfg
    assert (12,2,True) in cfg
    assert (6,4,True) in cfg
    assert (4,6,True) in cfg
    assert (3,8,True) in cfg
    assert (2,12,True) in cfg
    assert all(p<=12 for p,t,smt in cfg)
    assert all(p*t <= (24 if smt else 12) for p,t,smt in cfg)


def test_representative_pairs_span_observed_full_pair_wall_distribution():
    rows=[{'ia':i//12,'ib':i%12,'wall_seconds':float(i+1)} for i in range(144)]
    pairs=representative_pairs_from_events(rows,count=12)
    assert len(pairs)==12
    assert pairs[0]==(0,0)
    assert pairs[-1]==(11,11)
    assert len(set(pairs))==12


def test_select_exact_layout_rejects_any_nonexact_or_affinity_invalid_sample():
    samples=[
      dict(processes=12,kernel_threads=2,use_smt=True,batch_wall_s=10.0,numerical_array_exact_equal=True,affinity_disjoint=True,cross_l3_workers=0),
      dict(processes=6,kernel_threads=4,use_smt=True,batch_wall_s=8.0,numerical_array_exact_equal=False,affinity_disjoint=True,cross_l3_workers=0),
      dict(processes=4,kernel_threads=6,use_smt=True,batch_wall_s=9.0,numerical_array_exact_equal=True,affinity_disjoint=False,cross_l3_workers=0),
    ]
    best=select_exact_layout(samples)
    assert (best['processes'],best['kernel_threads'],best['use_smt'])==(12,2,True)
