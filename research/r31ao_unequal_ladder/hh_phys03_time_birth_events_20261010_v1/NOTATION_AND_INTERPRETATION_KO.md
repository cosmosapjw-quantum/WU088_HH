# PHYS03 기호와 국소 물리 해석

## 좌표와 정규화

\(x=x_{\rm HII}\), \(y_1=x_{\rm HeII}\), \(y_2=x_{\rm HeIII}\),
\(w\)는 eV/H 단위 기체 열에너지, \(P_j\)는 photons/H다.
\(r_{\rm He}=n_{\rm He}/n_H\), \(u=1-x\)라 두면
\[
\Pi=1+r_{\rm He}+x+r_{\rm He}(y_1+2y_2),\qquad
T=\frac{2E_{\rm eV}}{3k_B}\frac{w}{\Pi}.
\]
\(E_{\rm eV}\)는 1 eV의 erg 값이고
\(H_{\rm mean}\)는 팽창률이다. HH channel vector \(H(z)\)와 다른 기호다.

13.7 eV의 지정 birth에 대한
\[
A=cn_H\sigma_H(E_b),\qquad q=n_Hu^2k_{\rm LCS}(T),
\qquad H=q(1,0,0,-\chi_H,0_{\rm photons})
\]
를 사용한다. HH event에 추가 \(1/2\)를 넣지 않는다.

원 LCS rate의 logarithmic temperature slope를
\[
\nu=\frac{d\log k_{\rm LCS}}{d\log T}
 =1.2+\frac{157800\ {\rm K}}{T}
\]
라 하면
\[
T_\gamma=\frac{2E_{\rm eV}(E_b-\chi_H)}{3k_B},\qquad
\Xi=\frac{u}{\Pi}\nu\left(1-\frac{T_\gamma}{T}\right).
\]
여기서 \(T_\gamma\)는 birth photon의 excess energy를 temperature 단위로
바꾼 값이다. 우주배경복사의 온도를 뜻하지 않는다.
모든 상수는 PHYS02의 exact binary64-leaf semantics를 계승한다.

선택 initial point의 상속 값은
\[
T_0=49489.0775134\ldots\ {\rm K},\quad
T_\gamma=785.745018854\ldots\ {\rm K},\quad
\Xi_0=0.1769024684110926\ldots
\]
이다. 증거는 inputs/phys02/results/REMAINDER_256_FINAL.json의 leading와
inputs/PHYS01_LOCAL_COEFFICIENTS_FINAL.json이다.

## 음의 혼합 선도항이 생기는 이유

photoionization 한 번은 중성수소를 줄이고 입자 수를 늘리며,
동시에 \(E_b-\chi_H\)만큼 열에너지를 더한다.
현재 \(T_\gamma\ll T_0\)에서는 입자 수 증가가 평균 온도를 내리는 방향이다.
따라서 photo 변화에 따른 HH rate derivative는
\[
(H_zJB)_x=-Aq(2+\Xi)
\]
가 된다. \(2\)는 \(u^2\)의 중성수소 의존성,
\(\Xi\)는 그 photo 변화가 만든 온도 반응에 의한 추가 억제다.
또한 HH가 먼저 중성수소를 줄이면 photo RHS 자체가 달라져
\[
Q(H,B)_x=-Aq
\]
를 준다. 두 시간 순서가 합쳐져 uniform continuous cubic은
\[
I_x=-\frac{\lambda S}{6}Aq(4+\Xi)t^3+O(\lambda St^4)
\]
가 된다.

이 해석은 direct HH 증가량
\(D_x=x(\lambda,b)-x(0,b)\)의 부호와 다르다.
\(I_x<0\)는 HH와 새 photon source의 동시 효과가 단순 합보다 작다는
혼합 반응이다. HH 자체가 전체 HII를 감소시켰다는 의미가 아니다.
Actual 전체 이력에서 \(D_x\) 또는 \(I_x\)가 얼마인지는 별도 family 계산이 필요하다.

## 세 가지 시간 객체

| 시간 객체 | 의미 |
| --- | --- |
| smooth reference의 \(t-t_0\) | 정의한 공통 initial slice 뒤의 실제 연속 노출시간 |
| owner endpoint의 \(t_i\) | remap, birth 및 density를 조립하는 clock |
| BE의 \(\delta_i\) | endpoint 조립 뒤 implicit source map에 곱해지는 step 길이 |

각 객체를 구분해야 true terminal photon kick의 즉시 gas 반응 0과,
endpoint birth 뒤 BE의 nonzero formal gas response가 충돌하지 않는다.
