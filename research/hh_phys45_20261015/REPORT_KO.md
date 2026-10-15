# WU088_HH PHYS45: screened two-centre 외부 angular coupling과 rei_bianchi 전달용 엄밀 상계

2026-10-15 KST. Parent: [PHYS44 draft PR83](https://github.com/cosmosapjw-quantum/WU088_HH/pull/83),
commit `4b36f178d5effa2ccf960d5285372f2f51d21327`.
선택한 작업은 R5 구성적 유도 + C5–C8 실제 원본 구현·검산·최적화 및
`rei_bianchi` source 적용성 read-only intake다. Local Codex와 native
subagent 모두 사용하지 않았다. 다른 owner source/과학 solver를 수정하지 않았다.

## 1. 원래 물리, 적분 및 출처

고정 H(1s)+H(1s) one-electron spectator Hamiltonian은
\[
h_\lambda=-\frac12\Delta-\frac1r-\lambda S(s),\quad
S(s)=\left(1+\frac1s\right)e^{-2s},\quad
s=|\mathbf r-R\hat z|,\quad R=\kappa=7/10,\quad\lambda=1.
\]
길이 \(a_0\), 에너지 \(E_a=2I_0\)이고 전자 3차원은 Euclidean이다.
원래 \(\eta=F y,\;F=e^{e^{-s}},\;\xi=Fy-\phi\)와
\(\phi=e^{-r}/\sqrt\pi\)를 변경하지 않는다. 이 둘의 외부 경계는
PHYS44에서 구분했다. 원본 frozen NPZ에는 \(\ell=0,\dots,20\)의
21 partial waves, 6 radial panels, 11 nodes/panel 등 총 1386 complex128
값이 있으며 SHA256
`f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`.
Source는 반드시 byte-identical이어야 한다.
PHYS43의 잘린 annulus full-\(H_0^1\) dual transformed-D bound
\(0.917114942873\)은 별도로 유지한다.
원자 공급 \(I_0=13.605693122990\) eV와 receiver heat
\(\chi_H=13.598434599702\) eV는 다른 수치/잎이며,
\(c,\hbar,k_B\) 역시 consumer conversion 없이 버리지 않는다.
우주론 signature는 (-,+,+,+)다.

\(r>R\)에서 정규화한 \(Y_{\ell0}=\sqrt{(2\ell+1)/(4\pi)}P_\ell(\mu)\)를
쓰고 실제 물리적 screened angular matrix를 정의한다.
\[
V_{\ell m}(r)=\int_{S^2}Y_{\ell0}(\Omega) S(s)Y_{m0}(\Omega)\,d\Omega,
\quad
s^2=r^2+R^2-2rR\mu.
\]
\(\mu(s)=(r^2+R^2-s^2)/(2rR)\),
\(d\mu=-s\,ds/(rR)\)로부터
\[
\boxed{
V_{\ell m}(r)=\frac{\sqrt{(2\ell+1)(2m+1)}}{2rR}
\int_{r-R}^{r+R}P_\ell(\mu(s))P_m(\mu(s))
(1+s)e^{-2s}\,ds.
}
\]
따라서 Legendre는 \(s^2\) 다항식이고 적분항은
\(\int s^{2j}e^{-2s}ds+\int s^{2j+1}e^{-2s}ds\)의
양의 primitive moment로 나뉜다. 기존 PHYS39의
`power_exponential_moment`를 새 \(s^0\) 분모 없는 항에도
동일 조건으로 적용했다. 지수함수는 320항 positive Taylor
reciprocal과 정확한 geometric remainder의 **외향 유리수**
구간이며, \(\sqrt{(2\ell+1)(2m+1)}\)은 정수제곱근의
정확한 포함구간으로 처리한다.

Yukawa potential \(g_\alpha(s)=e^{-\alpha s}/s\)에 대해
\[
S(s)=[1-\partial_\alpha]g_\alpha(s)|_{\alpha=2}
\]
도 정확하다. 이 생성식은 screened-potential multipole
addition theorem과의 연결을 보여주지만, 이번 certified
행렬은 multipole truncation approximation이 아니라
**원래 단일 \(r\)의 \(Y_{\ell0}\) projection 정확한 적분**이다.
행렬은 대칭이고 \(S(s)>0\)이므로 원래
\(\{Y_{00},\ldots,Y_{20,0}\}\) 위에서는 양의 definite 이차형식이다.
이는 실수행렬 원소가 모두 양수라는 주장과 다르다.

## 2. 새로운 all-angle operator 상계와 high-\ell 잔여

\(r\ge B=20\), \(d=r-R\)에서
\[
0<S(r,\mu)\le S(d)
=(1+d^{-1})e^{-2d}.
\]
정규 직교각도 투영이 수축하므로,
\[
S(r+R)\,I\preceq V(r)
\preceq S(r-R)\,I
\]
는 임의 finite angular compression에도 성립한다.

\(S'(s)=-e^{-2s}(2+2/s+1/s^2)<0\),
\(S''(s)=e^{-2s}(4+4/s+4/s^2+2/s^3)>0\)이므로
감소하고 **볼록**하다. 이는 중심 대각항
\(S(r)I\)를 제거한 다음의 무한 angular Hilbert-space 상계를
제공한다.
\[
\boxed{
\|M_{S(r,\mu)}-S(r)I\|_{\rm op}
=\sup_{\mu}|S(s)-S(r)|
=S(r-R)-S(r).
}
\]
여기서 \(M_S\)는 전각도 곱셈 연산자다. 그래서
\[
\boxed{
\int_{B}^\infty 2\|M_S-S(r)I\|_{\rm op}\,dr
\le (1+(B-R)^{-1})e^{-2(B-R)}-e^{-2B}.
}
\]
증명은 첫 항에서 \(1+(r-R)^{-1}\le1+(B-R)^{-1}\),
둘째 항에서 \(S(r)\ge e^{-2r}\)를 사용하는
양의 적분 구간 분할이다.
같은 계산으로 full \(2M_S\)의 radial-\(L^1\) 상계는
\[
\int_B^\infty 2\|M_S\|_{\rm op}\,dr
\le (1+(B-R)^{-1})e^{-2(B-R)}.
\]

특히 임의 \(m\)에 대해 \(P_{\ell\le20}\)와
\(Q_{\ell>20}=I-P\)를 쓰면,
\(Q_{\ell>20}S(r)P=0\)이므로
\[
\|Q_{\ell>20} M_S P_{\ell\le20}\|_{\rm op}
\le S(r-R)-S(r).
\]
이는 **21-wave truncated original \(y\)에서 exterior
potential이 유발할 수 있는 high-\ell coupling의
엄밀한 operator coefficient bound**다. 21-wave 외부 산란
해의 \(\ell>20\) 파동함수 오차 또는 그 DtN의 상계는 아니다.

고정된 \(B=20\)에서의 인증값:
- 전체 screened \(+2V\) radial-\(L^1\) upper
  **\(1.8120565\times10^{-17}\)**.
- 중심 대각항을 뺀 비중심 \(+2(V-S(r)I)\)
  radial-\(L^1\) upper **\(1.3872211\times10^{-17}\)**.
- 중심 성분 분리 없이 비교하면 두 숫자는 **서로 다른
  연산자**의 상계다. 새 수치는 바로 off-central Volterra
  remainder를 설정하는 데 유용하다.
- \(B=20\)에서 비중심 operator의 pointwise upper
  \(1.3659793\times10^{-17}\).
- 종전 Lipschitz-only \(+2\) off-central radial upper
  \(2.5401167\times10^{-17}\)보다 엄밀 convex refinement는
  더 날카롭다.

**중요한 열린 보조정리:** 실제 outgoing Coulomb-plus-screened
Green \(G_C\)의 weighted operator kernel norm을 아직
인증하지 않았다. 만약 적절한 함수공간에서
\(q=\|G_C(2V)\|<1\)을 별도로 증명하면
\((I+G_C2V)^{-1}=\sum_{n\ge0}(-G_C2V)^n\)의 수렴과
\(\le1/(1-q)\) inverse norm이 따른다. **작은
\(\int\|2V\|\) 숫자만으로 이 \(q\)가 작다고 말할 수 없다**.
중심 \(S(r)\)를 background에 흡수한다면
그에 맞게 Green도 먼저 바꿔야 한다.
이것이 다음 PHYS46의 핵심 실증 의무다.

## 3. 21×21 실제 인증 행렬과 독립 검산

Original frozen model의 \(r=20a_0\), \(m=0\), \(0\le\ell,m\le20\):
서로 다른 **231개의 symmetric entry**를 계산하고
21×21 양방향 **441개**를 exact outward decimal로 저장했다.
\(\ell\)이 큰 다항식의 \(s^2\) 계수는 상당한 cancellation을
수반하기 때문에 **192항 exponential enclosure는
\(\ell=20\)에서 지나치게 넓은 포함구간**을 만들었다.
256항 이상으로 올려도 scientific operator 정의는
변하지 않으며, 정밀도는 엄격히 tight해진다.
이번 공식 run은 320항/24 decimal digits다.

선택된 rigorously enclosed matrix entries (original atomic units):
| \(\ell,m\) | certified interval |
|---|---|
| 0,0 | [5.983632, 5.983633] × 10⁻¹⁸ |
| 0,1 | [4.329202, 4.329203] × 10⁻¹⁸ |

**인증된 전체 angular spectral enclosure**
\(S(20+0.7)\le\lambda(V)\le S(20-0.7)\)에서
\[
\lambda_{\min}\ge1.098241\times10^{-18},\qquad
\lambda_{\max}\le1.8120565\times10^{-17}.
\]
같은 \(21\times21\) float64 Gauss512에서
\(\lambda_{\min}\approx1.107923206879\times10^{-18}\),
\(\lambda_{\max}\approx1.796168617451\times10^{-17}\)을 얻었으나
후자는 **NONCERTIFYING numerical preview**다.

로컬 Wolfram15에서 Yukawa 생성식, \(S'\), \(S''\),
\(s\)-Jacobian, 적분 normalization 등
**6/6 exact scalar zeros**, 그리고
\((\ell,m)=(0,0),(0,1),(1,1),(5,5),(20,20)\)의
독립 WorkingPrecision54 angular `NIntegrate`를 실행했다.
각 값은 Fraction interval 내부에 있다.
별도 mpmath70dps로 여섯 pairs와 독립 \(\mu\) 적분을 시행했고
모두 동일 구간 내부였다. float64 Gauss128/256/512와
실제 441개 원소의 strict interval inclusion도 확인했다.
이 독립 실수값/float값이 rigorous proof 자체를 대체하지는
않는다.

실행 과학 파일:
- `src/wu088_hh/phys45_screened_exterior.py`:
  exact Legendre polynomial, positive exp moments, full matrix,
  all-angle positivity/spectral bounds, high-l coefficient norm.
- `scripts/phys45_screened_exterior.py`:
  source-locked original 1386 values, 320-term canonical run.
- `tests/test_phys45_screened_exterior.py`:
  strict original immutable SHA check, 6 mpmath direct \(\mu\)
  comparisons, whole matrix symmetry/PSD and negative controls.
- `src/wu088_hh/phys45_screened_preview.py`,
  `scripts/phys45_screened_preview.py`:
  separately labelled noncertifying float64 Gauss and
  two matched vectorization microbenchmarks.
- `scripts/phys45_plot_screened.py`와
  `results/PHYS45_*.png`: certified matrix 중심값과
  분석적으로 증명한 외향 envelope의 시각화.

## 4. 로컬 실제 성능 및 테스트

실제 Ubuntu Python3.12.3, NumPy2.4.2, SciPy1.17.0,
pytest9.1.1. NumPy는 `pyproject.toml`의
명시적인 `numpy==2.3.5`와 다른 환경임을 보존했다.
`OPENBLAS_NUM_THREADS=1` 등의 thread cap으로
진행 중인 독립 REI AX08 solver와 과도하게 경합하지 않았다.

엄밀 유리수 인증 21×21 전체: **1-worker wall 2.18 s**,
**2-worker wall 1.41 s**, 약 **1.55×** CPU parallel speedup.
모든 과학적 JSON field는 workers/time 메타데이터를 제외하면
동일했다. Worker별 몇 개의 positive exp moments를
다시 계산하는 비용 때문에 thread oversubscription 없이
짧은 계산에선 2-worker가 적합했다.

별도 float64 512-point Gauss, 21×21, **160 반복**:
벡터화 NumPy matrix multiplication 0.00455 s,
scalar pairwise 441 sums 0.34105 s, 약 **75×**.
동일 격자의 최대 행렬차는 \(5.39\times10^{-33}\).
이 속도향상은 **NONCERTIFYING special-kernel only**이며
원래 REI chemistry solver와 exact Fraction 인증의 전체
실행속도로 확대하지 않는다.

전체 프로젝트 실제 regression: **275/275 PASSED**,
pytest **168.39 s**, exit code **0**.
Wolfram 원래 의도한 Yukawa 생성식 첫 표현은
ReplaceAll 적용의 괄호 우선순위로 한 항이 실패했다.
이를 `g45=...`, `(g45-D[g45,...])/.lam->2`로
수정해 실제 6/6 정확한 0을 얻었다. 이 실패는
CAS_SCRIPT_PRECEDENCE_REPAIR이며 원래 물리
미분식의 REFUTATION이 아니다.
정식 run stdout과 resource JSON은 연구 results에 보존했다.

## 5. 최신 REI 원본과 machine-readable handoff

읽은 최신 공개 [rei_bianchi PR129](https://github.com/cosmosapjw-quantum/rei_bianchi/pull/129)
head `fa20d75e344a28c833a47cbca82315ccbbdf6882`는
HALF_MINUS 완료, signed four-case H/He parity와
실제 source-clock cancellation 수정 연구를 포함한다.
실제 사용자 로컬 owner checkout은 다른 HEAD
`0fcb2dddf5de6b583c2e00f150abff0b2afb6315`다.
둘을 동일 revision으로 보지 않았다.
다른 [SOURCE07 PR128](https://github.com/cosmosapjw-quantum/rei_bianchi/pull/128)
은 photoionization-only dynamic source compression으로
HH 충돌 ionization coefficient 공급원이 아니다.

PHYS44 read-only `coverage.rs` 결과
`HH_R10` EXCLUDED,
`NO_EXTERNAL_PHYSICAL_SOURCE_ADMITTED`를 그대로 유지한다.
이번 새 `scripts/phys45_rei_advisory.py`는
현재 local REI original source SHA/HEAD,
PHYS45 original 21-wave matrix SHA, 실제 all-\(\ell\)
screened tail, missing microscopic rate 조건을
machine-readable JSON에 연결한다. 실제
\(\sigma(E)\), physical ion-pair channel, identical-pair
factor, Maxwellian \(k_{\rm HH}(T)\), absorber/thermal
source ownership, proper-frame clock·density와 같은
**본질적으로 남은 물리 입력**은 여전히 null/HOLD다.
PHYS19 LCS thermal response와 PHYS45 microscopic
Coulomb scattering은 같은 물리 source가 아니다.
사용자 목적에 직접 필요한 것은 source 식을 억지로
활성화하는 것이 아니라, 정확한 microphysics rate의
구성과 그 REI 적용영역을 먼저 닫는 것이다.

## 6. 1차 문헌과 한정된 기여

관련 선행연구:
- R. Nozawa, *Bipolar Expansion of Screened Coulomb Potentials,
  Helmholtz' Solid Harmonics, and their Addition Theorems*,
  DOI [10.1063/1.1704834](https://doi.org/10.1063/1.1704834).
- S. L. Marshall (2002), *Spherical harmonic expansion of the
  Green function*, DOI
  [10.1088/0953-8984/14/12/308](https://doi.org/10.1088/0953-8984/14/12/308).
- Volkov et al., *Potential splitting approach to multichannel
  Coulomb scattering*, [arXiv:1102.0549](https://arxiv.org/abs/1102.0549).

이들은 screened/Coulomb multipole 및 driven scattering
문헌으로서 연구 경로를 뒷받침한다. 어느 문헌도 이
**특정 WU088_HH original frozen 1386 입력에 대한
엄밀 행렬값의 제3자 인증**인 것으로 표기하지 않았다.

이번 selected PHYS45 scope의 과학 판정:
**EXACT-RATIONAL MATRIX_CERTIFIED at r20, analytic all-angle
operator/radial-\(L^1\) envelopes DERIVED, original source
LOCKED, numeric preview INDEPENDENTLY_CHECKED**.
그러나 물리 outgoing solution은 결코
`GREEN_RESOLVENT_CERTIFIED`가 아니다.
다음 실질적 의무는 Coulomb outgoing Green kernel의
weighted norm과 shifted central Yukawa background의
Volterra contraction, \(\ell>20\) propagated tail 및
driven regular origin/incoming adjoint다. 이어서 channel
resolved \(\sigma(E)\), \(k_{\rm HH}(T)\) 및
`rei_bianchi` named proper-time source의 동일-family
조건을 확인한다.

**HH production OFF. REI solver/owner files untouched.**
GitHub Draft PR과 Dropbox/Google Drive 원본-byte 백업 영수증은
별도 게시·보존 기록에 남긴다.
