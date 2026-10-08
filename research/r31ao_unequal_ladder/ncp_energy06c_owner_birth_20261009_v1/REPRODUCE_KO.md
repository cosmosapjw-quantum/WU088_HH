NCP 기존 검증된 owner cache와 Rust1.94.1을 사용한다. 기존 runtime/science suites를 변경하거나 실행하지 않는다.

```bash
export RUSTC=/root/WU088_HH_ON02_20261005/toolchain/prefix/bin/rustc
export RUSTFLAGS='-C opt-level=3 -C target-cpu=x86-64'
export CARGO_TARGET_DIR=/path/to/new-build
export HH_SEED=/root/WU088_HH_MASTER_EXEC_20261008/inputs/on06g/HH_ON06G_20261008_v1/seed
cd /root/WU088_HH_ENERGY06C_20261009/cargo
/root/BASS_HE_runtime/toolchain/cargo-1.94.1-x86_64-unknown-linux-gnu/cargo/bin/cargo test --locked --offline --bin owner_birth_probe -j 2
```

생성 Cargo wrapper/원 dependency 및 binary/checkpoint는 private sealed ZIP에 있다. public projection은 source/summary이고 전체 native restore bundle이 아니다. ZIP SHA/manifest 및 FINAL_SOURCE_BINDING_V3를 확인한다. preBE CLI는 SEED_DIR 한 argument만 받으며 checkpoint/source root/trajectory를 실행하지 않는다. prepare.py는 초기 RED scaffold 생성기이므로 재개 반환물에 다시 실행하지 않는다.
