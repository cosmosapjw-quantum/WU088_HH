# HH-PHYS04 scientific and coding contract

## Goal and authority

Continue PHYS03 with source-ordered mixed quartic, one-sided fixed-grid remap
and opacity defects, and a concrete NCP local Codex implementation handoff.
The current user requested both the next physics loop and that handoff.
Prior session authorization covers bounded theory/code/checks, additive
non-force publication to the research branch, and create-only Google Drive
and Dropbox backup. No actual native solver dispatch is authorized by this
packet; the current owner has budget 0.

Research parent: 93e04c51c682216d9cb662b77a52a5783b15c71f.
Actual owner: 569b04cd71e45756e0fd476aef6643bd9434f4fa.
Both refs are unchanged at intake. The PHYS03 immutable archive was restored
and its 110 payload identities verified; no old scientific suite was run.
Astra research/coding v4.0.0-20260908 cores were read from the restored exact
archives. Host declaration is GPT-6 Astra Pro; runtime attestation is absent.

## Definitions and protected meaning

State z=(x_HII,x_HeII,x_HeIII,w,P_0,...,P_{n-1}) uses fractions, eV/H,
photons/H, proper seconds, densities cm^-3, c and k_B explicit.
Metric convention is (-,+,+,+), though no metric-dependent calculation is used.
a=lambda multiplies only the HH ionization and linked binding-energy sink.
b multiplies only the designated future birth source; it does not remove
pre-existing photons or alias the existing fixed-configuration theta tag.
Each four-corner or mixed family starts from the same full initial state and
uses the same fixed geometry, grid, step clocks, rates, closure and tolerances.
For a restarted segment carry nonzero U,V,W; zeroing them changes the family.

The actual order is transport/redshift -> fixed-grid hat remap -> endpoint
birth -> coupled BE evaluated at endpoint density/time. Full is diagnostic;
the sequential two-half result is the accepted path in the owner design.
Keep the fixed-node cross section and its cutoffs; do not replace it with a
moving-energy evaluation. HI provider cutoff 13.60 eV differs from binding
energy 13.598434599702 eV.

## Scope

1. Derive a local one-sided h>0 remap expansion and its composition defect.
   Grid nodes are knots. Do not assume a two-sided C2 remap at h=0.
   Cell validity and low-energy guard number/energy are explicit.
2. Derive all terms of the local mixed h^4 coefficient for general smooth
   H/He thermal F(t,z;lambda), endpoint birth, and the declared remap.
   Density drift and noncommuting transport/photo terms are retained.
3. Compute source-bound opacity and heating functionals of the remap using
   exact binary64 input leaves and rigorous rational exponential enclosures.
   The inherited selected spectrum is a BE-stage aggregate. Its reuse as an
   operator diagnostic is not an actual macro predecessor or a trajectory.
4. Implement mixed sensitivity algebra for a regular implicit equality stage,
   retaining photon Hessian/product terms and old-state sensitivities.
   Actual root existence, branch regularity, interval inverse and uniform
   parameter-family bounds remain separate obligations.
5. Provide NCP local Codex prompt, machine-readable tasks and return schema
   tied to current source files/functions, including concrete source hazards.

## Acceptance and limits

New exact rational checks must discriminate the h^4 terms and operator
composition. Independent derivation/implementation paths and shared inputs
must be disclosed. New interval numerical claims get explicit enclosures and
an independent high-precision scalar witness. Units, sign, zero-H, zero-source,
zero-HH, knot/guard and conserved moment limits are checked when relevant.
Final PROMOTE_SCOPED must come from a fresh reviewer uninvolved in candidate
generation or validation design.

No native trajectory, nonlinear BE root, NCP dispatch, old atomic integral,
or completed PHYS01/02/03 scientific suite is rerun. Local algebra does not
certify actual finite-step gas error or finite mixed sign. Physical/production
admission stays HOLD. Legacy 24/289, 265 unbounded, epsilon_C/R null, B22 OPEN,
canonical S0 HH OFF and consumed ON06G 256 macros through 3.2e11 s are unchanged.

Stop after required derivation, new bounded evidence, independent decision,
handoff, publication and backups. An unavailable actual root is recorded once;
continue the feasible algebra instead of repeating adapter-only gap audits.
