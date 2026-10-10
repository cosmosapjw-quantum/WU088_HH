# PHYS03: 공통 시각의 혼합 event derivative

## 1. 무엇을 미분하는가

상태 \(z\)는 기체와 광자를 함께 포함한다. 두 control은
\(a=\lambda\), \(b=S/S_*\)이다. 같은 전체 초기상태에서 시작하고,
관측시각도 두 control과 무관하게 고정한다. 이미 존재하는 광자는
\(b=0\)에서도 유지한다.

고립된 event를
\[
g(t,z^-;a,b)=0,\qquad z^+=R(t,z^-;a,b)
\]
로 쓰자. \(f^-,f^+\)는 각각 event 전후의 벡터장이다.
guard와 reset은 \(C^2\), 양쪽 흐름은 필요한 차수로 매끄럽고,
\[
d=g_t+g_z f^-\ne0
\tag{1}
\]
를 가정한다. 인근 parameter family에서 event 순서가 같아야 한다.
접촉만 하고 되돌아가는 grazing, 동시 비가환 event, event 수 변화는
이 한 event 식의 적용 범위 밖이다.

기존 saltation matrix는 reset의 상태 Jacobian에 event-time 변화를
더한 일차 변분이다. 여기서는 같은 chain rule을 혼합 이차까지
전개한다. 문헌상의 일차 기준식과 transversality 조건은
Kong et al., *Proceedings of the IEEE* **112** (2024), 585–608,
DOI [10.1109/JPROC.2024.3440211](https://doi.org/10.1109/JPROC.2024.3440211),
[arXiv 2306.06862v3 §III-A, Eq. (9), Appendix A](https://arxiv.org/html/2306.06862v3)
를 참조했다. 아래 혼합식은 이번 루프에서 직접 유도한 식이다.
일반적인 문헌 최초성은 주장하지 않는다.

## 2. 움직이는 event 시각과 event 직전 상태

명목 event 시각을 \(\tau\)라 하고, 그 시각으로 연장한 pre-branch의
공통 시각 derivative를
\[
U=\partial_a z^-(\tau),\quad V=\partial_b z^-(\tau),\quad
W=\partial_a\partial_b z^-(\tau)
\]
라 하자. event 시각 \(\tau(a,b)\)의 미분은 \(\theta_a,\theta_b,\theta_{ab}\)로
표기한다. guard를 한 번 미분하면
\[
\theta_a=-\frac{g_zU+g_a}{d},\qquad
\theta_b=-\frac{g_zV+g_b}{d}.
\tag{2}
\]

움직이는 event 위의 상태 미분은
\[
\bar U=U+f^-\theta_a,\qquad \bar V=V+f^-\theta_b.
\]
확장 좌표를 \(\xi=(t,z,a,b)\)라 하고
\[
v_a=(\theta_a,\bar U,1,0),\qquad
v_b=(\theta_b,\bar V,0,1)
\tag{3}
\]
로 정의한다. 모든 \(g,R\) 도함수는 이 확장 좌표에 대한 도함수다.
각 \(f^\pm\)의 시간·매개변수 편미분에서는 \(z\)를 고정한다.

상태 합성 \(z^-(\tau(a,b),a,b)\)의 chain rule은
\[
\begin{aligned}
C^-={}&(J^-U+f_a^-)\theta_b
      +(J^-V+f_b^-)\theta_a\\
 &+(f_t^-+J^-f^-)\theta_a\theta_b,\\
\bar W={}&W+C^-+f^-\theta_{ab}.
\end{aligned}
\tag{4}
\]
여기서 \(J^-=f_z^-\)다. guard를 두 번 미분하고
\(g_zf^-\theta_{ab}\)를 \(g_t\theta_{ab}\)와 합치면
\[
\boxed{\theta_{ab}
 =-\frac{g_z(W+C^-)+D^2g[v_a,v_b]}{d}.}
\tag{5}
\]
명시적 \(g_{ab},g_{ta},g_{zb}\)도 \(D^2g[v_a,v_b]\)에 들어 있다.
state-dependent guard의 Hessian을 버리면 이 식이 달라진다.

## 3. reset을 미분하고 다시 공통 시각으로 맞추기

reset 직후의 moving-event derivative는
\[
\begin{aligned}
Y_a&=DR\,v_a,&Y_b&=DR\,v_b,\\
Y_{ab}&=DR\,(\theta_{ab},\bar W,0,0)+D^2R[v_a,v_b].
\end{aligned}
\tag{6}
\]
이 \(Y\)는 각 parameter의 서로 다른 event 시각에서 평가된다.
같은 물리 시각의 반응과 바로 빼면 안 된다.

post-branch를 명목 시각 \(\tau\)까지 매끄럽게 연장해 동기화하면
\[
U^+=Y_a-f^+\theta_a,\qquad
V^+=Y_b-f^+\theta_b.
\tag{7}
\]
그 혼합 derivative는
\[
\boxed{\begin{aligned}
W^+={}&Y_{ab}-f^+\theta_{ab}\\
 &-(J^+U^++f_a^+)\theta_b
  -(J^+V^++f_b^+)\theta_a\\
 &-(f_t^++J^+f^+)\theta_a\theta_b.
\end{aligned}}
\tag{8}
\]
식 (8)은 post-branch 합성
\(z^+(\tau(a,b),a,b)\)를 두 번 미분한 식에서 \(W^+\)를 풀어 얻는다.
따라서 마지막 줄의 부호나 \(U^+\) 대신 \(Y_a\)를 쓰는 오류가 없다.
실제 최종 관측시각까지의 post-event 흐름은 이 뒤에 별도로 전파한다.
명목 event와 정확히 같은 시각에서 불연속 상태의 모든 corner를
직접 비교할 수 있다는 뜻은 아니다.

매개변수에 직접 의존하지 않는 guard/reset에서 식 (7)의 \(U\) 계수는
\[
R_z+\frac{(f^+-R_zf^--R_t)\,g_z}{g_t+g_zf^-},
\tag{9}
\]
즉 일차 saltation matrix로 돌아간다.

## 4. 이번 HH control에 필요한 고정시각 특수형

실제 owner의 \(a,b\)는 주어진 배경 \(h_i\), 고정 energy grid,
prescribed step schedule를 변화시키지 않는다는 계약이다.
그러므로 그 계약 아래 event clock derivative는
\(\theta_a=\theta_b=\theta_{ab}=0\)이다. 별도로 존재하는 owner의
\(\theta\) 태그를 birth strength \(b\)로 재명명하지 않는다.

고정시각의 일반 reset은
\[
\begin{aligned}
U^+&=R_zU+R_a,\\
V^+&=R_zV+R_b,\\
W^+&=R_zW+R_{zz}[U,V]+R_{za}V+R_{zb}U+R_{ab}.
\end{aligned}
\tag{10}
\]

고정 배경의 photon transport/remap 뒤 additive birth는
\[
R(z;a,b)=Lz+b\,B_{\rm e},\qquad
L=\operatorname{diag}(I_{\rm gas},T_{\rm photon})
\]
이므로
\[
\boxed{U^+=LU,\quad V^+=LV+B_{\rm e},\quad W^+=LW.}
\tag{11}
\]
gas의 HH 감도와 기존 photon 감도를 전부 보존한다.
\(B_{{\rm e},a}=0\)이라고 해서 \(U,W\)를 0으로 만들지 않는다.
진짜 종료시각의 photon impulse는 gas를 바꾸지 않으므로
그 시각의 gas four-corner contrast도 바꾸지 않는다.

다만 실제 source는 endpoint birth 후 길이 \(\delta\)의 BE source map을
적용한다. 그 뒤의 gas 반응은 식 (11)만으로 끝나지 않는다.
같은 differentiable BE root branch가 존재하고
\(I-\delta J_+\)가 가역이면, formal implicit differentiation은
\[
\begin{aligned}
(I-\delta J_+)U_+&=U_{\rm in}+\delta H_+,\\
(I-\delta J_+)V_+&=V_{\rm in},\\
(I-\delta J_+)W_+&=W_{\rm in}
 +\delta\{Q_+[U_+,V_+]+H_{z,+}V_+\}.
\end{aligned}
\tag{12}
\]
여기서 \(V_{\rm in}\)에는 지정 birth의 \(B_{\rm e}\)가 이미 들어 있다.
이 식은 root family의 존재·유일성·uniform inverse bound를 인증하지
않는다. 이번 루프는 그 root를 계산하지 않았다.

## 5. fixed-grid 문턱과 moving characteristic 문턱의 차이

smooth characteristic의 에너지 자체로 \(\sigma(E(t))\)를 평가하는
모형에서 provider cutoff를 가로지르면 양쪽 벡터장이 달라질 수 있다.
상태에 jump가 없다면 \(R=I\)인 event로 식 (2)–(8)을 사용할 수 있다.
그 경우에도 guard, crossing direction, 양쪽 field를 정의해야 한다.

확인한 실제 owner는 \(E_jg(t_1)/g(t_0)\)로 transport한 뒤 fixed node에
hat remap하고, 그 fixed node 에너지의 단면적으로 BE를 만든다.
따라서 transported ray가 13.60 eV를 통과한다는 것과 BE의
단면적이 바로 0으로 전환된다는 것은 동일한 연산이 아니다.
고정 node cutoff와 hat knot를 source 순서대로 처리한다.

energy나 geometry를 매개변수로 변화시키려면 piecewise hat의 branch
전환을 함께 다뤄야 한다. knot에서 일반적인 \(C^2\) reset 가정은
깨진다. 이런 family는 one-sided chart로 나누고 경계 접합과 관측량을
검증해야 한다. 현재 \(a,b\)가 geometry와 clock에 영향을 주지 않는
설정에서는 이 문제를 가상의 moving-event 감도로 만들어 넣지 않는다.

## 6. 구현과 검산 범위

src/hybrid_mixed.py는 식 (2)–(8)을 구현한 algebraic operator다.
tests/test_hybrid_mixed.py는 다음 8개 검사를 시행했다.

| 검사 | 독립 기준 |
| --- | --- |
| 고정 birth/remap의 누적 \(U,W\) 유지 | exact rational 선형 chain rule |
| parameter-prescribed event time, explicit-time 전후 field, nonlinear reset | 닫힌 event/reset/flow 합성의 Sympy 미분 |
| 곡률 있는 state guard와 parameter-dependent post field | 닫힌 event-time 식 |
| state-dependent pre/post flow | exponential/logarithmic 닫힌 해의 미분 |
| 두 상태의 교차 reset | 다변수 닫힌 합성 |
| 같은 field의 identity event | event 삽입 전후의 동일 derivative |
| \(g_t+g_zf^-=0\) | 명시적 거절 |
| nominal point가 guard 밖 | 명시적 거절 |

모든 exact 비교가 통과했다. fixtures는 비물리 수학 예제이며
native gas solver, event locator 또는 interval event certificate가 아니다.
입력 dimension과 transversality는 확인하지만 arbitrary 사용자 함수가
\(C^2\)인지 또는 전체 parameter rectangle에 같은 event 순서가
유지되는지 프로그램이 자동 증명하지 않는다.

결과 상태는 derived + exact algebra checked + implementation verified다.
실제 HH event/root family 전체의 유한시간 인증은 아직 unresolved다.
