# PHYS77 공유 자원 enclosure runner

## 범위와 현재 상태

`source/run_enclosures.py`는 self-contained JSON request를 `cell_enclosure.certify_request(request)`에 전달하는 유한 개수의 작업 실행기다. ODE solver, 원래 trajectory 재계산, benchmark 진입점이 없다. 이번 구현 검증은 가짜 JSON worker와 임시 출력만 사용했다. 실제 enclosure campaign, ODE, NCP scientific job은 모두 0회다.

완료 판정은 `PASS_REQUESTED_PREFIX`에 한정한다. 이는 해당 request의 `config.max_cells`만큼 유한 owner의 셀을 봉입했다는 뜻이다. `NOT_CERTIFIED_REQUESTED_PREFIX`는 별도 보존 상태이며 `COMPLETED`를 생성하지 않는다. 물리적 angular/radial truncation, 전체 trajectory, continuum 또는 production admission으로 확장하지 않는다. `HH_R10=OFF`, production admission은 미발급이다.

`prepare_request`의 기본 `max_cells=1`은 predictor에 65개 node가 있어도 1개 셀만 요청한다. 전체 saved prefix를 요청하려면 입력을 작성하는 단계에서 정확한 요청 셀 수를 명시하고 검토해야 한다. 실행기는 이 설정을 수정하지 않는다.

## Source와 input identity

Source lock 파일은 `run_enclosures.py`, `cell_enclosure.py`, `owner_interval.py`, `export_owner.py`의 실제 최종 SHA256을 포함해야 한다. 외부 PHYS76 interval arithmetic 구현은 아래 해시로 별도 고정한다.

```json
{
  "schema": "PHYS77_ENCLOSURE_RUNNER_SOURCE_LOCK_V1",
  "entry_file": "cell_enclosure.py",
  "entry_function": "certify_request",
  "files": {
    "run_enclosures.py": "REPLACE_WITH_REVIEWED_SHA256",
    "cell_enclosure.py": "REPLACE_WITH_REVIEWED_SHA256",
    "owner_interval.py": "REPLACE_WITH_REVIEWED_SHA256",
    "export_owner.py": "REPLACE_WITH_REVIEWED_SHA256"
  },
  "external_files": {
    "interval_transport.py": {
      "path": "../../hh_phys76_time_transport_20261021/source/interval_transport.py",
      "sha256": "c8b21a2dfdb7ec5810710d2fda6d98922656ecf6d6ae86c82632caab3e227ce6"
    }
  }
}
```

이 예시는 형식 설명이며 실행 가능한 source lock이 아니다. Placeholder를 가진 lock은 거부된다. Lock은 엔진 source와 같은 디렉터리에 위치한다. Python과 설치된 NumPy/SciPy/mpmath/python-flint의 version을 case identity에 기록한다. Optional `expected_runtime`은 exact runtime 불일치를 preflight에서 차단한다. 실제 엔진의 local Python import도 source manifest에 포함돼야 한다.

HH74 `resources.py`는 수정하지 않고 SHA256 `7e2902c015aaae0d7ebd496b2f3dc9c5476bb48aff7b5f6d57ad6652313da8a3`로 재사용한다. Wrapper는 원본 `acquire`가 `cap` 대신 `capacity`를 사용하는 차이를 보정하여 공유 CPU admission 상한을 64로 제한한다.

각 case identity는 nested `table.provenance.case_identity.case_id`, 정확한 request file bytes SHA256, exporter와 동일한 canonical JSON SHA256, 요청 셀 수, source lock과 모든 source SHA256, runtime을 포함한다. Engine 반환의 `case_id`, `request_sha256`, requested/enclosed cell 수를 다시 대조한다. Source와 input은 호출 전후에 확인한다.

## 생성, 재개, 실패 보존

출력 경로는 `cases/<case_id>/<identity_sha256>/attempt-<UTC>-<UUID>/`다. 같은 identity의 case lock은 nonblocking exclusive `flock`으로 보호한다. 모든 science artifact는 create-only로 기록한다. 기존 attempt 파일은 덮어쓰지 않는다.

Engine이 JSON을 반환하면 먼저 `RESULT_UNVERIFIED.json`으로 원본 결과를 보존한다. 그 뒤 status, identity, source, input을 검증한다. 검증에 실패하면 계산 결과와 `FAILED.json`이 남으며 결과를 채택하지 않는다. 검증을 통과한 결과는 `result.json`으로도 저장하고 다음과 같이 구분한다.

| Engine 결과 | 보존 receipt | 기본 재개 동작 |
|---|---|---|
| `PASS_REQUESTED_PREFIX` | `COMPLETED.json` 및 SHA256 seal | 입력·identity·원본 결과·결과 파일·receipt를 hash 검증한 뒤 skip |
| `NOT_CERTIFIED_REQUESTED_PREFIX` | `NOT_CERTIFIED.json` 및 SHA256 seal | 보존하고 자동 재시도하지 않음 |
| Exception, 반환 identity 오류, 호출 후 source/input 변경 | `FAILED.json`, 가능한 원본 반환 결과 | 보존하고 자동 재시도하지 않음 |
| 시작됐지만 terminal receipt 없음 | 기존 attempt 유지 | 자동 재시도하지 않음 |
| 완료/비봉입 receipt 또는 artifact 손상 | 기존 bytes 유지 | `--retry-failed`를 줘도 차단 |
| 다른 process가 case lock 소유 | attempt 생성 없음 | `PENDING_CASE_LOCK` |

`--retry-failed`만 실패·중단·비봉입 request에 별도의 새 attempt를 허용한다. 성공한 완료는 이 flag로도 재실행하지 않는다. Source, request 또는 runtime이 달라지면 다른 identity의 연구 작업이다. 이를 기존 결과와 같은 계산으로 합산하면 안 된다.

## 공유 자원 admission

기본 shared lease 경로는 `/tmp/rei-bianchi-cooperative-leases`다. 같은 host와 PID namespace를 사용하는 HH74/PHYS76 launcher의 lease 형식을 재사용한다. CPU affinity, cgroup v2 quota와 memory limit, sampled busy CPU, global load의 allocation 비례 추정, MemAvailable, 기존 cooperative CPU/RAM lease를 모두 고려한다. 요청한 worker 수의 상한은 64, admission RAM ceiling은 128 GiB다. NCP는 최소 16 GiB를 남긴다. 기본 job memory estimate는 1 GiB다.

Resource slot을 확보한 뒤에만 worker를 만든다. 대기열의 request 전체를 ProcessPool에 미리 넣지 않는다. 작업 시작 전 lease의 liveness를 실제 child PID/start tick에 연결한 뒤 gate를 열어 엔진 진입을 허용한다. Gate 객체는 child 종료까지 유지한다. Parent가 사라져도 살아 있는 child의 lease를 parent 사망만으로 회수하는 문제를 줄인다.

공유 lease lock은 nonblocking이다. 자원이 없거나 lease 상태를 확실히 확인할 수 없으면 해당 invocation을 pending checkpoint로 끝낸다. 이미 실행 중인 own worker는 마무리하며 다른 process에 signal을 보내거나 종료하지 않는다. 다음 invocation에서 pending 작업만 이어갈 수 있다. 같은 invocation은 admission 가능한 작은 묶음만 계속 배분한다.

`--max-new-cases`는 필수 finite launch budget이다. `--max-dispatch-seconds` 기본 300초는 새 작업을 enqueue할 수 있는 기간이며 worker wall-time 상한이 아니다. 이미 시작한 작업을 강제로 중단하지 않는다. 개별 engine의 계산량은 request의 finite cell/inflation 설정으로도 제한한다.

## 한계와 이번에 관측한 환경

- Lease와 sampled availability는 advisory admission이다. Kernel CPU/RSS reservation, peer의 실제 최대 RSS 보장, 여러 container 간 완전한 resource isolation을 제공하지 않는다. Noncooperating process가 이후 시작되는 경쟁 조건도 제거하지 않는다.
- 공유 directory가 서로 다르거나 PID namespace가 다르면 하나의 host 전체 lease pool이라고 주장할 수 없다. 현재 dispatcher의 PID/start tick이 관측되지 않으면 lease directory를 변경하기 전에 실행을 보류한다.
- 이번 local sandbox에서는 `os.getpid()`에 대응하는 `/proc/<pid>/stat`가 없었다. 이 환경에서 실제 cooperative handoff가 성공했다는 주장은 하지 않는다. Fake tests는 synthetic liveness와 실제 `flock`을 사용해 protocol을 확인했다. NCP의 실제 shared namespace는 다음 preflight에서 별도로 관측해야 한다.
- `--site ncp`는 operator가 지정한 기록용 label이며 remote host 접속이나 NCP identity 인증이 아니다. Engine의 `NCP_jobs=0`은 local 함수 자체가 job을 생성하지 않았다는 뜻이다. Runner는 별도로 host/site label과 실제 dispatch 수를 기록한다.
- Execution wall/CPU 값은 비용 기록이다. 속도 향상 배수나 benchmark 결과로 사용하지 않는다.

## 다음 NCP invocation 형식

다음은 검토된 request 디렉터리, 최종 source lock, 새 출력 디렉터리가 준비됐을 때의 형식이다. 이번에 실행하지 않았다.

```bash
python source/run_enclosures.py --preflight \
  --requests REQUEST_DIRECTORY --output OUTPUT_DIRECTORY \
  --site ncp --workers 64 --memory-reserve-gib 16 --job-memory-gib 1
```

```bash
python source/run_enclosures.py --run \
  --requests REQUEST_DIRECTORY --output OUTPUT_DIRECTORY \
  --site ncp --workers 64 --memory-reserve-gib 16 --job-memory-gib 1 \
  --max-new-cases 4 --max-dispatch-seconds 300
```

위 4개는 예시 finite budget이다. 모든 request에 대한 complete campaign을 뜻하지 않는다. Preflight는 engine을 import하거나 lease를 획득하지 않으며 출력도 생성하지 않는다. 실제 launch 이전에 source lock, requested prefix, 기존 완료 skip 수와 pending 수를 검토한다.

## 검증 기록

`tests/test_run_enclosures.py`는 real `cell_enclosure`를 호출하지 않는다. Source/input guard, exact canonical identity, 성공 재개, 손상 차단, 비봉입과 실패 보존, 호출 중 input 변경, case lock 충돌, CPU/RAM quota와 residual capacity, nonblocking shared lease와 peer bytes 보존, PID 관측 실패, finite bounded fake spawn와 pending-only resume를 확인한다. 결과와 최종 source hash는 `RUNNER_VALIDATION.json`에 기록한다.
