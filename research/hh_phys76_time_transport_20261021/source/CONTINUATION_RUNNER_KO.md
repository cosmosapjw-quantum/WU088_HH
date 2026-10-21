# PHYS76: 저장된 z=4 상태에서 z=2까지의 신규 구간

`continue_saved.py`는 복원한 REI198 long collisionless 1231개 이력의 마지막 8상태를 그대로 받아 **새 z=4→2 구간만** 적분한다. 기존 z=20→4의 65개 표본과 원본 파일을 수정하거나 다시 계산하지 않는다. REI213 warm 729개, HH74 control 63개에는 적용하지 않는다. 분류는 radiation slice 625, matter slice 600, mixed cancellation 6이며, 3차원 parameter grid 또는 species-off 실험이라는 뜻은 아니다.

## 물리 및 identity

원본 `ComponentReduced.rhs`의 8상태 `(tau,b,q,E0,E2,E4,E6,E8)`를 사용한다. `tau=href*elapsed_seconds`, `q=s/href`, `x=ln(a/(1/21))` 및 원본 `a_ref,href`는 유지한다. 원본의 `src.xmax`는 이전 종료점을 나타내며, 새 적분 구간은 명시적으로 `(x_saved, log(7))`를 전달한다. `initial()`과 원본 `solve()`를 호출하지 않는다. 각 case의 `set_amplitude(A_m)` 값은 원본 receipt에서 읽는다. DOP853, `rtol=3e-11`, `atol=3e-13`, 시작점을 포함한 신규 33표본을 사용한다.

OWNER_LOCK 자체, 잠긴 7개 원본 파일, REI198 archive manifest 및 terminal index를 SHA256으로 고정한다. 각 raw NPZ/JSON은 manifest와 index에 모두 대조하고, 끝 상태와 global x를 binary64 바이트로 확인한다. Radiation slice의 component decomposition NPZ는 raw state NPZ와 별개로 identity에 기록한다. Before/after restart 진단은 저장된 진단과 정확한 바이트 일치를 요구한다. Before 진단도 동일한 33열 batch 형상을 쓴다. 한 열 GEMV의 sampled brightness와 여러 열 GEMM 사이 1 ulp 차이가 독립 검토에서 확인되었기 때문이며, 33열은 모두 **동일한 저장 상태/동일한 x**다. 이 검사는 시간 진행이나 ODE 실행이 아니다.

물질과 복사의 응력은 같은 comoving orthonormal normal frame에서 `diag(-p,-p,2p)`로 각각 저장한다. Signed 성분을 더한 total tensor에 norm을 취한다. 기존 `Sigma`, `Pi_*`는 half contraction이며, 명시적 `*_half`, `*_frobenius`도 함께 저장한다. 후자는 전자의 `sqrt(2)`배다. Sampled positivity는 continuum certificate가 아니다. `HH_R10=OFF`, production admission은 `NOT_ISSUED`다.

## 실행과 resume

```bash
python research/hh_phys76_time_transport_20261021/source/continue_saved.py \
  --preflight \
  --owner-root "$PHYS76_OWNER_ROOT" \
  --terminal-index "$PHYS76_TERMINAL_INDEX"

python research/hh_phys76_time_transport_20261021/source/continue_saved.py \
  --run \
  --owner-root "$PHYS76_OWNER_ROOT" \
  --terminal-index "$PHYS76_TERMINAL_INDEX" \
  --output "$PHYS76_TAIL_OUTPUT" \
  --site local --max-workers 2 --max-new-cases 1231
```

독립 검토 이후 실행한다. 출력 root는 원본 owner 밖에 두어야 한다. 필요한 case만 선택할 때 `--case-id`를 반복할 수 있다. `--run`은 명시적인 `--max-new-cases`를 요구한다. 동일 output의 완료 case는 identity와 history SHA256을 확인한 뒤 skip한다. 실패/중단 case의 디렉터리는 보존하고 자동 재시도하지 않는다. 새 attempt를 만들기 위한 우회로 기존 실패를 지우지 않는다.

각 case에는 create-only `STARTED.json`, `history.npz`, `COMPLETED.json` 또는 `FAILED.json`을 쓴다. 각 invocation도 시작/종료 receipt를 append-only로 남긴다. NPZ provenance에는 admission 시점 누적 비용 snapshot을, case/invocation JSON에는 실행 비용을 기록한다. 동시 진행 중인 case가 snapshot에서 빠졌다는 사실을 명시한다. 이것은 실행 회계이며 benchmark 또는 speedup 주장이 아니다. 종료 receipt가 없는 invocation은 예약 예산 전체를 사용한 것으로 보수적으로 처리한다.

## 자원 공유

변경하지 않은 HH74 `resources.LeasePool`을 재사용한다. 공유 경로 기본값은 `/tmp/rei-bianchi-cooperative-leases`다. NCP는 최대 64 workers/128 GiB 안에서 실제 affinity, cgroup, CPU busy 및 가용 메모리를 따른다. NCP 메모리 reserve는 16 GiB, local은 2 GiB이며 case당 예약은 0.25 GiB다. Local worker는 최대 2개다. BLAS/OpenMP thread는 1개다. LeasePool 인스턴스 capacity도 64로 제한하여 더 큰 host에서도 총 allocation ceiling이 늘지 않는다.

새 launch가 불가능하면 pending checkpoint를 남긴다. 이미 실행 중인 다른 작업을 종료하거나 signal하지 않는다. 이 runner의 누적 wall budget은 290초이며 신규 적분 admission/자체 RHS deadline에 5초 cleanup reserve를 적용한다. 완료 case나 원본 계산을 다시 실행하여 측정하지 않는다.

## 후속 조립

정상 완료 시 기존 65표본에 신규 `tail[:,1:]`의 32표본을 붙이면 z=20→2의 **97표본**이다. 시작점 overlap을 두 번 세지 않는다. State뿐 아니라 공통 진단값의 join도 정확한 일치를 확인한다. Radiation component 분석에는 기존 decomposition NPZ의 hash를, trajectory restart에는 기존 raw NPZ의 hash를 각각 보존한다. 새 tail receipt는 기존 1231개의 계산을 대체하는 receipt가 아니다.

10개 focused unittest는 synthetic byte-pinned fixture와 fake solver만 사용한다. Preflight, source 변조, endpoint 변조, before-solver boundary 불일치, returned restart 불일치, completed resume/hash 변조, 자원 부족 pending, 중단 ledger를 검증한다. 실제 적분/benchmark 실행은 이 unit-test 증거와 분리한다.
