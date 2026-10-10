# PHYS04: NCP 이식용 reduced-BE 혼합 감도

## 1. 실제 잔차와 photon 제거

NCP는 이 저장소의 host-local Codex 실행 lane이다.
현재 kernel은 smooth backward-Euler equality residual과
interval/Krawczyk 인증을 사용한다. 이 문서에서 complementarity 문제를
새로 도입하지 않는다. 모든 식은 같은 fixed grid/cutoff/guard branch와
유효 gas domain에서의 미분이다.

Gas y=(x,y1,y2,w), endpoint photon numerator N_j, step d에 대해

\[
\kappa_j(y)=cn_H[(1-x)\sigma_{H,j}
+f_{\rm He}(1-y_1-y_2)\sigma_{HeI,j}
+f_{\rm He}y_1\sigma_{HeII,j}],
\quad D_j=1+d\kappa_j,
\]
\[
P_j=N_j/D_j,\qquad
G(y;y_0,N,\lambda)=y-y_0-d\bar F(y,N;\lambda)=0.
\]

D_j>0 및 invertible G_y를 요구한다. 모든 rate/threshold/density/time
identity는 원 endpoint와 같아야 한다. y0,N의 parameter derivatives는
이전 상태에서 remap/birth/grouping을 거쳐 온 값이다.

## 2. 분모와 이전 photon 감도

a=lambda, b=source amplitude에 대해

\[
P_a=(N_a-PD_a)/D,\qquad P_b=(N_b-PD_b)/D,
\]
\[
\boxed{
P_{ab}=
(N_{ab}-PD_{ab}-P_aD_b-P_bD_a)/D.
}
\tag{1}
\]

N=0에서도 D>0이면 잘 정의된다. N이나 old stock으로 나누지 않는다.
Signed N_a,N_b,N_ab를 positivity clip하지 않는다.
D_ab에는 y의 mixed tangent W가 들어가므로 gas와 photon을 따로
상수로 미분하는 근사는 사용하지 않는다.

G_y=A라 하고 직접 parameter forcing만 넣은 G_a,G_b를 만들면
\[
AU=-G_a,\qquad AV=-G_b.
\]
그 뒤 y를 (value,U,V,0)의 혼합 jet으로 넣어 얻은 mixed residual r_ab에 대해
\[
\boxed{AW=-r_{ab}.}
\tag{2}
\]
r_ab는 기존 y0_ab, N_ab, gas Hessian, gas-photon cross derivatives와
HH strength derivative H_y V를 모두 포함한다.

Reduced RHS는 N에 선형이므로 F_NN=0이지만, F_yN과 F_yy는 일반적으로
0이 아니다. q(T)의 gas/He/energy Hessian과 photo denominator Hessian을
생략하면 식 (2)의 실제 model derivative가 아니다.

## 3. 이 패킷의 구현과 실제 owner의 연결

src/implicit_mixed.py는 D2(value,a,b,ab) 대수, 4x4 선형 풀이,
photon 제거, H/He photo stoichiometry, excess heat 및
HH의 (+q,-chi_H q) 연결을 구현한다. Nonphoto와 HH rate는 callback으로
주입한다. Production의 실제 FT03/LCS interval callback을 이 패킷에서
새로 구현하거나 native kernel에 연결한 것은 아니다.

mixed_at_candidate는 주어진 endpoint candidate에서 산술 감도를 만든다.
Root를 찾거나 원 native certificate를 발급하지 않는다.
반환된 primal residual, Jacobian, U,V,W와 감도 residual은 실제 root/tube,
interval inverse 및 source identity와 별도로 검증해야 한다.
Point Gaussian elimination 결과는 uniform parameter inverse bound가 아니다.

원 source의 linked_tangent_stage는 lambda-only incoming forcing와 고정
4x4 preconditioner inclusion을 준비해 둔 상태다. Local Codex는
이를 b와 ab까지 확장하고, 원 hh_interval_source와 hh_rate_jet의
Hessian/cross derivative 경로를 연결해야 한다.
Root/tube rectangle, strict inclusion, contraction 및 producer identity가
확보되기 전에는 실제 finite mixed sign을 승격하지 않는다.

## 4. 새 검산

tests/check_implicit_mixed.py는 사전에 정한 4-gas mixed polynomial family를
exact root family로 택하고, 별도의 dictionary-polynomial 표현으로
그 family를 만족시키는 incoming y0를 구성한다. Candidate는 D2와
generic elimination을 사용한다. H/He photo/heat 구조와 비선형 gas,
thermal HH surrogate를 모두 보존하되, 이 fixture는 실제 physical dataset이 아니다.

6개 case의 U,V,W 72개 rational slot이 prescribed derivative와 일치하고
primal/a/b/ab residual 96개가 정확히 0이다. N0=0이면서 signed derivative가
nonzero인 case를 포함한다. Singular Jacobian, zero denominator,
nonpositive photon denominator, sigma/threshold mismatch 네 경우를 거절한다.

두 경로는 source model 구조와 rational fixture를 공유한다.
같은 candidate를 다른 wrapper로 호출한 검증은 아니지만, 실제 provider
RHS의 독립 구현 검증도 아니다. Nonlinear root solve/IVP/native call은 0이다.
최초 실행 exit0 기록은 RUN_IMPLICIT_FIRST.json 및 logs/implicit_first.*,
정확 결과는 results/IMPLICIT_MIXED_EXACT_V1.json에 있다.
