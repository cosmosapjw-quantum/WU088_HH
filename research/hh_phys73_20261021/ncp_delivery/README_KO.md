# NCP: 구현 완료된 PHYS73 통합 batch 실행

## 입력과 compiler

실제 full Git checkout에서 실행한다. recovery ZIP를 Git clone으로 취급하지 않는다.
branch는 `research/hh-phys73-green-batch-20261021`이고 실제 source commit과
metadata HEAD는 `../publication/REMOTE_PUBLICATION.json` 및 외부 DELIVERY에서 확인한다.
실행 전에 같은 request에 대한 새 host return/이미 돌아가는 작업이 있는지 대조한다.
이 세션은 live NCP host에 접근하지 못했으며 제출 횟수는 0이다.

Python3.12.14, NumPy2.3.5, SciPy1.17.0, mpmath1.3.0, python-flint0.8.0을
실제로 검산했다. Python >=3.11의 실제 interpreter 또는 venv에 requirements를
설치한다. 외부 PYTHONPATH에만 mpmath를 두면 PHYS66 worker가 찾지 못할 수 있다.
Rust1.94.1과 GNU Fortran13.3.0이 sandbox에서 확인됐다. NCP에서는 host compiler로
빌드한다. Rust는 외부 crate가 없으며 Cargo network download가 필요 없다.
fast-math를 사용하지 않는다. 커널의 source SHA와 실제 binary SHA를 별도로 남긴다.

```bash
git clone --single-branch --branch research/hh-phys73-green-batch-20261021 https://github.com/cosmosapjw-quantum/WU088_HH.git WU088_HH_PHYS73
cd WU088_HH_PHYS73
git rev-parse HEAD
python3 -m venv ../wu088-phys73-venv
../wu088-phys73-venv/bin/python -m pip install -r research/hh_phys73_20261021/ncp_delivery/requirements-tested.txt
command -v rustc
command -v gfortran
```

이미 full clone이 있으면 기존 작업을 덮어쓰지 말고 별도 worktree/checkout을 쓴다.
branch가 이후 전진했다면 DELIVERY에 기록된 실행 source commit에서 체크아웃하거나,
실제 추가 변경을 읽고 새로운 source binding으로 실행한다.

## Plan과 전체 실행

repo root에서 아래 plan은 scientific child를 만들지 않고 실제 host 자원을 출력한다.
requested64/128과 실제 affinity/cgroup 제한을 혼동하지 않는다.

```bash
HH_R10=OFF ../wu088-phys73-venv/bin/python research/hh_phys73_20261021/implementation/ncp_batch.py --out /mnt/data/WU088_HH_PHYS73_BATCH --cpus 64 --memory-gib 128
```

새 실제 실행:

```bash
HH_R10=OFF ../wu088-phys73-venv/bin/python -u research/hh_phys73_20261021/implementation/ncp_batch.py --out /mnt/data/WU088_HH_PHYS73_BATCH --cpus 64 --memory-gib 128 --wall-seconds 86400 --run
```

`/mnt/data`가 없는 host에서는 충분한 저장공간의 새 절대 경로로 바꾸면 된다.
compiler가 PATH 밖이면 `--rustc /absolute/path/rustc --fc /absolute/path/gfortran`을 준다.
동일한 완료 출력에 같은 명령을 반복하면 성공 job은 hash 검증 후 child 0회로 재사용한다.
일치하지 않는 source/runtime/command나 변조된 성공 output은 자동 덮어쓰기하지 않는다.
runner의 `--wall-seconds`는 job별 한도이며 PHYS66의 내부 per-case 한도는 900초다.
오류가 난 attempt를 보존하고 환경만 고친 후 동일 binding의 미완료 작업을 재개한다.
source/runtime 자체를 바꾸면 새 출력 root를 사용하고 변경 이유를 기록한다.

## 실제 수행되는 작업

1. PHYS72 exact scalar3개와 Fortran compile/run, PHYS73 exact source budget, Rust build.
2. analytic positive Yukawa source로 L64/T44/N257와 N513/dps60 Coulomb packet 생성.
   최대64 independent process와 1 GiB/process 상한을 쓴다. 중첩 노드는 shared cache에서 재사용한다.
3. 최대64 worker Green sweep, radial refinement 비교, 같은 packet의 dense/sweep paired benchmark.
4. PHYS66 longtail6(6×4 GiB)과 validated L64의 j37..64(28×2 GiB)를 동시에 수행한다.
   j0..36은 저장된 enclosure를 재사용하며 원래 precision/오차 목표를 유지한다.
5. 결과와 소스·로그·SHA256 manifest를 묶고 ZIP를 전체 readback한다.

64/128 예산은 source 단계64 GiB, historical 동시 단계80 GiB이며 headroom16 GiB다.
실제 자원이 작으면 자동으로 workers가 줄어든다. 각 serial chain의 panel은 순서대로 진행한다.
완료된 PHYS70 native L64, PHYS71 D3 76 panels, inherited152 profiles는 queue에 없다.

## 판정과 반환

job 성공, full-L64 enclosure, finite-grid diagnostic, physical matched solution은 다른 상태다.
finite-grid source 결과는 `certified:false`; nested-grid 차이도 rigorous error가 아니다.
analytic error component4.918263356868373e-53은 exact continuum action에 관한 별도 상한이다.
validated L64의 실제 D1/D2 목표 미달은 실패 상태로 남고, 완료 PHYS69 all-angular D2를 취소하지 않는다.

최종 stdout의 `backup.archive`와 같은 prefix의 `_ACK.json`을 함께 반환한다.

```text
/mnt/data/WU088_HH_PHYS73_BATCH/archives/PHYS73_NCP_RETURN_<invocation>.zip
/mnt/data/WU088_HH_PHYS73_BATCH/archives/PHYS73_NCP_RETURN_<invocation>_ACK.json
```

ZIP는 실패·부분 진행도 보존하며 complete 여부는 내부 각 RESULT/EXECUTION을 읽어야 한다.
runner는 외부 upload, Git push/PR, remote host 제출을 수행하지 않는다.
실제 host 결과를 채택할 때 compiler·하드웨어·source SHA·동일 request·실제 output hash를 먼저 대조한다.

## 원래 과학적 제약

B27, k7/10, E49/200, eta_C=-10/7, eta=Fy, xi=Fy−phi를 유지한다.
frozen NPZ SHA `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`와
PHYS71 corrected D3 SHA `f75d082e1966dd61a326c37b6ff14e8f330e010341a59a88eb4ca8d4734e6173`
를 보존한다. 원래 matched boundary trace를 frozen interior NPZ에서 추정해 채우지 않는다.
VigilODE reflecting-grid boundary를 HH outgoing boundary로 사용하지 않는다. HH_R10=OFF.
