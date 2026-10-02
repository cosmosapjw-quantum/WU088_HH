# C3A: channel projector / parity effect / Hminus event contract

Conditional exact-reference only. No actual HH matrix evaluation, propagation, cross section, rate, source injection or production admission. Frozen107 CP1 singlet/47+2/Q/ETF/phase semantics remain unchanged. Full proofs,59 tests, source locks, raw logs and61-table DB are in the delivery ZIP; this Git directory carries the47-test regression subset.

## Metric projector

Let Psi=Bc, O=B^dagger B>0, N=c^dagger O c>0 and Z have full column rank. Define

G=Z^dagger O Z,
P=Z G^(-1) Z^dagger O,
K=OP,
w=c^dagger K c,
p=w/N.

Then P^2=P and P^dagger O=OP=K. The Hilbert-space projector is BZ G^(-1) Z^dagger B^dagger. Orthogonal decomposition proves0<=w<=N. Coefficient squared sums are not a substitute. Record N,w,p separately so normalized p does not hide norm drift.

Under B'=BT,c'=T^(-1)c,Z'=T^(-1)Z,O'=T^dagger OT for invertible T, P'=T^(-1)PT and N,w,p are invariant. Z->ZU for invertible U also leaves P unchanged.

Distinct subspaces are not automatically exclusive. O=[[1,1/2],[1/2,1]],c=e1,Z1=e1,Z2=e2 gives p1=1,p2=1/4: sum5/4, while the second coefficient is0. A categorical PVM requires Zalpha^dagger O Zbeta=0 for alpha!=beta; completeness additionally requires sum Kalpha=O. No clipping, symmetrization, pseudoinverse cutoff or probability renormalization is used.

## Parity compression is generally an effect

For c=Qa and any full-rank Q, set M=Q^dagger OQ,E=Q^dagger KQ and A=M^(-1)E. Q^dagger Q=I is unnecessary. The probability is a^dagger Ea/(a^dagger Ma), with0<=E<=M. A is not generally idempotent.

Proof: write O=R^dagger R,V=RQ M^(-1/2),Ptilde=RPR^(-1). V^dagger V=I and Ptilde is Hermitian idempotent. With Atilde=V^dagger Ptilde V,

Atilde-Atilde^2=F^dagger F,
F=(I-VV^dagger)Ptilde V.

Hence the compressed action is a projector iff P ran(Q) is contained in ran(Q), equivalently PQ=QA. O=I2,Q=(1,1)^T,Z=e1 gives A=1/2: an effect, not a projector. A full PVM can compress to a POVM.

The actual stored49x25 Q/parity were lifted from binary64 to exact rationals without recomputing sqrt(2). Parity Q=Q and parity^2=I hold. The24 non-ground diagonal entries of Q^dagger Q differ from1 by

-449514781148503/2535301200456458802993406410752.

This is represented-value arithmetic, not an HH defect attribution. Original Q was not repaired. With the expressly SYNTHETIC O=I49, the ionic rows47,48 union compresses to a projector whereas each orientation gives a1/2 effect. No actual HH O or population was evaluated.

## Events and energy

Order species as(H0,Hstar,Hplus,Hminus,e_free). Per-event changes are:

bound excitation=(-1,+1,0,0,0),
ion pair=(-2,0,+1,+1,0),
ground-product neutralization=(+2,0,-1,-1,0).

The conserved vectors are nuclei=(1,1,1,1,0),charge/e=(0,0,1,-1,-1),total electrons=(1,1,0,2,1). All dot products with these changes vanish. Ion-pair free-electron change is0; Hminus cannot be relabelled as a free electron. The third event explicitly selects ground products and is not a model of all measured neutralization channels.

For a common asymptotic energy convention,
DeltaE_model=E_Hplus+E_Hminus_trial-E_Ha_model-E_Hb_model.
Only consistently bound parameters allow the form I_H-A_H-Ea-Eb. Exact atomic energies, model trial energies and stored phase_E must not be silently mixed. No numerical threshold was supplied.

Signed per-event joule balance:
DeltaK_heavy+DeltaK_e+DeltaE_internal+DeltaE_radiation=W_external.
Missing terms are unavailable, not zero. Prescribed nuclear motion does not imply zero external work or a thermal heat assignment. For i*hbar*O*c_dot=(H-i*hbar*D_HH)c, O_dot=D_HH+D_HH^dagger, H=H^dagger, N_dot=0 but

d(c^dagger Hc)/dt=c^dagger[H_dot-D_HH^dagger O^(-1)H-H O^(-1)D_HH]c.

For general N, normalized mean energy and its derivative are divided by N. Thus norm preservation alone is not energy/heat closure.

## Scope and reproduction

The ionic state stays a declared variational trial channel, not an asserted exact Hminus eigenstate. Positive Ritz L2 populations do not define continuum ionization. Singlet alone does not define an unpolarized ensemble. Actual endpoint/channel/flux/domain/UQ authority is missing; request_rate always throws SourceUnavailable, never returns a fabricated zero.

From this Git directory, with installed Boost headers:

```sh
g++ -std=c++20 -O2 -fno-fast-math -Wall -Wextra -Werror -pedantic tests/regression_tests.cpp -o /tmp/c3a_regression
/tmp/c3a_regression
```

This runs47 new exact-reference regression cases, not the entire59-case bundle. Full reproduction instructions are in HANDOFF_KO.md inside the ZIP. Actual tested compiler:GCC14.2.0, installed Boost1.83. No target-host performance or floating interval certification is claimed.

Next:C3B_ASYMPTOTIC_OBSERVABLE_SPIN_FLUX_AND_RATE_REFERENCE_CONTRACT. Full C3/C4/C5 and physical/full49/BR01/BR02/review/production gates remain separate. Existing20/289 cells,missing269 unbounded,actual epsilon_C/R=null and B22 OPEN_UNDETERMINED are preserved.

Primary-source comparators, abstract inspected only:O'Regan et al.,PRB83,245124(2011),arXiv1102.1920;Stenrup et al.,PRA79,012713(2009),arXiv0902.1900. The former supports nonorthogonal tensor-consistent subspace reasoning; the latter distinguishes multiple neutralization final channels. Neither certifies this HH implementation or supplies its missing physical rates. W1R is generic algebra context only, not frozen107 authority.
