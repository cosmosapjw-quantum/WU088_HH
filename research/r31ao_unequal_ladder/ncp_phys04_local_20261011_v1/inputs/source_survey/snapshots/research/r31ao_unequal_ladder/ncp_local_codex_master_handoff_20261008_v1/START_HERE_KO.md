# NCP local Codex 원격 시작 안내 (2026-10-08 KST)

## 사용자가 전달할 최소 프롬프트

"GitHub 저장소 `cosmosapjw-quantum/WU088_HH`의 `research/r31ao-unequal-order-ladder-20260930` 브랜치를 fetch하고, `research/r31ao_unequal_ladder/ncp_local_codex_master_handoff_20261008_v1/START_HERE_KO.md` 및 같은 폴더의 `MASTER_HANDOFF_KO.md`를 읽어라. 기존 로컬 working tree, NCP one-shot registry, consumed scope는 건드리지 마라. 아래 검증된 Drive/Dropbox의 handoff ZIP을 현재 연결된 인증 수단으로 직접 회수하고 SHA-256을 검사한 뒤, 마스터 문서의 승인 범위 안에서 모든 가능한 작업을 실행하고, 미승인 과학 dispatch는 proposal만 작성하라. 다른 세 연구 스레드의 최신 HEAD도 다시 대조하고 실제 코드·시험·checkpoint·로그·이중백업·최종 반환까지 수행하라."

## Git 읽기 (기존 checkout을 자동 변경하지 말 것)

- 저장소: https://github.com/cosmosapjw-quantum/WU088_HH
- 브랜치: `research/r31ao-unequal-order-ladder-20260930`
- 전체 실행 계약: `research/r31ao_unequal_ladder/ncp_local_codex_master_handoff_20261008_v1/MASTER_HANDOFF_KO.md`
- 로컬 checkout이 있으면 우선 `git -C <REPO> status --porcelain`, `git -C <REPO> fetch origin research/r31ao-unequal-order-ladder-20260930` 후 `git -C <REPO> show FETCH_HEAD:research/r31ao_unequal_ladder/ncp_local_codex_master_handoff_20261008_v1/MASTER_HANDOFF_KO.md`로 읽는다.
- 로컬 repo가 없다면 새 디렉터리에 clone하되 과거 NCP 증거·scratch·원본 DB와 병합하지 않는다.
- master 원문 UTF-8 bytes 25668, SHA-256 `fd99de80071853e075367e03d19efd37cc414c83c9b87c79d8648942df897faf`.
- 기준 branch는 작업 중 전진할 수 있으므로 head/tree를 실제 실행 시작 시 기록한다. 오래된 SNAPSHOT_SHA로 reset/force/rebase하지 않는다.

## 모든 최초 실행 자료는 아래 봉인 ZIP 하나에 포함

- 파일명: `NCP_LOCAL_CODEX_MASTER_HANDOFF_BUNDLE_20261008_sha_2ddeeb797b84.zip`
- 크기: 1,331,729 bytes
- SHA-256: `2ddeeb797b84626d1d9c0e092764e8c16b2ead9fe55ee4287b418d471dab814d`
- Google Drive ID: `1u-r0hyMVeXd6OLxHxcqUIU2SRRYE0VVa`
- Google Drive URL: https://drive.google.com/file/d/1u-r0hyMVeXd6OLxHxcqUIU2SRRYE0VVa/view
- Google Drive parent: `1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM`
- Dropbox path: `/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/NCP_LOCAL_CODEX_MASTER_HANDOFF_BUNDLE_20261008_sha_2ddeeb797b84.zip`
- Dropbox file ID: `id:BSpOijBcT10AAAAAAD3d4w`
- 두 provider는 업로드 완료 및 객체 식별자를 반환했다. 전체 원격 재다운로드/독립 byte restore는 아직 미검증이다.

먼저 NCP의 content-addressed cache와 Dropbox/Drive 설정을 확인한다. 캐시에 동일 SHA가 있으면 재다운로드하지 않는다. 없다면 현지에서 이미 승인·설정된 rclone/클라우드 API/connector 중 작동하는 한 provider로 정확한 객체를 회수한다. rclone remote 이름을 `gdrive`나 `dropbox`라고 가정하지 않는다. 비밀번호·토큰을 명령 출력이나 Git에 남기지 않는다. Dropbox/Drive의 브라우저 미리보기 링크만으로 비인증 curl 다운로드가 된다고 가정하지 않는다. Cloud 접속 불가 시 사용자에게 먼저 ZIP 재업로드를 요구하지 말고 증거와 방법을 `BLOCKERS.json`에 기록하고 독립 작업을 진행한다.

새 전용 디렉터리에 복사 후:
```bash
sha256sum NCP_LOCAL_CODEX_MASTER_HANDOFF_BUNDLE_20261008_sha_2ddeeb797b84.zip
unzip -t NCP_LOCAL_CODEX_MASTER_HANDOFF_BUNDLE_20261008_sha_2ddeeb797b84.zip
mkdir -p extracted
cd extracted
unzip -q ../NCP_LOCAL_CODEX_MASTER_HANDOFF_BUNDLE_20261008_sha_2ddeeb797b84.zip
sha256sum -c NCP_LOCAL_CODEX_HANDOFF_SHA256SUMS_20261008.txt
```
SHA 또는 member hash가 맞지 않으면 실행 입력으로 쓰지 않는다. 검증된 `WU088_HH_ENERGY05_CORRELATED_TWO_SOURCE_TANGENT_20261008_v1.zip`은 이 ZIP 안에 있으며 별도 재업로드가 필요하지 않다. 이 ENERGY05는 총256 step의 ON06G 전체 checkpoint를 대체하지 않는다. ON06G/FD2/NCP 기존 거대 자료는 마스터 문서의 정확한 SHA·provider ID로 필요할 때만 자율 회수한다.

## 필수 과학·권한 경계

- 기존 NCP six-cell 및 FD1/FD2 consumed scope는 새 이름으로도 반복하지 않는다. 실제 승인기록과 이미 실행한 반환을 먼저 찾아 재사용한다.
- legacy 24/289, missing265 unbounded, epsilon_C/R=null, B22 OPEN_UNDETERMINED, canonical S0 HH OFF control, physical/production HOLD를 독립적인 새 증거 없이 변경하지 않는다.
- H–H 고정밀 atomic primitive 인증과 HH-LCS fastest-track은 다른 연구 경로다. REI/HE/CR 소유자의 결과·gate를 혼용하지 않는다.
- 새로운 exact scientific dispatch 권한이 없으면 원시 과학 배치를 실행하지 않고 proposal과 필요한 한 건의 승인 요청만 준비한다. 다른 비파괴적인 코드 구현·host/ABI 검증·unit 시험·사용 가능한 기록 분석은 계속한다.
- force push, 임의 branch reset, 데이터 삭제, 원본 DB overwrite, 시스템 전역 설치, fast-math/허용오차 완화, 무제한 자동 retry를 하지 않는다.

이 파일과 `MASTER_HANDOFF_KO.md`는 소스 및 실행 인계문이며 NCP에서의 실제 과학 실행 또는 장비·과금 증설 승인을 의미하지 않는다.
