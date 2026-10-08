# 실제 primitive API를 위한 고정 task adapter

이 추가 adapter는 기존 Fortran dispatcher의 `ABS_WORKER --manifest ABS_MANIFEST --task-index ORDINAL` 호출을 새 `native_driver.driver.run_task` API에 연결한다. 기존 MPI/Fortran source와 synthetic executor/launcher는 변경하지 않았다.

`prepare.py`는 사용자 측에서 선택한 입력 NPZ, plan SHA, build manifest SHA, limits와 서로 다른0..2591 primitive index 목록을 받는다. 새 directory에 MANIFEST.json, WORKLIST.txt, bound_worker.py, PREPARATION.json과 빈 results directory를 만든다. ordinal은 선택 목록의0-based 위치이며 native primitive 번호와 혼동하지 않는다. WORKLIST의 deadline은 고정 native wall cap+10초다. 부동소수 cost·reduction은 없다.

생성된 bound_worker에는 manifest의 실제 바이트 SHA와 core worker SHA가 literal로 들어간다. manifest 내부 self-hash만으로 실행을 허용하지 않는다. 후속 launcher는 PREPARATION의 bound_worker/worklist/manifest identity와 실제 파일을 독립적으로 대조해야 한다. base worker.py를 직접 실행하면 거절한다. manifest에 임의 실행 명령이나 driver 경로를 넣을 수 없다. 고정된 인접 native_driver의 검증된 API만 호출한다.

입력·plan·build·limits·binary·backend provenance 파일 identity, 전체 native dependency source, canonical plan과 task mapping, callback build mode를 실행 전후 확인한다. native driver는 자기 claim과 native binary/linked backend 검증 및 memory/wall/output 한도를 계속 적용한다. worker는 durable result를 다시 읽고 exact result schema, 전체 wrapper, task/window/limits/명령, envelope SHA를 검증한 경우에만 성공한다. 기존 output이나 claim은 자동 재사용·삭제·재실행하지 않는다. `validate_envelope`는 기존 성공 결과를 읽기만 하는 별도 검증에 사용할 수 있으며 실행 재사용 허가를 뜻하지 않는다.

## 실행 경계

**이 작업만으로 실제 native MPI host 실행이 지원된 것은 아니다.** 기존 `host_plan/launcher.py`는 SYNTHETIC_ONLY manifest만 허용하며 이 새 manifest를 받지 않는다. 새 worker는 nonroot 실행을 요구하고 root/oversubscription 우회를 제공하지 않는다. 기존 C bridge의 환경 격리 및 close-from 정책은 바꾸지 않았다.

native driver가 backend를 별도 process group으로 띄우므로 native manifest를 검증하는 새 host launcher의 topology/quota/memory admission, rank binding, job deadline, descendant cleanup과 collection이 연결·검증되어야 MPI 실행을 시작할 수 있다. 현재 새 native host guard는 구현하지 않았다. bound_worker를 임의 `mpirun`에 바로 연결하는 명령을 이 문서가 승인하지 않는다. cooperative native deadline이나 MPI bridge timeout만으로 전체 process 수명 containment를 보장하지 않는다.

테스트의 native API 호출은 fixture로 대체했다. 검증 대상은 순차 ordinal mapping, 고정 API 인자, durable output 검증, 입력/source 변경과 기존 결과 및 failure 거절이다. 실제 native/MPI 실행이나64-core 성능·production 결과로 세지 않는다. 부모가 이미 완료한 실제 pilot 결과는 재계산 없이 읽기 검증할 수 있다.

```bash
python -B prepare.py --input-npz ABS_INPUT_NPZ \
  --plan ABS_PLAN --plan-sha256 EXACT_PLAN_SHA \
  --build-directory ABS_BUILD --build-sha256 EXACT_BUILD_MANIFEST_SHA \
  --limits-json ABS_LIMITS --native-indices 0 17 23 \
  --output-directory ABS_NEW_BUNDLE
python -B -m unittest -v test_native_tasks.py
```

준비는 native를 실행하지 않는다. 이 adapter의 성공은 조건부 compact-interior envelope 기록이며 endpoint, normalization, full-domain, independent scientific review, production admission은 계속 별도다.
