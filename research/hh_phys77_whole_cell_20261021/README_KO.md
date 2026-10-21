# PHYS77: finite-owner whole-cell enclosure

실제 PR131 HEAD `ec28299fe7e81aab184b93aff787cb00a185dd2e`를 조상으로 하는 [Draft PR132](https://github.com/cosmosapjw-quantum/WU088_HH/pull/132)의 additive 연구다. 과학적 기준 PR128은 유지한다.

**실제 미완료 DAG의 whole-cell source 의무를 진행해, frozen finite-L8 owner의 첫 cell 하나에서 8개 상태 모두 strict inclusion을 확인했다.** 이 cell의 연속 시간 전체에 대해 signed matter/radiation source를 따로 감싸고 PHYS76의 조건부 memory transport에 연결했다. 전체 z20→2 history와 angular/momentum continuum 의무는 열려 있다.

## 결과와 실행 범위

| 항목 | 현재 상태 |
|---|---|
| 유도 | first-exit defect tube 정리, captured monopole-row correction 포함 |
| 실제 cell | `mixed_s+0_m+1`, x=0→0.02242319570764566769…, z≈20→19.534353 |
| signed source | cell 전체에서 Pm>0, Pr<0; total endpoint S interval은 0 포함 |
| 가벼운 구현 검산 | exporter 9 + independent arithmetic/cell 16 + fake runner 17 = 42개 distinct controls PASS |
| 독립 원본 식 비교 | 120-digit dimensional reference와 46개 scalar containment 비교 PASS |
| 완료 계산 재실행 | 0; 최초 실패 결과와 수정 후 최초 성공은 별도 보존 |
| 새 ODE / NCP / benchmark | 각각 0 |
| 향후 NCP 입력 | 별도 3개 case × 첫 4개 cell, `READY_NOT_RUN` |
| 전체 history / angular continuum | OPEN |
| HH_R10 / production | OFF / NOT_ISSUED |

## 읽기 순서

- [REPORT_KO.md](REPORT_KO.md): 결론, 범위, 실패와 교정, 실제 계산의 해석.
- [theory/THEOREM_KO.md](theory/THEOREM_KO.md): 정의·가정·유도·증명·source mapping.
- [OPTIMIZATION_REUSE_KO.md](OPTIMIZATION_REUSE_KO.md): 실제 반영한 계산 구조와 외부 방법 재사용.
- [SHARED_RUNNER_KO.md](SHARED_RUNNER_KO.md): source/input identity, 완료 skip, 공유 lease와 pending checkpoint.
- [CODEX_HANDOFF_KO.md](CODEX_HANDOFF_KO.md): NCP에서 바로 사용할 bounded invocation.
- [NEXT_THREAD_HANDOFF_KO.md](NEXT_THREAD_HANDOFF_KO.md): 새 대화 재개 prompt.
- [RESEARCH_LOOP.json](RESEARCH_LOOP.json), [DAG_OVERLAY.json](DAG_OVERLAY.json), [EXECUTION_LEDGER.json](EXECUTION_LEDGER.json): 연구 단계, 과학 DAG, 실제 실행을 분리한 기록.

## 실행에 필요한 파일

`source/run_enclosures.py`와 같은 directory의 `RUNNER_SOURCE_LOCK.json`이 4개 실행 source를 고정한다. 상위 repo의 PHYS76 `interval_transport.py`와 HH74 `resources.py`도 SHA256으로 고정한다. `inputs/pending_ncp/`에는 request JSON 3개만 있으며, manifest와 preparation receipt는 별도 경로에 있다. 각 request 안에 coefficient table과 시작 상태·predictor node가 들어 있으므로 NCP에서 원본 raw archive를 다시 export하지 않는다.

NCP 실행 명령은 handoff에 있다. 이미 완료한 `inputs/REQUEST_FIRST_CELL.json`은 pending directory에 넣지 않는다. 이 첫 성공의 원래 source hash와 이후 guard-only 수정의 관계는 `verification/INPUT_GUARD_VALIDATION_BRIDGE.json`에 있다. 성공 receipt를 새 source hash로 바꾸지 않았다.

이론과 core는 exact captured coefficients가 정의하는 실수 IVP를 대상으로 한다. 과거 raw archive가 constructor table을 저장하지 않았으므로 현재 capture가 과거 미상 runtime의 table과 bitwise 동일하다고 주장하지 않는다. 과거 machine trajectory 전체를 포함한다는 주장도 하지 않는다.

현재 source는 CPython 3.12.14/NumPy 2.3.5에서 검토했다. Frozen request 실행에는 NumPy와 Python 표준 Decimal이 필요하며 C++/Julia 컴파일이나 새 solver 설치는 필요 없다. Runtime 차이는 새 identity로 기록된다. `verification/`의 역사적 검토 scripts는 최초 경로를 보존한 감사 자료이며 NCP 실행 진입점은 `source/run_enclosures.py`다.

## 기존 preliminary plot 재사용

PHYS76에 이미 게시한 [z20→2 stress time evolution](../hh_phys76_time_transport_20261021/figures/z20_z2/01_separate_stress_time.png)과 [parameter sweep](../hh_phys76_time_transport_20261021/figures/z20_z2/04_full_parameter_sweep.png)을 재사용한다. 1231개 long collisionless 이력, REI213 warm 729개, HH74 control 63개는 서로 다른 물리 범위다. PHYS77의 한 cell 검증으로 기존 전체 plot을 continuum certificate로 승격하지 않는다.

게시·백업 단계의 실제 HEAD/ZIP/provider 증거는 `delivery/`에 기록한다. 최종 HEAD는 자기 자신을 포함하는 commit 내부에 쓰지 않고 외부 최종 delivery receipt에서도 제공한다.
