# NCP local Codex — 관측량 중심 HH 개발계획 적용

대상 저장소는 cosmosapjw-quantum/WU088_HH다. 이번 작업은 2026-10-12 감사에 따른 개발계획 변경이며 새 과학 실행 결과가 아니다. 최종 전달문에 적힌 실제 plan commit을 기존 인증과 verified cache로 확인한다. 별도 첨부 요청 없이 Git 또는 기존 Drive/Dropbox의 완전한 계획 ZIP을 사용한다.

먼저 root CURRENT_DEVELOPMENT_PLAN.json과 이 폴더의 DEVELOPMENT_PLAN_KO.md, NEXT_DAG.json, OBSERVABLE_CONTRACTS.json, NCP_TASKS.json, review/PLAN_REVIEW.json을 읽는다. PHYS11은 C2 328372568144c4cdb6cdecd94c9c9bff984e103e / science subtree 34c49fd710dc89b78e65e021959168139c105fa8의 기존 scoped 결과를 재사용한다. 원 PHYS11 tree와 기존 source/checkpoint/실패는 수정하지 않는다.

## 현재 실행 판단

**heavy_queue=[]; launch=false; NO_HEAVY_JOB_READY.**

이 plan snapshot에는 실행할 NCP job이 없다. 한 번의 bounded 문서·identity intake 후 상태를 반환한다. 빈 큐의 benchmark, 무한 readiness polling, 임의 scan, 완료된 pair·PHYS 결과의 재실행을 하지 않는다. root의 이전 R31K-B/R31M benchmark 설명은 해당 과거 native 작업을 선택했을 때의 절차다.

다음 짧은 과학 작업의 담당은 HERE다. PHYS11의 같은 COMMON·고정 α·정규화 birth 강도 b_amp=1에서 λ=0→1의 ΔxHII와 Δw를 기존 uniform U 포함으로 평가하는 L0–L2가 예정되어 있다. 기존 mixed I_O를 절대 HH 효과로 부르지 않는다. full과 first_half는 같은 COMMON에서 출발한 별개의 첫 단계다. 이 계획에서 해당 평가를 수행했다고 기록하지 않는다.

## 다음 실제 NCP 이관이 생겼을 때

관측량의 필요성 또는 독립 HH microscopic 연구 질문, 준비된 실제 미완료 task manifest, lane별 입력, 이미 수행한 pilot의 wall/CPU/RSS/output, 독립 partition이 모두 전달된 경우만 NCP_TASKS의 admission 절차를 적용한다. 현재 이 문서만으로 future task를 실행할 수는 없다.

NCP는 64 cores / 128GiB 사양이며 56 workers / 112GiB는 정책 상한이다. 실제 자원과 task 수에 맞게 줄인다. time carry와 공유 gas coupling을 깨지 않고 독립 family를 병렬화한다. 오래 걸리고 실제 병렬 이득이 있는 미완료 부분만 실행한다. 기존 tolerance·정밀도·source/array identity·실패 기록·checkpoint와 ACK 조건을 유지한다.

HH_LCS_EFFECTIVE_IONIZATION과 HH_SINGLET_ION_PAIR는 다른 반응이다. latter의 H⁺/H⁻ 사건은 즉시 자유전자 증가가 0이며 LCS k의 대체물이 아니다. FT03 BE native와 frozen107 atomic native도 구분한다. 단순 소스 결과로 actual native root/U/V/W/I, cosmological history, full49, production을 승인하지 않는다.

다른 저장소의 코드·PR·현재 실행을 변경하거나 중지하지 않는다. 결과는 실제 실행 여부와 return status를 담아 반환한다. 현재 기대 반환은 다음과 같다.

```json
{
  "project": "WU088_HH",
  "active_plan": "hh_observable_first_plan_20261012_v1",
  "status": "NO_HEAVY_JOB_READY",
  "heavy_queue": [],
  "launch": false,
  "new_scientific_runs": 0,
  "new_ncp_jobs": 0,
  "next_science_owner": "HERE",
  "next_science_nodes": ["L0_FIXED_FAMILY_CONTRACT", "L1_ABSOLUTE_HH_RESPONSE", "L2_SCOPED_PHYSICS_RESULT"]
}
```

위 JSON은 수행 사실의 기록이 아니라 현재 계획에 따른 기대 반환 형식이다. 실제 readback/실행 상태로 채운다. Git commit·ZIP SHA256/크기·실제 양쪽 backup ID는 게시 후 작성되는 최종 전달문과 영수증에 있다. 그 값이 없는 이 내부 문서에서 미리 만들어 넣지 않는다.
