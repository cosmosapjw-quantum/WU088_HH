# REI-ACCEL01 repo별 반환 — WU088_HH

2026-10-10. PHYS03의 full-vs-twohalf birth threshold remap 차이는 N2의 실제 numerical blocker로 반영합니다. N/E conservation만으로 chronology 정확도를 인정하지 않습니다. reduced scalar history에는 spectral remap 자체가 없으므로 이번 실행이 기존 native 문제를 수리한 것은 아닙니다. 실제 common-state family/root/tube 및 PHYS04 원 연구는 별도 lane에 보존합니다.

실제 계산: mean-volume z20→4+, 최종14개 경우×16384steps. FLRW z50=7.32839548, z90=6.28138267, tau_segment=.03744182127. r_i=.1의 delta tau=-2.61122e-5. 독립판정 PROMOTE_SCOPED_REDUCED_HISTORY; full native CR/RCT/HH/thermal HOLD.

[중앙 보고서·DAG·재개파일](https://github.com/cosmosapjw-quantum/rei_bianchi/tree/7530e0239a4d30e99bfeba68d4b4ddc0b78a2c18/research/broad_history_20261010) · [REI draft PR104](https://github.com/cosmosapjw-quantum/rei_bianchi/pull/104).

본 repo의 마지막 실제 source pin: `93e04c51c682216d9cb662b77a52a5783b15c71f`. 이번 commit은 연구계획/입력 포인터만 additive로 게시합니다. 생산 연산자·gate나 기존 owner branch는 변경하지 않습니다. 다른 비공개 채팅 스레드의 실행 ACK가 아닙니다.

다음 node: N2, A_HH. 변경 없는 옛 suite를 반복하지 말고 해당 node의 실제 source/코드/출력을4시간 단위로 checkpoint하십시오. 전체 원자 연구 완료로 해석하지 마십시오.
