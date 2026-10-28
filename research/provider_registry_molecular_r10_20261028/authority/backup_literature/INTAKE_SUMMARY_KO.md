# R10 백업·첨부·문헌 조사

현재 지정한 백업 폴더와 20개 첨부에서 R9의 실제 HD 반응 배열이나 밀도·시계가 묶인 새 물리적 consumer 입력을 추가로 확보하지 못했다. 이 결과는 조사 범위의 입력 상태이며 자료의 전 세계적 부재를 뜻하지 않는다. 새 이론 단위는 기존 자료에 대해 projected sink의 Markov generator 구조를 직접 활용하는 방향으로 진행할 수 있다.

## 백업 범위와 변화

Dropbox `/BASS_DERIVATION_DOSSIERS_20260912` 하위 전체를 9페이지로 열거했다. 5,193개 고유 경로이며 마지막 `has_more=false`를 확인했다. 그중 직접 자식은 3,475개, WU 폴더는 610개, CR 폴더는 206개다. R9 초기 조사값 3,464/599/205와 같은 직접 범위에서 각각 11/11/1개 증가했다. 5,193은 하위 폴더를 포함한 새 범위이므로 이전 3,464와 직접 차감하지 않는다.

Drive는 WU 642개, CR 188개를 반환했다. 각 폴더는 요청 상한 1,000개보다 작다. 상위 dossiers는 1,000개 상한에 도달해 역사적 ZIP 전체 목록은 부분적이다. 별도의 document 전용 3페이지 927개와 folder 27개는 마지막 page token이 없어 해당 검색 범위를 닫았다. 이 검색은 ZIP 전체 열거를 대신하지 않는다.

R9 초기 기준시각 2026-10-27 21:00:24 UTC 이후 파일 23개는 Drive/Dropbox 양쪽의 이름과 크기가 모두 같다. 구성은 R9 WU 단계·최종 11개, HE AZIMUTH09 단계·최종 11개, CR parent-event closeout 1개다. R9 최종 Dropbox 시각 22:06:16 UTC 이후 새 항목은 조사한 Dropbox 전체 하위 목록에서 0개다. R9 최종 ZIP 크기 4,519,806 bytes를 두 provider metadata에서 다시 확인했다. 이전 R9의 11개 ZIP·22개 원본 GET 해시 검증은 그 원래 근거를 재사용하며 이번 조사에서 재다운로드하지 않았다.

## 첨부 바이트 동일성

현재 첨부 20개를 실제 읽어 SHA256와 크기를 계산했다. R9 최종 commit `7a1430afb21736804286ca5284e0d8243016f2f4`에 보존된 R7 기록에서 읽은 `authority/backups/CURRENT_PROJECT_ATTACHMENTS.json`의 파일명·크기·SHA256와 모두 일치한다. 따라서 이전 60,882개 archive member metadata 조사와 15개 문헌 PDF 텍스트 조사를 재사용한다. 새 압축 해제, OCR 및 과거 과학 계산 재실행은 0회다.

## 읽은 1차 문헌과 이번 유도의 연결

1. Gaubert–Qu, arXiv1307.4649v3, DOI10.1007/s00020-014-2193-2: 실제 primary PDF 전문을 취득한 뒤 서론 식(1)–(2), 정리6.2, 예6.3의 stochastic Dobrushin coefficient를 확인했다. 행 확률행렬 convention을 열 generator convention으로 전치하면 zero-sum l1 부분공간의 정확한 contraction coefficient를 얻는다. `P=I+hA`의 작은 양의 h에서 column-overlap 공식을 전개한 `delta(P)=1-h*lambda(A)`와 시간 의존 연속시간 추정은 R10에서 직접 유도한다. 원전이 이 CT bridge 전체를 그대로 진술했다고 쓰지 않는다.
2. Michel–Siegle arXiv2403.07618v2: CTMC 절 정리4와 증명의 시작을 실제 읽었다. 초기 오차와 coarse-state-weighted defect 적분의 기존 error bound를 비교 기준으로 사용한다.
3. Hilder–van Meurs–Sharma arXiv2602.17579v1: 이번에는 abstract, introduction 및 앞부분 정의만 읽었다. 비평형 기준측도와 non-reversible coarse-graining 문맥을 제공하며 정리의 상수는 가져오지 않는다.
4. González-Lezana–Hily-Blant–Faure 2022, DOI10.1063/5.0128598: publisher indexed 본문의 실제 저자, 반응(1)/(2), II절, IIIA/B절과 supplementary/data-availability를 읽었다. 반응(1)의 reactive state-to-state 배열은 supplement에 있다고 명시하며, III B의 EMAA 링크는 반응(2)의 HD excitation을 가리킨다. 수치 배열 원본은 이번에도 취득되지 않았다. Gopakumar/Lique라는 계획용 약칭은 이 DOI의 저자명으로 교정한다.
5. DIGITAL.CSIC 10261/305186은 제목·저자·날짜만 확인한 locator다. 수치 첨부나 충분한 본문 읽기로 간주하지 않는다.

Exa 검색 3회(요청 결과 14칸), fetch 3회(5 URL), SciSpace 검색 3회(30 반환 논문 행)를 사용했다. 검색 결과를 모두 채택하지 않았고, 관계없는 결과는 폐기했다. 세 번째 Exa/SciSpace 검색은 선택된 projected-sink generator의 Dobrushin 전이를 뒷받침할 원전을 요청한 독립 검토자와 합의해 수행했다. 일반 Dobrushin 원리나 일반 no-go를 새 연구 성과로 주장하지 않는다.

## 도구 오류와 교정

Drive metadata 호출의 `url` 인자를 문서상 `fileId`로 교정하여 실제 metadata를 읽었다. Drive 상위 폴더 `top_k=5000`은 provider 최대1,000 제한으로 HTTP400을 반환했으며, 1,000개 목록과 별도 검색 범위를 정확히 기록했다. 과학 결과에 영향은 없다.

게시 대상은 이 디렉터리의 요약·입력 동일성·목록 metadata·문헌 비교뿐이다. 제3자 전문 및 장문 search snippets는 `local_only`에 두고 게시하지 않는다.
