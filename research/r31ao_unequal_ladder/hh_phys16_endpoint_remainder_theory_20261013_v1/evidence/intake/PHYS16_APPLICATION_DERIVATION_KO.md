# PHYS16: 상속된 포함 자료에 대한 첫 endpoint 결함 적용

## 결과와 근거 상태

같은 COMMON, 같은 고정 source 계열, 같은 전역 \((\lambda,b)\in[0,1]^2\)에서 PHYS15의 잔차식을 실제 외향 구간 산술로 평가했다. 2026-10-13 KST의 `checks/application/run01/`은 `CANDIDATE_COMPUTED`다. 새 유도와 코드의 독립 심사는 root가 진행한다. 상속된 source, 첫 half, Full, PHYS14 second-half의 유효성은 기존 전제다.

첫 계산의 유한 endpoint 차이 방향은 \(d=g_2-g_F\)이며,
\[
\begin{aligned}
d_x&\in[4.968073098724,6.424794326491]\times10^{-8},\\
d_w&\in[-2.378772061685,-1.828215860677]\times10^{-8}\ \mathrm{eV/H},\\
\Delta e&\in[4.968232944627,6.425017521665]\times10^{-8},\\
\Delta T&\in[-1.586022390056,-1.210760764188]\times10^{-3}\ \mathrm K,\\
\Delta n_e&\in[4.944257155952,6.394011555549]\times10^{-12}\ \mathrm{cm}^{-3}.
\end{aligned}
\]
표시된 decimal endpoint는 외향 반올림이다. 기계용 원본은 분자·분모를 모두 보존한다.

## 1. source 값·gradient·Hessian의 직접 사용

`SOURCE_BOX_COMPONENTS.json/nonphoto[i]`와 `SOURCE_BOX.json/q`는 원 convex gas domain \(X\)의 포함이다. 각 항은 `value`, `gradient[7]`, `signed_hessian[7][7]`를 가진다. 이번 gas 연산에는 앞의 네 좌표 \((x,y_1,y_2,w)\)를 사용한다. `SOURCE_CENTRE_COMPONENTS.json`과 `SOURCE_CENTRE.json/q`는 동일 gas centre \(c\)에서의 값과 도함수다. 수치값은 decimal 문자열 대신 `lo_bits`, `hi_bits`의 정확한 binary64 수로 읽는다.

\(G\subset X\)이고 \(\delta=G-c\)라 하면 기존 자료로
\[
[F](G)=[F](X)\cap\left([F](c)+[D F](X)\delta\right),
\]
\[
[D F_j](G)=[D F_j](X)\cap
\left([D F_j](c)+[D^2F_{j\cdot}](X)\delta\right)
\]
를 구성했다. 이 계산은 보존된 값과 도함수의 Taylor 포함을 적용한다. 반응 fit, 원 source kernel, 원 root solver를 호출하지 않는다. Hessian은 원 \(X\)의 포함을 그대로 재사용한다.

## 2. 실제 단계 증분을 공유하는 opacity 차이

상속된 개별 root hull은 \(x\)에서 약 \(0.0036\), \(w\)에서 약 \(0.131\)의 폭을 가진다. 실제 두 half의 연결은
\[
\boxed{s_{21}:=g_2-g_1=hB_2(g_2)+VP_2}
\]
를 만족하므로 이를 먼저 포함했다. 실제 결과는
\[
s_{21,x}\in[4.026226742267,4.238554960924]\times10^{-5},
\]
\[
s_{21,w}\in[-2.138278832743,-2.054999707633]\times10^{-4}\ \mathrm{eV/H}.
\]
\(P_2\)는 같은 \(Q_1=RZ_0+bJ\)와 \(A_1\)에서 만든 \(Q_2=RA_1Q_1+bJ\)에 \(L_2\)를 적용하고, 기존 PHYS14의 유효한 photon incoming/absorption 포함과 교차했다. 이 교차는 같은 정확한 함수에 대한 두 포함을 사용한다.

첫 half와 끝 시각의 투과 차이는 같은 \(s_{21,x}\)를 써서
\[
\boxed{\Delta A_{1,j}
=h\left[c\sigma_j(n_2-n_1)(1-x_2)-a_{1j}s_{21,x}\right]A_{1j}A_{2j}}
\]
로 평가했다. 이 차이를 정의한 뒤 일곱 광자 absorption 항과 여섯 outgoing 항 양쪽에서 재사용한다. Source의 상태 이동 항도 같은 증분을 사용한다.
\[
r_{g,\mathrm{move}}=-h\overline J_{12}s_{21},\qquad
\overline J_{12}=\int_0^1 DB_2(g_1+s(g_2-g_1))\,ds.
\]
평균 Jacobian의 포함은 두 상속 root hull의 convex hull에서 원 도함수로 구성한다.

## 3. Cooling cone으로 \(k_{w\mathrm{He}}\)를 포함하는 보조정리

원 FT03 photo-off source는 PHYS15에서
\[
F^{np}_w=n e\left(k_{wH}+f k_{w\mathrm{He}}\right)
\]
로 인수 분해했다. 원 반응 정의에서 CI와 DR의 에너지 항은 양의 계수·에너지·population을 곱한 cooling이다. RR의 열에너지 계수는
\[
\kappa_a=\frac{k_BT\alpha_a}{\epsilon_{\mathrm{eV}}}
\left(\frac32+s_a\right)
\]
이다. HeI에 대해서 \(3/2+s_I=1.5-0.654>0\)다. H와 HeII에서는
\[
u=\left[\frac{\Lambda_a}{0.522T}\right]^{0.470},\qquad
\frac32+s_a=1.5-1.503+1.923\cdot0.470\frac{u}{1+u}.
\]
원 source의 \(30000\le T\le110000\ \mathrm K\)에서 \(\Lambda_H=315614\ \mathrm K\), \(\Lambda_{II}=1263030\ \mathrm K\)이므로 \(u>1\)이다. 따라서 captured binary64 상수를 정확한 실수로 읽으면
\[
\frac32+s_a>1.5-1.503+\frac{1.923\cdot0.470}{2}>0.4489.
\]
양의 nuclear density와 물리적 분율 영역에서
\[
k_{wH}\le0,\qquad k_{w\mathrm{He}}\le0
\]
이고, 따라서
\[
\boxed{\frac{F^{np}_w}{n e f}\le k_{w\mathrm{He}}\le0.}
\]
실제 적용점은 온도 정렬 사상
\[
g_*=(x,y_1,y_2,w\Pi_2/\Pi_1),\qquad T_2(g_*)=T_1(g)
\]
이다. \(g_*\)에서 보존된 Full source의 \(F^{np}_w\) 포함과 양의 \(n_2,e_2,f_2\)를 사용하면
\[
k_{w\mathrm{He}}(g_*)\in[-8.824448068133\times10^{-9},0]
\quad [\mathrm{eV\,cm^3\,s^{-1}}].
\]
이는 He cooling의 개별 반응값을 재평가하지 않고 전체 cooling의 상계로부터 얻은 포함이다. 이번 적용에서 \(T_1\in[48925.84102475,49487.51623609]\ \mathrm K\)이고 \(g_*\)까지의 선분은 원 \(X\) 내부다.

\(\Delta f=f_1-f_2<0\)이므로 원 PHYS15 bridge의 thermal 보정은
\[
0\le n_1e_1\Delta f k_{w\mathrm{He}}
\le6.351387331127\times10^{-30}\quad[\mathrm{eV/H/s}].
\]
따라서 누락돼 있던 분리 성분의 포함을 이 보조정리로 닫았다. 새 transcendental 또는 반응 fit 평가는 0회다.

## 4. 잔차에서 componentwise endpoint 포함

일곱 광자 항은 PHYS15의 정확한 분해를 사용한다. \(\rho\)는 PHYS14의 유효한 고정밀 구간을 읽고 \(\rho^2\)를 같은 graph에서 계산한다. \(R-I\), \(R^2-R_F\), \([R,A]\)는 각 sparse coefficient를 먼저 인수 분해했다. Boundary column과 두 guard를 모두 유지한다. 총 birth는 exact captured \(M_F=2M\) 관계를 사용한다.

조립한 잔차는
\[
r=h\delta B_t(g_1)-h\overline J_{12}s_{21}+Vp.
\]
원 `UNIFORM_ARITHMETIC.json`의 동일 \(C,B,q,S\)를 함께 읽었다. \(C\)와 \(B\)의 저장값을 정확한 유리수로 사용하고 \(\sum_j B_{ij}S_j/S_i\le q<1\)를 확인했다. \(u=|Cr|\)를 componentwise magnitude로 두고
\[
(I-B)m=u
\]
를 정확한 4×4 유리수 소거법으로 풀었다. 모든 \(m_i\ge0\)이며 \(m-Bm=u\)를 정확히 확인했다. 따라서
\[
d\in[Cr]+[-Bm,Bm].
\]
그 뒤 \(\overline E=I-C\overline{\mathcal A}\)를 평균 Jacobian의 signed 포함에서 구성하고 원 \([-B,B]\)와 교차했다. 같은 \(Cr\)에 대해
\[
D\leftarrow D\cap\bigl([Cr]+[\overline E]D\bigr)
\]
를 세 번 수행했다. 이미 알려진 두 endpoint 사이의 선분에 적용하는 잔차 전달이므로 새 nonlinear root를 구하는 실행은 없다.

## 5. 유한 관측량과 항별 포함

같은 \(d\)로 \(d_e=d_x+f_2(d_{y_1}+2d_{y_2})\), \(\Delta n_e=n_2d_e\)를 구성하고
\[
\Delta T=\frac{C_Td_w-T_2d_e}{\Pi_2-d_e}
\]
를 외향 평가했다. 실제 포함에서 \(\Pi_F=\Pi_2-d_e>0\)이다. 각 잔차 항 \(r_s\)에는 같은 평균 행렬의 포함 \([\overline E]\), 같은 \(C,B\), 같은 유한 온도 covector를 적용했다.

이 결과는 연결된 고정 \(\alpha\) 및 전역 parameter 계열 전체에 대한 유효한 포함이다. Interval box 곱은 공통 factor를 여러 번 사용하는 경우에 여전히 폭을 늘릴 수 있다. 이번 구성은 공유 함수·차이식·단계 증분을 대수적으로 보존하고 난 뒤 자연 구간 산술을 적용한다. \(\lambda,b\)에 대한 완전한 affine/Taylor polynomial model을 새로 작성한 결과와는 표현력이 다르며, 그 차이는 다음 정밀화에서 실제 폭을 기준으로 선택할 수 있다.

## 실행 근거

- 실제 command, 실행 전 선언, code SHA: `checks/application/run01/PRE_RUN.json`.
- 실제 wall/CPU/RSS 및 output SHA: `checks/application/run01/RUN_RECORD.json`.
- Wrapper wall 0.465254261 s, user CPU 0.402452 s, peak RSS 41984 KiB, exit 0.
- 원 source/kernel/fit 호출 0, 새 root solve 0, history replay 0, cloud mutation 0.
- 전체 원 photon 33개와 guard 2개 및 원 signed carry data는 상속 자료로 유지한다. 이번 평가량은 유한 endpoint의 primal 포함이며 derivative carry의 부호를 임의로 바꾸지 않는다.

`run01`은 최초 유효 계산이다. 수치 결과를 바꿀 새 교정이 발견되면 해당 원인과 버전을 보존하고 변경 부분부터 다시 검토한다.
