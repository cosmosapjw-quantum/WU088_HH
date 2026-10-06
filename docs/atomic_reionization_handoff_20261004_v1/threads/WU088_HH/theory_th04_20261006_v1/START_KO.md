# HH-TH04: 공통 열적 영역과 HH 기체 차이의 전 구간 상계

판정: SOURCE_BOUND_FIRST_EXIT_DOMAIN_AND_UNIFORM_HH_GAS_DIFFERENCE_ENCLOSED.

TH03에서 null이던 B_h를 같은 exact-real FT03+LCS/S0-derived moving-cohort 모형의 원 초기값으로부터 닫았다. 0..8e11 proper seconds, |epsilon|<=.01, 고정 birth, 0<=lambda<=1에서 first-exit 공통영역과 5성분 양의 비교계를 유도하고, 6차 증강행렬의 유한 지수급수와 해석적 나머지를 구간평가했다. 이전 native endpoint/격자차이를 상계로 대입하지 않았고 새 gas IVP/native/BE root는 실행하지 않았다.

결과: sup|Delta h|<2.874e-7, sup|Delta HeII|<2.407e-10, sup|Delta HeIII|<1.150e-11, sup|Delta(w/w0)|<2.346e-7, sup sum|Delta p|<1.075e-7, sup|Delta T|<.01874 K. 공통 exact-real 해는 47241<T<50319 K 안에 있어 원35000..60000K guard를 벗어나지 않는다. 이는 LCS-ON/OFF 효과의 사전 상계이며 native 시간오차/physical fit정확도/작은 BI-FLRW 이중차이의 오차막대가 아니다.

TH03의 두 labelled cohort에 대한 조건부 terminal source 상계는 |K_Dh|<3.020e-11,2.960e-11; |K_DT|<8.155e-7,7.998e-7 K다. 실제 signed kink, 모든 동시군의 합과 parameter-prehistory 정칙성은 별도다. 새 geometry root를 풀지 않았다.

읽기: THEOREMS_KO.md, RESULT_SUMMARY.json, NEXT_HANDOFF_KO.md, BACKUP_RECEIPT.json. Git의 문서는 검색·인계용 별도 요약이며 standalone verifier가 아니다. 전체 유도, 원 source 사본2개와 identity, 선택된 TH03 inputs, proof helper, 2개 실패의 원본/traceback, 성공 로그, exact rational matrix/enclosures는 아래 ZIP에 있다.

- Archive: WU088_HH_TH04_THERMAL_GAS_ENCLOSURE_20261006_v1.zip
- bytes: 131241; entries44 / manifest payloads43
- SHA256: 971d56511dcf5f8fc4898dcbc7abb60d1723deea93a06e68242c00eea1586be4
- Drive ID: 1NA2JccTIF5I-Db_TPOzE7FhkB6xoV6VY
- Drive parent: 1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM
- Dropbox ID: id:BSpOijBcT10AAAAAADzg7A
- Dropbox path: /BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/WU088_HH_TH04_THERMAL_GAS_ENCLOSURE_20261006_v1.zip
- 양쪽 create-only 완료 ACK/name/path/size 확인, R1. 새 출력 full remote restore=false.

재현은 ZIP/HH_TH04_20261006_v1의 REPRODUCE_KO.md를 따른다. 새 출력 폴더에서 verify_gas_bound.py --output .../GAS_BOUND.json, verify_independent.py --certificate .../GAS_BOUND.json --output .../INDEPENDENT.json을 사용한다. Old TH03의 arithmetic module만 import하며 old verify/history는 실행하지 않는다.

최종 core73 + independent220 = 293 신규 checks. 별도47 metadata checks는 과학검사수에 합산하지 않는다. Rate구간은 새8Tcells에서 평가했으므로 이번 rate평가를0이라고 하지 않는다. Native/Rustcompile/gasIVP/BEroot/oldproofsuite/HHprimitive/NCP는0이다. 형식증명기/독립agent심사/TDD는 주장하지 않는다.

HHparent cf6222eac1622ae457ac02a744fd2f6183eec343, REI5673fc60e7e4db2a1c411aefae7dba4cda80d279를 게시 직전 다시 읽었고 동일했다. 최신 SPEC03의 짧은 spectral-feedback 결과는 수신만 했으며 이 HH bound로 전용하지 않았다. Canonical S0 OFFcontrol과 ACTIVE 연구, legacy24/289·265unbounded·epsilonnull·B22OPEN·consumedscopes를 유지한다. 이번에는 B_h가 없다는 입력대기로 회귀하지 않는다.
