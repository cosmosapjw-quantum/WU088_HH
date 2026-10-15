# WU088_HH PHYS40: 원래 two-centre 연산자의 일반 반경 전체 angular-coupling 인증

2026-10-15 KST. 정확한 시작점은 PHYS39 draft PR #78, commit `c5ce4c7a9698658156f7972f1f5ebf7c62a71443`. 이번 실행의 선택된 R5/C7B 결과는 **`C7B_GLOBAL_RADIAL_SCREENED_COUPLING_AND_OUTGOING_DUAL`의 구성적 부분 단계**, 즉 **모든 유리수 고정 반경에서 전체 screened angular PDE residual을 직접 인증하고, spectator coalescence와 떨어진 유한 부피 radial strip까지 이어 주는 것**이다. 코드·실제 Ubuntu 로컬 실행·Wolfram/xAct·회귀시험을 수행했으며, 별도 Codex는 사용하지 않았다. 원래 전체 radial continuum, origin, screened outgoing boundary, low-Schur inverse 및 physical amplitude는 아직 열린 의무다.

## 1. 원래 물리 및 단위

고정 frozen-direct spectator H(1s)+H(1s) Hamiltonian:
[
h_\lambda=-\frac12\Delta-\frac1r-\lambda(1+s^{-1})e^{-2s},\quad
s=|\mathbf r-R\hat z|,\quad R=\kappa=\frac7{10},\quad\lambda=1.
]
전자 공간 Euclidean, 우주론 배경 signature (-,+,+,+). 길이단위 a0=5.29177210544e-11m, 에너지 Ea=2I0, 원자 공급 ionization I0=13.605693122990 eV와 수신 heating chiH=13.598434599702 eV는 구분. c, ℏ, kB는 무단으로 1로 두지 않는다. 초기 1s orbital φ=e^{-r}/√π, Coulomb final-state phase, 원래 (S(R)-S(s)) transition, source lift `eta=phi+lambda xi=F y`, `F=e^{lambda e^{-s}}`를 고정한다. 충돌 event/tag 및 생산·재이온화 HH OFF 상태도 변경하지 않는다. 입력 frozen trial은 `FROZEN_U_SUBSET.npz` SHA256 `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`; 21 partial waves, 6 radial panels, 11 node per panel, 1386 complex values. PHYS36 parent source/h operator, PHYS37/38 cusp+interface, PHYS39 exact source and K_lm을 같은 identity로 사용한다.

## 2. 새 R5 정리: 완전 결합 screened angular norm을 일반 r에서 다항식으로 인증

`D_lu_l=u_l''+(κ²+2/r-l(l+1)/r²)u_l`, `α_l=√(2l+1)`,
`μ=(r²+R²−s²)/(2rR)`라 두고
```
A(s)=Σ α_l[D_lu_l(r)/r] P_l(μ)
B(s)=Σ α_l[u_l(r)/r] P_l(μ)
C(s)=Σ α_l[u_l'(r)/r−u_l(r)/r²] P_l(μ)
T(s)=Σ α_l[u_l(r)/r] l[P_(l−1)(μ)−μP_l(μ)]
H(s)=(r−Rμ)C(s)−(R/r)T(s).
```
물리 strong residual `mathcal R`를 `G(s)=√(4π)mathcal R(r,μ(s))`로 정규화하며, `E=e^{-s}`,
`U=E(1-E)/s-E/2-3E²/2`의 **원래** cusp-conjugated potential을 보존하면
```
G=A−2E H/s−2U B−2(1+κ²)e^{-r}e^{-E}.
```
이 식에서 `1/s`를 임의로 smoothing하거나 버리지 않고 `N(s)=sG(s)`로 치환해 정확히
```
N(s)=sA−2E H−2(E−E²)B+sEB+3sE²B
     −2(1+κ²)s e^{-r}e^{-E}.
```
Legendre `P_l(μ(s))`와 `T_l`은 `s²`의 정확한 다항식이다. (a=|r-R|, b=r+R, t=s-a)이면 (w=b-a=2\min(r,R)\le1.4)이며 임의 유리수 r>0에서
[
\boxed{\|\mathcal R(r)\|^2_{L^2(S²)}
=(2rR)^{-1}\int_a^b \frac{|N(s)|^2}{s}ds.}
]
특히 r=R에서 a=0이며 N(0)=0임을 정확한 유리수 계수로 검사해 `δ(s)`를 숨긴 잘못된 `1/s` 적분을 거부한다.

### 엄밀한 수치표현

`e^{-a}`, `e^{-2a}`, `e^{-r}`, `e^{-e^{-a}}`의 기본값을 192항 **양의 Taylor 지수함수 상계**로 감싼 뒤 **48자리 유리수 중심값**을 사용하고, 중심값과 정확한 상·하한의 차이를 전부 오차에 포함했다. 지수함수 Taylor 다항식은 (t\in[0,w])에서:
`E(s)\approx c_1\sum_{k=0}^N(-t)^k/k!`,
`E²(s)\approx c_2\sum_{k=0}^N(-2t)^k/k!`.
복합지수 `g(t)=e^{-c_1e^{-t}}`는 `g'(t)=c_1e^{-t}g(t)`의 정확한 유리수 recurrence로 구했고, `|t|\le3`에서 (\exp(\exp(3))<2^{31})라는 별도 양의 유리수 급수 충분조건을 확인해 Cauchy 나머지를 적용했다. `sqrt(2l+1)`은 정수제곱근 기반 64자리 정확한 포함구간이다.

전체 (N_N(t))은 정확한 Fraction 계수의 복소 다항식이고,
```
∫_0^w |N_N(t)|²/(a+t)dt
```
은 `a>0`이면 정확한 `A+B log((a+w)/a)`, `a=0`이면 constant0를 증명한 후 정확한 다항식 적분이다. 로그 역시 PHYS35의 양의 `atanh` 급수와 명시한 나머지로 제한한다. 별도로 `|P_l|<=1`, `|P_l'|<=l(l+1)/2`, `|(r-Rμ)/s|<=1` 및
```
(1−μ²)/s <=(r+R)^3/(4r² R²)
```
를 사용해 normalized coefficient approximation, E, E², g, source-prefactor 오차를 angular uniform norm의 외향 상계로 더한다. 따라서 accepted interval은 수치 quadrature 수렴값을 증명으로 사용하는 것이 아니다.

### 실제 코드와 리소스 병목 복구

최초 표현은 192항 지수함수의 **수천자리 Fraction 분모를 g-recurrence에 거듭제곱으로 반복 주입**해 (r=1a_0) 계산이 180초 동안 완료되지 않는 representation bottleneck을 일으켰다. 본 실행에서 **문제를 정밀도 손실 없이** 정확한 interval 가운데 48자리 유리수 중심/최대 이탈 구간으로 교정했다. 동일 frozen 1386입력 및 소스. 진단용 기존 자기 소유 프로세스만 종료했다. 수정 후 64차 (r=1) 인증 약7.39초, (r=R^+) 약2.42초이며 독립 SciPy s-Gauss 80/160/320이 모두 인증구간 내부였다. 실패한 최초 실행을 성공 벤치마크로 환산하지 않았다.

## 3. 계산 결과, 실제 original full coupling

64차, 12자리 외향 포함구간:
| r/a0, frozen radial trace | 전 각도 L2(S²) strong residual |
|---|---|
| 1/2 | [0.000066963532,0.000066963535] |
| 7/10 left | [0.001697685386,0.001697685395] |
| 7/10 right | [0.009340991920,0.009340991929] |
| 1 | [0.000101519237,0.000101519246] |
| 2 | [0.000013161125,0.000013161134] |

96차, 16자리 별도 검증:
```
r=7/10 right: [0.0093409919248040,0.0093409919248043]
r=1        : [0.0001015192412132,0.0001015192412135].
```
64차 범위 내에 96차가 들어오며 실제 NumPy `s`-Gauss 원 strong PDE 진단과 일치한다. 같은 r=R에서 PHYS37의 전혀 다른 `x=s/(2R)` 인증과도 독립 교차검증했다. 다른 원자물리 lane의 calibration 값은 사용하지 않았다.

## 4. 새로운 양의 부피 radial strip, r!=R

엄밀한 한 반경의 angular norm (Q(\rho))과 실제 frozen Chebyshev 다항식의 `u,u',u'',u'''` 구간 sup를 결합했다. `delta<|rho−R|`, `[rho-delta,rho+delta]`가 하나의 실제 dyadic panel 안에 있으면
```
|n(r)-n(rho)| <=2 |r-rho|/|rho-R|  (ALL physical angles),
Q(r) <= Q(rho)+K |r-rho|.
```
`K`에는 D-laplace radial variation, screened derivative, bounded conjugated potential `|U|<=1, |U'|<=5`, source smooth factor, spectator unit-vector variation이 모두 들어 있다. 모든 partial-wave magnitude/normalisation은 exact Fraction & integer sqrt upper다. `L²_t` Minkowski와 물리 반경 measure를 사용하여
[
\boxed{\|\mathcal R\|_{L²(\rho\pm\delta)}\le
\sqrt2(\rho+\delta)\left[
Q(\rho)\sqrt\delta +K\sqrt{\delta³/3}
\right].}
]
실제 인증 예시:
| center rho/a0 | delta/a0 | finite-volume broken L2 upper |
|---|---|---|
| 1/2 | 10^-3 | 0.003100658335 |
| 1/2 | 10^-4 | 0.000097694613 |
| 1   | 10^-3 | 0.002232635336 |
| 1   | 10^-4 | 0.000071621782 |

독립 24x64/48x128/96x256 NumPy/SciPy full-s-coordinate double Gauss는 엄밀 상계 아래 안정되며, 예를 들어 rho=1,delta=1e-3의 sampled3D ~4.540073e-6, rho=.5,delta=1e-3 ~1.499964e-6. 다소 넓은 인증은 K가 보수적인 절댓값 majorant이기 때문이며, 이 수치를 전역 PDE 물리적 정확성으로 확대하지 않는다. Coalescence r=R strip에는 PHYS38의 별도 **로그 방향장 정리**를 써야 한다.

## 5. 로컬 코드, 최적화, 수렴 및 CAS

실제 새 코드:
`src/wu088_hh/phys33_full_coupled_shell.py`, `src/wu088_hh/phys33_full_shell_preview.py`,
`src/wu088_hh/phys33_full_radial_strip.py`, `src/wu088_hh/phys33_general_strip_preview.py`,
`scripts/phys33_full_coupled_shell.py`,
`tests/test_phys33_full_coupled_shell.py`와 `tests/test_phys33_full_radial_strip.py`.

`forkserver` 4worker로 5개 실제 frozen shell(각 21 partial waves)을 비교:
```
one worker 28.39s measured inside CLI / 28.51s shell wall,
four workers 10.76s inside CLI / 10.89s shell wall.
```
약2.62x의 과학모델·정확도 조건 일치 실측 속도향상. 시험/벤치마크 모두 CPU 과중첩을 피하도록 OPENBLAS_NUM_THREADS=1 등. 원본 다른 Codex 세션/owner reionization Rust 실행은 전혀 변경하지 않았다. 직렬·병렬 같은 scientific interval/input/panel 필드, wall/runtime만 다름. 부모 peak RSS ~35–39MiB, 자식 프로세스의 전체 RSS와 혼동 금지.

Wolfram Engine15.0.1 로컬에 대해
```
N(s)=sG(s), spectator Jacobian, angular norm measure,
cusp factor, (1-e^-s)/s limit
```
등 스칼라 정확한 0 잔차6개, 실제 xAct/xTensor1.3.0 Euclidean Green product tensor 잔차0을 반환했다. 64차와 96차 포함구간의 중첩, 독립 NumPy s-좌표 (L²(S²)) 및 finite strip float cross-check, 기존 PHYS34–39 회귀 재사용을 포함한다. 사내 로컬 scientific reviewer 외부 독립성은 주장하지 않으며, native subagent `NOT_RUN` (도구 미노출), 사용자 지시대로 local Codex `NOT_USED`.

## 6. 다른 저장소 및 남은 증명 의무

최신 별도 BASS_HE PR63(일곱 번째 warm P01 cell의 exact ray memoization), bass_cr PR71(비열적 source envelope adaptive q bin) 및 rei_bianchi PR117와 작업 트리의 AX07 completed, AX08 signed in progress, AX11/12 pending 및 AX13 completed를 확인했다. WU088_HH에서는 공통 분자적분의 cache/병렬 할당이라는 방법론만 참고했다. radiation/RT source history, gas ion fraction, Bianchi shear 출력 등 다른 물리 숫자는 가져오지 않았다. HH cold IGM source OFF 조건 유지.

**아직 열려 있는 C7B**: 현재 5개 고정 반경과 2개 finite noncoalescing radial strip의 인증은 완료했지만, 전체 six panel의 실제 angular-coupled residual을 적분한 새로운 **전역** upper는 아직 계산하지 않았다. 기존 PHYS39 절단 annulus H^-1 upper `2.516921964597789440`는 부모대로 유효하다. 다음 `C7B_ALL_PANEL_RADIAL_INTEGRATION_AND_CONTINUOUS_OUTGOING_DUAL`에서 cusp PHYS38 strip, PHYS40 noncusp strips를 adaptive positive certified radial tiles로 완전히 덮고, 남은 origin patch·screened exterior DtN 및 연속 low-Schur infsup와 incoming adjoint를 결합해야 한다. 전역 two-centre scattering intensity, thermal rate, P01 physical transfer는 모두 `null`. Main merge·release·owner REI 변경 없음.
