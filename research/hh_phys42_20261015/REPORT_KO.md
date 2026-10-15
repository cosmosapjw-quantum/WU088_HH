# WU088_HH PHYS42: signed joint \((r,\mu)\) interval와 적응형 radial–angular 인증

작성 2026-10-15 KST. 직전 기준: [PHYS41 draft PR80](https://github.com/cosmosapjw-quantum/WU088_HH/pull/80) commit
`ae62c70a7ba262b3759096e220af131191e7458f`.
현재의 선택 단계는 해당 DAG의 C7B_STRONG_2D_RADIAL_ANGULAR_COUPLING_ADAPTIVE_ENCLOSURE,
이론 R5/R7 및 코딩 C5–C8의 **구성적 국소 부분 연구**다.
결론의 범위: 원래 fully coupled screened transformed PDE의 엄밀한
**noncusp positive-volume strip** strong L² upper를 두 실제 반경 근방에서
PHYS40보다 날카롭게 얻었다. 전체 6 radial panel에 대한 tight 2D
enclosure, origin/exterior scattering inverse, ionization rate는 미완료다.

## 1. 원래 물리·출처 고정

고정 원본 Hamiltonian은
\[
h_\lambda=-\frac12\Delta-\frac1r-\lambda(1+s^{-1})e^{-2s},
\quad s=|\boldsymbol r-R\hat{\boldsymbol z}|,\quad
R=\kappa=\frac7{10},\quad\lambda=1 .
\]
전자좌표는 Euclidean, 우주론적 부호는 (-,+,+,+).
물리 길이 \(a_0=5.29177210544\times10^{-11}\mathrm m\),
Hamiltonian 에너지 단위 \(E_a=2I_0=27.211386245980\mathrm{eV}\).
온도·서로 다른 에너지에서 \(c,\hbar,k_B\)는 무단으로 버리지 않는다.
원자 공급 \(I_0=13.605693122990\mathrm{eV}\)와
consumer heating \(\chi_H=13.598434599702\mathrm{eV}\)를 동일시하지 않는다.
초기 \(\phi=e^{-r}/\sqrt\pi\), spectator \(s\), Coulomb phase,
원본 \(S(R)-S(s)\) transition, \(\eta=F y\),
\(F=\exp(e^{-s})\)를 고정한다.
원본 frozen source는
`research/hh_phys34_20261015/inputs/FROZEN_U_SUBSET.npz`,
SHA-256 `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`;
21 partial waves × 6 radial panels × 11 nodes = 1386 complex128.
원본 nodal binary64를 exact dyadic으로 읽어 10차 Lagrange
polynomial을 구성한다. 이전 PHYS41의 1386 original-node 일치
증거는 유지된다. 각 \(\ell\)의 \(u_\ell,u_\ell',u_\ell''\)와 물리
source는 변경하지 않는다.

## 2. Derived theorem: signed cancellation과 바른 3차원 측도

\[
D_\ell u_\ell=u_\ell''+
 \left(\kappa^2+\frac2r-\frac{\ell(\ell+1)}{r^2}\right)u_\ell,
\quad \alpha_\ell=\sqrt{2\ell+1},\quad \mu=\cos\theta .
\]
고정 반경 \(r\), 모든 \(-1\le\mu\le1\)에서
\[
\begin{aligned}
A&=\sum_{\ell=0}^{20}\alpha_\ell
 \frac{D_\ell u_\ell}{r}P_\ell(\mu),&
B&=\sum_\ell\alpha_\ell\frac{u_\ell}{r}P_\ell(\mu),\\
C&=\sum_\ell\alpha_\ell
 \frac{r u_\ell'-u_\ell}{r^2}P_\ell(\mu),&
T&=\sum_\ell\alpha_\ell \frac{u_\ell}{r}
 \ell[P_{\ell-1}(\mu)-\mu P_\ell(\mu)] .
\end{aligned}
\]
따라서 \((1-\mu^2)\partial_\mu P_\ell=
\ell(P_{\ell-1}-\mu P_\ell)\)와 실제 Euclidean
spectator gradient에서
\[
\hat{\boldsymbol s}\cdot\nabla B
=\frac{(r-R\mu)C-(R/r)T}{s}
=\frac{H}{s}.
\]
또한 \(E=e^{-s}\), \(q(s)=(1-E)/s=\int_0^1 e^{-st}dt\),
\(U(s)=Eq-E/2-3E^2/2\),
\(S_0(r)=2(1+\kappa^2)e^{-r}\)를 사용한다.
PHYS40의 원래 전체 residual \(G=\sqrt{4\pi}\mathcal R\)는
\[
\boxed{
G=(A-S_0)-2\,\frac{E H}{s}-2UB+S_0(1-e^{-E}) .
}
\]
원래 \(S_0\)를 **먼저 \(A\)의 \(\ell=0\) radial numerator에서
상쇄**한 뒤 실수·허수 부호가 있는 구간 합산을 수행한다.
이는 PHYS41의 각 연산항 절댓값을 먼저 더한 전역 상계보다
국소 cancellation을 보존한다.

구체적으로 비-cusp cell \(I_r=[a,b]\), \(I_\mu=[m_0,m_1]\)에
대하여 \(a>0\), \([a,b]\)는 실제 frozen panel 내부,
\(R\notin[a,b]\)라고 한다. \(r^2D_\ell u_\ell\),
\(r u_\ell'-u_\ell\)와 \(u_\ell\)를 exact rational Lagrange
다항식으로 구성하고 각 radial cell에서 signed
Bernstein 계수 최솟값/최댓값으로 제한한다.
\(\ell=0\)의 source \(r^3S_0\)는 192항 양의
\(\exp(a)\) reciprocal outer bound 및 48-decimal center,
24차 alternating Taylor와 정확한 여항
\((b-a)^{25}/25!\)로 뺀다. 차원의 \(r^3\) 공통인수를
정확히 보존하여 source truncation의 잘못된 \(b^3/a^3\)
증폭을 피한다.

Angular Legendre 및
\(T_\ell=\ell(P_{\ell-1}-\mu P_\ell)\)도 각 \(I_\mu\)에서
exact rational Bernstein interval로 계산한다.
실수·허수 signed interval 연산은 총 21모드를 더할 때마다
18자리 **외향** rational decimal로 제한하여 분모 크기를
제어한다. \(\sqrt{2\ell+1}\)은 integer square-root
directed interval을 사용한다.

또한 \(s^2=(r-R)^2+2rR(1-\mu)\)에서
\[
s_{\min}^2=\operatorname{dist}([a,b],R)^2+
2aR(1-m_1),\qquad
s_{\max}^2=
\max(|a-R|,|b-R|)^2+2bR(1-m_0)
\]
는 바른 외향 포함구간이다.
제곱근의 상하한은 정확한 integer `isqrt`로 만들고,
\(\exp(-s)\)는 양의 Taylor 부분합 및
양의 geometric tail의 역수를 쓴다.
\(q(s)\)는 위 Laplace integral로 **단조 감소**하므로
양 끝점의 유리수 \(e^{-s}\) 포함구간으로 제한한다.
\(U(s)\), \(S_0(r)(1-e^{-E(s)})\), \(E(s)/s\)는 signed interval
곱셈·나눗셈으로 외향 평가한다. \(s_{\min}>0\) 조건은
**ordinary joint cell에만** 필요하다.
\(r=R\) cusp 영역은 별도 PHYS38 logarithmic shell strip에
남기며 \(1/s\)를 임의로 smoothing하지 않는다.

한 cell에서 얻은 구간 \(G_\Re\in[L_\Re,U_\Re]\),
\(G_\Im\in[L_\Im,U_\Im]\)에 대해 \(q_\Re=\max(|L_\Re|,|U_\Re|)\),
\(q_\Im=\max(|L_\Im|,|U_\Im|)\)라고 하자.
원래 \(G=\sqrt{4\pi}\,\mathcal R\) 정규화에 의하여
\[
\boxed{
\|\mathcal R\|^2_{L^2(I_r\times I_\mu\times S^1)}
\le \frac{b^3-a^3}{6}(m_1-m_0)
 (q_\Re^2+q_\Im^2).
}
\]
모든 rational radial/angular cell이 서로 겹치지 않고
원래 strip을 정확히 덮으면 **양수인 이 cell bound의 합**이
인증 결과다. 유리수 변환 및 잘못된 단위는 허용하지 않는다.

## 3. Adaptive priority: selection은 휴리스틱, 인증은 수학적

`src/wu088_hh/phys42_adaptive.py`는
유한 개의 초기 angle cells를 시작으로 각 radial slab에서
\(q_I^2\times\text{exact volume}\) upper가 가장 큰 cell을
반씩 나눈다. 분할 전의 모든 leaf partition과 그 합은
독립적으로 타당한 인증이므로 새 분할의 upper가 우연히
증가해도 **과거 최소 certified sum**을 보존한다.
실제로 최소를 준 `best_rational_partition`의 각 rational
경계·cell squared upper를 기록한다. 최소값끼리의 결합은
동일 radial slab의 여러 완전한 인증 중 하나를 택할 뿐이고,
누락된 물리 source가 아니다. Priority는 최적성 보증이 아니다.

Source SHA 고정, 동일 정렬, Python `Fraction` 덧셈,
cached exact Bernstein transforms 및
\(P_\ell,T_\ell\) angular brackets, safe `forkserver`
worker별 독립 slab 로딩을 사용한다.
Native subagents는 미노출이라 NOT_RUN이고, worker는 subagent가 아니다.
Local Codex는 사용하지 않는다.

## 4. 실제 original-frozen local 계산

모든 행은 동일 반폭 \(\delta=1/1000\,a_0\).
독립 원본 PHYS40에서는 \(r=1\) 국소 strip upper
0.002232635336, \(r=1/2\)에서는 0.003100658335이었다.

| Center | Mesh | Cells at final partition | Certified broken L² upper |
|---|---|---:|---:|
| \(r=1\) | uniform 2×32 | 64 | 0.007394419346 |
| \(r=1\) | uniform 2×96 | 192 | 0.002488855287 |
| \(r=1\) | uniform 4×96 | 384 | 0.002403569362 |
| \(r=1\) | adaptive 4×96 | 384 | **0.001675179274** |
| \(r=1\) | uniform 4×192 | 768 | 0.001232249515 |
| \(r=1\) | adaptive 4×192 | 768 | **0.000880652956** |
| \(r=1/2\) | uniform 4×128 | 512 | **0.001060854548** |

PHYS40 동일 범위 대비 \(r=1\) adaptive192 upper는
약 2.54배 감소, \(r=1/2\) uniform128은 약 2.92배 감소.
동일 4×192 *최종 leaf budget*에서 adaptive는 uniform보다
약 1.40배 감소하지만, priority split의 parent+child
증명 비용은 더 높다.

원래 double64 모든 SCREENED s-coupled 연산자를 직접
평가하는 별도 NumPy/SciPy 3D Gauss preview는
\(r=1,\delta=.001\)에서 약 \(4.540073\times10^{-6}\),
\(r=.5,\delta=.001\)에서 약 \(1.499964\times10^{-6}\).
이 진단은 재현 가능한 exploratory 값이며
**절대로 rigorous interval의 한쪽 끝값으로 사용하지 않는다**.
최신 upper에도 약 194배/707배의 slack이 남아 있다.

## 5. 코드 실행·CAS·검증 근거

실제 Ubuntu/local Python3.12.3, NumPy2.4.2, SciPy1.17.0,
pytest9.1.1에서 실행. 기존 pyproject pin
numpy==2.3.5와 active 2.4.2의 환경 편차는 별도 기록하고
프로젝트 요구 버전을 임의로 변경하지 않는다.
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1`
고정. 독립 float64 진단에서는 이전 PHYS40의
실제 broadcast/einsum/Legendre vectorized kernel을 재사용했다.
공식 인증은 exact Fraction이며 float vectorization으로
강제 치환하지 않았다.

실제 4×192 동일 소스 인증은 1-worker **37.41 s**, 4-worker **25.81 s**
(`/usr/bin/time` wall, 약 1.45배 가속). 이 속도만으로
전체 산란 solver 성능이 개선됐다고 주장하지 않는다.
Adaptive 4×192 / 4-worker는 **46.77 s**로 균일 4×192보다
느렸지만 인증 상계는 0.001232249515에서 0.000880652956으로
감소했다. 이는 **동일 leaf budget의 정확도와 실행비용 trade-off**다.
parent-only RSS는 직렬 45772 KiB, 병렬 35820 KiB였고
자식 프로세스 RSS를 합산한 총량과 혼동하지 않는다.

실제 신규 코드:
- `src/wu088_hh/phys42_joint_interval.py`: exact rational interval,
  signed Bernstein angular/radial, exp/q/U source bounds,
  original full strong residual and volume enclosure, 1/4 workers.
- `src/wu088_hh/phys42_adaptive.py`: positive leaf heap,
  final/best exact partition, independent source-verified radial workers.
- `scripts/phys42_joint_strip.py`, `scripts/phys42_adaptive_strip.py`:
  runnable CLI and JSON witness outputs.
- `tests/test_phys42_joint_interval.py` 및
  `tests/test_phys42_adaptive.py`:
  exact interval corner extrema, exact sampled s bracket,
  exact \(\ell=0,1,5,11,20\) angular Legendre/T values,
  70-digit mpmath physical E/U/q/source interval inclusion,
  original full PDE NumPy quadrature diagnostics,
  frozen SHA, cusp rejection, angular partition exact coverage,
  adaptive historical minimum validity, invalid worker rejection.

2026-10-15 로컬 Wolfram/xAct에서
scalar exact identity 25/25 zero (원래 source split, s-Jacobian,
gradient/Legendre algebra, physical 3D measure 포함),
xTensor1.3.0 Euclidean vector-scalar Leibniz tensor 0를 획득했다.
**처음 xAct 시도는 wolframscript ToExpression의 닫는
bracket가 하나 초과하여 exit4**였고,
원인을 실제 bracket count로 확인해 문자열을 수리했다.
이전 실패를 물리 또는 수치 theorem REFUTED로 오분류하지 않고
`CAS_SCRIPT_SYNTAX_ERROR → REPAIRED`로 보존한다.
수정 후 exit0 및 `results/CAS_XACT.stdout` 기록을 사용한다.
전체 pytest는 실제 Ubuntu에서 **227/227 PASS, exit code 0**,
pytest 집계 150.33 s, shell wall 151.26 s로 끝났다.
원본 PHYS41 214개 + 신규 PHYS42 13개를 실행했다.
실제 stdout/resource는 `results/FULL_SUITE.{stdout,resource}`로 보존한다.

## 6. 다른 저장소 및 문헌 근거

2026-10-15 최신 읽기 전용 PR:
- [BASS_HE PR64](https://github.com/cosmosapjw-quantum/BASS_HE/pull/64):
  exact 16 warm P01 source cells, 2904-ray memoization; 동일 종류의
  exact caching/셀 checkpointing 패턴만 활용한다.
- [bass_cr PR71](https://github.com/cosmosapjw-quantum/bass_cr/pull/71):
  true child moment 기반 positive adaptive q grid;
  원래 photon number/energy moment를 HH에 이식하지 않고
  **positive interval cell heap** 설계와 fail-to-HOLD 논리만 재사용한다.
- [rei_bianchi PR119](https://github.com/cosmosapjw-quantum/rei_bianchi/pull/119),
  [PR120](https://github.com/cosmosapjw-quantum/rei_bianchi/pull/120),
  [PR121](https://github.com/cosmosapjw-quantum/rei_bianchi/pull/121):
  actual H/He source conservation, conditional P01 bridging,
  frozen AX03 Bianchi-I SI clock/transport supplier.
  PHYS42 원자 산란 인증은 AX08 signed q shear signal, P01 tau,
  REI ion fraction 어느 것으로도 즉시 consumer admission되지 않는다.

참고 원문:
Kyoko Makino, Martin Berz, "Taylor Models and Other Validated
Functional Inclusion Methods", IJPAM 4(4), 379–456 (2003);
Gordon, Jirauschek & Kärtner, *Physical Review A* 73 042505 (2006),
DOI 10.1103/PhysRevA.73.042505;
Feldkamp, *J. Chem. Phys.* (1996), DOI 10.1063/1.471754;
Kato cusp/modern coalescence e.g. arXiv:2204.09897.
문헌은 validated dependency suppression 또는 Coulomb cusp
방법론의 **문헌 지원**이지, 이 특정 Hamiltonian 인증값의
대리 검증이 아니다.

## 7. 명시적 평가 및 다음 DAG

이론 identity와 positive-volume cell-bound는
**DERIVED + WOLFRAM CHECKED**.
두 실제 noncusp strips의 원본 strong PDE 상계는
**NUMERICALLY CERTIFIED ON STATED INPUT/DOMAIN**.
Python frozen-input 실행 및 regression은
**IMPLEMENTATION VERIFIED** (종료 증거 별도).
Global angular/radial coupled annulus 6-panel 통합은
**UNRESOLVED**. Physical electron scattering outgoing
amplitude/cross section and HH thermal rate는 `null` / HOLD.

다음 최소 DAG:
`C7B_GLOBAL_SIGNED_JOINT_TILING_WITH_PHYS38_CUSP_LOG_PATCH`.
두 센터 비cusp 전 radial panels를 error-budget-guided signed
rectangular enclosure로 덮고, \(r=R\)와 dyadic interface
mismatch 주변 \([R-\delta,R+\delta]\)는 기존 PHYS38
positive-log finite strip에 결합한다.
\(L²\) upper가 PHYS39 `2.516921964597789440`보다
낮다는 실제 증거가 없으면 외부 발표에서 tight global claim을
금지한다. 계면 delta H⁻¹, origin \(r<r_0\),
screened exterior DtN, continuous low-Schur inverse 및
incoming adjoint는 별도 admission gate로 남긴다.
HH production/P01/REI default OFF, no merge/consumer transfer.
