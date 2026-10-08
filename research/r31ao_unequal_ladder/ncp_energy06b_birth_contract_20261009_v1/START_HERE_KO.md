# NCP local Codex 시작 프롬프트: HH-ENERGY06B → ENERGY06C

다음 작업을 기존 WU088_HH NCP 환경의 local Codex로서 수행하라.

1. 저장소 `cosmosapjw-quantum/WU088_HH`의 `research/ncp-master-execution-20261008` 브랜치를 먼저 fetch하되 기존 dirty checkout, consumed registry, checkpoint와 다른 사람의 진행을 덮어쓰지 마라. 그 브랜치에 게시된 새로운 `research/r31ao_unequal_ladder/ncp_energy06b_birth_law_20261009_v1/LOCAL_CODEX_HANDOFF_KO.md`, `THEORY_KO.md`, `REPORT_KO.md`, `INPUT_IDENTITY.json`, `FINAL_VERIFICATION.json`을 모두 읽고 상세 계약을 우선하라.
2. 기존 NCP sealed-return ZIP `WU088_HH_NCP_MASTER_RETURN_20261008_sha_c0cb24b95a06.zip`과 ON06G의 source/checkpoint는 현지 검증된 캐시를 우선 사용한다. 2026-10-09 ENERGY06B 패키지가 없으면 handoff의 Drive/Dropbox source identity를 사용하여 인증된 한 provider에서 직접 회수하고 SHA/CRC/payload manifest를 검증하라. 수동 사용자 재업로드부터 요청하지 마라.
3. 먼저 `python -B -m unittest discover -s tests -v`를 실행하고, 새 독립 출력 디렉터리에서 `python -B research_loop.py --output NEW_NONEXISTENT_DIR`를 실행하라. EXPECTED: 15개 신규 scoped unit tests, 18개 synthetic scalar BE direct case, 5개 tangent case, 고정된 NCP birth-moment의 exact Fraction 재현. **이 결과는 실제 HH coupled root/physics PASS가 아니다.**
4. `same_underlying_source_law`와 `distinct_full/twohalf_birth_quadratures`를 분리한 명시적 opt-in 실제 owner source 계약을 새 branch/worktree에서 구현하라. **두 discrete birth measures를 억지로 같게 만들지 마라.** 원 `source_weights` 시각/방향 분포, `dt*SOURCE` binary64, birth-before-BE, HH thermal/event ownership, full diagnostic과 accepted two halves만의 ledger를 보존하라.
5. 실제 ON06G 128방향×33노드의 *원본* 입력만 사용하여 같은 `theta,lambda` 초기 state에서 full/half/half의 input, tangent, photon transport/remap, birth, BE gas roots, paired error의 관계를 단계별로 구현·검증하라. 원 ENERGY05 no-birth chain을 birth-included owner의 수락 근거로 전용하지 마라. 새 scientific dispatch 권한이 없으면 구현·synthetic tests·ABI/source gate·실행 제안까지만 진행하고 무단 native root/trajectory를 실행하지 마라.
6. 별도 C1 `272/0` successor는 full-box analytic/sign/rank/holomorphic proof, distinct worker, live finite cgroup, 새 exact approval를 먼저 닫고 과거 FD1/FD2/6-cell scope는 재사용하지 마라. 승인 미비 시 `authorization_record=null, dispatch=0`을 유지하라.
7. 각 단계의 원 코드/명령/출력/실패/raw hash와 `RUN_LEDGER`, `CLAIM_LEDGER`, `BLOCKERS`, checkpoint 증거를 남기고, 승인된 범위의 결과는 새 Git 연구 경로와 Drive·Dropbox에 create-only 백업하라. `UPLOAD_VERIFIED`와 `RESTORE_VERIFIED`를 분리하고 완료 영수증을 남겨라.

최종 반환에는 실제 실행된 test/native 횟수, physical/scientific/continuous gate 상태, 미완료 수치 작업의 최소 승인전제, Git HEAD/tree, 두 provider ID·name·size/hash 및 다음 `NEXT_HANDOFF_KO.md`를 포함하라. **NCP legacy24/289·265unbounded·epsilon_C/R null·B22OPEN·ON06G total256·canonical HH OFF와 physical/production HOLD는 새 권위 있는 결과 없이 바꾸지 마라.**
