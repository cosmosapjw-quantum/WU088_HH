# PHYS71 NCP 전달: 완료 결과 검증과 준비된 후속 실행

PHYS71 D3의 76개 수치 패널은 이 세션에서 완료됐다. 같은 요청을 새로
적분하지 않는다. 별도의 analytic correction을 포함한 최종 결과는
`d3/run_l36_t65_stable_errors/ALL_ANGULAR_CERTIFICATE.json`이며,
독립 읽기 검증과 표시 중심을 포함한 절대 오차 `7.121295358370e-79`가
고정 목표 `1e-78`을 통과했다. HH_R10=OFF다.

## 1. 복원과 무계산 검증

최종 PHYS71_DELIVERY의 SHA256을 대조한 후 capsule을 새 디렉터리에
복원한다. capsule은 필요한 source slice와 입력 archive를 포함한다.
전체 Git clone은 아니다. 원래 두 archive의 canonical 경로는 다음과 같다.

```text
research/hh_phys68_20261019/profiles/PROFILE_PANEL_PAYLOADS_20261019.zip
archives/PHYS69_BAND_PAYLOADS_20261019.zip
```

capsule 또는 해당 입력을 갖춘 저장소 루트에서 다음을 실행한다.

```bash
python3 -S -B research/hh_phys71_20261020/verification/verify_saved_d3.py \
  --root . \
  --campaign research/hh_phys71_20261020/d3/run_l36_t65_stable_errors \
  --display research/hh_phys71_20261020/DISPLAY_RESULT.json
```

이 verifier는 표준 Python과 정확한 Fraction 산술만 사용한다.
Flint import, Coulomb evaluation, 새·과거 물리 적분, 결과 파일 쓰기는0이다.
원래 producer와 현재 reader runtime을 구분하므로 producer Python
patch version이 달라도 이 검증은 가능하다.

원래 raw CERTIFICATE.json의 짧은 radial 소수는 inward rounding으로
거부됐다. 그 파일을 삭제하거나 수정하지 않는다. 정확한 numerical
evidence로 재사용하고, 위쪽 endpoint `1.48432231489e-79`를 사용한
별도 ALL_ANGULAR_CERTIFICATE.json을 최종 analytic 인증서로 읽는다.
원래 producer campaign 소스는 `verification/phys71_campaign.py.ORIGINAL_PRODUCER.txt`다.
현재 campaign은 올바른 상수로 수정되어 원래 fingerprint와 다르다.
동일하다고 가장하거나 guard를 해제해 원래 수치 CLI를 강제 재개하지 않는다.

완료된 corrected certificate의 재사용 경로는 다음이다.

```bash
python3 -S -B scripts/phys71_finalize.py
```

이미 파일이 있으면 독립 감사를 통과한 뒤 읽기 전용으로 반환한다.
적분은 호출하지 않는다. 이 명령을 앞의 검증에 덧붙여 반복할 필요는 없다.
교정 인증서가 누락되었지만 원래 76개 패널과 입력이 모두 검증되는 복원본에만
같은 명령으로 create-only analytic certificate를 만든다. 원래 수치 결과는 불변이다.

## 2. 계산 의존성과 실행기

완성된 수치 실행기는 `scripts/phys71_ncp.py`이며, 고정 L36/T65/N80/384bit
요청과 bounded POSIX child, 재개, hash/범위 검사, immutable payload,
timeout process-group cleanup이 구현되어 있다. 이번 완료본을 다시
계산할 명령은 인계하지 않는다.

producer runtime은 정확히 Python3.12.14 / python-flint0.8.0 / FLINT3.3.1이다.
일반 Python3.12라는 이유만으로 같은 engine fingerprint라고 주장하지 않는다.
capsule에는 CPython3.12 Linux x86_64 manylinux2014 wheel이 포함된다.
향후 별도 승인된 수치 요청에서 해당 ABI를 사용할 경우:

```bash
python3 -m pip install --no-index --no-deps --find-links wheels \
  --target runtime/python -r research/hh_phys71_20261020/ncp_delivery/requirements.txt
```

읽기 검증에는 이 설치가 필요 없다. 다른 architecture/ABI이면 맞는
`python-flint==0.8.0` wheel 또는 현지 빌드가 필요하며 기존 wheel을
호환된다고 선언하지 않는다. 모든 solver 설계는 여기서 제공한다.

## 3. 아직 실제 실행이 확인되지 않은 별도 요청

PHYS66 longtail6, PHYS68 validated L64, PHYS69 native L64,
PHYS70 optimized L64의 NCP host 상태는 UNKNOWN이다. 이 세션의
NCP 제출은0이다. 우선 실제 process/job/result와 최신 백업을 확인한다.
이미 완료됐으면 동일 request/source/seed/engine을 검증해 재사용한다.
진행 중이면 관찰하고 새 중복 job을 만들지 않는다.

별도 실행 우선 후보는 이미 구현된 PHYS70 optimized L64다.
전체 Git repo 또는 PHYS70 NCP capsule을 사용한다. PHYS71의 작은
capsule에 PHYS70의 Rust 소스를 중복 포함했다고 가정하지 않는다.

```bash
python3 scripts/phys70_ncp.py \
  --request research/hh_phys70_20261020/ncp_delivery/REQUEST_L64.json \
  --out runs/phys70_l64_preflight --make-seed
```

위 기본 preflight는 seed 생성·compiler·적분을 호출하지 않는다.
완료본과 진행 작업이 없고 실제 NCP 실행을 진행할 때만 다음을 쓴다.

```bash
python3 scripts/phys70_ncp.py \
  --request research/hh_phys70_20261020/ncp_delivery/REQUEST_L64.json \
  --seed /absolute/path/to/L64_SEED_INPUT.txt \
  --out runs/phys70_l64_block_simd \
  --run --timeout 900 --build-timeout 900 --memory-gib 4
```

동일한 L64 seed가 없을 때만 `--seed ...` 대신 `--make-seed`를 사용한다.
Rust1.94.1의 locked source를 현지 빌드한다. 제공된 PHYS70 측정 binary는
GLIBC2.39 요구가 있으므로 구형 host에서는 그대로 실행하지 않고 source를
컴파일한다. `native/phys70_optimized`와 path dependency인
`native/phys69_vigilode`를 함께 유지한다. pinned VigilODE와 Cargo.lock도 유지한다.

native 성공, 저장된 point error, 전체 적분 인증, 성능, 게시·백업·DAG를
분리한다. L28/D3 인증서를 L64나 λ=1 전체 응답의 인증서로 확대하지 않는다.
결과·request·seed·source·실행 receipt·stdout/stderr·compiler/flags/CPU/HEAD/
binary SHA와 checksum을 원문으로 반환한다.
