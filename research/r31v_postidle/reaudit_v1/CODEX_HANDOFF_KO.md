# Codex handoff: R31V 재감사 후 제한 재검증

이 프롬프트의 목적은 이미 제공된 수정 코드의 독립 검토와 NCP 경량 재검증이다. 새 개발 프로젝트나 heavy benchmark를 시작하지 않는다. 기존 POSTREVIEW_NCP_HANDOFF_KO.md보다 이 문서가 우선한다. 단, 실제 remote에 후속 commit이 있으면 그 diff를 읽고 반영한다.

## 1. Authority와 작업 공간

Repo: cosmosapjw-quantum/WU088_HH
Branch: codex/r31v-postidle-controls-20260928
Draft PR: #14
재감사 baseline: 7472171a3ff0e343dab2131cf063082e4740f7ff
baseline tree: b2bae4e294f06de3a567ef8fdc519f3bfd4385a8

새 publication commit/tree는 PR의 현 ref와 detached PUBLICATION_RECEIPT.json에서 확인한다. 프롬프트 안의 baseline을 실행 HEAD로 오인하지 마라. current ref, commit/tree, Python·NumPy·pytest identity를 RUN에 저장한다. 기존 dirty worktree와 raw evidence를 보존하고 fresh detached worktree를 사용한다. 강제 reset/clean/force push/main merge/타 owner PID kill/cgroup 변경은 금지다.

REVIEWED_FILES.json의 covered file SHA/size를 현재 checkout과 대조한다. 최초 FILE_MANIFEST.json은 historical checkpoint로 남겨둔 것이므로 현재 driver/test와 불일치한다고 이전 SHA로 되돌리지 않는다. manifest mismatch가 새 REVIEWED_FILES에서 생기면 provenance blocker로 멈춘다. 미래 identity와 현재 관측을 섞지 않는다.

## 2. blind reviewer 단계

이 handoff는 orchestrator용이며 reviewer에게 통째로 주지 않는다. 가능한 적격 isolated reviewer에게 BLIND_REVIEW_BRIEF_KO.md와 그 allowlist만 전달한다. 기존 결론·예상 통과 수·finding 목록·이 대화는 전달하지 않는다. 실제 reviewer session/harness admission을 기록한다. 독립 reviewer가 없거나 이미 노출되었으면 그 범위는 BLOCKED/UNBLINDED로 남기고 자가검토를 blind로 이름만 바꾸지 않는다.

reviewer가 source-first review와 독자 반례를 BLIND_REVIEW.json/md로 동결하고 hash를 반환한 뒤에만 REPORT_KO.md, RESULT.json, 새 tests를 공개한다. 발견사항을 대조해 실제 반례가 있는 추가 오류만 수정한다. 리뷰 의견에 자동 동의하지 말고 잘못된 지적이면 코드/검사 근거로 반박한다. 반복 감사가 아니라 첫 적격 검토, 필요한 최소 repair, 최종 revalidation까지가 범위다.

## 3. NCP 경량 실행

기존에 사용한 /root/wu088_hh_ncp_work_v2/venv/bin/python이 실제로 존재하는지 확인한다. 존재하면 PY로 사용하고, 없으면 현재 프로젝트의 검증된 환경을 찾는다. 새로운 시스템 패키지/컴파일러 설치나 native build는 이번 범위가 아니다. 실행 source worktree와 반환 evidence 경로를 분리한다. 새 RUN은 mktemp 또는 존재하지 않는 timestamp 경로로 만든다.

```bash
set -euo pipefail
# PY, RUN은 확인된 절대 경로이며 RUN은 이번에 새로 만든 디렉터리여야 한다.
"$PY" -m py_compile \
  research/r31v_postidle/m3_postidle.py \
  research/r31v_postidle/test_driver.py \
  research/r31v_postidle/test_adversarial_reaudit.py
"$PY" -m pytest -q \
  research/r31v_postidle/test_controls.py \
  research/r31v_postidle/test_metric_controls.py \
  research/r31v_postidle/test_driver.py \
  research/r31v_postidle/test_adversarial_reaudit.py \
  research/r31s_ncp/tests/test_m3_throughput.py \
  research/r31s_ncp/tests/test_m3_full_pair_screen.py \
  research/r31s_ncp/tests/test_m3_h0_authority.py \
  research/r31s_ncp/tests/test_authority_seed.py \
  research/r31s_ncp/tests/test_ncp_build.py \
  --junitxml="$RUN/PYTEST.xml" 2>&1 | tee "$RUN/PYTEST.txt"
"$PY" research/r31v_postidle/m3_postidle.py --phase describe > "$RUN/DESCRIBE.json"
"$PY" research/r31v_postidle/reaudit_v1/replay_raw.py --out "$RUN/RAW_REAUDIT.json"
```

각 command의 실제 exit를 명시적으로 별도 기록한다. set -e 때문에 script가 중단되더라도 완료한 evidence를 버리지 않는다. 테스트를 고의 실패시키는 RED phase를 NCP에서 반복할 필요는 없다. 예상 범위는 133 tests이나 실제 collected/pass/fail/skip 값을 그대로 보고한다. sandbox PASS를 NCP PASS로 대체하지 않는다. 이 명령은 H0Authority 생성/native H·pair 호출, pool benchmark를 수행하지 않는 경량 검사다. 기존 grid/source 확인과 synthetic component fixture는 허용된다.

## 4. 판정 경계

원 M3B 12 rows가 새 validator를 통과했다는 것은 저장된 관측의 일관성이 유지된다는 뜻이다. timed candidate 배열 전체의 독립 재계산이 아니며, source-derived native call count도 별도 계측기가 아니다. root/leaf counter 차이를 엄밀한 non-HH CPU 상계나 host isolation 증명으로 쓰지 않는다. prior manifest/history는 overwrite하지 않는다.

현재 scope에서 source/control 검토와 focused NCP revalidation을 닫을 수는 있다. production/provider/full49/trajectory admission, host exclusivity 인증, 전역 최적 layout 판정은 닫을 수 없다. 새 native preparation, M3A/M3B, z=1, z=0.5, full144, trajectory, M5 및 CR/HE 재실행은 금지다. 추가 layout 확인도 자동 시작하지 않는다.

## 5. 반환·GitHub·백업

반환 JSON에 reviewed/executed commit/tree, source manifest hash, 환경 identity, reviewer ID/exposure/admission, actual command/exits, tests, raw replay, 수정 diff, failure classification, M3B_RERUN=false, NEW_SCIENTIFIC_NODES=0, production_admitted=false를 담는다. 적격 reviewer가 없는 경우 independent_review_admitted=false를 유지한다.

실행 source checkout을 덮지 말고 publication worktree에서 새 evidence 디렉터리에 append한다. remote가 바뀌지 않았는지 확인한 뒤 ordinary non-force push한다. race 또는 conflict가 있으면 강제 갱신하지 않는다. 기존 raw/FAILED/RED 기록을 지우지 않는다.

Drive parent: 1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM
Dropbox parent: /BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928

새 결과만 create-only checkpoint로 양쪽에 백업하고 실제 provider ACK/object ID/size/checksum을 detached receipt에 보존한다. 기본 selective readback R1/R2로 종료하며 실제 다운로드 없이는 RESTORE_VERIFIED라고 쓰지 않는다. 검증된 이전 core archive를 매번 재다운로드하거나 덮지 않는다. 정상 receipt가 닫히면 이 노드를 종료하고 새 과학 단계는 별도 승인을 기다린다.
