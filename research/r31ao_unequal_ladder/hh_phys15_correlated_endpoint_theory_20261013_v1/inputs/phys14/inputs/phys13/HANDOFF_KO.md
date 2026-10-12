# PHYS13 후속 연구 인계

현재 과학 결과는 `REPORT_KO.md`, `theory/THERMODYNAMIC_RESPONSE_THEOREM_KO.md`, `results/thermo_v2/THERMO_RESULTS.json`이다. 최종 독립 판정은 `review/DECISION.json`의 PROMOTE_SCOPED다. 새 source/kernel/inverse/native root를 실행한 결과로 해석하지 않는다.

## 보존하고 재사용할 것

- 동일 α 및 원 source/C² root 포함 전제 아래 PHYS13의 유한 ΔT/Δe/Δn_e, 냉각 분해·비중, 일차 projected energy와 χ_eff를 재사용한다.
- 온도·전자 정의에는 exact(nHe_stored)/exact(nH)의 fhat와 원 kB/ev leaves를 사용한다. f와 fhat를 합치지 않는다.
- 미래 HH λ, 미래 birth b의 switch는 과거 HH ON·기존 photons·compensation을 지우지 않는다.
- PHYS09의 mixed temperature는 재사용한 기존 결과다. PHYS13의 새 ratio와 birth-only readout, 실제 계산하지 않은 electron ratio를 구별한다.
- Full과 first_half는 같은 COMMON에서 시작하는 두 별도 첫 단계다. 두 표를 더해 carried history를 만들지 않는다.
- 새 결과는 provider observable이며 실제 consumer admission, 전체 RUX 완료 또는 production을 뜻하지 않는다. 원 8개 HH DAG 노드와 global source DAG는 그대로다.

## 다음 물리 작업

실제 소비 요청이 있으면 전체 source/scenario/COMMON/고정 계수/연산자 관계와 관측량 정의를 결박한 뒤 기존 HH_DOMAIN_SCREEN으로 진행한다. 이번 타겟 조사에서는 요청이 결박되지 않았다. 같은 최신성 검색을 반복할 필요가 없다.

실제 다음 시간 단계의 온도 응답을 연구하려면, PHYS11의 source-aligned gas·photon 공동 carry와 실제 ray/guard 입력을 먼저 사용해야 한다. 원 `prebe_words.bin`의 identity와 layout은 PHYS11 `SOURCE_TO_CARRY_MAP_KO.md`에 보존돼 있다. 그 payload 확보와 fixed-family source coverage를 위한 작은 연산부터 시작하고, 완료된 첫 단계·원 H anchor·과거 과학 suite를 자동 재실행하지 않는다. 다음 implicit 단계의 root 포함이 확보된 뒤에만 유한 온도 전이를 계산한다.

독립 microscopic singlet/FT03 strict-native 경로는 원 source·basis·native authority 조건을 유지한다. 새로운 local/native 실행 예산이나 원 native authorization gate를 이 인계문으로 덮어쓰지 않는다. 이번 `NCP_TASKS.json`은 빈 큐이며 launch=false다. 작은 payload 문제를 heavy job으로 분류하거나 빈 큐를 benchmark하지 않는다.

## 파일과 실행

원 입력과 실제 실행 기록은 `inputs/`, `evidence/`에 있다. 새 재현을 수행할 물리적 이유가 있을 때만 새 출력 디렉터리로 `python3 src/thermo_response.py --out /absolute/new/path`를 실행한다. 원 `thermo_first`와 `thermo_v2`를 덮어쓰지 않는다. 독립 검토는 이미 완료됐으며 추가 전면 리뷰나 과거 suite 반복은 필요하지 않다.
