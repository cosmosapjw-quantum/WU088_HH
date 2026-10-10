# PHYS03: 유한 혼합 부호를 실제 시간·birth 모형으로 옮기는 조건

## 1. 정확한 비교 대상

\(b=S/S_*\)와 HH strength \(\lambda\)에 대해
\[
I_x=x(\lambda,b)-x(\lambda,0)-x(0,b)+x(0,0)
\]
를 쓴다. \(C^2\) family, 같은 control의 뜻, 같은 관측시각이면
\[
\frac{I_x}{\lambda b}
 =\int_0^1\!\int_0^1
 W_x(t;\alpha\lambda,\beta b)\,d\alpha\,d\beta,\quad
 W=\partial_\lambda\partial_bz.
\tag{1}
\]
축 위에서는 quotient의 연속 연장으로 읽고, \(I_x=0\)는 정확하다.

actual과 reference를 비교하려면 초기 physical slice, 전체 gas/photon/
guard state, source를 켜고 끄는 방식, 최종 clock을 먼저 정의해야 한다.
초기 상태가 서로 다르면 그 차이와 \(U,V,W\)의 초기 차이도
certified error budget에 넣어야 한다.
PHYS02 selected stage aggregate를 raw macro predecessor로 대체하는
숨은 초기값 변경을 허용하지 않는다.

## 2. smooth cell의 componentwise comparison

같은 좌표에서 augmented 상태를 \(X=(z,U,V,W)\)라 하고,
actual/reference의 장을 \(\mathcal G,\bar{\mathcal G}\)라 하자.
양쪽 해와 연결 segment를 포함하는 convex tube 전체에서
\[
|\mathcal G_i(t,\bar X)-\bar{\mathcal G}_i(t,\bar X)|\le r_i(t)
\]
와
\[
A_{ij}(t)\ge\sup|\partial_j\mathcal G_i|\quad(i\ne j),\qquad
A_{ii}(t)\ge\sup\partial_i\mathcal G_i
\tag{2}
\]
를 잡는다. \(A\)는 off-diagonal이 nonnegative인 Metzler matrix다.
대각에도 절댓값을 쓰면 더 보수적인 충분조건이 된다.
상단 Dini derivative로
\[
D^+|X-\bar X|\le A(t)|X-\bar X|+r(t)
\tag{3}
\]
가 성립한다.

\(\dot\Psi=A\Psi\), \(\Psi(s,s)=I\)의 positive propagator를 사용하면
\[
|X(t)-\bar X(t)|
\le \Psi(t,s)|X(s)-\bar X(s)|
 +\int_s^t\Psi(t,u)r(u)\,du.
\tag{4}
\]
이는 일반적인 mean-value formula와 scalar sign inequality의
componentwise 적용으로 직접 얻는 비교식이다. 이번 루프는 실제
\(A,r,\Psi\)의 수치 상계를 계산하지 않았다.

## 3. event와 discrete source map

공통 chart에서 두 augmented event map을 \(\mathcal R,\bar{\mathcal R}\)라 하자.
그 derivative bound와 model defect가
\[
K\ge\sup|D\mathcal R|,\qquad
\rho\ge|\mathcal R(\bar X)-\bar{\mathcal R}(\bar X)|
\]
를 만족하면
\[
|X^+-\bar X^+|\le K|X^--\bar X^-|+\rho.
\tag{5}
\]
움직이는 event에는 HYBRID_THEORY_KO.md의 공통 시각 동기화까지
포함한 map을 써야 한다. grazing 또는 event 순서 변화가 있으면
parameter domain을 나누고 해당 chart의 비교를 새로 정의한다.

BE를 연속 ODE의 실제 중간 trajectory인 것처럼 표현할 필요는 없다.
각 endpoint의 전체 source map을 \(\mathcal M_i,\bar{\mathcal M}_i\)라 하면
식 (5)를 그대로 적용해
\[
E_{i+1}\le K_iE_i+\rho_i,\quad
E_n\le K_{n-1}\cdots K_0E_0+
\sum_{j=0}^{n-1}K_{n-1}\cdots K_{j+1}\rho_j
\tag{6}
\]
를 얻는다. \(K_i,\rho_i\)는 remap, birth, BE의 합성 순서와
기존 mixed sensitivities를 포함해야 한다.
Actual BE root family와 uniform inverse bound가 없으면 이
augmented endpoint map의 수치 bound도 아직 주어지지 않는다.

## 4. 부호 전이를 위한 충분조건

식 (4)–(6)에서 전체 parameter rectangle의 최종 mixed 성분에
\[
|W_x^{\rm actual}-W_x^{\rm ref}|\le B_{W_x}(t)
\]
를 얻었다고 하자. 식 (1)로
\[
\left|\frac{I_x^{\rm actual}}{\lambda b}
      -\frac{I_x^{\rm ref}}{\lambda b}\right|
\le B_{W_x}(t).
\tag{7}
\]
Reference upper bound가 \(-m(t)<0\)이면
\[
\boxed{B_{W_x}(t)<m(t)}
\tag{8}
\]
가 actual mixed sign을 음수로 유지하는 충분조건이다.
전체 시간의 부호에는 모든 양의 시간에서 식 (8)을 확인해야 한다.
endpoint 하나의 확인으로 전체 시간 부호를 주장하지 않는다.

PHYS02 reference에는
\[
m(t)=-\{c_3\tau^3+U_4\tau^4\},\qquad
\tau=t/h,\quad h=1.25\times10^9\ {\rm s}
\]
를 사용할 수 있다. 상속된 endpoint upper bound의 보수적 margin은
\[
m(h)=2.01048731484330921217079362533946553489069
\times10^{-17}.
\tag{9}
\]
이 숫자는 frozen PHYS02 결과의 재표현이다. 새 actual tolerance,
오차 평가 또는 actual sign certificate로 승인된 숫자가 아니다.
앞의 초기 slice와 source semantics가 맞고 모든 comparison defect가
포함되어야 식 (9)의 margin과 비교할 수 있다.

## 5. 현재 가용성과 남은 수치 작업

| 항목 | 현재 상태 |
| --- | --- |
| owner background \(a_i,n_H,n_{He},H\) 및 grid/redshift | 원 source에서 확인 |
| full/half endpoint source 순서, 저장 preBE photons | 원 source/record에서 확인 |
| nonautonomous 감도, birth kernel, event mixed derivative | 직접 유도 및 exact algebra 검산 |
| threshold remap 한 column의 defect | actual leaf real-expression의 Arb enclosure |
| 새 native \((\lambda,b)\) common-state source family | 미구현 |
| accepted half1 checkpoint receipt 및 half2 exact incoming state | 새 owner 반환에서 null |
| trusted native root, parameter tube, inverse/preconditioner | 새 owner 반환에서 null |
| actual augmented \(K_i,\rho_i\) 또는 \(A,r\)의 uniform bound | 아직 없음 |
| \(B_{W_x}\)와 식 (8)의 실제 검증 | unresolved |

새 actual family가 없다는 이유로 source algebra를 중단하지 않았고,
실제 source가 알려졌다는 이유로 family bound를 만들었다고 주장하지 않았다.
이번 루프에서 완료한 것은 transfer의 충분조건과 필요한 실제 수치
객체의 정확한 식별이다.
