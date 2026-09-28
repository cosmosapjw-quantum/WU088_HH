# R31V NCP 실제 명령 및 종료 상태

- `git ls-remote --heads origin codex/r31v-postidle-controls-20260928`: exit 0, e7248a2b356392a47bda44d180e0d6ed4f012b20.
- `git fetch origin codex/r31v-postidle-controls-20260928 && git worktree add /root/WU088_HH_R31V -b codex/r31v-postidle-controls-20260928 origin/codex/r31v-postidle-controls-20260928`: exit 0. 기존 R31T worktree 보존.
- `python -m pytest -q research/r31v_postidle/test_controls.py research/r31v_postidle/test_metric_controls.py research/r31v_postidle/test_driver.py`: exit 127 (`python` 명령 없음; 테스트 미시작).
- `python3 -m pytest -q research/r31v_postidle/test_controls.py research/r31v_postidle/test_metric_controls.py research/r31v_postidle/test_driver.py`: exit 1 (`pytest` 모듈 없음; 테스트 미시작).
- `/root/wu088_hh_ncp_work_v2/venv/bin/python -m pytest -q research/r31v_postidle/test_controls.py research/r31v_postidle/test_metric_controls.py research/r31v_postidle/test_driver.py`: exit 0, 67 PASS (수정 전).
- `/root/wu088_hh_ncp_work_v2/venv/bin/python -m pytest -q research/r31s_ncp/tests/test_m3_throughput.py research/r31s_ncp/tests/test_m3_full_pair_screen.py research/r31s_ncp/tests/test_m3_h0_authority.py research/r31s_ncp/tests/test_authority_seed.py research/r31s_ncp/tests/test_ncp_build.py`: exit 0, 14 PASS.
- `python3 research/r31v_postidle/m3_postidle.py --phase describe`: exit 0, DESCRIBE_ONLY, native calls 0.
- `env -u LD_PRELOAD -u LD_LIBRARY_PATH /root/wu088_hh_ncp_work_v2/venv/bin/python`으로 `_runtime()`과 `_require_existing_h0_cache()` 호출: 수정 전 exit 1, `H0 build cache missing`; compiler symlink 버전 문자열 불일치 재현. 수정 후 exit 0.
- manifest 14개 SHA/size 및 baseline ancestor 도달성: exit 0.
- source/build/H0/pilot/exactness/ABI audit: exit 0, `SOURCE_BUILD_AUDIT.json`.
- 수정 후 focused + 관련 M3 테스트: exit 0, 84 PASS. 전체 과학 suite 미실행.

## Prepare

외부 `timeout --signal=TERM --kill-after=30s 2700s`가 명령과 자식 process group을 감쌌다. 아래 본체는 exit 0, `prepare.exit=0`이다. stdout/stderr는 각각 `prepare.stdout`, `prepare.stderr`에 저장됐다.

```bash
env -u LD_PRELOAD -u LD_LIBRARY_PATH /root/wu088_hh_ncp_work_v2/venv/bin/python research/r31v_postidle/m3_postidle.py --phase prepare --build /root/wu088_hh_ncp_work_v2/BUILD_STDOUT.json --h0-cache /root/wu088_hh_ncp_work_v2/m3_h0_build --grant research/r31v_postidle/evidence/ncp_host/20260928T132239Z_r31v/GRANT.json --reference-cache research/r31v_postidle/evidence/ncp_host/20260928T132239Z_r31v/reference_cache --exactness research/r31s_ncp/evidence/ncp_host/20260928T092409Z_18dd6940/M3_FULL_PAIR_EQUIVALENCE.json --pilot research/r31s_ncp/evidence/ncp_host/20260928T092409Z_18dd6940/M3_B192_PILOT.json --configs 64x1,32x2,30x2,4x16 --out research/r31v_postidle/evidence/ncp_host/20260928T132239Z_r31v/reference_prepare.json
```

## Benchmark

외부 `timeout --signal=TERM --kill-after=30s 5400s`가 명령과 자식 process group을 감쌌다. 아래 본체는 exit 0, `benchmark.exit=0`이다. stdout/stderr는 각각 `benchmark.stdout`, `benchmark.stderr`에 저장됐다.

```bash
env -u LD_PRELOAD -u LD_LIBRARY_PATH /root/wu088_hh_ncp_work_v2/venv/bin/python research/r31v_postidle/m3_postidle.py --phase benchmark --build /root/wu088_hh_ncp_work_v2/BUILD_STDOUT.json --h0-cache /root/wu088_hh_ncp_work_v2/m3_h0_build --grant research/r31v_postidle/evidence/ncp_host/20260928T132239Z_r31v/GRANT.json --reference-cache research/r31v_postidle/evidence/ncp_host/20260928T132239Z_r31v/reference_cache --exactness research/r31s_ncp/evidence/ncp_host/20260928T092409Z_18dd6940/M3_FULL_PAIR_EQUIVALENCE.json --pilot research/r31s_ncp/evidence/ncp_host/20260928T092409Z_18dd6940/M3_B192_PILOT.json --configs 64x1,32x2,30x2,4x16 --out research/r31v_postidle/evidence/ncp_host/20260928T132239Z_r31v/m3b_132.json
```
