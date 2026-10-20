# PHYS72 NCP 실행 계약

이론·정확 계산 코드·Fortran 구현은 완성됐다. 기본 Fortran compile/run도
이 회차 환경에서 실제 성공했다. NCP에는 준비된 코드의 선택적 재현만 남긴다.
이 결과를 위해 새 HH 적분 campaign이나 기존 D3/profile 재실행은 필요 없다.

## 시작 조건

실제 저장소의 새 PHYS72 branch를 fetch/clone하고 최종 DELIVERY의 HEAD와
대조한다. 원래 과학 parent는 PR123 HEAD
`7060b2390caa931a74b3a377150731b98c2431a9`다. 기존 checkout에 다른 작업이
있으면 별도 worktree를 사용한다. Capsule은 전체 Git clone이 아니며, 그 안의
`research/hh_phys72_20261020`만으로 아래 exact 계산은 독립 실행 가능하다.

먼저 같은 source/input identity의 완료 결과가 있는지 읽는다. 이미 있는 출력
디렉터리를 지우거나 덮어쓰지 않는다. 새 실행이 필요하면 새 경로를 쓴다.
`HH_R10=OFF`, frozen NPZ와 corrected D3 SHA는 `inputs/IDENTITIES.json`이다.
`eta=Fy`, `xi=Fy-phi`, `eta_C=-10/7` 구분을 유지한다.

## 정확 계산: Python 표준 라이브러리

저장소 또는 capsule 최상위에서 실행한다. `PHYS72_RUN_DIR`는 이번 실행을 위한
새 디렉터리다. 이 계산은 exact scalar arithmetic이며 적분을 호출하지 않는다.

```bash
set -eu
PHYS72_RUN_DIR=runs/phys72_exact_20261020
mkdir -p runs
mkdir "$PHYS72_RUN_DIR"
python3 research/hh_phys72_20261020/implementation/bounds.py \
  --terms 3 --lambda-abs 1 --budget 1e-78 \
  --frozen-npz research/hh_phys72_20261020/inputs/FROZEN_U_SUBSET.npz \
  --d3-certificate research/hh_phys72_20261020/inputs/ALL_ANGULAR_CERTIFICATE.json \
  --output "$PHYS72_RUN_DIR/EXACT_BOUND_CERTIFICATE.json"
python3 research/hh_phys72_20261020/implementation/third_and_higher.py \
  --input-root research/hh_phys72_20261020/inputs \
  --output "$PHYS72_RUN_DIR/THIRD_AND_HIGHER_ENCLOSURE.json"
python3 research/hh_phys72_20261020/implementation/angular_weights.py \
  --output "$PHYS72_RUN_DIR/ANGULAR_WEIGHTED_BOUNDS.json"
```

수용 기준은 exact `q=553311/10^26`, strict `abs(lambda)*q<1`,
`R_ge4<1.50654e-80`, combined radius `<7.271949342749e-79 a0^-1`,
고정 입력 SHA MATCH 및 `HH_R10=OFF`다. JSON의 absolute input path는 실행
위치에 따라 바뀌므로 출력 전체 hash가 이전 호스트와 같다고 요구하지 않는다.
source/input hashes와 정확한 분자·분모, 중심, semantic status를 비교한다.
표시된 충분 반경의 upward decimal로 수렴영역을 넓히지 않는다.

## Fortran compile/run

GNU Fortran 등 `REAL128`을 제공하는 Fortran 2008 컴파일러가 있으면:

```bash
python3 research/hh_phys72_20261020/ncp_delivery/run_native.py \
  --fc gfortran --lambda-abs 1 --terms 3 \
  --out runs/phys72_native_20261020
```

이 wrapper는 version, compile, native run을 각각 기록한다. 정상 설치라면
소스 변경이 필요 없다. 분리 설치한 컴파일러에서는 실제 host의 compiler,
`liblto_plugin.so`, runtime library 경로를 `--fc`와 `--fc-arg`로 지정한다.
이 회차에서 실제 사용한 경로와 최초 실패/수정 기록은
[NATIVE_README.md](NATIVE_README.md)에 있다. Rust 부재 때문에 Fortran을
우선 구현한 결과이며 Rust 설치는 이 실행의 선행 요건이 아니다.

기본 timeout은 명령별 60초, thread 환경은 1이다. 이 작은 스칼라 프로그램에
대형 job, multi-core sweep 또는 새로운 누적 계산 예산을 배정하지 않는다.
native 출력은 `certified:false`인 rounded diagnostic이다. `EXACT_AUTHORITY.json`
이 수렴과 오차 판정을 담당한다. 경계 근처 native 분기가 다르더라도 정확
Fraction 판정을 바꾸지 않는다. 직접 Fortran CLI는 잘못된 입력을 exit code로
거부한다. Wrapper는 실제로 시작한 compile/native/payload 단계의 결과와
실패를 기록한다. 일부 preflight 오류는 receipt 생성 전에 종료될 수 있다.

## 반환 계약

실제로 수행한 경우 source HEAD/tree, Python/Fortran 버전, 실행 argv,
source/input/binary SHA, stdout/stderr, exit code, compile/run wall time,
native JSON과 EXACT_AUTHORITY, 최종 EXECUTION을 함께 반환한다. 실패와
수정된 새 실행은 다른 디렉터리에 보존한다. native 시간은 HH solver 시간이나
수학적 검증 비용으로 바꾸어 보고하지 않는다.

기존 14-test suite, 22-check 독립 audit, manufactured quadrature, Coulomb point
검산은 현재 source identity에 대해 완료된 근거다. 호스트 이식에서 실제
변경이나 실패가 발생한 의존성만 필요한 만큼 검증한다. 기존 76 D3 panel과
152 profile은 이 계약이 실행하지 않는다.

Git 게시·provider 백업은 과학적 판정과 별개다. 결과를 게시할 경우 실제
source의 additive descendant draft PR과 create-only 결과 capsule을 쓰고,
현재 DAG의 completed 상태를 유지한다. `xi`, origin/incoming-adjoint,
`sigma(E)`, `k_HH(T)`는 이 실행 계약 밖의 후속 과학 의무다.
