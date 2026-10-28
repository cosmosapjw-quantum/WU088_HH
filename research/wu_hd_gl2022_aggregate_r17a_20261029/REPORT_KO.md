# WU088_HH R17A: GL2022 인쇄 총반응률의 제한적 원전-맞춤 진단

**판정:** 출판된 **두 개의 열평균 반응성 총반응률**에 관한 정확한 산술·별도 수치 검산을 완료했다. H⁺+HD→D⁺+H₂의 *개별 상태별 반응률*은 확보하지 못했다. 이번 진단은 새 WU 물리 DAG 노드로 채택되지 않았으며, 실제 HD source/state/consumer 미결이다. WU 33/48, REI 중앙 28/88, 물리 증분0.

## 출처 및 병렬 연구
원전: González-Lezana·Hily-Blant·Faure, JCP157(2022)214302, DOI10.1063/5.0128598, Sec III A/Fig5, https://pubs.aip.org/aip/jcp/article/157/21/214302/2842276/A-statistical-investigation-of-the-rate-constants . 사용 데이터는 출판 본문에서 인쇄된 **205/295K 총 SQM** 및 실험 대비값이며, 실제 보충자료의 state-to-state 숫자가 아니다. 보충 ZIP https://aipp.silverchair-cdn.com/jcp/article-supplement/2842276/zip/214302_1_epaps/ 는 실제 접근 시 HTTP403, 원본 바이트 미확보. R17 R1 PR152, R16 PR150, H–Li PR151, REI PR222 결과를 재사용한다. 신규 REC 분광 PR150은 original LAMDA HD 2289-byte 진단과 35Hz 7/8 failure를 보존하지만 reactive source row는 제공하지 않는다. REI PR252–255의 통계적 EOS/UVB 방향 분석도 이 HD 충돌 자료를 제공하지 않는다. 다른 source/corridor/ODE의 물리 채택으로 전이하지 않는다.

## 직접 산술
원래 논문에 인쇄된 반응률과 실험 중심·오차폭을 모두 N=10⁻¹⁰cm³s⁻¹ 단위의 exact decimal string으로 해석했다.

| T(K) | 논문 SQM 총율 | 실험 인쇄 중심± | 차이 (SQM−중심)/N | 차이/인쇄 오차폭 |
|---:|---:|---:|---:|---:|
| 205 | 1.21 | 1.1±0.2 | 0.11 | 0.55 |
| 295 | 2.21 | 1.7±0.2 | 0.51 | 2.55 |

1N=10⁻¹⁶m³s⁻¹. 오차폭을 표준편차라고 가정하지 않았으며 `2.55`는 통계적 유의성이나 χ²가 아니다. 종 순서(H⁺,HD,D⁺,H₂)의 ν=(-1,-1,1,1)는 H1·D·전하를 각각 정확히 보존한다. 저자가 본문에 따로 표기한 전온도 적합식 α=8.57N,γ=405K와 두 인쇄값을 정확히 지나는 임의 2점 지수식 γ₂≈404.76062365914649K,α₂≈8.715145953651N을 구분한다.

## 수학적 결과
어떤 고정 온도 T에서 K(T)=Σ_a w_a(T)r_a(T), w_a≥0일 때, 최소 두 양의 가중치가 있으면 그 가중합만으로 특정 r_a를 유일하게 결정하지 못한다. (K/w_a)e_a와 (K/w_b)e_b는 같은 합을 내는 두 비음수 할당이다. 실제 source-specific w가 없는 현재는 선택한 HD(v0,j2)→H₂(v′0,j′1) 반응률의 수치 bound를 발명하지 않는다. 이는 작은 정의역의 초등 선형대수 반례이며 새로운 강한 no-go 정리로 주장하지 않는다.

## 실제 코딩·독립 기준 결과
입력 source/transcription SHA를 코드와 결속했고 정확 유리수 SI변환 및 signed residual, predeclared 100-digit Decimal fit을 생성한다. Independent Fraction(Decimal)+95-digit mpmath로 출력의 exact6/highprecision4 비교를 수행하여 전부 PASS; 최대 diff=4.318884432e−90, 수용 기준1e−85는 실행 전에 동결. Mutation test 10개 및 create-only CLI 포함 pytest19/19 PASS (1.66s). Wolfram 한 번 13/13 정확 항등식을 true로 반환. Primary user1.00/system0.07, independent reference user1.06/system0.08, renderer user3.53/system0.65초. CAS CPU UNKNOWN. ODE0회, repair0회, 과거 캠페인 반복0회.

## 실제 그림의 판정
2PNG/2SVG를 저장된 PRIMARY 결과만으로 만들고 원본 PNG 두 개를 열어 축, legend, 샘플/전온도 적합 구별, `printed ±0.2 not 1σ`를 직접 확인. 전온도 곡선을 새로 측정한 200개의 독립 관측이라고 부르지 않는다.

## 제한·감사·진행도
Native independent different-author C9 리뷰는 실행 불가/NOT_RUN이므로 새 과학 DAG 승격0. Novelty 판정은 출판 총율과 초등 대수의 재사용이다. R17 native-state-source 노드는 `PROPOSED_NOT_RUN`, 예산 `NOT_ALLOCATED`, actual HD array/consumer/densityclock `INPUT_PENDING`, `HH_R10 OFF`, production `NOT_ISSUED`, L4 false. 여기에 새 후속 단위 예산을 소급 이월하지 않는다.

R1..R10, C1..C8, C10 등 실제 구현·수학/문헌·산출물 단계의 검증 상태는 `checkpoints/S10.json`과 후기 게시·백업 증거를 따른다. C9는 별도 비저자 검토가 제공될 때까지 hold. Stage ZIP은 각각 Git/Drive/Library 실제 ACK로 관리하고 Dropbox binary ZIP 여부는 제공자 ACK에 따라 참/거짓을 기록한다.

핵심 파일: `CONTRACT.json`, `authority/PUBLISHED_TWO_POINT_TRANSCRIPTION.json`, `theory/DERIVATION_KO.md`, `src/aggregate.py`, `verification/independent_reference.py`, `verification/REFERENCE_CONTRACT.json`, `results/INDEPENDENT_ASSESSMENT.json`, `verification/WOLFRAM_RESULT.json`, `figures/*`, `SCIENTIFIC_DECISIONS.json`, `EXECUTION_LEDGER.json`, `HANDOFF_KO.md`.
