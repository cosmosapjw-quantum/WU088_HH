# WU088_HH PHYS03 독립 최종 판정

## 1. 판정과 적용 범위

**최종 판정은 PROMOTE_SCOPED다.** PHYS03의 새로운 수식, 정확 대수 검사, 고정 에너지 격자 한 column의 구간 계산, 실제 source의 연산 순서와 자료 연결을 연구 결과로 채택할 수 있다. 수정이 필요한 과학적 blocking 오류는 발견하지 않았다.

**실제 owner의 유한 혼합 부호, native 공통 parameter family, 물리 및 production admission은 HOLD다.** C08은 부호 이전의 충분조건을 제시한 조건부 정리로만 채택한다. 그 조건의 실제 수치 충족은 KEEP_UNRESOLVED다. 이 판정은 실행 권한이나 native dispatch 범위를 변경하지 않는다.

검토 대상은 HH-PHYS03-review-v1의 고정된 18개 파일과 추가된 NOTATION_AND_INTERPRETATION_KO.md다. 기존 PHYS02의 완료된 수치 감사를 반복하지 않았다. PHYS02는 그 문서에서 정의한 frozen continuous reference에 대한 선행 정리로 사용했다.

| 주장 | 판정 | 허용되는 결론과 조건 |
| --- | --- | --- |
| C01 | PROMOTE | 같은 parameter-independent initial state, 고정 photon subspace, 상태와 무관한 birth, gas–photon bilinear photo 항을 전제로 한 nonautonomous cubic/quartic 공식과 제한된 nonphoto explicit-time 소거 |
| C02 | PROMOTE | baseline에서의 causal infinitesimal birth kernel과 birth 이전 HH tangent의 보존; 유한 source에는 parameter 평균이 필요 |
| C03 | PROMOTE | frozen equal-step birth 후 formal BE 합성의 혼합 cubic 계수 \(C_m\); 실제 BE root나 유한 step 오차의 증명은 아님 |
| C04 | PROMOTE | 동일한 event 순서와 transverse \(C^2\) chart에서의 공통시각 혼합 chain rule; fixed affine map의 tangent 전달 |
| C05 | PROMOTE | 지정 FLRW binary64 leaf와 provider에서 고정 grid 한 basis column의 semigroup 성질 실패 및 양의 opacity 차이; 광자수와 첫 에너지 모멘트 보존과 양립 |
| C06 | PROMOTE | 지정 상수와 자유 전파를 전제로 한 continuous/endpoint birth의 에너지 모멘트 차이 |
| C07 | PROMOTE | 실제 background 및 연산 순서, selected photon numerator의 archived half1 자료 연결, 새 공통 family가 아직 없다는 현 상태 |
| C08 | PROMOTE / KEEP_UNRESOLVED | augmented error의 조건부 부호 이전 정리는 PROMOTE; 실제 \(B_{W_x}\)와 조건 충족 여부는 KEEP_UNRESOLVED |

각 행의 PROMOTE는 이 표의 가정을 포함한다. 새로운 native finite sign, 실제 full/twohalf gas error, 실제 branch의 존재·유일성, native 연산별 반올림 enclosure, 연속 에너지 opacity의 물리적 정확성, 전역 또는 실제 전시간 부호로 확대할 수 없다.

## 2. 독립성과 실행 기록

Reviewer는 /root/decision_review다. PHYS03 후보 생성과 검증 설계에 참여하지 않았다. 이전 PHYS02의 최종 검토 경험은 있으나 이번 PHYS03의 대수, event 또는 chronology 후보 작성에는 참여하지 않았다. 실제 host가 표시한 모델 이름은 GPT-6 Astra Pro다. 별도의 runtime model ID나 cryptographic attestation은 제공되지 않았으므로 그런 확인을 수행했다고 주장하지 않는다.

Astra v4 연구 core와 model-routing 지침을 적용했다. 검토에서는 증명 가정과 식, 해당 구현, 기존 실행 로그, 고정된 source 구간 및 증거의 무결성을 대조했다. 기존 검사 개수 자체를 증명으로 대체하지 않았다.

기존 새 증거에는 정확 유리수 nonautonomous 36개 경우, formal BE 10개 경우, exact event 8개 테스트, Arb 256-bit chronology 및 mpmath 110자리 9개 대조가 있다. 이들의 코드와 로그를 읽었으며 원 candidate checker를 다시 실행하지 않았다. 이것들은 일반 정리의 유도와 서로 독립인 계산 표현을 보조하는 유한 검사다. 물리 이력, native family 또는 formal proof assistant certificate가 아니다.

Reviewer가 새로 실행한 것은 independent/reviewer_checks.py 한 번이다. 표준라이브러리의 정확 유리수와 파일 hash만 사용했으며 다음을 통과했다.

- REVIEW_TARGETS의 18개 파일 크기 및 SHA256 일치.
- source binding 25개 구간의 원파일 hash, byte slice hash, line/byte 범위 일치.
- 저장된 Arb 구간 20개의 exact dyadic 40개 끝점 순서와 decimal 표시의 외향성.
- 저장된 mpmath 값 9개의 exact 끝점 사이 포함. mpmath나 초월함수를 새로 평가한 것은 아니다.
- cutoff cell, active weight, 양의 opacity 차이, 자유 전파 에너지 순서 및 다음 left knot까지의 시간에 대한 strict interval 비교.
- selected photon 25개 값과 archived member 1 half1 preBE 자료의 정확한 연결. 해당 값들은 모두 양의 binary64 값이므로 정확 유리수 일치는 binary64 값 일치다.
- 주요 Markdown 8개 파일의 비정상 control character 부재.

Reviewer의 실행 exit code는 0이고 stderr는 비어 있다. 독립 확인 결과는 independent/REVIEWER_CHECKS.json에 저장했다. seed binary를 새로 decode하지 않았다. native dispatch, IVP trajectory, nonlinear BE solve, NCP, 이전 atomic integral, PHYS02 suite 재실행은 모두 0이다. 후보 문서나 구현은 수정하지 않았다.

## 3. Nonautonomous 혼합 도함수

고정 clock에서 \(F=F_0+\lambda H+SB(t)\)라 두면
\[
U'=JU+H,\qquad V'=JV+B,\qquad
W'=JW+Q(U,V)+H_zV
\]
다. 여기의 parameter 미분은 시간을 함께 바꾸지 않으므로 별도 \(F_t\) 항이 붙지 않는다. 반면 시간 Taylor 계수에는 \(D=\partial_t+F\cdot\nabla_z\)가 작용한다. 이 두 연산을 구분한 유도가 타당하다.

일반식의
\[
K_3=JK_2+2Q(H,B)+H_zV_2+2(DH_z)B
\]
와
\[
\begin{aligned}
K_4={}&JK_3+3(DJ)K_2+3Q(U_2,B)+3Q(H,V_2)\\
&+6(DQ)(H,B)+H_zV_3+3(DH_z)V_2+3(D^2H_z)B
\end{aligned}
\]
를 직접 미분 규칙으로 대조했다. \(3,6\)의 조합계수와 초기 \(U=V=W=0\)의 사용이 일관된다.

광자 방향을 annihilate하는 \(H_z,H_{tz},H_{zz}\), photon-independent HH, photo 항의 gas–photon bilinearity가 있어야 문서의 소거를 쓸 수 있다. 단지 photon에 대해 선형이라는 조건만으로 모든 고차 tensor 소거가 따라오는 것은 아니다. 후보는 더 강한 실제 구조를 명시했다. 이 조건에서 \(K_2=0\), cubic은 순간 frozen 값과 같으며, quartic의 explicit-time 차이는
\[
\Delta_tK_4=
3Q(H_t,B)+3Q(H,B_t)+6Q_t(H,B)
+H_z(JB_t+2J_tB)+3H_{tz}(JB)
\]
다. 직접 \(F_t,B_{tt},H_{tt}\)가 최종 reduced 식에서 사라지는 것은 이 구조에 의존한다.

Photon-independent nonphoto 항만 명시적으로 시간에 따라 바뀌고 \(H_t=B_t=0\)인 경우의 quartic 소거는 타당하다. 순간 nonphoto 값이나 그 상태 도함수가 전체 quartic에서 사라진다는 뜻은 아니다. 밀도 변화는 HH와 photo opacity에도 들어가므로 이 특별한 소거에 자동 포함되지 않는다. 정확 fixture에서 additive drift가 5차에 처음 영향을 주는 사례는 가능성을 보여 주며, 모든 nonphoto 시간 변화의 5차 계수가 반드시 nonzero라는 주장은 허용하지 않는다.

Quartic의 \(S\)-독립성과 \(\lambda\)-affinity는 이 구조 아래에서 허용된다. 이에 따른 \(\lambda^2S\)의 4차 출현 가능성과 \(\lambda S^2\)의 4차 부재를 사용할 수 있다. 실제 owner의 유한 시간 Taylor remainder를 얻었다고 해석할 수는 없다. 증거: smooth_theory/PHYS03_SMOOTH_THEORY_KO.md, check_nonautonomous.py 및 NONAUTONOMOUS_EXACT_CHECK.json.

## 4. Birth 이전 기억과 formal BE

Birth 시각 \(s\) 이전에 누적된
\[
U(s)=\int_0^s\Phi(s,u)H(u)\,du
\]
는 후속 source를 추가할 때 사라지지 않는다. 문서의 causal kernel은 birth 이후 전파되는 photon tangent와 기존 HH tangent가 만나는 \(Q(U,V)\) 항을 유지한다. \(H_zV\) 항과 함께 적분한 leading 식
\[
K_z(t,s)=\frac{(t-s)^2}{2}X+\frac{t^2-s^2}{2}Y+O(t^3),
\qquad X=H_zJ_0B,\quad Y=Q_0(H,B)
\]
는 동일 baseline, 작은 총시간의 전개로 타당하다. \(Y_x=-Aq\)이므로 tangent를 birth마다 0으로 되돌리면 \(-Aq\,s(t-s)\)를 잃는다. 이는 실제 chronology를 이어갈 때 중요한 차이다.

이 kernel은 baseline에서의 infinitesimal functional response다. 유한 \(\lambda\)와 유한 birth strength의 contrast를 얻으려면 공통 parameter 사각형의 혼합 도함수 평균과 균일한 remainder가 필요하다. Candidate는 그 제한을 유지한다.

Endpoint에서 birth를 더한 뒤 implicit source map을 적용하는 것은 observation 직전의 진짜 instantaneous kick과 다른 연산이다. 후자의 즉시 gas 변화가 0이어도 전자의 formal BE mixed response는 nonzero일 수 있다. 시간 객체를 구분한 설명이 올바르다.

공통 frozen initial state에서 \(\delta=h/m\)인 equal-step 합성의 cubic 계수
\[
C_m=\frac{4+\Xi}{6}+\frac{3+\Xi}{2m}
+\frac{5+2\Xi}{6m^2}
\]
는 문서의 이산 합과 일치한다. \(m=1\)에서 \(3+\Xi\), \(m=2\)에서 \(13/8+\Xi/2\), \(m\to\infty\)에서 \((4+\Xi)/6\)가 된다. 체크 구현은 step마다 세 번의 formal substitution으로 \(h^3\) 계수를 결정하며 수치 root를 풀지 않는다. \(C_m\)을 실제 \(h\)에서의 error ratio, 수렴 보증 또는 accepted BE branch의 존재 증명으로 사용할 수 없다. 중간 단계의 initial tangent가 nonzero이면 그것을 그대로 전달해야 한다.

추가 notation 문서의 \(\Xi\)와 \(T_\gamma\) 해석도 허용한다. \(T_\gamma\)는 birth excess energy에 대응하는 온도이며 CMB 온도가 아니다. 음의 mixed contrast는 HH와 지정 미래 photon source의 결합이 단순 합보다 작다는 뜻이다. direct HH 효과의 부호나 실제 전체 HII 변화의 부호와 같지 않다.

## 5. Event 혼합 chain rule

문서와 src/hybrid_mixed.py를 독립적으로 비교했다. Moving event state를 미분한 뒤, post-event flow를 사용해 같은 관측시각으로 되돌리는 구조가 맞다. 특히 mixed 식의 post-flow 항에는 moving event derivative \(Y_a,Y_b\)가 아니라 이미 공통시각으로 동기화된 \(U^+,V^+\)가 들어가야 한다. 구현은 이를 지킨다.

Guard Hessian에는 시간, 상태, 두 parameter의 혼합 항이 모두 포함되고, pre/post vector field의 명시적 시간·parameter 의존성도 포함된다. 첫 도함수의 상태 Jacobian 한계는 표준 saltation 식
\[
R_z+\frac{(f^+-R_zf^--R_t)g_z}{g_t+g_zf^-}
\]
와 일치한다. 이 대조에는 Kong, Payne, Zhu, Johnson의 원 논문, “Saltation Matrices: The Essential Tool for Linearizing Hybrid Dynamical Systems,” Proc. IEEE 112(6), 585–608 (2024), §III-A, Eq. (9)를 확인했다. 원문: https://arxiv.org/html/2306.06862v3 . 문헌의 1차 식과 이번 후보가 직접 유도한 2차 혼합 식의 역할을 구분한다.

정규성 조건은 중요하다. \(g_t+g_zf^-\ne0\), 같은 local event sequence, 충분히 매끄러운 one-sided flow와 reset이 필요하다. Grazing, 순서가 바뀌는 동시 event, 다른 event 개수, parameter 변화가 지나는 remap knot의 비매끄러운 chart를 이 일반식 하나로 인증하지 않는다. 구현은 주어진 도함수에 대한 point algebra operator이며 이 가정들을 자동으로 전역 검증하는 interval event solver가 아니다.

Geometry와 schedule이 두 control에 의존하지 않는 fixed affine map에서는
\[
U^+=LU,\qquad V^+=LV+B_e,\qquad W^+=LW
\]
가 된다. “기억 보존”은 이 선형 전달을 뜻하며 모든 성분 값이 그대로라는 뜻은 아니다. BE derivative 식은 해당 branch의 존재와 \(I-\delta J\)의 가역성을 조건으로 사용해야 한다.

Exact event 테스트 8개는 parameter-dependent event 시각, curved state guard, time/state-dependent 양쪽 flow, nonlinear 및 vector reset, identity event, off-guard/비횡단 거절을 포함한다. 단순히 구현식을 다시 적은 비교에 머무르지 않고 closed-form flow로부터의 미분과 대조하므로 이번 제한된 operator 검증에 적절하다.

## 6. 실제 source chronology와 remap 한 column

최신 owner commit 569b04cd71e45756e0fd476aef6643bd9434f4fa에 고정 Hubble background와 명시적인 clock, source law, 고정 grid가 있다. Background가 없다는 결론은 잘못이며 이번 후보는 그렇게 주장하지 않는다.

확인한 연산 순서는 기존 photons와 lower guard의 redshift, 고정 energy grid remap, endpoint birth, 방향별 photon numerator의 grouping, 이전 gas와 endpoint density를 조립한 BE source stage다. Full branch는 diagnostic이고, accepted 상태는 half1 뒤 half2를 이어 얻는다. Full을 accepted 누적 이력에 더하면 안 된다. 해당 순서와 ledger 분리를 raw source 구간에서 확인했다.

Selected 자료의 photon 25개는 archived member 1 half1 preBE record와 정확히 일치한다. 선택 항목은 gas at \(t_0\), remap과 birth 뒤의 photon numerator 및 density at \(t_1\)을 함께 쓰는 BE-stage aggregate다. Native continuous flow의 한 순간에서 동시에 나온 상태로 인증된 것이 아니다. 이 정정은 PHYS02가 그 수치를 명시적 mathematical initial state로 사용한 frozen 정리를 무효화하지 않는다. 실제 continuous history로 자동 연결할 근거를 제공하지도 않는다. Seed gas를 새로 decode해 bitwise 연결했다고 주장하지 않는다.

HI provider의 cutoff \(13.60\,\mathrm{eV}\)와 binding energy \(13.598434599702\,\mathrm{eV}\)는 구분된다. 선택한 index 16은 cutoff에 놓이고 그 왼쪽 node는 provider에서 inactive다. 실제 source에 바인딩된
\[
r=e^{-H\delta},\qquad
K=\frac{E_*}{E_*-E_-}
\]
에 대해 full remap의 active weight와 두 half remap의 active weight가 다르다. Candidate의 strict cell enclosure 안에서는
\[
w_{\mathrm{twohalf}}-w_{\mathrm{full}}
=K(K-1)(1-r)^2>0.
\]
이를 symbolic identity와 exact stored interval 양쪽에서 확인했다.

지정 column에서 full active weight는 약 \(0.131218064946\), twohalf는 약 \(0.319912042020\)이며 차이는 약 \(0.188693977074\)다. 해당 provider의 effective cross-section 차이는 약 \(1.19750789967\times10^{-18}\,\mathrm{cm^2}\)다. 두 remap은 photon number와 전파된 first energy moment를 보존할 수 있으면서도 threshold opacity moment는 보존하지 않는다. Moment 보존이 둘의 opacity 동등성을 뜻하지 않는다.

직접 characteristic 에너지는 half와 full 모두 cutoff 아래다. 이때 positive fixed-node opacity는 지정 provider와 fixed-grid projection 사이의 차이다. True atomic cross-section 정확도나 실제 photon 분포의 총 gas error로 해석할 수 없다. 계산 입력은 unit basis column이며 실제 전체 photon history가 아니다.

Arb 계산은 고정 binary64 leaf를 정확한 실수로 놓은 표현의 enclosure다. Native Rust의 각 곱셈, exp, 합산에서 발생하는 rounding을 같은 것으로 인증하지 않는다. 특히 source amplitude \(b\)의 수학적 lift는 고정된 birth vector를 선형 배율하는 정의이며 native rounded product를 모든 \(b\)에서 다시 계산한 family와 동일시되지 않는다.

자유 전파 에너지의 continuous emission, 두 endpoint birth, 마지막 endpoint birth 사이 순서도 같은 한계 안에서 유효하다. 이 차이는 energy moment이고 ionization error bound가 아니다. 증거: CHRONOLOGY_THEORY_KO.md, src/analyze_chronology.py, results/CHRONOLOGY_256.json 및 inputs/source_survey의 원문 binding.

## 7. 부호 이전 정리와 남은 gap

Augmented 상태 \(X=(z,U,V,W)\)에 대해 convex tube 위의
\[
D^+|X-\bar X|\le A|X-\bar X|+r
\]
와, ordered discrete map의
\[
E_{i+1}\le K_iE_i+\rho_i
\]
를 연결하는 충분조건은 타당하다. 연속 비교 행렬의 off-diagonal은 절댓값 derivative bound, diagonal은 signed derivative upper bound로 잡을 수 있다. Metzler 비교계의 이 구조는 단순 scalar 오차를 혼합 도함수 오차로 바꾸는 것과 다르다.

같은 parameter 사각형에서
\[
\left|\frac{I_x^{\mathrm{actual}}}{\lambda b}
-\frac{I_x^{\mathrm{ref}}}{\lambda b}\right|
\le B_{W_x}(t)
\]
가 성립하고 reference upper bound가 \(-m_{\mathrm{ref}}(t)\)이면,
\(B_{W_x}(t)<m_{\mathrm{ref}}(t)\)는 그 시각의 음의 부호에 충분하다. 전시간을 주장하려면 모든 해당 시각에 대해 필요하다. Parameter 축에서는 나눗셈을 그대로 실행하지 않고 혼합 평균의 연속 연장 또는 contrast 0을 사용한다.

현재 실제 \(B_{W_x}\)는 null이다. 새 공통 initial-state \(\lambda,b\) source family, accepted half1의 전체 checkpoint receipt, 정확한 half2 incoming state, trusted root/tube, uniform inverse 또는 preconditioner, augmented map의 \(K_i,\rho_i\)가 아직 없다. 역사적 point/root 자료의 존재는 이 새 family gap을 채우지 않는다. 반대로 이 gap 때문에 실제 background까지 없다고 말해서도 안 된다.

PHYS02의 inherited endpoint margin을 실제 오차 tolerance로 승인하지 않는다. 그 margin과 이번 remap weight 또는 \(\mathrm{cm^2}\) 단위 차이는 observable과 차원이 다르다. REMAINDER_OR_GAP.json이 이 구분과 null을 유지하므로 conditional theorem 채택에 지장이 없다.

## 8. 무결성, 필요한 수정 및 봉인

과학적 필수 수정은 없다. Reviewer의 무결성 검사 이후에도 검토 대상 18개 파일을 변경하지 않는다는 전제로 이 판정을 적용한다. 추가 notation 문서도 위 범위로 채택했다.

주요 hash:

| 파일 | SHA256 |
| --- | --- |
| REPORT_KO.md | fd574438f0cf5e73e7643c52c36e11341d2c08964ef147f3d87cfd96ec805916 |
| independent/REVIEW_TARGETS.json | a8e1a2db21e42db376ee0cae9e5fc8af127cd276e8735f63389db85679da20c5 |
| NOTATION_AND_INTERPRETATION_KO.md | cc17336010bb786dea7879090292f19e1023f555b8ccc8ce66d6d2cc98051b65 |
| results/CHRONOLOGY_256.json | aca8b36bd745dce156e514cafd42c228b59d72fc41dd446d2d48769f80378a7c |
| smooth_theory/NONAUTONOMOUS_EXACT_CHECK.json | 69f495579cbe82160a1d3d8c6766e8da19547f44601e8c6d93f935ad75a73989 |

모든 critical 파일의 실제 확인 hash, 25개 source 구간과 원파일 hash, 추가 로그 hash는 independent/REVIEWER_CHECKS.json 및 independent/DECISION.json에 보존했다. 이 reviewer 문서의 최종 SHA256은 DECISION.json의 review_document에 기록한다.

다음 작업은 닫히지 않은 범위에 맞추어야 한다. 실제 연산 순서를 반영한 quartic 분석, 초기 tangent 전달, source family와 augmented discrepancy의 연결이 필요할 수 있다. 이 판정은 그 작업의 수치 결과나 native 실행을 선승인하지 않는다. 이번 PHYS03 결과는 정의된 범위에서 봉인할 수 있다.
