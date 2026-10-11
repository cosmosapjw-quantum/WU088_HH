"""Serial PHYS07 first-run wrapper. No retries, installs, or scientific preflight."""
from pathlib import Path
import argparse, datetime, hashlib, json, os, resource, selectors, signal, subprocess, time

ROOT = Path(__file__).resolve().parents[1]
CG = Path('/sys/fs/cgroup/wu088_phys07_20261011')
CAP = 32 * 1024 * 1024
MEM = 512 * 1024 * 1024
TARGETS = ('phys07_sourcebox_full_first', 'phys07_sourcebox_first_half_first')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def inventory():
    files = []
    for folder in ('src', 'candidate/src', 'inputs'):
        for p in sorted((ROOT / folder).rglob('*')):
            if p.is_file():
                files.append(dict(path=str(p.relative_to(ROOT)), bytes=p.stat().st_size, sha256=digest(p)))
    for name in ('Cargo.toml', 'Cargo.lock', 'candidate/Cargo.toml', 'tools/run_bounded.py'):
        p = ROOT / name
        if p.exists():
            files.append(dict(path=name, bytes=p.stat().st_size, sha256=digest(p)))
    return files

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('run_id')
    ap.add_argument('mode', choices=('build', 'target'))
    ap.add_argument('command', nargs=argparse.REMAINDER)
    args = ap.parse_args()
    assert args.command
    evidence = ROOT / 'evidence' / args.run_id
    assert not evidence.exists(), 'First record already exists; replay denied'
    ledger = ROOT / 'evidence/RUN_LEDGER.jsonl'
    previous = [json.loads(s) for s in ledger.read_text().splitlines()] if ledger.exists() else []
    if args.mode == 'target':
        assert args.run_id in TARGETS
        assert args.command == ['target/debug/hh_phys07_sourcebox', args.run_id, 'inputs/FROZEN_SOURCE_CONTRACT.json']
        assert not any(r['run_id'] == args.run_id for r in previous)
        if args.run_id == TARGETS[1]:
            assert any(r['run_id'] == TARGETS[0] for r in previous)
    else:
        builds = [r for r in previous if r['mode'] == 'build']
        assert len(builds) < 3
        if builds:
            assert builds[-1]['exit'] != 0, 'Only concrete compile repairs allowed'
        assert args.command == ['cargo', 'build', '--offline', '--locked', '--jobs', '1', '--bin', 'hh_phys07_sourcebox']
    observed = {n: (CG / n).read_text().strip() for n in ('memory.max', 'memory.swap.max', 'cpu.max')}
    assert observed == dict(zip(('memory.max', 'memory.swap.max', 'cpu.max'), ('536870912', '0', '100000 100000')))
    assert not (CG / 'cgroup.procs').read_text().strip(), 'Concurrent child denied'
    evidence.mkdir(parents=True)
    before = inventory()
    executable = ROOT / 'target/debug/hh_phys07_sourcebox'
    binary_before = digest(executable) if executable.exists() else None
    cpu = min(os.sched_getaffinity(0))
    env = dict(os.environ)
    env['PATH'] = '/root/BASS_HE_runtime/toolchain/cargo-1.94.1-x86_64-unknown-linux-gnu/cargo/bin:/root/WU088_HH_ON02_20261005/toolchain/prefix/bin:' + env['PATH']
    env['CARGO_BUILD_JOBS'] = '1'
    assert not env.get('RUSTFLAGS') and not env.get('CARGO_ENCODED_RUSTFLAGS')
    wall = 300 if args.mode == 'build' else 60
    output_dir = ROOT / 'results' / ('full' if args.run_id == TARGETS[0] else 'first_half')
    def child_setup():
        (CG / 'cgroup.procs').write_text(str(os.getpid()))
        os.sched_setaffinity(0, {cpu})
        if args.mode == 'target':
            resource.setrlimit(resource.RLIMIT_AS, (MEM, MEM))
        resource.setrlimit(resource.RLIMIT_FSIZE, (CAP, CAP))
    utc = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()
    planned = dict(run_id=args.run_id, mode=args.mode, command=args.command, cwd=str(ROOT), started_utc=utc(),
                   source_input_manifest=before, executed_binary_sha256_before=binary_before,
                   dependency_manifest_sha256=digest(ROOT/'evidence/DEPENDENCY_SOURCE_MANIFEST.json'),
                   host_preflight_sha256=digest(ROOT/'evidence/HOST_PREFLIGHT.json'),
                   frozen_contract_sha256=digest(ROOT/'inputs/FROZEN_SOURCE_CONTRACT.json'),
                   compiler_flags=dict(RUSTFLAGS=env.get('RUSTFLAGS'), CARGO_ENCODED_RUSTFLAGS=env.get('CARGO_ENCODED_RUSTFLAGS'), CARGO_BUILD_JOBS='1'),
                   limits_requested=dict(wall_seconds=wall, memory_bytes=MEM, address_space_bytes=MEM if args.mode=='target' else None,
                                         swap_bytes=0, cpu_cores=1, concurrency=1, output_bytes=CAP),
                   limits_enforced=dict(cgroup=str(CG), observed=observed, affinity=[cpu], process_group_timeout=True,
                                        aggregate_output_monitor=True, single_file_RLIMIT_FSIZE=CAP))
    (evidence / 'PREDISPATCH.json').write_text(json.dumps(planned, indent=2))
    start = time.monotonic()
    proc = subprocess.Popen(args.command, cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            start_new_session=True, preexec_fn=child_setup)
    planned['pid'] = proc.pid
    planned['process_group'] = proc.pid
    sel = selectors.DefaultSelector()
    streams = {proc.stdout: (evidence/'stdout.txt').open('wb'), proc.stderr: (evidence/'stderr.txt').open('wb')}
    for stream in streams:
        os.set_blocking(stream.fileno(), False)
        sel.register(stream, selectors.EVENT_READ)
    written = 0
    killed = None
    while sel.get_map() or proc.poll() is None:
        artifacts = sum(p.stat().st_size for p in output_dir.rglob('*') if p.is_file()) if args.mode == 'target' and output_dir.exists() else 0
        if not killed and (time.monotonic()-start >= wall or written+artifacts > CAP):
            killed = 'WALL_LIMIT' if time.monotonic()-start >= wall else 'OUTPUT_LIMIT'
            os.killpg(proc.pid, signal.SIGKILL)
        for key, _ in sel.select(.01):
            b = os.read(key.fileobj.fileno(), 65536)
            if b:
                streams[key.fileobj].write(b)
                written += len(b)
            else:
                sel.unregister(key.fileobj)
    proc.wait()
    # Terminate any descendants even when the main process exited first.
    remaining = (CG/'cgroup.procs').read_text().strip()
    if remaining:
        try: os.killpg(proc.pid, signal.SIGKILL)
        except ProcessLookupError: pass
        if (CG/'cgroup.kill').exists(): (CG/'cgroup.kill').write_text('1')
    for stream in streams.values(): stream.close()
    usage = resource.getrusage(resource.RUSAGE_CHILDREN)
    after = inventory()
    record = dict(planned, finished_utc=utc(), elapsed_s=time.monotonic()-start, exit=proc.returncode,
                  termination=killed, timeout=killed=='WALL_LIMIT', stdout_bytes=(evidence/'stdout.txt').stat().st_size,
                  stderr_bytes=(evidence/'stderr.txt').stat().st_size, stdout_sha256=digest(evidence/'stdout.txt'),
                  stderr_sha256=digest(evidence/'stderr.txt'), rss_measured_bytes=usage.ru_maxrss*1024,
                  cpu_user_s=usage.ru_utime, cpu_system_s=usage.ru_stime,
                  executed_binary_sha256_after=digest(executable) if executable.exists() else None,
                  source_input_manifest_after=after, source_changed_during_run=before!=after,
                  cgroup_memory_peak_bytes=int((CG/'memory.peak').read_text()),
                  cgroup_memory_peak_scope='shared serial cgroup lifetime; per-child RSS reported separately',
                  cgroup_memory_events=(CG/'memory.events').read_text(), remaining_processes_after_exit=remaining)
    record['output_artifact_bytes'] = sum(p.stat().st_size for p in output_dir.rglob('*') if p.is_file()) if args.mode == 'target' else None
    record['output_limit_satisfied'] = written + (record['output_artifact_bytes'] or 0) <= CAP
    (evidence/'EXECUTION.json').write_text(json.dumps(record,indent=2)+'\n')
    with ledger.open('a') as f: f.write(json.dumps(record)+'\n')
    print(json.dumps({k:record[k] for k in ('run_id','exit','elapsed_s','rss_measured_bytes','termination','executed_binary_sha256_before','executed_binary_sha256_after','source_changed_during_run')}))
    raise SystemExit(124 if killed else proc.returncode)

if __name__ == '__main__': main()
