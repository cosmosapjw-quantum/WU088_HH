# PHYS72 — 실제 outgoing Coulomb Green 상한과 4차 이상 Born remainder

## 결과

원래 atomic exterior 문제의 실제 outgoing Coulomb Dirichlet Green operator에
대해 모든 각모드와 `r>=27`을 포함하는 명시적 가중 상한을 구성했다.
원래 screened multiplier를 결합한 연산자 노름은

\[
q\le\frac{553311}{10^{26}}=5.53311\times10^{-21}<1
\]

이다. 따라서 `lambda=1`에서 exterior Born 급수가 연산자 노름으로 수렴하며,
원래 성분 `(21,20),m=0`의 4차 이상 remainder는

\[
|R_{\ge4}(1)_{21,20}|<1.50654\times10^{-80}\,a_0^{-1}
\]

로 닫힌다. 계산값은 `verification/EXACT_BOUND_CERTIFICATE.json`에 정확한
유리수 분자·분모와 위로 반올림한 decimal로 저장했다.

완료된 PHYS71 D3 표시 중심을 그대로 쓰면

\[
[(Z_1-Z_0)-D_1-D_2]_{21,20},\quad m=0
\]

의 포함원이 다음과 같다. 여기서 빼는 `D1,D2`는 정확한 계수다.

\[
z_3=(2.14300135468641834333042543662
+1.71865149630238869433259719024\,i)\times10^{-71}\,a_0^{-1},
\]
\[
|T_{\ge3}-z_3|\le\epsilon_3+R_{\ge4}
<7.271949342749\times10^{-79}\,a_0^{-1}<10^{-78}\,a_0^{-1}.
\]

기존 `epsilon3=7.121295358370e-79`에는 표시 중심의 rounding error가 이미
들어 있다. 새 코드는 이를 두 번 더하지 않는다. 전체 수치 `DeltaZ` 중심을
조립할 때에는 기존 `epsilon1+epsilon2`와 새 합의 표시 반올림을 더해야 한다.
이번 산출물은 그 합을 계산했다고 주장하지 않는다.

## 무엇으로 상한을 얻었는가

고정된 원래 reduced operator는

\[
A_0=-\partial_r^2+J/r^2-2/r-k^2,\quad J=-\Delta_{S^2},
\quad u(B)=0,\quad B=27,\quad k=7/10.
\]

실제 outgoing `H_j^+=G_j+iF_j^C`로부터

\[
\mathcal G_j(r,s)=\phi_j(\min\{r,s\})\frac{H_j^+(\max\{r,s\})}{H_j^+(B)},
\qquad \phi_j(B)=0,\quad \phi_j'(B)=1
\]

을 구성했다. 도함수 점프는 `-1`, 경계 미분은 `+f_j(s)`다. 이 부호가
`A0^-1`과 `Z=+u'u^-1`의 기존 Born convention에 맞는다.

핵심 multiplier는 `beta=r-B/2`다. `w=u'-iku`를 사용하면 양의 radial/angular
energy와 Coulomb의 무한원 경계항이 함께 나온다. outgoing Coulomb 위상이
`kr+(1/k)log(2kr)`이므로 그 경계항은 0이 아니다. 이를 flux identity로
정확하게 처리하면

\[
X^2+BW^2+Y^2+\frac B2\|u'(B)\|^2
\le2FX+\frac2kFW,
\]

여기서 `F=||rf||`, `X=||u'-iku||`, `W=||u/r||`,
`Y²=integral (r-B)/r³ ||grad_Omega u||²`이다. `X`에 관해 완전제곱하면

\[
\|R_0^+f/r\|\le C_R\|rf\|,\qquad
C_R=\frac{10+\sqrt{1423}}{189}=0.2525009112577779\ldots<\frac{253}{1000}.
\]

마지막 유리수 endpoint는 정확한 다항식 값
`37701/7000000>0`으로 확인한다. angular energy의 계수가 모든 `j`에 대해
양이므로 유한 `L`의 최대값을 무한 모드에 대입할 필요가 없다.

원래 off-center potential은

\[
V=2(1+1/d)e^{-2d},\qquad d=|r\mathbf n-0.7\hat z|
\]

이며 `V<=delta exp[-2(r-B)]`, `delta=3e-23`을 만족한다. 이 envelope도
`exp(263/5)`의 양의 Taylor 합 80차로 정확히 검산했다. 따라서

\[
\|V\|_{H_-\to H_+}\le B^2\delta,
\qquad
\|\sqrt V R_0^+\sqrt V\|\le(253/1000)B^2\delta=q.
\]

`V`를 중심대칭으로 바꾸거나 angular coupling을 생략하지 않았다.

경계에서는 기존 `C_j`를 보존한 가중 norm을 쓴다.

\[
\|g\|_C^2=\sum_{jm}C_j^2|g_{jm}|^2,\quad
C_j=77\ (j\le28),\quad C_j=(800/189)(j+1)\ (j\ge29).
\]

이는 `H1(S2)`와 동등한 명시적 경계 norm이다. `5929`는 외부 두 모드
`C21*C20`의 곱이며 `sup_j C_j²`가 아니다. 이 norm에서

\[
\|R_{\ge N+1}(\lambda)\|
\le\frac\delta2\frac{|\lambda|^{N+1}q^N}{1-|\lambda|q}
\quad(N\ge1,\ |\lambda|q<1)
\]

를 얻었다. `(21,20)` 성분에는 이 식에 5929를 곱한다. 위 조건은 충분조건이며,
범위를 벗어난 입력은 코드가 `SUFFICIENT_CONDITION_NOT_MET`로 기록한다.
이를 발산 판정이나 strong no-go로 해석하지 않는다.

원래 multiplier 자체의 angular 미분도 명시적으로 제어했다.
`|grad_S log V|<=502943/358995<3/2`와 product rule로 radial/angular 가중공간
`X_-(H1)->X_+(H1)`에서 `||V||<=2B²delta`, 따라서 `||R0^+V||<=2q`를 얻는다.
기존 growing `C_j` 공간에서는 `||V||<=77B²delta`, `||R0^+V||<=77q`다.
두 값은 각각 `1.106622e-20`, `4.2604947e-19`로 1보다 작다. 상세 유도와
13개 정확 scalar witness는 `ANGULAR_MULTIPLIER_ADDENDUM.md` 및
`verification/ANGULAR_WEIGHTED_BOUNDS.json`에 있다. Born remainder는 계속
더 작은 bulk L2 sandwich 상한 `q`를 사용한다.

## 재사용과 새 실행

실제 원격 PR123 HEAD `7060b2390caa931a74b3a377150731b98c2431a9`에서
새 branch를 시작했다. PR121 HEAD가 그 조상임을 Git으로 확인했다.
cutoff 이후 GitHub·백업·host 대조는
`intake/POST_CUTOFF_RECONCILIATION.md`에 기록했다.

| 근거 / 실행 | 실제 범위와 판정 |
|---|---|
| PHYS63 | 실제 exterior LAP/Poisson/DtN 질적 존재, 완료 근거 재사용 |
| PHYS69 | 완료 D2와 전체 radial ratio lemma 재사용 |
| PHYS71 | 76 패널·152 profile 및 corrected D3 완료 근거 재사용 |
| 새 exact Python suite | 최초 13/13 통과, serialization 보완 후 최종 14/14 통과 |
| 독립 exact audit | defining scalar inverse와 finite polynomial을 비교하는 22개 검사 통과 |
| symbolic calculation | shifted coefficient residual 0, exact root witness 및 q/tail 대조 |
| manufactured identity | 새 4개 field, 12개 scalar quadrature; 상대 잔차 최대 3.94e-16 |
| actual Coulomb points | 60dps, 12개 기본 점+12개 recurrence 보조 쌍, scalar 함수 48회; 적분 0 |
| Fortran | Rust 부재 후 우선 검토·구현·실제 compile/run; rounded cross-check |
| PHYS71 panel/profile 재적분 | 0 |
| 이번 새 물리 campaign / NCP 제출 | 0 / 0 |

manufactured field는 원래 `A0`에 넣은 별도 검산 함수이며 frozen source 해가
아니다. Coulomb 점 검산은 Wronskian·경계조건·Green 점프와 대칭을 확인한다.
연속체 전체 상한은 해석적 증명에서 나온다. Fortran의 floating output도
인증값으로 사용하지 않고 정확 Fraction 결과와 비교한다. 구체적인 실행·실패·
수정·독립 검토는 `verification/`에 각각 남겼다.

## VigilODE와의 대응

VigilODE PR77/78은 다른 reflecting-grid 문제다. 그 grid generator와
boundary flux, row gain, invariant box 수치는 HH로 이식하지 않았다.
이 회차에서 사용한 구조는 실제 HH의 `(I-lambda S)z=b`에 대한
`||error||<=||residual||/(1-|lambda|q)`다. 여기서 `S`와 `q`는 위 Coulomb
증명으로 새로 정했다. 원래 model과 수학적 대응을
`theory/THEOREM_AND_MODEL_MAP.md`에 명시했다.

## 구현·NCP 인계

`implementation/bounds.py`는 표준 Python만으로 exact rational upper bound,
수렴 충분조건, 최소 보존 차수, 같은 공간 residual error를 계산한다.
`implementation/third_and_higher.py`는 고정 SHA 세 개를 확인한 뒤 기존 D3
표시 중심에 새 remainder만 더한다. 출력은 create-only다.

NCP에는 새 이론이나 미구현 알고리즘을 넘기지 않는다. 이미 준비된 코드를
환경에 맞춰 compile하고 실행·회수하는 선택적 재현만 남는다. 정확 Python
계산에는 외부 package가 필요 없다. Fortran compile/run 명령과 반환 계약은
`ncp_delivery/README_KO.md`에 있다. 이 해석적 결과를 승인하기 위해 새 장시간
수치 campaign을 요구하지 않는다.

## 단계·DAG

R1–R10과 C1–C10의 대응 근거는 `LOOP_RECORD.md`, 실제 실행은
`EXECUTION_LEDGER.json`, 과학 의존성은 `NEXT_DAG.json`에 분리했다.
Git 게시와 provider 백업은 `publication/`의 실제 ACK로 닫는다.

이번 회차에서 닫힌 것은 실제 exterior Green 가중 상한, 원래 screen의
operator bound, `lambda=1` 수렴, 4차 이상 tail 및 위 third-and-higher
포함원이다. 다음 물리 단계는 원래 source-driven `xi`, origin/incoming
adjoint matching, `sigma(E)`, Maxwellian `k_HH(T)`다. `eta=Fy`, `xi=Fy-phi`,
`eta_C=-10/7`을 계속 구분하고 `HH_R10=OFF`를 유지한다.

수학적 증명 전체와 원전 관계는
`theory/THEOREM_AND_MODEL_MAP.md`부터 읽으면 된다.
