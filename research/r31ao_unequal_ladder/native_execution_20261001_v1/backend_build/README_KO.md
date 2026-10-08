# 격리된 pinned 수치 backend 빌드

`build_backend.py`는 저장소의 원래 GMP 6.3.0, MPFR 4.2.2, FLINT 3.4.0 archive를 SHA256·크기로 확인하고 별도 prefix에 빌드한다. 시스템 라이브러리와 이전 연구 runtime은 교체하지 않는다. 실제 완료 상태는 동반 결과 JSON과 stage receipt를 따른다.

```bash
python build_backend.py gmp --work-root /absolute/new-build-root
python build_backend.py mpfr --work-root /absolute/new-build-root
python build_backend.py flint --work-root /absolute/new-build-root
```

기본 source archive 위치는 이 저장소의 `backend_sources/`다. FLINT Git archive는 `configure`를 포함하지 않으므로 실제 Autotools, GNU m4와 pkg-config가 필요하다. 별도 추출한 도구를 쓰는 경우 `--tools-prefix /absolute/tool-root`로 `bin/`과 `ENVIRONMENT.json`을 지정한다. 이번 실행의 도구 package 획득·해시와 경로 재배치는 별도 tool acquisition 증거에 기록한다. 임의로 만든 configure 또는 수치 header를 사용하지 않는다.

GMP는 `--disable-assembly`로 generic C 경로를 선택한다. MPFR는 release에 포함된 build system을 사용하도록 지원 옵션 `--disable-maintainer-mode`를 지정한다. 두 라이브러리의 생성된 Makefile에서 선택적인 `doc` 디렉터리만 제외하고 변경 전후 SHA를 기록한다. 수치 source와 생성된 수치 header는 이 목적으로 수정하지 않는다. 이 빌드는 NCP 64-core 최적 성능을 입증하는 빌드가 아니다.

동시 make 작업은 2개, 각 process 주소 공간은 1GiB, 각 stage에는 wall/log 크기 제한을 둔다. 목표 메모리 예산은 약 3GiB지만 process tree 전체 RSS의 hard limit은 주장하지 않는다. `RUSAGE_CHILDREN.ru_maxrss`는 자식 중 최대 사용량이며 aggregate나 차분값이 아니다. 초기 `/proc` 기반 관측은 PID namespace가 맞지 않아 사용할 수 없다고 별도 기록한다.

실패한 시도와 readback 불일치 기록은 보존한다. 완료 provenance에는 최종 성공 stage만 선택하며, 이전 실패·대체된 성공 기록을 별도로 연결한다. 이전 로그와 해시가 맞지 않으면 재사용하지 않는다. 원인이 밝혀지지 않은 로그 불일치는 해결된 것으로 표시하지 않는다.

GMP 정수 덧셈·곱셈·나눗셈 3개, MPFR 덧셈·곱셈·지수·제곱근·π 5개 테스트를 실행한다. FLINT 설치 직후 기존 native driver의 provenance gate에 맞는 `BACKEND_BUILD_PROVENANCE.json`과 검증 결과를 먼저 생성한다. 이후 `arb`, `acb`, `acb_hypgeom`, `acb_calc` module 검사는 별도 stage receipt를 가진다. 라이브러리 빌드나 upstream 테스트는 실제 HH 적분·historical ABI·독립 과학 심사·production admission을 자동 승인하지 않는다.
