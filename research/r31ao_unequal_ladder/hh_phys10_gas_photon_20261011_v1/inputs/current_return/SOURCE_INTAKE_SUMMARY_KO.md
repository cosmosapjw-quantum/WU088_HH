# PHYS10: 현재 NCP 반환 intake

2026-10-11 08:37–08:40 UTC의 고정 Git 조회에서 **NCP08과 NCP09 완료 반환을 모두 확인**했다. 이전 PHYS09 연구 시점의 `NCP08 NOT_OBSERVED`는 당시 조회 상태이며 현재 반환 상태를 대체하지 않는다. 이번 intake는 원 기록·hash와 로컬 재사용 입력의 동일성만 확인했으며 compiler, gate, oracle consumer, 과학 계산 및 native 호출을 새로 수행하지 않았다.

## 고정 현재 소스

| 대상 | commit | root tree | 판정 |
|---|---|---|---|
| PHYS09 research, PR40 | `2367504729026abc0d43eaba28703592e885dea4` | `a2338634a0af42b25d85ed9a93d1098930867397` | 이전 연구 그대로 |
| NCP08, PR41 | `5288fd50148755f5ed37391e3dcb612d8d51f130` | `e623ce7410b79741a4b43d1e5f5bb9b8cd07458c` | `PASS_SCOPED_T07` |
| NCP09, PR42 | `e6a72c3df5803b5b23f9a38918dad6a1eba7e1f7` | `6bf0e678f4e98787ffbe6b6f5ef9a3ce2d7abd94` | `REUSED_EXISTING_COMPLETE_SCOPED_REVIEWED` |

NCP09 연구 core는 `3e409503c40a7899033126a458b1cb06b227978a`, subtree `afdef4725df9fdb084038d291343ac371ef96196`로 보존되어 있다. NCP 반환 core commit은 `4b815f00579b9d70f21fa7a30f82f1dd9796741e`, 반환 subtree는 `8848dd72bf8483b65d1e52c5aaca734468445542`다. PR41,42는 open draft이고 PR40은 open non-draft다. 최신 12개 PR 범위와 codex/hh-phys prefix matching refs를 실제로 조회했다.

## 재사용할 실행 근거

NCP09 실제 source/input 13개와 NCP08 10개는 로컬 PHYS09/08의 bytes/SHA256와 전후 일치한다. 필요한 반환 text 35개를 exact Git blob SHA 및 크기에 대조해 모두 일치했다. PHYS09 원 archive와 MANIFEST SHA도 재사용 로컬 bytes에서 일치했다. 전체 원 소스·binary·archive를 다시 내려받지 않았다.

| 원 실행 | PHYS08 elapsed s | PHYS09 elapsed s |
|---|---:|---:|
| compiler identity | 1.030437 | 0.104139 |
| offline build | 1.421573 | 0.766846 |
| gate | 0.004197 | 0.062807 |
| exact consumer | 0.667820 | 0.083373 |

모든 원 process exit는 0이다. PHYS09 build maxRSS는 148,952 KiB, gate는 11,408 KiB, consumer는 20,628 KiB다. PHYS08 RSS의 130,424 KiB는 cumulative child maximum이며 개별 gate 메모리로 해석하지 않는다. 이 수치는 기록된 host에서의 실제 실행 시간이며 NCP 64-core scaling 측정이 아니다.

따라서 **완료된 PHYS08/09 작업을 다음 NCP 큐에 다시 넣지 않는다.** 현재 사용자 지시대로 경량 작업은 여기서 수행하고, NCP에는 실제 계산비·독립 분할 가능성이 확인된 새 heavy node만 넘겨야 한다. 기존 실행을 옮기기 위해 반복할 이유도 없다.

## 채택 범위와 수치

NCP09 비생성자 독립 판정은 `PASS_SCOPED_RECOVERED_PHYS09_SAVED_SOURCE_PROJECTED_INTERVAL_GATE`다. 보존된 Rust 출력의 exact rational oracle 전체 포함은 50/50, 원 입력 TSV endpoint 대응은 12,594개로 확인되어 있다. 이번 intake는 해당 독립 검증을 다시 실행하지 않고 Git-bound evidence로 재사용했다.

| stage | 실제 Rust projected energy, eV/H |
|---|---|
| full | `[-6.192852956727528e-16, -2.012354998700859e-16]` |
| 같은 COMMON의 first_half | `[-7.759698274994996e-17, -2.535731601320379e-17]` |

원 exact oracle endpoint와 실제 Rust outward endpoint를 구별한다. Direct `ell[W]`는 0 포함을 유지한다. Native root/U/V/W/I는 null, authority는 false다. Carried second_half, paired defect, time/continuum remainder, full49/production, PHYS07 reference energy와 NCP07 node32 predicate는 OPEN이다. PHYS08의 minsubnormal_signed는 strict-negative exact oracle이 binary64에서 unresolved로 넓어지는 기존 예외를 보존한다.

## 지침과 한계

현재 NCP09 Git root의 `AGENTS.md`는 frozen native/reference와 vendor source 보존, heavy kernels는 local runtime, bounded algebra/source/implementation checks는 sandbox, dependency 변화 없는 full-suite 재실행 금지를 명시한다. `research/`, `research/r31ao_unequal_ladder/` 및 새 반환 subtree에는 추가 AGENTS가 관측되지 않았다. 현재 사용자 지정의 경량/무거운 실행 분담과 충돌하지 않는다.

Rust 버전은 원 stdout의 1.94.1이고 보존된 compiler hash는 rustup proxy다. 실제 toolchain payload attestation은 아니다. 원 host의 CPU 모델이 기록되지 않아 target CPU 성능이나 64-core speedup을 주장할 수 없다. 이전 reviewer 연결 종료/outer timeout 기록은 과학 process exit0와 분리해 보존한다.

NCP09 delivery START/receipt는 양쪽 provider에서 archive를 다운로드·hash·manifest 검증·추출한 이력을 담는다. 이것은 기존 NCP 반환 receipt의 보고이며 이번 intake에서 새 remote restore를 수행한 것은 아니다. 기존 Git 반환 설명 포장과 복구 archive의 설명문·identity·validation 세 파일은 서로 다를 수 있으므로 전체 포장 byte identity도 주장하지 않는다.

## 근거 파일

- `SOURCE_INTAKE_SUMMARY.json`: 상태·pin·실행 요약과 제한
- `FETCHED_FILE_IDENTITY_MANIFEST.json`: Git-bound 원 text 35개
- `LOCAL_REUSE_MANIFEST.json`: 로컬 source/input 23개 전후 결박
- `files/ncp09/NCP_RETURN.json`, `files/ncp09/NCP_RUN.json`
- `files/ncp09/review/DECISION.json`, `files/ncp09/review/REVIEW_KO.md`
- `files/ncp09/ORACLE_CHECK.json`, `files/ncp09/execution/gate_first/stdout.txt`
- `files/ncp08/HH_PHYS08_ASTRA_ACTUAL_DECISION_20261011.txt`
- `files/delivery09/WU088_HH_PHYS09_NCP_START_20261011_v2.json`
- `observations/`: 실제 connector 응답 content snapshot. API JSON의 최종 줄바꿈은 저장 형식이며 위 scientific text의 Git byte 검증과 구별한다.
