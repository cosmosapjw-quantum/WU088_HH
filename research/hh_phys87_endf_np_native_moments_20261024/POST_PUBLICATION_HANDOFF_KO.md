# PHYS87 게시 후 판정과 복원 인계

## 서로 다른 실제 identity

| 역할 | 실제 값 |
|---|---|
| Parent FINAL | f4a6d5505c845a046e3b81d33a2992a239ab4c8b |
| S0 계약·이론 | b4e606c433bc0d7969227635b62f33e67a56c705 |
| S1 코드 | 94d3b35bb66df184cf370035f498effbb4534cc6 |
| S2 과학 | cf48be1b8838a3839fa3c605512c1a5bb4faa8e3 |
| 중앙 WU 관측 | 85f9ba1350c076e8df01f5858342df74c3574215 |
| FINAL containing HEAD/tree | 실제 PR144 최종 본문과 외부 final-delivery JSON |
| Scientific input/code identity | bc8a07546cab87dc79de5efee1e0d1917f7e88e851cdd8d5e7856f50f8c1c53d |

현재 문서의 생성은 FINAL publication/whole restore보다 앞선다. 원격 최종 HEAD, archive SHA와 양쪽 GET/restore는 실제 작업 뒤 외부 `PHYS87_FINAL_DELIVERY_20261024.json` 및 terminal receipt에 결속한다. 이 파일에 아직 존재하지 않는 자기 commit 또는 미래 upload ACK를 기입하지 않는다.

## Stage와 FINAL의 차이

S0와 S1은 각각 `delivery/S0_BACKUP_ACK.json`, `delivery/S1_BACKUP_ACK.json`의 actual dual ACK+metadata다. S2는 `delivery/S2_BACKUP_ACK.json`의 RECOVERY1을 채택했다. S2 첫 archive는 생성 영수증의 full bytes와 이후 실제 short bytes가 달라 preupload에서 거부됐다. 업로드0, 원인UNRESOLVED, source/result/science 불변이다. 실패 파일·영수증과 새 complete-close/CRC/atomic placement/whole-byte 관측을 보존한다.

| 채택 S2 객체 | 실제 값 |
|---|---|
| 파일 | PHYS87_S2_RECOVERY1_20261024_cf48be1b8838.zip |
| Bytes | 18545712 |
| SHA256 | 719da3433b912d554110998ee0f1d591214bf733a64dec4a4354e53b9e0db7e4 |
| Dropbox | id:BSpOijBcT10AAAAAAD_9dQ |
| Drive | 1-hVBvZY3q4VZNvRjgbzQXTJ7ge3ax6hx |
| 범위 | actual dual upload ACK+exact-ID size/folder metadata; remote stage whole GET NOT_RUN |

FINAL 양쪽 복원은 각 파일의 전체 다운로드가 종료된 뒤 size/SHA, 모든 ZIP CRC, manifest payload SHA, 원격 exact-tree blob IDs와 복원된 원본 bytes의 Git hash, 실제 디렉터리 추출 및 재해시로 판정한다. Parent whole archive는 PHYS86에서 완료한 원본/복원 evidence를 재사용하며 그 안의 모든 nested archives를 새로 전수 추출했다고 주장하지 않는다.

## 상태 해석

R1–R9/C1–C9 과학·구현 의무18개는 S2에서 COMPLETE_SCOPED다. R10/C10의 최종 게시·외부 원문 readback·전달이 실제 완료되면 external terminal receipt/PR body가20/20 한정 workflow completion을 기록한다. 이20은 과학 실행 수나 전 프로젝트 물리 완료율이 아니다. Theory-loop R10과 원래 물리 gate HH_R10도 다르다. HH_R10은 계속OFF다.

새 complete child는 ENDF_H1_NATIVE_FINITE_WINDOW_JOINT_MOMENTS, 부모 NUCLEAR_PHYSICAL_FINITE_T_EVENT_SUPPLIER는PARTIAL이다. Next atomic-to-bare capture remap은OPEN, full support/covariance/consumer는OPEN, actual rate/stopping activation은NOT_ISSUED다. 계약 밖 신뢰구간·tail·coupled-history·continuum certificate를 이 결과로 만들지 않는다.

완료 raw/source/code identity와 과거 실패/unknown 비용을 보존한다. 추가 과학 allowance는0이며 runtime 버전 차이는 replay 사유가 아니다. 다음 node 전에 최신 AGENTS·actual HEAD·다른 담당자의 변경·백업·누적 예산을 확인하고 원전/이론 계약부터 진행한다.

