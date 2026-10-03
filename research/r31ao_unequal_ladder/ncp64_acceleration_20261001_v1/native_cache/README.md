# Native callback cache candidate

The additive API is `wu088::polynomial_field_cached(..., Contract&, CacheStats&)` and `wu088::cached_slice_callback`, declared in `cached_callback.hpp`. `CachedSlice` contains the original `Slice source` plus a caller-owned `CacheStats*`. A process or thread needs its own mutable contract/stats; immutable parameters may be shared. Original source files remain unchanged.

Build only on a host with the pinned FLINT 3.4.0/GMP 6.3.0/MPFR 4.2.2 sidecar and verified backend record:

```bash
export WU088_BACKEND_PREFIX=/absolute/verified/prefix
export WU088_BUILD_PROVENANCE=/absolute/BACKEND_BUILD_PROVENANCE.json
export WU088_CACHE_BUILD_OUT=/absolute/new/cache-build
bash native_cache/build_host.sh
```

The script builds the source baseline and cached variant together, verifies dynamic-library paths and hashes, and emits `BUILD_READY.json`. It does not build libraries or execute the fixture. Compile `cached_callback.cpp` once; do not additionally compile old `callback.cpp`, which would duplicate definitions. A guarded executor must reverify the executable and linked-library identities immediately before later execution. `BUILD_READY.json` records these identities and explicitly says native equality is unverified.

The native worker protocol is:

```text
/absolute/native_cache_synthetic --output /absolute/new/payload.bin --case point107 --repeat 3 --precision 192
```

Cases are `point107`, `complex_point107`, `complex_box107`, and `errors`. Repeat is bounded to 1–100 and precision to 32–4096 bits. `errors` requires repeat 1. `--output` must name a new absolute file in an existing isolated directory; creation uses `O_EXCL`. There is no actual-HH input option. Recommended host verification matrix: the three valid cases at 64, 128 and 256 bits with repeat 2, plus `errors` at 128 bits. These are commands to be executed later under the host resource guard, not results already obtained.

Successful payload schema is `WU088_CACHE_SYNTHETIC_PAYLOAD_V1`, scope `SYNTHETIC_ONLY`. Exact real/imaginary `arb_dump_str` values are stored as JSON strings. The raw payload excludes timing, counters, output path and repeat count; the executor should retain its bytes directly and compare SHA256 values across worker counts. A separate stdout JSON contains paired timing and operation counters. Failure exits 2 and cannot produce a successful complete payload.

Current evidence: `VERIFICATION.json`, `STATIC_CHECKS.log`, `SOURCE_LOCK.json`. The mathematical cache argument and limitations are in `CACHE_EQUIVALENCE.md`. Native compilation/equality/benchmark remain unexecuted because this environment lacks the installed pinned backend and development headers. No measured native or NCP speedup is claimed.
