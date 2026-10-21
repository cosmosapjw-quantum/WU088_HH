# PHYS76: 조건부 연속시간 응답 구간과 저장 이력 진단의 연결

## 1. 정의와 과학적 기준

PR128의 `stress_memory.py`, `CONTRACT.json`을 기준으로 한다. 정규직교 normal frame에서
\(\sigma_{ab}=\operatorname{diag}(-s,-s,2s)\),
\(\pi^{(A)}_{ab}=\operatorname{diag}(-p_A,-p_A,2p_A)\), \(A=m,r\)다.
고유시간에서 \(H,s\)의 단위는 \(\mathrm{s}^{-1}\), \(p_A\)의 단위는 \(\mathrm{J\,m^{-3}}\),
\(K=8\pi G/c^2\)다. \(Kp_A\)는 \(\mathrm{s}^{-2}\)이므로
\(\dot s+3Hs=K(p_m+p_r)\)의 차원이 일치한다.

\[
x=\log(a/a_i),\quad S=\sqrt3\,s/H,\quad
P_A=\sqrt3 Kp_A/H^2,\quad q=-1-H'/H.
\]

따라서 \(S,P_A\)는 signed half-contraction 좌표이며,
\(\Sigma_h=|S|\), \(\Pi_{Ah}=|P_A|\)다.
Full Frobenius 값은 각각 \(\sqrt2\)배다.
총 응력의 norm은 \(\sqrt2|P_m+P_r|\)이며 두 norm의 합과 일반적으로 다르다.
두 성분의 상대부호와 같은 frame이라는 전제를 유지한다.

\(H>0\)인 구간에서 \(S\)를 미분하면

\[
S'=-(3+H'/H)S+P_m+P_r=-(2-q)S+P_m+P_r.
\]

아래에서는 계수와 species 첨자를 구별하기 위해 \(\alpha=2-q\)라 쓴다.
\(I(x)=\exp\int_{x_i}^x\alpha(v)\,dv=e^{3(x-x_i)}H(x)/H_i\)이고

\[
S(x)=S_i/I(x)+J_m(x)+J_r(x),\qquad
J_A(x)=I(x)^{-1}\int_{x_i}^x I(u)P_A(u)\,du.
\]

\(J'_A=-\alpha J_A+P_A\), \(J_A(x_i)=0\)다.
이는 실제 같은 coupled trajectory에 조건부인 선형 기여 분해다.
Species를 제거하여 배경과 source가 바뀌는 별도의 실험에는 해당하지 않는다.

## 2. 연속시간 구간 정리

한 cell \([x_n,x_{n+1}]\), \(h=x_{n+1}-x_n>0\)에서
\(\alpha,P_A\)가 가측·본질적으로 유계이고 거의 모든 점에서

\[
\alpha\in[\alpha_-,\alpha_+],\quad P_A\in[p_{A,-},p_{A,+}]
\]

라는 **전체 cell enclosure**가 독립적으로 주어졌다고 가정한다.
또한 \(J_A(x_n)\in\mathcal J_{A,n}\)라 하자.
\(\Phi(a,h)=\int_0^h e^{-au}\,du\)를 정의하면

\[
\Phi(a,h)=\begin{cases}(1-e^{-ah})/a&a\ne0,\\h&a=0,\end{cases}
\]

\[
\mathcal G=[e^{-\alpha_+h},e^{-\alpha_-h}],\qquad
\mathcal R=[\Phi(\alpha_+,h),\Phi(\alpha_-,h)]
\]

에 대해 다음이 성립한다.

\[
\boxed{\mathcal J_{A,n+1}=\mathcal G\mathcal J_{A,n}
                  +\mathcal R[p_{A,-},p_{A,+}]\ \ni J_A(x_{n+1}).}
\]

곱과 합은 signed 실수 구간 연산이다. 초기 기억에는
\(\mathcal D_{n+1}=\mathcal G\mathcal D_n\)를 사용한다.
총 signed shear는 \(\mathcal D_n+\mathcal J_{m,n}+\mathcal J_{r,n}\)에 속한다.
\(\alpha\)의 양성을 요구하지 않는다. 음수 구간에서는 응답이 증폭될 수 있다.

**증명.** 선형방정식의 절대연속 해는 variation of constants에 의해

\[
J_A(x_{n+1})=GJ_A(x_n)+
 \int_{x_n}^{x_{n+1}}\exp\!\left[-\int_u^{x_{n+1}}\alpha(v)\,dv\right]P_A(u)\,du
\]

로 표현된다. 적분 kernel \(g(u)\)는 양수이고
\(e^{-\alpha_+(x_{n+1}-u)}\le g(u)\le e^{-\alpha_-(x_{n+1}-u)}\)다.
따라서 \(G\in\mathcal G\), \(r=\int g(u)du\in\mathcal R\)이고 \(r>0\)다.
양의 가중평균 \(\bar p_A=r^{-1}\int gP_A\)는
\([p_{A,-},p_{A,+}]\)에 속하므로 적분항 \(r\bar p_A\)는
\(\mathcal R[p_{A,-},p_{A,+}]\)에 속한다.
이전 cell의 포함관계에 대한 귀납법으로 모든 node의 포함관계를 얻는다.
같은 \(\alpha\)에서 유래하는 \(G,r\)의 의존성을 구간 연산이 잊으면
범위가 넓어질 수 있으나 포함관계는 보존된다.

\(\partial_a e^{-au}=-u e^{-au}\le0\)이므로 \(\Phi\)는 실수 \(a\)에서 감소한다.
\(a\to0\) 극한은 \(h\)다. 이 두 성질이 위 endpoint 순서를 정한다.

## 3. Residual을 사용한 후속 의무

연속인 근사 \(\widehat J\)가 각 cell에서 절대연속이고
\(r=\widehat J'+\alpha\widehat J-P\)의 전체 cell enclosure가 있으면,
\(e=J-\widehat J\)는 \(e'=-\alpha e-r\)를 만족한다.
위 정리를 source \(-r\)에 적용하면 node error enclosure를 얻는다.
저장된 node 값으로 만든 piecewise-linear \(\widehat J\)도 사용할 수 있지만,
\(\alpha,P\) 또는 residual의 연속구간 bound는 별도로 제공되어야 한다.
샘플 잔차와 coarse/fine sampled quadrature 차이는 이 전제를 제공하지 않는다.

현재 정리는 finite owner closure의 한 signed scalar transport 방정식에 대한 결과다.
원래 coupled Einstein–Boltzmann 시스템의 해·각도 truncation·cold EoR closure를
인증하려면 그 시스템에서 \(\alpha,P_m,P_r\)의 전 구간 enclosure를 산출해야 한다.
따라서 원 DAG의 `CONTINUUM_TIME_ANGULAR_CERTIFICATE`는 열린 채로 유지한다.

## 4. 구현과 rounding 계약

`source/interval_transport.py`는 위 정리의 구간 재귀를 구현한다.
입력 endpoint와 cell 폭은 유한 decimal string으로만 받고,
전체 cell/초기값 witness의 locator·source identity·method를 보존한다.
이 문자열의 존재만으로 witness를 인증하지 않는다.
출력 상태는 항상 `conditional_on_input_enclosures`이며
`input_witnesses_verified=false`다.

기본 사칙연산은 서로 분리된 `ROUND_FLOOR`/`ROUND_CEILING` context로 수행한다.
Python 문서는 `Decimal.exp`의 `ROUND_HALF_EVEN` 올바른 rounding을 명시한다.
따라서 각각의 exp 결과에서 같은 정밀도의 직전/직후 표현가능 수를 잡으면
rounding error를 포함한다. exp에 전달하는 \(-ah\)도 먼저 구간으로 감싼다.
Exact negation에는 context를 적용하지 않는 `copy_negate()`를 쓴다.
Underflow·subnormal·overflow·invalid·division-by-zero는 trap으로 실패시킨다.
[Python Decimal의 공식 계약](https://docs.python.org/3/library/decimal.html#decimal.Decimal.exp).

작은 \(z=-ah\)에서는 \(1-e^z\)의 상쇄를 피하기 위해

\[
\Phi(a,h)=h\sum_{k=0}^{\infty}\frac{z^k}{(k+1)!}
\]

를 구간으로 합한다. \(|z|\le u\le1/8\)이고 \(k\)차까지 합했다면

\[
|\mathrm{tail}|\le
 \frac{u^{k+1}}{(k+2)!}\,
 \frac{1}{1-u/(k+3)}.
\]

각 tail 항의 비가 \(u/(k+3)\) 이하이므로 기하급수 상계가 성립한다.
구현은 이 상계를 위로 rounding하고 유한합 interval에 \([-tail,tail]\)을 더한다.
이는 표준 exponential-integrator \(\varphi_1\)의 스칼라 형태다.
[Niesen–Wright 원 논문](https://arxiv.org/abs/0907.4631)의 §2와
[SciPy exprel 공식 문서](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.exprel.html)를 대조했다.
SciPy/NumPy의 float exp 또는 exprel을 이 interval certificate의 내부 계산으로 사용하지 않는다.

## 5. 저장 이력의 빠른 누적 진단

별도 `cumulative_memory.py`는 PR128과 같은 \(W=e^{3(x-x_i)}H/H_i\)와
signed source를 사용해 \(W^{-1}\operatorname{cumulative\_simpson}(WP_A)\)와
대수적으로 같은 local transport 재귀를 계산한다. 전역적으로 커지는 \(W\) 배열은 만들지 않는다.
전체 \(N\)개 node의 결과를 \(O(KN)\) 연산으로 만들 수 있다.
균일한 홀수 node grid의 마지막 endpoint는 PR128 composite Simpson 식과 일치한다.
중간 odd node는 인접한 다음 sample을 이용할 수 있으므로
`simpson(y[:j+1])`를 모든 prefix에 독립적으로 적용한 값과 일반적으로 다르다.
이는 저장 데이터의 후처리로 허용되며 실시간 causal integrator라는 주장을 하지 않는다.
Quadratic interpolant의 음의 quadrature weight 때문에 부족한 해상도에서
양의 source를 적분한 모든 increment의 양성이 자동 보장되지 않는다.
[SciPy cumulative_simpson 공식 정의](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.cumulative_simpson.html).

## 6. 근거와 남은 의무

구간정리와 series remainder는 위에서 직접 유도했다.
Wolfram은 \(\int_0^h e^{-a(h-t)}dt=\Phi(a,h)\), \(a\to0\) 극한,
\(S\) normalization 항등식의 residual 0을 반환했다.
마지막 symbolic query에는 undefined-symbol와 중간 zero-division warning이 함께 있었으므로
원문을 `evidence/`에 보존하며 이를 수치 enclosure 검증으로 사용하지 않는다.
상수 coefficient의 별도 160자리 closed-form 계산과 signed interval corner들을
targeted unittest로 비교한다. 이 manufactured 검증은 새로운 과학 ODE 실행이 아니다.

이번 결과는 기존 구간해석과 variation of constants의 프로젝트 적용이다.
신규 no-go·문헌 대비 신규 정리·전체 continuum certificate를 주장하지 않는다.
실제 REI history의 whole-cell 입력 enclosure가 남은 구체적 의무다.
`HH_R10=OFF`, production admission은 발급하지 않는다.
