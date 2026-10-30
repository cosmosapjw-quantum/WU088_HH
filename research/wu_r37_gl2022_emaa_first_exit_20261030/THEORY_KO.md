# WU R37 | 원본 GL2022/EMAA의 HD5 화학반응 대비 최초 영역 이탈

2026-10-30 KST. 부모 보호: WU Draft PR #175 HEAD `875426d01600649fb0c59938ad41ecdca2761f8b`. 사용자가 2026-10-30 제공한 두 **원논문 PDF**와 기존 R36 소스 원본을 현재 사용한다. 모든 기존 R36 입력 불변.

## 원전과 물리적 해석

- González-Lezana, Hily-Blant, Faure, JCP **157**, 214302 (2022), DOI `10.1063/5.0128598`: Eq. (3) SQM integral cross section, Eq. (4) thermal averaging, Eq. (5) rotational thermal average, Eqs. (6)-(7) nuclear-spin weights `1/4` even `j'`, `3/4` odd `j'`. Reaction (1) `H+ + HD(v,j) -> D+ + H2(v',j')`, reaction (2) nonreactive `H+ + HD`. `H2(v'=0, j'=0..9)` product rates are original *computed SQM* rate coefficients, not measurements.
- Velilla et al., JCP **129**, 084307 (2008), DOI `10.1063/1.2973629`, Eq. (7)-(13) global ARTSP-derived H3+ Born-Oppenheimer PES. Its **37170 cm^-1** H+ + H2 threshold is measured from H3+ PES minimum for nonisotopic H3+ and **not** a validated `H+ + HD -> D+ + H2` isotope-specific threshold or physical Q. Original Fortran coefficients are supplied separately as EPAPS document `E-JCPSA6-129-612834`, not present in either uploaded article PDF.
- EMAA raw `HD.Rovibration.805a7aa5.radex`, source ID `10.17178/emaa_hd_rovibration_805a7aa5`, 171×25 H+ (partner 7) rates within first 19 rovibrational states, HITRAN/EMAA 52 spectroscopic states and 368 radiative transitions. Uploaded raw bytes SHA256 locked, **upstream independent server-byte authentication still open**.
- Frozen primary original reaction array: `GL2022_700_SOURCE.json` from nested R36→R35→R34→R33 archive, 700 exact printed computed rates (10 final H2 J' × 7 initial HD J × 10 original T). This is a transcription/source-token artifact, with source caveats.

## Exact source-graph domain

We intentionally restrict initial/transient states to `S={HD(v=0,J=0..4)}`. Only original exact common gas temperatures `55,105,255,505,1005,1505,2005,3005 K` are used, avoiding 15 K unqualified `.000(00)` and 2505 K suspect `j=3,j'=7` exponent. Initial HD J5 reaction tokens include a suspicious duplicate source row, so HD J5 is **outside** S. The R36 EMAA collisional graph is used to construct exact transitions from S to other 19 H+ documented states; EMAA 52-state radiative A graph is used to construct exact radiative transitions from S to outside S. **Exit is defined on the available input graph**, and no unprovided collider or chemical channel is set to physical zero. The full cosmological gas does not stop evolving on exit.

Gas proton densities `n(H+)=1e-2,1,1e3,1e6 cm^-3` remain fixed. External isotropic prescribed radiation: `T_r=2.7255(1+z) K`, `z=0,10,30,100,300`. `OFF` means Planck occupation is zero, but spontaneous emission remains ON; it is not a physical negative redshift epoch. Two chemistry policies: source raw SQM vs explicit Eq. (6)-(7) product-spin-weighted `w(j') = 1/4 (even), 3/4 (odd)`. The latter is primary, former is named counterfactual.

## Killed generator, source-labeled processes

Column convention: `G_{ij}` is the rate from HD state `j` to `i`. Let `C_{ij}=n(H+) k_{j->i}^{EMAA}` with upward rates from detailed balance using EMAA/HITRAN energies `E_j` and `g_j=2J_j+1`. Radiation rates for each catalogued upper-lower pair `(u,l)` at external `T_r` are `A_ul (1+nbar_ul)` for emission, `A_ul(g_u/g_l)nbar_ul` for absorption, `nbar_ul=[exp((E_u-E_l)/(k_B T_r))-1]^{-1}`. For `OFF`, `nbar=0` but spontaneous radiation persists.

Chemical absorption to H2 final rotation `alpha=0..9` is `Q_{alpha,j}=n(H+) w_alpha k^{GL}_{j->alpha}` (rate in s^-1). Define documented source-graph exits `e_j^C=sum_{i in 19\S} C_{ij}` and `e_j^R=sum_{i in 52\S}R_{ij}`. For `i != j` in S, `G_{ij}=C_{ij}+R_{ij}`; `G_{jj}=-sum_{i !=j in S} G_{ij}-sum_alpha Q_{alpha,j}-e_j^C-e_j^R`. Thus `-G` is a nonsingular M-matrix at the tested positive rates.

Residence matrix `N=(-G)^(-1)` gives expected dwell times. For initial `e_j`, the *first-termination* probabilities are

`P_alpha^chem = [Q N]_{alpha,j}`, `P_exit^C = [e^C N]_j`, `P_exit^R=[e^R N]_j`.

Normalization follows algebraically: `1^T G=-(1^T Q+e^C+e^R)` so `(1^T Q+e^C+e^R)(-G)^(-1)=1^T`.

This **does not** give the ultimate probability of H2 production in complete chemistry; trajectories can return from beyond S. Full reaction enthalpy Q, isotope-specific native threshold, true heating/cooling, and astrophysical transfer are **unresolved**.

## Original-paper thermal comparison, explicitly hybrid

Paper Eq. (5) may be projected onto the trusted printed partial set `j∈{0,1,2,3,4,6}` using `Z_rot(j0..8)` and spin weights from Eqs. (6)–(7). This uses EMAA **HITRAN energy levels**, not an independently verified original 2022 SQM source energy ladder. Therefore the difference between printed Table 11 total and our partial sum **cannot be assigned solely to omitted j5,j7,j8 rates**. The subtotal fraction is a SOURCE-CHOICE diagnostic, *not* exact published k(T) reproduction or certified lower bound for a different energy convention. At 55 K the fraction is 0.9999330 and at 3005 K it is 0.6398755 under this hybrid energy representation. Do not interpolate the missing states or convert the printed thermal Arrhenius gamma=405 K into a PES-native threshold.

## Verification status and limits

Python normal/optimized regression 12/12; independent embedded first-step-chain implementation at (105 K, n=1e3, z=300) agrees with 65-digit continuous-time residence inverse. Symbolic Wolfram two-state absorbing probability sum exactly 1. Probability normalization maximum within full source-selected 1920 cases is 2.0735060368142087e-16 by 65-digit calculation; no negative clipping. Both calculations are same-author or external CAS cross-check, **not distinct-author R6/C9**.

Canonical WU DAG **34/49 unchanged**. Auxiliary R37 **1/1 scoped**; R6 distinct author NOT_RUN; C9 distinct author NOT_RUN; `PES_NATIVE_THRESHOLD=NULL`, `PHYSICAL_Q=NULL`, `OWNER_ACK=NOT_OBTAINED`, `HH_R10=OFF`, `FULL_A=NULL`, `L4=false`, `PRODUCTION=NOT_ISSUED`. KEEP DRAFT / NO MAIN MERGE / NO CROSS-REPO MUTATION / AUTO_NEXT=false.
