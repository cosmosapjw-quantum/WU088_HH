# WU088_HH R35 | Restricted HD5 photon counting statistics, GL2022 source-locked

Date: 2026-10-30 KST. Immutable predecessor WU PR #173 HEAD `47cbb18274ce53ffb71c657ceafbdf25662c5617`. Original previous scientific archive SHA256 `a43d9fa8a39f64bde756b9b2d942b831d3d2560717198dac98a0a228bf5a370e`.

## Model and scope

The original R32 first-quench source gives probabilities b_J(T, policy, J_v1), J=0..10, for the first v=1 -> v=0 collisional quench by H+. Define w=sum_{J=0}^4 b_J in [0.23637, 0.36865] on R34 source-grid and conditional starting vector alpha_J=b_J/w for J<=4. The missing mass 1-w is NOT set to zero. Existing R33 provides a source-locked restricted HD(v=0,J=0..4) Markov chain with inelastic H+-collisions, externally prescribed isotropic CMB Planck photons and restricted GL2022 proton chemistry H+HD -> D+H2(v'=0,J'=0..9). Gas temperature and H+ density held fixed. The R34 original parent includes a documented representation seam between R32 CDMS and R33 Sung energies; R35 photon energy and its variance use solely R33 Sung line energy differences, not this seam as heat.

This is a conditional two-stage model, not the full H/D chemistry, not full vibrational radiative transfer, not the cosmic photon stress tensor or observed CMB spectra.

## Probability-generating resolvent

Column generator G has off-diagonal transition G_{ij}>=0 (rate j->i), diagonal negative total exit incl chemical loss q_j. The rates of true radiative downward transitions (spontaneous + CMB stimulated emission) j->j-1 are d_j=A_j(1+nbar_j) and upward absorptions j-1->j are a_j=A_j(g_j/g_{j-1}) nbar_j with g_j=2j+1, nbar_j=(exp(100 h c nu_j/(k_B T_r))-1)^(-1). The photon energy is epsilon_j=100 h c nu_j (J), where nu_j is the line wavenumber in cm^-1. Positive transfer means energy entering the radiation bath.

Tilt ONLY the off-diagonal radiative elements, not the unchanged loss diagonal:
G(lambda)_{j-1,j}=G(0)_{j-1,j}+d_j (exp(lambda epsilon_j)-1),
G(lambda)_{j,j-1}=G(0)_{j,j-1}+a_j (exp(-lambda epsilon_j)-1).
Other matrix elements unchanged, noting G(0) also contains collision terms. Let R=(-G(0))^-1 and q=Q^T 1. Then the terminal-chemistry moment-generating function of signed radiative energy Y is
Phi(lambda)=q^T (-G(lambda))^-1 alpha,
where Phi(0)=1 because the selected five-state restricted chemistry is absorbing.

Define D=G'(0) and S=G''(0) (off-diagonal entries weighted by signed energy and squared energy). Since q^T R=1^T from exact column-mass identity,
E[Y]=1^T D R alpha,
E[Y^2]=1^T S R alpha + 2 1^T D R D R alpha,
Var[Y]=E[Y^2]-E[Y]^2.

The separate spontaneous + stimulated emission count and absorption count are computed with offdiagonal matrices H_emit,H_abs containing their raw rates. E[N_emit]=1^T H_emit R alpha and E[N_abs]=1^T H_abs R alpha. Their second moments and covariance follow from ordered pairs of event insertions: E[N_e N_a]=1^T(H_e R H_a R + H_a R H_e R)alpha.

Exact 2-state symbolic check: with upper -> lower radiation a, lower -> upper radiation b, chemical sinks q0,q1, initial upper, the net signed photon number is a Bernoulli variable with p=a q0/(a q0+b q1+q0 q1). Its probability generating function is 1-p+p exp(s), variance p(1-p). Wolfram confirmed this symbolic identity. All matrices have dimensions s^-1 and photon energy has units J. q^T R alpha dimensionless. Energy mean/variance dimensions J/J^2.

## Scientific result, numerical domain

The 3,528 R34 original cases (six valid shared GL2022 temperatures 55,105,255,505,1005,3005 K × two v1 quench policies × seven source-defined initial v1 J × two R33 spin-policy treatments × three density ratios × seven prescribed CMB boundaries) have exact finite-state photon first/second cumulants. The 324 R34 source-bracketed radiation balance roots are re-evaluated with these moments. Every one of 324 has |mean radiation energy| <= 4.1e-31 J numerically with strictly positive variance, whose standard deviation ranges from 1.8561926925252e-21 to 1.6932528957687e-20 J per selected molecule. This is NOT proof that the 324 roots are the only mathematical roots over z=0..300, nor a cosmic thermal equilibrium condition.

Sample Tgas=105 K, initial v1J0, DB_UPWARD_V1 and Eq6-7_spin_effective, ratio n/ncrit=1: z*=46.71781031147414, mean energy ~3.60877e-36 J, standard deviation 5.70136963447e-21 J, mean emitted count 1.26860268695, mean absorbed count 1.46908527082, covariance 2.05545291323, selected landing mass 0.35878275195. Absorption is certain only within the restricted downstream chemistry.

Separate source-restricted product bounds: for each H2 product J', let p_J' be the known contribution per initial v1 molecule from first quench landing J<=4. Because the omitted probability mass r=1-w is not specified, a logically valid bound *in the assumed two-stage branch partition* is p_J' <= P_J' <= p_J'+r (one specified product can receive at most all missing mass). No claim about actual full physical network is made, and there is no bound for full-network photon number moments from omitted trajectories. The entire 35,280-row bound atlas preserves source-missing mass.

## Open/held

EMAA HD-H+ RADEX original 171x25 ASCII NOT_ACQUIRED; numeric comparisons = 0. Original GL2022 JCP 157 214302 DOI 10.1063/5.0128598 and EMAA dataset DOI 10.17178/emaa_hd_rovibration_805a7aa5 are separate source identities. Original REC-HD PR #169 now carries CDMS 2011 v2 native fit/par/lin/egy files, but WU has not received native owner approval and unrounded full precision covariance remains unavailable. Velilla2008 native PES sigma(E), physical Q and CR owner ACK remain open.

Canonical DAG 34/49 unchanged; R35 1/1 scoped auxiliary only. Different-author R6/C9 NOT_RUN. HH_R10 OFF; FULL_A null; L4=false; production NOT_ISSUED. No merge, no foreign repo mutation, no automatic next node.
