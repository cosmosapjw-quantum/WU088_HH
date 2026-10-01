# G1 — implementation에 필요한 정리와 정확한 적용 범위

검토 기준은 현재 branch의 parent commit `393eb882f7fbf160cfb465849d9652c7b026b5be`에 보존된 source-functional map 및 endpoint theorem review다. 기존 accepted A–E, epsilon/Gram 정리는 재증명 대상으로 돌리지 않았다. 아래 결과는 그 정리를 실행 코드에 연결하는 추가 lemma다. 모든 계산 예는 synthetic exact rational/polynomial이며 실제 Frozen107 입력·B192 배열·HH integrand를 평가하지 않았다.

**결론:** 선택된 continuous-target route의 수학적 적용 lemma는 아래 명시된 전제하에 PROVED다. 원 소스의 ideal algebra와 target의 대응은 exact source bytes를 읽고 확인했다. 새 callback의 실제 코드 및 pinned backend binding, 실제 endpoint/interior/final-D 수치 enclosure, feasibility, 최종 decision review는 각각 별도 gate다. 여기서 `certified_epsilon=null`, `certified_eta=null`, `rigorous=false`를 유지한다.

## 1. SSOT와 정확한 target — G1-01

대상은 stored Frozen107 bits의 정확한 실수 lift에서 정의한 continuous O/G와 source-prescribed D assembly다. finite quadrature/floating producer와 continuous integral을 같다고 놓지 않는다. 실제 producer discrepancy 전체는 나중의 final D-ball 대 raw-array 비교에 들어간다.

직접 읽은 원본은 `research/r31an_reference_certification/ncp_preflight_20260930/source_snapshot/` 아래 다음 네 파일이다. 새로운 수치 실행 없이 bytes와 SHA256를 확인했다.

| 파일 | SHA256 | 의미 대응 |
|---|---|---|
| `completion/mixed_h/h0_fused.cpp` | `d019713f8a9c6e864d60cc796104a0cdef629e491e6ab8de757995aa4f3672f2` | Gaussian geometry, O, negative center derivatives |
| `completion/mixed_h/od_run.py` | `63c0925ff938340feceb5768aba40da348b3afe323214a9792012e9d0bbc664d` | 47×2 registry, orbital contraction, parity, phase, D assembly |
| `exact_weights/exact_laplace_weights.py` | `8ad5273551728a3608b5f8d43ea77f732aebeddc96bea767be0f79206fcc39eb` | signed Hermite densities, weighted UU plane, direct monomial C |
| `completion/radial/DERIVATION.md` | `3214cdaf252ce3ea48026df643aaedae37674753f6f99746c9c3aaa30b9bdc70` | exact radial target and analytic derivatives |

`h0_fused.cpp`의 `rad[p+1]`, `rad[11+p]`, `rad[21+p]`는 p=0,…,8에 대해 각각 M_p, ∂s M_p, ∂s² M_p다. `ww[p*nn+ij]`는 UU contraction이며 O/G에서는 다른 VU/UV plane을 쓰지 않는다. `der[4]`, `der[5]`는 각각 d1z,d2z 미분이고 `vals`에서 부호를 바꿔 G1,G2를 만든다. `od_run.calc`는 그 O/G1/G2만 export한다. `assemble`의 active XOR cusp, p reflection 및 G extra minus, phase와 conjugation 위치도 map과 일치한다. 수학적 동일성은 이 ideal algebra의 의미에 관한 것이며 legacy special-function approximation의 정확성·quadrature exactness·bit equality를 주장하지 않는다.

## 2. 미분과 적분 교환 — G1-02

전제는 μ>0, a,b>0, 유한 비음수 정수 donor degrees, 실수 centers와 wave numbers다. d1,d2의 작은 compact real neighborhood를 잡아 D1,D2의 공통 상계를 둔다. Gaussian에 대한 center 미분은 유한 차수 다항식을 곱한다. pz의 polynomial 미분까지 포함하면 이미 accepted Gaussian majorant의 P_G1/P_G2가 neighborhood 전체를 지배한다. Hermite signed density의 finite absolute envelope 및 그 전체 양의 축 적분 상계는 유한하다. 따라서 absolute Fubini와 dominated differentiation을 순서대로 적용하여 공간 적분과 t,u 적분 모두에서 한 번의 center 미분을 교환할 수 있다.

q1,q2는 center 미분 동안 고정한다. v,z 또는 phase를 동시에 미분하는 다른 target에는 이 lemma를 그대로 적용하지 않는다. pz의 부호는

`-∂d[(r_z-d) exp(-a|r-d|²)] = [1-2a(r_z-d)²] exp(-a|r-d|²)`

이므로 +1 항이 필수다. px에는 그 delta 항이 없다. 실제 입력에서 majorant가 작을지는 이 존재·교환 정리와 별개다.

## 3. Radial continuation과 r=0,1,2 — G1-03/G1-04

`A=a+t`, `B=b+u`, `σ=(1/A+1/B)/2`, `δ=m1-m2`, `s=δ·δ`에서 dot은 bilinear다. Hermitian norm을 사용하면 complex analyticity를 깨고 target도 바뀐다. Re(A),Re(B)>0이면 Re(1/A),Re(1/B)>0이므로 Re(σ)>0이다.

실수 양의 A,B와 실수 Gaussian mean에서 noncentral radial Gaussian moment의 식이 성립한다. 양변을 Gaussian의 linear source parameters에 대한 entire functions로 본다. 공간 적분 쪽은 compact complex source set에서 Gaussian times exp(linear growth)로 지배되고, special-function 쪽은 1F1의 entire argument dependence로 entire다. 각 source coordinate에 대한 identity theorem을 반복 적용한 다음 A,B의 오른쪽 반평면으로 analytic continuation한다. 이 방법은 공간의 비해석적 `|r1-r2|^k`를 complex contour로 이동시키지 않는다. 따라서 실수 q가 만드는 complex means 및 허용된 complex t,u box에도 같은 표현을 쓴다.

고정 σ에서

\[
M_k=(2σ)^{k/2}\frac{Γ((k+3)/2)}{Γ(3/2)}\,{}_1F_1(-k/2;3/2;-s/(2σ)),
\]
\[
∂_s^rM_k=(2σ)^{k/2}\frac{Γ((k+3)/2)}{Γ(3/2)}
\frac{(-k/2)_r}{(3/2)_r}\left(-\frac1{2σ}\right)^r
{}_1F_1(-k/2+r;3/2+r;-s/(2σ)).
\]

분모 parameter는 3/2,5/2,7/2여서 pole이 없다. 1F1 power series의 coefficient를 r번 미분하면 rising-factorial factorization으로 위 식을 얻는다. entire series이므로 compact s-domain에서 termwise differentiation이 가능하다. s=0에서도 그대로 finite하며 s 또는 sqrt(s)로 나누지 않는다. k=0,r>0 및 k=2,r=2의 zero Pochhammer는 정확한 0으로 먼저 반환해야 한다. 0에 nonfinite special-function result를 곱해 얻는 NaN은 증명이 아니다.

짝수 k의 독립 확인식은 M0=1, M2=s+3σ, M4=s²+10σs+15σ², M6=s³+21σs²+105σ²s+105σ³, M8=s⁴+36σs³+378σ²s²+1260σ³s+945σ⁴다. exact coefficient tests 및 독립 Cartesian Gaussian moment expansion이 이를 확인했다. odd k의 전체 함수를 synthetic polynomial test만으로 검증했다고 주장하지 않는다; 그 일반성은 위 analytic series proof에서 나온다.

FLINT 3.4.0의 보존된 공식 D08 문서에 따라 `acb_hypgeom_m(..., regularized=0, ...)`만 이 1F1 convention이다. regularized=1은 Γ(b)로 나눠 다른 함수를 만든다.

## 4. 명시적 O/G callback algebra — G1-05

`h1=a/A`, `h2=b/B`, `n1=m1-d1`, `s1=2h1δz`, `s2=-2h2δz`와

\[
L_1=2a n_{1z}=h_1(-2td_{1z}+iq_1),\quad
L_2=2b(m_{2z}-d_{2z})=h_2(-2ud_{2z}+iq_2)
\]

를 정의한다. Gaussian base product를 B0라 하고 `F_s=M`, `F_pℓ=n1ℓ M+(δℓ/A)M'`로 둔다. σ는 이 center 미분에서 일정하므로

\[
∂_1F_{pℓ}=\delta_{ℓz}(h_1-1)M+n_{1ℓ}M's_1
 +\delta_{ℓz}(h_1/A)M'+(δ_ℓ/A)M''s_1,
\]
\[
∂_2F_{pℓ}=n_{1ℓ}M's_2-\delta_{ℓz}(h_2/A)M'
 +(δ_ℓ/A)M''s_2.
\]

s channel에서는 `∂jF_s=M'sj`다. 최종 `O=B0 F`, `G_j=-B0(L_jF+∂jF)`가 된다. product/chain rule과 source `der[4]/der[5]`의 항별 대응으로 증명했다. 9개 formal variable polynomial ring에서 M(s)=s^n,n=0,…,4를 직접 미분한 결과와 위 식의 모든 coefficient를 비교했다. tests는 source module을 실행하지 않는다.

## 5. Box guard와 nested uniformity — G1-06/G1-07

각 closed input box에서 Re(t),Re(u)의 **lower bound**가 strict positive이어야 하며 Re(A),Re(B),Re(σ)와 모든 division/power domain도 box 전체에서 증명한다. midpoint positivity는 충분하지 않다. principal powers는 오른쪽 반평면에서 단일 holomorphic branch다. outward interval dependency 때문에 σ의 단순 enclosure가 왼쪽까지 넓어지면 subdivision 또는 더 강한 domain proof를 요구한다. invalid callback으로 계속하지 않는다.

compact product domain에서 위 Gaussian domination은 uniform이므로 jointly holomorphic f(t,u)에 대해 `H(t)=∫[lu,Tu] f(t,u)du`가 holomorphic이다. outer callback에 box Z가 들어오면 inner evaluation은

`{H(t): t in Z} ⊆ returned complex ball/rectangle`

를 만족해야 한다. parameter Z를 그대로 inner callback에 전달하고 모든 inner arithmetic/enclosure를 Z 전체에 대해 수행하는 구성은 이 포함관계가 유지되는 한 허용된다. 매 호출의 partition이 달라도 set inclusion은 유지된다. outer midpoint에서 한 번 계산한 inner result는 이 조건을 충족하지 않는다. f(t,u)=t, u∈[0,1], Z=[0,2]만으로 midpoint value 1이 전체 image [0,2]를 담지 못하는 반례가 생긴다.

FLINT D07의 callback `order=1`은 함수값과 해당 input box에서의 holomorphy를 요구한다. radial derivative r=1을 요구하는 의미가 아니다. order>1은 Taylor coefficients 미구현이면 모든 requested output coefficient를 nonfinite로 처리하고 로그에 남긴다. return code만으로 실패를 전달하지 않는다. inner/outer requested tolerance는 certificate radius가 아니며 finite returned enclosure 자체를 검사한다. parameter width 때문에 inner range가 좁아지지 않는 경우는 resource/feasibility 문제다.

## 6. Endpoint convention과 enclosure geometry — G1-08/G1-09

accepted density term `e^{-λ/t} A t^{-ν}`, λ=μ²/4>0, ν>1에 대해 lower cutoff ℓ>0에서

\[
\int_0^ℓ e^{-λ/t}t^{-ν}dt=λ^{1-ν}Γ(ν-1,λ/ℓ)
\]

다. y=λ/t 치환 시 limit가 ∞에서 λ/ℓ로 바뀌고 orientation이 뒤집혀 **upper** incomplete gamma가 나온다. FLINT D08의 `gamma_upper(..., regularized=0, ...)`와 일치한다. 여기의 ν−1은 양의 half-integer이며 양의 recurrence `Γ(s+1,x)=sΓ(s,x)+x^s e^-x`를 쓸 수 있다. Γ(1/2,x)≤e^-x/√x는 x>0에서 적분 integrand의 u^-1/2≤x^-1/2로 바로 나온다. 따라서 exact rational/outward elementary upper evaluator도 타당한 대안이다.

upper cutoff T에서 `(a+t)^(-3/2)≤t^(-3/2)`를 써 `T^(-ν-1/2)/(ν+1/2)`를 얻는다. interior mass의 upper gamma difference는 `Γ(ν−1,λ/T)−Γ(ν−1,λ/ℓ)` 순서다. outward subtraction이 너무 넓어지는 것은 불확실성이지 음의 적분이 아니다. whole-domain upper W와 endpoint upper S를 빼 `J=W−S`로 interior upper를 만들면 일반적으로 틀린다. J는 자체 상계로 계산한다.

2D complement는 `(E_t×all_u) disjoint_union (I_t×E_u)`라서 `C_F(S_tW_u+J_tS_u)`로 bound한다. corners를 두 번 더하지 않는다. 이 scalar bound B는 complex modulus에 대한 bound이므로 endpoint residual disk `|e|≤B`를 뜻한다. Arb rectangular representation에서는 각각 real/imag radius에 B를 더해 포함시킬 수 있다. 반대로 rectangle radii rx,ry를 disk로 바꾸려면 `sqrt(rx²+ry²)`의 outward upper가 필요하다; max(rx,ry)는 (rx,ry) corner를 놓친다. 이 사각형→disk 전환으로 생기는 최대 √2 과대평가는 validity에 영향을 주지 않으며 width accounting에는 기록한다.

## 7. Exact lift, finite contraction, phase/conjugation — G1-10/G1-11

stored C, pref, v, phase_E, orbital coefficients, exponents는 exact represented reals다. z=3/4와 tau=(3/4)/v는 rational operations로 정의하며 v≠0이다. donor rational C나 새 normalization certificate로 stored bits를 교체하지 않는다. ideal normalization `sqrt(2)*pref*(2a/pi)^(3/4)*(2b/pi)^(3/4)` 및 p-channel `2sqrt(a)`는 이 exact inputs에서 outward 평가한다. 역사적 rounded normalization 또는 rounded tau를 target으로 재사용하는 것은 다른 target을 만들 수 있다.

유한 scalar contraction `y=Σw_jx_j`에서 exact w_j와 `|x_j−c_j|≤r_j`이면 `|y−Σw_jc_j|≤Σ|w_j|r_j`다. w_j 자체가 ball이면 `|w_jc_j−ŵ_jĉ_j|≤|ŵ_j|r_x+|ĉ_j|r_w+r_wr_x` 또는 ball multiplication으로 처리한다. 전체 연산을 outward ball로 수행하고 final D radius에서 추출하면 중간 radius를 별도로 다시 더하지 않는다.

real phase angle의 exact exponential은 unit modulus, ±1 parity도 isometry, conjugation은 complex modulus isometry다. angle uncertainty는 outward exp/multiplication 안에서 이미 반영한다. 이산 row contraction 및 phase를 끝낸 real-positive-domain O/G 결과에 source formula대로 conjugation을 적용한다. complex t,u callback 안의 literal conjugation은 antiholomorphic다. reflected continuation은 이번 구현 계약에 넣지 않는다.

기존 epsilon theorem에 의해 final D entry balls로 raw discrepancy를 bound하고 Frobenius bound로 spectral ε_C,ε_R를 얻는다. finite contractions의 cancellation을 midpoint 관찰만으로 radius에서 빼지 않는다. old X0…X8 항도 final raw-comparison epsilon에 다시 더하지 않는다.

## 8. Strict Pareto sufficient condition — G1-12

exact represented gap interval이 `[g_-,g_+]`이고 같은 metric의 source perturbation bound가 ε이면 true continuous-target gap의 lower bound는 `L=g_-−2ε`다. 이는 두 candidate error가 각각 ε 이하 변한다는 reverse-triangle estimate에서 나온다. K에는 `(ε_C+ε_R)/2`, Dmax에는 `max(ε_C,ε_R)`를 쓴다. max의 active block을 고정할 필요가 없다.

두 metric 모두 `L_j≥−tol`, 적어도 하나가 `L_j>tol`이면 exact-real frozen Pareto rule의 sufficient condition이다. strict `>` 경계에서 equality는 통과하지 않는다. legacy gap ĝ를 audit할 때 η=max(|ĝ−g_-|,|ĝ−g_+|)는 `ĝ−η≤g_-`를 보장하므로 conservative lower가 된다. η를 실제 certificate 없이 0으로 놓지 않는다. arithmetic tolerance의 exact authority는 원 comparator의 binary64 bits를 별도 기록해야 한다. real mathematical rule 충족과 original floating comparator의 instruction-level predicate 재현은 다른 claim이다. 이 theorem helper는 frozen comparator를 교체하지 않는다.

## 9. 실행 검산과 남은 의무

`python -m unittest discover -s theorem_checks -p 'test_*.py' -v`로 15개 synthetic exact tests를 실행했다. polynomial coefficient equality, independent Gaussian moments, upper-gamma orientation, strict boundary 및 rejection cases를 포함한다. test receipt는 `theorem_checks/VERIFICATION.json`에 있으며 원 과학 suite의 test count와 합치지 않는다. SymPy가 현재 Python과 primary runtime 모두에 없어 표준 라이브러리 Fraction polynomial ring을 사용했다. 이 환경 의존성은 수학적 blocker가 아니다.

남은 것은 `REMAINING_THEOREM_OBLIGATIONS.json`의 구현·실행 binding이다. G1 수학적 implication의 closure만으로 B01 전체, B02, B04 actual execution, B05 feasibility 또는 rigorous source reference certification을 닫지 않는다. G6 actual HH pilot/full-D workload는 별도 numerical authorization에 따라야 한다. 독립 분업 검토 및 exact tests도 프로젝트의 admitted final decision reviewer를 자동 대체하지 않는다.
