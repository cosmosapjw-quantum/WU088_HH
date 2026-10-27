# WU088_HH R7 연구 보고서 — 비선형 반응 피드백과 공유 저장고 오차

작성 기준: 2026-10-27 23:27:52 KST. 연구 브랜치 `research/provider-registry-20261025`, draft PR150.

## 1. 이번 연구에서 완성한 것

R6에서 미해결로 남긴 상태 의존 형성률과 fine/coarse source 차이의 오차 제어를 실제 질량작용 반응식에 연결했다. 일반 유한 상태계의 투영 항등식, 인과적인 블록 끝점 오차 재귀, HD 공유 저장고의 scalar 오차식, 방향을 보장하는 유리수 구현을 작성했다. 독립 일반 정리 심사, primary144/144, 독립 reference376/376 및 C9 심사를 거쳐 조건부 이론·구현 노드를 채택했다.

연구 DAG는 **15/30**이다. R6의13/28에서 실제 새 이론·구현 의무2개를 등록하여13/30으로 시작했고, 이론 채택 시14/30, 코드 채택 시15/30이 되었다. 상속한28개 노드 객체는 바뀌지 않았다. R1–R10 및 C1–C10은 작업 절차20단계이며 연구 DAG30개와 다른 집합이다. 정확한 단계 상태는 `WORKFLOW_RECORD.json`에, 게시·백업 상태는 `delivery/PUBLICATION_INDEX.json`에 있다.

새 physical IVP, 새 GL2022 native reactive 행, 물리 소비자 승인은 각각0이다. `HH_R10=OFF`, `production=NOT_ISSUED`, `L4_ready=false`, 중앙·물리 완료 증가량0을 유지한다. 완성된 것은 명시한 조건을 검증할 수 있는 이론과 오차 상계 API이다.

## 2. 최신 저장소·브랜치·백업·첨부 조사와 종합

이번 조사는 접근 가능한 **51개 저장소, 2,357개 branch refs**를 페이지 끝까지 열거했다. 공개35개/1,874 refs와 비공개16개/483 refs를 합한 수치다. 공개 branch 비교에서 새3개, 변경5개, 삭제0개를 확인했다. 모든 저장소의 모든 파일·모든 과거 commit을 읽었다는 뜻은 아니다. 관련 PR 본문38개와 실제 scoped 원문15개를 추가로 읽고, 공개 가능한 원문은 Git blob identity에 결속했다. 비공개 저장소의 이름과 내부 SHA는 게시하지 않았다.

추가로 새로운 백업6개에서 선택 member25개를 읽고, 첨부20개의 현재 SHA를 기록했다. 첨부 문헌 ZIP의 PDF15개에서 텍스트를 추출하여 조사했으며 OCR은 수행하지 않았다. Dropbox dossiers3,438개 직계 항목은6페이지 전체를 열거했고, Drive dossiers는 최신1,000개까지여서 역사 전체 목록은 partial이다. 이미 검증한 R4/R5/R6 ZIP을 다시 다운로드하거나 과학 실행을 반복하지 않았다. 자료 intake 최종 기준은2026-10-27 22:18:05 KST이며, Git branch snapshot과 뒤이어 확인한 immutable PR/source pin의 시점은 각각 원 장부에 남겼다.

다른 대화 스레드 전문을 직접 읽는 기능은 사용할 수 없었다. 해당 대화의 repo에 게시된 handoff·report·백업과 현재 첨부 자료를 읽었다. 따라서 다른 모든 대화 전문까지 전수 열람했다고 주장하지 않는다. 첨부의 이전 전체-file SHA가 없는 항목은 이름·크기가 일치한다는 사실을 byte-identical 판단으로 바꾸지 않았다.

| 새 근거 | 실제 확인한 결과 | WU 연구에 반영한 결정 |
|---|---|---|
| HE PHOTON05 | photon+정지 bare-alpha→두 ground bare-deuteron 조건부 사건 사상. EXFORM0475002의12개 좌표,24/24 검증. 기존 plotting CPU4.40726504s는4s 한도 FAIL | 사건·상태·각도·source 정합의 근거로 재사용. 실제 flux/정규화/소비자 입력과 중앙 승인을 별도 상태로 유지 |
| HE ANGULAR06 S03 |26/26 PASS, CPU0.273874185s. 새 plot5.791514953s/6s PASS, local5/8 | 새 plot 통과가 PHOTON05의 원래 실패를 지우지 않는다. caller 각분포와 실제 물리 정규화는 여전히 필요 |
| BASS Phase A PR205 |67/67와 독립 PASS. endpoint 연산자2개, diffusion inverse4개, fixed-TR Maxwellian channel moments | endpoint 결과를 보존한다. finite-time dynamics Phase B 실행 완료로 확대하지 않는다 |
| CR R8 및 C03 |100K H1/He4 조건부 low-birth causal RR 계약. C03 코드는 작성됐지만 새 PREPARED/ARRAYS native 산출물은 아직 없음 | 새 조건부 baryon/electron 수치를 과거 PHYS02의 원 source 사실로 소급하지 않는다. HD native packet으로 전용하지 않는다 |
| REI R7 PR240 |finite-cohort Stieltjes/common cumulative-chain sharp-bound 이론, 신규20+기존16 검증 미실행 및 HOLD_RESOURCE | 공유 history를 연결한 이론적 진전을 기록하되 실행 통과나 새 WU source로 계산하지 않는다 |
| BASS DV2D |저장된11 pytest와828 basis rows, instantaneous class-B generator/angular measure | 유한시간 IVP 또는 새 HD 소비자 승인과 구분한다 |

SciSpace2회에서20개 metadata, Exa4회에서21개 결과/15개 URL을 확인했다. CLUE 원 논문의 polynomial ODE/Jacobian exact lumping을 배경 근거로 읽었다. GL2022 DOI의 HAL `hal-04285297v1`이라는 새 경로를 확인했지만, 실제 공개 API에는 논문 PDF만 표시됐고 PDF 접근은 차단됐다. 상태별 formation/destruction 배열은 입수하지 못했다. 이번 작업은 기존 선형/정확 lumping 개념의 최초 발명을 주장하지 않으며, 이 저장소에 열린 비선형 피드백 의무를 구성적으로 완성한다.

상세 조사: `authority/INTAKE_DECISIONS_KO.md`, `authority/REUSE_AND_DELTA.json`, `authority/inventory/`, `authority/backups/`, `theory/LITERATURE_AND_SOURCE_STATUS.json`.

## 3. 일반 비선형 블록 오차 정리

열벡터 convention으로 미세 상태를 x, 집계를 y=Px, lift를 E(t), residual을 r=x−E(t)y라고 둔다. PE=I, PK=0을 가정하고

\[
x'=K(t)x+S a(x,t),\qquad \bar y'=PSa(E(t)\bar y,t)
\]

를 비교한다. 허용한 coarse defect는 별도 source 상계로 포함한다. Q=I−EP이면

\[
r'=Kr+(KE-\dot E)y+QSa(x,t)
\]

라는 정확한 항등식이 성립한다. K의 propagator는 kerP에서 블록 내부 비확대이고 길이 H의 전체 블록에서 norm≤rho라고 가정한다. 이 인증서는 실제 사용한 K, norm, H, clock에 결속되어야 한다.

잔차 norm R과 coarse 오차 E_c를 다음 비교계로 감싼다.

\[
B=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
a,b,c\ge0,\quad d\in\mathbb R,\qquad g\ge0.
\]

블록 내부의 시각 u에는

\[
\binom{R(u)}{E_c(u)}\le
e^{Bu}w_0+\int_0^u e^{Bs}g\,ds.
\]

끝점은 명목 혼합의 수축을 추가해

\[
\boxed{w_{n+1}\le T w_n+q},\qquad
T=e^{BH}-(1-\rho)e_1e_1^T,\quad
q=\int_0^H e^{Bs}g\,ds.
\]

a≥0와 비음수 교차항에서 exp(BH)의 첫 대각성분≥1이므로 T는 비음수다. rho의 이득은 블록 시작 시 존재한 residual에 적용된다. 반응이나 외부 source가 블록 후반에 새로 만든 residual까지 동일한 rho로 줄여서는 안 된다.

그 차이는 양의2상태계에서도 드러난다. gamma=1, H=1이고 마지막 epsilon=1/4 구간에 총량 J=1의 forcing이 들어오면 실제 끝점은4(1−exp(−1/4))≈0.884796868이다. forcing 전체에 rho=exp(−1)를 곱하면0.367879441만 허용하여 실제 값보다 작아진다. 이 반례는 특정 잘못된 갱신식을 배제하는 것이며 물리적 과정의 불가능성 주장은 아니다.

d<0이면 coarse 오차 상계가 내부에서 감소할 수도 있다. 따라서 블록 끝점의 값이 그 블록 전체 supremum이라고 가정하지 않는다. 점별 query는 원래 B를 쓰고, 시간 전체를 덮는 상계에는 d를 max(d,0)으로 바꾼 비음수 행렬 Bplus를 사용한다.

## 4. HD 공유 저장고에 대한 구체식

u=H2, v=D+, w=H+, x_j=HD_j로 두고, 상태별 사건을

\[
u+v\rightleftarrows w+x_j,\qquad
a_j^+=k_f\alpha_j u v,\quad a_j^-=d_jw x_j
\]

로 쓴다. 양의 질량작용률과 정확한 정수 사건 열은 비음수 경계를 보존한다. 집계 X=sum_j x_j에서 H원자핵, D원자핵, 전하의 보존량은 각각2u+w+X, v+X, v+w이다. Fine와 coarse가 같은 보존량류에서 시작하면

\[
y-\bar y=(-1,-1,1,1)\eta,\qquad
\eta=X-\bar X,\quad E_c=|\eta|,\quad
\|y-\bar y\|_1=4E_c.
\]

같은 상태 집합과 공통 pool에 결속된 pi와 d를 쓰면 dbar=dᵀpi에 대해

\[
\eta'=-\left[\frac{k_f}{2}(u+v+\bar u+\bar v)
+\frac{\bar d}{2}(w+X+\bar w+\bar X)\right]\eta
-w d^Tr+\delta_c
\]

이다. 여기서 delta_c는 명시한 coarse source 차이이며, 상계에 g_e로 포함한다. 저장고 오차를 일반적인 양의 Lipschitz 성장항으로만 바꾸면 이 음의 감쇠를 잃는다. 이번 정리는 해당 보존량 구조를 이용해 감쇠를 유지한다.

실제 coefficient API는 whole-block density/rate/lift 상자와 q_star≥||Kpi−pi_dot||, theta_star≥||alpha−pi||, source defect 상계를 받아 a,b,c,d,g를 바깥 방향으로 구성한다. 반응 소멸/reset의 residual 항은 aR 안에 이미 포함하므로 여기서 쓰는 rho는 명목 K의 인증서이다. K 자체가 저장고에 의존하는 경우에는 별도의 feedback 항 또는 전체 family 인증서가 필요하다.

이 식을 native formation p-H2 ground ensemble과 GL2022 thermal/spin-summed destruction 자료에 적용하려면 실제 pool/state/spin 대응이 먼저 필요하다. 둘을 자동으로 동일 pool이나 detailed-balance 쌍이라고 선언하지 않는다. TIQM과 SQM도 하나의 source에 합산하지 않는다.

## 5. 구현, 검증, 실제 수치

`src/nonlinear_feedback.py`는 표준 라이브러리의 정확한 Fraction과 directed dyadic 정수 산술로 동작한다. 소비 종의 지수가0인 항은 먼저0으로 처리하여0 밀도에서 음의 지수·0/0을 만들지 않는다. 사건 열의 정확한 보존량, simplex, 초기 불변량 compatibility, clock/source/certificate 결속, 부적절한 float·음수·역전 상자 입력을 검사한다.

비교 지수는3×3 augmented matrix의 양의 Taylor 급수와 geometric tail로 감싼다. 꼬리는 실제 위로 반올림한 행렬의 norm을 사용하고, exp(−shift)는 양의 exp 다항식 경계의 reciprocal 방향을 바르게 적용한다. 행렬 역연산을 사용하지 않아 B가 특이해도 유효하며 B²=0은 정확한 다항식으로 처리한다. 이번 고정 입력은 degree48, dyadic256bits다. 구현의 지원 범위는 일반 species1–16, HD상태1–13, 사건64개 이하, 질량작용 총차수4 이하이며, 그 밖의 입력은 거부한다.

| 독립된 근거 | 실제 결과 | 실제 CPU |
|---|---:|---:|
| 생산 검증 |144/144 PASS, 실패0, exit0 |0.239641s |
| 별도 SciPy expm 및 DOP853 reference |376/376 PASS, 실패0, exit0 |4.632575s |
| Wolfram 새 항등식 |24/24 잔차0 반환, late-forcing 반례 확인, 실제 경고 보존 |kernel0.278886s |
| 독립 최종 C9 |조건부 코드 채택 PASS, 열린 material finding0 |새 과학 실행0 |

생산 및 reference CPU는 import와 결과 직렬화까지 포함한 OS 자식 프로세스 값이다. 각60초 계약을 충족한다. CAS에는 Power::infy, Infinity::indet, General::messages가 발생했고 원인을 확정하지 않았다. 그래서 CAS는 경고 없는 증명이 아니라 조건부 상징 계산 보조 근거이다. 실제 일반 증명, 방향 산술 검토, primary 및 독립 reference 근거를 함께 사용한다.

독립 reference는 생산 core와 R6 core를 import하지 않았다. Fine/coarse RHS를 따로 작성하고 DOP853 rtol1e−11, atol1e−13을 사용했다. HD4개 사례 각각3블록, 블록당65개 시각을 저장했으며 경계를 공유하여 사례당193개 고유 시각이다. 다음 표는 세 번째 블록 끝점의 저장된 수치다. 표시용 반올림 값이며 정확한 생산 유리수는 원 결과에 남겼다.

| 대조군 | 실제 R | R 끝점 상계 | 실제 E_c | E_c 끝점 상계 |
|---|---:|---:|---:|---:|
| 2상태 무반응 | 0.05578254 | 0.0610351562 | 0 | 0 |
| 2상태 비선형 | 0.0569720248 | 0.0678086556 | 0.000194000957 | 0.000518154657 |
| 2상태 coarse source 차이 | 0.0569720248 | 0.0678093985 | 0.000119621922 | 0.000686842273 |
| native9 K + 조건부 합성 반응 | 1.17212346e-07 | 7.02055984e-05 | 6.82571111e-10 | 1.1941991e-06 |

E_c는 scalar |eta|이고 전체 coarse L1 오차는4E_c이다. 모든 시간은 각 입력에 명시한 fixture clock이다. Native9상태 사례도 기존 excitation K/H/rho에 새 합성 반응 계수와 밀도를 결합한 조건부 대조군이다. 실제 기체의 새 physical IVP로 해석하지 않는다. 특히 native9상태 상계는 실제 저장 오차보다 상당히 크다. 유효한 전역 상계와 실제 오차의 근접한 예측은 서로 다른 성질이며, 이번 결과만으로 목표 물리 정확도를 달성했다고 결론 내리지 않는다.

Reference는 고정 tolerance를 적용한 binary64 수치 대조이다. 예를 들어 반응 없는 사례의 이론상0인 E_c에 약1e−16 차이가 생길 수 있다. 이것을 정확한 유리수 부등식 판정과 혼동하지 않는다. Native 저장 궤적의 최대 H/D/전하 drift는 약1.11e−14였으며, 일반 증명의 유효성은 유한 시각 sampling에 의존하지 않는다.

첫 실행 전에 발견한 CPU 집계 표기 문제1건은 전체 process와 run-local 값을 분리해 해결했다. 수정 전 과학 실행은 없었고 repair run도0이다. 새 primary/reference/CAS 각1회 후 잔여0/0/0, R6 및 PHYS91 잔여0/0/0, global remaining 및 전체 과거 CPU는 unknown/null이다.

## 6. 단계별 게시와 백업

| 단계 | 산출물 | DAG | 실제 commit | 게시·양쪽 원본 대조 |
|---|---|---:|---|---|
| R1/C1 | 문제·정책·실제 새 의무 고정 | 13/30 | `284717f359f1` | 확인 완료 |
| R2/C2 | 최신 원천 종합과 이론–코드 대응 | 13/30 | `34b1d470059b` | 확인 완료 |
| R3/C3 | 비교식·계수·고정 입력 | 13/30 | `e96c12ede3ae` | 확인 완료 |
| R4/C4 | 반례와 유한 실행 설계 | 13/30 | `80d3c2079419` | 확인 완료 |
| R5/C5 | 일반 증명·생산 코드 동결 | 13/30 | `b299fe34de97` | 확인 완료 |
| R6/C6 | 독립 증명 심사·primary144/144 | 13/30 | `513308f39ed3` | 확인 완료 |
| R7/C7 | reference376/376·qualified CAS | 13/30 | `f6beb6c7ea81` | 확인 완료 |
| R8/C8 | 이론 채택·정확도/비용 | 14/30 | `77f239583346` | 확인 완료 |
| R9/C9 | 독립 C9·코드 채택·과학 payload 동결 | 15/30 | `05aba8402363` | 확인 완료 |
| R10/C10 | 최종 보고서·handoff·전체 scoped source | 15/30 | 실제 게시 후 receipt에 기록 | 이 문서를 포함하는 S10 게시·백업 진행 단계 |

각 확인된 백업은 Dropbox와 Drive에 업로드한 뒤 실제 원본 ZIP을 다시 읽어 SHA256, ZIP CRC, member 길이·mode·SHA256·Git blob identity를 확인했다. 이전 snapshot의 알려진 입력을 새 결과처럼 재계산하지 않았다. Git 게시에는 expected-SHA와 force=false를 적용했고 main merge는 수행하지 않았다. Final metadata의 자체 archive hash는 그 archive 안에 스스로 기록할 수 없으므로 실제 후속 receipt와 PR 본문에 보존한다.

과학 채택 commit: `05aba84023630e17ca005df5d5b595c374fa540f`.
과학 payload: `a0da528aa0b6a8870f5e1476306fc9e8e9f4a1fcecd05a1ede6593dde611dae2`.
S10 source commit: `PENDING_ACTUAL_S10_PUBLICATION`.

## 7. 다음 이론·코딩 연구의 실행 조건

다음 우선 작업은 이 오차 상계를 실제 source/consumer에 결속하는 것이다. 필요한 것은 native 상태별 formation/destruction 자료와 원문·버전·단위, 공통 반응물 pool과 state/spin 대응, branch alpha 및 초기 fine/coarse 상태, density와 clock, 블록 전체 양의 상자, 명목 K의 같은 H/rho 인증서, 실제 소비자와 목표 오차이다. 자료가 없으면0으로 채우지 않고 INPUT_PENDING을 보존한다.

이미 완료한 R6/R7 실행, 공개 branch 전수 목록, 백업 원본 대조를 일상적인 새 스레드라는 이유만으로 반복하지 않는다. 새로운 입력이나 실제 추가 의무가 식별되면 그 차이를 먼저 고정하고, 새 유한 실행 계약의 pass/fail 다음 행동을 명시한 뒤 필요한 계산만 수행한다. 실제 collider density가 K에 피드백하는 경우가 확인되면 K(y) 변화항의 상계 또는 생성자 family의 time-change/whole-block 인증이 다음 이론 후보이다. 상세 계약은 `followup/NEXT_INPUT_CONTRACT.json`과 `followup/NEXT_RESEARCH_ACTION_KO.md`에 있다.

복사 가능한 다음 스레드 문맥은 `HANDOFF_KO.md`에 제공한다. 위 완료는 이론·구현의 명시적 범위에 대한 판단이며, 미입수 물리 입력이 불가능하다는 판정은 아니다.
