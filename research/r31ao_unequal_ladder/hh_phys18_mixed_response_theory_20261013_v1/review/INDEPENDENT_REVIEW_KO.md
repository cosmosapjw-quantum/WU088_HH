# PHYS18 독립 과학 검토

검토자 `/root/hh_phys18_mixed_review`는 원 PHYS15/16/17 source·carry·계약과 새 PHYS18 유도·application을 별도로 읽었다. 새 implicit mixed forcing, photon chronology, 원 inverse 전달, 유한 온도·interaction에 대하여 **PROMOTE_SCOPED**를 지지한다. 적용 범위와 exact file identity는 동반 `INDEPENDENT_REVIEW.json`에 결박한다.

## 1. 채택 결과

동일한 COMMON, 고정 admissible α, 공유된 전역 λ,b∈[0,1]²와 원 C² source/root 조건에서

\[
\partial_{\lambda b}\Delta T,\ \mathcal I
\in[-2.668505746423,-2.118796636045]\times10^{-12}\ \mathrm K
\]

가 성립한다. I는 같은 α의 네 corner 대비다. 상한의 음의 여유는 2.118796636045×10⁻¹² K 이상이다. M3 직접 implicit 포함도 음수이며, M4 상관식은 작은 stage·endpoint 차이를 보존하여 실제 폭을 줄였다.

임의의 양의 면적 parameter subrectangle에는 면적을 곱한 같은 포함이 적용된다. 따라서 이 유한 온도 결함은 strict submodularity를 가지며, b가 증가하면 Fλ가 감소하고 λ가 증가하면 Fb가 감소한다. 각 1차 도함수의 원 부호 Fλ<0, Fb>0는 PHYS17의 전역 포함을 재사용한다.

## 2. 독립 방법과 실제 실행

`checks/independent/review_arithmetic.py`는 후보 evaluator와 PHYS14 helper를 import하지 않는다. 검토된 PHYS17 독립 검사기의 정확한 유리수 interval primitive를 재사용하고 새 혼합 식을 직접 작성했다. 후보의 256-bit outward 연산과 달리 중간 rounding 없는 유리수 연산을 사용한다. 4×4 inverse majorant는 후보의 소거법 대신 24항 Leibniz determinant와 Cramer 공식으로 검산했다.

광자 mixed 전파에는 값·λ·b·λb를 두 nilpotent 변수의 다항식 계수로 두고 coefficient convolution을 구현했다. Absorption의 혼합 도함수는 analytic primitive로 따로 구성한다. 실제 일곱 sector×35 photon/guard slot×4 coefficient=980개 모두 후보의 해당 포함 안에 들어갔다. M13 stage 식과 number/energy mixed ledger도 별도로 재구성했다.

두 번째 독립 실행은 **22/22 PASS**, 자체 wall 1.370457 s, wrapper wall 1.468329 s, peak RSS 48,604 KiB로 끝났다. 원 source callback·새 nonlinear root·history replay는 각각 0회다.

| 독립 점검 | 실제 확인 내용 |
|---|---|
| 원 계약·입력 | 계약의 24개 SHA/size, 실제 evaluator의 16개 입력 identity |
| 원 mixed carry | 첫 half·둘째 half·Full U,V,W의 36 gas 성분, ordinary ∂λb 의미 |
| source slot | Ggg 64개, Ggλ/Ggb 32개, Gλb 4개가 원 signed Hessian slot과 일치 |
| mixed direct | M3의 JF W+B(gF;UF,VF), Taylor factorial 없음 |
| mixed correlated | M4의 9개 endpoint 보정, M5/M6의 dₓ 인자, M7의 q Hessian 선분 포함 |
| C² source bridge | W₁,V₁ 방향의 정확한 density/temperature pullback·He projector 첫 미분 |
| stage source | M8–M11의 9개 gas residual sector |
| photon | 980 coefficient 포함, 35-slot M13, mixed number·energy ledger |
| inverse | 원 C,B,q,S 및 centered JF, Cramer majorant, signed fixed-point 3회 |
| finite observable | M15/M16의 동일 ΠF, 여섯 quotient geometry 항, 직접·상관·원 carry 교집합 |
| physical readout | 25개 RHS를 중복 없이 3개 그룹으로 묶은 같은 inverse·covector 전달 |
| finite contrast | 전역 mixed interval의 면적 적분, 원 prior와의 폭·magnitude 비율 |

## 3. 이론식의 검토

M3는 H(gF;λ,b)=0을 두 번 미분한 표준 implicit tangent 식이다. M4는 rλb=JyW+B(g₂;U,V)에서 JF Wd를 뺀 후 동일 Hessian의 bilinear 차이를 전개하여 얻는다. 이 과정은 원 source의 C² 정칙성만 사용한다. Hessian 값의 차는 공통 signed 범위의 차로 포함하였으며, 추가적인 Hessian-Lipschitz 상수를 가정하지 않았다.

Full incoming QF=RFZ₀+2bJ의 factor 2와 Full duration의 ℓ=2ha는 서로 다른 위치에서 생긴다. 실제 Hgb=2ΣνℓJ/D²와 그 공간차에 두 인자가 모두 올바르게 반영되었다. 원 Gλb의 미세한 subnormal 폭은 원 gas-fixed affine 구조에서 얻은 정확한 0과 교차했다.

일곱 photon sector는 remap R과 absorption diagonal A의 순서를 유지한다. b가 앞에 붙은 birth sector는 mixed 미분에서 직접 λ derivative가 남으므로 b=0의 sector 값과 mixed response를 구분한다. Number/energy guard를 유지한 ledger와 실제 Full photon 차이의 (18.43) 부호도 일치한다. 활성 heat leaf는 exact(Ej)−exact(χH)와 실제 원 bit 자료에서 일치함을 확인했다.

N=FΠF를 혼합 미분하여 finite temperature 식을 얻고, ΠF,λb=le(W−Wd)를 넣으면 Wd의 계수는 nF=CTew−TFle가 된다. 선형화된 분모로 바꾸지 않았다. 혼합 미분과 같은 α의 네 corner 대비를 연결한 FTC, marginal ordering, 축의 정확한 비선형성을 보존한 cross reconstruction도 모두 검토했다.

균형 bilinear 식 (18.15), 대칭 Hessian contraction (18.16), true-Full photon mixed 식 (18.43), finite Neumann tail (18.48)는 완결된 항등식·경계로 채택한다. 이들의 모든 추가 tightening 경로를 새 수치 실행했다고 기록하지 않는다. 현재 부호 판정은 실제 run02/readout01에 근거한다.

## 4. Wolfram와 xAct

새 Wolfram source와 실제 raw output을 읽었다. Wolfram 15.0.1에서 공식 xTensor 1.3.0, xPerm 1.2.4를 불러오고 WL group backend를 사용했다. 7개 abstract-index tensor 식과 14개 scalar/matrix 성분이 모두 정확히 0이었다. Mixed chain rule, M4 cancellation, bilinear/Hessian 대칭, M5/M6 rational difference, mixed absorption primitive, finite T 및 비가환 2-slot photon graph가 포함된다.

원 output의 Symbol::undefined2는 의도적으로 임의의 scalar function head HH18/B18을 사용하는 형식미분에서 발생했다. 원 메시지와 formal derivative를 보존한 상태로 항등식 양변이 정확히 소거되었으므로 해당 algebra 검산의 blocker로 판정하지 않았다. 물리적 35-slot 포함은 위의 별도 실제 interval 실행에서 확인했다.

## 5. 실패 기록과 최소 교정

주 application run01은 guard field를 정수 key로 읽다가 실패했고, 원 PHYS14의 `number`, `energy_eV_per_H` 명명 slot으로 접근하여 run02에서 성공했다. 실패 코드와 로그가 보존되어 있다.

독립 checker run01은 19개 항목을 통과하고 prior 표현 검사 하나에서 실패했다. 원 exact decimal 1.958485175177039e−9는 저장 시 256-bit outward dyadic interval이 되므로 singleton일 필요가 없다. 검토기의 `point()` 가정을 **정확한 원 decimal이 저장 interval에 들어감**으로 교정했다. 생산 코드·결과는 전혀 변경하지 않았다. `CHECKER_CORRECTION.json`과 첫 실패 checker를 보존하고, 새 grouped readout 검사를 더한 run02에서 전체 22개를 통과했다.

후속 계약의 두 first-derivative field를 실제 원 JSON의 `nonphoto[*].gradient`로 교정한 수정본을 검토했다. 마지막 메타데이터 검사에서는 nested interval object와 그 `exact` member를 혼동한 독립 검토기 비교문을 교정했으며, 원 실패 검사기와 교정 기록을 보존했다. 이후 후속 계약의 23개 파일 identity·실제 read field, corollary의 여섯 exact interval, outward 소수와 cross midpoint/radius 일치가 모두 통과했다. 이 검사는 기존 결과의 포함 관계를 다시 계산하거나 새 물리 실행을 한 것이 아니다.

## 6. 문헌·신규성·NG1–NG7

SciSpace와 Exa를 실제 사용하여 SLN15의 2차 tangent theorem, Lewis의 C² reduced Hessian, Pacaud 등의 tensor contraction/adjoint 및 Xue의 incremental sensitivity를 원문에서 대조했다. Neumaier/Rump의 validated sensitivity·preconditioning 전제는 PHYS17의 완료된 읽기 기록을 재사용했다. 이번 성과는 원 WU088_HH 자료에 대한 상관 혼합 결함의 구체적 포함과 물리적 방향이다.

새 strong no-go를 주장하지 않는다. NG1–NG7 심사는 정확한 family·양화, 논증의 닫힘, 상속된 존재하는 기초 모델, 실제 mechanism, 다음 연구 선택에 미치는 귀결, 가까운 원전과의 범위 비교, 독립 검토로 나누어 완료했다. 부호가 음수라는 결과를 전체 물리 이론의 불가능성으로 확장하지 않는다.

## 7. 다음 pure-curvature 계약의 준비

`NEXT_CURVATURE_PROPOSAL_KO.md`의 C1–C20도 독립 검토했다. JkKk=−(Hgg[pk,pk]+2Hgθpk+Hθθ), carried incoming Q₂,θθ, source 시각·공간 차, finite temperature의 factor 2가 맞다. 양의 convex interpolation weight와 음의 Peano kernel을 사용한 signed bilinear remainder 및 (Mλλ+Mbb)/8 상계도 C²에서 성립한다.

새 first-half inverse readiness는 원 A_Gg의 16개 성분에서 별도로 재계산했다. C₁=I, S₁=diag(1,1,1,13.5)에 대해

\[
q_1=\frac{5095881330588929517}{9444732965739290427392}
<0.0005396<1
\]

이 일치했다. `checks/independent/preflight01/CURVATURE_PREFLIGHT_REVIEW.json`에 별도 PASS를 기록했다. 이것은 첫 half의 선형 inverse 준비이고 두 pure RHS·응답의 새 application 상태는 not_run이다.

수정된 후속 계약의 SHA256은 `6c41482b636e14f5c8bea6ad70c1f7698fbf21f4c4bbc1141b469f746d1c1126`이다. 23개 입력의 실제 size·SHA와 JSON/함수 read field를 `checks/independent/SUCCESSOR_BINDING_CHECK.json`에 결박했다.

현재 blocking finding은 없다. 다음 pure-curvature 연구의 새 수치 의무는 그 단위의 계약과 실제 상태로 관리한다.
