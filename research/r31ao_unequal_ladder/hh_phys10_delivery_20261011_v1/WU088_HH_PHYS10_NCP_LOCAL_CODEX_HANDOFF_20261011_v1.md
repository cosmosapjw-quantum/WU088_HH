# 첨부 없는 PHYS10 NCP 시작 정보

PHYS08/09는 `REUSED_EXISTING_COMPLETE`, PHYS10은 `COMPLETE_HERE`다.
현재 `heavy_queue=[]`, `launch=false`다. 아래 파일을 읽고 완료 evidence를 연결한 뒤
`NO_HEAVY_JOB_READY`를 반환하라. 짧은 계산·build·gate·consumer를 다시 실행하지 않는다.
사용자가 별도 전달 파일을 첨부할 필요는 없다.

- Repository: `cosmosapjw-quantum/WU088_HH`
- Research branch: `research/hh-phys10-gas-photon-ledger-20261011`
- 정확한 PHYS10 science core commit: `c9fc72d92dc008f1be20a1e00839a422d0ce29ce`
- Core subtree: `b7592637e565666ad92047b7ea25067a4d6bd34b`
- Core path: `research/r31ao_unequal_ladder/hh_phys10_gas_photon_20261011_v1`
- 실제 parent NCP09 commit: `e6a72c3df5803b5b23f9a38918dad6a1eba7e1f7`
- PR: https://github.com/cosmosapjw-quantum/WU088_HH/pull/43
- 실제 독립 과학 판정: `PROMOTE_SCOPED`
- Archive: `WU088_HH_PHYS10_GAS_PHOTON_NCP_HANDOFF_20261011_v1_sha_55d4422bed00.zip`
- Archive bytes: 1114035
- Archive SHA256: `55d4422bed00ba9b9c9afecd5474dae1e57839d57caa9a783778ca563bbeeb9c`
- Core MANIFEST SHA256: `14635f20b0553871bfdd3ad9a7893bfc526021477dab8bc5bac52891db1134c1`
- Drive archive ID: `1G2KOvjewJ6bZJTc5hiEBbnm4rAaj8QMh`
- Drive archive: https://drive.google.com/file/d/1G2KOvjewJ6bZJTc5hiEBbnm4rAaj8QMh/view?usp=drivesdk
- Dropbox archive ID: `id:BSpOijBcT10AAAAAAD4LAA`
- Dropbox archive path: `/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/WU088_HH_PHYS10_GAS_PHOTON_NCP_HANDOFF_20261011_v1_sha_55d4422bed00.zip`

위 science core commit과 subtree는 실제 게시된 고정 source/결과 identity다.
이후 delivery-only commit에서도 동일 core subtree를 확인하면 이 pin을 유지한다.
양쪽 업로드 완료와 metadata를 기록했으며 새 전달물의 원격 재다운로드 복원을 주장하지 않는다.
아래 과학·실행 계약과 현재 빈 NCP queue를 유지한다.

---

# WU088_HH PHYS10 — NCP local Codex 전달

이 문서 앞에 게시 시점의 실제 Git commit/tree 및 Drive/Dropbox archive identity를 담은 detached 전달 header가 붙는다. Self commit이나 archive 해시를 본문에서 임의로 만들지 않는다. Header에 결박된 Git core 또는 기존 백업으로 아래 패키지를 확보할 수 있으므로 사용자에게 별도 첨부를 요청하지 않는다.

## 목적과 현재 결론

WU088_HH PHYS10 결과를 기존 로컬 연구 상태에 연결하라. 사용자는 짧은 경량 계산을 이 대화 호스트에서 끝내고, 실제 길고 무거우며 독립 병렬 작업으로 이익을 얻는 계산만 64코어·128 GiB NCP에 넘기도록 지시했다.

이번 전달 상태는 다음과 같다.

- PHYS08 Rust scalar gate: `REUSED_EXISTING_COMPLETE`.
- PHYS09 Rust projected-energy gate: `REUSED_EXISTING_COMPLETE`.
- PHYS10 exact-rational 기체–광자 ledger: `COMPLETE_HERE`.
- `NCP_TASKS.json`의 `heavy_queue=[]`, `launch=false`.

**이번에는 과학 계산·compiler/build/gate/consumer를 실행하지 말고, 결과를 읽고 결박한 뒤 `NO_HEAVY_JOB_READY`를 반환하라.** 새 작업을 만들거나 동일 준비 상태를 주기적으로 polling하지 않는다.

실행 위치와 중복 실행에 관해서는 현재 PHYS10 `NCP_TASKS.json`을 따른다. 옛 PHYS08/09 handoff의 pending 실행 지시는 실제 완료 반환과 현재 사용자 지시에 의해 해소됐으며, 원 문서는 provenance로 보존한다.

## 읽을 파일과 identity

정확한 detached header의 commit과 core tree를 우선 확인한다. 이미 동일 identity의 패키지가 있으면 재사용한다. Archive를 새로 내려받았다면 크기·SHA256과 내부 MANIFEST/SHA256SUMS를 확인한다. 기존 작업 디렉터리·실패·완료 checkpoint를 덮어쓰지 않는다.

패키지에서 다음 순서로 읽는다.

1. `SCIENTIFIC_CONTRACT.md`, `REPORT_KO.md`, `review/DECISION.json`.
2. `results/ledger_first/SUMMARY.json`, `evidence/ledger_first/EXECUTION.json`.
3. `inputs/current_return/SOURCE_INTAKE_SUMMARY.json`와 `FETCHED_FILE_IDENTITY_MANIFEST.json`.
4. `inputs/current_return/files/ncp08/VALIDATION.json` 및 `inputs/current_return/files/ncp09/NCP_RETURN.json`.
5. `EXECUTION_ROUTING_KO.md`, `NCP_TASKS.json`, `NEXT_DAG.json`.

완료한 기존 소스의 고정 pin은 다음과 같다.

- PHYS09 research core commit: `3e409503c40a7899033126a458b1cb06b227978a`.
- PHYS09 research delivery: `2367504729026abc0d43eaba28703592e885dea4`.
- PHYS09 core subtree: `afdef4725df9fdb084038d291343ac371ef96196`.
- NCP08 completed head: `5288fd50148755f5ed37391e3dcb612d8d51f130`, PR #41.
- NCP09 completed head: `e6a72c3df5803b5b23f9a38918dad6a1eba7e1f7`, PR #42.
- NCP09 original execution commit: `638af93295c5205c1683c33c9e2b97fe8f3e910d`.

이 pin들은 이전 소스의 실제 identity다. PHYS10 자체의 pin은 detached header를 따르며 위 이전 commit으로 대체하지 않는다.

## 읽어서 재사용할 실제 결과

PHYS08 gate는 0.004196964 s, PHYS09 gate는 0.062806829 s에 완료됐다. 원 compiler/build/consumer와 독립 검토 기록을 보존한다. NCP09에서 검증한 50개 exact-oracle 포함을 다시 검사하는 프로그램을 실행하지 않는다.

새 PHYS10 `ledger_first`는 여기서 0.7208253940043505 s, 최대 RSS 23924 KiB, exit 0, 35 assertions와 7 semantic cases로 완료됐다. Before/after 19개 binding은 동일하다. 같은 COMMON에서 별도로 시작한 Full과 first_half의 유한 photon mixed energy는 각각

- Full: `[2.0147819024003132e-16, 6.190685965150866e-16] eV/H`.
- First_half: `[2.5372573637033666e-17, 7.758341579441771e-17] eV/H`.

기체+광자 ledger의 사전 투영 구간은 각각

- Full: `[-3.1314477547412323e-19, 2.4467453520579934e-19] eV/H`.
- First_half: `[-1.9605021839988345e-20, 1.5319948343632613e-20] eV/H`.

이 결과는 저장 source inclusion과 같은 fixed-coefficient (C^2) family 전제 아래의 유한 사각형 interaction이다. Total 구간은 0을 포함하며 exact zero나 전역 보존을 선언하지 않는다. PHYS09 기체 음의 interaction과 PHYS10 생존 광자의 양의 interaction을 같은 계열에서 결합한 결과다. 실제 native root, 시간 진화 또는 carried second_half 실행을 나타내지 않는다. 정확한 유도·해석·채택 범위는 보고서와 최종 독립 판정을 따른다.

## 미래 heavy 작업의 선행조건

현재 이 절은 실행 명령이 아니다. `NEXT_DAG.json`의 미래 의무를 다음 연구 상태에 보존한다.

첫째, joint gas/photon/guard/ledger 값과 U,V,W carry를 같은 family로 유도·구현해야 한다. 실제 compensation 상태, source/흡수/work/HH ledger와 per-H 정규화, eV/H 단위, stage f와 stored-density ratio를 보존한다. 실제 background/clock·초기조건·photon/source history·closure·고정 계수와 parameter domain이 없으면 합성 입력으로 대신하지 않는다.

둘째, actual first-half 출력에 결박된 다음 단계 source coverage, positive denominator, physical state, hat/guard chart와 (C^2) 조건을 확보한다. 같은 COMMON의 first_half를 carried second_half로 바꾸어 부르지 않는다. Native issuer/root와 수학적 family를 연결해야 하는 의무는 별도로 닫는다. 이 유도와 필요한 작은 검증은 여기서 우선 완결한다.

셋째, 물리적으로 필요한 유한 independent-family task 집합이 생기면 새 대표 task의 실제 wall/CPU, peak RSS, 출력량으로 계산량을 판단한다. 완료 pilot을 다시 실행하지 않는다. 기본 future admission 정책은 미완료 직렬 work 600 s 이상, 독립 family 8개 이상이며 recovery/I/O를 포함해 NCP 이익이 있어야 한다. 이 운영 문턱을 맞추려고 scan을 늘리지 않는다. 현재 이 조건을 충족한 task 목록은 없다.

미래 NCP campaign은 family 전체를 process별로 분리하고 각 family 내부 시간 carry는 순차로 유지한다. Energy group마다 독립 gas solve를 수행하거나 시간 조각을 독립 family처럼 취급하지 않는다. Inner ray 병렬화가 필요하면 원 canonical Jet 합산 순서와 trace 의미를 보존한다.

64코어·128 GiB는 명목 사양이다. 미래 기본 pool 상한은 56개 single-thread worker와 112 GiB이며 8코어·16 GiB를 남기는 정책이다. 실제 cpuset/quota/physical core·SMT/가용 RAM/cgroup/다른 작업을 확인해 더 낮은 한도를 적용한다. Worker 메모리 상한은 새 representative peak RSS의 2배와 명시된 필요량 중 큰 값으로 설정·집행한다. Worker 수는 실제 CPU budget, 미완료 task 수, pool RAM/worker limit의 최솟값을 넘지 않는다. 이 수치들은 선택한 제한이며 측정된 speedup이 아니다.

Task key에는 input/source/coefficient/parameter/grid/closure/binary identity와 parent carry checkpoint를 결박한다. 같은 identity의 완료 결과는 재사용한다. 첫 실패·raw log·출력·실제 resource 기록을 보존하고 새 정보 없이 같은 실패를 다시 실행하지 않는다. 현재 runtime 설치·교체·기존 suite 재실행·source retry는 수행하지 않는다.

## 반환 형식과 중단점

이번 intake의 반환에는 다음을 명시한다.

- `status: NO_HEAVY_JOB_READY`.
- `PHYS08: REUSED_EXISTING_COMPLETE`.
- `PHYS09: REUSED_EXISTING_COMPLETE`.
- `PHYS10: COMPLETE_HERE`.
- `heavy_queue: []`, `launch: false`.
- `new_scientific_runtime_calls: 0`.
- 읽은 PHYS10 실제 commit/tree 또는 archive SHA와 완료 evidence 포인터.
- 다음 선행조건은 joint carry, 실제 normalized history, next-stage coverage/native-family binding, 필요한 task 집합과 측정 비용임을 기록.

Actual native root/U/V/W/I는 null, authority는 false를 유지한다. Carried second_half, paired defect, time/continuum remainder, full49/production, 과거 PHYS07 reference energy 및 node32 per-node predicate는 OPEN이다. 원 실행 host와 이번 intake host, model 요청과 actual attestation을 구별한다. 과거 review transport timeout을 과학 계산 실패로 바꾸지 않는다.

현재 queue가 빈 것을 확인하면 이 bounded intake를 종료한다. 추가 첨부 요청, 경량 프로그램 재실행, 임의 parameter scan, main merge, force push, runtime 설치, 주기적 polling은 이 전달의 작업에 포함되지 않는다.
