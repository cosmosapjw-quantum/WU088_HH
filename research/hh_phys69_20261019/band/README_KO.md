# PHYS69: 새 intermediate j=29..36의 검증된 second-Born band

## 정확히 추가하는 계산

이 실행기는 PHYS68에서 완료한 j=0..28의 원래 물리 계산을 호출하지 않는다.
외부 채널은 ell=21, ellprime=20, m=0이며 새 중간 채널은 j=29..36이다.
16개의 대칭 pair와 Coulomb mode 집합 {20,21,29,30,31,32,33,34,35,36}만 구성한다.
외부 채널 20,21의 Coulomb 함수를 평가하는 것은 새 16개 pair의 정의에 필요하다.
이 두 채널을 새 intermediate 합에 더하지 않는다.

고정 입력은 B=27, T=65, k=7/10, E=49/200 Hartree이며 원래 screened potential과
frozen NPZ SHA256 `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`를 보존한다.
half_width=1/4, zero_free_radius=1/2, majorant_radius=2, Taylor degree=96,
Arb precision=512 bits, angular coefficient precision=1536 bits를 사용한다.
76개 panel 전체에 대한 새 band의 numerical absolute L1 error 목표는 1e-63이다.
`REQUEST_BAND_29_36.json`은 생략 필드 없는 실행 입력이다.

## 유도와 PHYS68의 재사용 범위

PHYS68의 정규화된 outgoing Coulomb 해를 F_j(r)=H_j^+(kr)/H_j^+(kB)로 둔다.
따라서 F_j(B)=1이다. 물리에서 eta=Fy, xi=Fy-phi와 Coulomb 매개변수
eta_C=-10/7은 서로 구별한다. m=0의 원래 V=2(1+1/d)exp(-2d)의 angular matrix를 V_ab라 한다.
새 pair마다

\[
K_{ab}(r)=F_a(r)F_b(r)V_{ab}(r),\qquad
q_{ab}(r)=\int_r^T K_{ab}(s)\,ds,
\qquad q'_{ab}=-K_{ab},\quad q_{ab}(T)=0
\]

를 사용한다. 그러면 D1_ab(r)=q_ab(r)/(F_a(r)F_b(r))이고,

\[
D^{T,[29,36]}_{2,21,20}(B)
=\sum_{j=29}^{36}\int_B^T
\frac{q_{21,j}(r)q_{20,j}(r)}{F_j(r)^2}\,dr.
\]

이 곱은 복소 bilinear 곱이다. 복소켤레를 삽입하지 않으며 lambda^2 계수에 추가 2를 곱하지 않는다.
F_21(B)=F_20(B)=1이므로 B에서 별도의 외부 정규화 계수를 적용하지 않는다.
`tests/test_phys69_band_profiles.py`의 독립 상수해 F_j=1, V_ab=상수는
q_ab(r)=V_ab(T-r), D2=Sum(V_21j V_20j)(T-B)^3/3을 직접 비교한다.
별도의 순허수 V 시험은 부호와 bilinear 정규화를 구별한다.

PHYS68에서 완료된 구현 `src/wu088_hh/phys68_profiles.py`의 Taylor/Cauchy/다항 적분,
complex ball 직렬화, outgoing Coulomb disk, exact angular Laurent coefficient,
오른쪽 경계 carry 검사를 재사용한다. 새 `build_band_panel`은 동일한 유효 적분 구성을
명시된 pair와 mode 집합으로 제한한다. 기존 PHYS68 파일의 바이트는 수정하지 않았다.
각 panel의 large disk R=2에서 K의 Cauchy bound를 얻고, rho=1/2에서 엄밀한
Coulomb zero-free lower bound가 양수인 경우에만 q_lj q_pj/F_j^2를 나눈다.

중심 c, 반폭 h에 대해 K의 N차 Taylor 다항식을 K_N이라 하면

\[
R_K \le M_K\frac{(h/R)^{N+1}}{1-h/R},\qquad
q(c)\in q(c+h)+\int_0^h K_N(t)dt+\{z:|z|\le hR_K\}.
\]

q의 small-disk majorant는 |q(c+h)|+(rho+h)M_K(rho)이다. 따라서 second-Born
integrand의 majorant는 M_q(21,j) M_q(20,j)/lower(F_j)^2이고, panel 적분 나머지는
2h M_integrand (h/rho)^(N+1)/(1-h/rho) 이하이다.
Arb가 Taylor coefficient, angular coefficient, Coulomb evaluation, upstream carry,
다항식 연산 및 적분의 반올림을 함께 포함한다. 최종 보고 오차는 복소 ball의 두 component
radius를 정확한 dyadic rational로 더한 L1 값이다. decimal display는 증명의 입력으로 사용하지 않는다.
q는 q(T)=0인 analytic primitive로 이어지므로 마지막 panel의 Cauchy disk에서도 원래 K를
사용한다. T 밖에서 K를 불연속으로 영 처리하지 않는다.

## 실행 및 재개 계약

`ENGINE_BINDING_BEFORE_EXECUTION.json`은 새 source/CLI, 재사용한 PHYS68 수치 소스,
공통 process wrapper, Python/FLINT runtime과 frozen 원자료 SHA를 묶는다.
`run_j29_36_t65/REQUEST.json`의 동일 fingerprint에서만 `--resume`을 허용한다.
각 panel은 payload SHA, panel index/center, 전체 새 intermediate/Coulomb mode 집합,
필요 pair 집합 및 이전 q_left 직렬화의 SHA와 묶인다. 복원된 q_right box는 이전 q_left를
엄밀히 포함해야 한다. Arb magnitude 복원의 outward rounding을 허용하면서 원래 저장된
경계 바이트의 hash를 유지하는 PHYS68의 수정된 carry 규칙을 그대로 사용한다.

새 reader는 dyadic mantissa/exponent의 bool과 float를 거부한다. `int(1.9)` 같은 절삭을
사용하지 않는다. 실제 물리 계산 전에 새 제조해·계약 시험 36/36개를 통과했다.
시험 영수증은 `tests/RECEIPT.json`이며 이전 물리 실행이나 이전 전체 test suite를 반복하지 않았다.

`run_j29_36_t65`는 이 스레드에서 이미 완료되었다. NCP에서는 다음 명령으로 보존된 결과를
읽기 검증한다. 이 검증기는 Python 표준 라이브러리만 사용하며 원래 certificate와 panel을 쓰지 않는다.

```bash
python research/hh_phys69_20261019/band/verify_saved_band.py
```

완료된 디렉터리에는 실행기 `--run --resume`을 적용하지 않는다. `--max-new-panels 0`을
붙여도 결과를 다시 합산하고 CERTIFICATE.json의 실행 메타데이터를 갱신하므로 보존된 certificate
SHA가 바뀐다. 완성본에는 위 검증기와 root의 별도 all-angular 조합 읽기 검증을 사용한다.

다음 완성된 재개 인터페이스는 정확히 같은 fingerprint의 **PARTIAL_CHECKPOINT**가 남았을 때만
사용한다. 현재 완료본에 적용할 NCP 실행 지시가 아니다.

```bash
python scripts/phys69_band_profiles.py \
  --request research/hh_phys69_20261019/band/REQUEST_BAND_29_36.json \
  --out EXISTING_PARTIAL_CAMPAIGN_DIRECTORY \
  --run --resume \
  --wall-seconds 240 --memory-gib 4 --ncp-limits
```

`--run`은 한 child만 시작하며 240초 wall cap,
4 GiB Linux RLIMIT_AS, BLAS/OpenMP thread 1을 적용한다. NCP에서 solver를 새로 설계할 필요가 없다.

## Certificate의 정확한 의미

`PHYS69_FINITE_T_BAND_CERTIFICATE_V1`의 `D2_B_cutoff`는 새 j29..36의 finite-T band이다.
`D2_numerical_absolute_error_l1`는 문자열 numerator/denominator로 기록한 정확한 유리수이다.
이 결과 자체에 radial cutoff error나 j>36 angular error를 넣지 않는다.
full_intermediate_sum은 [29,30,31,32,33,34,35,36]이고 전체 0..36을 뜻하지 않는다.

전체 second-Born m0 entry의 조합은 root의 별도 인증에서 PHYS68의 저장된 finite-T cutoff와
이 새 band cutoff를 정확히 더한 다음, 두 numerical error와 하나의 공통 PR115 L64/T65
radial error bound 및 새 j>36 angular bound를 더한다. PHYS68의 이미 확장된 full-radial box를
조합 입력으로 쓰면서 radial error를 다시 더하지 않는다.

원래 source-driven xi, 원점 및 incoming adjoint, 모든 고차 Born response, sigma(E),
Maxwellian k_HH(T)를 이 band의 성공으로 인증하지 않는다. PHYS63의 질적 존재는 ESTABLISHED를
유지하며 HH_R10은 OFF이다. Git 게시, 클라우드 백업, NCP 제출과 전체 DAG 판단은
별도 root 영수증으로 기록한다.
