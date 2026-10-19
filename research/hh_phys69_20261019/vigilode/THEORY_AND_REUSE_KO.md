# PHYS69: VigilODE의 원래 HH Born 적분 적용

## 기존 실행 근거를 먼저 회수한 결과

2026-10-19의 원격 및 백업 확인에서 VigilODE PR71
`fa07baf27a37674848d963e30e010d54e4af3f33`을 회수했다.
해당 PR와 대조한 구현 브랜치의 최신 소스는
`a21d573980f66fe02891bd216153443b5352f921`이며, main은 별도의 오래된
`8d0c79184e09efb5bdadc24a6315c60a71a44264`이다.

새 CT CSV 2,700행은 백업과 PR71의 원격 checkout에서 **바이트 단위로 같다**.
SHA256은 `03eda7909f39c467d1ddce7990dd2707b94a4dbb9bde5e036e21f1cf9435e2fa`다.
이 실행의 측정 Rust commit은 `8a8bd409b1d96c7b7421f496d229e119fd3d284e`다.
해당 commit에서 a21d573까지의 15개 변경은 Python triage/harness와 관련 기록,
ignore 파일이며 Rust 소스 변경은 없다. a21d573에서 PR71까지는 보고서/CSV/검산기
6개 경로 추가뿐이다. 따라서 기존 측정은 원래 측정 identity로 재사용하고,
이번 HH 이식의 빌드 identity는 실제 a21d573 git dependency 및 Cargo.lock으로 고정한다.

후속 `VigilODE_VODE_Diffsol_Comparison_20261019.zip`
SHA256 `790b4621e09dff21e196cc548b7851ca751d09f7b0287c52e0bc857fca2ad9ae`도
백업에서 회수해 10개 manifest payload 해시를 확인했다. 이는 기존 VODE 20개 결과행과
A07 비교를 보존한다. 이 자료의 세 solver를 동일한 달성 오차에서 비교한 속도 순위는
UNRESOLVED다. 두 호스트의 시간을 나누지 않았다. 기존 VigilODE benchmark,
VODE, PHYS68 RK4 및 Arb 적분의 신규 재실행 수는 모두 0이다.

CT 보고서의 `status=ok`와 실제 요청 출력 오차는 별개다. 2,639개 성공행 중
2,329개가 표본 출력 격자의 `R_up<=1`을 충족했다. 특히 한 nonlinear
Prothero–Robinson 조건에서 dense-off의 R_up은 약 1,752였다. 그래서 새 HH
클라이언트는 종점으로 직접 착지하고, 기존 PHYS68 Arb enclosure와 별도로 비교한다.
이 benchmark를 HH 문제의 전역 정확도 증명으로 사용하지 않는다.

원전:

- [PR71의 원래 CSV 및 근거 범위](https://github.com/cosmosapjw-quantum/vigilode/tree/fa07baf27a37674848d963e30e010d54e4af3f33/research/benchmark_results_20261019)
- [실제 사용하는 matrix-free U-form API](https://github.com/cosmosapjw-quantum/vigilode/blob/a21d573980f66fe02891bd216153443b5352f921/crates/rodas5p-integrators/src/rodas5p_matrix_free_fast.rs)
- [문제와 callback 계약](https://github.com/cosmosapjw-quantum/vigilode/blob/a21d573980f66fe02891bd216153443b5352f921/crates/rodas5p-integrators/src/problem.rs)
- [현재 accuracy·promotion 범위](https://github.com/cosmosapjw-quantum/vigilode/blob/a21d573980f66fe02891bd216153443b5352f921/README.md)

## 원식과 정확한 변수 변환

원래 원자 좌표, B=27, T=65, k=7/10, R0=7/10,
E=49/200 Hartree와 Coulomb eta_C=-10/7을 유지한다.
`eta=Fy`, `xi=Fy-phi`는 eta_C와 다른 원래 물리량이다.
동결 NPZ의 SHA256 검사는 실제 bytes에 적용한다. 이 외부 Born 계수 클라이언트는
그 NPZ를 source-driven xi의 구동항으로 사용하지 않는다.

정규화한 outgoing Coulomb 함수는

\[
\mathcal F_j(r)=H_j^+(r)/H_j^+(B),\qquad
G_j(r)=\partial_r\mathcal F_j(r),\qquad H_j^+=G_j^{C}+iF_j^{C}.
\]

여기서 도함수 상태 G_j와 Coulomb irregular 함수 G_j^C를 구분했다.
시간 변수는 tau=T-r로 둔다. s=2^80을 사용해 A_j=s q_{21,j},
C_j=s q_{20,j}, z=s^2 D2를 정의한다. L28에서는 복소수 117개,
실수 234개 상태이고, L64에서는 실수 522개다. 두 스케일은 binary64에서 정확히
표현되며 s^2=2^160이다.

\[
Q_j(r)=k^2+2/r-j(j+1)/r^2,
\quad V(r,\mu)=2(1+1/d)e^{-2d},
\quad d=\sqrt{r^2+R_0^2-2rR_0\mu}.
\]

정규직교 m=0 Legendre 기저에서 V_lj를 적분한다. 순방향 tau 방정식은

\[
\dot{\mathcal F}_j=-G_j,\qquad \dot G_j=Q_j\mathcal F_j,
\]
\[
\dot A_j=s\mathcal F_{21}\mathcal F_jV_{21,j},\qquad
\dot C_j=s\mathcal F_{20}\mathcal F_jV_{20,j},
\quad
\dot z=\sum_{j=0}^L\frac{A_jC_j}{\mathcal F_j^2}.
\]

초기 tau=0은 r=T이고 A=C=z=0이다. 마지막 tau=38에서
D2=z/2^160, q=A/2^80으로 돌린다. 복소수 곱은 bilinear이고 켤레를 쓰지 않는다.
D2는 lambda^2 계수이므로 ordinary second derivative의 2를 추가하지 않는다.
이 식은 PHYS68의
q_lj(r)=integral_r^T F_l(s)F_j(s)V_lj(s) ds와
D2(B)=sum_j integral_B^T q_21j q_20j/F_j^2 dr에서 바로 따른다.

## 해석적 JVP와 비자율 시간 편미분

변분을 delta로 쓰면

\[
\delta\dot A_j=sV_{21,j}(\delta\mathcal F_{21}\mathcal F_j
  +\mathcal F_{21}\delta\mathcal F_j),
\]

C 행도 동일한 구조다. 마지막 성분은

\[
\delta\dot z=\sum_j\left[
 \frac{\delta A_j C_j+A_j\delta C_j}{\mathcal F_j^2}
 -\frac{2 A_jC_j\delta\mathcal F_j}{\mathcal F_j^3}\right].
\]

F와 G의 선형 변분도 직접 구현한다. 따라서 조립 Jacobian이나 유한차분 JVP가
필요하지 않다. 정확한 tau 편미분에는

\[
\partial_\tau Q_j=2/r^2-2j(j+1)/r^3,
\qquad
\partial_r V=-2e^{-2d}(2+2/d+1/d^2)(r-R_0\mu)/d
\]

를 사용하고, partial_tau V=-partial_r V를 넣는다. 이는 고정 상태에서의
편미분이므로 F/G/q의 total derivative를 중복해서 포함하지 않는다.
RHS, JVP, partial_tau는 같은 고정 quadrature의 함수를 미분한다. quadrature cache는
정확한 r 비트와 immutable 계수에만 묶으며 상태나 JVP는 캐시하지 않는다.

## 오류 예산과 결과의 채택 범위

원래 1e-48 크기인 D2에 보통의 scalar atol을 직접 적용하면 그 성분의 수치 제어가
소실될 수 있다. 2^160 배율은 이를 O(1) 크기로 만든다. 현재 L28 요청의 atol=1e-12는
q 단위로 `1e-12/2^80`, D2 단위로 `1e-12/2^160`에 대응한다.
이 값들은 embedded **국소 추정자**의 scale이고, 전체 구간의 성분별 오차 보증은 아니다.
VigilODE WRMS는 모든 실수 상태를 함께 사용한다.

`scripts/phys69_vigilode.py`는 실제 반환 시각 2개와 각각의 정확한 상태 차원을 확인한다.
길이가 짧은 배열을 zip으로 잘라 비교하지 않는다. attempt ledger, JVP count와
조립 Jacobian/직접분해 count도 검사한다. L28 실제 결과의 오차는 기존
PHYS68 certificate SHA256
`ddaae206009a276def281af5526851ceb717baf2e0de5f8472552a9db340de9a`
의 dyadic midpoint/radius 및 증명된 radial tail에서 독립적으로 계산한다.
native binary64 값을 Fraction으로 정확히 읽고 정수 isqrt로 거리의 상하한을 구하므로,
이 후처리에는 새 Arb/Rust 적분이 필요 없다. 1e-6 상대오차를 사전 고정한 수용 기준으로 쓴다.
통과하면 **그 저장된 native D2 값의 참오차**가 제한되며, solver 전체를 인증하지 않는다.

## 적용한 Rust 패키지와 추가 후보

| 패키지 | 확인한 1차 자료 / 적용 | 범위 |
|---|---|---|
| VigilODE a21d573 | 기존 RODAS5P matrix-free U-form, GMRES `solve_into`와 LS workspace, PI controller를 실제 호출 | endpoint adaptive diagnostic. protected Arb 경로는 그대로 재사용 |
| num-complex **0.4.6** | [공식 API](https://docs.rs/num-complex/0.4.6/num_complex/)의 Complex64 사용 | 복소수 bilinear 산술. arbitrary precision/interval이 아님 |
| gauss-quad **0.3.2** | [공식 GaussLegendre API](https://docs.rs/gauss-quad/0.3.2/gauss_quad/struct.GaussLegendre.html), Bogaert O(n) node/weight 구현을 사용 | 기존 수작업 Newton node 생성과 다른 angular 구현. f64 node/weight 오차까지 인증하지 않음 |
| flint-sys **0.9.0** | [공식 FFI 모듈](https://docs.rs/flint-sys/0.9.0/flint_sys/)의 Arb/acb/Coulomb 연결 가능성 확인 | bundled C FLINT를 빌드하는 추가 native 의존성. 현재 인증은 이미 설치·검증된 python-flint/FLINT로 유지 |
| rug | [공식 자료](https://docs.rs/rug/)의 MPFR/MPC/GMP 기반 correctly-rounded 다중정밀도 | 고정밀 산술만으로 자동 ODE enclosure가 되지 않는다. 이번 binary64 대조에 불필요한 native build를 추가하지 않음 |
| Diffsol **0.17.1** | [공식 API](https://docs.rs/diffsol/0.17.1/diffsol/)의 JVP, BDF/SDIRK/ERK 및 출력 quadrature 조사 | 원 요청의 VigilODE와 기존 Arb가 이미 서로 다른 계산경로를 제공하므로 이번 실행에 제3 ODE engine은 추가하지 않음. 백업 A07의 측정 버전은 별도 **0.16.1** |
| scirs2-special | [공식 README](https://github.com/cool-japan/scirs/blob/master/scirs2-special/README.md)의 Coulomb 기능 선언 확인 | 이 프로젝트의 eta_C, large-L 정규화와 인증 범위에서 적용 검증하지 않아 seed 대체에 채택하지 않음 |

VigilODE는 MIT, num-complex는 MIT/Apache-2.0, gauss-quad는 MIT/Apache-2.0다.
crate 버전과 registry checksum은 Cargo.lock에 고정한다. 전체 native source는
`native/phys69_vigilode/`에 있고 기존 PHYS68 파일은 변경하지 않는다.

## 계속 남는 과학 의무

이 native 적용의 대상은 finite-L external Born coefficient다. finite-L 바깥 angular
response, 원래 driven xi, 원점/incoming adjoint 및 sigma(E)/Maxwellian k_HH(T)의
완료 상태는 각자의 증명/실행에 따른다. PHYS63 질적 existence는 ESTABLISHED,
HH_R10은 OFF로 유지한다.
