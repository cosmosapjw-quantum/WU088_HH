# 다음 입력 의무와 재사용 경로

이 문서는 전체 연구를 종료하는 판정이 아니라, 현재 회수·검증한 입력을 반복 계산하지 않고 다음 변경 의존성부터 이어가기 위한 기록이다. 최종 수용 범위는 `SCIENTIFIC_ADMISSION.json`, 실제 실행은 `EXECUTION_LEDGER.json`, 저장은 `delivery/`를 참조한다.

## 현재 기준

원 PNG와 원 19개 반응식은 회수되었다. 원 19개 ID/28개 명시 방향과 뒤의 18-family 조건부 모형을 구분한다. R1의 전자·분자·음이온·동위원소·약반응 원자료와 accepted finite compiler를 그대로 사용한다. 회수한 자료에서 실제로 채워진 셀과 남은 셀은 `registry/targets.json`, `registry/coverage.json`에 있다. 19개 ID가 모두 있다는 사실은 모든 물리 계수가 승인됐다는 뜻이 아니다.

## 1. He4(γ,dd)의 직접 수치 행

다음 source 의무는 `sources/he4_photon/TARGET6_DEPENDENCY.json`에 고정한 정확한 직접 측정 문헌의 수치 표 또는 실제 EXFOR entry이다. 현재 회수한 Shima의 no-candidate 관찰, 그 문헌의 ref37, 역포획 `D(D,γ)He4` 자료는 서로 다른 종류의 근거다. Shima의 관찰로 숫자 0이나 신뢰수준 없는 upper limit을 만들지 않는다. 연결된 직접 측정 문헌의 존재와 그 수치 행을 실제로 읽은 상태를 구분한다.

실제 행을 회수하면 입사 광자 에너지/폭, 각도와 적분 범위, 상태·가지, 단위, 통계·계통 불확실성, 원문/entry hash와 행 locator를 추가한다. 다른 열과 기존 source packet은 재작성하지 않는다. 현재 packet에 보존된 인증 요구/403/503은 접근 결과이며 물리적 단면적의 부재를 뜻하지 않는다.

## 2. He3와 Li7 native photonuclear 자료의 가지 연결

He3의 MF3/MT5와 MF6 deuteron yield는 실제 원자료의 인수 형태로 보존돼 있다. native file의 가지 설명, 두 격자의 interpolation 법칙과 정의역, 수율/단면적 단위를 연결한 별도 계약이 다음 입력이다. 원자료가 변하지 않은 상태에서 파일 회수나 전체 parser를 반복하지 않는다. 현재 수행한 것은 두 인자의 전사이며 곱셈·rate fold는 수행하지 않았다.

Li7의 MF3/MT5는 total photoabsorption이고 MF6는 inclusive 생성물 수율이다. 원 ID11의 배타적 `Li7(γ,t)He4`에 필요한 결합된 최종 상태의 자료를 확보하거나, source가 실제로 허용하는 조건부 사상을 별도로 유도해야 한다. inclusive yield를 바로 원 가지의 확률이나 단면적으로 대체하지 않는다.

## 3. He4 빔 평균 측정과 선택한 소비자의 대응

Shima와 Murata의 표를 각각 유지한다. beam spectrum, detector efficiency/acceptance, angular correction, 표에 표시된 평균 에너지의 가중치가 같지 않다. 소비자가 사용하는 광자 스펙트럼/시계/밀도/상태가 지정되면 해당 관측량과의 대응을 먼저 명시한다. 수치가 다른 두 실험을 임의로 평균하거나 같은 단일 에너지 값으로 만들지 않는다. source의 통계·계통 오차 및 비대칭 오차를 보존한다.

## 4. 물리 rate/Q·에너지 장부

NACRE-II의 실제 표, JENDL의 channel 값, NIST의 total-absorption 값과 과거 constant-S/1-v 조건부 계산은 별개다. 100 K/10000 K 조건부 모형을 NACRE-II native 온도 범위의 실증 결과로 승격하지 않는다. NIST total absorption을 특정 partial channel로 할당한 과거 가정도 남긴다.

각 활성 후보에는 질량 관례(중성 원자/이온/bare), 전자 결합 에너지, daughter state/branch, 연관 공분산, neutrino/escaping photon/fast product의 소유권과 하나의 named consumer가 필요하다. R1의 atomic-to-bare 이론과 PHYS91의 저장 결과를 재사용하되, PHYS91의 MT102 B1 open 의무와 나머지 source별 의무를 서로 대신하지 않는다. raw Q 필드와 threshold를 승인된 침적 Q로 치환하지 않는다.

## 5. 원자·분자·음이온의 남은 범위

R1의 21-population/39-direction historical view, 여섯 Voronov 원 fit, HeI RR fit a/b 교정, NUBASE 5,843 source-state catalogue, UMIST·HD·LiH의 실제 행은 고정된 결과로 재사용한다. 10개 과거 finite-CI admission gap과 현재 source candidate의 존재는 별개다. HD formation/destruction, LiH의 비광자 formation/destruction, source-native isotope/electronic/vibrational/rotational state 및 driver qualification은 해당 owner의 다음 입력이다. NUBASE의 전체 행을 활성 species 집합으로 읽지 않는다.

## 실행·게시 계약

새 노드 전에 최신 root AGENTS, local/remote HEAD, 병렬 owner 작업과 마지막 실제 backup ACK/byte readback을 확인한다. 본 R2의 완료된 24개 열, R1의 125개 열, 기존 249 checks, PHYS91와 REI219 완료 계산은 관련 identity가 같으면 다시 실행하지 않는다. 변경된 source가 요구하는 파서·정수 사상·검증만 분리한다.

PHYS91 primary/reference/Wolfram remaining은 모두 0이다. global historical CPU·money·remaining은 null이며 미측정을 0으로 바꾸지 않는다. 현재의 짧은 parsing/projection 검증 비용은 별도 기록이고 과거 과학 예산의 잔액을 옮기지 않는다. HH_R10은 OFF, L4_ready는 false, production은 NOT_ISSUED이다.

사용자는 필요한 자동 게시와 Dropbox/Drive 백업을 이미 승인했다. 각 새 소스 단위를 검증·독립 검토한 뒤 실제 최신 SHA를 expected SHA로 사용해 non-force 갱신하고, 정확한 source commit의 ZIP을 양쪽에 백업한 실제 ACK와 다운로드 해시를 기록한다. 고정 인계서와 과거 source ZIP의 원 bytes는 유지한다.
