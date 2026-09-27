# R31P direct midpoint source handoff

Canonical node: `R31P_MIDPOINT_DIRECT_SOURCE_MATERIALIZATION`.

This node materializes the five R31J-preregistered midpoint sentinels
`z = [4,12,24,40,56]` before any interpolation target is evaluated.

Frozen post-return interpolation contract:

- method: piecewise linear only after direct-midpoint validation;
- max direct-vs-interpolated H error: `2e-7 Eh`;
- whitened independent generator relative error: `2e-12`;
- interpolated raw matrices must also pass the inherited raw matrix gates;
- only failing intervals may be bisected;
- minimum interval width: `1 a0`;
- unresolved failure: `STOP_INTERPOLATION_RESOLUTION_UNRESOLVED`.

## Local work only

For every midpoint, compute direct H at B160 and B192 using the already promoted
R31M tuned foreign-H sidecar. The Ryzen 9 5900X host profile selects 2 outer
processes x 12 OpenMP threads with SMT, one process per CCD. Existing bounded
12-pair delta backup/ACK remains unchanged.

OD192 and JVP192 use the recovered CP4 source family and 12 outer physical-core
serial pair workers. There is no new inner native parallelism in these kernels.

Ionic z=4,12,24 reuses the admitted CP4 nodes. Only z=40 and z=56 run the strict
CP4 `node_cli_v2.py` 20/24/ld24 three-job admission sequence (2 native threads).

No interpolation, full49 admission, propagation or observable computation runs
in the local handoff.

## Command

```bash
cd ~/WU088_HH
git fetch origin
git switch r31p-midpoint-direct
git pull --ff-only

export WORK=/mnt/sn850x2t/hh_heavy_manual_20260926
export RUNTIME="$WORK/runtime/WU088_HH_LOCAL_RUNTIME_SEED_20260926_v2"
source "$WORK/venv/bin/activate"
export GDRIVE_RCLONE_REMOTE='gdrv:'
export DROPBOX_RCLONE_REMOTE='dbx:'

bash scripts/r31p_run_midpoints.sh
```

Expected terminal status:

`R31P_MIDPOINT_DIRECT_COMPLETE_DURABLE`

Canonical return artifact:

`$WORK/r31p_midpoint_direct/R31P_MIDPOINT_DIRECT_SUMMARY.json`

Completed anchor pair states are not rewritten.
