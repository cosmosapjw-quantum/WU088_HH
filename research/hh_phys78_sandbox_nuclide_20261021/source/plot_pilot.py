#!/usr/bin/env python3
"""Plot saved PHYS78 exploratory histories. This module never integrates an ODE.

Usage: python source/plot_pilot.py --input results/pilot --output figures
Input: cases/<stem>.npz and cases/<stem>.json, with status COMPLETE.
All numeric points come from those files; zeros are never replaced by a log floor.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import tempfile
from dataclasses import dataclass
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "phys78_matplotlib_cache"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import LogNorm, Normalize


WIDTH_IN = 180.0 / 25.4
SCOPE = (
    "Exploratory: isotropic reacting gas + anisotropic collisionless matter/radiation; soft UV."
)
CONVENTION = (
    r"$\pi_{\rm gas}=0$; $\pi_m$ is collisionless DM. Full Frobenius norms; "
    "no nuclear-reaction claim."
)
VECTOR_KEYS = (
    "x", "z", "b", "s_over_H", "Sigma_F", "Pi_m_F", "Pi_r_F",
    "Pi_total_F", "signed_Pi_m_F", "signed_Pi_r_F", "H_per_s", "T_K", "xe",
    "rho_baryon", "rho_m_kinetic", "rho_r_free", "energy_balance_rel",
    "nuclei_rel_error",
)
GROUPS = {
    "n": (0, r"Free neutron"),
    "H1": (1, r"$^1\mathrm{H}$"),
    "D2": (1, r"$^2\mathrm{H}$ (D)"),
    "T3": (1, r"$^3\mathrm{H}$ (T)"),
    "He3": (2, r"$^3\mathrm{He}$"),
    "He4": (2, r"$^4\mathrm{He}$"),
    "Li6": (3, r"$^6\mathrm{Li}$"),
    "Li7": (3, r"$^7\mathrm{Li}$"),
}
ION_COLORS = ("#0072B2", "#D55E00", "#009E73", "#CC79A7")
ION_STYLES = ("-", "--", "-.", ":")


@dataclass
class Case:
    alias: str
    case_id: str
    params: dict
    data: dict[str, np.ndarray]
    npz_path: Path
    receipt_path: Path

    def value(self, key: str, default: float = 0.0) -> float:
        return float(self.params.get(key, default))


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def canonical_name(value: object) -> str:
    text = value.decode("utf-8") if isinstance(value, bytes) else str(value)
    if text in ("n", "neutron"):
        return "n"
    match = re.fullmatch(r"(H1|H|D2|D|T3|T|He3|He4|Li6|Li7)[_:](\d|IV|III|II|I)", text)
    if not match:
        raise ValueError(f"Unsupported species identifier: {text!r}")
    iso = {"H": "H1", "D": "D2", "T": "T3"}.get(match[1], match[1])
    charge = {"I": "0", "II": "1", "III": "2", "IV": "3"}.get(match[2], match[2])
    return f"{iso}_{charge}"


def load_cases(input_dir: Path) -> tuple[list[Case], list[dict]]:
    cases, skipped = [], []
    folder = input_dir / "cases"
    if not folder.is_dir():
        raise ValueError(f"Missing saved-case directory: {folder}")
    expected_species = {"n"} | {
        f"{iso}_{q}" for iso, (charge, _) in GROUPS.items() if iso != "n"
        for q in range(charge + 1)
    }
    for path in sorted(folder.glob("*.npz")):
        receipt_path = path.with_suffix(".json")
        if not receipt_path.is_file():
            raise ValueError(f"NPZ has no matching completion receipt: {path}")
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        if receipt.get("status") != "COMPLETE":
            skipped.append({"npz": str(path), "status": receipt.get("status")})
            continue
        checksum_path = receipt_path.with_suffix(".json.sha256")
        if checksum_path.exists() and checksum_path.read_text().strip() != digest(receipt_path):
            raise ValueError(f"{receipt_path.name}: completion receipt checksum mismatch")
        if "npz" in receipt:
            saved = receipt["npz"]
            if path.stat().st_size != saved["bytes"] or digest(path) != saved["sha256"]:
                raise ValueError(f"{path.name}: saved scientific data checksum mismatch")
        with np.load(path, allow_pickle=False) as stored:
            required = set(VECTOR_KEYS) | {"Y", "species_names", "UV_mean_eV", "UV_N_perH"}
            missing = sorted(required - set(stored.files))
            if missing:
                raise ValueError(f"{path.name}: missing {missing}")
            data = {key: np.array(stored[key], copy=True) for key in required}
        n = data["z"].size
        if n < 2:
            raise ValueError(f"{path.name}: at least two saved epochs required")
        for key in VECTOR_KEYS:
            if data[key].shape != (n,) or not np.all(np.isfinite(data[key])):
                raise ValueError(f"{path.name}: {key} is not a finite ({n},) vector")
        if np.any(np.diff(data["x"]) <= 0) or np.any(np.diff(data["z"]) >= 0):
            raise ValueError(f"{path.name}: expected increasing x and decreasing z")
        names = [canonical_name(s) for s in data["species_names"].tolist()]
        if len(names) != 21 or len(set(names)) != 21 or set(names) != expected_species:
            raise ValueError(f"{path.name}: expected exact 21-species isotope/charge inventory")
        data["species_names"] = np.asarray(names)
        if data["Y"].shape == (n, 21) and n != 21:
            data["Y"] = data["Y"].T.copy()
            data["Y_input_layout"] = np.asarray("epochs_by_species; explicitly transposed for isotope plots")
        else:
            data["Y_input_layout"] = np.asarray("species_by_epochs")
        uv_layouts = {}
        for key in ("UV_mean_eV", "UV_N_perH"):
            if data[key].shape == (n, 3) and n != 3:
                data[key] = data[key].T.copy()
                uv_layouts[key] = "epochs_by_bands; explicitly transposed for photon plots"
            else:
                uv_layouts[key] = "bands_by_epochs"
        data["UV_input_layouts"] = uv_layouts
        for key, shape in (("Y", (21, n)), ("UV_mean_eV", (3, n)), ("UV_N_perH", (3, n))):
            if data[key].shape != shape or not np.all(np.isfinite(data[key])):
                raise ValueError(f"{path.name}: {key} is not a finite {shape} array")
        for key in ("Sigma_F", "Pi_m_F", "Pi_r_F", "Pi_total_F"):
            if np.any(data[key] < 0):
                raise ValueError(f"{path.name}: negative stored norm in {key}")
        params = receipt.get("case", {})
        case_id = str(params.get("id", path.stem))
        if any(c.case_id == case_id for c in cases):
            raise ValueError(f"Duplicate COMPLETE case identity: {case_id}")
        cases.append(Case(f"C{len(cases):03d}", case_id, params, data, path, receipt_path))
    if not cases:
        raise ValueError("No COMPLETE saved cases; no scientific figures generated")
    return cases, skipped


def style() -> None:
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 8.2,
        "axes.titlesize": 9, "axes.labelsize": 9,
        "xtick.labelsize": 8, "ytick.labelsize": 8,
        "legend.fontsize": 7.5, "axes.linewidth": .7,
        "lines.linewidth": 1.3, "savefig.dpi": 300,
        "pdf.fonttype": 42, "ps.fonttype": 42,
    })


def make_figure(rows: int, cols: int, height_mm: float, title: str, subtitle: str = ""):
    fig, axes = plt.subplots(rows, cols, figsize=(WIDTH_IN, height_mm / 25.4), squeeze=False)
    fig.suptitle(title, y=.975, fontsize=10.2)
    if subtitle:
        fig.text(.5, .925, subtitle, ha="center", va="top", fontsize=7.7)
    fig.subplots_adjust(left=.11, right=.975, top=.83 if subtitle else .86,
                        bottom=.20 if height_mm < 110 else .14, hspace=.47, wspace=.34)
    fig.text(.02, .055, SCOPE, fontsize=6.8, va="center")
    fig.text(.02, .022, CONVENTION, fontsize=6.8, va="center")
    for ax in axes.flat:
        ax.grid(True, which="major", alpha=.22, linewidth=.5)
        ax.spines[["top", "right"]].set_visible(False)
    return fig, axes


def z_axis(ax, cases: list[Case]) -> None:
    zmax = max(float(c.data["z"][0]) for c in cases)
    zmin = min(float(c.data["z"][-1]) for c in cases)
    ax.set_xlim(zmax, zmin)
    ticks = [v for v in (20, 15, 10, 8, 6, 4, 2) if zmin <= v <= zmax]
    if len(ticks) >= 2:
        ax.set_xticks(ticks)
    ax.set_xlabel("Redshift z")


def positive_line(ax, z, values, **kwargs) -> tuple[int, int]:
    values = np.asarray(values, dtype=float)
    pos = values > 0
    if np.any(pos):
        ax.plot(z, np.where(pos, values, np.nan), **kwargs)
    elif kwargs.get("label"):
        ax.plot([], [], **kwargs)
    return int(np.count_nonzero(values == 0)), int(np.count_nonzero(values < 0))


def finish_log(ax, positive_values: list[np.ndarray], zeros: int = 0, negative: int = 0) -> None:
    positive_values = [np.asarray(v)[np.asarray(v) > 0] for v in positive_values]
    positive_values = [v for v in positive_values if v.size]
    if positive_values:
        ax.set_yscale("log")
    else:
        ax.set_ylim(0, 1)
        ax.set_yticks([])
        empty_text = ("No positive stored values\n(inspect negative samples)" if negative
                      else "All stored values are zero\n(no logarithmic ordinate)")
        ax.text(.5, .50, empty_text,
                transform=ax.transAxes, ha="center", va="center", fontsize=8)
    if zeros or negative:
        txt = f"{zeros} exact-zero samples omitted; no floor"
        if negative:
            txt += f"\n{negative} negative samples omitted; see manifest"
        ax.text(.02, .02, txt, transform=ax.transAxes, fontsize=6.4,
                va="bottom", bbox={"facecolor": "white", "alpha": .82, "edgecolor": "none"})


def save_figure(fig, output: Path, name: str, description: dict, manifest: dict) -> None:
    outputs = []
    for ext in ("png", "pdf"):
        path = output / f"{name}.{ext}"
        fig.savefig(path, facecolor="white")
        outputs.append({"path": path.name, "bytes": path.stat().st_size, "sha256": digest(path)})
    plt.close(fig)
    manifest["figures"].append({"name": name, "width_mm": 180, "outputs": outputs, **description})


def representative(cases: list[Case], requested: str | None) -> Case:
    if requested:
        found = [c for c in cases if requested in (c.case_id, c.alias)]
        if len(found) != 1:
            raise ValueError(f"Requested representative case is not unique/present: {requested}")
        return found[0]
    uv = sorted({c.value("uv_scale", 1.) for c in cases})
    target = uv[len(uv) // 2]
    subset = [c for c in cases if c.value("uv_scale", 1.) == target]
    return min(subset, key=lambda c: abs(float(np.sqrt(6.) * c.data["s_over_H"][0]))
               + abs(float(c.data["signed_Pi_m_F"][0]))
               + abs(float(c.data["signed_Pi_r_F"][0])))


def highlighted(cases: list[Case], rep: Case) -> list[Case]:
    ordered = sorted(cases, key=lambda c: float(c.data["Sigma_F"][-1]))
    picks = [rep, ordered[0], ordered[len(ordered) // 2], ordered[-1]]
    unique = []
    for case in picks:
        if case.case_id not in {c.case_id for c in unique}:
            unique.append(case)
    return unique


def signed_axis(ax, which: str, values: np.ndarray) -> None:
    nonzero = np.abs(values[values != 0])
    if nonzero.size and nonzero.max() / nonzero.min() >= 20:
        setter = ax.set_xscale if which == "x" else ax.set_yscale
        setter("symlog", linthresh=float(nonzero.min()) / 2., linscale=.7)
    if which == "x":
        ax.axvline(0, color=".7", lw=.6, zorder=0)
    else:
        ax.axhline(0, color=".7", lw=.6, zorder=0)


def sweep(cases: list[Case], rep: Case, output: Path, manifest: dict) -> None:
    uv = rep.value("uv_scale", 1.)
    chosen_uv = [c for c in cases if c.value("uv_scale", 1.) == uv]
    rad = min({c.value("A_r") for c in chosen_uv}, key=abs)
    left = [c for c in chosen_uv if c.value("A_r") == rad]
    sigma = min({c.value("sigma0_F_signed", float(np.sqrt(6.) * c.data["s_over_H"][0]))
                 for c in chosen_uv}, key=abs)
    right = [c for c in chosen_uv
             if c.value("sigma0_F_signed", float(np.sqrt(6.) * c.data["s_over_H"][0])) == sigma]
    final = np.asarray([c.data["Sigma_F"][-1] for c in chosen_uv])
    pos = final[final > 0]
    if pos.size and pos.min() < pos.max():
        norm = LogNorm(vmin=float(pos.min()), vmax=float(pos.max()))
    elif pos.size:
        norm = Normalize(vmin=0, vmax=float(pos.max()))
    else:
        norm = Normalize(vmin=0, vmax=1)
    cmap = plt.get_cmap("viridis")
    fig, axes = make_figure(1, 2, 108, "Initial-condition sweep: actual saved points",
                           f"UV scale = {uv:g}; exact parameter slices; no interpolation")
    fig.subplots_adjust(right=.845, wspace=.46)
    specs = [
        (left, lambda c: np.sqrt(6.) * c.data["s_over_H"][0],
         lambda c: c.data["signed_Pi_m_F"][0],
         r"Initial signed $\Sigma_F$", r"Initial signed $\Pi_{m,F}$", f"$A_r={rad:g}$"),
        (right, lambda c: c.data["signed_Pi_m_F"][0],
         lambda c: c.data["signed_Pi_r_F"][0],
         r"Initial signed $\Pi_{m,F}$", r"Initial signed $\Pi_{r,F}$", rf"Initial signed $\Sigma_F={sigma:g}$"),
    ]
    panels = []
    for ax, (subset, getx, gety, xlabel, ylabel, title) in zip(axes.flat, specs):
        xv = np.asarray([getx(c) for c in subset], dtype=float)
        yv = np.asarray([gety(c) for c in subset], dtype=float)
        cv = np.asarray([c.data["Sigma_F"][-1] for c in subset])
        positive = cv > 0
        if positive.any():
            ax.scatter(xv[positive], yv[positive], c=cv[positive], norm=norm, cmap=cmap,
                       s=31, linewidths=.4, edgecolors="#303030", zorder=3)
        if (~positive).any():
            ax.scatter(xv[~positive], yv[~positive], facecolors="none", edgecolors="black",
                       s=37, linewidths=.9, label=r"Final $\Sigma_F=0$", zorder=4)
            ax.legend(loc="best", fontsize=6.7)
        signed_axis(ax, "x", xv)
        signed_axis(ax, "y", yv)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title + f"; n={len(subset)}", fontsize=8.5)
        panels.append({"case_ids": [c.case_id for c in subset], "x": xv.tolist(), "y": yv.tolist(),
                       "color_final_Sigma_F": cv.tolist(), "exact_zero_color_count": int((~positive).sum())})
    if pos.size:
        cax = fig.add_axes([.885, .23, .025, .56])
        fig.colorbar(ScalarMappable(norm=norm, cmap=cmap), cax=cax,
                     label=r"Final $\Sigma_F$ (stored endpoint)")
    else:
        fig.text(.89, .48, "All final\n$\\Sigma_F=0$", fontsize=8, ha="center")
    save_figure(fig, output, "01_parameter_sweep", {"kind": "actual_point_slices", "panels": panels}, manifest)


def evolution(cases: list[Case], picks: list[Case], output: Path, manifest: dict) -> None:
    fields = [("Sigma_F", r"Shear $\Sigma_F$"), ("Pi_m_F", r"Collisionless DM $\Pi_{m,F}$"),
              ("Pi_r_F", r"Free radiation $\Pi_{r,F}$"), ("Pi_total_F", r"Tensor-sum norm $\Pi_{{\rm total},F}$")]
    fig, axes = make_figure(2, 2, 158, "Shear and separate anisotropic-stress evolution",
                           f"{len(cases)} completed histories in gray; selected case IDs in color")
    colors = plt.get_cmap("tab10").colors
    for ax, (key, label) in zip(axes.flat, fields):
        zero, negative = 0, 0
        for c in cases:
            zc, nc = positive_line(ax, c.data["z"], c.data[key], color=".69", alpha=.38, lw=.65)
            zero += zc
            negative += nc
        for i, c in enumerate(picks):
            positive_line(ax, c.data["z"], c.data[key], color=colors[i], lw=1.45,
                          label=c.alias, zorder=5)
        finish_log(ax, [c.data[key] for c in cases], zero, negative)
        z_axis(ax, cases)
        ax.set_ylabel(label)
        ax.legend(loc="upper right", ncol=2, fontsize=6.7)
    save_figure(fig, output, "02_stress_time_evolution",
                {"kind": "all_saved_norm_histories", "highlighted_case_ids": [c.case_id for c in picks],
                 "zero_policy": "exact zeros omitted on log ordinate; no floor or component-norm summation"}, manifest)


def species_panel(ax, case: Case, iso: str) -> dict:
    charge, label = GROUPS[iso]
    names = case.data["species_names"].tolist()
    wanted = ["n"] if iso == "n" else [f"{iso}_{q}" for q in range(charge + 1)]
    rows = case.data["Y"][[names.index(n) for n in wanted]]
    total = np.sum(rows, axis=0)
    positive_total = total > 0
    ax.set_title(label)
    z_axis(ax, [case])
    ax.set_ylabel("Isotope-normalized charge fraction")
    evidence = {"isotope": iso, "species": wanted, "total_min": float(total.min()),
                "total_max": float(total.max()), "zero_total_epochs": int((total == 0).sum()),
                "negative_total_epochs": int((total < 0).sum())}
    if not positive_total.any():
        ax.set_ylim(0, 1)
        ax.set_yticks([])
        msg = "Abundance is exactly zero\ncharge fractions are undefined" if np.all(total == 0) else "No positive isotope abundance\ninspect saved numerical values"
        ax.text(.5, .5, msg, transform=ax.transAxes, ha="center", va="center", fontsize=8)
        evidence["fraction_status"] = "UNDEFINED_NO_POSITIVE_ABUNDANCE"
        return evidence
    fractions = np.full(rows.shape, np.nan)
    np.divide(rows, total[None, :], out=fractions, where=positive_total[None, :])
    zeros, negative = 0, 0
    for q, values in enumerate(fractions):
        label_q = "n" if iso == "n" else ("I", "II", "III", "IV")[q]
        zc, nc = positive_line(ax, case.data["z"], values, color=ION_COLORS[q],
                              ls=ION_STYLES[q], label=label_q)
        zeros += zc
        negative += nc
    finish_log(ax, list(fractions), zeros, negative)
    if np.any(fractions > 0):
        lo, hi = ax.get_ylim()
        ax.set_ylim(lo, max(hi, 1.08))
    ax.legend(loc="best", ncol=2, fontsize=7)
    evidence.update({"fraction_status": "NORMALIZED_ON_POSITIVE_TOTAL_ONLY",
                     "zero_fraction_samples_omitted": zeros, "negative_fraction_samples_omitted": negative,
                     "sum_minus_one_maxabs": float(np.nanmax(np.abs(fractions.sum(axis=0) - 1.)))})
    return evidence


def species_figures(case: Case, output: Path, manifest: dict) -> None:
    sets = [("03a_H_D_T_neutron", ["H1", "D2", "T3", "n"], 2, 2, 152),
            ("03b_helium_isotopes", ["He3", "He4"], 1, 2, 99),
            ("03c_lithium_isotopes", ["Li6", "Li7"], 1, 2, 99)]
    for name, isotopes, rows, cols, height in sets:
        fig, axes = make_figure(rows, cols, height, "Isotope-resolved ionization history",
                               f"Representative {case.alias}; UV scale={case.value('uv_scale', 1.):g}; each isotope has its own denominator")
        evidence = [species_panel(ax, case, iso) for ax, iso in zip(axes.flat, isotopes)]
        save_figure(fig, output, name, {"kind": "isotope_charge_fractions", "case_id": case.case_id,
                                      "species_evidence": evidence}, manifest)


def thermal_photons(cases: list[Case], picks: list[Case], rep: Case, output: Path, manifest: dict) -> None:
    colors = plt.get_cmap("tab10").colors
    fig, axes = make_figure(1, 2, 99, "Reacting gas temperature and electron abundance",
                           "Completed histories in gray; selected case IDs in color")
    for ax, key, ylabel in zip(axes.flat, ("T_K", "xe"), ("Gas temperature [K]", r"Electron abundance $x_e$ (stored definition)")):
        zero, negative = 0, 0
        for c in cases:
            zc, nc = positive_line(ax, c.data["z"], c.data[key], color=".7", lw=.65, alpha=.4)
            zero += zc
            negative += nc
        for i, c in enumerate(picks):
            positive_line(ax, c.data["z"], c.data[key], color=colors[i], label=c.alias, lw=1.5)
        finish_log(ax, [c.data[key] for c in cases], zero, negative)
        z_axis(ax, cases)
        ax.set_ylabel(ylabel)
        ax.legend(loc="best", ncol=2, fontsize=6.7)
    save_figure(fig, output, "04a_temperature_electrons", {"kind": "gas_history", "case_ids": [c.case_id for c in picks]}, manifest)

    fig, axes = make_figure(1, 2, 101, "Soft-UV photon populations and energies",
                           f"Representative {rep.alias}; three stored bands; no reconstructed source history")
    for ax, key, ylabel in zip(axes.flat, ("UV_N_perH", "UV_mean_eV"),
                              ("Photon abundance per H nucleus", "Mean photon energy [eV]")):
        zero, negative = 0, 0
        for j, values in enumerate(rep.data[key]):
            zc, nc = positive_line(ax, rep.data["z"], values, color=ION_COLORS[j],
                                  ls=ION_STYLES[j], label=f"Band {j + 1}")
            zero += zc
            negative += nc
        finish_log(ax, list(rep.data[key]), zero, negative)
        z_axis(ax, [rep])
        ax.set_ylabel(ylabel)
        ax.legend(loc="best", fontsize=7)
    save_figure(fig, output, "04b_soft_uv_photons", {"kind": "stored_photon_bands", "case_id": rep.case_id}, manifest)


def conservation(cases: list[Case], picks: list[Case], output: Path, manifest: dict) -> None:
    fig, axes = make_figure(1, 2, 102, "Stored numerical consistency diagnostics",
                           "Absolute saved residuals; sampled diagnostics do not certify continuum error")
    colors = plt.get_cmap("tab10").colors
    metrics = {}
    for ax, key, label in zip(axes.flat, ("energy_balance_rel", "nuclei_rel_error"),
                              ("Absolute relative energy residual", "Absolute relative nuclei residual")):
        zero = 0
        for c in cases:
            values = np.abs(c.data[key])
            zc, _ = positive_line(ax, c.data["z"], values, color=".69", lw=.65, alpha=.4)
            zero += zc
        for i, c in enumerate(picks):
            positive_line(ax, c.data["z"], np.abs(c.data[key]), color=colors[i], label=c.alias, lw=1.5)
        finish_log(ax, [np.abs(c.data[key]) for c in cases], zero)
        z_axis(ax, cases)
        ax.set_ylabel(label)
        ax.legend(loc="best", ncol=2, fontsize=6.7)
        metrics[key] = {"max_abs": max(float(np.max(np.abs(c.data[key]))) for c in cases),
                        "zero_samples": zero}
    save_figure(fig, output, "04c_conservation_diagnostics", {"kind": "sampled_consistency_only", "metrics": metrics}, manifest)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="Directory containing cases/*.npz and completion JSONs")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--case", help="Representative case ID or generated C000 alias for isotope and photon figures")
    args = parser.parse_args(argv)
    cases, skipped = load_cases(args.input)
    args.output.mkdir(parents=True, exist_ok=True)
    style()
    rep = representative(cases, args.case)
    picks = highlighted(cases, rep)
    manifest = {
        "schema": "PHYS78_SAVED_PLOT_MANIFEST_V1", "scope": SCOPE,
        "physics_split": "isotropic reacting gas pi_gas=0; anisotropic matter is collisionless nonbaryonic DM",
        "norm": "full Frobenius; half-contraction values are smaller by sqrt(2)",
        "total_norm": "stored Pi_total_F; tensor signed sum precedes norm",
        "new_ODE_integrations": 0, "data_source": str(args.input.resolve()),
        "representative_case": rep.case_id, "representative_selection": "explicit --case or median UV scale then smallest initial tensor amplitudes",
        "highlighted_case_ids": [c.case_id for c in picks], "skipped_incomplete_receipts": skipped,
        "zeros": "No positive floor. Exact zeros omitted on logarithmic ordinates and counted. Zero isotope abundance has undefined charge fractions.",
        "figures": [], "cases": [], "actual_ranges": {},
        "render_software": {"numpy": np.__version__, "matplotlib": matplotlib.__version__},
        "source_sha256": digest(Path(__file__)),
    }
    rows = []
    for c in cases:
        s = c.data
        row = {"alias": c.alias, "case_id": c.case_id, "sigma0_F_signed": float(np.sqrt(6.) * s["s_over_H"][0]),
               "Pi_m0_F_signed": float(s["signed_Pi_m_F"][0]), "Pi_r0_F_signed": float(s["signed_Pi_r_F"][0]),
               "A_m": c.value("A_m"), "A_r": c.value("A_r"), "uv_scale": c.value("uv_scale", 1.),
               "z_initial": float(s["z"][0]), "z_final": float(s["z"][-1]), "epochs": s["z"].size,
               "Sigma_F_final": float(s["Sigma_F"][-1]), "Pi_m_F_final": float(s["Pi_m_F"][-1]),
               "Pi_r_F_final": float(s["Pi_r_F"][-1]), "Pi_total_F_final": float(s["Pi_total_F"][-1])}
        rows.append(row)
        manifest["cases"].append({**row, "params": c.params, "npz": str(c.npz_path.resolve()),
                                  "npz_sha256": digest(c.npz_path), "receipt": str(c.receipt_path.resolve()),
                                  "receipt_sha256": digest(c.receipt_path),
                                  "Y_input_layout": str(s["Y_input_layout"]),
                                  "UV_input_layouts": s["UV_input_layouts"],
                                  "norm_identity_max_abs": {
                                      "Sigma": float(np.max(np.abs(s["Sigma_F"] - np.sqrt(6.) * np.abs(s["s_over_H"])))),
                                      "matter": float(np.max(np.abs(s["Pi_m_F"] - np.abs(s["signed_Pi_m_F"])))),
                                      "radiation": float(np.max(np.abs(s["Pi_r_F"] - np.abs(s["signed_Pi_r_F"])))),
                                      "total": float(np.max(np.abs(s["Pi_total_F"] - np.abs(s["signed_Pi_m_F"] + s["signed_Pi_r_F"]))))}})
    for key in ("Sigma_F", "Pi_m_F", "Pi_r_F", "Pi_total_F", "T_K", "xe"):
        values = np.concatenate([c.data[key] for c in cases])
        pos = values[values > 0]
        manifest["actual_ranges"][key] = {"minimum": float(values.min()), "maximum": float(values.max()),
                                          "smallest_positive": float(pos.min()) if pos.size else None,
                                          "exact_zero_samples": int((values == 0).sum()),
                                          "negative_samples": int((values < 0).sum())}
    with (args.output / "PLOTTED_CASES.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    sweep(cases, rep, args.output, manifest)
    evolution(cases, picks, args.output, manifest)
    species_figures(rep, args.output, manifest)
    thermal_photons(cases, picks, rep, args.output, manifest)
    conservation(cases, picks, args.output, manifest)
    manifest["completed_case_count"] = len(cases)
    manifest["figure_count"] = len(manifest["figures"])
    (args.output / "PLOT_MANIFEST.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": "COMPLETE_SAVED_DATA_PLOTS", "cases": len(cases),
                      "figures": len(manifest["figures"]), "output": str(args.output.resolve()),
                      "representative": rep.case_id, "new_ODE_integrations": 0}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
