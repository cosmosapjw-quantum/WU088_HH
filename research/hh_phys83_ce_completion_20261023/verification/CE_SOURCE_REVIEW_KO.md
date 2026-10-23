# PHYS83 source and physics review before coding

Review time: 2026-10-23. Reviewed parent: `09289300ec2e500806aa2cb82365f00329e41c8c`.
Active instructions: user-provided `physmath-research-loop` 1.0.0. The earlier S0
source and theory records identify 1.3.0; those historical records are preserved.

## Decision

The preserved finite H I `1s / 2s / 2p` CCC source card, matched collision kernel,
and integrated thermal/atomic/radiative energy contract are suitable inputs for
the requested detached implementation. This is a read-only source and algebraic
review. No historical scientific identity, 902-row source reciprocity matrix,
rate grid, population integration, Wolfram check, or benchmark was rerun.

One interface notation finding was reported and the new continuation contract
now resolves it: the earlier `CONTRACT.json` uses `Qth` for signed thermal change,
whereas `DERIVATION_KO.md` uses `Q_th` for positive heat withdrawal. Use
`thermal_change_eV = -heat_withdrawal_eV`; both old conservation equations then
represent the same result. This needs no source or scientific recomputation.

## Primary-source inspection

| Item | Direct evidence read | Adoption |
|---|---|---|
| CCC channel names and units | Preserved `CCC_README`, all four raw headers and endpoint rows; [author index](https://atom.curtin.edu.au/ccc-db/index.html) | `final.initial`, integrated state cross section in `a0^2`, incident energy in eV |
| CCC native threshold | Forward raw threshold `10.2043500`, zero cross section; first positive knot `10.2043885` | Preserve native energy coordinate and first-cell interpolation choice |
| Reciprocal support | Forward support shifted by the same native gap; reverse raw files begin at excess `0.0000385` eV | Reuse existing print-precision checks; no independent reverse interpolation |
| Degeneracies | LS term weights plus [CHIANTI official ion page](https://db.chiantidatabase.org/h/h_1.html) and fixed `h_1.elvlc` | `g_1s = 2`, `g_2s = 2`, aggregate `g_2p = 2 + 4 = 6` |
| Radiative branches | Fixed `h_1.wgfa` first four rows | `A_2gamma = 8.229 /s`, `A_M1 = 2.496e-6 /s`, both fine 2p branches `A_E1 = 6.260e8 /s` |
| Metastable decay interpretation | [Parpia & Johnson 1982](https://doi.org/10.1103/PhysRevA.26.1142), primary abstract | 2E1 and M1 are radiative decay channels. The generic zero-wavelength `autoionizing rate` text in the raw file is a metadata sentinel, not a physical autoionization channel. |
| Effective collision strength alternative | [Anderson et al. 2000](https://www.adas.ac.uk/docs/h1_rmatrix.pdf), Eqs. (2)–(4), plus [2002 corrigendum](https://doi.org/10.1088/0953-4075/35/6/701), Table 1 | Alternative Maxwell-averaged source only; not substituted into the active finite CCC operator |
| Two-photon counting | [Kulkarni & Shull 2023](https://arxiv.org/html/2302.13963v1), Section II and footnote 4 | One two-photon decay event produces two photons and total energy Delta. Their higher-level case-B model is a separate closure. |

The official CHIANTI page gives ion version 11.0.1 and explicitly attributes its
effective collision strengths to Anderson 2000, revised 2002. Its `scups` year
1972 for PRA 26, 1142 is inconsistent with the publisher's 1982 record. The fixed
`wgfa` and source contract already preserve and explain this bibliographic typo.

Anderson 2002 Table 1 replaces the original 2000 effective-strength table. Its
two first ground-state rows are, at electron temperatures in eV
`[0.5, 1, 3, 5, 10, 15, 20, 25]`:

- `Upsilon_1s2s = [0.260, 0.296, 0.326, 0.339, 0.373, 0.406, 0.436, 0.461]`.
- `Upsilon_1s2p = [0.429, 0.529, 0.853, 1.15, 1.81, 2.35, 2.81, 3.20]`.

These are useful prospective comparison inputs. They average an independently
completed energy-domain model and are not a numerical reference identity for
the finite CCC W-PL operator. Their lowest source temperature is 0.5 eV; they
do not independently support a 255 K extrapolation.

## Independent algebraic checks

For source-native gap Delta, excess energy epsilon, and upper-to-ground weight
ratio `r = g_u / g_g`, define

`W(epsilon) = (epsilon + Delta) sigma_up(epsilon + Delta)` and
`epsilon sigma_down(epsilon) = W(epsilon) / r`.

Both Maxwell integrals then use the same `M0 = integral W exp(-epsilon/theta)
d epsilon` over the same shifted finite support. Consequently

`q_up / q_down = r exp(-Delta/theta)`.

This establishes detailed balance for the selected finite interpolated model.
The raw reverse table is an independent printed-data check, not a second kernel
to interpolate. Differentiation at fixed source and endpoints gives

`d log q_up / dT = ((Delta + M1/M0)/theta - 3/2)/T`,

`d log q_down / dT = ((M1/M0)/theta - 3/2)/T`.

The PL cell representation has nonnegative left/right basis weights. Summation
of these weights preserves positivity without subtracting large global
incomplete gamma moments. `W(0)=0` and the tiny first positive source knot fix
the first cell by the chosen model; they do not independently prove a physical
threshold asymptotic.

For each collisional event, excitation transfers Delta from translational energy
to atomic excitation; deexcitation reverses this transfer. A spontaneous decay
transfers Delta from the atomic store to radiation. With the same Delta in all
three owners, the signed sum vanishes event by event. One two-photon event has
energy Delta, not 2 Delta. The separate M1 event has one photon. No assumption
about a monochromatic half-energy photon spectrum is needed for these integrated
number and energy moments.

The identical fine-2p A values make the aggregate 2p spontaneous loss exactly
`A_p * n_2p` within the adopted unresolved card. The observed fine-level energies
are not identical to the native CCC gap; replacing only the radiative energy by
spectroscopic energies would change the energy contract. The current same-gap
approximation is explicit and coherent.

The three-level star remains a formal restricted population model at high
density: the source README explicitly warns that degenerate same-n dipole
transitions such as 2s–2p are formally infinite in the LS model. Their omission
is a scoped subsystem choice. Its `A/q_down` diagnostic is not a complete
physical hydrogen critical density. This limitation is already prominent in
the frozen contract and needs no new prohibition.

## Preservation and tool status

Exa search and fetch, SciSpace paper search, and official web-source reads were
actually used. Exa requested 15 candidate results across three searches;
SciSpace was called once. Tool receipts are in `tool_receipts.json` and
`tool_receipts_additional.json`. File identities and reviewed paths are in
`source_manifest.json`.

Raw Anderson 2000 and Kulkarni–Shull 2023 PDFs were downloaded and text-extracted.
The direct Anderson 2002 HTTP request returned an HTML challenge, saved as
`anderson2002_http_challenge.html`; it is not a PDF success. Its full text and
table were read through Exa and preserved separately in
`anderson2002_exa_extract.txt`. No publisher access control was bypassed.

This review ends before the same agent's separately delegated coding task.
The subsequent coder role must not be counted as an independent review of its
own implementation.
