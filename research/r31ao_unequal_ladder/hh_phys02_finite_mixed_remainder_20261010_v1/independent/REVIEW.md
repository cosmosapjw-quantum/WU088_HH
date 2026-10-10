# HH-PHYS02 독립 최종 decision review

**판정: PROMOTE_SCOPED.** 지정된 exact-real frozen continuous source에서 동일 초기조건의 photon–HH 혼합 응답에 대한 유한시간 음의 부호와 Taylor 나머지 상계를 승격한다. 이 범위의 blocking finding과 필수 수정은 없다. 원 구현·후보 생성·검증 설계에 참여하지 않은 별도 reviewer가 실제 파일을 읽고 판정했다.

검토자는 이 실행 문맥의 host developer metadata로부터 `GPT-6 Astra Pro`라는 모델 라벨을 읽었다. 부모 모델명으로 자식 모델을 추정하지 않았다. 별도의 runtime model ID나 attestation은 노출되지 않아 그 의미의 model identity verification은 주장하지 않는다. Astra v4 research `PROJECT_INSTRUCTIONS.md`, `docs/MODEL_ROUTING.md` 및 상태 템플릿을 읽었으며, 템플릿의 `NOT_RUN`을 과거 연구 증거로 취급하지 않았다.

## 1. 승격하는 정확한 주장

PHYS01의 봉인 입력 `inputs/SELECTED_SOURCE.json`에 기록된 **old_gas와 old_point_photons**를 모든 경로의 공통 초기 전체 상태로 유지한다. FT03의 H/He CI, RR, 두 DR, 열항과 expansion work, LCS의 HH 채널을 유지한다. density, photon energy, cross section, mean expansion rate는 하나의 source interval 안에서 고정한다. 남은 9개 활성 photon 좌표는 각각 전파하고, 16개 zero-cross-section 좌표는 정확한 상수로 제거한다. source는 원 index 24에만 연속 주입한다.

매개변수와 시간은

\[
 0\le\lambda\le1,\qquad 0\le s\le1,\qquad
 S=sS_*,\quad S_*={\rm binary64}(5\times10^{-15}),\qquad
 \tau=t/h,\quad h=1\,250\,000\,000\ \mathrm{s}
\]

이다. 모든 저장된 float와 rate literal은 해당 binary64 값의 exact real로 해석하고, 이후 초월함수와 산술은 실수식에 대한 Arb enclosure로 평가한다. native 중간연산의 rounding을 replay한 모형이 아니다. 단위는 gas fraction, eV/H, photons/H 및 proper seconds이며, `c`와 `k_B`를 명시적으로 유지한다.

\[
 I_x=x(\tau;\lambda,s)-x(\tau;\lambda,0)
       -x(\tau;0,s)+x(\tau;0,0)
\]

에 대해, \(\lambda s>0\)일 때

\[
 \frac{I_x}{\lambda s}
  \in C_3\tau^3+[L_4,U_4]\tau^4,\qquad 0\le\tau\le1,
\]

\[
 C_3\simeq-2.01590641628966920488326362037\times10^{-17},
\qquad
 [L_4,U_4]\subset
 [5.1715113729,5.4191014461]\times10^{-20}.
\]

따라서 **모든 \(0<t\le h\), \(\lambda>0\), \(s>0\)에서 \(I_x<0\)** 이다. \(\lambda=0\), \(s=0\), 또는 \(t=0\)에서는 rectangle 정의에 의해 \(I_x=0\)이다. 분모가 0인 축에서 정규화된 비를 계산한다는 주장은 하지 않는다.

최종 시각의 outward decimal 요약은

\[
 \frac{I_x(h)}{\lambda s}
 \in[-2.010734905,-2.010487314]\times10^{-17}
\]

이다. 전체 4차 이상 나머지의 크기는 cubic leading term의 **0.269% 미만**이며, 더 직접적인 상계는 \(0.00268818\,\tau\) 배이다. 이는 이 source의 cubic 시간근사에 대한 나머지 비율이다. 물리 모형 전체의 정확도 또는 실제 owner macro의 수치오차율을 뜻하지 않는다. 음의 \(I_x\)는 두 효과를 단순 가산했을 때보다 동시 효과가 작다는 뜻이며, HH 단독의 총 이온화 기여가 음수라는 뜻이 아니다.

권위 있는 수치 결과는 `results/REMAINDER_256_FINAL.json`이다. 정확한 dyadic endpoint와 더 긴 outward decimal은 해당 파일에 있다. 위 짧은 수치 표시는 그 결과를 바깥으로 감싼 것이다.

## 2. 논증을 직접 확인한 사항

정규화 시간 RHS를 \(F_\tau=h(F_0+\lambda H+sS_*B)\), \(J=\partial_zF_\tau\), 그리고 \(U=\partial_\lambda z\), \(V=\partial_s z\), \(W=\partial_\lambda\partial_s z\)로 쓰면

\[
 U'=JU+hH,\qquad V'=JV+hS_*B,\qquad
 W'=JW+(\partial_z^2F_\tau)[U,V]+hH_zV
\]

이며 초기 sensitivity는 모두 0이다. `HD`의 값/두 일차/혼합 성분은 이 확장계를 생성한다. mixed product의 두 cross term, reciprocal의 계수 2, exp/log 및 비정수 power의 chain rule이 맞다. 명시적인 source forcing을 중복 계산하거나 \(S_*\)를 두 번 곱한 항은 없다.

동일 초기조건과 매개변수 기본정리를 사용하면

\[
 I_x=\int_0^\lambda d\alpha\int_0^s d\beta\,
 W_x(\tau;\alpha,\beta)
 =\lambda s\int_0^1da\int_0^1db\,
 W_x(\tau;a\lambda,bs)
\]

이다. 따라서 전체 rectangle의 uniform sensitivity enclosure가 유한한 네 모서리 차이를 그대로 제한한다. 큰 상태값 네 개를 차분하여 작은 신호를 추측하지 않는다.

최종 13개 동적 좌표 × 4개 HD 성분의 **52개 모두 strict inclusion**을 얻었다. 코드가 확인한 식은 \(Y_0+[-1,1]|G(\mathcal Y)|\subset\operatorname{int}\mathcal Y\)이며 \(0\le\tau\le1\)의 적분상을 포함한다. 최초 exit에서 적분식이 여전히 strict 내부를 강제하므로 exit가 불가능하다. compact box 안에서 smooth RHS가 bounded하고 locally Lipschitz이므로 존재·유일성과 구간 끝까지의 continuation을 얻는다. 이 논증에는 별도의 contraction factor가 필수 전제가 아니다.

state box 전체의 온도는

\[
 T\in[49482.0213623046875,49496.134765625]\ \mathrm{K}
\]

이며 HH와 FT03의 온도 영역, H/He 분율과 simplex, 양의 열에너지·photon·입자수 조건이 모두 닫혔다. 따라서 사용된 실수 RHS는 전체 box 안에서 필요한 \(C^5\)보다 강한 매끄러움을 갖는다. 서로 독립인 sensitivity 구간은 실제 correlation을 버려 enclosure를 넓힐 수 있지만, 실제 sensitivity를 제외하지 않는다.

`Jet`는 ordinary time coefficient, 즉 시간도함수를 factorial로 나눈 계수를 저장한다. `flow_jet`의 recurrence \(z_{n+1}=F_n/(n+1)\)는 이를 유지하며, 각 차수의 전체 RHS를 계산한 뒤 모든 상태 계수를 갱신하므로 in-place 갱신으로 성분을 섞지 않는다. 전체 augmented box의 arbitrary point에서 얻은 `jet[0].a[4].c[3]`는 \(W_{x,\tau}^{(4)}/24\)의 uniform enclosure다.

PHYS01에서 계승한 \(W_x(0)=W_x'(0)=W_x''(0)=0\)와 매개변수에 무관한 cubic 계수에 Taylor 적분 나머지를 적용하면

\[
 W_x(\tau)=C_3\tau^3+
 \frac16\int_0^\tau(\tau-u)^3W_x^{(4)}(u)\,du.
\]

가중치가 비음수이고 그 총 가중치가 \(\tau^4/24\)이므로 signed interval도 나머지에 사용할 수 있다. 코드가 이미 factorial과 \(h\) scaling을 반영했으므로 추가로 24로 나누거나 \(h^4\)를 곱하지 않은 것이 맞다. 이 나머지는 4차 계수 하나가 아니라 그 뒤의 모든 시간차수를 포함한다.

독립 유도 문서의 초기 \(K_4\) tensor 식, \(S\) 독립·\(\lambda\) affine 구조, HI-only bilinear photo source의 초기 \(K_{4x}\)가 기존 photon의 두 순간을 통해 들어온다는 식도 가정과 함께 확인했다. 그 두 순간으로 전체 유한시간 photon dynamics가 닫힌다는 승격은 하지 않는다. 이 보조 대수 결과는 유한시간 sign의 필수 수치 증거를 대신하지 않는다.

## 3. Source 및 검증 근거

원 Rust와 Python 전사를 읽어 H/He 사건율의 정규화, 각 종의 CI/RR, 두 DR와 서로 다른 열에너지, RR kinetic loss, photon 소모·excess heating, HH의 \(n_H(1-x)^2\) 및 추가 1/2 부재, expansion work를 대조했다. 저장된 \(n_{He}\)의 binary64 값과 \(r=n_{He}/n_H\)를 유지한다. \(r\)을 다른 exact-real leaf인 `f_he`로 치환하지 않는다. Source auditor의 별도 결과도 동일한 전사를 지지한다.

| 증거 | 실제 범위 | 판정에서의 역할 |
|---|---|---|
| `logs/tests_initial.stderr` | 14 tests, exit 성공 기록: HD/Jet, scalar exact flow, domain, photon/channel 구조, tube, 초기 4차 구조 | 현재 algebra 및 source 구현 검증의 근거 |
| `independent/SOURCE_AUDIT_CHECKS.json` | 3개 상태에서 39 RHS·39 coefficient scalar 비교, 비영 initial sensitivity의 exact polynomial 계수 40개, nonlinear HD 4개 및 identity/bin/density 검사; 총 130 assertion | 다른 계산 경로에 의한 bounded source·chain-rule 검산 |
| `independent/K4_EXACT_CHECK.json` | 비물리 polynomial source의 6개 매개변수 조합에서 exact rational tensor/series 일치 | 새로운 4차 대수식의 구현 독립적 검산 |
| `results/REMAINDER_256_FINAL.json` | 전체 매개변수·시간 rectangle의 52성분 tube와 signed 4차 도함수 상계 | 핵심 유한시간 enclosure |
| `results/REMAINDER_384_CHECK.json` 및 `PRECISION_COMPARISON.json` | 한 번의 higher-precision 검사에서 sign/tube 유지, 최종 R4·I interval이 256-bit 결과 안에 있음 | 집중된 정밀도 일관성 확인; 물리 수렴 인증은 아님 |
| `EXACT_SERIALIZATION_CHECK.json` (이 review와 같은 폴더) | reviewer가 두 결과의 150개 ball, 즉 300개 decimal endpoint를 Fraction으로 직접 검사; signed sum·음의 부호·0.269% 부등식도 exact rational 검사 | 외부로 저장된 수치가 실제 enclosure를 보존함을 확인 |

Source auditor의 110자리 mpmath scalar는 독립적인 수치 oracle이다. 그 scalar 비교 자체를 엄밀 interval proof로 부르지 않는다. 핵심 bound는 Arb와 tube/remainder 논증에 의존한다. 130 assertion을 130개의 독립 물리상태나 130개의 science suite로 부르지 않는다.

Reviewer가 추가 수행한 것은 저장된 dyadic/decimal certificate와 source identity에 대한 경량 exact-rational 검사뿐이다. ODE trajectory, nonlinear BE root, native/atomic integral, NCP, parent 전체 suite는 수행하지 않았다. `INPUT_IDENTITY.json`의 6개 source/input size·SHA256과 source auditor가 기록한 candidate 4개 핵심파일 hash도 직접 일치 확인했다.

## 4. 보존된 최초 실패와 한계

첫 endpoint display는 방향성을 보장하지 않는 decimal이었다. `failures/NUMERIC_EXPORT_NOTE.json`이 이를 보존하며, 이번 판정은 exact dyadic과 directed 42-significant-digit decimal을 내보낸 `REMAINDER_256_FINAL.json`만 사용한다. 초기 display를 certificate로 사용하지 않는다. 현재 final 결과의 모든 endpoint를 reviewer가 정확 유리수로 검사했으므로 이 문제는 blocker가 아니다.

Source auditor의 최초 comparator는 independent scalar를 다시 Arb ball로 만든 뒤 그 전체의 containment를 요구했다. 변환에 따른 추가 radius 때문에 한 항목이 실패했고, 독립 110자리 scalar를 candidate의 exact endpoints와 직접 비교하도록 고쳤다. 최초 script와 실패를 보존했고 candidate scientific source는 바뀌지 않았다. 수정 후 기록은 130 assertion 성공이다. 이는 candidate 물리식의 실패로 분류하지 않는다.

이 판정의 증거 상태는 **derived + numerically checked + implementation-verified**이다. Python/Arb/FLINT 전체를 proof assistant로 형식 검증했다는 뜻은 아니다. 실제 검토한 파일과 content hash를 `DECISION.json`에 기록했다. 동일 hash와 동일 claim의 불필요한 재감사를 다음 단계의 조건으로 추가하지 않는다.

다음 주장은 계속 제외한다.

- actual owner의 full/two-half macro, BE root 존재·유일성·family certificate 또는 accepted chronology;
- 실제 time-dependent geometry, density, redshift/remap, source history, birth/reset·threshold crossing;
- 원 native binary64의 매 연산 rounding이나 native result의 정확도;
- HH atomic fit의 물리적 적절성·불확실성, 전체 energy ledger, 전체 angular grid 및 full history;
- 최대 유효 horizon, \(t>h\)의 부호, 추가 광종·He photo 또는 이번 rectangle 바깥의 매개변수;
- 다른 관측량의 유한시간 부호, total ON/OFF response의 부호 또는 production/physical admission.

Canonical S0 OFF, legacy 24/289와 265 unbounded, B22 open 등의 상태는 이 결과로 바꾸지 않는다. 새로운 독립 입력이나 consumer가 생기면 그 차이와 필요한 의존성만 다음 work unit으로 검토하면 된다.

## 5. 최종 disposition

`PROMOTE_SCOPED`: 위 §1의 exact-real frozen matched-source finite-time mixed-ionization sign와 remainder bound, 그리고 명시된 구조 가정 아래 독립 유도한 초기 4차 대수식.

`blocking_findings=[]`, `required_changes=[]`. 새로운 native 실행이나 owner macro 작업을 이 판정의 전제처럼 뒤에 추가하지 않는다. 그 작업들은 별도의 실제 입력·범위·gate를 가진 후속 주장이다.

최종 주 보고서에서 지적했던 K 단위 두 곳의 literal carriage return은 `\mathrm{K}`로 수정되었다. Reviewer는 변경된 두 표현, `CR_count=0`, 아래 최종 보고서 SHA-256만 확인하여 typography correction을 닫았다. Scientific audit를 반복하거나 scoped 판정을 바꾸지 않았다.

    WU088_HH_PHYS02_REPORT_KO.md
    21e8223ceca3358b7038d1dc06170fda887e249046443f9a01ad06d002a57b2b

최종 봉인 전 주 보고서 §5와 handoff의 표현을 “lambda²S가 4차부터 나타날 수 있다”로 좁힌 것을 확인했다. 이는 이 판정의 허용 주장과 일치하며, 실제 coefficient가 반드시 nonzero라는 새 주장을 포함하지 않는다. 변경된 문장과 최종 보고서 identity만 확인했고 scientific audit는 반복하지 않았다. 위에 표시된 보고서 hash는 이 마지막 주장 축소를 반영한 최종본이다.

이 REVIEW.md의 h·T 단위에 남아 있던 literal carriage return 두 곳도 roman s/K 명령으로 수정했다. 최종 control-character 검사에서 newline을 제외한 ASCII 제어문자는 0개였다. DECISION.json의 review_document hash는 이 수정까지 포함한다.
