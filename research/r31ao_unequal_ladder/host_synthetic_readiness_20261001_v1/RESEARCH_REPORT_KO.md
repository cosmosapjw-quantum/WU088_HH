# WU088 HH 호스트 합성 실행 준비 및 ABI 증거 수집

시작 HEAD `7e9a2ac73f694450d4dd1e95b201d50bace8f25f`, tree
`f2d3886be1cdcb8dc1777c5a1ebf0b8b2ac2d0d8`와 PR #33 open/draft/unmerged를
확인하고 이전 handoff의 다음 노드를 진행했다. 이번 결과는 실행 가능한
호스트 도구와 그 합성 검증이다. 실제 backend/native build와 실제 HH 인증은
수행하지 않았다. B01–B05의 과학적 closure를 새로 주장하지 않는다.

## 구현과 확인 범위

| 산출물 | 실제 확인 | 남은 경계 |
|---|---|---|
| `backend_runner.py` | 오프라인 고정 소스 intake, 실행 순서, create-only, 자원 제한, 합성 marker, 기본 plan-only | 실제 로컬 library compile 및 native runtime 미실행 |
| `provenance_gate.py` | 소스/컴파일러/단계 receipt/실제 로그/라이브러리 SHA 및 runtime linkage 검사 | 완전한 위조 기록의 독립 실행 입증 기능은 없음 |
| `abi_witness.py` | 현재 NumPy 환경에서 정확 dyadic 및 signed-zero/복소/C·F sentinel 8개 | 과거 producer 연결과 실제 HH payload admission 아님 |
| 역사적 텍스트 3개 | R31AL 환경·pre-output lock·runtime inventory의 Git blob/SHA 고정 | 당시 NumPy extension/config와 serializer→B192 연결 미확보 |

세 소스 archive는 GMP 6.3.0, MPFR 4.2.2, FLINT 3.4.0으로 유지했다. 실제
archive의 안전 추출도 수행했으며 GMP 2,343개, MPFR 591개, FLINT 10,193개
member가 검사됐다. archive 내부 link는 없었다. configure/bootstrap 옵션은
해당 archive의 원문에서 확인했다. FLINT는 Git archive여서 `autoreconf`를
포함한 bootstrap 단계가 필요하다. 이 환경에는 pkg-config, autoreconf,
autoconf, automake, libtoolize, m4가 없으며 plan이 이를 명시적으로 반환했다.
사용자의 master prompt §8에 따라 실제 library build는 로컬 실행에 남겼다.

## 실제 결함과 수정

이전 verifier는 build-log SHA 문자열의 존재를 검사했으나 실제 로그 bytes는
확인하지 않았다. 새 verifier는 필수 stage receipt와 stdout/stderr를 모두
읽고 SHA를 대조한다. 독립 검토에서 새 코드의 `sha256=null`이 hash-only 경로로
들어가 비교를 생략하는 문제를 재현했고, 필수 SHA 형식 검사를 추가했다.
수정 후 네 원 재현은 모두 거절됐다. Stage receipt 자체가 일치해도 참조한
stdout을 변조하면 거절하는 별도 RED→GREEN도 남겼다.

Petras fixture는 diagnostic 두 줄 뒤에 JSON marker를 쓰므로 stdout 전체를
JSON으로 읽으면 정상 결과도 실패한다. 원 fixture는 유지하고 실행기의 마지막
marker 해석을 수정했다. ABI collector는 NumPy의 public module alias 대신
실제 serializer 함수의 `co_filename`을 통해 구현 source를 추가로 해시하도록
수정했다. 최초 실패·수정 전 기록·현재 결과를 분리해 보존했다.

## 검증 결과

| fresh 통합 suite | tests | skip | exit |
|---|---:|---:|---:|
| 출처/로그/링크 gate | 12 | 0 | 0 |
| 오프라인 backend 실행기 | 12 | 0 | 0 |
| NumPy ABI witness | 14 | 0 | 0 |

정확한 command/cwd/exit/로그/source SHA는
`evidence/integration/VERIFICATION.json`에 있다. 기존 구현 56개의 lock도 모두
일치했다. 이 테스트 수를 기존 science suite 수에 더하지 않는다.

현재 probe에서 Python/NumPy/serializer/extension/header 등 16개 파일의
42,433,492 bytes를 해시했고, NumPy 2.3.5의 little-endian binary64 및
x87 16-byte-component 후보를 합성 bytes에서 확인했다. 별도 reviewer가
8 sentinel의 96개 실수 성분을 G2 decoder 호출 없이 정수 비트 해석해
exact dyadic·signed zero·C/F index·복소 성분을 검산했다. 이 결과는 현재
호스트에 한정된다. NumPy serializer source가 확보한 C04 pin과 같아도
과거 wheel/extension binary와 같은 실행이었다는 증거는 아니다.

Native runner는 프로세스별 address-space/CPU/file cap과 process-group wall
종료를 사용한다. 전체 tree RSS는 제한하지 않으며 workspace/log cap은
주기적 검사다. 실행기의 실제 library/native route는 아직 **implemented,
runtime-unverified**다. Python 합성 tests와 source extraction을 native PASS로
표기하지 않는다. Artifact review는 project-level scientific admission과 다르다.

## 다음 최소 실행

`LOCAL_CODEX_HANDOFF_KO.md`의 새 sidecar 실행이 다음 노드다. ZIP에 이전
잠긴 구현과 세 원 archive를 함께 넣어 다운로드 없이 실행하도록 했다.
필수 도구가 갖춰진 Linux host에서 명시적 `--execute-host-synthetic` 호출로
실제 backend provenance와 두 fixture 결과를 얻어야 한다. 동시에 원래 보존된
Python/NumPy 환경 및 contemporaneous linkage를 확보한다.

실제 HH 배열/endpoint/integral/gap/certificate는 이번 실행기 범위에 없다.
과거 ABI와 native 증거가 확보되면 기존 `NUMERICAL_EXECUTION_SCOPE.json`의
binary identity와 실행 준비 상태를 갱신한 뒤 actual HH 범위를 별도로 승인받는다.
ε/η=null, rigorous=false와 기존 PRIMARY/SECONDARY finite-order verdict는 유지했다.

게시·이중 백업의 실제 commit/tree와 provider ID는 detached
`DELIVERY_RETURN.json` 및 `DELIVERY_RECEIPT.json`을 따른다. 공개 Git에는
text code/report/evidence만 넣고, 세 제3자 archive는 비공개 전달 ZIP에만 포함한다.
ACK·metadata size 확인과 원격 복원은 구별하며 `RESTORE_VERIFIED=false`다.
