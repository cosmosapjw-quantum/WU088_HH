# WU088_HH

Frozen107 두 전자 H-H 연구의 source-bound 계산·성능 진단 저장소. 현재 릴리스는 **R31K-B 연구 결과와 검증된 범위의 최적화 후보**이며 완성된 scattering/production solver가 아니다.

다섯 anchor의 H order-comparison은 통과했다. full49는 새 z의 독립 dotO/ionic 입력이 필요하다. 상세 판정: `docs/research/RESULTS_KO.md`, 유도: `docs/research/MATHEMATICS.md`, 검증: `evidence/FINAL_VERIFICATION.json`.

## 기존 runtime을 유지한다

이 저장소는 현재 설치한 runtime을 삭제·교체하지 않는 overlay다. `native/reference`와 `vendor/orchestration`은 회수한 원본 bytes를 보존한다. 완성된 1,440개 pair는 다시 계산하지 않는다. 저장소의 raw ASSEMBLED 배열과 identity/event 자료로 가벼운 수렴·성능 분석을 재현할 수 있다. 전체 pair ZIP은 원래 Drive/Dropbox 백업에 남아 있다.

Local scientific runtime 기본 위치:

```bash
export WORK=/mnt/sn850x2t/hh_heavy_manual_20260926
export RUNTIME="$WORK/runtime/WU088_HH_LOCAL_RUNTIME_SEED_20260926_v2"
source "$WORK/venv/bin/activate"
```

## R31M topology-aware host autotune

저장소 root에서:

```bash
bash scripts/benchmark_host.sh
```

실제 affinity/core/SMT/L3 topology와 quota/memory를 기록하고, 동일 frozen107의 B32/g80 component에서 physical-core 및 SMT process/thread 조합을 비교한다. 각 worker는 disjoint CPU set에 pin한다. 결과는 `$WORK/wu088_hh_bench_<UTC>_<pid>/`에 쓰며 `HOST_TUNING_PROFILE.json`까지 생성한다. 기존 pair를 덮어쓰거나 candidate `.so`를 runtime에 설치하지 않는다. 상세 계약은 `docs/coding/R31M_HOST_AUTOTUNE.md`를 참조한다.

튜닝 profile 생성 뒤 native candidate의 science-resolution exactness는 별도 `scripts/representative_native_regression.py`로 확인한다. 이 gate도 production provider를 자동 승격하지 않는다.

## 여기서 이미 실행한 가벼운 분석의 재현

```bash
python scripts/analyze_anchors.py --out local_runs/anchor_h.json
python scripts/analyze_costs.py --out local_runs/scheduling.json
python -m pytest -q
```

같은 output 파일은 덮어쓰지 않는다. 재현이 필요한 경우에만 새 경로를 지정한다. 기존 과학 full suite를 반복 실행하는 명령은 아니다.

## 후속 승인된 H wave에 적용할 scheduler

**지금 midpoint/propagation을 시작하라는 명령이 아니다.** 먼저 새 anchor의 독립 입력 및 full49 gate를 닫아야 한다. 허가된 새 wave를 실행할 때의 진입점은 `scripts/wide_hybrid_orchestrator_cost.py`다. 기존 frozen kernel을 쓰며 별도의 new native candidate는 자동 적용하지 않는다.

```bash
export R31K_RUNTIME_ROOT="$RUNTIME"
python scripts/wide_hybrid_orchestrator_cost.py \
  --n 160 --g 80 --z 16 --gamma-scale unit \
  --workers 12 --max-new-pairs 12 --max-wall-seconds 300 \
  --execution-lane local \
  --legacy-runner vendor/orchestration/r31k_generic_local_adapter.py
```

위 z16 state가 이미 완료되고 동일 identity라면 `SOURCE_COMPLETE_REUSED_NOT_REASSEMBLED`로 반환한다. 다른 compiler/native identity가 발견되면 섞어서 재개하지 않고 중단한다. pending delta가 있으면 return code74로 먼저 백업을 요구한다. 실제 시간 제한은 in-flight wave의 안전 경계에서 작동하며 300초 hard kill이 아니다.

Pending delta helper:

```bash
python scripts/backup_pending.py \
  --folder "$RUNTIME/completion/mixed_h/wide_hybrid12/B160_g80_sunit_z4030000000000000" \
  --drive gdrv: --dropbox dbx: \
  --receipts "$WORK/wu088_hh_backup_receipts"
```

여기서 drive/dropbox 이름은 사용자가 이미 구성한 raw rclone remote다. 두 provider를 병렬 전송하되 모두 raw SHA/size readback을 통과해야 원래 ACK contract를 호출한다. 새 계산과 백업을 겹치지 않는다. 이 예시는 z16의 정확한 binary64 경로이며 임의 z에 문자열을 복사해 쓰지 않는다.

## 실행환경

Linux, GCC C++17/OpenMP, NumPy2.3.5. 기존 runtime grid에는 SciPy1.17.0이 필요하다. 테스트에는 pytest, 선택적인 Boys audit에는 mpmath1.3.0이 필요하다. 이번 실제 검증 환경은 Python3.13.5/GCC14.2.0이며 사용자 Ubuntu/Python3.12/GCC13 조합은 host benchmark 결과로 따로 기록해야 한다. `sudo`는 사용하지 않는다.

## Git 작업 흐름

정본 원격은 `cosmosapjw-quantum/WU088_HH`다. 기능 변경은 별도 branch/PR로 진행하고 `main`에 force push하지 않는다. 로컬에서는 `git pull --ff-only` 후 위 benchmark를 실행한다. 기존 runtime 삭제, 완료된 anchor 재계산, 자동 candidate 설치는 하지 않는다.
