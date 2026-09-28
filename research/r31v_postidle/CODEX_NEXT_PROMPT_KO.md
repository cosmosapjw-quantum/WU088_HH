# WU088_HH R31V: 코드 검토 및 bounded M3B 실행 인계

너는 이 단계의 주 개발자가 아니라 제공된 구현의 검토자·최소 수정자·NCP 실행자다. 사용자가 ChatGPT에서 작성한 코드를 먼저 push하고 cloud Codex 예산을 검토/실행에 집중하도록 정했다. 구현을 다시 설계하거나 범용 scheduler를 먼저 만들지 말라.

## 기준 source와 변경 금지 범위

Repo: cosmosapjw-quantum/WU088_HH
Branch: codex/r31v-postidle-controls-20260928
Baseline ancestor: ff3db87dfbadd5f1eed89b413e5b785baf63a429
Baseline tree: 6dbd1fbfa9e0cbfa34f69147178b7954fdafa2b0

현재 remote ref를 읽고 exact commit/tree를 기록하라. 기존 dirty worktree나 실행 evidence를 덮지 말고 새 worktree를 사용한다. main merge, force push, reset --hard, 타 owner PID kill, affinity/cgroup 강제 이동을 하지 않는다. 연구 branch를 base로 한 stacked PR이며 PR12/13 원본은 보존한다.

먼저 research/r31v_postidle/REPORT_KO.md, SOURCE_PINS.json, FILE_MANIFEST.json, controls.py, m3_postidle.py와 tests를 읽는다. FILE_MANIFEST의 파일 SHA/size를 검증하고 기준 ancestor의 도달성을 확인한다. 실제 remote HEAD가 이 안내 후 변경됐다면 변경을 읽어 영향만 확인하며 과거 SHA로 강제 되돌리지 않는다.

## 이미 끝난 것을 다시 실행하지 않는다

- HH의 H0 authority는 이미 반영됐다. B160 M3A, B192 1x1 memory pilot, 6 full-pair equality를 보존한다. 기존 오염 M3B만 새 run identity로 대체 측정한다. 오염 기록을 삭제하지 않는다.
- bass_cr F1-R2는 297/297 F1_ENGINE_ADMISSION_PASS이며 exactly-once 승인 소비 완료다. F0/F1/F1-R2/F2/F3를 이 작업 때문에 재실행하지 않는다.
- BASS_HE resume-004는 runtime closure가 있고 CODE-I02 독립 재검수가 남아 있다. 그 56-action 계산을 이 HH 작업 때문에 재실행하지 않는다.
- 세 세션 idle은 사용자 보고다. 실제 VM의 PID/process-tree/cgroup/affinity/quota/memory를 읽기 전용으로 확인한다. idle 보고를 live census 완료로 바꾸어 기록하지 않는다.

## 1. 집중 코드 검토와 빠른 재검증

```bash
python -m pytest -q research/r31v_postidle/test_controls.py research/r31v_postidle/test_metric_controls.py research/r31v_postidle/test_driver.py
python research/r31v_postidle/m3_postidle.py --phase describe
```

67 local focused tests, 별도 복구 R31U 15 tests는 이전 ChatGPT 환경 증거이며 NCP PASS가 아니다. 이 VM에서 focused tests를 재실행한다. 기존 research/r31s_ncp/tests의 관련 M3 focused tests도 시행한다. scientific native 호출 없는 범위부터 확인한다.

특히 legacy module namespace import와 spawn pickling, 실제 build JSON fields, H0 compiler/cache handshake, longdouble serialization, rounding context, cgroup hierarchy visibility, 원자적 checkpoint 실패를 검토하라. 필수 수정은 여기 제공된 좁은 경계에서 하고 failing test와 수정 근거를 남긴다. helper의 fake-backend test를 실제 native integration 증거로 승격하지 않는다.

전체 suite를 실행하지 못하면 구체적인 누락 범위를 기록하되, 무조건 새로운 full production run으로 확대하지 않는다.

## 2. 동일성 및 read-only host inventory

새 work directory와 run ID를 만든다. 현재 boot ID, 모든 관련 PID/PPID/명령/worker 수, leaf 및 조상 cgroup 경로, cpu.max, effective affinity, memory.current/max, swap 및 다른 두 owner의 실행 상태를 읽고 inventory JSON+SHA를 저장한다. 이미 남은 process/lease가 있으면 자동 지우거나 재시작하지 않는다.

HH 단독 BENCHMARK_EXCLUSIVE 창을 확보한다. 큰 컴파일·압축·백업 업로드·다른 native pool을 측정 중 겹치지 않는다. 다른 Codex 창은 코드/문서 읽기만 가능하다. 실제 독점 조건을 확인할 수 없으면 BLOCKED_HOST_ALLOCATION으로 종료하고 유효하지 않은 ranking을 만들지 않는다.

grant JSON은 schema=WU088_R31V_GRANT_V1, epoch_id, mode=BENCHMARK_EXCLUSIVE, 명시적 cpus 목록, 현재 boot_id, 승인된 종료시각 expires_unix, memory_reserve_bytes, fixed_workload_132_approved=true, idle_census_confirmed=true를 포함해야 한다. 마지막 두 필드는 실제 inventory와 이 인계의 제한된 benchmark amendment 검토가 끝난 뒤에만 기록한다. 형식만 맞춘 grant를 독립적인 승인/독점 증명으로 취급하지 말라. 실제 cgroup namespace가 외부 quota를 숨기지 않는 NCP VM인지 확인한다.

기본 shortlist는 64x1,32x2,30x2,4x16이다. host/grant가 충분하지 않으면 자동 CPU mask 확대나 64 강제를 하지 말고 stop 또는 근거를 갖춘 더 작은 별도 epoch 계획을 반환한다. HH32/HE16/CR12 공유 운영 최적화를 동시에 하지 않는다.

## 3. 기존 native authority 재사용 경계

실제 checkout에서 기존 R31S/R31T build 안내와 evidence/ncp_host/20260928T092409Z_18dd6940/COMMANDS.md를 읽어 정확한 build 경로를 찾는다. 기록의 절대 경로를 현재 머신에 존재한다고 가정하지 않는다.

build JSON, 두 foreign .so 실제 bytes, H0 source/spec/binary, grid seed, NumPy/longdouble ABI가 기존 equality/pilot과 호환되는지 확인한다. source/binary/ABI가 바뀌면 필요한 fresh strict build와 bounded full-pair gate를 먼저 수행하고 그 정확한 report를 사용한다. 동일성이 충분하면 M3A 전체나 새 scientific node를 반복하지 않는다. 새 runner는 exactness status, source/H0 binary/build key/grid 및 6 sample rows를 확인한다. binary/runtime equivalence의 독립 검토를 생략할 권한은 아니다.

B192 pilot의 source-bound receipt를 사용한다. 기존 pilot은 private_worker_bytes=32454656을 기록하지만 이 숫자를 CLI에 무검증으로 hard-code하지 말고 pilot JSON identity와 현 runtime을 확인한다. memory guard는 실측 값에 engineering safety factor를 적용하는 것으로 true peak-memory 정리라고 하지 않는다.

## 4. 새 opt-in runner로 준비와 측정을 분리

다음 변수는 검토한 실제 파일 경로로 설정한다. placeholders를 실행하지 말라. OUT은 아직 존재하지 않는 새 파일이어야 한다. NCP에서 기존 budget/시간 한계를 확인한 뒤 각 command를 전체 process group에 적용되는 외부 timeout으로 감싸고 종료 상태를 기록한다. 무한 재시도나 자동 resume는 금지한다.

```bash
COMMON=(--build "$BUILD_JSON" --h0-cache "$H0_CACHE" --grant "$GRANT_JSON"
        --reference-cache "$REFERENCE_CACHE" --exactness "$EXACTNESS_JSON"
        --pilot "$PILOT_JSON" --configs '64x1,32x2,30x2,4x16')
python research/r31v_postidle/m3_postidle.py --phase prepare "${COMMON[@]}" --out "$RUN/reference_prepare.json"
python research/r31v_postidle/m3_postidle.py --phase benchmark "${COMMON[@]}" --out "$RUN/m3b_132.json"
```

prepare는 12 unique pair의 serial reference만 명시적으로 준비한다. 검증된 같은 numeric context의 기존 entry는 재사용하며 일부 완료 cache는 원자적으로 보존한다. benchmark는 reference cache miss에서 실패하고 즉석 reference precompute를 하지 않는다. 모든 timed configuration에는 같은 순서의 132 tasks, 3 repetitions를 공급한다. timed output을 memoize하지 않는다.

원래 worker arithmetic/reduction/strict flags를 바꾸지 않는다. fixed histogram 비교는 기존 M3A ranking을 소급 취소하지 않으며 새 비교와 구분해 보고한다. checkpoint에 REVIEW_REQUIRED가 있어도 final production admission이 아니다. heavy gate는 여전히 닫혀 있다.

## 5. 결과 반환, 게시, 이중백업

각 sample exactness/observed affinity/team/worker CPU/ancestor CPU/throttling/memory/runtime 조건을 대조한다. 공유 ancestor CPU를 HH 단독 사용량으로 표시하지 않는다. 코어 수나 공유 workload throughput의 단위가 다른 결과를 단순 합산하지 않는다. 오염·interrupt·환경 오류와 실제 수치 불일치를 구별하고 원시 실패를 보존한다.

commit/tree, 파일 해시, 실제 commands/exits, host/grant identity, reference cache hit/miss/준비 비용, 고정 histogram/hash, 각 반복 수치, native call accounting, workload 시간·비용, 미검증 사항을 RETURN.json과 한국어 handoff로 작성한다. 반복 성능 pair와 새 scientific node 수를 분리한다.

변경 및 실행 evidence를 ordinary non-force push한다. 현재 두 프로젝트의 remote가 달라졌으면 이전 스냅샷과 차이를 읽고 필요한 운영 상태만 갱신한다. 타 repo의 science state를 이 HH PR에서 수정하지 않는다.

Google Drive+Dropbox에 create-only checkpoint를 두고 provider ACK/object ID/size/checksum을 기록한다. selective readback 원칙을 따른다. raw 다운로드/identity 검증 없이 RESTORE_VERIFIED라 하지 않는다. 백업/압축은 timed measurement 바깥에서만 한다. 실패가 있으면 전체 성공으로 표현하지 않는다.

## 잠금과 다음 최소 node

z1,z0.5,full144,trajectory,M5,production admission,main merge는 실행하지 않는다. M4 async 완성을 이유로 bounded M3B를 불필요하게 막지 않지만 M4를 승인 완료로 바꾸지도 않는다. 정상 종료 뒤 다음 최소 작업은 결과 독립 검토와 M3B 비교 판정이다. 아직 derivative/remainder enclosure가 없는 phase-separated interpolation이나 H-skip을 자동 승격하지 않는다.
