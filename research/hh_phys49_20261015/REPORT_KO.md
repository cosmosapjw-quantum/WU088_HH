# WU088_HH PHYS49: 원래 H-H screened Coulomb 고차채널 Dirichlet 역연산자

2026-10-15 KST. 기존 [PHYS48 PR87](https://github.com/cosmosapjw-quantum/WU088_HH/pull/87)
HEAD 4bb2e3e0574c3d6a47850eb319ae31e5382561c7의 후속 R5+C5/C6/C7/C8.
원래 `h=-Delta/2-1/r-(1+1/s)exp(-2s)`, `s=|r-R zhat|`,
R=kappa=7/10, 원자 단위 a0와 Ea=2I0, 스핀/입사 source
`eta=F*y`, `xi=F*y-phi`는 변경하지 않았다.
원본 1386 complex128, 21-mode six-panel frozen NPZ SHA256:
`f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`.
원본은 r<=20까지만 저장됐으며, 이 연구에서 r>20의
물리적 trial을 발명하거나 연장하지 않는다.

## 1. Constructive infinite-angular Dirichlet collar theorem

범위는 r in [20,27] a0, radial 양끝에서 **고차채널의
Dirichlet trace가 0**인 함수공간 `L2(dr; l2 over ell>=21, all m)`.
저차 P= P_(ell<=20), 고차 Q=I-P를 쓰고 유한구간 고차
Coulomb 기준 연산자를 다음처럼 정의한다.

```
A0_high=Q[-d²/dr² + ell(ell+1)/r² -2/r - kappa²]Q
A_high=A0_high-2 Q S(s) Q
A_high u_high = 2 Q S(s) P u_low
```

원래 screened potential S(s)=(1+1/s)exp(-2s)이고
원래 3차원 angular 정규화 Y_lm와 모든 m에서 성립한다.

r<=27, ell>=21이므로 ell(ell+1)>=462>r,
barrier가 단조감소하여
`ell(ell+1)/r²-2/r-49/100 >= 1693/24300>0`.
두 양끝 고차 Dirichlet 조건에서는 Poincare의
`pi²/(27-20)² >9/49`를 적용할 수 있으므로,

```
lambda0 = 9/49 + 1693/24300
        = 301657/1190700 = 0.253344251280759... .
```

이는 ell>=21 **무한 angular block 전체에 공통**인
정확한 유리수 lower form bound다. 실제 물리 potential의
양의 scalar supremum은 r>=20, s>=19.3에서

```
delta = 2(1+1/(20-0.7))*exp[-2(20-0.7)]
      < 3.624112937975321688970e-17 .
```

이 지수함수의 upward upper는 PHYS45의 동일 원본
192항 positive Taylor reciprocal + 엄밀 remainder를
Fraction으로 재사용한다. QSQ operator norm은 delta 이하,
thus `q=delta/lambda0 <1`이며 bounded perturbation
and positive-form/Friedrichs inversion yields a unique
**zero-Dirichlet** high-ell solution with

```
||u_high||_(L2(dr angular)) <= alpha ||u_low||
alpha = delta/(lambda0-delta)
      <= 1.430509245682087984816e-16 .
```

이것은 고차모드를 임의 finite ell로 잘라 얻은 수치
실험이 아니라 **all ell>=21, all m** coercive theorem이다.
단 원래 outgoing Coulomb boundary trace는 일반적으로
0이 아니므로 전역 물리해에 무조건 적용하지 않는다.

## 2. PHYS47 original Bernstein tail와 intermediate scattering

N>0, 중간 M=ell21..20+N과 T=ell>20+N을 분리한다.
PHYS47의 원래 screened positive angular Chebyshev
상계에서 `eps_N = ||2 Q_T S P||`는
`2*PHYS47.rho_prefactor(rho)*rho^-N` 이하이며,
25개 원본 admissible 정수 rho=4..28 중 최소인 값을 택한다.
이는 본래 PHYS47의 **radial integral +2S upper**를
collar의 **pointwise +2S upper**로 변환하면서 필요한
계수 2를 명시적으로 보존한 값이다.

전체 고차 응답 `||u_M||<=||u_high||<=alpha||u_low||`,
그리고 `lambda_T>=9/49 +(21+N)(22+N)/27²-2/27-49/100`
를 사용하면 Schur block equation
`A_TT u_T = 2 Q_T S P u_low +2 Q_T S Q_M u_M`에서
다음 포함구간을 얻는다.

```
||u_T|| <= (eps_N+delta*alpha)/(lambda_T-delta) ||u_low||.
```

이때 intermediate multi-hop 21..20+N 경로가 존재하므로
원래 PHYS47 직접 coupling만으로 full response를
과소평가하지 않는다.

선택된 exact rational upward bounds:

| 출력 high ell | 원래 전체 screened Dirichlet collar L2 gain upper |
|---:|---:|
| ell>=21 | 1.430509245682087984816e-16 |
| ell>=25 | 5.335610727928371135709e-19 |
| ell>=29 | 6.447104670595219190848e-23 |
| ell>=33 | 2.185562821537284543108e-27 |
| ell>=37 | 3.673102035286166988943e-32 |
| ell>=41 | 2.616352402209727124725e-33 |
| ell>=61 | 1.078376869645499710182e-33 |

ell>=41에서는 direct 2S coefficient <=6.01347e-37이지만
ell21..40을 거친 간접 source 때문에 rigorous propagated
Dirichlet bound가 ~2.61635e-33으로 더 크다. 이는
중요한 물리적/수학적 차이다. 해당 상계는 u_low가
이 구간에서 임의로 주어졌을 때의 조건부 결과이지,
frozen 원본의 영역 밖 이력을 관측하거나 재현한 값이 아니다.

## 3. 독립 수치 검산 및 실측 최적화

`src/wu088_hh/phys49_dirichlet_collar.py`:
원래 SHA lock, exact-rational positive spectrum, 보존적인
upward scientific bounds, PHYS47 원래 analytic source
coefficients 및 1-/2-worker science parity.

`scripts/phys49_dirichlet_preview.py`: 별개
NONCERTIFYING finite-difference m=0 high ell21..28,
low ell20 manufactured `sin(pi(r-20)/7)`, r20..27
**zero Dirichlet high boundary**. 원래 실제 screened
angular potential, GL128/256 angular, radial 32/64/128
격자, SciPy sparse solve + lowest spectral eigensolver 사용.
이 수치 시험은 frozen physical low-u extension이 아니다.

| Radial interiors | Angular nodes | Numerically min eigen | high/low L2 response |
|---:|---:|---:|---:|
| 32 | 128 | 0.457834177375251 | 2.3667178056416683e-19 |
| 64 | 128 | 0.457979329963611 | 2.3644806208223073e-19 |
| 64 | 256 | 0.457979329963586 | 2.364480620821446e-19 |
| 128 | 192 | 0.458016930693380 | 2.3638228879285145e-19 |

수치 출력은 해당 무한 angular bound보다 작지만
유한 격자 분해능 자체는 수학적 enclosure가 아니다.

로컬 Wolfram 15과 연결된 Wolfram evaluator는
`1693/24300`, `301657/1190700`,
원본 Coulomb barrier derivative, Poincare sine mode,
screened q와 alpha 및 ell41 intermediate Schur tail을
독립 검사했다. Local CAS exit0. Python PHYS49 표적
19개 통과, 전체 WU088_HH **333/333 passed**,
pytest 206.12s exit0. Runtime NumPy 2.4.2 vs 원 프로젝트
고정 pin 2.3.5 차이를 공개한다.

Matched CPU benchmark:
- PHYS49 exact-rational N20, 모든 25 rho 검색 대비
  이미 인증된 rho18만 고정 재계산은 **3.14x**
  (동일 정확도·같은 N20 bound, 다른 이전 N 값은 탐색하지 않음).
- 별도 NONCERTIFYING 원래 screened 64 radial × 128 mu,
  8×8 angular Gram same quadrature: NumPy batched product
  vs explicit pairwise sum 약 **59.20x**, 최대 차이
  3.08e-33 atomic units.
- 이 값은 전체 원래 WU 산란 solver나
  rei_bianchi native H/He/Thomson solver의 가속이 아니다.

## 4. Cross-repo science intake and next obligation

최신 rei_bianchi PR141과 PR142는 현재 실제 source-driven
H/He–gamma/nu–Einstein Sigma/pi background를 짧은
고온 near-z4 시나리오에서 결합하고 있다.
그들은 original external H-H microscopic thermal rate를
공급하지 않으며, 초기 cold z20 physical EoR 전체 이력도
완료하지 않았다. 원래 private owner checkout의
HEAD 0fcb2dddf5de6b583c2e00f150abff0b2afb6315와
saved AX08 checkpoint는 이 연구가 변경하지 않았다.

PHYS49의 결과는 원래 물리 방향을 유지하는 조건부
**finite radial Dirichlet coercive infinite-angular response**이다.
실제 Coulomb radiation boundary를 가정한 outgoing Green
kernel, 원점 정칙 extension, physical source xi=Fy-phi,
incoming adjoint, sigma(E)와 identical-pair Maxwellian
k_HH(T)를 인증했다고 할 수 없다. 따라서
rei_bianchi HH_R10 production OFF.

다음 PHYS50은 r20과 r27의 고차 boundary trace 및
Dirichlet-to-Neumann lifting을 실제 outgoing Coulomb/Jost
outer solution에 연결하는 것. 이 때 PHYS48의 Coulomb
barrier action, PHYS47의 direct angular tail과 이번
coercive inverse를 조합해 boundary residual 및 global
Schur norm을 인증해야 한다. 이후에 물리적 collision
rate source와 REI proper-time consumer ownership을 다룬다.

핵심 참고: NIST DLMF Coulomb special-function Wronskian
33.2, Zhao–Wang–Xie (2013) analytic Bernstein ellipse
Chebyshev/Jacobi bounds, PHYS47 exact source-authored proof.
Chung (2024) regular Coulomb F bounds는 outgoing
irregular Coulomb G의 고차 장벽을 자동 통제하지 않는다.

Local Codex NOT_USED, native subagent NOT_RUN (not exposed).
