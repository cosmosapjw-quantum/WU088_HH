# PHYS73 runtime intake

2026-10-20 UTC, sandbox only. No HH campaign was executed.

The attached Rust1.94.1 archive is usable. SHA256 `294b3d81fa72e62581276290c60c81eb8b58498d333d422ca1dfc432877d0c40`,192287020 bytes. The supplied detached signature was read but is **not cryptographically verified**: no independently trusted key was selected. The attached environment script only names an old `/mnt/data` prefix and was not sourced.

The archive was inspected(51085 members), then only rustc/cargo/std plus installer metadata were safely extracted(194 members,595641109 bytes). The installer ran with scoped prefix `/tmp/phys73_runtime/prefix` and `--disable-ldconfig`; no global installation was changed. `rustc --version --verbose` reports1.94.1,e408947bfd200af42db322daf0fadfe7e26d3bd1,LLVM21.1.8; cargo reports1.94.1,29ea6fb6a5db279426f4cc4e17aa385f05a0cfbc.

The std-only `runtime_smoke.rs` compiled and executed successfully. It computes the already-established PHYS72 scalar tail in f64 only to check the new runtime. It reports relative difference2.220446049250313e-16 against the rounded reference and `certified:false`. This is not a new mathematical certificate or a speedup measurement. Install6.227997491994756s,compile0.09691282799758483s,run0.0011682769982144237s on this sandbox; allexit0. Full commands,outputs,and hashes are in `RUST_INSTALL_AND_SMOKE.json`.

Resource observations: process affinity9 CPUs(0–8),cgroupquota8 CPUs(`800000 100000`),cgroupmemory8589934592bytes(8GiB),and Rustavailable_parallelism8. These are sandbox observations. NCP64core/128GB is the user target and must be detected again on the actual host.

`gfortran` was absent on PATH, but the prior scoped GNUFortran13.3.0 install remains at `/tmp/wu088_phys72_fortran/root/usr/bin/x86_64-linux-gnu-gfortran-13`; version query succeeded. No new Fortran compile/run was needed for this capability decision.

Use absolute `/tmp/phys73_runtime/prefix/bin/rustc` for a direct std-only build, or set task-scoped `RUSTC` and PATH when using Cargo. The project must still pin its input,source,binary,compiler flags,and actual worker plan in each NCP result.
