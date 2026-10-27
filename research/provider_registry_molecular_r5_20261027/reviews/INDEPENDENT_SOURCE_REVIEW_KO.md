# R5 독립 primary-source 조사 기록

작업자: /root/r5_primary_sources. 원 조사 종료 관측: 2026-10-27 09:41:35 UTC.
보존 날짜: 2026-10-27. 이 문서 작성 중 새 검색/계산/재감사는 하지 않았다.

## 실제 확보한 자료와 재사용 상태

LAMDA 원 데이터 링크:
https://home.strw.leidenuniv.nl/~moldata/datafiles/hd.dat
공식 설명:
https://home.strw.leidenuniv.nl/~moldata/HD.html
공식 포맷:
https://home.strw.leidenuniv.nl/~moldata/molformat.html

Exa의 clean text와 web 도구의 65행 text/plain representation에서 실제로 다음을 읽었다.
- HD native level ID1..9, J0..8, g=1,3,...,17.
- 에너지 cm^-1: 0.000000000,89.227931611,267.069663831,532.310801589,
  883.163758456,1317.309260961,1831.950752927,2423.883499771,3089.576092837.
- Collider ID2 para-H2, ID3 ortho-H2.
- 각 collider의 9개 하향 전이와 native temperatures 50,100,200 K, 총54개 rate cells(cm^3/s).
- 8개 radiative A 값과 line frequencies.
- Native transitions upper/lower level IDs:
  (2,1),(3,1),(3,2),(4,3),(5,4),(6,5),(7,6),(8,7),(9,8).

설명 페이지의 파일 버전은 7 June 2021.
분광 출처 CDMS version2 December2011, 충돌 출처 Flower1999 Table2와 J2->0의 Table1이다.
공식 data format은 collider ID와 단위를 직접 명시한다.

이 작업자는 실제로 현재 자료를 다시 취득했다. Root는 이후 REC139에 LAMDA54/24LTE 근거가
이미 완료되어 있다고 알려 주었다. 따라서 전체 프로젝트 수준의 새로운 수치발견으로 중복계수하지 않고
source 재확인·재사용 근거로 취급한다.

HTTP 원본 바이트는 취득하지 않았다. Exa/web retrieval representation의 해시와
원본 HTTP file SHA256를 구분해야 한다.
주어진 9개 edge의 연산자만 정의하며 누락 전이를 물리적 0으로 확정하지 않는다.
Collider 밀도와 ortho/para 비율은 별도 입력이다.
공식 HD prose에는 "v=1 level (~3100 cm^-1)" 표현이 있으나 파일은 J만 표기한다.
이 불일치를 그대로 기록하고 파일에 없는 vibrational/isotope qualification을 추가하지 않는다.
같은 HD 파일의 상대 상태에너지는 분자 간 chemical Q나 공통 chemical zero가 아니다.

## EMAA 신규 정확한 dataset identity

https://doi.org/10.17178/emaa_hd_rovibration_805a7aa5
https://api.datacite.org/dois/10.17178/emaa_hd_rovibration_805a7aa5
https://doi.osug.fr/r/EMAA_HD_Rovibration_805a7aa5

실제 metadata:
52 energy levels,368 radiative transitions;
H1326 collision transitions,15T5..5000K;
H+171 collision transitions,25T5..3005K;
collected2023-07-03, metadataupdated2025-01-27T15:59:51Z;
format Radex, CC-BY4.0, contentUrl:null.
공식 DOI 및 DataCite와 OSUG 페이지를 읽었지만 numeric payload는 취득하지 않았다.
변경된 machine-readable 경로:
https://api.datacite.org/dois/10.17178/emaa_hd_rovibration_805a7aa5/media
실제 응답 data:[].
이는 endpoint 응답이며 원 데이터 부재를 뜻하지 않는다.
이 dataset은 GL2022 reaction2 HD->HD excitation이며 destruction의 대체물이 아니다.

## 문헌과 spin convention

SciSpace에 완전한 자연어 연구 질문을 보내10편을 받았다.
관련 primary identities:
GL2022 DOI10.1063/5.0128598;
Desrousseaux,Konings,Loreau,Lique2021 DOI10.1039/D1CP02564C.

공식 RSC landing:
https://pubs.rsc.org/en/content/articlelanding/2021/cp/d1cp02564c
공식 author manuscript 실제 full text 취득:
https://hal.science/hal-03323406v2/document

Desrousseaux2021 Eq10의 para/ortho factors는 distinguishable-particle convention에서 1/2,3/2다.
본문은 Lepers 계열과 약2배 normalization 차이도 설명한다.
GL2022의1/4,3/4를 서로 다른 source convention에 자동 적용하면 안 된다.
본 조사에서 GL2022 또는 Desrousseaux의 완전한 reactive numeric array를 취득하지 않았다.
기존 실패 supplement URL은 이 작업에서 새로 반복하지 않았으며 과거 접근오류를 이번 관측으로 가장하지 않는다.

## 실제 도구 행동

SciSpace search1회, 반환10편.
질문:
Where can the original state-to-state rate coefficient data for H+ + HD(v=0,j) -> D+ + H2(v'=0,j')
from Gonzalez-Lezana,Hily-Blant and Faure(2022), DOI10.1063/5.0128598, be obtained,
and what primary studies provide related HD destruction data and their nuclear-spin statistical conventions?

Exa search3회, numResults 각각8,6,6, 요청결과 총20:
1. GL2022 original supplementary numerical data와 공식author/institutional deposit.
2. EMAA HD rovibration Radex file, exactdataset805a7aa5 및 official API.
3. Desrousseaux2021 d1cp02564c supplementary state-to-state data.

Exa fetch3회:
1. EMAA DOI, RSC landing, DataCite record (3 URLs).
2. LAMDA hd.dat, HD.html, HAL03323406v2/document, OSUG DOI record (4 URLs).
3. DataCite exactDOI/media (1 URL).

Web open/click3회:
1. OSUG DOI HTTP, EMAA HD landing, RSC articlehtml.
   EMAA landing 성공; OSUG/RSC는 tool inaccessible.
2. LAMDA hd.dat,HD.html,LAMDA home,DataCite record.
   LAMDA3pages 성공; DataCite webtool inaccessible (Exa에서는성공).
3. LAMDA format 및 공식페이지에서 연결한 ADS Schöier2005/Flower1999.
   Format 성공; ADS2개는405 MethodNotAllowed.

Wolfram0회, source rate numerical evaluation0회, 원 raw archive 취득0회.
그 뒤 수행한 독립 mathematical prototype56checks는 별도verification evidence다.
본 보존작업에서 scientific execution/search/CAS를 추가하지 않았다.
