# 제한 재현 계약
본 인계는 자동 재실행 지시가 아니다. 완료 target/old suite를 다시 실행하지 않는다.
원로그는 evidence/RUN_LEDGER.jsonl 및 각 .stdout/.stderr/.json에 있다. 실제 명령은 cargo build --offline --locked --bin phys06_targets 및 명시된 새 target 6개뿐이며 기존 Rust1.94.1을 사용했다. run_bounded.py는 systemd cgroup 자원한계 확인과 stdout/stderr/time/RSS 수집용이다.
변경 의존성이 새로 생긴 경우에만 handoff 한계 안에서 해당 target/build를 좁혀 실행한다. 현재 native/IVP/heavy ceiling0을 유지한다.
로컬 ZIP/manifest 검증은 tools/verify_local_package.py로 수행할 수 있으며 과학 코드는 실행하지 않는다. 의존 sibling ncp_energy06e_certificate_20261010_v1/original_owner_dependency는 고정 v2 Git tree에 있으며 원본을 수정하지 않았다.
