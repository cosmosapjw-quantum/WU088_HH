# NCP M0/M1/M2 handoff

`HOST_PROBE.raw.json` is a byte-identical copy of
`/root/wu088_ncp_probe.djNQYK/HOST_PROBE.json` (68,532 bytes,
SHA-256 `81ff4649892619262c0f2b2717fae098f8e9b591ba7aa6528ccbb8b6afdb8cf1`).
`M1_M2_RESULT.json` is a separate, normalized execution record; it makes no
byte-identity claim for its own contents.

The probe reports CPUs 0–63 as allowed, planning budget 64, no visible cgroup
CPU quota or memory maximum, 132,752,199,680 available memory bytes, no swap,
and no warnings. Its guest topology has one reported NUMA node, singleton
thread sibling lists, and one reported shared L3 CPU list. None of these guest
values proves physical host topology. The compiler is GCC 13.3.0; long double
has 64 mantissa bits in 16 storage bytes, and `_Float128` has 113 mantissa bits.

The fresh venv and native build tree are under `/root/wu088_hh_ncp_work`.
The reference and candidate were built from this checkout with strict floating
point flags. `ncp_build.py` verifies reference source hashes, probe budget,
precision macros, and build identity. It removes `LD_PRELOAD` and
`LD_LIBRARY_PATH` from trusted compiler children. It reads source in place and
writes binaries only to the separate work root.

The existing n=4 synthetic cancellation component fixture matched exactly for
both output and sumabs at candidate teams 1 and 2. This is a component check,
not B160/B192 z=2 representative evidence or provider promotion.

The frozen runtime model `FROZEN_INPUTS.npz` and runtime grid
`completion/mixed_h/native.py` were not found on this VM. Consequently no
B160/B192 representative pair or host tuning benchmark was run. The listed
64-slot and half-budget configurations are unmeasured candidates. The next
step is to provide the immutable frozen runtime location or verified restore;
then run bounded same-host B160/B192 samples and tuning without changing the
scientific authority or expanding to M3.

To reproduce the M1 build after creating a fresh venv with NumPy 2.3.5 and
SciPy 1.17.0:

```bash
/root/wu088_hh_ncp_work/venv/bin/python research/r31s_ncp/ncp_build.py \
  --probe research/r31s_ncp/evidence/ncp_host/HOST_PROBE.raw.json \
  --work-root /root/wu088_hh_ncp_work
```
