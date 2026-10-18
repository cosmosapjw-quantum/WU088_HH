# WU088_HH PHYS64 실행 인계

추가 사용자 파일 다운로드, 키 전달 또는 수동 명령을 요구하지 말고 기존 승인된 환경에서 실행하라. Repository cosmosapjw-quantum/WU088_HH의 branch research/hh-phys64-c5c8-order-resolved-ncp-20261018을 fetch하라. 기준 parent는 R5 PR111 commit0218ef1de8d36d0562b09b075aad0ad6f3055970이고 그 parent는 PHYS63 PR110 653db0dfaa57f04d7c0a93017c60a5902bdb319e다. 기존 dirty checkout은 reset/clean하지 말고 격리 worktree를 사용하라. README_KO.md와 NEXT_DAG.json을 먼저 읽고 실제 HEAD/source hashes를 기록하라.

이번 단계의 solver, tests, producer, parallel/resume/archive 실행 코드는 모두 native Git 파일로 작성되어 있다. 새 solver 설계나 Rust 이식을 시작하지 말라. Python3.11+와 requirements-tested.txt의 기존 의존성으로 실행한다. Python 의존성이 없을 때만 독립 venv를 만들고 명시된 패키지를 설치하되 원래 repo 환경을 덮어쓰지 말라.

호스트 hostname/nproc/free -h를 검사하라. s1a0e5abed09,64CPU,약125GiB가 승인된 NCP에 해당하면 SSH를 거치지 않고 직접 실행하라. 로컬 Ubuntu라면 기존 승인된 연결 `ssh -i /home/cosmosapjw/.ssh/ncp_key -o IdentitiesOnly=yes root@49.50.142.2 -p 22`를 사용한다. 키 내용을 복사/출력하거나 known-host 검증을 끄지 말라. 권한이 없으면 NCP 실행만 BLOCKED로 남기고 원본과 현재 가능한 검산 결과를 보존하라.

원본 NPZ SHA256은 f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d다. 다음을 순서대로 실행하고 각 exit/log를 보존하라.

```bash
python3 scripts/phys64_ncp.py --preflight-only --out research/hh_phys64_20261018/ncp_run
python3 scripts/phys64_ncp.py --profile smoke --workers 2 --resume --out research/hh_phys64_20261018/ncp_run
python3 scripts/phys64_ncp.py --profile extended --workers 4 --memory-gib 4 --timeout 180 --resume --out research/hh_phys64_20261018/ncp_run
```

smoke가 실패하면 extended를 시작하지 말라. 모든 case의 profile/code/runtime/input SHA를 결박하고 hash가 맞는 성공 case만 재사용하라. 실행기는 최초 실패를 attempt 폴더에 보존하고, CPU BLAS1thread/nice+10/개별timeout/VM ceiling을 적용한다. 다른 REI/BASS 작업을 종료하지 않는다. 예상 결과를 PASS로 쓰지 말라.

D1,D2,D3를 분리된 배열로 검토하라. D2를 total-D1으로 재계산하지 말라. L/T/GL/rtol 변화는 별도 오차축으로 비교하고 self-difference를 엄밀한 오차 상계로 오인하지 말라. low ell0/1의 continuum Catalan bound를 P20-Q21 또는 전체 물리적 외부영역에 적용하지 말라. 실제 E=49/200 Hartree와 off-centre screening, eta=Fy,xi=Fy-phi를 유지한다.

실행 종료 시 결과 JSON/NPZ/원시 stdout stderr/실제 wall RSS/복구 여부를 additive branch와 Draft PR에 게시하라. 전체 Git bundle과 SOURCE_RESULTS.zip(실행기 자동 생성)을 기존 Dropbox와 Google Drive에 각각 업로드하고 독립 재다운로드/SHA256/manifest/git-bundle-verify를 수행하라. 업로드만 성공한 것과 복원 성공을 구분한다. 별도 계정 생성이나 인증정보 변경 없이 사용 가능한 기존 GitHub/클라우드 connector를 활용한다. 권한 blocker가 있으면 구체적 원인과 현재 archive 위치만 보고하며 사용자 수동 작업을 요구하지 않는다.

최종 한국어 보고에는 실제 실행 호스트, commit/tree, 성공/실패 case 수, D1/D2/D3 비교, 제한된 검증 범위, PR 및 두 provider 복원 상태를 제시하라. HH_R10=OFF, 전체 original driven xi/regular-origin/incoming-adjoint/sigma(E)/k_HH(T)는 HOLD다.
