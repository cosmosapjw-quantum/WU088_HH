# Codex / NCP handoff: PHYS77의 준비된 세 prefix만 실행

## 복사할 작업 지시

```text
$physmath-research-loop를 사용해 WU088_HH Draft PR132의 PHYS77을 이어라.
Repository: https://github.com/cosmosapjw-quantum/WU088_HH
Branch: research/hh-phys77-whole-cell-enclosure-20261021
Actual remote parent: PR131 ec28299fe7e81aab184b93aff787cb00a185dd2e
Scientific baseline: PR128 92f5ab9dba531ebe05909dcb77d3740d2c68c580
Unit: research/hh_phys77_whole_cell_20261021

먼저 실제 PR132 HEAD/branch ref와 delivery/의 최신 receipt를 확인하고,
소유하지 않은 worktree를 변경하지 말고 그 HEAD의 별도 worktree를 만들어라.
다른 branch/repo/backup에서 이 세 request가 이미 완료됐는지 exact request,
table, source-lock, runtime identity로 대조하라. 완료된 identity는 반복하지 마라.

이 단위의 유도/코드/42개 distinct controls/46 scalar point comparisons는 완료됐다.
mixed_s+0_m+1의 첫 cell은 실제 PASS이며 그 계산은 반복하지 마라.
추가 의무는 inputs/pending_ncp/의 세 request, 각각 첫 4개 cell뿐이다.
이는 기존 trajectory의 finite real-lift 포함 증명 시도이며 새 ODE가 아니다.
원본 raw history/constructor를 다시 취득하거나 export할 필요가 없다.

최종 RUNNER_SOURCE_LOCK.json SHA256:
8d1bf0ca0ea7467516c9dbd804443b557c67119d73011389a283b11124bd7ebb
Source lock과 external PHYS76 transport/HH74 resources SHA를 그대로 확인하라.
Python/NumPy가 있는 기존 환경을 사용하라. Runtime은 case identity에 기록된다.
NCP 환경 차이 때문에 수정해야 한다면 최소 변경과 새 identity/근거를 보존하라.
성공 receipt를 새 source hash로 소급해서 바꾸지 마라.

아래 preflight 후 finite --run을 실행하라. 전체128GiB 중 최소16GiB를 남기고,
affinity/quota/busy/load와 공통 lease를 읽어 최대64CPU 안에서 배분하라.
이미 돌고 있는 작업 때문에 일괄 중지하지 말고 가능한 slot에만 배분하라.
shared lease path와 PID namespace는 같은 host의 다른 HH/REI launcher와 맞춰라.
다른 process를 kill/signal하지 마라. Nested threads=1을 유지하라.
슬롯0이면 pending checkpoint로 남기고 같은 output을 다음 invocation에서 재개한다.

PASS_REQUESTED_PREFIX만 COMPLETED로 채택한다. NOT_CERTIFIED/FAILED의 최초
result/receipt는 보존하고 자동 재시도하지 마라. 구체적 새 진단 없이 재실행 금지.
완료/실패/보류 개수와 실제 host/resource/site 증거를 분리하여 보고하라.
3×4 cells는 최대 요청 범위이며 성공을 미리 가정하지 않는다.

같은 normal orthonormal frame의 signed matter/radiation tensor를 따로 보존한다.
total tensor를 합한 뒤 norm; Frobenius=sqrt2×half. 같은 trajectory의 memory는
조건부 기여이고 species-off causality가 아니다. Sample quadrature residual을
continuum certificate로 승격하지 마라. Full history/angular/momentum은 OPEN.
HH_R10=OFF, production admission NOT_ISSUED, benchmark0, 새 ODE0.

실행 결과를 실제 remote descendant의 additive draft PR로 게시하고,
유도/코드/검증/실행/게시/Drive+Dropbox backup/DAG 상태를 각각 기록하라.
기존 파일을 덮어쓰지 말고 PHYS77 successor unit에 새 결과와 immutable receipt를 둬라.
```

## NCP에서 repo root 기준 명령

아래 output은 새 repo worktree 바깥의 지속 경로다. 같은 identity를 재개할 때 같은 output을 사용한다. 출력이 이미 있으면 runner가 hash와 seal을 대조한다. `inputs/REQUEST_FIRST_CELL.json`은 완료한 local witness이므로 이 directory에 복사하지 않는다.

```bash
PHYS77_UNIT="research/hh_phys77_whole_cell_20261021"
PHYS77_OUT="$PWD/../PHYS77_NCP_PREFIX_20261021"

python3 "$PHYS77_UNIT/source/run_enclosures.py" --preflight \
  --requests "$PHYS77_UNIT/inputs/pending_ncp" \
  --output "$PHYS77_OUT" \
  --site ncp --workers 64 \
  --memory-reserve-gib 16 --job-memory-gib 1

python3 "$PHYS77_UNIT/source/run_enclosures.py" --run \
  --requests "$PHYS77_UNIT/inputs/pending_ncp" \
  --output "$PHYS77_OUT" \
  --site ncp --workers 64 \
  --memory-reserve-gib 16 --job-memory-gib 1 \
  --max-new-cases 3 --max-dispatch-seconds 300
```

`--max-dispatch-seconds`는 새 worker를 배정하는 시간 창이며 실행 중 worker의 강제 종료 시간이 아니다. Worker당 계산량은 request의 `max_cells=4`, `max_inflations=8`로 유한하다. `--site ncp`는 operator label이며 실제 remote host 증명을 대신하지 않는다.

준비된 3개 독립 작업이므로 동시 worker의 실질 상한은3이다. 64개를 채우기 위해 완료 case를 복제하거나 서로 의존하는 한 history의 cell을 독립 실행하지 않는다. 다음에 새로운 미완료 request가 충분히 준비되면 같은 dispatcher가 남는 자원 내에서 더 많은 case를 배분한다.

## 채택과 중단 기준

| 관측 | 다음 행동 |
|---|---|
| Source/input mismatch | 출처를 대조하고 원인 해결; 고정 hash를 임의로 바꿔 우회하지 않음 |
| 다른 작업이 자원 사용 중 | 남는 slot에만 배분; 외부 process 유지 |
| 가용 slot0 또는 shared liveness 불명 | pending checkpoint 보존; 환경 관측 후 동일 output으로 재개 |
| PASS_REQUESTED_PREFIX | request의 finite prefix에만 완료 부여 |
| NOT_CERTIFIED_REQUESTED_PREFIX | 최초 defect/radii/domain 결과 보존, 해당 실패 원인 연구 |
| 호출 후 input/source 변경 | RESULT_UNVERIFIED와 FAILED 보존, 결과 미채택 |
| 기존 COMPLETED | 모든 seal/hash 검증 후 skip |
| 기존 output 손상 | 보존하고 차이 조사; retry flag로 덮어쓰거나 우회하지 않음 |

이번 local sandbox preflight는 source/input PASS, eligible3, quota8CPU/RAM8GiB, NCP용 reserve16GiB로 slots0이었다. 실제 NCP 실행은0이다. NCP에 Python3/NumPy가 준비돼 있으면 이번 core에 별도 compilation은 필요 없다.
