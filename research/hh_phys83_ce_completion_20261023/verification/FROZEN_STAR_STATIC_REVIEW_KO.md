# Frozen H I 3-state star 독립 정적 검토

## 판정과 검토 identity

**STATIC_REVIEW_PASS_SCOPED.** 원래 PHYS83의 닫힌 1s/2s/2p 모델에 대해
스펙트럼 해, 반복근 적분, 사건 적분, 에너지 부호 및 coronal 비교식에서
수정을 요구하는 대수적 결함을 찾지 못했다. 이는 정적 수식–코드 검토다.
수치 정확도, branch 경계, scipy의 incomplete-gamma 평가 또는 전체 과학 grid의
PASS를 뜻하지 않는다. 그 판정은 별도 독립 verifier가 담당한다.

검토자는 `source/nuclear_ownership.py` 작성자이나 `source/frozen_star.py`의
작성자는 아니다. 이번 검토에서는 커널을 import하거나 실행하지 않았다.
새 numerical kernel 호출 0, 과학 실행 0, 기존 완료 identity 재실행 0,
production kernel 수정 0이다.

| 증거 | 검토한 SHA256 |
|---|---|
| `source/frozen_star.py`, 12,414 bytes | `78421356c6b985d845f452f42e6b03c8ea657171ad826df51b3a1dbcf454578f` |
| `theory/PARENT_DERIVATION_KO.md` | `2d31b237fe3f91fedb4d44f9e7a947e57a1f01a41494b9d45aae2bb80588b445` |
| `theory/MATCHED_CE_IMPLEMENTATION_MAP_KO.md` | `b66696877a381556ab35c3678db4634c2e827e14df65a2e599c30ddfe414f181` |
| `CONTRACT.json`, revision 2 | `d9eb980df5236e2b2ca3da313813c3ca2b21562f90486f1173d0ea509bc4dcc5` |

물리 기준은 부모 PHYS83 S0 `09289300ec2e500806aa2cb82365f00329e41c8c`의
구성적 유도 §§4–7 및 이 continuation의 계약이다. 이하 행 번호는 위에
기록한 `frozen_star.py` bytes에 대한 위치다. 외부 문헌이나 새 수치 결과를
추가한 검토가 아니다.

## 1. 선택한 유한 모델과 고유값

`a_i = ne q_up_i`, `c_i = ne q_down_i`, `d_i = c_i + A_i`이고, 상위 두
population은 다음 식을 따른다.

\[
\dot x=a-Bx,\qquad
B=\begin{pmatrix}d_s+a_s&a_s\\a_p&d_p+a_p\end{pmatrix},
\qquad x(0)=0.
\]

112–129행의 trace, discriminant, determinant는 이 행렬과 일치한다.
특히

\[
\det B=d_sd_p+a_sd_p+a_pd_s>0,\quad
\delta=\sqrt{(d_s+a_s-d_p-a_p)^2+4a_sa_p},
\]

이며 `fast=(trace+disc)/2`, `slow=det/fast`는 작은 고유값을
`trace-disc`로 빼서 얻지 않는다. `gap=disc` 역시 가까운 두 저장 고유값을
다시 빼서 얻지 않는다. 위 항들은 모두 양의 감쇠율에 해당한다.

`d_s <= d_p`일 때 123행의 shift는

\[
(\lambda_l-d_s)(\lambda_f-d_s)=a_s(d_p-d_s)
\]

에서 얻은 `lambda_l-d_s`다. 따라서 `coef_s = d_p-lambda_l`,
`coef_p = d_s-lambda_l`이고, 반대 순서의 분기도 같은 항등식으로 성립한다.
이는 부모 §5의 해에 필요한 계수다. 상위 준위의 방사율을 서로 뒤바꾸거나
trace에 두 번 더하는 오류가 없다.

## 2. 세 적분 분기와 반복근

### 작은 시간: 38–57행, 72–86행

`_phi_minus(1,x)`와 `_phi_minus(2,x)`는 각각
`(1-exp(-x))/x`, `(exp(-x)-1+x)/x^2`다. `x <= 1/2`에서 사용하는
급수의 항 비는 `-x/(n+order)`여서 절댓값이 감소한다. 코드가 마지막
포함 항의 크기를 기준으로 멈추는 것은 다음 항의 교대급수 bound보다
보수적이다. `x=0`에서는 각각 1과 1/2로 이어진다.

`h_n(xs,xf) = sum_j xs^j xf^(n-j)`로 놓으면 코드의 recurrence
`homog = xf*homog + xs^n`는 이 complete homogeneous polynomial을 만든다.
이에 따라

\[
H_2=t^2\sum_{n\ge0}{(-1)^n h_n(x_s,x_f)\over(n+2)!},\qquad
H_3=t^3\sum_{n\ge0}{(-1)^n h_n(x_s,x_f)\over(n+3)!}.
\]

이는 원래 divided difference의 직접 전개이며, 고유값 차로 나누지 않는다.
`xf <= 1/2`와 `0 <= xs <= xf`에서는 항이 감소하므로 사용한 절단 판정과
일치한다. 두 고유값이 동시에 0인 형식적 극한도 `t^2/2`, `t^3/6`이다.
실제 H I 모델에서는 양의 spontaneous A 때문에 두 고유값이 0이 되지 않는다.

### 가까운 양의 근: 87–105행

코드는 부모 유도에 제시된 `delta*t` 전개를 그대로 자르는 대신,
`rho = delta/slow <= 1/4`와 정규화된 incomplete gamma를 쓴다.
이는 다른 근사가 아니라 같은 양의 적분을 재배열한 것이다.
`x=slow*t`, `P(a,x)=gamma(a,x)/Gamma(a)`로 놓으면

\[
H_2={1\over\lambda_l^2}\sum_{n\ge0}(-\rho)^n P(n+2,x),
\]

\[
H_3={1\over\lambda_l^3}\sum_{n\ge0}(-\rho)^n F_n(x),\qquad
F_n=xP(n+2,x)-(n+2)P(n+3,x).
\]

코드 94행의 bracket은

\[
F_n={1\over(n+1)!}\int_0^x(x-y)y^{n+1}e^{-y}\,dy>0
\]

이다. 또한 incomplete-gamma recurrence에서

\[
P(n+2,x)-P(n+3,x)>0,\qquad
F_n-F_{n+1}=P(n+3,x)>0
\]

를 얻는다. 그러므로 두 급수 모두 다음 항/현재 항의 절댓값이 `rho` 이하이며,
코드의 `abs(current)*rho/(1-rho)`는 남은 절대합의 bound다. 두 급수 중
작은 부분합에 대해 공통으로 검사하는 100행은 각각을 따로 검사하는 것보다
보수적이다. `rho=0`에서는 첫 항만 남고 뒤의 항은 정확히 0이다.

따라서 같은 양의 근 `lambda`에 대해

\[
H_2={1-(1+\lambda t)e^{-\lambda t}\over\lambda^2},\qquad
H_3={\lambda t-2+(\lambda t+2)e^{-\lambda t}\over\lambda^3}
\]

가 구현된다. `t=0`은 앞선 명시적 zero-time 분기가 처리한다. 이 반복근
항등식에는 diagonalizable 가정이 필요하지 않아 형식적 Jordan limit에도
유효하다.

95–96행은 이론적으로 양의 bracket이 부동소수점에서 음수가 되면
clipping 없이 실패한다. 그 guard가 실제 지원 영역과 분기 경계에서
불필요하게 발동하지 않는지는 독립 수치 검증 대상이며, 정적 유도만으로
scipy 평가 오차를 인증하지 않는다.

### 분리된 근: 106–109행

이 분기는 `fast*t > 1/2`이며 가까운 양의 근 조건에서 벗어난 뒤에만
실행된다. 따라서 작은 시간 및 반복근에서의 작은 차끼리의 차분은 앞선
분기가 처리한다. 두 positive decreasing 함수의 차를 `gap`으로 나누는
부호도 올바르다. 이 분기의 실제 상대오차 및 두 분기 경계의 연속성은
독립 verifier의 기존 population/event gate로 확인해야 한다.

## 3. Signed 계수와 population/integral의 조건수

255–258행은 부모 §5의 `h_fast + coef*H2`, `G_fast + coef*H3` 해를
그대로 계산한다. 일부 coefficient가 음수라는 사실은 음의 population을
도입한 것이 아니다. 상세평형 계약이 cancellation을 제한한다.

예를 들어 `d_s <= d_p`이면 음의 계수는 p 성분에만 나타난다.
`H2/h_fast <= 1/lambda_l`, `H3/G_fast <= 1/lambda_l`이고
`lambda_l <= d_s+a_s`이므로 두 bracket은 각각 해당 첫 항의
`d_s/lambda_l >= 1/(1+a_s/d_s)` 배 이상이다.
matched rate에서 `a_s/d_s <= exp(-Delta/kBT) < 1`이므로 이 비는 1/2보다
크다. 반대 순서에서는 `a_p/d_p <= 3 exp(-Delta/kBT) < 3`으로부터
1/4보다 큰 bound가 나온다. 따라서 계약 안의 signed coefficient를
임의로 양수화하거나 clipping할 필요가 없다.

전체 세 상태 generator는 양의 star detailed balance를 갖는다.
ground-start의 ground return probability는 stationary ground probability
이상이며,

\[
p_g(t)\ge p_g^*={1\over1+a_s/d_s+a_p/d_p}> {1\over5},\qquad
J_g(t)\ge t/5
\]

이다. 따라서 `pg=1-ps-pp`, `jg=t-js-jp`의 복원은 계약 내에서 임의로
작은 차를 만드는 경로가 아니다. 개별 상위 population의 stationary
값에 대한 단조성은 주장하지 않는다. 260–263행의 비유한값/음수 거절과
무 clipping 정책도 계약과 일치한다.

## 4. 사건 수, 에너지 및 소유권

264–277행은 population 적분에서 각각 `a_i Jg`, `c_i Ji`, `A_branch Ji`를
계산한다. 다음 두 항등식이 독립적으로 비교되도록 raw 항을 남긴다.

\[
x_s=C_s^+-C_s^- -C_{2\gamma}-C_{M1},\qquad
x_p=C_p^+-C_p^- -C_{E1}.
\]

원자 내부 에너지는 `Delta*(ps+pp)`이며, escaped radiation은
`Delta*(two+m1+e1)`다. 2-photon 사건은 photon 수에서만 2배이고, 에너지에서는
pair 전체에 Delta를 한 번만 할당한다. 이 구현은 두 광자 각각을
Delta/2의 단색광으로 가정하지 않는다.

열 bath의 signed change는

\[
\Delta u_{th}=-\Delta(C_s^++C_p^+-C_s^- -C_p^-)
\]

이다. `raw_event_thermal_change_eV`는 이 사건식에서 계산하고,
`thermal_change_eV = -(Uatom+Egamma)`는 양의 storage/escape 결과에서
안정하게 계산한다. 두 계산의 차인 `raw_energy_residual_eV`를 버리지
않는다. `heat_withdrawal_eV`는 양의 withdrawal 표기이며 부모 유도의
Q_th와 일치한다. 계약의 signed Qth와 부모 유도의 withdrawal Q_th 사이
명칭 차이를 별도 notation resolution으로 닫은 방식도 적절하다.

`gross_energy_scale_eV`는 양의 gross event/store 합이다. 이에 대한
sampled residual을 net-cooling의 상대오차나 continuum certificate로
해석하면 안 된다. `nuclei_residual` 역시 ground를 보완해 만든 구조적
합계 검사이므로, 독립 reference population 비교를 대체하지 않는다.

이 atom CE 모델은 translational particle 수를 바꾸지 않는다. 고정 T/ne
출력은 prescribed-bath의 에너지 교환 장부이며 coupled thermal update가
아니다. 주어진 source-native LS gap을 사용한 local normal-frame 스칼라
회계까지의 범위이고, finite-mass recoil·방출각 분포·signed tensor closure는
여기서 새로 인증하지 않는다. 201–206행의 owner guard는 native radiative
owner와 detached spontaneous owner의 동시 활성화를 명시적으로 거절한다.

## 5. Coronal 비교와 해석 범위

238–249행에서 `R=a_s/d_s+a_p/d_p`, `eta_i=c_i/A_i`이면

\[
j_i=A_i x_i^*={a_i\over(1+\eta_i)(1+R)},\qquad
{j_i^{cor}\over j_i}-1=\eta_i+R+\eta_iR,
\quad j_i^{cor}=a_i.
\]

출력한 exact-to-coronal factor와 relative overestimate는 이 식과
일치한다. collisional quenching과 ground depletion을 모두 포함하며,
photon count rate와 energy power의 2-photon 계수도 구분한다.

**비차단 표기 주의:** `ne=0`에서는 실제와 coronal power가 모두 0이지만,
`exact_to_coronal_*`는 식의 연속 연장값 1을 반환한다. 이는 무효한 직접
0/0 나눗셈을 수행한 것이 아니다. 0-density row를 외부 표에 포함한다면
이 factor가 analytic continuous extension임을 표 설명에 한 번 명시하면
충분하다. production 수식 수정은 필요 없다.

이 bound는 closed finite star의 stationary 비교다. high-density H I의
완전한 물리, 일반 transient의 steady coronal 오차 bound, 빠진 CE/CI/RR,
2s–2p mixing, opacity 또는 coupled thermal/charge history의 bound로
확장하지 않는다. `coverage()`가 이 경계를 드러내고 있다.

## 6. 독립 수치 단계에 남기는 항목

본 정적 검토에는 수치 실행이 없다. 다음 항목은 이미 배정된 독립 검증이
판정할 구체적 수치 위험이다.

- exact repeated root 및 양쪽 인접 근에서 H2/H3의 독립 positive-integral 비교.
- `fast*t = 1/2`와 `gap/slow = 1/4` 분기 양쪽에서 같은 적분으로의 연속성.
- source-pinned 범위의 stiffness 양끝에서 population/integral/event reference
  비교와 무 clipping 양성성.
- raw energy residual과 per-level event balance의 계약 gate, owner-conflict 거절.

현재 결론은 **정적 대수·범위·소유권 검토 통과**다. 새 science 완료,
수치 grid PASS, production admission 또는 continuum certificate로 격상하지
않는다. `HH_R10=OFF`, `Production admission=NOT_ISSUED`를 유지한다.
