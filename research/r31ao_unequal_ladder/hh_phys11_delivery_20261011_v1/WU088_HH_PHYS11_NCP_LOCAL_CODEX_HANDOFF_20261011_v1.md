# 첨부 없는 PHYS11 NCP 시작 정보

PHYS08/09/10은 `REUSED_EXISTING_COMPLETE`, PHYS11은 `COMPLETE_HERE`다.
현재 `heavy_queue=[]`, `launch=false`다. 아래 파일을 읽고 완료 evidence를 연결한 뒤
`NO_HEAVY_JOB_READY`를 반환하라. 짧은 계산·build·gate·consumer를 다시 실행하지 않는다.
사용자가 별도 전달 파일을 첨부할 필요는 없다.

원 NCP08/09 완료 반환도 archive의 `inputs/prior_returns/`에 함께 보존했다.
`files/ncp08/VALIDATION.json`, `files/ncp09/NCP_RETURN.json` 및 각 execution
기록을 이 디렉터리에서 읽을 수 있다. 현재 PHYS11 작업 계약을 따르고 옛 pending 지시는 재실행하지 않는다.

- Repository: `cosmosapjw-quantum/WU088_HH`
- Research branch: `research/hh-phys11-joint-carry-20261011`
- 정확한 PHYS11 science core commit: `ff43bf4c149437e329715274c96a5597a6862d53`
- Core subtree: `34c49fd710dc89b78e65e021959168139c105fa8`
- Core path: `research/r31ao_unequal_ladder/hh_phys11_joint_carry_20261011_v1`
- 실제 parent PHYS10 commit: `7a5eb687515aa29934de764d04fd7493f289ac24`
- PR: https://github.com/cosmosapjw-quantum/WU088_HH/pull/44
- 실제 독립 과학 판정: `PROMOTE_SCOPED`
- Archive: `WU088_HH_PHYS11_JOINT_CARRY_NCP_HANDOFF_20261011_v1_sha_946a93390a91.zip`
- Archive bytes: 2563320
- Archive SHA256: `946a93390a91c4dcfd5164887121954f77be74a01d8c93576f859f38dcaab90b`
- Core MANIFEST SHA256: `09be062fa7a1bc64b9de8483480d88c2980a5f719874c21c4e2e119b494f9108`
- Drive archive ID: `1ZaycDIwCHO125rbcAWa_qctaVAmy_V3F`
- Drive archive: https://drive.google.com/file/d/1ZaycDIwCHO125rbcAWa_qctaVAmy_V3F/view?usp=drivesdk
- Dropbox archive ID: `id:BSpOijBcT10AAAAAAD4NIA`
- Dropbox archive path: `/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/WU088_HH_PHYS11_JOINT_CARRY_NCP_HANDOFF_20261011_v1_sha_946a93390a91.zip`

위 science core commit과 subtree는 실제 게시된 고정 source/결과 identity다.
이후 delivery-only commit에서도 동일 core subtree를 확인하면 이 pin을 유지한다.
양쪽 업로드 완료와 metadata를 기록했으며 새 전달물의 원격 재다운로드 복원을 주장하지 않는다.
아래 과학·실행 계약과 현재 빈 NCP queue를 유지한다.

---

# WU088_HH PHYS11 — NCP local Codex 전달

게시 시점의 실제 Git commit/tree, archive bytes/SHA256, Drive·Dropbox object ID를 담은 detached header가 이 문서 앞에 붙는다. PHYS11 자체의 identity는 그 header를 사용한다. 아래 과거 pin으로 대체하거나 임의 hash를 만들지 않는다. Git 또는 기존 백업에서 전체 패키지를 확보할 수 있으므로 추가 첨부를 요청하지 않는다.

## 이번 작업

PHYS11의 완료된 경량 물리 결과를 기존 WU088_HH 연구 상태에 연결하라. 사용자는 경량 실행을 ChatGPT 측에서 완료하고 실제로 길고 무거우며 병렬계산으로 이익을 얻는 부분만 64코어·128 GiB NCP에 넘기도록 지시했다.

현재 `NCP_TASKS.json`의 `heavy_queue=[]`, `launch=false`다. 이번에는 새 과학 계산·compiler/build/gate/consumer·source/provider/root/inverse/history를 실행하지 않는다. 기존 완료 증거와 PHYS11 actual summary/execution 및 최종 독립 decision을 읽어 연결한 뒤 `NO_HEAVY_JOB_READY`를 반환하라.

PHYS08와 PHYS09의 옛 pending 실행 지시는 실제 완료 반환으로 해소됐다. PHYS10의 `ledger_first` 역시 완료한 경량 연구 결과이므로 재사용한다. 원 문서·최초 실패·미해결 항목은 provenance로 남긴다.

PHYS11 `carry_v2`는 여기서 **4.029582589995698 s**, 최대 RSS **29900 KiB**, exit 0으로 완료했다. **168 assertions / 8 semantic cases**, 단계별 33 groups와 165 carry intersections, 19개 binding 전후 동일을 기록했다. `NCP_TASKS.json`과 `review/DECISION.json`을 읽고 실제 채택 범위를 따른다. 완료 프로그램을 재실행하지 않는다.

최초 `carry_first`는 0.1667173830064712 s, RSS 19728 KiB, exit 1이었다. Full Jet인 `COMMON_INPUT_SCOPE.old_gas`를 bare interval로 읽은 `KeyError: lo_bits`였고, 첫 물리 stage가 끝나기 전의 입력 schema 처리 오류다. 실제 full Jet를 읽고 값과 0인 미래 partial을 확인하는 부분만 수정했다. 입력·tolerance·precision은 유지했다. 첫 snapshot/log와 `evidence/FIRST_FAILURE_AND_CORRECTION.json`을 그대로 보존한다. 이 최초 실패를 NCP에서 다시 재현할 의무는 없다.

## 확보와 읽기

이미 동일 identity의 core가 있으면 재사용한다. 새 archive를 다운로드했다면 실제 bytes·SHA256와 내부 MANIFEST/SHA256SUMS를 확인한다. 기존 작업 디렉터리·완료 checkpoint·최초 실패를 덮어쓰지 않는다. 업로드 ACK·metadata 일치를 실제 downloaded-byte restore 검증이라고 부르지 않는다.

읽을 순서는 다음과 같다.

1. `SCIENTIFIC_CONTRACT.md`, `REPORT_KO.md`, `review/DECISION.json`.
2. `results/carry_v2/SUMMARY.json`, `evidence/carry_v2/EXECUTION.json`; 특정 결과 항목이 필요할 때 `results/carry_v2/CARRY_RESULTS.json`.
3. 패키지에 보존된 현재 PHYS11 source intake 및 원 PHYS08/09/10 완료 evidence.
4. `EXECUTION_ROUTING_KO.md`, `NCP_TASKS.json`, `NEXT_DAG.json`.
5. Source-to-carry map 및 joint composition 유도에서 actual state와 conditional source-family 구분.

이전 결과의 고정 pin은 다음과 같다.

- PHYS10 전달 commit: `7a5eb687515aa29934de764d04fd7493f289ac24`.
- PHYS10 core commit: `c9fc72d92dc008f1be20a1e00839a422d0ce29ce`.
- PHYS10 core subtree: `b7592637e565666ad92047b7ea25067a4d6bd34b`.
- PHYS10 PR: `https://github.com/cosmosapjw-quantum/WU088_HH/pull/43`.
- NCP08 완료 head: `5288fd50148755f5ed37391e3dcb612d8d51f130`.
- NCP09 완료 head: `e6a72c3df5803b5b23f9a38918dad6a1eba7e1f7`.

PHYS10 원 실행은 0.7208253940043505 s, RSS 23924 KiB, exit 0, 35 assertions / 7 semantic cases다. `inputs/phys10/SUMMARY.json`, `inputs/phys10/EXECUTION.json`, `inputs/phys10/DECISION.json`에서 재사용한다. NCP08 gate는 0.004196964 s, NCP09 gate는 0.06280682899523526 s였다. 이 완료 실행을 NCP 작업으로 다시 만들지 않는다.

## PHYS11 결과의 의미

PHYS11은 저장된 33개 incoming group complete Jets와 99개 rate Jets, 기체 U/V/W를 결합한다. Source-aligned group 값·U/V/W, quotient 포함과의 교집합, absorbed/source/HH/thermal 및 source-derived escape \(\Gamma_*\) ledger carry와 joint composition의 정의·유도·구현 상태를 확인한다.

Full과 first_half 모두 node 24의 photon mixed carry는 양수, node 16–23의 8개는 음수, 나머지 24개는 0 포함이다. Source-derived escape와 thermal work를 포함한 증대 mixed ledger는 Full `[-5.788230243389953e-40, 6.862357933552255e-39]`, first_half `[-6.9733119029796365e-40, 8.2693439649913e-39]` eV/H다. 이 작은 구간은 새 bookkeeping 항을 추가한 source identity의 잔여이며 PHYS10과 다른 관측량이다. 수치 정확도가 수십 자릿수 개선됐다거나 전역 보존이 증명됐다고 해석하지 않는다. 두 구간은 0을 포함한다.

Geometry·clock·고정 coefficient tuple과 per-H 정규화를 보존한다. Value의 physical cone과 signed tangent/Hessian을 구분한다. Historical HH ON·기존 ledger·primal compensation을 보존하며 미래 실수-family derivatives로 덮어쓰지 않는다.

Full과 first_half는 같은 COMMON에서 별도로 시작한다. Group carry는 실제 4,224개 ray·node와 128개 guard 전체 상태를 대신하지 않는다. Same-node denominator가 ray에 공통이라는 algebraic lift와 실제 native distribution graph의 identity는 별개다. `phys04_distribute_after_be`의 scalar coefficient capture 순서가 residual과 다르며, 33×3 계수 확인이 필요하더라도 경량 작업이다.

\(\Gamma_*\)는 source-derived radiative observable이다. 실제 native escape-rate Jet나 실제 escape 상태를 생성했다고 선언하지 않는다. Actual native root/U/V/W/I는 null, native_authority=false를 유지한다. Actual carried second_half, full/two-half paired defect, time/continuum remainder, 전역 transport/guard/escape/redshift 에너지 수지, full49/production 및 기존 OPEN을 보존한다.

## 다음 물리 의무와 NCP 사용 조건

`NEXT_DAG.json`은 필요한 actual ray/guard 자료, source/native product graph 및 escape 연결, complete joint state, 다음 단계 source coverage와 실제 history를 구분한다. 이론·작은 구현·경량 검증은 여기서 계속하도록 기록한다. 원 PREBE binary 4.1 MB의 가용성·download·decode를 heavy 계산으로 배정하지 않는다. 합성 입력으로 actual history의 빈칸을 채우지 않는다.

미래에 새로운 NCP campaign을 만들려면 실제 미완료 task manifest, 입력·source·parameter·closure·clock identity, 대표 실제 task의 wall/CPU time·peak RSS·출력 bytes가 필요하다. 완료 pilot을 재사용하고, 작업 수를 늘려 코어를 채우지 않는다. 현재 조건을 충족한 heavy task 집합은 없다.

병렬 단위는 독립 physical family의 전체 history다. 각 family의 gas/photon/guard/ledger 시간 carry는 순차이며 같은 gas를 공유하는 energy groups는 독립 gas solve가 아니다. Canonical reduction과 source trace 의미를 보존한다. Frozen107 atomic pair/OpenMP 및 완료1440 pair를 HH task로 재활용하지 않는다.

64코어·128 GiB는 사용자 target ceiling이며 관측된 호스트나 측정된 speedup이 아니다. 미래 정책 상한은 56 single-thread workers와 112 GiB, reserve는 8 CPU 상당과 16 GiB다. Actual cpuset/quota/physical core·SMT/NUMA/cgroup/가용 RAM/경쟁 작업을 먼저 읽어 실제 낮은 한도를 적용한다. Worker memory governor와 immutable task/checkpoint identity를 고정하기 전에는 dispatch하지 않는다. Nested BLAS/OpenMP threads는 별도 계약이 없으면 1이다.

기존 planning heuristic의 미완료 직렬 work 600 s 및 독립 family 8개는 예시 문턱이며 물리적 필요조건·자동 실행 규칙·속도 보장이 아니다. 독립 작업 2개가 각각 충분히 큰 경우도 새 구체적 비용 계약으로 판단할 수 있다. Recovery/I/O까지 포함해 실제 유리해야 한다. 예시 문턱에 맞추려고 scan을 늘리지 않는다. 별도의 물리적으로 정당한 heavy 계약은 새 구체적 evidence가 생길 때 작성한다.

## 반환과 종료

이번 반환은 다음 정보를 포함한다.

```text
status: NO_HEAVY_JOB_READY
PHYS08: REUSED_EXISTING_COMPLETE
PHYS09: REUSED_EXISTING_COMPLETE
PHYS10: REUSED_EXISTING_COMPLETE
PHYS11: COMPLETE_HERE
heavy_queue: []
launch: false
new_scientific_runtime_calls: 0
```

실제로 읽은 PHYS11 commit/tree 또는 archive identity, final decision, summary/execution 경로를 적는다. 다음 입력·연결 의무는 기록하되 이번 intake에서 새 프로그램을 만들거나 실행하지 않는다. Empty queue를 확인하면 이 bounded intake를 종료한다. 같은 readiness를 주기적으로 polling하지 않는다.

사용자는 이 연구의 additive Git branch/PR 및 기존 Drive·Dropbox 백업을 이미 승인했다. 이를 이유로 재승인을 요구하지 않는다. Main merge·force push·runtime 설치/교체는 이 전달의 범위에 포함되지 않는다.
