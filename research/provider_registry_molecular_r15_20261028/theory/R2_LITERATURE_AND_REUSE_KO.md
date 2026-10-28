# R15 R2 — 원전·선행 결과와 재사용 범위

상태: **R2 근거 취득·재사용 종합 완료**. R15의 증명·CAS·수치 실행·독립 심사·채택은 이 문서의 완료와 구별한다. 저자 작업은 원문 읽기, 수동 수학 검토와 문서 작성이며 과학 실행은 0회다. 현재 알려진 게시 기준은 S01 `9003d45d710ac56497152055d31e2bef55f3f7fa`, 전체 DAG **29/46**이다. S02의 실제 게시·백업 영수증은 root가 별도로 기록한다.

## 1. 이번에 재사용하는 문제와 결과

R15의 입력은 각 exact rational source cell에서 주어진 네 개의 **원래 비음수 Bernstein-B3 계수**다. 이 표현을 통해 staircase kernel과의 global-memory convolution을 비음수 Bernstein-B4로 구성하고, 그 quartic의 whole-cell supremum을 유한 깊이·유한 작업량으로 둘러싼다. 이어 고정 signed scalar 계수에 대한 양의 degree-four exponential moments를 사용한다. Source 함수가 실제 fine/coarse domain forcing의 상계라는 전제와 full-generator contraction certificate는 입력 결속 사항이다.

직전 R14의 읽은 원본은 `inputs/R14_theory_PROOF_KO.md`의 §1, §3–4, §6–7, §9다. 그 원본의 결속은 R14 FINAL `6ca324dbc5d3c4b5c064f7621730eb0d6ee5eb51`, tree `1bcbb222a5d5c0791b46015116287917d9b84923`, science S09 `dfdefe47ef0c28ae94f6e6727d3230ceed5c356d`, 105-file scientific payload SHA256 `b68ab395e4e36ea7a6b49bb6c0b1f44fb75d10522f223d29657907179ac24e4b`다. 해당 파일은 이번 leaf에 보존되어 있다.

| 재사용 대상 | 실제로 읽은 위치·결과 | R15에서 유지할 조건 | 새로 처리할 차이 |
|---|---|---|---|
| Full-A 비교와 staircase memory | R14 §1: \(H=\pi d^\top-\operatorname{diag}(d)\), \(A_w=K+wH\), \(h(a)=q^{\lfloor a/\tau\rfloor}\) | 고정 K/π/d, 전체 w box, 모든 시작시각, zero-mass residual, 짧은 나머지의 nonexpansivity, \(h(0)=1\) | source 차수를 높여도 q/τ certificate의 family·state·clock 결속은 그대로 필요 |
| Rational translated event grid | R14 §3 | source knots의 \(k\tau\) 이동과 observation knots의 exact union; 원래 \(t_0\) history 보존 | quadratic effective-piece preprocessing을 사용하지 않고 원래 cubic source cells를 사용 |
| Exact positive overlap | R14 §3: fixed affine L/U/M, Simpson identity, Bernstein product | source-domain 내부 affine restriction, \(D=U-L\ge0\), 양의 원래 계수 | B1×B2의 cubic를 B1×B3의 quartic으로 직접 확장 |
| Actual endpoint와 left limit | R14 §3 | initial \(h(t-t_0)R_0\)의 jump와 연속 convolution을 구별 | B4 endpoint를 저장해 같은 규약 적용 |
| Independent original-integral route | R14 §4: \(J_m=\int v^m h(v)\,dv\) | production coefficient 조립을 import하지 않고 원래 source polynomial 적분 | m=0..2에서 m=0..3으로 확장 |
| Positive signed exponential propagation | R14 §6 | \(E=|\eta|\), coarse \(l^1=4E\), c≥0, 고정 signed \(d_c\), \(|d_c|T\le16\), outward arithmetic | B3의 네 beta moments를 B4의 다섯 moments로 직접 유도 |
| Whole-E comparison | R14 §7 | whole-R upper와 source whole upper로 상수 forcing majorant 구성; 다음 셀에는 별도 polynomial endpoint upper 전달 | B4 whole-R certificate를 입력으로 사용 |

R14의 full pointwise-nonnegative quadratic cone 전처리는 R15의 original-coefficient input cone을 대신하지 않는다. 예를 들어 \((u-1/2)^2\)의 degree-three Bernstein 계수는 \((1/4,-1/12,-1/12,1/4)\)다. 함수는 비음수지만 현재 original-coefficient 조건은 만족하지 않는다. 이 예는 명시한 입력 범위를 구별한다.

## 2. 실제로 읽은 수학 원전과 적용

### 2.1 Mourrain–Rouillier–Roy: Bernstein 표현과 restriction

원전: Bernard Mourrain, Fabrice Rouillier, Marie-Françoise Roy, **The Bernstein Basis and Real Root Isolation**, MSRI Publications 52 (2005), pp. 459–478. [원문 PDF](https://library.slmath.org/books/Book52/files/24roy.pdf).

실제 읽은 부분은 §2의 sign variation 정의, Proposition 2.3, Proposition 2.4, Proposition 2.8, Algorithm 2.9 및 correctness 절 진입부다. Proposition 2.3은 interval Möbius transform의 power coefficients와 Bernstein coefficients가 양의 binomial factors로 대응함을 설명한다. Proposition 2.4의 root count는 **open interval**에 대한 것이다. Proposition 2.8의 convex-hull bound와 Algorithm 2.9의 de Casteljau restriction은 quartic의 값과 restricted coefficients를 둘러싸는 데 직접 사용한다.

R15에서 적용할 조건은 exact rational interval, 유한 차수 polynomial, subdivision parameter 0≤θ≤1이다. De Casteljau의 convex combination은 양의 원래 계수를 보존한다. Cubic forcing의 affine image가 source cell 내부에 있으므로 overlap 조립에 적용할 수 있다. 실제 계산할 계수·구간을 이 조건과 연결하며 root-count theorem 자체를 whole-supremum certificate로 대신 쓰지 않는다.

### 2.2 Sagraloff: subdivision sign-variation inequality

원전: Michael Sagraloff, **When Newton meets Descartes: A Simple and Fast Algorithm to Isolate the Real Roots of a Polynomial**, arXiv:1109.6279v1 (2011-09-28). [원문 PDF](https://arxiv.org/pdf/1109.6279).

실제 읽은 부분은 interval variation의 정의, Descartes root bound의 설명, Theorem 2의 **P4** 및 주위 조건이다. P4에서 서로 겹치지 않는 두 subinterval에 대해

\[
\operatorname{var}(f,I_1)+\operatorname{var}(f,I_2)\le\operatorname{var}(f,I)
\]

를 재사용한다. Bernstein coefficient의 zero-dropping variation과의 연결은 위 Möbius coefficient relation이 제공한다. R15는 fixed depth의 function enclosure를 구성하므로 원전의 square-free root-isolation 종료·root-separation complexity 전체를 이식할 필요가 없다. Repeated root, splitpoint root, 실제 실근이 없는 mixed coefficients도 R15의 직접 보조정리에서 함께 처리한다.

R15의 \(3D\) split / \(6D+1\) visit bound와 \(M_B2^{-D}\) hull gap은 원전에서 그대로 인용할 결과로 취급하지 않는다. Derivative degree 3, exact midpoint subdivision, mixed-sign-only traversal라는 이번 설계에 대해 R5에서 직접 유도할 항목이다. R4에는 그 candidate argument를 제시한다.

### 2.3 Sharma: 표현 확인과 midpoint 규약 점검

읽은 자료: Vikram Sharma, **The Descartes Method for Real Root Isolation**, §3 Bernstein representation, derivative·endpoint·convex-hull·Möbius·de Casteljau 부분. [강의노트 PDF](https://www.imsc.res.in/~vikram/poly-2012/descartes.pdf).

이 자료는 같은 표현과 계수 규약을 교차 확인하는 데 사용했다. 검색으로 회수된 midpoint split parity 문구는 midpoint root의 multiplicity 항을 분리하지 않은 형태로 적용하지 않는다. 다음 간단한 exact 예에서 zero-dropping variation의 손실은 홀수다.

\[
f(u)=2u-1:\quad B=(-1,-1/3,1/3,1),\quad V(B)=1.
\]
\[
B_L=(-1,-2/3,-1/3,0),\qquad B_R=(0,1/3,2/3,1),
\quad V(B_L)=V(B_R)=0.
\]

이는 splitpoint root를 open-interval root count에서 제외하는 규약과 일치한다. R15는 midpoint multiplicity를 수반하는 별도 parity equality를 사용하지 않고 위 inequality만 사용한다. 이 점검은 회수된 표현의 국소 적용 조건 확인이다.

## 3. 표준 도구와 R15의 직접 구성 구분

Bernstein convex hull, de Casteljau, degree elevation, product identity, cubic에 대한 Simpson exactness, polynomial forcing의 exponential integration은 표준 도구다. R15의 연구 단위는 다음 연결과 유한 계약을 실제로 완성하는 것이다.

1. Exact nonaligned clocks에서 original positive B3 source를 B4 global-memory polynomial로 한 번 조립한다.
2. Derivative-B3의 mixed-sign leaves만 세분해 depth96까지의 방문 수를 사전 제한한다.
3. Root separation 없이 unresolved mixed leaves의 coefficient hull로 명시적 whole-cell gap을 증명한다.
4. 고정 signed \(d_c\)에 대한 B4 moments를 positive series와 reflection으로 계산하고 whole-E/endpoint 결과를 연결한다.
5. 원래 unsplit monomial 적분과 power-polynomial reference로 다른 계산 경로를 만든다.

이 단위의 신규성은 WU의 현재 입력·메모리·표현·finite-budget 계약을 완성하는 데 두며, 관련 알고리즘 전체의 학술적 최초성은 주장하지 않는다. 전역 불가능성/no-go 주장은 이번 문서에 없다.

## 4. 최신 소스 조사에서 전이할 수 있는 것

현재 accessible owner metadata census와 선택한 immutable source 본문의 결과는 `authority/intake/SYNTHESIS_KO.md`, `authority/intake/github/SYNTHESIS_KO.md`, `authority/intake/pr/SYNTHESIS_KO.md`, `authority/intake/backups/SYNTHESIS_KO.md`에 결속되어 있다. 전체 metadata 열람 범위와 실제 과학 본문 열람 범위는 그 문서에서 분리한다. 다른 repo에서 확인된 endpoint·static-lapse·source-point validation은 그 소스의 조건부 결과로 보존한다. 해당 결과만으로 WU의 full-A family/state/clock certificate나 실제 HD reactive array 결속이 새로 확보되지는 않았다.

Root가 확보한 GL2022 원문 맥락 및 검색 결과는 실제 native reactive array 파일 회수와 별도로 기록한다. 현재 이 연구 단위의 physical input은 `INPUT_PENDING_IN_INSPECTED_SCOPE`, native v는 `UNSPECIFIED`다. 실제 source array와 named consumer/state/density/clock를 회수하면 정확한 source identity와 기존 수학 전제를 대조하는 후속 결속으로 이어진다. `MISSING_NOT_ZERO`, TIQM/SQM 구별, HH_R10 OFF, production NOT_ISSUED, L4 false, central/physical delta 0은 유지한다.

## 5. 실제 읽기·작성 범위와 단계 경계

원문 회수 raw는 `r15_work/private/primary_fetch.json`에 보존되며 공개 산출물에는 원문 전체를 복제하지 않는다. Discovery 기록은 `r15_work/private/math_scispace.json`, `r15_work/private/math_exa.json`이다. 이 문서는 위에 적은 원전 passage와 baseline proof를 읽어 재사용 조건을 연결했다. 새 broad survey, 과학 Python/import/compile, CAS, ODE, remote write는 수행하지 않았다.

`skill_context_used`:

- `r15_work/skill_context/SKILL_1_0_0.md`: 사용자가 선택한 full R1–R10/C1–C10 구조.
- `r15_work/skill_context/SKILL_1_3_0.md`: 현재 통합 정책.
- `r15_work/skill_context/references/THEORY_LOOP.md`: R2 원전·재사용 종합, R3 주장 구별, R4 구체식·대표 예제.
- `r15_work/skill_context/references/RESEARCH_POLICY.md`: 직접 진술, 구성적 연결, strong no-go 구분.
- `r15_work/skill_context/references/POLICY_INTEGRATION.md`: 단계·실행·심사 경계와 실제 영수증.
- `r15_work/skill_context/references/EVIDENCE_AND_HANDOFF.md`: typed identity와 실제 실행/저장 근거 구분.
- `r15_work/skill_context/references/SUBAGENT_MODE.md`: root의 제한된 authoring 위임과 단일 외부 쓰기 소유권.

R2의 결과는 R3의 주장 장부와 R4의 구성 선택에 투입한다. Full proof와 CAS source의 R5 작성은 root의 다음 단계 인계 후 수행한다.
