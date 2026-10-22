# HH1: one D potential for PI/RR event energy

Scope: additive successor component of PHYS79's D_PI_RR_ENERGY_ADAPTER. The owner
atomic code and PHYS79 collision code were read at HEAD
3304d16db1dc9bf868c185a8eeb6cc9dbc270e50. This unit supplies an executable
event-energy map. Cross sections, rate coefficients and emitted photon spectra
are supplied by the caller and keep their own physical provenance.

## Derivation and physical simplification

Let Y_i=n_i/n_H1 be abundance per conserved reference H1 nucleus. The local ideal
reacting gas has one temperature T, free-electron abundance x_e and particle
count N=sum_i Y_i+x_e. Nonrelativistic translational thermal energy per reference
H1 is u=(3/2) k_B N T. The ionic binding ledger uses positive ionization
potentials relative to the neutral ground state, b=sum_i epsilon_i Y_i.

The adopted PHYS79 rounded ground-state model fixes
Delta=43 k_B K and I_D=I_H+Delta. The inherited H threshold is13.6eV.
This is an explicit finite model; the 43K constant is not an isotope-structure
calculation. SI-defined k_B=1.380649e-23 J/K and eV=1.602176634e-19 J give
Delta=0.003705453302722427eV in the executed binary64 arithmetic.

For a PI event D+gamma(E)->D+ +e, the photon supplies E. The ionization
cost is I_D and the remaining translational energy is E-I_D. Thus the
binding/gas/radiation changes per event are

    Delta b=+I_D, Delta u=E-I_D, Delta u_gamma=-E, Delta x_e=+1.

This map requires E>=I_D. In particular, a photon in [I_H,I_D) may ionize
the inherited H model but not this D model. Reusing an H event rate in this gap
and changing only the heat term would create a negative PI excess. The adapter
rejects the unsupported D event rather than accepting such a heat source.
The cross-section kernel must separately be made consistent with this threshold
before combining a whole new trajectory.

For radiative recombination D+ +e->D+gamma, let e_c>=0 be the supplied mean
captured kinetic energy under the caller's chosen rate-weighted electron
distribution. In Case A the emitted photon escapes the local reacting parcel:

    Delta b=-I_D, Delta u=-e_c, Delta u_gamma=I_D+e_c, Delta x_e=-1.

The radiation ledger here includes escaping photons. Their energy must not be
inserted automatically into the local gray-photon inventory. Photon-number
changes in the API are aggregate book entries and do not specify a bin.

For both events Delta b+Delta u+Delta u_gamma=0 exactly in real arithmetic.
Multiplication by event rate R [per H1/s] yields eV per H1 per proper second.
Each event is independent, so any linear combination conserves the three-ledger
energy at the local interaction level. An H PI, forward D/H CX, D RR cycle has
zero net ionic energy; with the same potential its gas and radiation transfers
cancel exactly. This is a useful cross-process compatibility check.

The inherited RR kinetic moment is already computed from its fitted alpha(T)
using <e_c>=k_B T[3/2+d ln alpha/d ln T]. Under a temperature-independent capture
cross section, differentiating the Maxwellian average gives that identity.
This unit reuses the identity and accepts a supplied e_c; it does not assert
that an unchanged H fit is an isotope-correct D recombination fit or that
replacing a threshold alone enforces microscopic Milne detailed balance.

Atomic reactions preserve the number of nuclei, hence dN/dt=dx_e/dt.
Differentiating u gives

    dT/dt = (2 q)/(3 k_B N) - (T/N) dx_e/dt

for a local reaction heat q. When u obeys du/dt=-2 H u+q per reference nucleus,
the full temperature derivative is

    dT/dt = -2 H T + (2 q)/(3 k_B N) - (T/N) dx_e/dt.

The final term comes from the change in number of thermal particles. It is
absent from the u source itself and must not be charged twice. The expansion
term is supplied separately by the cosmological background, not derived from
the reaction-energy identity.

## Implementation and numerical meaning

hh1_d_threshold constructs one potential; hh1_event maps PI or Case-A RR into
the five scalar ledger entries; hh1_temperature_rhs implements the chain rule.
All inputs/results must be finite, energies/rates nonnegative and T,N,k_B
strictly positive where applicable. Invalid calls preserve the output object.
PI heat forms E-I before multiplying by rate, avoiding subtraction of large
total energy powers. No species projection, floor, basis change or tolerance
change is introduced. C99 costs O(1) arithmetic and O(1) memory per event.
No timing comparison with a solver is claimed.

The primary verification independently uses exact Fraction arithmetic on the
actual binary64 arguments. It tests conservation against this exact-input
oracle, not against a duplicate floating evaluation of the implementation.
The exact symbolic identities are additionally checked by root's actual Wolfram
call. Fraction arithmetic identifies algebraic and sign errors; it is not a
continuum or astrophysical-model accuracy certificate.

## Executed result

One build and one verification pass completed in0.398514s (command wall0.520427s).
Compiler: GCC13.3.0, C99, -O2, -Wall -Wextra -Werror -pedantic -fPIC -shared;
binary64. There were72 event cases,8 domain/invalid cases,27 temperature
chain-rule cases and one closed-cycle check. All passed. Maximum scaled
three-ledger residual8.54910e-17, component error7.24609e-17, temperature
chain-rule error1.70746e-16. Gates were fixed at16 and32 binary64 epsilons on
the specified energy/temperature scales before execution.

The computed D potential is13.603705453302721eV. A supplied18eV PI photon
deposits4.396294546697279eV into gas per event. The RR example with a deliberately
supplied e_c=k_B*300K radiates13.629557453089157eV per event; that chosen capture
energy is an API example, not a prediction of the inherited recombination fit.

No ODE, benchmark campaign, NCP launch or completed scientific-identity replay
was performed. Native provider admission is NOT_ISSUED and HH_R10 remains OFF.

## Research/code map and next obligation

R1–R3/C1–C2: exact PHYS79 owner/source/intake and explicit ledger scope.
R4–R5/C3: event-local energy map plus closed-cycle and temperature derivation.
C4: single-worker sandbox,30s initial ceiling, root publication after result.
C5–C8/R7: C99 source plus one executed exact-input oracle and finite numerical
checks. R6/C9: root Wolfram conservation/chain-rule check; independent code review
status belongs to root's actual review receipt, not an assumed child review.
R8–R10/C10: this energy-map component PASS_SCOPED; parent adapter PARTIAL.
The parent owner low-T CI source node remains NEXT_OPEN. The next D task is a
source-qualified threshold/cross-section/RR-moment binding and one changed-
dependency coupled control. Existing PHYS78/79 histories remain immutable.

Primary inherited source pointers:
- Verner et al.1996, DOI10.1086/177435, author photo.dat, for the pinned H fit.
- Verner & Ferland1996, DOI10.1086/192284, author table1.dat, for RR fits.
- Savin2002, DOI10.1086/324218, for D/H ground-state CX and isotope defect.
These source applications were previously documented by PHYS79 and are reused.
No new low-temperature rate or physical cross-section data were produced here.

