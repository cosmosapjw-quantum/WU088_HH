# PHYS90 FINAL 게시 후 인계 규칙

이 파일은 S2 과학 결과 이후의 전달 전용 FINAL commit에 속한다. 과학 코드는 S1에서 동결되었고, 독립 최종 검토와 결과는 S2에서 완료되었다. FINAL은 S2의 descendant이며 이미 완료한 계산을 다시 실행하지 않는다.

## 실제 identity의 결속

- S2: `60d062104438b3f99553a74d210e9c2b48ed2dd3`, tree `d30e3cf68cc80d4559304657364f1b2dce4eb62e`.
- Scientific identity: `a7107870ad5a66e3bb602115f1068ca7366444b42c539e1a6b4b83da2037513a`.
- S2 백업의 실제 ACK와 별도 metadata는 `delivery/S2_RECEIPT.json`에 있다. S0/S1/S2 stage whole GET는 각각 0이다.
- 이 파일을 포함하는 FINAL SHA는 자기 참조로 기록할 수 없다. 외부 `PHYS90_FINAL_DELIVERY_20261025.json`, `PHYS90_FINAL_DELIVERY_TERMINAL_20261025.json` 및 PR147 최종 actual 본문에서 정확한 FINAL HEAD/tree와 provider ID를 읽는다.

## 최종 검증의 구별

FINAL ZIP은 Dropbox와 Drive에서 각각 실제 whole GET하여 원본 bytes/SHA256, 모든 member CRC, manifest payload SHA, authoritative remote Git tree identity, frozen7과 reused inputs2, 실제 추출을 검증한다. Remote Git raw key GET는 공유된 선택 파일이며 전체 Git member 수만큼의 개별 GET를 뜻하지 않는다. PHYS89 whole archive는 원본 bytes 하나로 포함하며 nested restore는 0이다.

MAIN과 TERMINAL도 양쪽에서 각각 실제 원문 GET하여 크기·SHA·parsed identity를 확인한다. Git 안의 보고서와 MAIN의 18/20은 작성 시점의 불변 snapshot이다. 후속 TERMINAL, 중앙 actual 게시와 PR147 actual readback이 이 유한 자식의 R1–R10/C1–C10 20/20을 결속한다. 전체 물리 목표 완료율은 null이다.

중앙 게시 직전 actual HEAD/AGENTS/병렬 delta를 다시 읽고 expected SHA와 force=false로 가산 게시한다. 원 40 contracts/planstatus/dependencies, 7 authorities, 17 integration edges, 다른 39 nodes와 모든 기존 WU 관측키를 보존한다. HH handoff는 기존 25,081 bytes와 고정 최초 11,893 bytes prefix를 보존한다.

## 과학적 범위와 다음 의무

이번 finite child는 `COVARIANCE_FORMATTING_CELL_AND_MATCHED_CONSUMER_ENVELOPE`이며 admission은 `PASS_SCOPED_CONDITIONAL_COVARIANCE_CELL_AND_CONSUMER_ENVELOPE`다. t=1의 모든 2×2 조건이 성립하더라도 전체 153×153 PSD compatibility는 UNRESOLVED이다. 조건부 표시 반올림 셀은 실제 physical confidence interval이나 원자료의 formatter guarantee가 아니다.

다음 단일 부모는 `NUCLEAR_BARE_KERNEL_SOURCE_AND_CONSUMER_CONTRACT`, 상태는 `PARTIAL_INPUT_DEPENDENCIES`다. Current MT102 nominal에 결속된 원 precision covariance·formatter/approved correction, actual atomic→bare kernel 및 exact mass/electron-target state, full-support tail B0/BA, named thermal/fast/radiation consumer의 measure·clock·reference-density·ownership ACK를 먼저 확보한다. REI beta 계약을 capture ACK로, BASS manufactured cohort를 nuclear consumer로 승격하지 않는다.

완료 PHYS78–90 identity와 PHYS82 CRLF ancestry를 재사용한다. HH_R10=OFF, production admission=NOT_ISSUED, ODE=0, benchmark=0, nuclear activation=0, fast stopping=0. 모든 소진 허용량 remaining=0, budget reset=false. 새로운 의무를 별도 계약으로 동결하기 전 추가 과학 계산을 실행하지 않는다. 기타 실제 비용과 모든 실패는 EXECUTION_LEDGER 및 원 receipts를 유지한다.
