# Source and implementation boundaries

The selected numerical contract comes from the immutable repository source, not a new approximation: `../gap_closure_20261001_g0_g6_v1/validated_callback/callback.cpp`, its header, and `../theory_closure_20261001_v1`. Exact source identities are in `native_cache/SOURCE_LOCK.json` and the delivery manifest. The original helper bodies are included once in the same translation unit as the cached entrypoint.

Host scheduling/build decisions were checked against these primary references on 2026-10-01:

* Open MPI 5.0.10 mpirun: https://docs.open-mpi.org/en/v5.0.10/man-openmpi/man1/mpirun.1.html . Its CPU-list/rankfile processor indices may use hwloc logical numbering. This package instead applies and reads back explicit Linux OS CPU affinity in each rank guard, and uses `--bind-to none` at the MPI layer.
* Open MPI 4.1.8 mpirun: https://www.open-mpi.org/doc/v4.1/man1/mpirun.1.php . Local slots, process count and oversubscription are made explicit; defaults are not treated as target topology evidence.
* GNU Fortran C interoperability: https://gcc.gnu.org/onlinedocs/gfortran/Interoperability-with-C.html . The dispatcher calls the C process bridge with `ISO_C_BINDING` and `bind(C)`.
* GNU GCC optimization options: https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html . Native scientific code keeps strict floating semantics; compiler vector reports are captured for the integer dispatcher. An optimization flag is not proof that a scientific loop vectorized.
* POSIX process spawning: https://pubs.opengroup.org/onlinepubs/007904975/functions/posix_spawn.html and Linux manual https://man7.org/linux/man-pages/man3/posix_spawn.3.html . The bridge uses explicit argument vectors and a separate process group, not shell interpolation.

These references support implementation choices only. They do not show that this host has OpenMPI, that the selected compiler can build the Fortran source, or that the NCP workload will obtain any particular speedup. Build/runtime receipts on the actual NCP are still required.
