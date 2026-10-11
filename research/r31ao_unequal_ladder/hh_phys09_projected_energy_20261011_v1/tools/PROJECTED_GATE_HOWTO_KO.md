# PHYS09 저장 Jet 검증기

이 코드는 연구 호스트에서 빌드하거나 실행하지 않았다. `READY_NOT_RUN`이다.
NCP에서 이미 설치된 `rustc`만 사용한다. PHYS08의 별도 대기 작업은 이 wrapper가 호출하지 않는다.

```bash
python3 tools/run_ncp_projected.py --run-dir /absolute/path/outside/frozen/package/phys09_ncp_first
```

실행 폴더는 새 절대 경로여야 하고 동결된 PHYS09 패키지 밖에 둔다. wrapper는 compiler identity 1회,
오프라인 build 1회, 저장 입력 gate 1회, exact oracle consumer 1회만 순서대로 실행한다.
각 단계 첫 실패의 원문 stdout/stderr와 실행 기록을 남기고 재시도하지 않는다. source producer,
Python 연구 진단, root solver, Cargo, 설치, PHYS08 wrapper를 실행하는 경로는 없다.

| 단계 | wall/CPU | 주소 공간 | 파일별 최대 크기 |
|---|---:|---:|---:|
| compiler `-vV` | 10 s | 512 MiB | 16 MiB |
| build | 60 s | 512 MiB | 16 MiB |
| gate | 15 s | 256 MiB | 16 MiB |
| exact consumer | 15 s | 256 MiB | 16 MiB |

입력은 원본으로부터 고정한 `results/projected_first/GATE_INPUTS.tsv`의 12,594행이다.
두 stage마다 108개의 전체 signed Jet와 고정 계수, 반경, 중심, 중심 잔차를 읽는다. 예상 수는
`10 + 16 + 16 + 108 × 57 + 99 = 6297`로 코드가 유도한다. 모든 필수 key를 소모한 뒤 남는 key,
중복, 누락, 잘못된 bit word, 비유한 수, 뒤집힌 구간은 거절한다. HHQ도 모든 성분을 읽고 검증한다.
HH 에너지 상쇄는 동일한 captured threshold를 쓰는 반응 벡터 항등식으로 먼저 적용한다.

Rust의 `gamma` 출력은 `[0, gamma_upper]`이다. 내부에서 넓힌 `abs(K)`의 상계를 exact scalar로
오인하지 않도록 선택한 포함 구간이다. image margin도 beta와 행 합의 안전한 상계를 사용한
포함 구간으로 출력한다. 실제 gate 조건은 `gamma.hi < 1`, 모든 `margin.lo > 0`, 그리고 `det(C)`의
구간이 0을 포함하지 않는 것이다. 4개의 Neumann 항에 반경 가중 나머지 상계를 더한다.
원본의 모든 signed derivative 꼬리와 수치적 lambda 교차 꼬리를 유지한다.

Rust 내장 검사는 7개 의미 그룹이다. 다른 합성 입력에서 손으로 구한 HH 상쇄, 다섯 항의 부호 반전,
0/0 접촉, 두 좌표가 결합한 역행렬과 필수 꼬리, 음의 최소 subnormal과 signed zero, 잘못된 영역과
수축 조건, 입력 및 산술 거절을 확인한다. 이 합성 입력은 실제 두 stage와 별개이며 source 실행의
대체 증거가 아니다. 내장 `evaluate` 호출은 정상 합성 1회와 거절 합성 5회, 실제 저장 stage 2회다.

`diagnostics/check_projected_rust.py`는 입력 TSV의 hash/크기를 oracle과 대조하고, 모든 50개 출력
구간이 exact Fraction oracle의 양 끝을 포함하는지 확인한다. 실제 endpoint에서 부호를 다시 정한다.
부호가 넓어져 0을 포함하면 그 부호 의무는 OPEN으로 기록한다. `PASS_SCOPED_OUTPUT_CONTAINMENT`는
네이티브 root 권한의 승격이 아니다. 제공된 stdout만으로 실행을 입증할 수 없으므로 wrapper가
source/input/compiler/binary의 전후 hash, 실제 명령, exit, elapsed와 Linux `wait4` RSS를 함께 남긴다.

성공 시 `HOST.json`, 네 단계의 `EXECUTION.json`과 원문 logs, `ORACLE_CHECK.json`,
`PROJECTED_ENERGY_SIDECAR.json`, `NCP_RUN.json`을 반환한다. 실제 native root/U/V/W/I는 계속 null이다.
