# R11 명제·전제·구현 대응

## 대상과 양화

열벡터 관례를 사용한다. 유한 차원 n=1..13, 고정 exact K, pi, destruction d에 대해 K의 열합은0이고 비대각은 비음수, pi는 확률벡터, d>=0이다. H=pi*d^T-diag(d), A_w(t)=K+w(t)H. 인증된 같은 clock의 닫힌 구간 I에서 모든 가측 w:I→[m_w,M_w], 0<=m_w<=M_w를 양화한다. 모든 block [s,s+tau]⊂I가 대상이다. 비선형 실제 해를 따라 결정되는 w도 whole-domain box가 입증돼 있으면 이 family의 원소다.

Z={r:1^T r=0}. rho(T)는 T의 Z상 l1 유도노름이다. R=||r||1, E=|eta|, coarse l1=4E. forcing f_r는 Z에 속하고 전체 fine-domain에서 ||f_r||1<=g_r, coarse 차이는 D+E<=cR+d_c E+g_e이다. c>=0, d_c signed, g_e>=0. 이 whole fine/coarse 전제는 입력의 과학적 의무다.

K-only certificate는 rho(exp(K*tau))<=q_K를 인증한 원래 결과다. 저장 R7 세2state는 exp(-1/2)<=5/8의 exact analytic certificate, native9는 R6 native_mu_256의 전체 Kbox certificate에 현재 midpoint K가 포함된 결과를 재사용한다. 고정 homogeneous K이므로 시간차 tau의 인증이 모든 시작시각에 적용된다. full A의 인증은 아래 두 새 연결로 만든다.

## 명제와 API의 연결

| ID | 결과 | 구현·검토 의무 |
|---|---|---|
| T1 | A_w는 전체 family에서 보존적 Metzler, U_w는 column stochastic | generator_certificate exact sign/column/simplex guards |
| T2 | rho(U_w(s+tau,s))<=min(1,q_K+tau*M_w*||H||1) | ordered Duhamel와 두 전파자의 l1 nonexpansiveness |
| T3 | b_H=max d_j(1-pi_j)=||H||1/2; U_w>=exp(-b_H∫w)exp(Ktau) | scalar shift의 양의 propagator comparison |
| T4 | rho(U_w)<=1-exp(-b_H M_w tau)(1-q_K) | common stochastic component decomposition; finite precision positive gap |
| T5 | h(u)=q^floor(u/tau),h0=1; R<=hR0+h*g_r | all-start composition와 source-age 위치 |
| T6 | aligned-grid F_n=delta sum h_(n-1-j) g_j, R_n=h_n R0+F_n | 정확한 셀 분할; current forcing h0 |
| T7 | 셀 내부 R은 L_n과 V_n 사이 affine, V는 오른쪽 left limit | whole-cell 인증에 initial-kernel downward jump 포함 |
| T8 | signed d_c의 positive Bernstein moments로 E endpoint를 적분 | exp 및 W0/W1의 dyadic128/Taylor96 outer intervals |
| T9 | Rwhole을 넣은 scalar 비교해 양끝 최대가 Ewhole을 덮음 | signed d derivative fixed sign, rounded endpoint도 포함 |
| T10 | 같은 source/state/clock/closed cell upper들의 min은 유효 | R10 실제 SHA/pointer, point/whole 구별, global R age 불변 |

현재 구현 grid의 원점은 저장 source와 같은 t0=0이다. t_n=n*delta, tau=m*delta이며 m은1..192 정수다. g_r,g_e는 해당 same grid의 scalar 또는 셀별 배열, c와 d_c는 sweep 전체에 고정한다. 다른 forcing grid나 시간가변 c,d_c로의 일반화는 이 API가 수행하지 않는다. 분석적 정리의 가측 forcing 적분과 현재 finite API는 이 대응으로 연결된다.

## 단위·정규화와 출력 의미

K, wH, c, d_c의 단위는 declared inverse time, g_r/g_e는 declared density/time이다. tau*M_w*||H||1 및 d_c*delta는 무차원이다. Native K 사례도 현재 density/clock은 저장된 조건부 dimensionless fixture의 좌표이며 physical binding은 INPUT_PENDING이다. Native v=UNSPECIFIED, MISSING_NOT_ZERO, TIQM/SQM 구별을 보존한다.

Raw lower는 생산 코드가 선택한 고정 유리수 q에 대응하는 이상적 비교해의 lower다. 실제 물리 오차의 lower는 출력하지 않는다. Capped 출력은 upper만 반환한다. 그림의 endpoint 연결선은 시각적 안내이며, whole_cells_upper가 닫힌 셀 인증을 제공한다.

## 근거 재사용과 교정 범위

R10 과학 payload와36개 DAG 객체를 변경하지 않는다. R8 원래726/727+1FAIL, 별도24/24 exact-phi, R10 최초 postprocessing ID실패와 DOC01/META02 종료, CAS15zero+warnings/causeNOT_ESTABLISHED, 저장 sample의 tolerance-qualified 판정을 그대로 참조한다. 이번 새 node의 채택은 R11 실제 proof/code/reference 및 독립 review에 한정된다.
