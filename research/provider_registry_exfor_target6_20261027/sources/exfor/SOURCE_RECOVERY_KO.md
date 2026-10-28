# He4(γ,dd): 실제 EXFOR 표 회수

공식 IAEA-NDS/NRDC의 versioned EXFOR master export에서 원 target 6 정방향의 수치 자료를 회수했다. 기존 403/503 검색 인터페이스를 재시도하지 않고, `IAEA-NDS/exfor_master@939a14d7bba1ddce51975cb5e8711ce96b3b0871`의 반응 코드 검색과 개별 entry를 사용했다. 이는 실제 수치 공급자의 존재를 확인하는 추가 입력이다. 기존 유한 수 장부나 물리 rate/Q 승인을 다시 계산하지 않는다.

| 공급자 subentry | 원 자료 출처 | 원 관측량 | 행 수 |
|---|---|---|---:|
| M0011002 | Arkatov 등, UFZ 23, 918 (1978); 저자 제공 TABLE | SIG, EN 26–65 MeV, MICRO-B | 14 |
| M0475002 | Arends 등, Phys. Lett. B 62, 411 (1976), Table 1 | DA, EN 213/258/330 MeV; ANG-CM; DATA-CM NB/SR | 12 |
| M0475003 | 같은 Arends 실험, Table 2 | SIG, EN 201–359 MeV, NB | 6 |
| M0826002 | Arkatov 등, YF 16, 12 (1972), Table 1; SNP 16, 6 (1973) 번역 | SIG, EN-MIN/MAX 30–75 MeV, MICRO-B | 4 |

4개는 공급자 TABLE subentry 수다. 통계적으로 독립적인 네 실험이라는 뜻이 아니다. 특히 M0475002/003은 같은 실험의 서로 다른 관측량·EN 격자이며 공분산이 제공되지 않았다. 원 값을 평균하거나 DA로부터 SIG를 생성하지 않는다.

## 원시 자료와 의미

`raw/`의 네 entry는 전체 원 bytes이며 SHA256과 Git blob SHA1을 함께 고정한다. 각 공급자 행에는 원 numeric literal, 11열 고정폭 cell, DATA/COMMON/BIB와 parent BIB의 1-based 행 locator를 보존한다. `provenance/PROVIDER_README.md`와 `LICENSE.txt`는 같은 commit에서 얻은 공식 provenance와 CC BY 4.0 조건이다. 원 저자·논문·EXFOR accession/revision을 각 record에 남긴다. 변환한 JSON의 변경은 구조화된 전사와 해석 주석뿐이다.

SIG의 적분은 이차 입자의 각도·에너지에 관한 구분이다. M0826002의 입사 에너지 bin과 MICRO-B를 incident-energy integral ∫σdE로 읽지 않는다. 그 bin의 response/가중치는 entry에서 확인되지 않아 null이다. 원 EN과 EN-MIN/MAX는 EXFOR 관례상 lab이며, M0475002의 ANG-CM/DATA-CM은 CM이다. 정의의 정확한 공식 문서·절·PDF 쪽은 `SEMANTICS_REFERENCE.json`에 있다. 해당 문서는 web text로 읽었고 full-PDF bytes/hash를 검증했다고 주장하지 않는다.

모든 표의 ERR-S는 원 단위의 통계 오차로 보존한다. 신뢰확률·공분산·합성오차는 추가하지 않는다. M0826001의 감마 beam intensity 불확실성은 원문에 최대 5%로 제시되어 M0826002에만 parent 조건으로 연결한다. 이를 정확한 5% Gaussian 오차로 바꾸거나 통계 오차와 합산하지 않는다. 다른 entry에 없는 계통오차를 0으로 두지 않는다.

원 반응 코드는 He4와 두 D의 핵종을 명시한다. 전자·이온 전하·핵상태와 실제 소비자에 대한 결속은 별도다. 기존 event 열의 D 생성 중복도 +2와 실험 DA의 particle/event counting 관례도 별도다. 동일 D라는 이유로 원 SIG에 1/2를 곱하지 않으며, entry만으로 full-sphere/half-sphere normalization을 확정하지 않는다.

## 보조 자료와 제외

M0011003의 7행은 EP/POLAR=2인 electric quadrupole(E2) 성분으로 `AUXILIARY_ROWS.json`에 따로 남긴다. 이는 beam polarization degree 2가 아니며, 총 SIG에 합산하거나 4 primary variants/36 rows에 포함하지 않는다.

M0826003 및 M0034005/006은 provider가 CURVE 출처로 표시한 행이다. 전체 원 entry와 제외 locator만 보존하고 이번 primary 표에 넣지 않는다. 그래프 전사는 수행하지 않았다. 원자·핵종 전체 registry나 다른 photonuclear 가지를 이 검색에서 확대하지 않는다.

Rice 등의 Phys. Rev. C 61, 064612 (2000) 수치표를 읽었다고 주장하지 않는다. 이번에 회수한 것은 위의 실제 EXFOR TABLE 자료이며, 원 target 6의 수치 공급자 공백에 직접 대응한다. 원 source support 밖의 외삽, 역반응 변환, rate fold, Q 계산, state/branch/consumer 활성화는 수행하지 않는다.
