# 영향범위 검증과 복원 명령

원 과학 이력과 ENERGY05 root를 재실행하지 않는다. 실행원문은 증거 COMMANDS.jsonl에 있다.

```bash
HH_ON06G_CRATE=/root/WU088_HH_MASTER_EXEC_20261008/inputs/on06g/HH_ON06G_20261008_v1/worktree/rust/rei_microphysics /root/wu088_hh_ncp_work_v2/venv/bin/python -B -m pytest -q -p no:cacheprovider research/r31ao_unequal_ladder/ncp_master_execution_20261008_v1/test_energy06_preflight.py
```

Cargo wrapper는원sealedG crate와sealedENERGY05 tangent_lib.rs를path dependency로연결했다. runs/master_20261008/cargo_probe/Cargo.lock와 CARGO_PROBE_BINDING_FINAL를읽고동일source/compiler/env를확인한다. 새변경이있을때만 scoped cargo test --locked --offline --all-targets를사용한다. 원dependency과학suite는호출하지않는다.

checkpoint_probe는 INPUT NEW_OUTPUT EXPECTED_TIME 세인자를받고 NEW_OUTPUT/complete로4member복사본을게시한다. process exit0·해시·완료영수증도함께확인하고디렉터리존재만으로durable성공을추론하지않는다. existing출력거절, .pending은미완성이다. 원격복구된원본SHA/manifest를먼저확인한다. trustedcodec/source-tag는임의proof를인증하지않는다.

checkpoint_moment_audit.py --root SEALED_G --final VERIFIED_FINAL_GENERATION --output NEW_JSON은8개의기존seed/final배열만exact검산한다. root/history/source호출없음. standalone데이터상품이아니며원봉인자료를PACKAGE_INDEX의ID/SHA로회수해야한다.
