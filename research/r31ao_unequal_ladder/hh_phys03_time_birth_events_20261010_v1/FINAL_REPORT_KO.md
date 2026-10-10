# WU088_HH PHYS03 — 시간 의존성, photon birth, 문턱 remap의 혼합 반응

2026-10-10. PHYS02 다음 물리 연구 루프를 완료했다. 독립 최종 판정은 PROMOTE_SCOPED다. 실제 native family의 유한시간 부호와 physical/production admission은 미해결/HOLD로 유지한다. 판정 원문은 independent/DECISION.json과 FINAL_STATUS_KO.md에 있다.

## 1. 이번 루프의 물리 결론

**같은 HH 강도와 같은 총 광자 수를 써도, birth 시점과 remap–BE의 연산 순서가 혼합 이온화 반응을 바꾼다.** PHYS02의 frozen continuous 부호 정리를 actual endpoint-birth owner에 곧바로 적용할 수 없는 이유를 유도식과 실제 source의 국소 수치로 분해했다.

새 결과는 네 가지다.

1. Smooth nonautonomous cell에서는 명시적 시간도함수가 mixed cubic에 들어오지 않는다. Quartic의 새 항을 전부 구했고, photon-independent nonphoto drift는 그 차수에서도 소거된다.
2. Birth 이전부터 쌓인 HH 감도를 보존하는 causal kernel과, \(m\)회 birth+BE의 선도계수 \(C_m\)을 도출했다. Continuous rate, initial impulse, terminal impulse, endpoint birth+BE를 같은 것으로 취급할 수 없다.
3. 같은 물리 시각으로 맞춘 event의 혼합 이차 derivative를 구현하고 닫힌 해로 검산했다. 실제 \((\lambda,b)\) 고정 geometry 계약에서는 event clock 미분이 0이고, 기존 \(U,W\)는 그대로 전파된다.
4. 실제 FLRW grid의 13.60 eV node에서 한 full remap과 두 half remap의 활성 weight가 각각 약 0.1312181과 0.3199120임을 확인했다. Photon number와 첫 energy moment가 같아도 opacity는 같지 않다.

유도와 새 범위의 검산은 완료했다. Actual native four-corner family의 유한시간 혼합 부호, production 사용, 전체 이력 정확도는 이번 결과에 포함되지 않는다.

## 2. 계승 결과와 실제 source를 연결한 방식

직전 PHYS02 연구 commit:

    0bf109607e51873b6cf44ed8d3eb8f719388fb9b

현재 actual owner commit:

    569b04cd71e45756e0fd476aef6643bd9434f4fa

원 선택 source JSON SHA-256:

    26a340065a9a99d02903bf0cc008baaf6ade00d2e845beb9d2b0b7d801316494

PHYS02는 같은 전체 initial state에서
\[
\dot z=F_0(z)+\lambda H(z)+bS_*B,\qquad
S_*={\rm binary64}(5\times10^{-15})
\]
를 정의한 frozen continuous 모델이었다. 그 모델에서 \(h=1.25\times10^9\) s,
\(\tau=t/h\)에 대해
\[
\frac{I_x}{\lambda b}
 \in c_3\tau^3+[L_4,U_4]\tau^4<0
\]
를 이미 인증했다. 상속된
\(c_3=-2.0159064162896692\ldots\times10^{-17}\),
\(U_4=5.419101446044448\ldots\times10^{-20}\)와
endpoint의 안전한 짧은 enclosure
\[
[-2.010735,-2.010487]\times10^{-17}
\]
는 그 범위에서 유지된다. 이번 루프에서 기존 tube/적분 suite를 다시 실행하지 않았다.
근거: inputs/phys02/results/REMAINDER_256_FINAL.json,
inputs/phys02/independent/DECISION.json.

새 source 조사에서 중요한 시간 의미가 닫혔다.
선택 old_point_photons 25개는 저장 native preBE record의
member1 half1, line5의 해당 group과 전부 binary64 bitwise 동일하다.
그러나 그 stage의 gas는 \(t_0=160000000000\) s의 이전 gas,
photon과 density는 endpoint \(t_1=160625000000\) s의 조립값이다.
즉 하나의 BE-stage aggregate다. PHYS02는 이를 새 수학적 초기값으로
선언한 결과이며, 실제 macro 이전의 continuous snapshot임을 보인 결과는 아니다.

실제 배경은 이미 source에 있다.
\[
a_i(t)=e^{h_it},\quad
n_H(t_1)=10^{-4}e^{-(h_1+h_2+h_3)t_1},\quad
n_{He}=0.083n_H.
\]
선택 member1은 \(h_i=10^{-14}\ {\rm s}^{-1}\)인 FLRW다.
새 owner는 common-state four-corner 계약과 synthetic isothermal family를
추가했지만 actual native family/root/tube를 제공하지 않았다.
배경 가용성과 실제 해·감도 family의 가용성은 서로 다르다.

근거: inputs/source_survey/SOURCE_SURVEY_KO.md,
SOURCE_LINE_BINDINGS.json, SOURCE_IDENTITY_VERIFICATION.json.
30개 snapshot과 25개 source 구간의 byte/hash binding을 보존했다.
원 seed binary의 gas4를 새로 독립 decode한 것은 아니며,
gas의 시간 의미는 원 source와 저장 selected record에 근거한다.

## 3. 명시적 시간변화가 들어오는 첫 차수

차원 있는 source strength \(S=bS_*\)를 잠시 독립변수로 쓴다.
\[
F(t,z;\lambda,S)=F_0(t,z)+\lambda H(t,z)+SB(t).
\]
\(H\)는 photon-independent이고 photon 성분이 0이다.
\(B,B_t\)는 같은 고정 photon 좌표부분공간에 놓인다.
Photo RHS는 gas–photon bilinear이고 H/He, 열, 팽창 channel은 보존한다.
\(J=F_z,\ Q=F_{zz}\)이며 \(t\)-편미분에서는 \(z\)를 고정한다.

공통 clock에서
\[
\dot U=JU+H,\qquad
\dot V=JV+B,\qquad
\dot W=JW+Q[U,V]+H_zV.
\]
같은 parameter-independent 전체 initial state이면 \(U_0=V_0=W_0=0\)이다.

\(K_r=W^{(r)}(t_0)\)라 하면
\[
K_2=0,\qquad
\boxed{K_3=H_zJB+2Q(H,B).}
\]
명시적 \(H_t,B_t,F_t\)가 cubic에 별도 항으로 들어오지 않는다.

Quartic의 instantaneous frozen 계수를 \(K_4^{\rm fr}\)라 할 때
\[
\boxed{
\begin{aligned}
K_4&=K_4^{\rm fr}+\Delta_tK_4,\\
\Delta_tK_4
 &=3Q(H_t,B)+3Q(H,B_t)+6Q_t(H,B)\\
 &\quad+H_z(JB_t+2J_tB)+3H_{tz}(JB).
\end{aligned}}
\]
직접 \(F_t\) 벡터, \(B_{tt}\), \(H_{tt}\)는 이 차수의 최종 식에서 소거된다.
\(\Delta_tK_4\)는 \(\lambda,S\)에 무관하여 기존 quartic의 \(S\) 독립성과
\(\lambda\) affine 구조가 유지된다.

명시적 변화가 photon-independent nonphoto 장 \(N(t,y)\)에만 있다면
\(J_t^N B=Q_t^N(H,B)=0\)이므로 \(\Delta_tK_4=0\)다.
Instantaneous \(N,N_y,N_{yy}\)는 frozen quartic에 여전히 들어간다.
이 소거는 예를 들어 \(-2H_{\rm mean}(t)w\)의 explicit
\(H_{\rm mean,t}\) 변화만 다룰 때 적용된다.
밀도가 바뀌어 HH amplitude와 opacity도 바뀌면 quartic 보정이 일반적으로 생긴다.

검산은 actual history에 대한 적분이 아니라 구조를 보존한 exact rational
다변수 polynomial fixture다. 6 time-dependent family와 6 parameter point,
36개 case에서 모든 5개 상태성분이 독립 time-series recurrence와 일치했다.
별도 additive drift fixture의 mixed \(x\)는 5차에서 처음 달라졌다.
전체 유도와 식의 가정은 smooth_theory/PHYS03_SMOOTH_THEORY_KO.md §§2–5에 있다.

## 4. Birth 이전 HH를 기억하는 kernel

HH와 추가 source가 없는 기준 trajectory의 variational propagator를
\(\Phi(t,s)\)라 하면
\[
U(r)=\int_0^r\Phi(r,u)H(u)\,du.
\]
정해진 시각 \(s\)에 단위 photon impulse를 넣는
혼합 functional kernel은
\[
\mathcal K_z(t,s)=
\int_s^t\Phi(t,r)
\left[
Q_0(r)\{U(r),\Phi(r,s)B(s)\}
+H_z(r)\Phi(r,s)B(s)
\right]dr.
\]
이 식의 \(U(r)\)는 birth 이전의 HH 누적을 포함한다.

Frozen leading limit에서 \(X=H_zJ_0B,\ Y=Q_0(H,B)\)라 두면
\[
\boxed{
\mathcal K_z(t,s)
=\frac{(t-s)^2}{2}X+\frac{t^2-s^2}{2}Y+O(t^3).
}
\]
13.7 eV HI birth에 대해
\[
A=cn_H\sigma_H(E_b),\quad q=n_H(1-x)^2k_{\rm LCS}(T),
\]
\(X_x=-Aq(2+\Xi)\), \(Y_x=-Aq\)이므로
\[
\boxed{
\mathcal K_x(t,s)=
-Aq\left[s(t-s)+\frac{3+\Xi}{2}(t-s)^2\right]+O(t^3).
}
\]
Birth 때 HH 감도를 0으로 reset하면 \(-Aq\,s(t-s)\)를 누락한다.
이 항은 birth 전에 HH가 바꿔 놓은 중성수소를 새 광자가 만나는 효과다.
\(\Xi\ge0\)인 local leading kernel에서는 같은 질량의 photon이 일찍
들어올수록 음의 혼합 반응이 더 크다. 이는 all-time 부호 정리는 아니다.

같은 총 photon 질량 \(M=Sh\)로 비교한 leading factor는 다음과 같다.

| source / 연산 | \(I_x/(\lambda MAqh^2)\)의 leading factor |
| --- | ---: |
| uniform continuous rate | \(-(4+\Xi)/6\) |
| initial impulse 뒤 continuous evolution | \(-(3+\Xi)/2\) |
| 관측 종료시각의 true terminal impulse | \(0\) |
| birth 뒤 길이 \(h\)의 한 frozen BE map | \(-(3+\Xi)\) |

True terminal impulse와 endpoint birth+BE는 gas의 노출시간이 다르다.
상속 \(\Xi_0=0.1769024684110926\ldots\)에서 한 BE map의 leading 크기는
uniform continuous의 약 4.56353배다. 실제 유한 step 오차율을 뜻하지 않는다.

### \(m\)회 birth+BE의 계수

같은 raw 초기상태, 총 시간 \(h\), 각 step의 birth \(Sh/m\)을 쓰는
frozen formal BE 합성에서
\[
\boxed{
I_{x,m}=-\lambda SAqh^3 C_m+O(\lambda Sh^4),\qquad
C_m=\frac{4+\Xi}{6}
+\frac{3+\Xi}{2m}
+\frac{5+2\Xi}{6m^2}.
}
\]
\(m=1\)에서는 \(3+\Xi\),
\(m=2\)에서는 \(13/8+\Xi/2\),
\(m\to\infty\)에서는 \((4+\Xi)/6\)으로 간다.

| 분할 | 상속 \(\Xi_0\)를 넣은 \(C_m\) |
| --- | ---: |
| 1 | 3.176902468411093 |
| 2 | 1.713451234205546 |
| 4 | 1.149032021378466 |
| 8 | 0.908649016033850 |
| continuous limit | 0.696150411401849 |

전체 vector의 계수는
\[
\alpha_mX+\beta_mY,\qquad
\alpha_m=\frac{(m+1)(m+2)}{6m^2},\quad
\beta_m=\frac{(m+1)(2m+1)}{6m^2}.
\]
\(m=1,2,3,5,8\)과 두 \(\lambda\) 기준점, 총 10개 case에서
formal implicit polynomial substitution으로 모든 상태성분의 cubic
계수를 독립 확인했다. Nonlinear BE root는 계산하지 않았다.
실제 mid-history의 \(U_{\rm old},V_{\rm old},W_{\rm old}\)가 이미 nonzero이면
위 zero-initial 전개를 다시 시작하지 않고 그 감도를 전파해야 한다.

## 5. Event에서 mixed sensitivity를 전파하는 방법

일반 regular event \(g(t,z;\lambda,b)=0\), reset \(R\)에 대해
event-time의 first/mixed derivatives, 움직이는 event 위의 reset,
공통 nominal time의 post branch로 돌아오는 보정을 모두 유도했다.
분모 \(g_t+g_zf^-\ne0\), \(C^2\) guard/reset, 같은 event 순서가 필요하다.
정확한 식과 증명은 HYBRID_THEORY_KO.md에 있다.

일차 한계는 표준 saltation matrix로 돌아간다.
문헌 기준은 Kong et al. (2024),
[DOI 10.1109/JPROC.2024.3440211](https://doi.org/10.1109/JPROC.2024.3440211),
[arXiv §III-A](https://arxiv.org/html/2306.06862v3)다.
혼합 이차식은 이번 직접 chain-rule 유도이며 문헌 최초성은 주장하지 않는다.

현재 actual owner의 고정 h/q/grid/source shape/clock에서
\(a=\lambda,b=S/S_*\)만 바꾸는 계약은 geometric event clock을 바꾸지 않는다.
이 설정의 photon map이
\[
R(z;a,b)=Lz+bB_e
\]
이면
\[
\boxed{U^+=LU,\quad V^+=LV+B_e,\quad W^+=LW.}
\]
이전 감도를 지우지 않는 것이 핵심이다.
Owner의 \(\theta\)는 현재 fixed-configuration tag이며 \(b\)와 다르다.
진짜 geometry family나 adaptive clock family에는 zero-time-derivative
결론을 그대로 적용할 수 없다.

닫힌 event-time/flow/reset 합성을 Sympy로 미분해 구현과 비교한
8개 검사에서 PASS였다. 이 구현은 algebraic derivative operator이고,
실제 event locator나 native root validator는 아니다.

## 6. 실제 문턱 remap이 보여 준 추가 효과

확인한 owner 순서는
transport → fixed-grid hat remap → endpoint birth → coupled BE다.
BE 단면적은 transported ray energy가 아니라 fixed node에서 평가한다.
Provider cutoff는 13.60 eV, HH binding energy는 13.598434599702 eV다.

선택 FLRW의 \(\delta=6.25\times10^8\) s, \(H=10^{-14}\ {\rm s}^{-1}\)에서
node16 \(E_*=13.6\) eV의 단위 basis packet을 진단했다.
바로 아래 node는 \(E_-=13.599804324962749\) eV다.
\(r=e^{-H\delta}\), \(K=E_*/(E_*-E_-)\)라 하면
\[
w_\delta=\frac{E_*r-E_-}{E_*-E_-},\quad
w_{2\delta}=\frac{E_*r^2-E_-}{E_*-E_-},
\]
\[
\boxed{w_\delta^2-w_{2\delta}=K(K-1)(1-r)^2>0.}
\]

| 같은 총 시간 \(2\delta\)의 transport | 활성 node16 weight | effective \(\sigma_H\) [cm²] |
| --- | ---: | ---: |
| 한 full remap | 0.1312180649460370 | \(8.32748727801\times10^{-19}\) |
| 두 half remap | 0.3199120420203140 | \(2.03025662747\times10^{-18}\) |
| 두 half − 한 full | 0.1886939770742770 | \(1.19750789967\times10^{-18}\) |

두 방식 모두 photon number와 첫 energy moment를 보존한다.
그런데 transported characteristic의 energy는 cutoff 아래이고,
fixed active node로 배분된 weight에는 양의 sigma가 남는다.
따라서 number/energy ledger만으로 opacity 또는 HH mixed response의
정확도를 인증할 수 없다.

실제 input leaf를 사용한 Arb 256-bit enclosure가 cell membership,
weight 순서와 양의 차이를 확인했다. 독립 mpmath 110자리 계산 9개도
정확한 Arb endpoint 안에 들어갔다.
한 column 진단이며 저장된 전체 photon history 또는 gas error가 아니다.
Rust의 연산별 binary64 rounding replay도 아니다.

흡수가 없는 birth energy moment도 따로 계산했다.
같은 photon 수에서 continuous 주입 대비 한 endpoint 주입은 약
6.250013 ppm, 두 endpoint 주입은 약 3.125003 ppm의 energy excess를 갖는다.
이것도 source 연령 모멘트의 차이이며 actual ionization error는 아니다.

전체 식, 단위, exact endpoints는 CHRONOLOGY_THEORY_KO.md와
results/CHRONOLOGY_256.json에 있다.

## 7. 유한시간 부호 전이의 충분조건과 현재 gap

\(X=(z,U,V,W)\)를 함께 비교해
\[
|W_x^{\rm actual}-W_x^{\rm ref}|\le B_{W_x}(t)
\]
를 parameter rectangle 전체에서 인증하면,
\[
\left|\frac{I_x^{\rm actual}}{\lambda b}
      -\frac{I_x^{\rm ref}}{\lambda b}\right|
\le B_{W_x}(t)
\]
다. Reference upper bound가 \(-m(t)\)이면
\(B_{W_x}(t)<m(t)\)가 음의 혼합 부호를 보존하는 충분조건이다.

Smooth cell에는 componentwise variational comparison을,
각 endpoint의 remap–birth–BE에는 전체 augmented map의
\(E_{i+1}\le K_iE_i+\rho_i\)를 쓰면 된다.
Initial slice와 source control 의미를 먼저 맞추고,
초기 차이 및 event/model defect를 빠짐없이 budget에 넣어야 한다.

PHYS02의 endpoint margin은 약 \(2.0104873\times10^{-17}\)이다.
현재 actual family에 이 수치를 tolerance로 부여하거나
이번 remap weight 차이를 이 margin과 직접 비교하지 않았다.
둘은 관측량과 차원이 다르다.
전체 논증과 적용 조건은 REMAINDER_TRANSFER_KO.md에 있다.

| 이미 있는 것 | 아직 필요한 것 |
| --- | --- |
| 실제 background, fixed grid, redshift, birth law와 step clocks | native common-state \((\lambda,b)\) family |
| 저장된 full/half1 preBE photon record | 새 accepted half1 전체 checkpoint receipt와 half2 incoming state |
| 새 mixed derivative·birth/BE coefficient 유도 | trusted root/tube 및 uniform inverse bound |
| 문턱 remap의 source-bound 한 column enclosure | full augmented map의 \(K_i,\rho_i,B_{W_x}\) bound |

## 8. 실행 근거와 다음 연구

| 범위 | 새 검증 |
| --- | --- |
| source identity / selected-stage linkage | 30 snapshots, 25 source 구간, 25 photon bitwise 일치 |
| 비자율 cubic/quartic | 36 exact rational cases, 모든 5개 상태성분 |
| birth kernel | uniform/linear profile, initial/terminal impulse, prebirth memory |
| 반복 birth+BE | 10 formal-series cases, 모든 상태성분 |
| 공통 시각 event derivative 구현 | 8 exact closed-form/guard tests |
| actual-leaf remap 및 free birth energy | Arb256 strict enclosure + 9 independent mpmath checks |

과학 checker의 최초 실행은 모두 PASS였다. 문서 저장 과정의 형식 오류는
failures 및 smooth_theory/FIRST_ARTIFACT_WRITE_FAILURE.json에 별도로 보존했다.
Native dispatch, IVP, nonlinear BE root, NCP, 기존 atomic integral, 완료한
PHYS02/peer suite의 재실행은 각각 0이다.

다음 PHYS04의 물리 목표는 **fixed-grid remap과 H/He·열 feedback을 포함한
full/two-half 혼합 결함의 다음 차수**다. 이번 \(C_m\)의 cubic을 출발점으로,
고정 grid의 one-sided 시간 전개, endpoint density 변화, birth/BE 노출을
같은 순서로 넣어 quartic 및 opacity-weighted defect를 분해한다.
Actual native family가 제공되면 그 family와 연결한 유한 bound로 확장하고,
그 전에 가능한 source-bound algebra를 기존 adapter 재작성으로 대체하지 않는다.
NEXT_DAG.json과 NEXT_HANDOFF_KO.md에 정확한 입력 및 금지된 승격을 기록한다.

계승 ceiling은 HH research ACTIVE, canonical S0 HH OFF control,
legacy 24/289와 265 unbounded, epsilon_C/R null, B22 OPEN,
ON06G 256 macro 및 \(3.2\times10^{11}\) s 완료 scope 보존,
physical/production HOLD다.

## 9. 독립 최종 판정

독립 reviewer는 PHYS03의 후보 작성과 검증 설계에 참여하지 않은 /root/decision_review다. 핵심 18개 파일의 hash를 고정한 상태에서 수식·구현·source·evidence를 대조했고 과학적 필수 수정은 없다고 판정했다.

새로운 확인은 exact rational/파일 identity 검사 1회이며, 20개 Arb 구간의 정확한 끝점 40개와 decimal 외향성, mpmath witness 9개, source 구간 25개, selected photon 25개의 저장 half1 연결을 확인했다. 원 candidate checker나 PHYS02 suite를 반복 실행하지 않았다.

C01–C07은 문서의 명시된 범위에서 PROMOTE다. C08은 augmented error의 조건부 부호 이전 정리만 PROMOTE이고, 실제 B_Wx와 충분조건의 수치 충족은 KEEP_UNRESOLVED다. Native 실행 권한이나 physical/production admission을 변경하지 않는다.

이 최종 보고서의 과학 본문은 검토된 REPORT_KO.md와 동일하다. 표지의 판정 상태와 이 절만 추가했다. 검토된 원본과 REVIEW_TARGETS hash는 그대로 보존했다. 독립 검토 원문은 independent/DECISION_REVIEW_KO.md다.
