# PHYS67: Coulomb 함수와 outgoing impedance의 실제 구간 인증

## 결과와 범위

고정된 `ell={0,20,21,28,64}`, `r/a0={27,55,65,75}`의 20개 점에서
Coulomb `H+=G+iF`, `d_r H+`, `Z=+d_r H+/H+` 및 `H+(r)/H+(27)`를
512-bit Arb/Acb 직사각형 구간으로 실제 계산했다. 각 입력은 정확한
정수·유리수에서 ball로 변환하며, 결과는 이진 midpoint와 radius를 정확한
mantissa/exponent로 저장한다. `POINT_CERTIFICATES.json`이 수치 근거다.

기존 `phys63_scaled_riccati.central_impedance`의 55자리 mpmath 계산에서
최종 반환된 complex128 값을 동일한 20개 점의 구간과 비교했다. 해당
binary64의 두 성분은 `as_integer_ratio()`로 정확히 회수했다. 새 인증의
최대 오차 상한은 `8.387e-17 a0^-1`보다 작다. 이 상한은 출력값과 정확한
Coulomb impedance의 점별 차이에 적용된다.

| 실제 결과 | 전체 20점에 대한 엄격한 상한 |
|---|---:|
| Z 직사각형의 Euclidean 반경 | `<1.152e-100 a0^-1` |
| H(r)/H(27) 직사각형의 Euclidean 반경 | `<3.345e-101` |
| 기존 binary64 Z의 절대오차 | `<8.387e-17 a0^-1` |

이 decimal 상한들은 정확한 유리수와 저장된 dyadic 상한의 비교로 확인했다.
간단한 읽기용 `display` 필드의 표시 반경은 자릿수 축약 오차를 포함하므로,
그 값을 실제 계산 반경으로 읽지 않는다. 검산은 `VERIFICATION.json`에 있다.

특히 장벽 안쪽 `ell=64,r=27`에서

\[
Z_{64}(27)\simeq-2.24730477021993327253584217113
 +i\,1.33486572550249197408155081503\times10^{-51}\ a_0^{-1}
\]

이며 imaginary ball의 하한은 엄격하게 양수다. 작은 outgoing flux를
binary64의 real 부분에 더해서 저장하지 않고 실수·허수의 오차를 따로
보존한다. 마지막 식의 소수는 근삿값이며 인증 범위는 JSON의 dyadic ball이다.

## 고정 물리와 미분 convention

좌표는 `r=physical radius/a0`, `B=27`, `k=7/10`,
`E=49/200 Hartree`, `eta_C=-10/7`이다. 원래 screened Hamiltonian은

\[
h=-\frac12\Delta-\frac1r-
\left(1+\frac1d\right)e^{-2d},\qquad
d=|\mathbf x-(7/10)\hat{\mathbf z}|.
\]

이 단위에서 Coulomb 기준해의 radial equation은

\[
h_\ell''(r)+\left(k^2+\frac2r-
\frac{\ell(\ell+1)}{r^2}\right)h_\ell(r)=0.
\]

`rho=kr`를 사용하면 DLMF 33.2.1의 계수
`1-2 eta_C/rho-ell(ell+1)/rho^2`가 된다. 따라서 `d_r=k d_rho`이고
반환하는 Z에는 반드시 k가 한 번 들어간다. `eta_C`는 Coulomb 함수의
매개변수다. 기존 원천 변수 `eta=Fy`, `xi=Fy-phi`는 별개로 유지한다.
원래 NPZ SHA256 `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`를
`source_guard`로 확인했다. 이 해시는 입력 provenance를 고정한다.

## 계산식과 normalization 검사

DLMF 33.2.11–12와 33.4.4에 따라

\[
H_\ell^+=G_\ell+iF_\ell,\qquad
G_\ell\partial_\rho F_\ell-F_\ell\partial_\rho G_\ell=1,
\]

\[
\partial_\rho H_\ell^+=
\left(\frac{\ell+1}{\rho}+\frac{\eta_C}{\ell+1}\right)H_\ell^+
-\sqrt{1+\frac{\eta_C^2}{(\ell+1)^2}}H_{\ell+1}^+.
\]

이를 정확 유리수 입력에 대한 Arb 사칙연산·제곱근·Coulomb 평가로 계산한다.
`ell=64`의 미분에 필요한 `ell=65` 값은 recurrence 내부 보조값이다.
공개 certificate가 PHYS65의 finite-L 범위를 늘리지는 않는다.

Wronskian으로

\[
\operatorname{Im}Z_\ell(r)=\frac{k}{G_\ell^2+F_\ell^2}>0
\]

가 성립한다. 코드의 구간이 이 부호를 직접 분리하며, 회귀검사는 incoming
`H-=G-iF`의 `Im Z<0`와 구별한다. 또한
`Im Z*(F^2+G^2)`의 ball이 `7/10`을 포함하는지 검사하므로 부호뿐 아니라
`rho` 대 `r` 미분 scale도 확인한다.

두 번째 미분은 `arb_series([rho,1]).coulomb`의 2차 coefficient에서 얻는다.
`2 c_2+q c_0`가 0을 포함하는지 F와 G에 대해 확인했다. 같은 FLINT 내부
루틴을 공유할 수 있으므로 series와 recurrence의 일치를 독립 소프트웨어
검증이라고 부르지 않는다.

## 정의식 직접 미분에 의한 별도 산식

양의 real rho에서 DLMF 33.2.8의 phase와 power를 결합하면,
rho와 독립인 0이 아닌 상수 C에 대해

\[
H_\ell^+(\eta_C,\rho)=
C\,\rho^{\ell+1}e^{i\rho}U(a,b,-2i\rho),
\quad a=\ell+1+i\eta_C,\quad b=2\ell+2.
\]

여기서 principal branch의 `arg(-2i rho)=-pi/2`를 취한다.
`exp[-i eta_C log(2 rho)]`와 power에 있는 `rho^(i eta_C)`가 상쇄되어
남는 rho power가 `rho^(ell+1)`임을 확인한다. DLMF 13.3.22의
`d_z U(a,b,z)=-a U(a+1,b+1,z)`를 대입하면

\[
Z_\ell(r)=k\left[
\frac{\ell+1}{\rho}+i+
2ia\frac{U(a+1,b+1,-2i\rho)}{U(a,b,-2i\rho)}\right].
\]

이 식은 ell-shift Coulomb recurrence를 호출하지 않는 별도 산식이다.
실제 20점 모두에서 유한한 ball을 얻었으며 recurrence의 impedance ball과
겹친다. 두 산식의 특수함수 구현은 FLINT를 공통 기반으로 사용한다.
기존 mpmath 구현은 별도의 소프트웨어이며, 그 출력의 실제 오차는 위 ball
차이로 인증한다.

256-bit 예비 probe의 `ell=64,r=75`에서는 Tricomi U의 denominator ball이
0을 포함했다. 이는 그 정밀도·산식의 enclosure가 넓어서 생긴 수치 진단이다.
384-bit와 512-bit에서 denominator를 분리했으며 최종 receipt는 512-bit를
사용한다. 처음 실패와 수정 근거는 `VERIFICATION_FAILURES.json`에 보존했다.

## 정확한 출력과 binary64 오차

Acb의 complex ball은 원판이 아니라

\[
[m_R-r_R,m_R+r_R]+i[m_I-r_I,m_I+r_I]
\]

형태의 직사각형이다. 네 값은 각각 integer mantissa와 power-of-two
exponent로 저장한다. 읽기 함수의 Arb radius 생성은 한 radius ulp만큼
넓어질 수 있으며, 검사는 원래 저장한 rectangle의 포함을 요구한다.
문자열의 보이는 마지막 자릿수를 인증 endpoint로 사용하지 않는다.

정확히 저장된 binary64 값 `z_hat`와 정확한 수학값을 포함하는 rectangle Q에
대해 ball 연산으로 `z_hat-Q`를 구성한 뒤 `abs_upper()`를 취한다. 반환된
dyadic 값 e는 모든 `z in Q`에 대해 `|z_hat-z|<=e`를 만족한다. 이 절차에는
mpmath의 자기 추정 오차나 55자리 계산의 정확성 가정이 들어가지 않는다.

## 실행·검증·다음 연결

환경: Python 3.12.14, python-flint 0.8.0, FLINT 3.3.1; 정확한 Python 버전과
platform 문자열은 receipt에 있다. 20점+binary64 비교는 5.37초에 종료했고,
새 테스트 24개가 모두 통과했다. PHYS64 20건과 PHYS66 campaign은 실행하지
않았다. 실행 명령은 다음과 같다.

```bash
PYTHONPATH=src python research/hh_phys67_20261019/coulomb/run_certificate.py \
  --source research/hh_phys34_20261015/inputs/FROZEN_U_SUBSET.npz \
  --output research/hh_phys67_20261019/coulomb/POINT_CERTIFICATES.json
python -m pytest tests/test_phys67_coulomb_certificate.py -q
```

`outgoing_h_acb(ell,radius)`는 caller의 precision context를 유지하고
`Re(radius)>0`에서 analytic outgoing H+를 반환한다. 이 반평면 조건을
확인할 수 없으면 indeterminate를 반환하므로 validated complex quadrature가
원점·branch cut을 가로지르는 영역을 허용하지 않는다. 이것이 다음 radial
integration certificate에 제공하는 직접 계산 인터페이스다.

이번 subunit이 인증한 대상은 정확한 점의 Coulomb 특수함수와 저장된
binary64 impedance 오차다. 전체 ODE 적분 오차, angular 제외 sector,
원래 source-driven xi, origin/incoming adjoint matching, sigma(E),
Maxwellian k_HH(T)는 각각 자신의 다음 의무로 남는다. PHYS63의 확립된
all-angular 존재성과 PHYS65/66의 해석적 bound를 그대로 재사용하며
`HH_R10=OFF`를 유지한다. 게시·원격 backup·독립 최종 검토는 root의
통합 기록에서 실제 상태를 보고한다.

## 원전과 API 근거

- NIST DLMF 33.2: Coulomb equation, H+/H- normalization, U representation,
  Wronskian. https://dlmf.nist.gov/33.2
- NIST DLMF 33.4.4: ell-shift derivative recurrence.
  https://dlmf.nist.gov/33.4
- NIST DLMF 13.3.22: Tricomi U derivative.
  https://dlmf.nist.gov/13.3
- python-flint 공식 Acb 문서: rectangular enclosures, Coulomb tuple,
  Tricomi U, abs_upper. https://python-flint.readthedocs.io/en/latest/acb.html
- python-flint 공식 series 문서.
  https://python-flint.readthedocs.io/en/latest/arb_series.html
- Arb 공식 소개: rigorous ball arithmetic. https://arblib.org/

문헌·API 확인일: 2026-10-19. 웹 문서 latest 표기는 0.9.0이며 실제 실행한
0.8.0의 호출 서명·직렬화 규약은 현재 interpreter의 docstring과 실행으로
별도 확인했다. 웹 문서 버전과 실행 binary version을 혼동하지 않는다.
