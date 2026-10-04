# HH-F1C — raw cutoff의 두-root 정리와 source-specific box guard

판정: `CUTOFF_NONUNIQUENESS_THEOREM_AND_SOURCE_GUARD_VERIFIED__WAITING_ON_REI_DOMAIN`.

F1B를 계승하여 3000 K raw floor에서 HH-only backward Euler가 서로 다른 두 양의 온도 root를 가질 수 있음을 증명했다. 각 smooth branch의 det>=1과 모순되지 않는다. 큰 floor-only step의 양의 온도 root 부재도 보였다. 실제 consumer/history 실패를 관측했다는 뜻은 아니다. 새 solver나 원자 적분을 만들거나 실행하지 않았다.

## 읽을 곳

이 폴더의 THEOREM_AND_GATE_KO.md, RESULT_SUMMARY.json, BACKUP_RECEIPT.json을 먼저 읽는다. Git에는 exact source-branch helper와 전체 20개 unit tests가 있다. 전체 증명·proof script·정확한 입력과 outward witnesses·원본 RED/GREEN/최종 로그·frozen F1B sources·machine-readable gate/DAG/후속 handoff는 아래 ZIP에 있다. Git의 축약 문서와 ZIP의 상세 문서는 동일 bytes라고 주장하지 않는다. 두 Python 파일은 ZIP과 byte 동일하다.

- ZIP: WU088_HH_FAST_F1C_DELIVERY_20261005_v1.zip
- bytes: 56821; 37 entries, 36 manifest payload files
- SHA256: f9765f9d4a04f9d5fcf6599dfd7e8eea9a47bd58d0b1900184f6564f6e35490c
- Drive ID: 169TBg41D8ZTv6vywMc1nyhdtQNlRz9Kj
- Drive parent: 1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM
- Dropbox ID: id:BSpOijBcT10AAAAAADyNfA
- Dropbox path: /BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/WU088_HH_FAST_F1C_DELIVERY_20261005_v1.zip
- 양 provider 완료 ACK/ID/name/size 확인. 새 출력 RESTORE_VERIFIED=false. 원 F1B 입력은 실제 회수 후 41 payload 검증 완료.

HH source HEAD는 5731c27fd49c386bc953f98fb9ad8118f7c35e6c이다. REI 최초 aa3e98d7에서 게시 준비 중 9daef2087cbd40d67d898f8de789f9f00386affe로 전진했음을 읽었다. 새 native FLRW 모듈은 수신했지만 원 hhe_events/microstep 본문은 바뀌지 않았고, 최종 atomic review는 HH-F1의 F07 대기·HH-F2 NOT_INTEGRATED·HH optional exclusion을 유지했다. REI-F04도 별도 pending이다. 외부 tests/history는 여기서 재실행하지 않았다.

다음: 실제 REI-F07 domain/distribution/constants/단일 원자·열 owner/observable budget을 받아 HH-F1을 닫고, 소비자가 정한 실제 seam에서 HH-F2를 연결한다. full/half1/half2 각각의 인증 box 전체에 guard를 적용한다. cutoff 교차는 smooth 경로를 거절하며 branch-preserving step 또는 명시적 piecewise 처리 결정은 소비자가 소유한다. 작은 residual·에너지 보존·국소 Jacobian만으로 root를 임의 선택하지 않는다. 이 guard로 F04 remainder/root/width certificate를 대체하지 않는다.

기존 source에 새 의존성 변화가 없는 한 F1B/F1C/FLRW/원자 suite를 반복하지 않는다. legacy 24/289, 265 unbounded, epsilon_C/R=null, B22 OPEN_UNDETERMINED와 consumed FD1/FD2/pilot 범위를 보존한다. 같은 HH branch append-only/nonforce, 기존 Drive/Dropbox create-only를 유지한다. HH는 새 Bianchi/thermal/history solver나 별도 F09 campaign을 만들지 않는다.

필요할 때 이 Git 폴더에서 `python -B -m unittest discover -s tests -v`를 실행한다. 전체 proof는 ZIP에서 `python -B research/verify_cutoff_theorem.py --output /tmp/NEW_HH_F1C.json`으로 실행하며 출력은 create-only다.
