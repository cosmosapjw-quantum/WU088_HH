# PHYS23: HH rate envelope → observable budget

## 확정된 출발점

PHYS22의 `DECISION.json`, `INPUTS.json`, `results/interval_result_v3.json`, `checks/EXACT_AUDIT.json`, `report/REPORT_KO.tex`를 읽는다. 채택된 목표는 고정 warm P01, gas4/photon2904, t∈[0,1e11] proper seconds, 동일 IC/source/geometry/closure의 명시적 실수값 명목 모델이다.

공통 first-exit tube와 비교계는 λ∈[0,1]의 유한 해 차이를 직접 닫는다. endpoint ΔT∈[-5.83789,-5.57637]e-11 K, Δe∈[7.60418,8.28307]e-16 electrons/H. 가중 비교행렬 norm은 0.03688471538571053이다. PHYS21의 PL tangent를 재생산하거나 동일 source 표를 다시 만드는 작업을 기본 다음 단계로 삼지 않는다.

## 다음 연구 질문

현재 유한 응답 포함을 **물리적 HH rate 불확실성과 수신 관측량의 명시적 오차 예산**에 연결한다. 기존 HH_DOMAIN_SCREEN → HH_MATERIALITY의 구조를 유지한다.

1. 원 effective ionization H0+H0→H+ + H0 + e_free 채널과 온도 영역이 일치하는 원전·코드·microscopic 입력을 먼저 회수한다. singlet H+ + H− ion-pair 채널과 event/rate convention을 섞지 않는다.
2. 이용 가능한 근거로 k_-(T)≤k(T)≤k_+(T)를 구성한다. 문헌에서 상대 오차가 정량화되지 않았다면 서로 다른 실제 rate prescription을 구별해 비교하고, 수치 envelope를 측정 오차로 자동 해석하지 않는다.
3. PHYS22의 source/geometry·교차항 majorant를 재사용한다. 바뀐 k envelope가 영향을 주는 q, gas first-exit 및 finite comparison만 갱신한다. 모든 λ와 두 해가 같은 공통 영역에 남는 것을 유지한다.
4. 실제 수신 interval과 T/e/τ/visibility 등 요청된 observable 및 budget을 고정한다. 현재 warm endpoint에만 필요한 예산이라면 |ΔT|≤5.83789e-11 K 및 |Δe|≤8.28307e-16를 즉시 활용한다. 다른 시나리오나 긴 history에서는 해당 입력·시간 범위를 새로 포함한다.
5. 직접 유도, CAS/수치 확인, source accuracy, native implementation의 근거를 각각 기록한다. 별도 reviewer가 없으면 같은 assistant의 복수 경로로 정확히 표기한다.

## 재현·보존

명령과 출력은 `REPRODUCE.md` 참조. NPZ와 emissivity bytes가 이번 묶음에 들어 있다. `raw/`의 v1 syntax 실패, v2 수 표현 교정, v3 채택과 xAct metadata 교정을 보존한다. 구간 v3를 다시 돌려야 할 과학적 이유가 없는 동안 저장된 majorant와 exact closure를 직접 재사용한다.

HH_STRICT_NATIVE, HH_SINGLET, 전체 RUX 및 physical-admission 의무는 각 원 근거대로 독립 보존한다. 새 HPC queue는 비어 있다. 원격 게시 상태는 외부 `DELIVERY_RECEIPT`의 실제 object ID·commit을 사용한다. 업로드 확인과 복원 확인은 서로 다른 상태다.
