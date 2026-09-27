"""R31P direct midpoint preregistration and planning.

This module records the already-frozen R31J midpoint/interpolation contract.
It does not evaluate interpolation or admit trajectory/production physics.
"""
from __future__ import annotations
import math
import struct

MIDPOINTS=(4,12,24,40,56)
H_ORDERS=(160,192)
CP4_REUSED_IONIC=frozenset({4,12,24})


def interpolation_contract()->dict:
    return {
        'method':'piecewise_linear_only_after_midpoint_validation',
        'H_midpoint_max_abs_Eh':2e-7,
        'whitened_independent_generator_relative_error':2e-12,
        'interpolated_raw_gates_must_also_pass':True,
        'adaptive_rule':'bisect_only_failing_intervals',
        'minimum_interval_width_a0':1.0,
        'on_failure':'STOP_INTERPOLATION_RESOLUTION_UNRESOLVED',
    }


def h_folder_name(n:int,z:float,g:int=80,scale:str='unit')->str:
    if n not in H_ORDERS or g!=80 or scale!='unit':
        raise ValueError('R31P H source uses only frozen B160/B192 g80 unit-scale contract')
    z=float(z)
    if not math.isfinite(z) or z not in MIDPOINTS:
        raise ValueError('z is not a preregistered R31P midpoint')
    return f'B{n}_g{g}_s{scale}_z{struct.pack(">d",z).hex()}'


def midpoint_plan(*,existing_ionic_nodes)->dict:
    existing={int(z) for z in existing_ionic_nodes}
    if existing != set(CP4_REUSED_IONIC):
        raise ValueError('ionic reuse set must be exactly preregistered CP4 midpoint nodes 4,12,24')
    return {
        'schema':'WU088_R31P_MIDPOINT_DIRECT_PLAN_V1',
        'midpoints':list(MIDPOINTS),
        'h_orders':list(H_ORDERS),
        'od_z':list(MIDPOINTS),
        'jvp_z':list(MIDPOINTS),
        'ionic_reuse':sorted(CP4_REUSED_IONIC),
        'ionic_compute':[z for z in MIDPOINTS if z not in CP4_REUSED_IONIC],
        'interpolation_contract':interpolation_contract(),
        'interpolation_evaluated':False,
        'trajectory_runs':0,
        'trajectory_admitted':False,
        'production_admitted':False,
    }
