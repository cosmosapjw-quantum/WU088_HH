"""Read-only WU R20 prospective consumer compatibility check.

This module NEVER imports or patches a foreign owner's code and NEVER issues
physical admission.  The numerical RHS is an isolated synthetic transport oracle
for the R19 105 K one-way four-state nominal rate, not an owner integration.
"""
from __future__ import annotations
from decimal import Decimal, InvalidOperation
from fractions import Fraction
from typing import Mapping, Sequence

SOURCE_STATES = ("H+", "HD(v=0,j=2)", "D+", "H2(v=0,j=1)")
SOURCE_PDF_SHA256 = "a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754"
R19_HEAD = "218f353e67ac533b9fb6d54156ec3db6e8827db6"
RATE_SI = Fraction(23, 200000000000000000)  # m^3/s, printed SQM nominal only
TEMPERATURE_K = 105
NU = (-1, -1, 1, 1)
NUCLEI = {"H": (1, 1, 0, 2), "D": (0, 1, 1, 0), "charge": (1, 0, 1, 0)}
SI_PER_CONSUMER_VOLUME = {"m^-3": 1, "cm^-3": 1000000}

# Pinned, actually inspected owner callsites. Not an exhaustive source-tree scan.
INSPECTED = {
    "REC_PR156_ROTATIONAL": {
        "repo": "cosmosapjw-quantum/rec_bianchi",
        "commit": "8806a4f757d916b6cf040625be931a66e2f0f6fe",
        "path": "research/rec_hd_multichannel_affinity_20261029/code/multichannel.py",
        "function": "generate",
        "blob": "029255494bf0a63b93bf8b2715327a8585afb5f3",
        "role": "HD_ROTATIONAL_RADIATIVE_COLLISION_DIAGNOSTIC",
        "states": tuple(f"HD(v=0,j={j})" for j in range(9)),
        "temperature_nodes_K": (50, 100, 200),
        "density_unit": "cm^-3",
    },
    "CR_PR121_HE_BUDGET": {
        "repo": "cosmosapjw-quantum/bass_cr",
        "commit": "6c3c91f9fd6261b6d79383ef7c5c8de7b6004fb6",
        "path": "research/cr_generic_budget_ssp_20261029/generic_budget_flow.py",
        "function": "ExactBudgetFlow",
        "blob": "fdde86ca6d57dcd5fcdbd8356825153a5fb65db6",
        "role": "FINITE_HE_HIGH_LOW_EVENT_BUDGET",
        "states": ("Atom",),
        "temperature_nodes_K": (),
        "density_unit": None,
    },
}


class ContractError(ValueError):
    """An invalid synthetic unit, state or clock contract was requested."""


def dec(value: object, label: str, *, positive: bool = False, signed: bool = False) -> Decimal:
    if isinstance(value, bool):
        raise ContractError(f"{label}: boolean is not a physical number")
    try:
        out = Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError) as exc:
        raise ContractError(f"{label}: invalid decimal") from exc
    if not out.is_finite() or (out <= 0 if positive else (out < 0 and not signed)):
        raise ContractError(f"{label}: nonfinite or out of range")
    return out


def check_state_order(order: Sequence[str]) -> tuple[str, ...]:
    if len(order) != 4 or len(set(order)) != 4 or set(order) != set(SOURCE_STATES):
        raise ContractError("exact four source-resolved species/states required")
    return tuple(order)


def chemical_rhs(
    state: Sequence[object], order: Sequence[str], density_unit: str,
    proper_seconds_per_coordinate: object, theta_per_proper_second: object = "0",
    *, temperature_K: int = TEMPERATURE_K,
) -> tuple[Decimal, ...]:
    """dy/ds in consumer density units per coordinate unit.

    Only a synthetic, fixed 105 K one-channel numerical oracle. Clock factor
    g=dt_proper/ds must be strictly positive. theta is prescribed s^-1.
    """
    names = check_state_order(order)
    if density_unit not in SI_PER_CONSUMER_VOLUME:
        raise ContractError("only physical number densities m^-3 or cm^-3")
    if type(temperature_K) is not int or temperature_K != TEMPERATURE_K:
        raise ContractError("exact T=105 K source node only")
    if len(state) != 4:
        raise ContractError("exactly four densities required")
    vals = {name: dec(value, name) for name, value in zip(names, state)}
    g = dec(proper_seconds_per_coordinate, "dt_proper/ds", positive=True)
    theta_raw = dec(theta_per_proper_second, "theta_s^-1", signed=True)
    alpha = Decimal(SI_PER_CONSUMER_VOLUME[density_unit])
    rate_in_consumer_units = (
        Decimal(RATE_SI.numerator) / Decimal(RATE_SI.denominator) * alpha
    )
    flux = rate_in_consumer_units * vals[SOURCE_STATES[0]] * vals[SOURCE_STATES[1]]
    rhs = {name: g * (Decimal(NU[i]) * flux - theta_raw * vals[name])
           for i, name in enumerate(SOURCE_STATES)}
    return tuple(rhs[name] for name in names)


def invariant_residual(
    state: Sequence[object], rhs: Sequence[Decimal], order: Sequence[str],
    g: object = "1", theta_per_proper_second: object = "0",
) -> dict[str, Decimal]:
    """d(w.y)/ds + g theta (w.y), in the consumer number-density units."""
    names = check_state_order(order)
    if len(state) != 4 or len(rhs) != 4:
        raise ContractError("state and RHS must both have length four")
    smap = {n: dec(v, n) for n, v in zip(names, state)}
    rmap = dict(zip(names, rhs))
    clock = dec(g, "g", positive=True)
    theta = dec(theta_per_proper_second, "theta_s^-1", signed=True)
    out = {}
    for key, weights in NUCLEI.items():
        total = sum(Decimal(w) * smap[n] for w, n in zip(weights, SOURCE_STATES))
        deriv = sum(Decimal(w) * rmap[n] for w, n in zip(weights, SOURCE_STATES))
        out[key] = deriv + clock * theta * total
    return out


def assessed_callsite(name: str) -> dict:
    """Evidence-scoped rejection of two known non-matching callsites.

    Even a contract-compatible hypothetical site cannot be activated without
    distinct owner ACK plus physical/energy/full-network gates.
    """
    if name not in INSPECTED:
        raise ContractError("unknown or uninspected consumer identity")
    c = INSPECTED[name]
    reasons = []
    if c["role"] != "REACTIVE_FOUR_STATE_MASS_ACTION_RHS":
        reasons.append("DIFFERENT_OPERATOR_ROLE")
    if len(c["states"]) != 4 or set(c["states"]) != set(SOURCE_STATES):
        reasons.append("NO_EXACT_FOUR_STATE_NETWORK")
    if TEMPERATURE_K not in c["temperature_nodes_K"]:
        reasons.append("NO_SOURCE_105K_NODE")
    if c["density_unit"] not in SI_PER_CONSUMER_VOLUME:
        reasons.append("NO_NUMBER_DENSITY_CONTRACT")
    return {
        "name": name, "repo": c["repo"], "commit": c["commit"],
        "path": c["path"], "function": c["function"], "blob": c["blob"],
        "reason_codes": reasons,
        "compatibility": "REJECTED_INSPECTED_CALLSITE" if reasons else "REQUIRES_OWNER_REVIEW",
        "actual_owner_ack": "NOT_OBTAINED", "physical_binding": False,
    }


if __name__ == "__main__":
    import json
    print(json.dumps({"schema": "wu.r20.owner_binding_preflight.v1",
                      "source_pdf_sha256": SOURCE_PDF_SHA256, "r19_head": R19_HEAD,
                      "rate_m3_s": str(RATE_SI), "canonical_dag": "34/49",
                      "HH_R10": "OFF", "L4": False, "production": "NOT_ISSUED",
                      "inspected": [assessed_callsite(name) for name in INSPECTED]}, indent=2))
