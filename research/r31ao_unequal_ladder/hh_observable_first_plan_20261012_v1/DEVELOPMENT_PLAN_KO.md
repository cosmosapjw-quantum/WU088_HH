# WU088_HH — 관측량 중심 개발계획

2026-10-12 · 결정: **SCIENTIFIC_FAST_TRACK_RESET의 WU088_HH 범위 채택**

## 1. 바뀌는 개발 순서

앞으로 WU088_HH의 작업은 먼저 답할 물리 질문과 산출물을 정하고, 그 산출물에 필요한 입력·정확도·계산만 수행한다. 현재의 첫 후속 질문은 **동일한 고정 소스 계열에서 미래 HH 항을 켜고 끄면 수소 이온화 분율과 기체 에너지가 얼마나 달라지는가**다. 기존 결과를 재사용하는 짧은 평가부터 여기서 수행한다.

HH 연구는 독립 연구와 다른 프로젝트에 결과를 공급하는 역할을 함께 유지한다. 선택한 유효모형의 결과, Bianchi의 prescribed-history 수송, 정밀 native 인증, microscopic 충돌 연구는 서로 다른 산출물이다. 모든 산출물이 full49나 원 native의 전구간 인증을 기다리는 실행 순서는 사용하지 않는다. 해당 인증 자체를 주장할 때에는 원래 조건을 모두 유지한다.

이번 변경은 계획·진입 문서·작업 분담의 변경이다. 새 과학 수치, PHYS12 결과, 새 native 승격을 발표하지 않는다. PHYS11의 과학 파일과 판정은 원 bytes 그대로 재사용한다. `rei_bianchi`의 코드·실행·PR 상태를 이 변경으로 조작하지 않는다.

실제 다음 위치는 [NEXT_DAG.json](NEXT_DAG.json), 수량·단위 계약은 [OBSERVABLE_CONTRACTS.json](OBSERVABLE_CONTRACTS.json), NCP 분담은 [NCP_TASKS.json](NCP_TASKS.json)에 있다. 감사 채택 내역은 [AUDIT_ADOPTION.json](AUDIT_ADOPTION.json), 확인한 원문은 [SOURCE_REFERENCES.json](SOURCE_REFERENCES.json)에 기록한다.

## 2. 출발점: 완료된 결과를 다시 만들지 않는다

계획의 HH 기준은 `research/hh-phys11-joint-carry-20261011`, PR44의 C2 `328372568144c4cdb6cdecd94c9c9bff984e103e`다. PHYS11 과학 subtree는 `34c49fd710dc89b78e65e021959168139c105fa8`, delivery subtree는 `50f7f872d52c21ce2b8c23f1ec3c523f57464a54`다. 2026-10-12 06:09 UTC의 bounded refs/PR 조사에서 확인한 기준이며, 서로 다른 프로젝트의 여러 branch를 하나의 최신 head라고 묶지 않는다.

| 확인된 근거 | 이번 계획에서의 의미 |
| --- | --- |
| PHYS11은 두 same-COMMON 첫 단계의 33-group 및 장부 value/U/V/W carry를 완료했고 독립 `PROMOTE_SCOPED` 판정을 받았다. 기존 carry_v2는 4.0296초, 29,900 KiB의 실행이었다. | 완료 계산과 독립 검토를 재실행하지 않는다. source-family 조건부 결과와 기존 그림을 그대로 사용한다. |
| PHYS11의 actual native root/U/V/W/I는 null이며 second_half, 시간·연속체 remainder, 전역 보존은 OPEN이다. | 이번 우선순위 변경으로 OPEN을 PASS로 바꾸지 않는다. 작은 장부 residual을 시간 오차나 전역 보존으로 해석하지 않는다. |
| rei PR104는 이미 z=20→4+의 reduced history와 그림을 가지고 있으며, 14개 fine case의 기존 적분시간 합은 3.2106초다. | reduced 첫 그림을 새로 만드는 계획을 반복하지 않는다. 기존 결과의 해석과 다음 Bianchi 고유 관측량이 후속 목표다. |
| PR104 DAG의 S0–S2는 HH·CR·RCT 원 증명 경로에 의존하지 않는다. A_HH는 original mixed certificate만 차단한다. | 이미 문서화된 비차단 원칙을 HH의 실제 진입 안내와 실행 우선순위에도 적용한다. 의존성을 이번에 처음 해제했다고 주장하지 않는다. |
| rei PR110의 C12 gen96은 목표 epoch 1/129, 현재 배정 없음, scientific admission false다. 이전 G1_FINE의 129-epoch 완료·기각 기록은 별개다. | 일부 진척을 전체 native 승인으로 읽지 않는다. 현재 실행을 중지하거나 재개하는 권한으로 이 문서를 사용하지 않는다. |

원문: [HH PHYS11 보고서](https://github.com/cosmosapjw-quantum/WU088_HH/blob/328372568144c4cdb6cdecd94c9c9bff984e103e/research/r31ao_unequal_ladder/hh_phys11_joint_carry_20261011_v1/REPORT_KO.md), [rei PR104 보고서](https://github.com/cosmosapjw-quantum/rei_bianchi/blob/f66929c23ea3fa6e39dd4808e5b27d136c568a03/research/broad_history_20261010/REPORT_KO.md), [PR104 DAG](https://github.com/cosmosapjw-quantum/rei_bianchi/blob/f66929c23ea3fa6e39dd4808e5b27d136c568a03/research/broad_history_20261010/DAG.json), [C12 handoff](https://github.com/cosmosapjw-quantum/rei_bianchi/blob/17f8d0daa72e0f76a49cde01b110f650a6688c42/research/accel02_20261011/q1b/c12/HANDOFF.json).

## 3. HH의 두 반응 계열을 분리한다

### HH_LCS_EFFECTIVE_IONIZATION

PHYS01–11에서 선택한 유효 소스는

\[
F=F_0+\lambda H+SB,\qquad
H=(q,0,0,-\chi_H q,0_\gamma),\qquad
q=n_H(1-x_{\mathrm{HII}})^2 k_{\mathrm{LCS}}(T).
\]

여기서 \(\chi_H=13.598434599702\) eV이며, 이 기존 closure의 q에 추가 1/2를 넣지 않는다. q는 H핵당 초당 소스, w는 eV/H, 기존 P는 photons/H, nH는 proper cm⁻³다. 미래 항의 계수 λ를 바꿀 뿐, 과거 HH가 만든 상태나 이미 존재하는 광자를 삭제하지 않는다.

PHYS11은 이 선택된 소스 계열의 조건부 응답을 다룬다. 이 계열을 다른 미시 반응의 단면적·물리율과 동일시하지 않는다. [PHYS01 원문](https://github.com/cosmosapjw-quantum/WU088_HH/blob/328372568144c4cdb6cdecd94c9c9bff984e103e/research/r31ao_unequal_ladder/hh_phys01_photo_hh_competition_20261010_v1/START_HERE_KO.md).

### HH_SINGLET_ION_PAIR

frozen107/CP1의 singlet ion-pair 연구는 H⁺와 H⁻를 만드는 별도 microscopic 프로그램이다. 이 사건의 즉시 자유전자 증분은 0이다. 동일 population의 unordered pair는 n²k/2, 다른 population의 cross pair는 na·nb·k로 세고, 사건당 stoichiometry를 따로 적용한다. 이 1/2 규칙을 위 LCS 소스에 소급 적용하지 않는다.

singlet-only 계산은 unpolarized rate가 아니다. spin population, 충돌 에너지·impact parameter, 상대속도 분포, tail, 채널별 단면적과 오차가 필요하다. T와 균질성만으로 Maxwell 분포를 선언하지 않는다. 현재 physical rate는 미확보이며 H⁻를 삭제하는 coarse export도 허용되지 않는다. 이 연구는 자체의 충돌 관측량이 목표이면 독립적으로 계속할 수 있다. rei의 소비 요청을 기다릴 필요는 없다. [C3B 이론](https://github.com/cosmosapjw-quantum/WU088_HH/blob/328372568144c4cdb6cdecd94c9c9bff984e103e/research/r31ao_unequal_ladder/c3b_rate_contract_20261003_v1/C3B_THEORY_KO.md), [C4A 소스·장부](https://github.com/cosmosapjw-quantum/WU088_HH/blob/328372568144c4cdb6cdecd94c9c9bff984e103e/research/r31ao_unequal_ladder/c4a_local_source_20261003_v1/README_KO.md).

또한 `native`를 둘로 구분한다. `NATIVE_ATOMIC_FROZEN107`은 atomic C++ integral/trajectory provider이고, `NATIVE_FT03_BE`는 PHYS11 계열의 Rust BE root·분포·escape 구현이다. 한쪽의 정확성이나 성능 확인이 다른 쪽을 승인하지 않는다.

## 4. 산출물별 개발 경로

| 경로 | 다음 산출물 | HH 쪽 역할과 의존성 |
| --- | --- | --- |
| L: 선택된 HH 유효 소스 | 고정 모형의 HH-on/off ΔxHII·Δw와 비가산 응답의 구분 | 현재 HERE 우선. 같은 소스의 기존 U 포함을 재사용하며 full49 및 actual native 인증을 공통 선행조건으로 두지 않는다. |
| A: reduced reionization | 기존 평균 이력·천체물리 scenario·matched-H 대조 | rei 소유. 기존 PR104 결과 활용. HH 전체 완료를 대기하지 않는 소비 계약을 HH에서 유지한다. |
| B: prescribed-history Bianchi 수송 | 방향별 spectrum·anisotropy·Thomson polarization | rei/Bianchi 소유. 지정한 xe(t), Tb(t), 배경·tetrad·초기 복사장부터 시작할 수 있다. detailed HH는 필수 입력이 아니다. |
| C: 최소 복사–기체 결합 | 적절한 moment와 one-way/two-way 비교 | rei 소유. HH-OFF 또는 명시된 유효 closure로 시작한다. HH를 실제 추가할 때 채널·단위·오차를 명시한다. |
| D1: 실제 FT03 carry 인증 | actual root/response, 전 단계 연결, 시간·전역 주장 | PHYS11 원 DAG의 source/native graph, ray/guard, next-stage coverage 의무를 그대로 둔다. 해당 인증이 목표일 때만 이 경로를 선택한다. |
| D2: microscopic singlet ion-pair | 채널별 scattering/cross-section/rate의 자체 과학 결과 | frozen107의 기존 조건을 유지한다. 준비된 실제 충돌 관측량을 근거로 별도 경량·대형 작업을 선정한다. |

A/B/C는 외부 프로젝트와의 목표·입력 경계이며 이번 HH commit의 구현 완료 항목이 아니다. D1/D2를 새로 완료했다고 표시하지 않는다. HH 자체의 상세 반응물리가 연구 질문이면 그 가치로 작업을 정당화할 수 있다.

CAMB의 TanhReionization 및 CLASS의 reio_inter는 주어진 이온화 이력과 CMB 계산을 분리하는 실제 인터페이스 사례다. 이것은 Bianchi 구현의 검증이나 이번 프로젝트의 속도 측정이 아니다. [CAMB 공식 문서](https://camb.readthedocs.io/en/latest/reionization.html), [CLASS 공식 explanatory.ini](https://github.com/lesgourg/class_public/blob/master/explanatory.ini), 2026-10-12 열람. 첨부의 FlexRT 세부 성능 수치는 이번 계획의 NCP 비용 근거로 사용하지 않는다.

## 5. 첫 HERE 마일스톤: 절대 HH 기여

### 질문과 고정 대조

PHYS11의 정규화 photon-birth 강도 매개변수 b를 이 문서에서는 **b_amp**라고 부른다. PHYS01에서 사용했던 광자 birth 시각 b와 다르다. b_amp=1에 고정하고 같은 COMMON·같은 α·같은 계수·같은 source-stage의 λ=0과 λ=1을 비교한다.

\[
D_{\rm HH}O(b_{\rm amp})=O(1,b_{\rm amp})-O(0,b_{\rm amp}),
\qquad O\in\{x_{\mathrm{HII}},w\}.
\]

기존 비가산 응답은

\[
I_O=D_{\rm HH}O(1)-D_{\rm HH}O(0)
\]

다. 따라서 음의 I_x는 HH 자체가 이온화를 줄인다는 결론이 아니다. 기존 mixed 결과를 absolute HH efficiency로 이름만 바꾸지 않는다.

먼저 기존 `inputs/phys09/PROJECTED_RESULTS.json`의 U=∂λz가 같은 고정 α의 연속·매끄러운 root 계열에서 λ∈[0,1], b_amp∈[0,1] 전체를 포함하는지 원 계약과 함께 확인한다. 그 전제가 적용되면

\[
D_{\rm HH}O(1)=\int_0^1 U_O(\lambda,1)\,d\lambda
\]

의 기존 uniform enclosure를 재사용할 수 있다. 새 native solver나 full49 입력은 이 **조건부 같은 계열 평가**의 필요조건이 아니다. 적용 전제가 없으면 부족한 전제를 정확히 기록하고, 저장된 U를 actual history로 대체하지 않는다.

### 순서와 완료 기준

1. **L0 — bounded intake와 산출물 계약.** 대상 source/COMMON/α, 매개변수 이름, U의 적용 영역, fixed birth 설정, proper time을 묶는다. 읽을 파일은 이 질문에 필요한 작은 원문·저장 결과에 한정한다.
2. **L1 — 기존 포함의 국소 평가.** full d=1.25×10⁹ s와 first_half d=6.25×10⁸ s를 각각 같은 COMMON에서 출발한 별개의 첫 단계로 제시한다. 둘을 연속된 두 half나 cosmological history로 표시하지 않는다. 이미 있는 U 구간으로 얻을 수 있는 finite on/off 포함을 먼저 계산하고, 모형·입력 구간의 폭과 산술 오차를 구별한다.
3. **L2 — 물리 결과 한 장.** ΔxHII와 Δw의 구간·부호·차원을 표와 작은 그림으로 제시하고, 기존 I_O와 의미를 비교한다. 0을 포함하면 부호 미정으로 보고한다. consumer tolerance가 없으면 “무시 가능” 판정을 만들지 않는다.
4. **L3 — 다음 비용 결정.** 이 결과가 답하는 범위와 답하지 못하는 범위를 기록한다. 추가 정밀화가 실제 포함·부호·소비 결정을 바꾸는 경우만 다음 한 작업을 고른다. 범위가 충분하면 이 단계에서 끝낸다.

L0/L1은 다음 과학 루프에서 HERE가 수행할 예정이며 이번 계획 변경에서 실행 완료로 세지 않는다. 첫 평가는 저장된 구간 재사용과 bounded arithmetic으로 한정한다. 불필요한 과거 suite·기존 PHYS11 계산을 재실행하지 않는다. 별도의 긴 캠페인은 이 마일스톤의 자동 후속 작업이 아니다.

## 6. 정확도: 관측량과 주장에 맞춰 구분한다

**물리 항등식과 정의는 유지한다.** nuclei/charge·에너지·광자 장부, positivity, 단위·부호, source identity와 실패 보존을 성능을 위해 약화하지 않는다. 기존 frozen source의 허용 오차·정밀도·채널·배열도 변경하지 않는다.

새 결과는 수치 오차, 포함구간의 입력·계수 의존성, closure 차이, 천체물리 scenario 차이를 별도 열로 보고한다. scenario envelope를 통계적 신뢰구간이나 posterior uncertainty라고 부르지 않는다. 모든 내부 항목에 동일 상대오차를 요구하는 대신 결과의 사용 목적과 전달 오차를 먼저 정한다.

절대 오차 ε_abs, 필요할 때만 상대 오차 ε_rel, 0 근처 판정, 적용 구간, norm, 입력 범위와 종료 기준은 결과를 바꿀 실행 전에 고정한다. 현재의 L1은 **검증된 전제 아래 기존 uniform enclosure를 그대로 전달하는 결과**를 목표로 한다. 부호가 정해지지 않아도 유효한 포함을 보고하고 종료할 수 있다. cosmological significance를 주장하는 허용치는 아직 주어지지 않았으므로 `null / NOT_SPECIFIED`로 남긴다. 이 상태가 경량 결과의 보고를 막지는 않지만 “HH가 작아서 생략 가능”이라는 주장을 허용하지도 않는다.

감사의 |Δτ|≈2.6×10⁻⁵에 대한 10% 예시는 **paired Δτ의 절대 수치오차 약 2.6×10⁻⁶**에 관한 예다. 총 τ의 상대오차도, HH의 고정 tolerance도 아니다. PR104의 τ20→4는 전체 CMB optical depth가 아니다. 선택된 fesc·C·T scenario 효과가 shear보다 크다는 사실만으로 HH 영향의 상한을 얻지 않는다.

작은 차이는 가능한 한 response equation 또는 같은 입력을 공유하는 고정밀 paired 계산으로 평가한다. 10⁻¹⁷ 정도 mixed 신호를 별개의 binary64 네 이력 뺄셈만으로 인증하지 않는다. zero-containing 구간, signed/subnormal tail, 실제 실패는 그대로 보존한다.

## 7. 소비 인터페이스의 물리적 정의

`OBSERVABLE_CONTRACTS.json`의 정의를 우선한다. HH의 xHII=nHII/nH와 소비자의 xe=ne/nH는 다르며 xe에는 He 전자가 포함될 수 있다. nH는 H핵 proper density이고, 같은 정의의 ne=nH·xe로 연결한다.

양의 광로 optical-depth 증분은 dτ_path=c·σT·ne·dt다. 관측자까지 남은 τ_to_observer(t)=∫t^t0 c·σT·ne dt′라면 시간 미분의 부호는 음수다. conformal time η가 초 단위이면 dt=a dη이므로 양의 opacity 계수는 a·c·σT·ne다. η를 길이로 정의하면 c의 위치를 그 정의에 맞춰 바꾼다. dot-kappa의 부호나 c=1을 암묵적으로 옮기지 않는다.

Bianchi 평균 scale factor의 z_a=a_mean⁻¹−1은 일반적으로 방향별 관측 redshift와 동일하지 않다. 같은 H(a), scalar source·closure·초기조건의 평균 이력만 비교하면 matched FLRW stiff-fluid 배경과 퇴화할 수 있다. 이 조건부 논리는 모든 Bianchi 물리에 대한 no-go가 아니다. 방향별 spectrum·anisotropy·polarization의 비퇴화성을 별도로 확인해야 한다.

J_E가 angular mean intensity일 때만 Γ_s=4π∫J_E σ_s/E dE라고 쓴다. 표적당 heating은 4π∫J_E σ_s(E−E_s)/E dE이며 체적당 heating에는 표적 밀도를 곱한다. 각도별 I_E이면 먼저 ∫dΩ를 수행한다. photons/H를 photon density와 혼용하거나 nH로 중복 나누지 않는다. energy tail을 줄일 때는 Γ와 heating moment의 누락 범위를 따로 정량화한다.

## 8. NCP 64코어·128GiB의 실제 사용 조건

현재 `heavy_queue=[]`, `launch=false`, 상태는 **NO_HEAVY_JOB_READY**다. 이는 HH 연구 중단이 아니라 현재 실제 준비된 장시간 작업이 없다는 뜻이다. 짧은 데이터 읽기·구간 평가·계수 확인·작은 그림은 HERE에서 처리한다. 64코어를 채우기 위한 임의 parameter grid, 반복 벤치마크, 완료된 pair·consumer 재실행은 만들지 않는다.

NCP 이관에는 다음 과학적 근거 중 하나가 필요하다.

- 소비 관측량의 오차·민감도 분석이 추가 HH 정확도의 필요성을 보여 준다.
- 또는 구체적인 HH 자체의 microscopic 관측량이 독립 연구 목표이며, 그 목표를 위한 계산이다.

그 후에 실제 미완료 task와 immutable input, 준비된 실행기, dependency, measured pilot의 시간·RSS·출력량, 독립 병렬 단위가 있어야 한다. task는 lane별 선행조건을 충족한다. D1의 native 인증 작업과 D2의 충돌 작업에 동일한 선행조건을 기계적으로 강요하지 않는다.

병렬 단위는 실제 독립 physical family나 충돌 조건이다. 각 history 내부의 시간 전진은 순차적이고, 같은 gas에 결합된 energy group을 독립 history처럼 분리하지 않는다. 순차 stiff solver에 코어를 추가하는 것만으로 시간 문제가 해결된다고 가정하지 않는다.

NCP의 56 workers·112GiB는 8 cores·16GiB를 남기려는 정책 상한이며 측정된 최적값이 아니다. 실제 cpuset/quota/경쟁 작업/RAM 및 worker RSS를 보고 더 줄인다. 실효 worker 수는 task 수, CPU, 메모리, I/O 제약의 최소값을 넘지 않는다. 과거의 600초·8 family는 계획용 휴리스틱이지 실행 허가나 작업을 부풀릴 목표가 아니다. 현재 빈 queue에서 topology benchmark를 수행하지 않는다.

고정 계수 dN/dt=S−κN의 exponential update는 유용한 국소 알고리즘 후보지만, gas와 결합해 변하는 κ,S의 frozen-coefficient 오차는 따로 있다. C12 저장 진단은 stiffness 가설을 지지하는 입력이며 전체 solver의 order reduction 증명이나 측정된 가속률은 아니다. 이 계획은 해당 알고리즘을 구현·교체하지 않는다.

## 9. 작업과 전달 절차를 줄인다

이번 변경은 하나의 계획 묶음과 실제 진입 문서를 한 commit/PR에 담는다. 검증은 JSON·경로·DAG·변경 범위와 독립 계획 검토에 한정한다. 과학 suite, target benchmark, 과거 독립 판정의 반복은 수행하지 않는다.

앞으로 새로운 중요한 과학 주장·알고리즘 교체·승격 시 독립 검토를 수행하고, 같은 불변 결과에 대한 반복 리뷰를 기본 단계로 넣지 않는다. 긴 계산의 복구 지점, 중요한 연구 상태 변화, 사용자가 요청한 전달 시점에 backup을 만든다. 이번 전달은 사용자의 기존 요청에 따라 완전한 ZIP과 실제 Git/Drive/Dropbox 위치를 담은 최종 handoff로 마무리한다. 별도 첨부가 없어도 이전 PHYS11 원본과 새 계획을 회수할 수 있게 한다.

upload ACK·metadata 확인과 원격 download/restore의 byte 검증은 구분한다. 실제로 수행하지 않은 복원을 완료했다고 기록하지 않는다. 원 실패·checkpoint·source bytes는 보존하고, manifest 자신을 자신의 hash 안에 넣는 순환 식별자를 만들지 않는다.

## 10. 다음 호출에서의 시작점

HERE 연구 요청이면 L0→L1→L2를 수행한다. 한 번의 bounded 결과가 물리 질문에 답하면 종료하고, 실제 필요한 다음 작업만 L3에서 선정한다. NCP local Codex는 [HANDOFF_KO.md](HANDOFF_KO.md)를 읽고 현재 queue가 비어 있으면 **NO_HEAVY_JOB_READY**를 반환한다. 예전 README의 host benchmark나 과거 미완료 handoff를 현재의 자동 실행 지시로 해석하지 않는다.

성공 기준은 원자물리 provider들의 일괄 PASS가 아니다. **선택된 물리 질문에 대한 재사용 가능한 결과, 그 결과의 정확한 적용 범위, 추가 비용이 필요한 이유 또는 여기서 멈추는 이유**를 한 묶음으로 제공하는 것이다.
