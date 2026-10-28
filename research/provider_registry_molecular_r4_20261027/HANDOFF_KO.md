# WU088_HH molecular R4 — 실행 가능한 인계

## 현재 권위

- Repository: cosmosapjw-quantum/WU088_HH
- Branch: research/provider-registry-20261025, open draft PR150
- 회수한 S09 source: f949c21cca6e2534b725241068bd6c6e06158495
- S09 tree: 92b79d59129f9545785da0b56e39da3b1a4df261
- 이번 R10 문서의 게시 identity: delivery/R10_PUBLICATION.json이 존재하면 그 실제 영수증과 포함 commit을 사용한다.
- 과학 canonical SHA256: 34765b943cce5a67d49a622f76c0cf9aeceb635c8cd6a3cf58b5cebb8e3c5fde

먼저 최신 AGENTS.md, 이 leaf의 REPORT_KO.md, SCIENTIFIC_ADMISSION.json, DAG.json, WORKFLOW_RECORD.json, delivery/S09.json, delivery/S09_RECOVERED_READBACK.json, delivery/R10_PREPARATION_STATUS.json을 읽는다. 이전 S09의 R9/C9 pending 표시는 과거 snapshot이며 후속 회수 영수증에 실제 commit·현재 provider 객체를 결속했다.

## 완료한 것

R4의 6 supplier variants, 77 native cells, 6 정수열, 13 조건부 claims, 29 native formula 표본은 이미 독립 수용됐다. 기존 28/28 구현검증과 8/8 groups·1138 assertions를 재사용한다. S09 Drive 원본 1,092,150 bytes의 SHA256은 84e7f59613b26add26c3d8ce4ff64cc49db99782e644345065cdff7c6d9f19ac이며 CRC145/145, payload SHA144/144, Git blob144/144를 이번 재개에서 메모리 검증했다. S01–S09 양쪽 현재 객체 metadata도 확인했다. 이번에 Dropbox S09 전체 GET은 수행하지 않았다.

로컬 DAG는 9/24, 완전히 종료한 workflow는 18/20이다. R10/C10 보고서·다음 입력 계약·인계 내용은 준비됐으나 아래 S10 전달이 남아 있다. 모든 이전 수치·원자료·첫 실패·검토·예산을 보존한다.

## 지금 실행할 전달 작업

이번 호스트의 Python·C++ 호출과 파일 쓰기는 SERVICE_ERROR였고 실제 프로세스가 시작되지 않았다. **새 턴에서는 현재 runtime을 다시 probe한다.** 실패를 상속하거나 compiler/package 부재를 추정하지 않는다. 다음은 패키징 재개 명령이며 이번에 실행 성공했다고 주장하지 않는다.

현재 checkout의 무관한 작업을 보존하고 최신 연구 branch를 fetch한 뒤 별도 detached worktree를 준비한다. 최신 원격 source가 이 인계의 후손인지와 추가 병렬 결과를 확인한다. 기존 working tree를 reset/clean하거나 기존 archive를 덮어쓰지 않는다.

~~~bash
git fetch origin research/provider-registry-20261025
git worktree add --detach /tmp/wu088-r4-s10-resume FETCH_HEAD
cd /tmp/wu088-r4-s10-resume
WU_S10_SOURCE_COMMIT=$(git rev-parse HEAD)
python3 research/provider_registry_molecular_r4_20261027/delivery/package_checkpoint.py \
  --commit "$WU_S10_SOURCE_COMMIT" --stage S10 --full
~~~

예시 worktree 경로가 이미 있으면 먼저 상태를 읽고 새 경로를 선택한다. Packager는 기존 동명 ZIP을 거부한다. 이미 성공한 동일 source의 S10 ZIP이 있으면 그 receipt/bytes를 읽고 재사용한다.

--full은 AGENTS.md, R4, R1, R2, R3, program_expansion_20261025, rei_chem_ledger_20261025를 정확한 Git blob에서 묶는다. 모든 원본을 확보하지 못하면 FULL로 표시하지 않는다. 과학 module·compiler·Wolfram·plotter는 호출하지 않는다. Python 표준 library와 Git만 필요하다.

생성된 ZIP을 기존 승인된 다음 경로에 create-only 저장한다.

- Dropbox: /BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/<actual_archive_name>
- Google Drive parent: 1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM

각 actual upload 응답과 객체 ID/size를 기록한 뒤, 각 provider에서 실제 원본 전체를 읽어 SHA256·size·CRC·manifest member SHA를 비교한다. 일회성 Dropbox 링크는 HEAD/Range로 소모하지 않는다. 불완전 다운로드와 첫 실패는 보존한다. 임시 signed URL은 공개 Git metadata에 넣지 않는다.

성공하면 delivery/S10.json, delivery/FINAL_SOURCE_READBACK.json에 실제 S10 source commit/tree, archive identity, provider ACK, 검증 결과를 쓴다. 그때 R10/C10 workflow를 20/20으로 닫고 DAG9/24와 physical flags를 그대로 유지한다. Source ZIP이 자기 후속 delivery metadata를 포함한다고 주장하지 않는다. 후속 metadata는 최신 실제 expected SHA에 force=false로 게시하고 readback한다. Main merge는 수행하지 않는다.

## 다음 과학 입력과 반환

followup/NEXT_INPUT_CONTRACT_KO.md 및 .json의 GL2022 HD state block을 진행한다. 원 supplement의 k_jj'(T)/d_j, 상태 에너지, spin/support 규약, 실제 consumer x 또는 pi와 clock/density를 확보한 뒤 변경된 입력만 연산한다. 현재는 원문상 자료 존재 확인, 수치 배열 retrieval 미완료다. EMAA excitation과 destruction을 구분한다.

반환에는 actual HEAD/tree, 새 변경 파일, 재사용한 과학 identity, 실제 명령/exit/CPU와 미계측 비용, archive SHA/size/provider ACK, 두 실제 readback, 미완료 입력을 포함한다. PHYS91 primary/reference/Wolfram 잔여0, global history/remaining null, HH_R10=OFF, production=NOT_ISSUED, L4_ready=false를 유지한다.

## 다음 대화에 복사

~~~text
$physmath-research-loop로 cosmosapjw-quantum/WU088_HH 연구를 이어가라.
research/provider-registry-20261025의 최신 AGENTS와
research/provider_registry_molecular_r4_20261027/HANDOFF_KO.md,
REPORT_KO.md, SCIENTIFIC_ADMISSION.json, WORKFLOW_RECORD.json,
delivery/S09.json, S09_RECOVERED_READBACK.json, R10_PREPARATION_STATUS.json,
있으면 R10_PUBLICATION.json을 먼저 읽어라.
R4 scientific payload SHA34765b943cce5a67d49a622f76c0cf9aeceb635c8cd6a3cf58b5cebb8e3c5fde,
완료 계산과 PHYS91 잔여0을 재사용하라. 로컬 DAG9/24, workflow18/20에서
R10/C10 내용은 준비됐고 최종 S10 full source ZIP·실제 양 provider byte readback이 남았다.
현재 runtime을 직접 probe하며 과거 SERVICE_ERROR를 상속하지 마라.
기존 package_checkpoint.py --full로 과학 재실행 없이 전달을 완료하고,
actual expected SHA에 non-force 게시 및 기존 승인된 Dropbox/Drive backup을 수행하라.
그 다음 followup/NEXT_INPUT_CONTRACT.json의 GL2022 HD state-to-state 원자료와
실제 consumer 상태/clock/density를 결속하여 변경된 입력만 연구하라.
매 단계 DAG수와 실제 게시/백업 상태를 구분하고 새 copyable handoff를 반환하라.
~~~
