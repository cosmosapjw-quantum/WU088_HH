# NCP native 합성 검증 인계

`NEXT_ACTION=NCP_HOST_NATIVE_SYNTHETIC_ACCEPTANCE_AND_RETURN`

이 문서는 `HOST_EXECUTION_CONTRACT.json`의 host implementation 단계를 실행하기 위한 명령 명세다. 실행 전 그 계약을 먼저 읽는다. 과학 소스 기준은 `cosmosapjw-quantum/WU088_HH`, branch `research/r31ao-unequal-order-ladder-20260930`, commit `b66732540d8c428830c957003ea87d705355f49f`, tree `92561187ddbc6f03665253807b235279b052a081`이다. 이후 coordinator 문서만 추가한 successor에서 시작할 수 있으나 아래 사용 소스의 bytes가 기준과 일치해야 한다. 과거 SHA로 reset하거나 기존 runtime을 덮어쓰지 않는다.

범위는 새 sidecar backend build와 합성 native 검증이다. 실제 Frozen107/HH 배열 읽기, actual HH callback/적분, represented-array gap, archived B192 재계산, G7, full-cell, 모델 재학습, production은 포함하지 않는다. 기존 B128/B160 승인은 소진되었고 z=0.75는 holdout이다. `actual_HH_runs=0`, `rigorous=false`, `certified_epsilon=null`, `certified_eta=null`을 유지한다.

아래 heredoc은 기존 Python API를 호출하는 문서 명령이다. 새 실행기 파일을 만들거나 보호 소스를 수정하지 않는다. 실패는 evidence를 보존하고 즉시 중단한다. 같은 command/output directory를 자동 재시도하지 않는다. 한도·정밀도·case·rank 수를 자동 확대하지 않는다.

## 1. 경로와 환경 선택

사용자가 선택한 실제 절대 경로를 환경변수로 제공한다.

- `WU088_PROJECT_ROOT`: ZIP의 `research/`를 포함하는 해제 root 또는 동일 구조의 저장소 root.
- `WU088_SOURCE_DIR`: 고정 C01/C08/C09 archive가 있는 실제 디렉터리. ZIP이면 보통 root의 `backend_sources`.
- `WU088_RUN`: 기존 부모 아래 아직 존재하지 않는 실행 root.
- `WU088_PYTHON`: 선택한 실제 Python 3 executable의 절대 경로. 아래 build shell 내부의 `python3`도 같은 선택을 가리키도록 PATH를 확인한다.
- `WU088_COORDINATOR`: 이 문서와 `HOST_EXECUTION_CONTRACT.json`이 있는 실제 절대 디렉터리. 동봉 runtime ZIP을 별도로 풀었다면 source root와 달라도 된다.

```bash
set -euo pipefail
: "${WU088_PROJECT_ROOT:?실제 절대 source root 필요}"
: "${WU088_SOURCE_DIR:?실제 절대 archive directory 필요}"
: "${WU088_RUN:?아직 존재하지 않는 절대 run root 필요}"
: "${WU088_PYTHON:?선택한 Python3 절대 경로 필요}"
: "${WU088_COORDINATOR:?이 문서와 scope JSON의 절대 디렉터리 필요}"
export WU088_RESEARCH="$WU088_PROJECT_ROOT/research/r31ao_unequal_ladder"
export WU088_OLD="$WU088_RESEARCH/gap_closure_20261001_g0_g6_v1"
export WU088_HS="$WU088_RESEARCH/host_synthetic_readiness_20261001_v1"
export WU088_ACCEL="$WU088_RESEARCH/ncp64_acceleration_20261001_v1"
test ! -e "$WU088_RUN"
mkdir "$WU088_RUN"
"$WU088_PYTHON" -B - <<'PY'
import hashlib,json,os,pathlib
root=pathlib.Path(os.environ['WU088_PROJECT_ROOT'])
co=pathlib.Path(os.environ['WU088_COORDINATOR'])
contract=json.loads((co/'HOST_EXECUTION_CONTRACT.json').read_text())
claimed=contract.pop('SCOPE_HASH')
raw=json.dumps(contract,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
assert hashlib.sha256(raw).hexdigest()==claimed, 'scope hash mismatch'
assert hashlib.sha256((co/contract['COMMANDS']['document']).read_bytes()).hexdigest()==contract['COMMANDS']['sha256']
for row in contract['SOURCE_HASHES']:
    data=(root/row['path']).read_bytes()
    assert len(data)==row['bytes'] and hashlib.sha256(data).hexdigest()==row['sha256'], row['path']
for key,name in [('gmp','C09.tar.xz'),('mpfr','C08.tar.xz'),('flint','C01.tar.gz')]:
    row=contract['INPUT_HASHES']['backend_archives'][key]
    data=(pathlib.Path(os.environ['WU088_SOURCE_DIR'])/name).read_bytes()
    assert len(data)==row['bytes'] and hashlib.sha256(data).hexdigest()==row['sha256'], name
with (pathlib.Path(os.environ['WU088_RUN'])/'SOURCE_SCOPE_CHECK.json').open('x') as f:
    json.dump({'scope_sha256':claimed,'source_files_checked':len(contract['SOURCE_HASHES']),
               'archive_count':3,'status':'MATCH'},f,indent=2)
PY
"$WU088_PYTHON" -B "$WU088_ACCEL/host_plan/planner.py" > "$WU088_RUN/HOST_PLAN_INITIAL.json"
```

Linux/GNU C/C++/Fortran, OpenMPI 4 또는 5, make/autotools/m4/pkg-config 및 glibc 2.34 이상이 필요하다. 자동 설치·sudo·MPI root bypass·oversubscription은 없다. 물리 64코어인지 SMT 포함 64vCPU인지 관측한다. 기본 reserve는 16GiB다. `BLOCKED`이면 실제 사유를 반환한다.

## 2. BUILD scope: backend source → binary

BUILD scope에는 archive/source/compiler/tool identity와 bounded 명령을 결박한다. 아직 만들어지지 않은 backend binary SHA를 예측하거나 null을 승인된 science identity로 사용하지 않는다. build가 성공한 뒤 별도의 native synthetic 실행 scope에 실제 binary/library hashes를 결박한다.

```bash
"$WU088_PYTHON" -B "$WU088_ACCEL/backend_build/build_fast.py" \
  --source-dir "$WU088_SOURCE_DIR" --output "$WU088_RUN/backend" \
  > "$WU088_RUN/BACKEND_PLAN.json"
```

계획이 `PLAN_READY`이고 계약의 source/tool/resource 선택과 맞을 때에만 한 번 실행한다.

첫 build 실행 전에 downstream Codex가 `HOST_BOUND_SCOPE.json`을 create-only로 작성한다. 여기에는 상위 scope SHA256, `SOURCE_SCOPE_CHECK.json`, `BACKEND_PLAN.json`의 SHA256, 실제 START_HEAD/TREE(archive 작업이면 원 commit과 archive hash를 따로 기록), 모든 절대 경로, Python/tool/wrapper identity, 실제 argv와 한도를 넣는다. `BACKEND_PLAN.preflight.tools.python3`의 실제 파일이 선택한 `WU088_PYTHON`과 같은 bytes인지 확인한다. OpenMPI wrapper와 mpirun 선택도 이 시점에 기록한다. source/compiler/tool이 plan 이후 바뀌면 실행하지 않는다.

각 S1–S6 stage 및 각 calibration attempt의 첫 process launch 시 `STAGE_CONSUMPTION.json`에 action, parent scope hash, command argv, 시작 UTC, attempt ID와 `CONSUMED`를 기록한다. 아래 코드 블록은 계산 명령이며 이 coordinator ledger를 대신하지 않는다. downstream Codex가 stage별로 기록·실행·receipt 결박 순서를 지킨다. 중단 뒤 기존 consumed stage를 통째로 재실행하지 않는다. 아직 실행하지 않은 후속 stage만 이전 PASS receipt와 byte identity를 확인한 후 계속할 수 있다. 반복 trial은 사전에 정한 별도 attempt이며 실패 재시도가 아니다.

```bash
"$WU088_PYTHON" -B "$WU088_ACCEL/backend_build/build_fast.py" \
  --source-dir "$WU088_SOURCE_DIR" --output "$WU088_RUN/backend" --execute \
  > "$WU088_RUN/BACKEND_BUILD_STDOUT.json"
export WU088_BACKEND_PREFIX="$WU088_RUN/backend/prefix"
export WU088_BUILD_PROVENANCE="$WU088_RUN/backend/BACKEND_BUILD_PROVENANCE.json"
"$WU088_PYTHON" -B "$WU088_HS/provenance_gate.py" \
  "$WU088_BUILD_PROVENANCE" "$WU088_BACKEND_PREFIX" \
  > "$WU088_RUN/BACKEND_CHAIN_VERIFICATION.json"
```

기본 global build wall은 10,800초다. CPU/메모리 관측에 따라 build concurrency를 정하고 검사 병렬도는 최대 2다. 컴파일러당 AS 2GiB, 전체 RAM은 hard cgroup으로 보장한다고 주장하지 않는다. output의 `PREFLIGHT.json`, `FAST_BUILD_CONFIG.json`, `HOST_RESOURCE_PLAN.json`, `FAST_BUILD_RESULT.json`, provenance 및 stage logs를 보존한다. prefix가 이미 있다면 이 명령을 다시 실행하지 말고 기존 반환 identity와 합치 여부부터 확인한다.

## 3. 기존 callback/assembly 및 Petras acceptance

가속 builder는 library만 빌드한다. cache equality가 assembly나 Petras wrapper를 검증하지 않으므로 이 두 gate를 생략하지 않는다. 아래는 원 `backend_runner.run_stage()`를 재사용한다. build에 8MiB FSIZE의 process guard를 잘못 씌우지 않고 원 stage의 2GiB 파일 cap을 유지한다. 전체 baseline 단계는 900초, 각 compile 180초, 각 합성 run 180초, 프로세스당 AS 4096MiB다. 원 `run_stage`의 workspace/log limit도 유지한다.

```bash
"$WU088_PYTHON" -B - <<'PY'
import json, os, pathlib, sys, time
hs = pathlib.Path(os.environ['WU088_HS'])
old = pathlib.Path(os.environ['WU088_OLD'])
run = pathlib.Path(os.environ['WU088_RUN'])
sys.path.insert(0, str(hs))
import backend_runner as br
from provenance_gate import verify_backend, verify_linkage
pre = json.loads((run/'backend/PREFLIGHT.json').read_text())
tools = pre['tools']
prefix = pathlib.Path(os.environ['WU088_BACKEND_PREFIX'])
record_path = pathlib.Path(os.environ['WU088_BUILD_PROVENANCE'])
root = run/'baseline-native'
root.mkdir(exist_ok=False)
for name in ('logs','home','tmp'):
    (root/name).mkdir()
c = dict(br.CONFIG)
env = br.clean_environment(root, prefix, tools, c)
deadline = time.monotonic()+900
accepted=[]
for label, script, outvar, binary_name in (
    ('callback','validated_callback/build_host.sh','WU088_BUILD_OUT','native_synthetic'),
    ('petras','interior_pilot/build_petras_host.sh','WU088_PETRAS_BUILD_OUT','native_petras_synthetic')):
    lock = br.check_input_lock()
    record = verify_backend(record_path, prefix)
    out = root/('native_'+label)
    stage_env = {**env, 'WU088_BACKEND_PREFIX':str(prefix),
                 'WU088_BUILD_PROVENANCE':str(record_path),outvar:str(out)}
    br.run_stage({'id':label+'-compile','stage':'native-build','cwd':str(root),
        'argv':[tools['bash'],str(old/script)],'wall_seconds':180},
        root, stage_env, c, deadline)
    binary = br.identity(out/binary_name)
    linkage = br.run_stage({'id':label+'-linkage','stage':'linkage','cwd':str(root),
        'argv':[tools['ldd'],binary['path']],'wall_seconds':10},
        root, stage_env, c, deadline)
    linked = verify_linkage(pathlib.Path(linkage['stdout']['path']).read_text(),
        {n:v['binary_path'] for n,v in record['libraries'].items()})
    record = verify_backend(record_path,prefix)
    for n,item in linked['libraries'].items():
        if br.identity(item['path'])['sha256'] != record['libraries'][n]['binary_sha256']:
            raise ValueError('linked-library mismatch: '+n)
    if br.identity(binary['path']) != binary:
        raise ValueError('native binary changed before execution')
    br.write_json(out/'LINKAGE_VERIFIED.json',linked)
    guardout=root/(label+'_guard')
    argv=[tools['python3'],str(old/'host_guard/run_guarded.py'),
          '--wall-seconds','180','--memory-mib','4096',
          '--output-dir',str(guardout),'--',binary['path']]
    scope={'schema':'WU088_HOST_SYNTHETIC_STAGE_BINDING_V1','action':label,
           'scope':'SYNTHETIC_ONLY','input_lock':lock,'binary':binary,
           'backend_record':br.identity(record_path),'linkage':linked,
           'commands':[argv],'one_shot':True,'no_auto_rerun':True,
           'no_scope_expansion':True,'actual_HH_runs':0}
    br.write_json(out/'NATIVE_EXECUTION_BINDING.json',scope)
    br.run_stage({'id':label+'-synthetic','stage':'native-run','cwd':str(root),
        'argv':argv,'wall_seconds':182},root,stage_env,c,deadline)
    receipt=json.loads((guardout/'PROCESS_RECEIPT.json').read_text())
    if receipt['status']!='PROCESS_COMPLETED' or receipt['returncode']!=0 or receipt['stdout_preview_truncated']:
        raise ValueError('incomplete native synthetic: '+label)
    marker=br.parse_native_marker(label,receipt['stdout'])
    accepted.append({'fixture':label,'binary':binary,**marker,
        'execution_binding':br.identity(out/'NATIVE_EXECUTION_BINDING.json'),
        'guard_receipt':br.identity(guardout/'PROCESS_RECEIPT.json')})
br.write_json(root/'BASELINE_NATIVE_RETURN.json',{
    'status':'BASELINE_CALLBACK_ASSEMBLY_AND_PETRAS_SYNTHETIC_ACCEPTED',
    'fixtures':accepted,'actual_HH_runs':0,'scientific_promotion':False})
PY
```

Callback는 callback.cpp + assembly.cpp + native_synthetic.cpp를 빌드한다. 원 flag는 `-O2 -fno-fast-math`이며 script 자체에 `-ffp-contract=off`는 없다. 이를 cache의 다른 flag와 동일했다고 기록하지 않는다. Petras는 `-O2 -fno-fast-math -ffp-contract=off`다. 두 script 모두 build만 하며 fixture 실행은 위 별도 stage가 담당한다.

원 marker parser의 승인 조건은 다음이다.

- Callback: stdout JSON 한 줄, 정확한 key/type/value `{"scope":"SYNTHETIC_ONLY","native_synthetic_passed":true}`.
- Petras: 앞의 두 줄이 각각 `one_dimensional_polynomial=`, `nested_polynomial=`로 시작하고 마지막 JSON이 `{"synthetic_only":true,"native_fixture_checks":10,"actual_HH_evaluations":0}`.
- Guard: `PROCESS_COMPLETED`, returncode 0, stdout preview 비절단. exit 0만으로 native acceptance라 하지 않는다.

## 4. Cached callback build와 정확도 matrix

cache build에도 위 기존 `run_stage`를 적용한다. source lock, backend provenance, compiler, linked-library bytes를 검증한 `BUILD_READY.json`을 native task manifest의 입력으로 묶는다. build receipt는 build-only 기록 그대로 보존하며 이후 검증 성공에 맞춰 덮어쓰지 않는다.

```bash
export WU088_CACHE_BUILD_OUT="$WU088_RUN/cache-build"
"$WU088_PYTHON" -B - <<'PY'
import json, os, pathlib, sys, time
sys.path.insert(0,os.environ['WU088_HS'])
import backend_runner as br
run=pathlib.Path(os.environ['WU088_RUN'])
root=run/'cache-build-stage';root.mkdir(exist_ok=False)
for n in ('logs','home','tmp'):(root/n).mkdir()
tools=json.loads((run/'backend/PREFLIGHT.json').read_text())['tools']
c=dict(br.CONFIG)
env=br.clean_environment(root,pathlib.Path(os.environ['WU088_BACKEND_PREFIX']),tools,c)
for k in ('WU088_BACKEND_PREFIX','WU088_BUILD_PROVENANCE','WU088_CACHE_BUILD_OUT'):
    env[k]=os.environ[k]
br.run_stage({'id':'cache-compile','stage':'native-build','cwd':str(root),
    'argv':[tools['bash'],str(pathlib.Path(os.environ['WU088_ACCEL'])/'native_cache/build_host.sh')],
    'wall_seconds':180},root,env,c,time.monotonic()+180)
PY

for WU088_BITS in 64 128 256
do
  "$WU088_PYTHON" -B "$WU088_ACCEL/executor/make_fixture.py" \
    --output-manifest "$WU088_RUN/cache_${WU088_BITS}.json" \
    --output-root "$WU088_RUN/cache_${WU088_BITS}_tasks" \
    --build-ready "$WU088_CACHE_BUILD_OUT/BUILD_READY.json" \
    --backend-library-path "$WU088_BACKEND_PREFIX/lib" \
    --case point107 --case complex_point107 --case complex_box107 \
    --precision "$WU088_BITS" --repeat 1
  "$WU088_PYTHON" -B "$WU088_ACCEL/executor/run_local.py" \
    --manifest "$WU088_RUN/cache_${WU088_BITS}.json" --workers 1
done
"$WU088_PYTHON" -B "$WU088_ACCEL/executor/make_fixture.py" \
  --output-manifest "$WU088_RUN/cache_errors.json" \
  --output-root "$WU088_RUN/cache_errors_tasks" \
  --build-ready "$WU088_CACHE_BUILD_OUT/BUILD_READY.json" \
  --backend-library-path "$WU088_BACKEND_PREFIX/lib" \
  --case errors --precision 128 --repeat 1
"$WU088_PYTHON" -B "$WU088_ACCEL/executor/run_local.py" \
  --manifest "$WU088_RUN/cache_errors.json" --workers 1
```

총 10 tasks, native repeat=1이다. 각 task의 기본 native wall=120초, AS=1GiB, sampled RSS=768MiB와 output cap은 생성 manifest에 기록된다. baseline/cached `acb_equal` 및 real/imag exact Arb dump equality가 fixture의 자체 acceptance다. tolerance overlap만으로 대체하지 않는다. collector `COLLECTED`와 선언/완료 task count까지 확인한다.

## 5. Fortran/OpenMPI build와 1/2/4-rank smoke

실제 선택한 OpenMPI wrapper 경로를 지정한다. 다중호출 wrapper는 파일 symlink target 이름으로 치환하면 동작이 바뀔 수 있으므로 `mpifort`/`mpicc`라는 **호출 경로 이름을 유지**한다. hash는 그 경로를 열어 읽은 실제 bytes로 계산한다. 다른 환경의 예시 hash를 넣지 않는다.

```bash
: "${WU088_MPIFORT:?선택한 mpifort의 절대 호출 경로 필요}"
: "${WU088_MPICC:?선택한 mpicc의 절대 호출 경로 필요}"
export WU088_MPIFORT_SHA256
export WU088_MPICC_SHA256
WU088_MPIFORT_SHA256="$("$WU088_PYTHON" -c 'import hashlib,sys;print(hashlib.sha256(open(sys.argv[1],"rb").read()).hexdigest())' "$WU088_MPIFORT")"
WU088_MPICC_SHA256="$("$WU088_PYTHON" -c 'import hashlib,sys;print(hashlib.sha256(open(sys.argv[1],"rb").read()).hexdigest())' "$WU088_MPICC")"
"$WU088_PYTHON" -B "$WU088_ACCEL/mpi_fortran/build.py" \
  --output-dir "$WU088_RUN/mpi-build" \
  --mpifort "$WU088_MPIFORT" --mpifort-sha256 "$WU088_MPIFORT_SHA256" \
  --mpicc "$WU088_MPICC" --mpicc-sha256 "$WU088_MPICC_SHA256"
"$WU088_PYTHON" -B "$WU088_ACCEL/mpi_fortran/host_smoke.py" \
  --mpi-binary "$WU088_RUN/mpi-build/ncp64_dispatch" \
  --output-dir "$WU088_RUN/mpi-smoke" \
  --reserve-gib 16 --worker-mib 1024 --wall-seconds 120 --cpu-units 50000
```

build.py는 wrapper/compiler `--showme` 구성과 hash, source/binary identity, 실제 compile/link logs, integer vectorization report를 기록한다. build의 성공 상태는 `BUILT_NOT_MPI_RUNTIME_VERIFIED`다. smoke는 rank당 manifest가 다른 12개 integer CPU-work fixtures를 1/2/4 ranks로 실행하고 모두 12개 수집 및 동일 canonical digest일 때 `SMOKE.json.status=PASS_SYNTHETIC_MPI_1_2_4_RANKS`를 기록한다. 정수 SIMD report를 scientific SIMD 증거로 해석하지 않는다. task scope 문자열만으로 실행권한이 생긴다고 보지 않는다.

## 6. 고정 96-task native calibration

앞의 모든 gate가 통과했을 때만 진행한다. 3 valid cases를 순서 그대로 32번 나열한 96 tasks, precision=128, native repeat=1로 고정한다. 관측된 허용 total ranks 중 1/2/4/8/16/32/64에 각각 **미리 계획한 두 trial**만 수행한다. 최대 14 attempts, attempt별 900초다. 실패 자동 재시도는 없다. rank2는 계산 worker 1개다. native precision/case/argv/library identity와 task ID 순서를 바꾸지 않는다. 출력 root와 host attempt 경로만 달라진다.

```bash
"$WU088_PYTHON" -B - <<'PY'
import hashlib,json,os,pathlib,subprocess,sys
accel=pathlib.Path(os.environ['WU088_ACCEL'])
run=pathlib.Path(os.environ['WU088_RUN'])
sys.path.insert(0,str(accel/'host_plan'))
import planner
sys.path.insert(0,str(accel/'executor'))
from make_fixture import create_native_fixture
plan=planner.plan(planner.detect())
if plan['status']!='PLAN_READY':raise RuntimeError('host resource plan blocked')
ranks=list(plan['calibration_total_ranks'])
if not ranks or len(ranks)>7 or any(r not in (1,2,4,8,16,32,64) for r in ranks):
    raise RuntimeError('invalid bounded rank plan')
root=run/'native-calibration';root.mkdir(exist_ok=False)
schedule={'schema':'WU088_NATIVE_CALIBRATION_SCHEDULE_V1','scope':'SYNTHETIC_ONLY',
    'ranks':ranks,'trials_per_rank':2,'max_attempts':14,'wall_seconds_per_attempt':900,
    'tasks':96,'precision_bits':128,'native_repeat':1,'cases':['point107','complex_point107','complex_box107']*32,
    'host_plan':plan,'no_auto_rerun':True,'no_scope_expansion':True}
(root/'SCHEDULE.json').write_text(json.dumps(schedule,indent=2)+'\n')
returned=[]
for rank in ranks:
    for trial in (1,2):
        tag=f'rank_{rank}_trial_{trial}'
        manifest=root/(tag+'.json');worklist=root/(tag+'.worklist')
        host=root/(tag+'_host')
        create_native_fixture(str(manifest),str(root/(tag+'_tasks')),None,schedule['cases'],
            precision=128,repeat=1,
            build_ready=str(pathlib.Path(os.environ['WU088_CACHE_BUILD_OUT'])/'BUILD_READY.json'),
            backend_library_path=str(pathlib.Path(os.environ['WU088_BACKEND_PREFIX'])/'lib'))
        subprocess.run([sys.executable,'-B',str(accel/'mpi_fortran/export_worklist.py'),
            '--manifest',str(manifest),'--output',str(worklist)],check=True)
        argv=[sys.executable,'-B',str(accel/'host_plan/launcher.py'),
            '--manifest',str(manifest),'--worklist',str(worklist),
            '--mpi-binary',str(run/'mpi-build/ncp64_dispatch'),'--output',str(host),
            '--ranks',str(rank),'--wall-seconds','900','--reserve-gib','16','--worker-mib','1024',
            '--backend-library-path',str(pathlib.Path(os.environ['WU088_BACKEND_PREFIX'])/'lib'),
            '--execute-synthetic']
        binding={'argv':argv,'manifest_sha256':hashlib.sha256(manifest.read_bytes()).hexdigest(),
            'worklist_sha256':hashlib.sha256(worklist.read_bytes()).hexdigest(),
            'one_shot':True,'no_auto_rerun':True,'actual_HH_runs':0}
        (root/(tag+'_binding.json')).write_text(json.dumps(binding,indent=2)+'\n')
        subprocess.run(argv,check=True)
        result=json.loads((host/'HOST_RUN.json').read_text())
        collector=result['collector']
        if result['status']!='EXECUTION_COMPLETE' or collector['status']!='COLLECTED' or collector['complete_task_count']!=96:
            raise RuntimeError('incomplete calibration attempt')
        returned.append({'ranks':rank,'trial':trial,'wall_seconds':result['wall_seconds'],
            'canonical_payload_digest':collector['canonical_payload_digest']})
        if len({x['canonical_payload_digest'] for x in returned})!=1:
            raise RuntimeError('payload identity changed; timing adoption refused')
(root/'CALIBRATION_RETURN.json').write_text(json.dumps({
    'status':'NATIVE_SYNTHETIC_CALIBRATION_COMPLETE','attempts':returned,
    'actual_HH_runs':0,'scientific_promotion':False},indent=2)+'\n')
PY
```

launcher가 각 실행 직전에 자원을 다시 확인하고 rank affinity readback과 전체 collector gate를 적용한다. 저장된 plan보다 자원이 줄어 차단되면 ranks를 몰래 줄이거나 메모리 reserve를 낮추지 않는다. 실패 attempt의 manifest/binding/log/output은 보존한다. 모든 digest가 같을 때만 rank별 두 trial의 timing을 비교한다. 측정은 native 합성 workload에만 해당하며 실제 HH/G7 성능 수치가 아니다. 작은 task에서는 dispatch/hash/수집 overhead가 우세할 수 있다.

## 7. 반환·게시·백업

`HOST_EXECUTION_CONTRACT.json`의 RETURN 필드를 채운다. 최소 다음은 실제 bytes·실행 receipt로 결박한다.

- START/END HEAD/tree, 기준 소스와 successor 문서의 분리, 실제 command/exit/wall/resource/CPU/ABI.
- source archives, compiler/wrapper, backend/source/native binary, 실제 linked libraries, manifest/worklist/collector payload digest의 identity.
- backend build, baseline callback/assembly, Petras, cache matrix, MPI smoke, calibration을 각각 별도 gate로 기록. 실행되지 않은 gate는 false/NOT_EXECUTED.
- `PREFLIGHT`, 모든 stage logs/receipts, native 실행 전 binding, `BUILD_READY`, MPI `BUILD.json`/vector report/`SMOKE.json`, host binding receipts, collector 결과.
- historical ABI 자료가 실제 발견됐다면 원 binary/config/serializer→archived output custody를 evidence-only로 반환. 새 venv probe로 과거 ABI를 승인하지 않는다. 부재이면 B03=`RAW_ABI_AUTHORITY_BLOCKED` 유지.
- 실패는 IMPLEMENTATION / RUNTIME_ENVIRONMENT / RESOURCE_LIMIT / EVIDENCE_AUTHORITY로 구분. 실패 stage의 evidence를 보존하고 자동 rerun·precision/tolerance/geometry/order 확대를 하지 않는다.
- `actual_HH_runs=0`, rigorous/production/independent scientific admission=false, ε/η=null.

같은 research branch에 code/report/receipt만 ordinary non-force 게시한다. 새 branch, force, rebase, main merge는 없다. native libraries/binaries와 제3자 source archives는 공개 Git에 넣지 말고 private create-only checkpoint에 보존한다. Google Drive parent `1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM` 및 Dropbox `/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928`를 계승한다. SHA256/bytes/provider ACK/object ID/metadata size/verification tier를 기록한다. 실제 복원 byte 검증 전 `RESTORE_VERIFIED=false`다. 전송 수단이 없으면 로컬 결과를 보존하고 미전송 상태를 반환한다.

이 반환이 닫는 것은 native implementation acceptance와 합성 성능 gate다. source accuracy, actual HH feasibility, rigorous reference certificate 또는 physical/production gate를 자동 승격하지 않는다. 이후 실제 HH pilot/represented-array/G7는 실제 binary·input·ABI identity와 별도 명시적 authorization을 갖춘 새로운 scope로만 다룬다.
