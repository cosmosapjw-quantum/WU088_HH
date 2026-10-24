# PHYS86 독립 R6 이론·계약 검토

## 판정

**DERIVED_SCOPED_REVIEW_PASS / GO_IMPLEMENT_REVIEWED_BUDGET.** 검토한 CONTRACT revision1과 `theory/JUTTNER_REACTION_MOMENTS_KO.md`의 식(1)–(13)은 명시한 같은-frame classical common-T 분포, 고정 species 및 differentiation 조건 아래 일치한다. 발견한 두 P2 정의역 문제는 root가 수정했고 수정본을 다시 읽어 닫았다. 남은 blocking theory finding은0이다.

이 판정은 이론 채택과 동결 구현 준비에 대한 것이다. 실제 reference 검증, exact request의 실행 GO, scientific implementation admission은 발급하지 않는다. S1 게시·양쪽 ACK 후 root가 정확한 request identity에 실행 GO를 내리는 기존 순서를 유지한다. 새 reference output과 code diff는 C9에서 실제로 읽는다.

## 검토 범위와 방법

검토자는 source와 구현을 작성하지 않았다. PHYS85의 exact event owner, 독립 four-vector oracle, 두 실패 raw/receipt, 원래 finite-T 이론을 직접 읽은 뒤 이번 새 CONTRACT와 이론 전부를 읽었다. 정규화 적분, partition log derivative, thermal composition chain rule, flux 및 동일입자 counting, covariance/variance, Bessel recurrence, finite polynomial witness를 독립 대수 유도로 대조했다. 수치·Wolfram·과거 kernel을 실행하지 않았다.

읽기 시점 branch는 `research/hh-phys86-juttner-reaction-moments-20261024`, native HEAD는 부모 `696eca5cf9f1fcbf722370833535f4144af0a54a`다. 새 연구 경로는 아직 untracked 준비 상태였고 부모 파일 변경은 관측되지 않았다. 이 검토는 새 경로의 이 두 review 파일만 작성한다. 실제 검토한 원문의 bytes/SHA256은 동반 JSON에 결속한다.

## 1. Frame·분포·flux

`p^mu=(E/c,p)`, metric −+++에서 `D=-c² p_a·p_b`는 양의 energy²이다. `v_rel=c sqrt(D²-epsilon_a² epsilon_b²)/D`와 `v_flux=D v_rel/(E_aE_b)`는 속도 차원을 가진다. 정규화된 두 `d³p` 분포 평균에는 `sigma*v_flux`가 들어간다. 이를 invariant relative speed 자체로 부르는 오류는 없다. 같은 normal frame에서 모든 event energy와 debit을 평가한다.

정규화에서 `p=mc sinh chi`를 대입하면

\[
Z=4\pi m^3c^3\int_0^\infty\sinh^2\chi\cosh\chi\,e^{-z\cosh\chi}d\chi
=\pi m^3c^3(K_3-K_1)=4\pi m^3c^3K_2/z.
\]

따라서 식(4)의 `4*pi*m²*c*k_B*T*K2`가 맞으며 차원은 momentum³이다. 고정 degeneracy와 `(2*pi*hbar)^(-3)`는 확률 정규화의 양쪽에 같이 들어갈 때 상쇄된다. `d³p/E` 분포를 이 EOS와 섞지 않았다.

동일종에 대해서는 unordered event rate의 `1/(1+delta_ab)`와 반응물 stoichiometric debit을 동시에 명시했다. a=b일 때 한 species의 소모는 −2R이며 event rate의 1/2와 별개다. 현재 세 실제 capture 채널은 서로 다른 두 reactant다. 최종 branch와 total/partial cross section의 정규화는 실제 supplier 의무로 유지된다.

## 2. 선택 에너지와 가변 composition EOS

독립 유도는 `log kappa=log N-log Za-log Zb`를 직접 미분한다. 고정 nonnegative B에 대해 `-d_beta log N=<S>R`, `-d_beta log Zi=<Ei>i`이므로

\[
\langle S\rangle_R-\bar E_a-\bar E_b=-\partial_{\beta_T}\log\kappa.
\]

`d beta_T/dT=-1/(k_B T²)`와 rest energies의 상쇄가 식(1)의 **양의** slope 항을 준다. 비상대론적 COM 분리는 쓰지 않는다.

EOS의 composition 항을 생략하지 않고

\[
C_V\dot T=R\langle hK_c-K_{in}\rangle_R
 -R[-u_a-u_b+\langle h\rangle_R u_c]
\]

를 먼저 만든 뒤 선택 식을 대입하면 식(3)이 나온다. `hKc`의 joint mean을 유지하며 `mean(h)*mean(Kc)`로 바꾸지 않는다. h=0 all-fast와 h=1 instantaneous caloric birth의 의미도 각각 맞다. 실제 fast stopping은 이 caloric closure에서 유도되지 않았다.

단위도 일치한다. `C_V`는 energy/(proper volume·temperature), R은 events/(proper volume·normal proper time)이며 `k_B T² d_T log kappa`와 `Kc-u_c`는 energy다. `N_th`를 쓰는 NR 표현은 본문의 n_i와 같은 number-density convention으로 읽는다. 총입자수를 쓰려면 R과 C_V를 동일 volume으로 함께 옮겨야 한다.

## 3. Covariance·곡률·T-dependent kernel

정규화 분포의 score가 `-(S-mean(S))`이므로 T독립 phi의 β 미분은 `-Cov(phi,S)`다. T로 바꾸면 식(9)의 양의 부호가 맞는다. 두 번째 β 미분에서 event-selected joint variance를 구하고 thermal partition의 두 variance를 빼면 식(10)이다. Event selection 뒤 두 reactant가 독립이라고 가정하지 않았다.

`B_T`를 직접 미분할 때 얻는 항은

\[
A_T=N^{-1}\int(\partial_T B_T)e^{-\beta_TS}d\lambda.
\]

따라서 식(11)의 `d_T log kappa-A_T` 부호가 맞다. 이 표현은 B=0에서 log를 나누지 않는다. 일반 평균 미분의 kernel 항은 정확히

\[
N^{-1}\int(\phi-\langle\phi\rangle_R)(\partial_T B_T)e^{-\beta_TS}d\lambda
\]

이며, score가 정의되고 적분 가능한 경우 `Cov(phi,d_T log B)`로 쓸 수 있다. T의존 phi에는 `mean(d_T phi)`가 더해진다. 원문은 기본 고정 kernel과 판별용 T-dependent kernel을 구별하며, 바뀌는 domain·quantum occupancy·screening을 자동 채택하지 않는다.

## 4. 열용량·극한

`K2=K0+2K1/z`, `K1'=-K0-K1/z`, `K2'=-K1-2K2/z`에서 `r'=r²+3r/z-1`을 직접 얻었다. 따라서

\[
u=\epsilon(r-1)+3k_BT,\qquad
u'/k_B=3+z^2-z^2r^2-3zr
\]

가 맞다. 별도 partition 경로의 `u'=Var(E)/(k_B T²)>0`와도 일치한다. NR에서 `u'→3k_B/2`를 넣으면 PHYS85 all-fast source를 회복한다. 고정종수 초상대론적 수학 극한의 `u'→3k_B`도 일치한다. 이 극한을 실제 bare-nucleus source의 물리적 사용 domain으로 확대하지 않았다.

큰 z의 cancellation은 원문에 남겨둔 production 수치 구현 의무다. 본 판정으로 안정한 floating-point Bessel kernel이나 continuum quadrature를 발급하지 않는다.

## 5. Finite witness의 독립 구성 대조

네 pair의 `(energy sum, base weight × G)`는 `(6,2),(8,3),(7,8),(9,8)`이다. 따라서 순서를 에너지별로 모으면

\[
N=2q^6+8q^7+3q^8+8q^9,
\quad Z_a=q^2+2q^3,\quad Z_b=2q^4+q^6.
\]

이는 계약의 polynomial oracle과 일치한다. 직접 moment 경로와 이 polynomial을 미분하는 oracle은 같은 생산 함수를 다시 호출하는 경로가 아니다. `d/db=-q d/dq`의 부호도 맞는다. q의 세 유리수점은 dimensionless exponential-family witness이고 nuclear cross-section data 또는 Jüttner continuum quadrature로 표시되지 않았다.

`G_b=qG`에서는 normalized event measure가 유지된다. `log kappa`에는 `log q=-b`가 더해져 `-d_b log kappa`가1 증가한다. Kernel score `d_b log G_b=-1`을 더한 선택 식은 원래 값으로 돌아간다. 따라서 보정항 생략 control이 nonzero이고 보정된 결과가 zero라는 판별은 적절하다. 이 결과는 정적 대수 판별이며 이번 검토에서 세 q점이나 Wolfram을 실행하지 않았다.

Caloric reference의 `u_c,R,C_V`는 formal symbols로 유지하고 coefficient identity를 검증하도록 계약이 보완되었다. 임의의 physical daughter EOS·rate를 만들어 넣지 않는다. 구현은 T>0, C_V>0, R>=0의 조건과 R=0 early source return을 구별해야 한다. R=0이더라도 nonpositive C_V를 유효한 온도 domain으로 승격하지 않는다.

## 6. 발견 사항과 처리

| ID | 등급 | 관측·영향 | 처리 |
|---|---|---|---|
| R6-01 | P2 | 초안 §5가 zero rate와 undefined normalized moment를 함께 기술하여 κ>0이나 density=0인 R=0과 구별하지 못함 | 수정본 §5와 CONTRACT의 caloric source 항이 N=κ=0, density-driven R=0, API early return을 분리. **CLOSED** |
| R6-02 | P2 | 일반 phi의 covariance identity에 energy second moment만으로 충분하지 않은 추가 적분가능성 조건이 필요 | 수정본 식(9) 앞에 mean(abs(phi)), mean(abs(phi S)) 유한성과 dominated differentiation 명시. **CLOSED** |

각 수정은 원래 물리 목표·수치 허용오차를 바꾸지 않고 정확한 정의역을 보완했다. 남은 blocking finding은0이다. 참고로 일반 kernel derivative의 integral 표현을 위 §3에 명시하여 score가 없는 경우의 의미도 고정했다. 이는 새 실행 gate를 추가한 것이 아니다.

## 7. 근거 문헌의 실제 대조

- [Chacón-Acosta 외, arXiv:0910.1625v1](https://arxiv.org/html/0910.1625v1) 식(1)을 직접 열어 comoving momentum density와 `4*pi*m²*c*k_B*T*K2` 정규화를 확인했다. 원문의 설명과 이번 normalized f_i의 n_i 분리가 일치한다.
- [Cannoni, arXiv:1506.07475v3](https://arxiv.org/html/1506.07475v3) Appendix B 식(64),(66)–(67),(71)–(75),(82)–(83)을 읽어 flux, pair factor, normalized thermal average 대응을 확인했다. 본 연구는 그 논문의 특정 annihilation cross section이나 relic-density 결과를 사용하지 않는다.
- [Wolfram BesselK 공식 문서](https://reference.wolfram.com/language/ref/BesselK.html) Applications의 relativistic ideal-gas heat capacity 식을 직접 읽어 식(12)의 독립 표현과 대조했다. 도구 실행으로 그 식을 검산한 것은 아니다.

원전은 normalization/flux/EOS의 배경을 제공한다. 이번 direct selection·composition·kernel correction 연결은 위 독립 유도로 검토했다. 새로운 보편적 정리의 문헌 신규성 또는 strong no-go를 주장하지 않으며 NG1–NG7은 새 no-go 채택 대상 없음이다.

## 8. 검토된 budget과 진행 범위

PHYS85의 기존 누적 Wolfram2회와 과거 잔여 cap0, namespace 실패와 truncated raw는 보존한다. 새 명시 계약은 **진단된 출력 교정1회 + 새 finite-moment reference1회**, optional probe0, 각각60초/inner55초, 한 kernel이다. 따라서 기존 두 호출을 포함한 현 계획의 누적 상한은4회다. 첫 항은 미완료 reference의 transport correction이며 두 번째는 이번 새 moment interface의 최초 application이다. 두 항을 별도로 장부에 적고 completed science replay로 바꾸지 않는다.

이 검토는 현 사용자의 내장1.0.0 연구·생산적 오류수정 요청, 새 출력 failure diagnosis, 독립적인 새 이론 질문과 한정된 계약을 근거로 **구현 준비 예산을 수용**한다. 과거 allowance를0에서 바꿨다고 기록하지 않는다. inherited spend/remaining/currency=null, reset=false이며 금액0이나 가용 예산 확인으로 추정하지 않는다. Additional repair는 자동 allowance가 아니고 새 구체적 진단을 controller가 평가하는 별도 변경이다.

Local reserve1.5GiB+job0.5GiB는 유지하며 PHYS84 최초 수치 실행을 이 cloud reference로 우회하지 않는다. 이번 reviewer의 scientific evaluation·Wolfram·local child·parent kernel·completed replay·remote mutation·다른 process 종료는 모두0이다.

**HH_R10=OFF; production admission NOT_ISSUED.** 실제 nuclear supplier/rates/stopping, physical finite-T averaging, coupled thermochemical/spectral trajectory, stable finite-precision production Bessel implementation은 별도 OPEN 의무로 남는다.
