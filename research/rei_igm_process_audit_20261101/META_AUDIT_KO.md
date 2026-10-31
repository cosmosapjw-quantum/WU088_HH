# WU088_HH 연구 운영의 적대적 메타 감사 | 2026-11-01

## 감사 경계와 재현 가능한 출처

이 심사는 물리 이론·수치 산출물의 존재를 부정하지 않는다. 원래 **REI Bianchi IGM** 중앙 연구 미션에 비추어 과제 선정, 실제 소비자 연결, DAG 완료 증거, 소스 provenance, PR·백업 비용, 운영 문서의 최신성을 판정한다. **동일 모델에 의한 적대적 자체 검토**이고 제3자 독립 referee는 NOT_RUN이다.

현재 GitHub 원전:
- REI 원계획 `cosmosapjw-quantum/rei_bianchi/docs/atomic_reionization_handoff_20261004_v1/RESEARCH_PROGRAM_KO.md`와 `GLOBAL_DAG.json`, source Git blob `d95c959dc22f8b4549e14eff23b2b4ff083a2e35`: 31개 원계획 작업. 원계획의 기본 관측/물리 목표는 source-qualified 첫 reionization paired history, 원자 owner와 우주론 계산자 분리, HH·He 정밀연구의 조건부 호출, 응용 소모자 한 번만 실행이다.
- REI `research/orchestration_expansion_20261025/FROZEN_STATUS.json`: 87-node 중앙 확장 compiler, 39개 owner/closure 필드 부족. `research/rei_physical_fast_20261028/STATE.json`와 최신 REI Draft PR #317 `45154b5d661296ec4ae5d39bc1d1502c1d9761f3`: 중앙 **28/88**, working **33/88**, F4 **4/7**, L4=false, PRODUCTION=HOLD, recent delta=0. 31/87/88은 시간과 범위가 다른 세 DAG snapshot이다. 공통 분모가 아니다.
- WU 실물 `research/wu_hd_source_bound_r18_20261029/DAG.json` Git blob `8428fcc97ab47376882175fba094973982a6da88`: 49 object, 34 COMPLETE_SCOPED, central/physical delta=0, immutable inherited48. `original_next_task=WU_HD_REACTIVE_STATE_SOURCE_NEXT`, named REC/CR consumer, matching states/n/T/clock and energy budget still OPEN. Latest WU R45 PR #184 was Draft HEAD `bad4fc9bfe7ce16fcf359841ef5db8452b2b4338`.
- Original P0/P1/P2 successors `rei_bianchi/docs/fastest_track_chat/REI-CODEX-SCIENCE-20261014/EXECUTION_DAG.json`: RUX00/RUX02-05 source+FLRW first interval; RUX06–08 matched Bianchi; RUX09–11 observables. HH/He/CR precision extensions are optional, no all-extensions AND gate.
- REI owner nodes `research/orchestration_expansion_20261025/node_plans/REI-EXP-SCENARIO.md` and `REI-EXP-EVENT-CONSUMER.md` require actual named state/source/clock, correct normalization, unique energy owner, no invented rates. `REI-L4.md` still WAITING_SELECTED_PHYSICAL_BINDINGS.

## 발견 사항: 가장 강한 형태로 공격한 뒤 범위를 제한한 판정

### MA-01 (CRITICAL, mission drift): 표면적 산출물의 증가와 중앙 물리 DAG의 무진전
WU PR #173–#184, R34–R45 12개 연속 Draft에서 최신 WU 34/49 (+0); 특히 R43 136,419행, R44 318,846행, R45 80,796행은 서로 다른 조건의 **source-derived model rows**이다. REI F4 PR #295–#317에도 여러 original-source 이벤트·CCC·Li·He 파생 산출물이 있지만 소유자 PR #317 자체가 중앙28/88 및 F4 4/7 (+0)를 보고한다. 그러므로 '많은 계산'이나 '많은 PR'이 본래 IGM 목표에 대한 완료 노드를 증명하지 않는다.

*반론:* 이 중에는 미시물리와 미분/보존·photon bookkeeping에서 실제 성과가 있다. 고품질 source 확보와 불확실성 제거는 응용의 전제다. 문제는 연구의 가치 부재가 아니라 그 성과를 원래 **누가, 어느 상태와 clock에서 소비할지** 계속 미루는 자동 연구 선택이다. **최소 수정:** 신규 분자를 추가하지 말고 기존 REI-EXP-SCENARIO/RUX05를 다음 default로 하고 WU source lane을 조건부 호출한다.

### MA-02 (CRITICAL, scientific semantic mismatch): R45 우주론 이력은 IGM/Bianchi physical consumer가 아니다
R45는 출판 Faure21 rate를 바탕으로 가정된 초기 이온화·Compton 배경의 균질 FLRW (z=1500→30)를 적분하고, 임의 생성준위와 고정배경의 52상태 molecule을 연결했다. 이 이력은 잠정 재이온화 시대 후보 (6≤z≤10)도, 별도의 재이온화 이후 Lyα/UVB 보정 구간 (2.4≤z≤4.75)도 포함하지 않는다. 따라서 Bianchi I 시선 방향·광자 수송·완전한 thermo-chemical Q·실제 REC/REI state의 소비를 입증하지 않는다. 'real physical data rows'라는 구어는 관측값 또는 실제 공진화 production output으로 읽힐 위험이 있다. H+ 충돌 grid와 gas Q의 부재도 구분한다.

*최소 수정:* 출처있는 수치 결과는 **conditional model**로 보존한다. 동일 관측량에의 영향/소스 지원/도메인 정합성이 확인되기 전까지 HH/HD는 REI 기본 시나리오의 필수 dependency로 만들지 않는다. 필요하면 materiality 검산으로 재호출한다.

### MA-03 (HIGH, priority inversion): 소비자보다 공급자 refinement가 우선
WU 원시 49 DAG는 REI-like molecular source/owner에 국한된 후속 `WU_HD_REACTIVE_STATE_SOURCE_NEXT`의 native state/density/clock을 조건으로 명시한다. R43–R45는 original EMAA/Grackle/Faure 자료로 source competence를 크게 넓혔지만 정작 named REC/CR/REI importing callback과 동일 에너지 ledger를 하나도 admission하지 못했다. REI F4도 frozen BASS193의 점·event·first-collision 대상을 여러 번 확대했으나 shared H/He+photon+thermal history가 아닌 응용 전 단계다.

*최소 수정:* science-grade NEXT_CONSUMER_UNIT에 실제 owner·source·observable·domain을 지정하고, 입력이 맞지 않으면 오직 그 물리적 불일치만 반환한다. 기존 SOURCE→CONSUMER seam을 중복 구현하지 않는다.

### MA-04 (HIGH, authority drift): root SSOT와 actual HEAD 간 시간 불일치
WU root `AGENTS.md` 최상단 priority는 여전히 R18(2026-10-29), root `CURRENT_DEVELOPMENT_PLAN.json`은 PHYS19(2026-10-13), live research는 R45(2026-10-31). REI `main`의 PROJECT_STATE는 2026-08-11, 이후 F4 owner 작업은 계속 Draft PR에 누적된다. 따라서 root/branch/dated DAG 중 어느 것이 최신 작업 선택의 authority인지 정하지 않으면 history로 fallback하거나 오래된 완료 조건을 재사용하기 쉽다.

*최소 수정:* immutable historical files는 건드리지 않고 WU root `CURRENT_MISSION_DAG.json`을 **현재 routing SSOT**로 지명한다. root AGENTS와 README에는 짧은 pointer만 추가한다. REI owner central DAG는 읽기 전용으로 둔다.

### MA-05 (HIGH, Goodhart/metric contamination): workflow completion을 science admission과 혼합할 위험
20단계 R/C 기록, 다중ZIP·복원률, SHA256, 동일 작성자 자기 심사, 행/그림/PR 개수는 품질과 재현성의 지표지만 논문 주장이나 중앙 완료노드가 아니다. PR #184의 R6/C9 distinct-author는 NOT_RUN이고, PR 리뷰 상태/CI와 독립 물리 검증도 구분해야 한다. '34/49'의 분자계수 보조 완료를 '28/88' REI main solver 진전으로 복사하면 거짓 진전이 된다.

*최소 수정:* 동시에 `REI_CENTRAL, REI_WORKING, WU_CANONICAL, CORE_DELTA`를 정확한 authority ref와 함께 표기한다. 백업과 물리 완료는 분리한다. 새로운 행정 approval gate는 만들지 않는다.

### MA-06 (MEDIUM, process starvation): 반문헌 탐색·백업·검토 자체가 목적이 되는 루프
근거 보존과 이중백업은 사용자 요구이고 성공적으로 수행됐다. 그러나 동일한 마이크로 문제의 잦은 successor PR, 자기 검토 재귀, '새 마지막 blocker' 회전은 실제 source/consumer coupling보다 운영비를 키운다. 이미 풀린 원전 복구·보존법칙을 동일 입력으로 재실행하는 것은 과학적 진전이 아니다.

*최소 수정:* 하나의 bounded 물리 의무당 한 차례 구현·한 차례 필요한 검증 및 체크포인트. 두 연속 비진전 메타/부속 루프 후에는 자동 신규 가지 대신 기존 CORE_NOW 중 가장 짧은 실행 가능한 단계로 복귀. 사용자가 명시적으로 새 탐색을 선택하면 제한하지 않는다. 이것은 합의 서류를 추가하는 gate가 아니다.

### MA-07 (HIGH, integration scientific hazards): 미시물리 port의 계량·대칭성 오류
`n_s/n_ref`에서 (n_ref\propto a^{-3}) 고정 comoving bookkeeping과 evolving physical species reference는 다르다. `dot(n)+3Hn=S`와 `dot(x)=S/n_ref`는 고정 comoving 기준에만 해당하고, 실시간 reference injection이면 `-x S_ref/n_ref`가 생긴다. normal-tetrad mean-z는 시선 방향 관측 z와 다르다. H I homogeneous opacity와 group-effective opacity를 중복 감쇠시키지 말아야 하며, ionization/heat/secondary/photon energy는 unique owner가 필요하다. Tensor source는 full signed sum 뒤 동일 frobenius 기준으로 평가한다.

*최소 수정:* source 소비자 계약에 표기와 conserved ledger를 함께 박고, 없는 term을 0으로 대체하지 않는다. **예상 falsifier**는 same-source matched FLRW/Bianchi one-interval residual과 observer tau/visibility, not coefficient atlas.

### MA-08 (CRITICAL, discovered during fresh hostile review): 관측 보정 구간을 EoR로 오인하는 시간축 드리프트
최초 개정안은 Becker–Bolton Lyα forest 관측 (2.4≤z≤4.75)을 '첫 EoR interval'의 주 구간으로 제시했다. 그러나 이것은 **재이온화 이후의 IGM**이고, REI의 최초 재이온화 물리 이력을 직접 대체하지 못한다. 이 혼동을 그대로 두면 미시물리 → 관측 보정이라는 또 다른 측면 경로로 central science target이 바뀐다.

*구성적 수정:* 재이온화 시대 우선 구간(예시로 6≤z≤10, 단 원전·기하·clock 지원이 확인되기 전까지 미승인)과 2.4≤z≤4.75의 후기 Lyα 검증·보정을 **두 별개 모델/자료 도메인**으로 명시했다. Puchwein 표의 범위가 넓다는 것만으로 고적색편이 실제 물리/관측 source가 확보된 것은 아니다. WU/REI/BASS 등 소유자끼리 범위를 먼저 맞추고 동일 조건의 paired history를 생성해야 한다. 새 과학 DAG node나 행정 승인 gate를 추가하지 않는다.

## 정제된 우선순위: 이 문서의 산출물이지 새 중앙 DAG의 승인 아님

1. **CORE** REI-EXP-SCENARIO + RUX-P0: 첫 재이온화 시대 물리 입력을 별도로 선택한다. 6≤z≤10은 **탐색 후보**일 뿐 원전이 확정된 계산 구간이 아니며, UVB source/escape, IC, H/He photon/thermal state, n_e/T, proper clock/frame, 실제 BASS geometry의 정의역이 공통으로 일치해야 한다. Becker–Bolton 및 Puchwein이 겹치는 **2.4≤z≤4.75는 재이온화 이후 Lyα 보정·대조 구간**으로 따로 둔다. Low-z 보정의 성공은 고적색편이 EoR 결과를 증명하지 않는다.
2. **CORE** REI-L0/L1, RUX05: 하나의 physical source-qualified H/He thermal+photon FLRW interval, 한 번의 보존/검산. 해당 데이터가 없으면 source-matched interval의 구체 missing field만 보고하고 다른 ready science와 병행.
3. **CORE** RUX06–11, REI-L4와 observable: 동일 IC/source에서 Bianchi–FLRW 차이, angular photon transport, optical depth/visibility.
4. **CONDITIONAL** WU/HD·REC/CR/He precision은 source/consumer overlap과 observable 물질성 materiality가 확인되거나 사용자가 명시적으로 요청하면 재개. 과거 미시물리 신뢰성은 유지한다.
5. **LEGACY** 원자 및 수리물리 탐색은 명시적으로 callable. 무조건적 금지/퍼센트 작업 배분/강제 merge나 IVP는 하지 않는다.

## 왜 이 감사가 또 하나의 드리프트가 아니어야 하는가

이번 범위는 **WU의 49 scientific node object 전부 변경 없이**, 88 central status도 변경 없이, 오직 실행 routing/개발 지침에 한 번 가해지는 수정이다. Review의 review를 만들지 않는다. '감사완료'는 완료 과학노드 증가가 아니므로 `WU 34/49, REI 28/88`을 보존한다. 다음 PR은 meta-refinement가 아닌 **REI 실물 소비자 한 개를 도달 가능하게 만드는 물리/코딩 작업**이어야 한다.

### 보류·구분
- 외부 독립 R6/C9, full production, 새 user-owned physics authorization, REI authority merge: NOT_RUN.
- 현재 주어진 같은 저장소 정보에서 WU R18 source DAG의 49개 node object와 중심 repo 문서의 원본/commit을 읽었다. 다른 모든 대화·삭제된 브랜치·비공개 Git 과거 blobs 전수검사 주장하지 않는다.
- 물리 proof/교체 계산 없음: 연구 운영의 메타 감사다. 기존 R45 과학결과의 유효범위를 변경하지 않는다.

**판정:** 운영/우선순위 수준에는 실질적인 drift가 있으며, 물리 산출물은 source-qualified enabling evidence로 유지하되, 다음 default를 named EoR consumer와 paired Bianchi observables로 전환한다.
