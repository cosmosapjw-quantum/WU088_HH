# WU088_HH R28: GL2022 원본 비반응적 HD 재분배와 교환·복사 첫 사건 경쟁

기준: WU R27 Draft PR #166, HEAD `0505e978b31f976015d7ed8d12c4a5dc4fe42989`, 원본 GL2022 SI PDF 273,554 B, SHA-256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`, DOI `10.1063/5.0128598`. 보존 대상은 반응성 채널 `H+ + HD(v=0,J) -> D+ + H2(v'=0,J')`와 다른 **비반응성** 채널 `H+ + HD(v,J) -> H+ + HD(v',J')`이다. 이 두 반응을 동일한 생성/소멸 화학종의 관측값으로 오인하지 않는다.

## 1. 원본에서 실제 획득한 물리 수치

GL2022 supplementary Tables **12–28**에는 정확히 `156`개의 원본 표 행 × 10개의 인쇄된 온도 노드 `15,55,105,255,505,1005,1505,2005,2505,3005 K` = **1,560 인쇄 셀**이 있다. 원본 PDF bytes를 SHA로 고정하고 서로 다른 PDF 텍스트 추출 엔진 두 개(`pdftotext -layout`, PyMuPDF)를 각각 실행하여 1,560/1,560 셀의 `(Table,v,J,T,token)` 열을 직접 비교했다. `m(nn)`은 해당 원본 표의 `m*10^(-nn) cm^3/s` 표기이고, `(nn)`은 오차막대가 아니다. 정확한 산란 단면적의 불확실성은 자료에 제공되지 않았다.

- 원문 표기상 구문 유효: **1,548셀**. 이는 원본 숫자 정합성을 뜻할 뿐 물리 정확도 인증이 아니다.
- Table 12, 초기 `HD(v0,J1)`, 1505 K: 인쇄 `1.91(11)`이 인접 1005 K `2.48(10)`, 2005 K `1.56(10)`에 비해 비단조적 십진 지수 의심. **원본 고정, 해당 조건부 결과 보류**.
- Table 15 `HD(v0,J3)->HD(v0,J3)` 대각 self-state 값 10개: 표에는 존재하지만 상태 변화율에 합산하지 않는다. 전자기 혹은 산란적 탄성분을 별도 처리하기 전까지 `SOURCE_IDENTITY_DIAGONAL_PRINTED`로 보존한다.
- Table 17 초기 `(v1,J2)`, 2005 K: 인쇄 `1.58(10` (닫는 괄호 누락). **소스 그대로 보존, 숫자로 복원하지 않는다**.
- 회전 탈여기 부분집합: `v=0`, `J=1..6`, `v'=0`, `0<=J'<J`, 10 온도에서 `sum_{J=1}^6 J * 10 = 210` 원본 rate 셀. 이 부분집합만 R28의 첫 사건 비교에 사용한다. 비반응성 데이터만으로 상향 전이, vibrational redistribution 또는 원본 페이퍼 전체 collider closure를 주장하지 않는다.

기존 R26의 700셀 생성물 rate (Tables1–10)와 R27의 REC161 Einstein A 전사 자료를 함께 묶는다. REC161은 원본 LAMDA `hd.dat` 2289 B를 본 연구에서 재취득하지 못한 *출처 기반 전사*로 유지한다. 최신 REC162의 CDMS v2 회전 준위 대조는 독립 보조 분광 근거이지 교환반응의 PES-native Q를 제공하지 않는다.

## 2. 세 가지 위험률의 구성적 유도

유한 동차 고정부피 계를 가정하자. `p=n_H+` (양성자 수밀도, cm^-3), 초기 HD(v0,J) 하나, 외부 고정 온도 `T`를 선언한다. `k^SQM_(J,J')` 는 GL2022 반응 출력의 인쇄 계산율, `w_J'=1/4 (even),3/4 (odd)` 는 저자 Eq(6–7)의 nuclear-spin effective 관례이며,

\[
K_\mathrm{ex}(J,T)=\sum_{J'=0}^9 w_{J'}k^{\mathrm{SQM}}_{J,J'}(T),\qquad
K_{\downarrow}(J,T)=\sum_{L=0}^{J-1}k^{\mathrm{HD}}_{(0,J)\to(0,L)}(T).
\]

두 합의 단위는 `cm^3 s^-1`. A는 `A_{J->J-1} [s^-1]`. 모델은 세 사건의 순간 위험률을

\[
\lambda_\mathrm{ex}=pK_\mathrm{ex},\qquad
\lambda_{\downarrow}=pK_{\downarrow},\qquad
\lambda_\gamma=A
\]

으로 정의한다. 동일한 초기 상태와 일정한 위험률에서 세 독립 Poisson clocks의 최소시간은 총 위험률 `lambda_tot`의 exponential 분포이므로

\[
P_\mathrm{ex}^{(3)}(p)=\frac{pK_\mathrm{ex}}{p(K_\mathrm{ex}+K_\downarrow)+A},\quad
P_{\downarrow}^{(3)}(p)=\frac{pK_\downarrow}{p(K_\mathrm{ex}+K_\downarrow)+A},\quad
P_\gamma^{(3)}(p)=\frac{A}{p(K_\mathrm{ex}+K_\downarrow)+A}.
\]

모든 값은 무차원이며 셋의 합은 1. R27에서 정의한 `p_0=A/K_ex`를 대입하면

\[
P_\mathrm{ex}^{(3)}(p_0)=\frac{K_\mathrm{ex}}{2K_\mathrm{ex}+K_\downarrow}<\frac12\quad(K_\downarrow>0).
\]

`p->infinity`에서 `P_ex^(3) -> K_ex/(K_ex+K_down)`. 실제 누락된 모든 다른 경쟁 채널의 위험률이 음수가 아니고 같은 전구체를 소모한다면 이 3-사건 확률은 **그 경쟁들을 포함한 실제 첫 사건의 상계**이다. 그러나 추가 음의 위험률, 비-Markov memory, 또는 다른 초기 상태 섞임에서는 해당 불등식을 주장하지 않는다. `P_ex(p)=1/2`을 만족하는 유한 양의 밀도는 `K_ex > K_down`일 때만 존재하며 `p_1/2=A/(K_ex-K_down)`이다. 3-사건 모형 이외의 광학두께, 배경 복사, upward collisions 등은 없는 조건이다.

## 3. 실제 수치 근거와 물리 해석

GL2022의 source-only SQM과 Eq6–7 spin-effective reaction-rate 정책을 **서로 혼용하지 않고** R27에 고정된 효과율을 이어받았다. 비반응성 down rates는 2022 원본 인쇄값을 그대로 사용한다. 이 서로 다른 정책을 결합한 위험률은 **명시된 모형의 제약된 물리 비교**이며 저자들이 인증한 완결된 chemical network가 아니다.

60 초기 `(J=1..6, T)`의 R27 수용 후보를 검증해 43개에서 source-positive / malformed-free / suspect-free three-clock 값을 산출했다. 보류 17행은 R27 인쇄 영 6, R27 source duplicate suspect 9, R27 outlier exponent 1, 이번 R28 Table12 outlier 1. 악성 출력이 NULL일 때 0으로 대치하지 않는다.

105 K에서 `P_exchange^(3)(p_0)`: J1 0.021650823943899..., J2 0.092926491283548..., J3 0.190240283345956..., J4 0.188732815973210..., J6 0.201102524851098.... J5는 출처 의심으로 제외. J2의 `K_down=1.143e-9 cm^3/s`, J2 `K_ex=1.30461670021225166825e-10 cm^3/s`, `A_2->1=5.159e-7 s^-1`이며 R27의 단독복사 50% density인 `p0=A/K_ex≈3954.418 cm^-3`에서 경쟁을 반영한 교환반응 첫 사건 확률은 약 9.293%다.

이 계산은 새로운 *published SQM physical-source derived* number table이지 2026년 관측 측정, 오류 막대가 붙은 소스, 열적으로 평형화된 초기 HD 배치, 비등방 우주론의 abundance 예측, 열 흡수 Q 또는 native PES threshold가 아니다.

## 4. 실제 blocker와 채택 판정

- 원본 Velilla2008 H3+ PES Fortran은 EPAPS `E-JCPSA6-129-612834` (DOI 10.1063/1.2973629)에 있다고 논문이 명시하지만 이번 실행에서 원본 바이너리와 동일 PES의 state-resolved `sigma(E)`는 **여전히 미취득**. 2022 source printed rates를 역산해 Q를 인증할 수 없다.
- GL2022 main Eq5의 `HD J0..8`과 SI thermal Table11 설명의 `HD J0..6` 충돌 및 누락된 J7/J8 data remains. Table11 full-physics identification HOLD.
- REC PR162 CDMS source is native HD term spectroscopy but HD chemical owner not accepted. CR PR128 H/He absorption is not HD molecular collision owner. Foreign repos read-only.
- 새로운 중앙 canonical DAG 수가 34/49 그대로이다. 이번 `WU_R28_GL2022_INELASTIC_ORIGINAL_AND_THREE_HAZARD`는 source-verified auxiliary dataset 1/1 **scientific result**; independent different-author R6/C9 `NOT_RUN`, native_subagent `NOT_RUN`; full owner and Q requirements not satisfied, so 35/50 upgrade is **not admitted**. Original 49 objects unchanged.
- `physical_Q=null`, `PES_native_threshold=null`, `owner_ACK=null`, `full_A=null`, `HH_R10=OFF`, `L4=false`, `production=NOT_ISSUED`.