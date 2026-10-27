# WU088_HH R8 연구 보고서

## 1. 결과와 채택 상태

**같은 R7 입력과 저장된 궤적을 유지하면서 native 9-state 사례의 최종 오차 상계를 R에서 48.0844%, E에서 48.1532% 줄였다. 조건부 이론과 구현을 독립 심사 후 채택했으며 과학 DAG는 17/32다.** 기존 30개 노드 객체는 그대로 보존하고 두 R8 노드만 완료했다. [최종 수치 요약][finalresults] [과학 채택][admission]

Primary는 **237/237 PASS**, 최초 독립 reference는 **726/727 PASS·1 FAIL 보존**, 해당 스칼라의 exact-rational 보완은 **24/24 PASS**다. 최종 C9는 `PASS_SCOPED_CONDITIONAL_CAUSAL_LAG_KERNEL_CODE`, 미해결 실질적 지적은 **0개**다. 최초 reference의 FAIL과 비용을 유지하면서 별도의 엄밀한 상하계로 그 의무를 해결했다. [최종 독립 심사][c9] [보완 결과][scalar]

채택 source commit은 `eb437ab5ec60d3b503be115c5560a85172502aba`다. 48개 과학 파일의 payload SHA256은 `9fb1e28631426a8e891ae59ee74441e79edb0473b8c78daf51a935627cf37485`다. 이 identity는 후속 보고서·백업 영수증·최종 metadata HEAD와 구분한다. 선행 R7 최종 commit은 `c1badb7de44131715a4998d76515506da5573707`이며 당시 DAG15/30에서 R8 두 노드를 등록한15/32를 거쳐17/32가 됐다. 중앙28/88과 REI working33/88은 별도 장부다. [Payload 목록][payload] [조사 종합][survey]

이번 변화는 과거 forcing이 거친 혼합을 상계 적분 안에 보존하는 것이다. R6의 네 시간창 인증, R7의 비선형 두 성분 비교식과 저장된 전체 구간 상계를 조합했다. 새 생성자·반응률·Gibbs 인증과 새 ODE 적분은 **0회**다. 실제 HD 소비자·native reactive array·밀도/clock 결속은 아래 §8의 입력 의무로 유지한다.

**전달 상태:** S01–S10의 게시와 Drive·Dropbox 원본 바이트 검증을 모두 완료했다. 이론 R1–R10은10/10, 코딩 C1–C10은10/10이며 workflow20/20이다. 과학 DAG17/32와 이 workflow 완료 수는 별개다. 최종 metadata source에는 실제 S10 영수증을 포함하며, 그 보존본 자신의 전달 영수증은 외부 최종 영수증으로 제공한다.

## 2. 최신 조사에서 확인한 범위와 연구 방향

Git 조사의 마지막 관측은 2026-10-27 14:49:29.871 UTC다. 접근 가능한 **51개 저장소, 2,362개 branch ref, 65페이지**를 끝까지 열거했고 페이지 실패는 없었다. 공개 35개 저장소의 1,879개 ref 중 새 ref 5개·HEAD 변경 5개를 확인했다. 비공개 16개 저장소의 483개 ref는 집계만 공개했다. 동시 원자적 snapshot이나 모든 branch 내용·tag·이력의 열람은 아니다. 최신 PR 35개와 선정된 고정 source 파일을 읽어 종합했다. [조사 목록][inventory]

Dropbox dossiers 3,446행·6페이지와 WU 588행·CR 183행은 지정 범위의 끝까지 확인했다. Drive의 WU 620행·CR 165행도 확인했지만 상위 최신 1,000행은 전체 이력을 보장하지 않는다. R7 최종 archive는 기존 원본 해시 증거와 두 제공자의 metadata를 대조했다. 다른 대화 스레드 전체 조회는 **0건**, PersonalContext는 이용 불가였다. 첨부 20개의 원본 byte도 이번에는 확인할 수 없어 R7의 SHA·PDF 근거를 원래 범위로 재사용했다. 접근 불가능한 대화·첨부까지 전수 열람했다고 주장하지 않는다. [백업·대화 범위][intake]

| 최신 변경 | 실제 진전 | WU에 주는 의미 |
|---|---|---|
| REC H5 | 313개 native Wien 도함수와 whole-cell 경계, 독립 containment 10,016개 및 control 38개 | 새 광자 자료 공급자다. 실제 HD 소비자·분자 반응률 결속을 공급하지 않았다. |
| BASS B3h | Phase A 67/67, Phase B 379/379 및 선택한 effective-H 유한 거래 | 중앙 장부가 27/88에서 28/88로 한 노드 증가했다. WU의 분자 노드 완료로 옮겨 세지 않는다. |
| REI recovery·atomic storage | 과거 NOT_RUN 이후 recovery 36 PASS와 workflow 20/20 확인; 새 atomic storage는 C5 정적 통과·실행 0 | 오래된 handoff의 미실행 표시는 역사로 구분한다. 새로운 H1 계약도 HD 분자 소비 계약과는 별개다. |
| CR low-birth causal RR | primary 112/112, reference 517/517; 실패 한 건을 포함한 47회 평가 이력 보존 | 고정 H1/He4 조건의 범위 한정 성과다. 실제 HD packet과 결합 bath는 공급하지 않았다. |
| HE ANGULAR06·APERTURE07 | ANGULAR06의 source 게시 영수증 확인; APERTURE07은 32/32와 최종 심사 대기 | 과거 backup-only 표시는 전달 상태에서 해소됐다. 물리 DCS·rate·열 침적의 미결 조건은 유지한다. |
| BASS DV2E·Vigil | prescribed Bianchi V 수송 계약, causal homotopy의 native 계약 검사 진전 | WU의 HD client tube·collider 법칙·물리 clock 결속을 새로 제공하지 않았다. |

다른 owner의 전체 채택을 재심사한 결과는 아니다. REI working **33/88**, 중앙 **28/88**, WU **15/32**를 별도로 유지했다. 실제 HD 소비자·반응성 배열·collider clock은 새로 공급되지 않아 `INPUT_PENDING`으로 남기고, 관측된 R7 상계의 보수성 개선을 선택했다. [조사 종합][survey]

## 3. 이론: 지연에 따라 달라지는 수축을 강제항 적분에 보존

### 3.1 같은 family에서만 결합하는 지연 커널

잔차 공간 $Z=\ker\mathbf1^T$에서 명목 전파자 \(\Phi\)가 모든 시작 시각 \(s\)에 대해

\[
\|\Phi(s+H_j,s)z\|_1\le\rho_j\|z\|_1,\qquad z\in Z
\]

를 만족하고, 남는 부분 구간에서는 비팽창한다고 하자. R6의 네 인증은 동일한 \(\lambda\)와 \(P_{\rm lower}\)를 저장하며, 선행 증명의 ordered-product 하한은 시작 시각에 의존하지 않는다. R7 native9의 저장된 \(K\)는 그 구간 family의 정확한 midpoint다. 이번 runner는 실제 source hash, midpoint 소속, 상태 순서, clock, norm, family를 확인했다. 단지 metadata의 Boolean을 참으로 두고 결속을 대신하지 않았다. [일반 증명 §1–3][proof] [정적 심사][preflight]

Native 네 창은 \(H_j=\{8,32,128,256\}/\lambda\)다. 가장 긴 창을 \(H\), \(\delta=H/64\)로 두면 정확히

\[
m_j=H_j/\delta\in\{2,8,32,64\},\qquad T=3H=192\delta
\]

이다. \(h_0=1\)에서

\[
h_n=\min\!\left(h_{n-1},\ \min_{j:m_j\le n}\rho_jh_{n-m_j}\right)
\]

를 구성한다. 각 항은 전파자 합성과 유도 norm의 곱셈 부등식으로 얻는 독립적인 상계다. 모든 시작 시각에서 같은 인증이 유효하므로 서로 다른 길이의 창을 조합할 수 있고, 유효한 상계들의 최솟값도 상계다. 이에 따라 \(0\le h_n\le h_{n-1}\le1\)이며 \(h(u)=h_{\lfloor u/\delta\rfloor}\)가 임의 지연 \(u\)를 덮는다. 이는 순간적인 exponential gap을 추론하는 절차가 아니다. 두 상태 사례에는 기존 \(H=1/4,\rho=5/8\) 인증을 재사용한다. [증명 §3][proof]

### 3.2 비선형 feedback과 끝점·전체 cell의 차이

\(R=\|x-\pi X\|_1\), \(E=|\eta|\)로 놓는다. R7의 동일 초기 불변량 조건에서는 전체 coarse \(L^1\) 오차가 \(4E\)다. 저장된 비교 계수는

\[
\|F_r(t)\|_1\le aR+bE+g_r,\qquad
D^+E\le cR+dE+g_e,
\]

이며 \(a,b,c,g_r,g_e\ge0\), \(d\in\mathbb R\)이다. 각 사례의 세 블록은 같은 \(B=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\)와 \(g\)를 사용한다. 반응 feedback은 이 계수에 이미 포함되며, \(h\)는 명목 \(K\)의 전파에 적용한다. [증명 §2][proof]

이전 pass의 whole-cell 상계 \(U_j\)에서 \(F_j=aU_{R,j}+bU_{E,j}+g_r\), \(L_j=cU_{R,j}+g_e\)를 만든다. \(I_n=[n\delta,(n+1)\delta]\) 전체를 덮는 residual 식과 그 오른쪽 끝점 식은 각각

\[
\widehat R_n^W=h_nR_0+\delta\sum_{j<n}h_{n-j-1}F_j+\delta F_n,
\]
\[
\widehat R_{n+1}^P=h_{n+1}R_0+\delta\sum_{j\le n}h_{n-j}F_j
\]

이다. 전체 cell에서는 과거 항의 최소 지연이 \((n-j-1)\delta\)이고 끝점에서는 \((n-j)\delta\)이므로 index가 다르다. 현재 cell의 forcing은 아직 긴 혼합 창을 거치지 않았으므로 계수 \(h_0=1\)을 유지한다. 마지막 순간에 집중된 강제항에 전체 블록 \(\rho\)를 곱하면 상계가 깨진다는 R7 반례와도 일치한다. 이번에는 그 반례의 저장된 값을 재사용하고 현재 cell 계수를 새 analytic control로 확인했다. [증명 §6·11][proof]

### 3.3 음의 감쇠 계수를 유지하는 coarse 상계

\[
e=e^{d\delta},\qquad \phi=\int_0^\delta e^{du}\,du
=\begin{cases}(e^{d\delta}-1)/d,&d\ne0,\\\delta,&d=0.\end{cases}
\]

항상 \(\phi>0\)이다. \(d\le0\)이면 과거 cell과 초기항의 최댓값을 왼쪽에서, \(d>0\)이면 오른쪽에서 취한다. 따라서

\[
\widehat E_n^W=
\begin{cases}
e^nE_0+\phi\sum_{j<n}e^{n-j-1}L_j+\phi L_n,&d\le0,\\
e^{n+1}E_0+\phi\sum_{j<n}e^{n-j}L_j+\phi L_n,&d>0,
\end{cases}
\]

이고 모든 부호에서 끝점은

\[
\widehat E_{n+1}^P=e^{n+1}E_0+\phi\sum_{j\le n}e^{n-j}L_j
\]

로 주어진다. \(d=0\)에서도 식이 연결되므로 \(B^{-1}\)이 필요하지 않다. Native9의 \(d=-1/20000000\)을 0으로 바꾸지 않고 그대로 유지했다. [증명 §7][proof]

### 3.4 정확히 두 번의 개선과 상방 산술

초기 \(U_n^0\)는 R7의 `whole_block_upper`를 각 블록마다 64개 cell에 그대로 복제한 값이다. 각 pass는 이전 배열만 읽고, 새로 계산한 전체 cell 상계와 이전 상계의 성분별 최솟값을 취한다.

\[
U_n^{p+1}=\min\{U_n^p,\widehat F(U^p)_n\},\qquad p=0,1.
\]

이전 배열이 참 오차를 덮으면 양의 kernel과 비음수 forcing 계수로 계산한 새 배열도 덮는다. 두 유효한 상계의 최솟값 역시 유효하므로

\[
\text{actual}(t)\le U_n^2\le U_n^1\le U_n^0\quad(t\in I_n)
\]

가 성립한다. 수렴이나 strict contraction을 가정하지 않고 두 번에서 멈춘다. 계산에는 정확한 유리수와 \(\operatorname{up}_{128}(x)=\lceil2^{128}x\rceil/2^{128}\)를 사용한다. 양의 곱·합을 위로 반올림하되, 마지막 최솟값은 다시 반올림하지 않아 원래 exact cap을 넘지 않는다. [증명 §8–10][proof]

끝점은 별도 배열로 유지한다. 실제 저장된 R7 query의 절대 시각은 `t0 + query.t`이며, macro 끝점의 더 강한 인증값은 `certificate.w_next_upper`다. `queries[-1].bound`와 이를 혼동하지 않는다. 각 사례의 15개 query와 3개 true endpoint는 원본 JSON pointer와 exact clock으로 결속했다. 수치 reference 표본을 cap으로 쓰거나, point cap을 전체 cell에 이식하거나, 저장되지 않은 시각으로 보간하지 않았다. [정적 심사][preflight]

이 원리의 일반 배경은 Mitrophanov의 연속시간 Markov chain 섭동 경계에 이미 있다. 조사에서 출판사 원문 §2, 식 2.5–2.7을 읽었으며, 지연별 ergodicity coefficient를 forcing convolution에 사용하는 기본 원리 자체를 새 정리로 주장하지 않는다. WU의 범위 한정 기여는 저장된 네 인증을 같은 family로 결합하고, R7의 비선형 두 성분 feedback·음의 coarse 감쇠·전체 cell/끝점 구분을 고정된 상방 산술 구현으로 연결한 것이다. [Mitrophanov, 2005][mitrophanov] [문헌 조사][literature]

## 4. 네 사례의 실제 저장된 끝점 비교

아래는 모두 세 번째 블록 끝점의 값이다. 소수는 표시용 근사이고 정확한 유리수는 원시 결과에 보존돼 있다. ‘저장 수치값’은 R7의 기존 binary64 궤적 표본이며 새 연속 ODE 인증이 아니다. 감소율은 기존 R7 상계 대비 R8 상계의 감소다. [수치 요약][metrics]

| 사례·성분 | R7 상계 | R8 상계 | 저장 수치값 | 상계 감소 |
|---|---:|---:|---:|---:|
| 두 상태, 반응 없음 — R | 0.06103515625 | 0.06103515625 | 0.05578254004 | 0% |
| 두 상태, 반응 없음 — E | 0 | 0 | 0 | 해당 없음 |
| 두 상태, 비선형 — R | 0.06780865563 | 0.06780448733 | 0.05697202483 | 0.006147% |
| 두 상태, 비선형 — E | 5.181546573×10⁻⁴ | 5.165339428×10⁻⁴ | 1.940009571×10⁻⁴ | 0.312786% |
| coarse source defect — R | 0.06780939849 | 0.06780523435 | 0.05697202483 | 0.006141% |
| coarse source defect — E | 6.868422729×10⁻⁴ | 6.852219030×10⁻⁴ | 1.196219221×10⁻⁴ | 0.235916% |
| 조건부 native9 — R | 7.020559835×10⁻⁵ | 3.644764302×10⁻⁵ | 1.172123464×10⁻⁷ | **48.084421%** |
| 조건부 native9 — E | 1.194199103×10⁻⁶ | 6.191540755×10⁻⁷ | 6.825711107×10⁻¹⁰ | **48.153195%** |

Native9의 기존/새 상계 비는 R에서 약 1.9262, E에서 약 1.9288이다. 그러나 새 상계도 저장된 수치값보다 각각 약 **310.95배**, **907.09배** 크다. 따라서 보수성이 실제로 줄었다는 결론은 지지되지만 충분히 날카로운 물리 오차 인증을 달성했다고 볼 수는 없다. 반응 없는 control은 개선이 없고, 두 상태의 비선형 사례 개선도 작다. 개선을 모든 입력에 균일하게 강요하지 않는 구성과 일치한다. [수치 요약][metrics]

그림 `results/NATIVE9_BOUNDS.svg`는 R8 193개 끝점, R7의 원본 query·macro endpoint, 기존 수치 표본 193개를 표식으로 구분한다. 전체 구간을 덮는 선은 R7의 실제 whole-block 계단 상계뿐이다. $E(0)=0$은 로그축에서 제외하고 이를 명시했다. 축은 무차원 \(\tau/H\)이며 물리적 초 단위로 해석하지 않는다. 그림의 끝점·표본·전체 구간 표식을 구분하며, 최종 상태 문구를 실제 C9 판정에 맞춰 갱신했다. 원래 그림의 생성 이력과 비용은 provenance에 남긴다. [그림·후처리 근거][plot]

## 5. 검증 결과와 REF01의 정확한 의미

Primary는 네 HD 사례와 다섯 analytic control에서 **237/237 PASS**를 기록했다. 독립 reference는 생산 코어를 import하지 않고 Decimal80 직접 합산과 별도 닫힌식을 사용했다. 최초 결과는 **726/727 PASS, 1 FAIL**이며, 성분 비교로는 **22,658/22,659 PASS, 1 FAIL**이다. 이 숫자를 독립적인 물리 시나리오 수로 해석하지 않는다. 원본 reference의 상태는 계속 `FAIL`이다. [생산 원시 결과][primary] [독립 원시 결과][reference]

실패는 native9의 \(\phi\) 한 값이다. 생산 상계와 Decimal80 참조의 차이는 양수

\[
2.91082879488003260494168072896889699597324659550784\times10^{-30}
\]

이며, 고정 근접성 기준 $10^{-30}\max(1,|P|,|\phi_{\rm ref}|)$를 초과했다. 과소상계를 관측한 항목은 아니다. 음의 \(d\)에서 생산값은 저장된 지수 하한 \(\ell\)로부터 \(P=\operatorname{up}_{128}((1-\ell)/|d|)\)를 계산한다. 지수 구간 폭이 정확히 \(51/2^{128}\), \(|d|^{-1}=20,000,000\)이므로

\[
0\le P-\phi\le\frac{u-\ell}{|d|}+2^{-128}
=\frac{1020000001}{2^{128}}=:A
\]

라는 매개변수 의존 오차 예산을 얻는다. 기존 reference의 공통 근접성 기준은 이 증폭을 반영하지 않았다. 최초 정적 심사도 이 정확도 조건을 놓쳤다는 한계를 실패 심사에 기록했다. 원래 FAIL을 소급해서 PASS로 바꾸지 않는다. [REF01 독립 심사][failure]

### 고정한 표적 보완: 실제 24/24 PASS

보완 계약은 이 스칼라 하나를 생산 구현과 독립적인 exact Fraction 급수로 재판정한다. $x=|d|\delta\in(0,1)$에서

\[
L=S_9=\delta\sum_{k=0}^{9}\frac{(-x)^k}{(k+1)!}
\le\phi\le
U=S_8=\delta\sum_{k=0}^{8}\frac{(-x)^k}{(k+1)!},
\qquad U-L=\frac{\delta x^9}{10!}
\]

이다. 실행 전에 차수와 24개 명명된 검사를 고정했다. 핵심 조건은 $P\ge U$, $P-L\le A+(U-L)$, $P-U>10^{-30}$다. 앞의 두 조건은 상계와 분석적 여유를 검증하고, 마지막 조건은 참값과의 차이 자체가 기존 근접성 기준을 넘는다는 사실을 독립적으로 확인한다. 차수를 결과에 따라 올리거나 전체 reference 허용치를 완화하지 않는다. [보완 수학 계약][repairmath]

Runner SHA256 `219825e3786085951e456cb7408044598bc30166f5decee5669bc27c4147998d`를 고정한 **1회, 전체 CPU 10초, wall 30초** 계약 아래 실제 **24/24 PASS, exit 0**을 얻었다. 적분 bracket 폭은 약 $3.11549724\times10^{-76}$, $P-S_8$은 약 $2.91082879\times10^{-30}$, 분석적 예산은 약 $2.99751060\times10^{-30}$다. 저장된 $\phi$가 엄밀한 상계임을 확인했고, 최초 근접성 FAIL을 다른 exact 기준으로 재판정했다. [보완 실행 계약][repaircontract] [실제 결과][scalar]

보완 원시 SHA256은 `0ea2399efd86657703a826e01b2c71528e994b990ae6ab9ffdab8c84653f2dcc`, 전체 OS CPU는 **0.072788초**, wall은 **0.073632초**다. 새 exp·ODE·생성자 계산과 primary·전체 reference 재실행은 0이다. 원본 primary SHA `520110d1…`, reference SHA `da699b9a…`, 기존 FAIL과 비용을 보존했다. 독립 최종 C9는 실제 결과를 읽고 REF01을 종료했으며 조건부 이론·코드를 채택했다. [최종 심사][c9] [보완 실행 영수증][scalarprocess]

## 6. CAS의 부분 확인과 남은 기호식

최초 Wolfram 호출은 해결되지 않은 `Greater` 식의 JSON 직렬화에서 실제 `$Failed`를 반환했다. 원본 응답과 `Power::infy`, `Infinity::indet`, export 오류를 보존했다. 별도로 허가한 export 수리 1회에서는 scalar residual **7/7=0**, kernel control **9/9=0**, 즉 16개 영 잔차를 얻었다. 부호식은 **6개 중 4개가 True**였고 두 식은 기호식으로 남았다. 경고의 수학적 원인은 `NOT_ESTABLISHED`다. [CAS 기록][cas]

미해결 두 항목에는 일반 증명의 독립 근거가 있다. \(\phi>0\)은 양의 지수함수를 양의 길이 구간에서 적분한 사실로, 과거 cell의 지연 하한은 \(t\ge n\delta\), \(s\le(j+1)\delta\)의 차로 얻는다. 이 수동 증명이 CAS가 실제로 True를 반환했다는 뜻은 아니다. 따라서 CAS 상태는 **qualified partial symbolic corroboration**으로 유지한다. 일반 증명은 별도 독립 심사에서 material finding 0으로 범위 한정 통과했다. [이론 심사][theoryreview]

## 7. 실행 비용·게시·백업과 재현 경계

| 작업 | 실제 실행·상태 | 기록된 비용 |
|---|---|---|
| Primary | 1회, exit 0, 237 PASS | OS CPU 3.807278초, wall 3.808826초 |
| 최초 reference | 1회, exit 1, 첫 FAIL 보존 | OS CPU 0.440898초, wall 0.443167초 |
| 최초 과학 CAS | 1회, export 실패 | tool wall 10.1초, 실제 CPU 미제공 |
| 과학 CAS export 수리 | 1회, 부분 기호 확인 | tool wall 14.2초, 실제 CPU 미제공 |
| 저장 자료 그림 후처리 | 새 과학 평가 0 | 최초 CPU 4.317594초 + 최종 상태 갱신 CPU 26.291498초; 이전 비용 보존 |
| 표적 \(\phi\) 보완 | 1회, exit 0, 24/24 PASS | OS CPU 0.072788초, wall 0.073632초 |

세 Python 과학 실행의 실제 CPU 합은 **4.320964초**이며 import와 직렬화를 포함한다. 그림 후처리와 CAS는 별도다. CAS wall 시간을 CPU로 대체하지 않는다. 원래 R8 primary/reference 및 이전 R6/R7/PHYS91 예산은 소진 상태를 유지했고, 표적 보완의 별도 1회 allowance도 사용했다. 전체 과거 CPU와 전역 잔여 예산은 `null`이며 추정하지 않는다. [실행 장부][ledger] [보완 영수증][scalarprocess]

S01–S10의 source commit과 단계 ZIP을 게시했으며 Drive·Dropbox에서 실제 원본 바이트를 다시 받아 SHA256과 크기를 대조했다. 최초 reference가 실패한 S07도 원본 실패 결과와 비용을 그대로 보존했다. 각 R_i/C_i 쌍은 하나의 공유 S_i checkpoint로 게시·백업했다. Archive 범위는 R4–R8 분자 leaf, AGENTS와 지정 workflow이며 전체 저장소 이력은 별도다. [전체 게시·백업 색인][delivery]

| 단계 | 고정 source commit | 완료/전체 DAG | 실제 이중 보존 상태 |
|---|---|---:|---|
| S01 | `a50f018dd723` | 15/32 | [Drive 원본](https://drive.google.com/file/d/1ibp0idfL1NAlczdNKHo2xVlEY3ekZLVw/view) · SHA256/bytes 일치 |
| S02 | `667c60543f99` | 15/32 | [Drive 원본](https://drive.google.com/file/d/1nPOYH_iCvF0w_5_izHS_mXo33ZJ3C7iR/view) · SHA256/bytes 일치 |
| S03 | `d2c999833ce4` | 15/32 | [Drive 원본](https://drive.google.com/file/d/1FXqgxQTw26p9OqZIN7dCRQ2UsdEXv2kL/view) · SHA256/bytes 일치 |
| S04 | `30b11c5502aa` | 15/32 | [Drive 원본](https://drive.google.com/file/d/11AB3LXOZLGrze6X1RLMtTZeAzMY0e1he/view) · SHA256/bytes 일치 |
| S05 | `3f0093c7080f` | 15/32 | [Drive 원본](https://drive.google.com/file/d/1w51iMFSHoN2wGAcKBoNFgMl2leScKVhn/view) · SHA256/bytes 일치 |
| S06 | `72931db38a5d` | 15/32 | [Drive 원본](https://drive.google.com/file/d/1io-m6kAbhHpWcAT81HavEd17MDD6_0P3/view) · SHA256/bytes 일치 |
| S07 | `b87ea61ab2d5` | 15/32 | [Drive 원본](https://drive.google.com/file/d/1RoF5ffwHyFyu00MHPlNBOs3RXFGfaCTE/view) · SHA256/bytes 일치 |
| S08 | `ade11fe31248` | 15/32 | [Drive 원본](https://drive.google.com/file/d/1JjHuO0ca2XVoskTJxQ_N3Y3wectiod_I/view) · SHA256/bytes 일치 |
| S09 | `eb437ab5ec60` | 17/32 | [Drive 원본](https://drive.google.com/file/d/118Vg_ppWpIuMQ_VnjsRB7ElIZT1koIPM/view) · SHA256/bytes 일치 |
| S10 | `73f628736df3` | 17/32 | [Drive 원본](https://drive.google.com/file/d/104pqHMeL5lyyOWZQFTCED3E0zUmNRDmF/view) · SHA256/bytes 일치 |

최종 metadata source archive는 S10 영수증을 포함한 별도 snapshot이다. 그 archive 자신의 업로드·readback 영수증은 자기 source에 포함될 수 없으므로 외부 최종 영수증으로 제공한다. 과학 payload, source commit, ZIP SHA256을 서로 대체하지 않는다.

## 8. 물리 적용의 조건과 다음 행동

Native source의 선택은 100 K, collider 2인 para-H2 회전 여기 자료다. 원천의 진동 상태는 `UNSPECIFIED`를 유지한다. Flower 원문은 이번 조사에서 abstract·metadata와 제공자 맥락을 읽은 범위이며 Tables 1/2 전체를 읽었다고 주장하지 않는다. 회전 여기 자료를 반응성 파괴율로 바꾸어 쓰지 않는다. 실제 밀도가 없으므로 \(\tau=n_{\rm coll}(10^{-11}\,\mathrm{cm^3/s})t\)를 물리 시간으로 환산할 수 없다. [Flower, 1999][flower] [LAMDA HD][lamda] [문헌 범위][literature]

물리 적용을 위해서는 명명된 HD 소비자의 상태 순서·초기 조건·불변량, 호환되는 상태별 형성·파괴 배열과 선택한 이론 대안, collider pool·밀도·온도·clock, 그리고 소비 구간의 tube·오차 기준이 필요하다. 조사한 최신 owner 자료는 이 결속을 완성하지 않았다. 따라서 현재 `physical_consumer_admitted=false`, HH_R10은 OFF, production은 NOT_ISSUED이며 물리 완료와 중앙 완료의 증가분은 0이다. [연구 계약][contract]

다음 연구는 [NEXT_INPUT_CONTRACT.json][next]에 고정했다. 우선 GL2022의 원래 상태별 reactive 배열(10.1063/5.0128598) 또는 명명된 실제 소비자의 입력을 받아 상태·spin·공통 pool을 결속한다. 그 소비자의 collider density와 clock, 초기 불변량, 전체 구간을 덮는 양의 box, 관측량과 목표 오차를 확인하고 기존 R6/R7/R8 인증을 적용한다. 실제 K가 상태에 의존해 기존 결속이 부족한 경우에만 추가 feedback 항이나 운영 시간 좌표의 변환을 유도한다.

기존 R4–R8 성공 결과·실패 기록·검산·CAS·백업은 identity와 전제가 유지되면 재사용한다. 새 입력이나 구체적인 새 수학 의무 없이 pass 수를 늘리거나 이전 실험을 반복하지 않는다. 물리 입력의 미확보는 해당 입력 의존성으로 기록한다. 이번 연구는 새 strong no-go를 주장하지 않으며, late-forcing 반례는 현재 cell forcing에 전체 블록 수축을 잘못 곱하는 식의 실패 범위로 한정했다. NG1–NG7에 대한 범위 검토는 [과학 채택 기록][admission]에 있다.

## 9. 구현 재사용과 재현 경계

구현 진입점은 [src/volterra_feedback.py][core]의 `kernel_ladder`, `coarse_step_factors`, `volterra_two_pass`다. 마지막 함수는 `B, g, delta, initial, baseline_cells, certificates`와 키워드 `binding, point_caps=(), bits=128`을 받는다. Caller는 원본 baseline/cap의 실제 소속, 상태·clock·norm·같은 family와 all-starts 조건을 결속해야 한다. API의 Boolean metadata만으로 물리적 입력의 유효성이 만들어지지는 않는다.

코어는 최대192 cell, 최대8 인증, 정확히2 pass, dyadic128와 제한된 유리수 정수 크기를 사용한다. 일반 구현의 도메인과 이번 고정 검증 입력을 구분한다. 실제 검산의 지수 인수는 $|d\delta|\le1/4$이고, 전체 허용 도메인의 모든 입력을 표본 검사했다는 주장은 하지 않는다. 각 명령·입력·원시 출력·전체 프로세스 비용은 raw/와 EXECUTION_LEDGER.json에 보존했다.

다음 대화에서는 [HANDOFF_KO.md][handoff]의 복사 블록과 실제 최종 영수증을 사용한다. 승인된 게시 대상은 `research/provider-registry-20261025`와 draft PR150이며, expected-SHA·force=false의 추가 게시를 유지한다. Main merge와 다른 owner 저장소의 변경은 이 결과에 포함되지 않는다.

[contract]: CONTRACT.json
[dag]: DAG.json
[inventory]: authority/INVENTORY_DELTA.json
[survey]: authority/SYNTHESIS_KO.md
[intake]: authority/BACKUP_CONTEXT_INTAKE.json
[proof]: theory/PROOF_KO.md
[preflight]: reviews/C9_PREFLIGHT_REVIEW_KO.md
[metrics]: results/FINAL_RESULTS_SUMMARY.json
[plot]: results/PLOT_PROVENANCE.json
[primary]: raw/PRIMARY_RESULTS.json
[reference]: raw/REFERENCE_RESULTS.json
[failure]: reviews/REFERENCE_FAILURE_REVIEW_KO.md
[repairmath]: reviews/PHI_SCALAR_REPAIR_MATH_KO.md
[repaircontract]: verification/PHI_SCALAR_REPAIR_CONTRACT.json
[cas]: raw/WOLFRAM_QUALIFIED_SUMMARY.json
[theoryreview]: reviews/R6_THEORY_REVIEW.json
[ledger]: EXECUTION_LEDGER.json
[delivery]: delivery/PUBLICATION_INDEX.json
[literature]: authority/LITERATURE.json
[mitrophanov]: https://files.ele-math.com/articles/mia-08-15.pdf
[flower]: https://doi.org/10.1088/0953-4075/32/7/016
[lamda]: https://home.strw.leidenuniv.nl/~moldata/HD.html

[snapshot]: https://github.com/cosmosapjw-quantum/WU088_HH/tree/eb437ab5ec60d3b503be115c5560a85172502aba/research/provider_registry_molecular_r8_20261027
[scalar]: raw/PHI_SCALAR_REPAIR_RESULTS.json
[scalarprocess]: raw/PHI_SCALAR_REPAIR_PROCESS.json

[finalresults]: results/FINAL_RESULTS_SUMMARY.json
[admission]: SCIENTIFIC_ADMISSION.json
[payload]: SCIENTIFIC_PAYLOAD_MANIFEST.json
[c9]: reviews/C9_FINAL_REVIEW_KO.md
[next]: followup/NEXT_INPUT_CONTRACT.json
[core]: src/volterra_feedback.py
[handoff]: HANDOFF_KO.md
