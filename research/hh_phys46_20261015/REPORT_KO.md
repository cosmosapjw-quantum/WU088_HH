# WU088_HH PHYS46: 21채널 screened Coulomb outgoing Volterra 수렴의 구성적 증명

2026-10-15 KST. Parent: [PHYS45 draft PR #84](https://github.com/cosmosapjw-quantum/WU088_HH/pull/84),
commit `b3f9d4cb228b8800cc72beef05a0d33f0a249ff9`.
요청 연구 단계: R5 이론 유도, C5 구현, C6 물리·코드 검증, C7 CAS,
C8 성능 및 `rei_bianchi` 전달 적합성, 게시 및 양대 클라우드 이중백업.
User-requested local Codex: NOT_USED; native subagent: NOT_RUN (실제 dispatch 도구 없음).

## 1. 물리학적 경계, source-lock, 다음 대상

원래 one-electron frozen spectator H(1s)+H(1s) Hamiltonian:
\[
h=-\frac12\Delta-\frac1r-\left(1+\frac1s\right)e^{-2s},\quad
s=|\mathbf r-R\hat{\mathbf z}|,\quad R=\kappa=\frac7{10}.
\]
전자 공간은 Euclidean, \(a_0\)와 \(E_a=2I_0\)의 고정 원자 단위를 쓴다.
원래 \(\eta=Fy,\ F=e^{e^{-s}},\ \xi=Fy-\phi\),
\(\phi=e^{-r}/\sqrt{\pi}\)를 바꾸지 않았다.
원본 binary64 21 partial-wave/6 radial-panel ×11 node = 1386
complex128 파일 SHA256
`f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`.
기존 PHYS43 truncated annulus \(\|\mathcal R_D\|_{(H_0^1)^*}
\le0.917114942873\)의 인증을 변경하지 않았다.
PHYS45 \(r\ge20\) full angular \(2\int\|S\|dr
\le1.8120565\times10^{-17}\) 증명은 상속한다.
원본 atomic supply \(I_0=13.605693122990\,{\rm eV}\)와
consumer \(\chi_H=13.598434599702\,{\rm eV}\)는 분리하며
\(c,\hbar,k_B\), gas-frame proper seconds는 부적절하게 버리지 않는다.

이번 정리는 **raw physical homogeneous radial Schrödinger
\(\ell=0,\ldots,20\), \(m=0\) Galerkin projection에 한정**된다.
이것은 \(\eta=Fy\)의 transformed-D residual이나
실제 nonzero driven incident \(\xi\) source가 아니다.
초기/최종 state의 무한 angular hierarchy를 새로 인증했다고도
주장하지 않는다. 이 경계가 향후 정확한 microscopic
\(\sigma(E)\), \(k_{\rm HH}(T)\)를 공급하기 위한 필수 분리다.

## 2. Outgoing Green kernel과 Schrödinger의 정확한 부호

각 \(\ell\)의 base radial Coulomb operator는
\[
\mathcal L_\ell=\partial_r^2+q_\ell(r),\quad
q_\ell(r)=\kappa^2+\frac2r-\frac{\ell(\ell+1)}{r^2},
\qquad \kappa=\frac7{10}.
\]
\(H_\ell^\pm(r)=H_\ell^{(\pm)}(\eta_C,\kappa r)\),
\(\eta_C=-1/\kappa=-10/7\).
Wolfram/NIST의 \(H_\ell^+=G_\ell+iF_\ell\),
\(H_\ell^-=\overline{H_\ell^+}\) convention에서
\[
W_r(H_\ell^+,H_\ell^-)=-2i\kappa.
\]
따라서 \(r\le t\)의 정확한 real-valued retarded radial kernel:
\[
\boxed{K_\ell(r,t)=
\frac{H_\ell^+(r)H_\ell^-(t)-H_\ell^-(r)H_\ell^+(t)}
{2i\kappa}.}
\]
즉 \(K_\ell(t,t)=0\),
\(\partial_rK_\ell(t,t)=1\),
\(\mathcal L_{\ell,r}K_\ell(r,t)=0\) for \(r<t\).
따라서
\[
\mathcal L_\ell\int_r^\infty K_\ell(r,t)f(t)\,dt=-f(r).
\]
원래 \(+2S\) 가 들어간 물리 radial equation
\[
U''+\operatorname{diag}(q_\ell)U+2V_{21}(r)U=0
\]
의 outgoing Volterra equation은
\[
\boxed{
U(r)=D_H(r)+\int_r^\infty
 \operatorname{diag}(K_\ell(r,t))\,2V_{21}(t)U(t)\,dt,
\quad D_H(r)=\operatorname{diag}(H_\ell^+(r)).
}
\]
PHYS45에서 동일 원본 potential \(S(s)\)의 normalized
angular compression \(V_{21}\)를 엄밀 계산했으며,
모든 \(r\ge20\)에서
\(\|V_{21}(r)\|_{2\to2}\le(1+(r-R)^{-1})e^{-2(r-R)}\).
\(H_\ell^\pm\)의 절댓값은 같으므로
\[
|K_\ell(r,t)|\le
\frac{|H_\ell^+(r)|\,|H_\ell^+(t)|}{\kappa}.
\]
Green 부호, Wronskian current와 대각점 jump를 local Wolfram15와
독립 Python/mpmath에서 확인했다. 단일 산란 source/observable
계약은 이 수학적 Green operator와 분리한다.

## 3. 모든 원본 retained 21모드에 공통인 rigorous Coulomb envelope

\(T=31a_0\)를 먼저 실제 후보로 선택했다고 가정하지 말고,
\(T\in\{29,30,\ldots,40\}a_0\)를 exact-rational sweep으로 비교한다.
임의의 \(0\le\ell\le20\), \(r\ge T\)에서
\(q_\ell(r)\ge q_*:=q_{20}(T)>0\)
(\(q_\ell'(r)=2[\ell(\ell+1)-r]/r^3\);
각 \(q_\ell\)은 하나의 극대점만 갖고 내부 극소점을 갖지 않음).
또한
\[
\int_T^\infty |q_\ell'(r)|dr
\le\frac2T+\frac{420}{T^2}=v_*.
\]
복소 Coulomb outgoing radial solution의 양의 에너지
\[
\mathcal E_\ell(r)=|H_\ell'|^2+q_\ell(r)|H_\ell|^2
\]
는 \(\mathcal E_\ell'=q_\ell'|H_\ell|^2\).
\(H_\ell^+(r)\sim
\exp[i(\kappa r-\eta_C\log(2\kappa r)-\ell\pi/2+\sigma_\ell)]\),
\(\mathcal E_\ell(\infty)=2\kappa^2\)이므로
\[
\mathcal E_\ell(r)
\le2\kappa^2\exp(v_*/q_*).
\]
따라서 모든 \(r\ge T\)에서
\[
|H_\ell|^2+|H_\ell'/\kappa|^2
\le2\kappa^2\exp(v_*/q_*)
\left(\frac1{q_*}+\frac1{\kappa^2}\right)=:A_T^2.
\]
\(\exp(v_*/q_*)\)는 72항의 **정확한 양의 rational
Taylor polynomial과 양의 geometric tail remainder**로 상계한다.
\(M_T\)를 정수로 선택해 \(M_T^2>A_T^2\)를
Fraction comparison으로 증명한다. 최적 정수 반경 \(T=31\)에서
\[
q_*=\frac{11289}{96100},\quad
v_*=\frac{482}{961},\quad
v_*/q_*=\frac{48200}{11289},\quad
A_T^2<739.445441693<28^2.
\]
\(B=20\le r\le T\)에서 상태 벡터
\(X=(H_\ell,H_\ell'/\kappa)^T\)는
\(X'=\begin{pmatrix}0&\kappa\\-q_\ell/\kappa&0\end{pmatrix}X\).
이 구간에서는 \(-0.46\le q_\ell(r)\le0.59\),
따라서 Euclidean operator norm은 모든 \(0\le\ell\le20\)에서
\[
\|A_\ell(r)\|_2\le c:=\frac{59}{70}.
\]
Gronwall을 뒤로 적용하면 양의 가중 함수
\[
\boxed{
w_T(r)=\begin{cases}
M_T e^{c(T-r)},&20\le r\le T,\\
M_T,&r\ge T
\end{cases}
}
\]
는 \(|H_\ell^+(r)|\le w_T(r)\),
\(|H_\ell^{+\prime}(r)|/\kappa\le w_T(r)\)를
모든 retained 21모드에 대해 보증한다.
무한한 \(\ell\rightarrow\infty\)에서는 \(c\)와 \(M\)
이것 그대로를 사용할 수 없다. 이것은 **유한 원본 채널 정리**다.

## 4. 구성적인 Volterra contraction과 finite outgoing DtN

Banach matrix-function norm
\[
\|U\|_w=\sup_{r\ge20}
\frac{\|U(r)\|_{2\to2}}{w_T(r)}
\]
에서 각 Green kernel의 diagonal matrix norm과
원래 screened angular matrix 상계를 결합하면
\[
\|\mathcal KU\|_w\le Q_T\|U\|_w,\quad
Q_T=\frac2\kappa\int_{20}^{\infty}
w_T(t)^2(1+(t-R)^{-1})e^{-2(t-R)}dt.
\]
\(d=B-R\), \(c=59/70\)로 놓고
\(1+(t-R)^{-1}\le1+d^{-1}\)를 사용하면
\[
\boxed{
Q_T\le\frac{M_T^2}{\kappa}(1+d^{-1})
\left[
\frac{e^{-2d+2c(T-B)}}{1+c}
+e^{-2(T-R)}
\right].}
\]
우변의 두 exponential은 각기 192항 reciprocal positive
exp-Taylor 포함구간으로 **위쪽에서** 평가한다.
\(T=31\), \(M_T=28\)일 때
\(-2d+2c(T-B)=-702/35\),
\(-2(T-R)=-303/5\)이므로
\[
\boxed{\|\mathcal K\|_w
\le 0.000001244396026504989795\equiv Q<1.}
\]
12개 \(T=29,\ldots,40\) 중 이 명시적 유리수 energy-envelope
후보군에서 \(T=31\)이 최선이다. 모든 실수 \(T\)에 걸친
전역 최적화라는 주장은 하지 않는다.

Banach 고정점 정리로 유한 21채널 **동차**
screened-outgoing Volterra Jost matrix \(U\)는 존재·유일하고
Neumann series는 수렴한다. 정규화된 해
\(U_0=D_H\)는 \(\|U_0\|_w\le1\)이므로
\[
\|U-U_0\|_w\le\alpha:=\frac{Q}{1-Q},\quad
\boxed{\alpha\le1.244397575028387552\times10^{-6}.}
\]
Neumann series에서 1차 Born까지 포함한 나머지는
\[
\left\|U-U_0-\mathcal K U_0\right\|_w
\le\frac{Q^2}{1-Q}
\le1.548523397758\times10^{-12}.
\]
이 bound는 실제 radial quadrature 없이 엄밀하게 유지되며,
물리적 source-to-cross-section bound는 아니다.

\(D=D_H(B)\),
\(D'=\partial_r D_H(B)\)라 하면
\(U(B)=D(I+E)\),
\(U'(B)=D'(I+E')\),
\(\|E\|_2,\|E'\|_2\le\alpha\).
후자의 bound도 Coulomb Wronskian으로 \(D'_l\ne0\)와
\(|K'_l(B,t)/H_l^{+\prime}(B)|\le|H_l^+(t)|/\kappa\)
를 사용해 도출한다. \(\alpha<1\)이므로
\(\det U(B)\ne0\). 따라서 원래 retained homogeneous
outer problem의 outgoing DtN \(Z^{21}(B)=U'(B)U(B)^{-1}\)
는 실제로 잘 정의된다.

\(Z_C=D'D^{-1}\)는 PHYS44의 diagonal Coulomb reference다.
\[
\boxed{
\|D^{-1}[Z^{21}-Z_C]D\|_2
\le\frac{2\alpha}{1-\alpha}\,
\max_{0\le\ell\le20}|Z_{C,\ell}(B)|,
}
\]
여기서 **엄밀한 계수**
\(2\alpha/(1-\alpha)\le
2.488798247111278544\times10^{-6}\).
이것은 similar-to-\(D\) normalized 경계 비교식이지,
기저변환 없는 \(Z-Z_C\) norm의 같은 숫자가 아니다.
\(\max|Z_{C,\ell}|\)는 정확한 Coulomb function으로
정의된 기준값이다. 본 결과를 아직 infinite-\(\ell\)
physical outgoing DtN이나 \(\xi=Fy-\phi\)의 비동차
surface law로 승격하지 않았다.

## 5. 원래 angular coupling을 사용한 독립 수치 확인

독립 비인증 1차 Born 미리보기:
- radius 구간 \([20,31]\), \([31,43]\), \([43,55]\)에
  각각 24,24,16개의 Gauss radial nodes, 192개의 angular nodes.
- \(\ell=0\ldots20\) Coulomb \(H^+=G+iF\), 고정 원래
  screened full \(21\times21\) \(V_{\ell m}(r)\)를
  42자리 mpmath special functions + NumPy angular quadrature로 계산.
- 실제 source-locked, 그러나 **quadrature는 엄밀하지 않음**.
- 정규화된 1차 Born 경계 변화
  \(\|D^{-1}\delta U(B)\|_2\approx
  7.7816000351\times10^{-18}\),
  \(\|D'^{-1}\delta U'(B)\|_2\approx
  5.6873466283\times10^{-17}\).
- 1차 Born으로 만든 similarity-normalized DtN 차이:
  약 \(1.4635290725\times10^{-17}\).
- 이 수치들은 rigorous \(Q\), \(\alpha\)보다 작고
  screened exterior의 작음을 보여주지만 **구간적분의
  전역 검증으로 사용되지 않는다**.
- Actual source-bound NEUMANN remainder의 가장 날카로운
  보존 값은 상기 \(1.548523397758\times10^{-12}\)다.

## 6. 수학적 Wolfram/검증 및 CPU 최적화

실제 Wolfram Language 15 및 독립 plugin:
- 정확한 \(q_*,v_*,v_*/q_*\), \(\beta_1,\beta_2\);
- \(A_T^2<28^2\) 및 \(Q<1/2\) 수학적 검산;
- \(\ell=0,5,15,20\)에서 outgoing Green diagonal zero,
  radial derivative jump +1, homogeneous ODE \(0\),
  outgoing flux Wronskian \(+\kappa\);
- 비가환 \(2\times2\) 표본으로
  \((I+E')(I+E)^{-1}-I=(E'-E)(I+E)^{-1}\)를 정확히 0 검산.
CAS exit code 0과 원 stdout을 저장했다.

Python targeted new **15/15 PASS**, whole WU package
**290/290 PASS**, pytest193.60s, process exit0.
코드 `src/wu088_hh/phys46_volterra.py`, 실행
`scripts/phys46_volterra.py`, 검사
`tests/test_phys46_volterra.py`,
`scripts/phys46_born_preview.py`,
`scripts/phys46_benchmark.py`,
`scripts/phys46_plot_bounds.py`가 원래
input SHA를 읽고 동일 계산을 재현한다.

12개 patch search의 실제 30회 serial 중앙 wall
\(0.00671123\)s, 이미 인증된 \(T=31\)
single-patch exact recomputation \(0.00103899\)s:
**6.46×** 동일 수렴계수/모형의 빠른 추후 재검산.
동일 전체 후보를 2-worker forkserver로 실행하면
process startup이 커서 중앙 wall \(0.101691\)s,
따라서 이 미시커널에서는 **1-worker가 더 경제적**이다.
이 값은 전체 원래 H-H scattering solver,
`rei_bianchi` native solver 또는 H/He 이력의 CPU 가속이 아니다.

실제 환경 Python3.12.3, NumPy2.4.2, SciPy1.17.0,
pytest9.1.1. 선언된 NumPy pin 2.3.5와 다름을 명시한다.

## 7. 최신 rei_bianchi 및 source-admission 경계

공개 최신 [rei_bianchi PR134](https://github.com/cosmosapjw-quantum/rei_bianchi/pull/134)
(원본 C12 crossrepo intake)은 이미 **WU088_HH PR83
기존 source guard**를 사용했고, 예상대로 외부
`HH_R10`을 승인하지 않았다. [PR135](https://github.com/cosmosapjw-quantum/rei_bianchi/pull/135)는
별개로 사용자의 표준
\(\Sigma=|\sigma|/H\), radiation/matter
anisotropic stress \(\pi_{ab}\)를 도입하는 실제
Einstein-background 연구다. 이 물리 input과
원자 \(\sigma(E)\) 또는 electron collision rate를
서로 혼동하지 않는다.

현재 로컬 원본 consumer checkout
`/home/cosmosapjw/Dropbox/bianchi/rei_bianchi`
HEAD `0fcb2dddf5de6b583c2e00f150abff0b2afb6315`
은 위 공개 PR134·135 각각과 다른 revision이다.
로컬 `rust/rei_microphysics/src/coverage.rs`의
`HH_R10` EXCLUDED, `NO_EXTERNAL_PHYSICAL_SOURCE_ADMITTED`
상태가 그대로다.
이번 finite21 *homogeneous exterior* Jost 정리만으로는
\(\sigma(E)\), \(\langle\sigma v\rangle\), 입사 \(1s\) source,
동일 입자 대칭인자 1/2, Maxwellian
\(k_{\mathrm{HH}}(T)\), gas-frame source ownership과
시간축이 증명되지 않는다.
따라서 **REI에서 실수치 \(q_{\rm HH}\),
\(\dot T_{\rm HH}\), \(\dot n_e\)를 생성하지 않았고,
HH production은 OFF**다.

## 8. 문헌·다음 구성적 의무

참고 선행연구:
- [Volkov et al., Potential splitting approach to multichannel Coulomb scattering](https://arxiv.org/abs/1102.0549).
- [Jost function for coupled channels](https://arxiv.org/abs/nucl-th/9808034).
- [NIST DLMF 33.2 Coulomb functions and Wronskians](https://dlmf.nist.gov/33.2),
  [DLMF 33.4 recurrence](https://dlmf.nist.gov/33.4).
이 문헌들은 Coulomb asymptotics, multichannel Jost 구성,
상호작용 분리의 이론적 배경이다. 본 정리의 **유리수
source-locked 수치상계와 채택된 21채널 범위**는
이번 직접 유도·테스트한 결과다.

다음 DAG는 단순 메타감사가 아니라
**(i)** \(\ell>20\) centrifugal barrier와 Coulomb amplitude에
대한 연속 angle-weighted norm/analytic high-\(\ell\) envelope를 구성해
PHYS46의 finite21 수렴조건을 physical infinite-dimensional
problem으로 확장,
**(ii)** 실제 비동차 \(\xi=Fy-\phi\)와 원점 정칙 extension을
원래 source 위에서 결합,
**(iii)** incoming adjoint, microscopic cross section and rate,
**(iv)** 물리적 `rei_bianchi` proper-time event/thermodynamic
reaction ownership을 승인받는 순서다.

**현재 과학 판정**:
`RIGOROUS_FINITE21_OUTGOING_JOST_CONTRACTION` 및
`SOURCE_LOCKED_ORIGINAL_COULOMB_AND_SCREENING` 성립.
`INFINITE_ANGULAR_OPERATOR/DRIVEN_SOURCE/PHYSICAL_RATE`는
명시적 후속 연구 의무로 HOLD.
원래 REI owner data, AX08 science solver와 온도 이력,
Git source production은 하나도 변경하지 않았다.
