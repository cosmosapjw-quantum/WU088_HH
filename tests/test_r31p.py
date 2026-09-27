import pytest


def test_midpoint_plan_preserves_r31j_preregistration_and_direct_only_scope():
    import wu088_hh.r31p as r31p
    plan=r31p.midpoint_plan(existing_ionic_nodes={4,12,24})
    assert plan['midpoints']==[4,12,24,40,56]
    assert plan['h_orders']==[160,192]
    assert plan['od_z']==[4,12,24,40,56]
    assert plan['jvp_z']==[4,12,24,40,56]
    assert plan['ionic_reuse']==[4,12,24]
    assert plan['ionic_compute']==[40,56]
    assert plan['interpolation_evaluated'] is False
    assert plan['trajectory_runs']==0
    assert plan['production_admitted'] is False


def test_interpolation_contract_is_frozen_before_midpoint_values():
    import wu088_hh.r31p as r31p
    c=r31p.interpolation_contract()
    assert c=={
        'method':'piecewise_linear_only_after_midpoint_validation',
        'H_midpoint_max_abs_Eh':2e-7,
        'whitened_independent_generator_relative_error':2e-12,
        'interpolated_raw_gates_must_also_pass':True,
        'adaptive_rule':'bisect_only_failing_intervals',
        'minimum_interval_width_a0':1.0,
        'on_failure':'STOP_INTERPOLATION_RESOLUTION_UNRESOLVED',
    }


def test_h_folder_uses_exact_binary64_z_encoding():
    import wu088_hh.r31p as r31p
    assert r31p.h_folder_name(192,4.0)=='B192_g80_sunit_z4010000000000000'
    assert r31p.h_folder_name(160,56.0)=='B160_g80_sunit_z404c000000000000'


def test_midpoint_plan_rejects_unregistered_or_missing_reuse_nodes():
    import wu088_hh.r31p as r31p
    with pytest.raises(ValueError,match='ionic reuse'):
        r31p.midpoint_plan(existing_ionic_nodes={4,12,24,40})
