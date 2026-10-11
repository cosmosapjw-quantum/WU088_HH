# 첨부 없는 PHYS09 NCP 시작 정보

이 파일의 아래 전체 handoff를 실행하라. 사용자가 별도 전달 파일을 첨부할 필요는 없다.

- Repository: `cosmosapjw-quantum/WU088_HH`
- Research branch: `research/hh-phys09-projected-energy-20261011`
- 정확한 science core commit: `3e409503c40a7899033126a458b1cb06b227978a`
- Core subtree: `afdef4725df9fdb084038d291343ac371ef96196`
- Core path: `research/r31ao_unequal_ladder/hh_phys09_projected_energy_20261011_v1`
- PR: https://github.com/cosmosapjw-quantum/WU088_HH/pull/40
- Archive: `WU088_HH_PHYS09_PROJECTED_ENERGY_NCP_HANDOFF_20261011_v1_sha_810192192496.zip`
- Archive bytes: 1718264
- Archive SHA256: `81019219249628c4d04df003ffd008eb48a26655577219bb3670729fd10760bb`
- Core MANIFEST SHA256: `6ca00fc8b46b4e09bdbd101cff89b6cd6a490d40ec4d45620d97391e5c7cfce6`
- Drive archive ID: `1eIkbtentbsc2cZfrX_WnYNvILAFslpVu`
- Drive archive: https://drive.google.com/file/d/1eIkbtentbsc2cZfrX_WnYNvILAFslpVu/view?usp=drivesdk
- Dropbox archive ID: `id:BSpOijBcT10AAAAAAD4Iow`
- Dropbox archive path: `/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/WU088_HH_PHYS09_PROJECTED_ENERGY_NCP_HANDOFF_20261011_v1_sha_810192192496.zip`

위 core commit은 source/결과가 봉인된 commit이다. 같은 branch의 이후 delivery-only commit에서도 core subtree가 동일하면 이 source pin을 유지한다. 아래 과학·실행 계약을 바꾸지 않는다.

---

# WU088_HH PHYS09 — NCP local Codex handoff

## 목적과 바로 이어갈 위치

WU088_HH의 PHYS09 전달물을 복구하고, 저장 자료만 소비하는 NCP gate를 수행하라. 별도 사용자 첨부는 필요 없다. 이 core에는 PHYS09의 모든 source/input/code/oracle 및 PHYS08의 완전한 선행 ZIP이 들어 있다. 완료된 과학 source producer를 다시 호출하지 않는다.

현재 이 파일은 science core의 일부이므로 자기 archive/commit hash를 스스로 담지 않는다. 실제 pin과 원격 object ID는 함께 게시되는 `WU088_HH_PHYS09_START_HERE_20261011_v1.json` 및 `WU088_HH_PHYS09_FINAL_DELIVERY_RECEIPT_20261011_v1.json`을 읽어라. Core MANIFEST/SHA256SUMS, archive SHA256와 고정 Git tree를 대조하라. Receipt 자체의 hash는 detached index/최종 전달 메시지를 따른다.

정본 repo는 `cosmosapjw-quantum/WU088_HH`, 예정 연구 branch는 `research/hh-phys09-projected-energy-20261011`, core path는 `research/r31ao_unequal_ladder/hh_phys09_projected_energy_20261011_v1`다. Branch 이름만 믿지 말고 START에 기록된 정확한 commit과 subtree를 확인하라. 기존 checkout에 미완료 변경이 있으면 보존하고 새 detached worktree 또는 별도 staging에서 수행하라. Default/main merge, force push, runtime 설치·교체를 하지 않는다.

## 복구할 백업 위치

- Google Drive folder: `1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM`.
- Dropbox: `/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928`, namespace `183516487`.
- 새 archive는 `WU088_HH_PHYS09_PROJECTED_ENERGY_NCP_HANDOFF_20261011_v1_sha_*.zip`이며 정확한 파일명·SHA·object ID는 START에 있다.

Git pin과 backup archive 중 가용한 한 경로에서 필요한 bytes를 복구하면 된다. 이미 검증된 로컬 payload가 있으면 그것을 재사용한다. 새로 remote bytes를 다운로드한 경우에만 실제 restore 검증이라고 보고한다. 양쪽 업로드 ACK와 metadata 확인을 다운로드 restore라고 부르지 않는다. 다른 이름의 반환 또는 미게시 local run의 존재 여부는 NCP에서 관측해서 기록하라.

## 먼저 읽을 근거

`README_KO.md`, `SCIENTIFIC_CONTRACT.md`, `RESEARCH_STATE.json`, `REPORT_KO.md`, `review/DECISION.json`, `theory/PROJECTED_ENERGY_THEOREM_KO.md`, `NCP_TASKS.json`, `GATE_INTERFACE.md`, `results/projected_first/GOLDEN_ORACLE.json` 및 원 repo AGENTS의 관련 부분을 읽어라.

모델은 실제 host metadata와 이미 선택된 harness를 정직하게 기록하라. Included Astra v4 패키지는 기존 선택의 연속 자료다. 모델 라벨을 보고 실제 모델 전환을 했다고 주장하지 않는다. WU088_HH에 다른 project의 local-heavy-only 규칙을 자동 확장하지 않는다.

## 상속된 실제 상태

- 최신 source delivery는 NCP07 `4d5c18b8a6d348e2de42b5e12dc0fd4d753add7b`, source core `dfa574ce2c302ff2dce38d0e487903d57f1db977`.
- PHYS08 research delivery는 `3490c77ea548fa810443b06546ba847856a7eaea`다. 2026-10-11 06:30:12 UTC intake에서 예상 NCP08 반환은 미관측이었다. 이 timestamp 뒤의 실제 완료가 있으면 identity를 검사하여 재사용한다.
- PHYS09 exact-rational first run은 PASS, 48 assertions/8 semantic cases, 0.8762889720092062 s, RSS 26,184 KiB, source/input 전후 unchanged, stderr 0이었다. 이 프로그램을 NCP에서 습관적으로 다시 실행하지 않는다.
- `PROJECTED_RESULTS.json` SHA256 `c6329fed8c411e1592bd1a0c63ebd9ca6151e81500ed1f46fb6b40f4b7758444`.
- `GOLDEN_ORACLE.json` SHA256 `df7b7f88b99764c4c54ae2e3ffac79e23e27cd6b01abba040f4a01cb1e406752`.
- `GATE_INPUTS.tsv` SHA256 `a371d7f54ee4eb57bcb5095e928e6d9647e8dc2bcd7a9d3e5f5eca6225ef05da`, 715,374 B, 12,594 rows plus header.

원 source-inclusion과 C² 전제 아래의 mathematical fixed-leaf family에서 full I_e는 [−6.192852956727484e−16,−2.012354998700877e−16] eV/H, first_half I_e는 [−7.75969827499494e−17,−2.5357316013204017e−17] eV/H다. Direct ell[W]의 0-containing interval은 그대로 남아 있다. 이 표를 Rust의 실제 실행 결과로 복사하지 않는다.

## A. PHYS08 pending gate 처리

먼저 NCP local 및 게시된 NCP08 반환에서 PHYS08의 동일 source/input tuple에 결박된 실제 완료를 찾는다. `NCP_RUN.json`, compiler/build/gate/consumer 원 로그와 `ORACLE_CHECK.json`, `WEIGHTED_SOURCE_SIDECAR.json`, source/input/binary hash, 독립 판정이 같은 실행을 가리키는지 확인하라. 동일 성공 evidence가 있으면 **REUSED_EXISTING_COMPLETE**로 기록하고 빌드·gate·소스 계산을 반복하지 않는다.

동일 입력의 최초 실행 evidence가 없으면 포함된 archive를 새 경로에 풀어라.

```bash
python3 tools/prepare_predecessor.py --dest /absolute/create_only_physics_run/phys08_unpack
```

실제 출력이 가리킨 `HH_PHYS08_20261011_v1`에서 선행 contract/review/manifest와 다음 파일을 읽은 뒤 한 번 실행한다.

```bash
python3 tools/run_ncp_weighted.py --run-dir /absolute/create_only_physics_run/ncp08_weighted
```

이 helper는 기존 rustc identity, offline build 하나(60 s,512 MiB), gate 하나(10 s,128 MiB), oracle consumer 하나(10 s,128 MiB)를 수행한다. PHYS08 원 limits와 출력을 그대로 따른다. 과거 PHYS08 Python exact reference 또는 NCP07 PreBE/source를 재실행하지 않는다. 이미 실패 evidence가 있으면 그것을 보존하고 원인을 분류하라. 입력·코드 변화 없는 동일 실패 재시도는 하지 않는다. 구체적인 수정이 필요한 경우 우선 해당 실패를 결과물로 남기고, 원 scope 안에서 정당화한 correction만 별도 revision/run ID로 다룬다.

PHYS08의 native scalar gate 성공은 PHYS09 mathematical theorem의 전제를 대신하지 않는다. 두 작업의 provenance는 분리한다. 선행 gate에 blocker가 있어도 PHYS09 saved-input 작업이 독립적으로 실행 가능하면 그 작업은 계속하고 각각의 성공/실패를 보고하라.

## B. PHYS09 새 projected-energy gate

PHYS09 package root에서 입력/manifest를 확인하고 새 run directory를 지정한다.

```bash
python3 tools/run_ncp_projected.py --run-dir /absolute/create_only_physics_run/ncp09_projected
```

`/absolute/create_only_physics_run`은 실제 host의 가용 scratch/work 경로로 정하고 HOME 같은 시스템 변수를 바꾸지 않는다. 이미 존재하는 run directory를 지우거나 덮어쓰지 않는다.

허용되는 실제 명령은 기존 `rustc -vV` 한 번, dependency-free offline Rust build 한 번(60 s,512 MiB), 새 gate 한 번(15 s,256 MiB), exact-oracle consumer 한 번(15 s,256 MiB)이다. 각 output/log는 최대 16 MiB다. Wrapper는 실제 command, compiler/flags/host, elapsed/RSS/exit, 원 stdout/stderr, source/input/binary 전후 hash를 남긴다. Toolchain을 설치하거나 network dependency를 가져오지 않는다. Compiler 부재나 runtime 실패는 그 사실대로 보존한다.

검사 대상은 모든 33×3 photo rate, nonphoto, 원 G의 full signed 7-slot Jets다. Stage f와 stored fhat, heat+threshold의 정확한 source 의미를 보존한다. 네 Neumann 항과 엄밀한 tail, 원 G_lambdab 및 Hessian, energy scalar 식의 다섯 항을 모두 포함한다. NaN/Inf, zero-touching divisor, 잘못된 layout, 부족/중복/추가 key, contraction 실패 또는 radius domain 문제를 숨기지 않는다.

Rust interval은 exact rational oracle의 구간 전체를 포함해야 한다. 단순 overlap, 숫자 자릿수 비교 또는 expected sign 문자열 복사는 통과가 아니다. 실제 끝점으로 STRICT_NEGATIVE/STRICT_POSITIVE/ZERO_CONTAINING을 정하고, projected energy upper<0인 stage만 strict negative로 기록한다. 원 source/고정 계열과 연결이 없는 generic fixture 결과를 native root certificate로 분류하지 않는다.

## C. 검토·반환·양쪽 백업

실제 비생성 reviewer가 새로운 Rust code/컴파일/실행·consumer 결과와 최초 실패가 있다면 그 실패까지 읽어 최종 scoped decision을 남긴다. Code/test author가 스스로 PROMOTE하지 않는다. 추가 전체 suite나 review의 review를 실행할 필요는 없다.

반환 core에는 다음을 넣어라.

- 실제 input/root/research commit과 tree, package/archive/manifests의 identity.
- PHYS08 reused/completed/blocked 상태와 원 실행 evidence 포인터.
- PHYS09 `HOST.json`, compiler identity/build/gate/consumer 각각의 `EXECUTION.json`, stdout/stderr, binary/source/input hashes.
- `ORACLE_CHECK.json`, `PROJECTED_ENERGY_SIDECAR.json`, `NCP_RUN.json`.
- `NCP_RETURN.json`, `RETURN_KO.md`, `CLAIM_LEDGER.json`, `BLOCKERS.json`, `NEXT_HANDOFF_KO.md`, `review/DECISION.json`.
- 최초 실패와 correction source가 있으면 그대로 포함하고, 로그 없는 PASS로 대체하지 않는다.
- 독립된 Git branch/PR 및 complete archive, START, handoff, receipt/index를 같은 Drive/Dropbox 폴더 양쪽에 게시한다.

제안 NCP branch는 `codex/hh-phys09-ncp-20261011`이다. 이미 있다면 실제 head/worktree 상태를 확인해 미완료 변경을 보존하고, 새 stage 이름 또는 명확한 fast-forward를 사용한다. 서로 다른 source 결과를 한 실행으로 합치지 않는다. 자동 main merge나 runtime provider 교체는 하지 않는다.

## 최종 claim ceiling

Native PreBE/residual/FT03/HH/provider, nonlinear endpoint/root, IVP, carried step, old suite의 **새 호출 예산은 모두 0**이다. Inherited uninstrumented counters는 null을 유지한다. Actual native root/U/V/W/I는 null이고 native authority는 false다. 이번 Rust consumer가 확인할 것은 saved-source arithmetic의 실행 포함이다.

Carried second_half, full/two-half paired defect, time/continuum remainder, full49와 production은 OPEN이다. 원 PHYS07 reference energy OPEN과 원 NCP07 node32 per-node predicate OPEN을 수정하지 않는다. 새 source-family 에너지 결과와 이전 predicate를 정확히 구분해 반환하라.
