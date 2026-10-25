# PHYS91 — 전체 covariance formatting cell의 정확한 PSD 인증

## 1. 이번 질문과 완료 근거의 재사용

부모 PHYS90 FINAL은 `9d32d115c0b8c5d5b2ce3a66ebc4a7f277334fcc`다. PHYS89가 원문에서 정확히 해독한 현재 ENDF H-1 MF33/MT102의 대칭 표시행렬 \(F\in\mathbb Q^{153\times153}\), token별 halfULP 행렬 \(H\)와 PHYS90의 exact pair 결과를 그대로 읽는다. 이는 PHYS88의 153 native knots/152 interpolation cells와 서로 다른 데이터 구조다. 원 ENDF decode, raw \(F\) eigensolve, pair scan, 기존 nominal integrals를 실행하지 않는다.

PHYS90은 모든 singleton·2×2 principal block의 조건부 가능성을 닫았다. 그 결과는 \(t_{\rm pair}\)의 정확한 bracket이며 전체 PSD 가능성의 충분조건이 아니다. 이번 질문은 하나다.

\[
\mathcal B_t=\{C=C^T: |C_{ij}-F_{ij}|\le tH_{ij}\},\qquad
t_*=\inf\{t\ge0:\mathcal B_t\cap\mathbb S_+^{153}\ne\varnothing\}.
\]

원 token의 halfULP는 **가정한 nearest-formatting의 닫힌 셀**이다. 실제 formatter guarantee, confidence region, source-approved correction은 아니다. \(F,H\)의 SHA와 dimension은 계약의 입력이다. 실제 데이터에서는 모든 \(H_{ij}>0\)를 exact arithmetic으로 확인한 뒤 아래 distance 정리를 적용한다.

## 2. 가중 entry norm과 정확한 support

대칭 공간에 trace pairing \(\langle A,B\rangle=\operatorname{tr}(AB)\)를 쓴다. \(H_{ij}>0\)일 때

\[
\|E\|_{\infty,H}=\max_{i\le j}\frac{|E_{ij}|}{H_{ij}},\qquad
h_H(Y)=\sum_iH_{ii}|Y_{ii}|+2\sum_{i<j}H_{ij}|Y_{ij}|.
\]

독립변수는 upper-triangle entry다. 따라서 off-diagonal 계수는 \(2Y_{ij}\)다. 각 entry의 endpoint를 그 계수의 부호에 맞춰 선택하면

\[
\max_{C\in\mathcal B_t}\langle Y,C\rangle
=\langle Y,F\rangle+t\,h_H(Y)
\]

를 정확히 달성한다. 이는 PHYS90의 symmetric shared-entry support 식을 일반 PSD dual 행렬에 적용한 것이다. \(Y=\sum_a w_aw_a^T\)일 때 먼저 합한 \(Y_{ij}\)에 절댓값을 취한다. \(\sum_a h_H(w_aw_a^T)\)로 대체하면 entry cancellation을 잃어 더 약한 검사가 된다.

## 3. Primal–dual distance 정리

모든 \(H_{ij}>0\)인 경우

\[
\boxed{\quad
t_*=\min_{C\succeq0}\|C-F\|_{\infty,H}
=\max_{\substack{Y\succeq0\\h_H(Y)\le1}}-\langle F,Y\rangle .
\quad}
\]

Primal의 유한 feasible point는 임의의 \(\lambda>0\)에 대한 \(C=\lambda I\)와 충분히 큰 \(t\)로 구성된다. \(C=\lambda I\succ0\), \(t>\|C-F\|_{\infty,H}\), \(t>0\)를 택하면 PSD와 모든 entry 부등식에 strict slack이 있으므로 이 SDP의 Slater 조건을 직접 확인한다. \(0\le t\le t_0\)인 feasible sequence에서는 모든 \(C\) entry가 유계이며 closedness 때문에 최소가 달성된다.

약한 쌍대성은 계산으로도 즉시 확인된다. \(C\succeq0,\ Y\succeq0\)이면 \(\langle C,Y\rangle\ge0\)이고

\[
-\langle F,Y\rangle
\le\langle C-F,Y\rangle
\le\|C-F\|_{\infty,H}h_H(Y).
\]

Slater에 따른 강한 쌍대성으로 양쪽 최적값이 같다. \(h_H\)가 norm이고 \(Y\succeq0,\ h_H(Y)\le1\)인 집합은 compact이므로 dual 최대도 달성된다. \(t_*=0\)일 때에는 \(Y=0\)이 최대0을 보장한다. 이 주장은 일반 SDP에서 모든 infeasibility가 단순한 strict separator를 갖는다는 주장이 아니다. 여기서는 양의 \(H\)를 갖는 distance 문제의 Slater 조건을 실제로 구성했다.

고정된 \(\mathcal B_t\)는 compact이다. 따라서 PSD cone과 만나지 않으면 strict separation이 가능하며, cone의 self-duality에 의해 \(Y\succeq0\)인 separator를 쓸 수 있다. 일반적인 unbounded affine SDP의 weak infeasibility를 이 compact cell에 옮겨 해석하지 않는다.

## 4. 완성된 유리수 인증서가 주는 두 endpoint

### 4.1 Primal

정수행렬 \(V\in\mathbb Z^{n\times r}\), 양의 정수 \(q\), 유리수 \(d_i\ge0\)를 받아

\[
C=\frac{VV^T}{q^2}+\operatorname{diag}(d)
\]

로 정의한다. 모든 실수 \(x\)에 대해 \(x^TCx=\|V^Tx\|^2/q^2+\sum_i d_ix_i^2\ge0\)이므로 PSD는 exact다. 이후

\[
\alpha=\max_{i\le j}\frac{|C_{ij}-F_{ij}|}{H_{ij}}
\]

를 모든11,781 upper entries에서 exact 계산하면 \(t_*\le\alpha\)다. \(C\)의 float eigenvalue나 Cholesky 성공을 근거로 삼지 않는다. Diagonal padding을 포함한 최종 \(C\)가 모든 부등식의 대상이다.

### 4.2 Dual

정수 \(W\ne0\), 양의 \(q\)로 \(Y=WW^T/q^2\succeq0\)를 만든다. 실제 양의 \(H\)에서는 \(h_H(Y)>0\)이며

\[
\beta=-\frac{\langle F,Y\rangle}{h_H(Y)}
\quad\Longrightarrow\quad t_*\ge\max(0,\beta).
\]

\(\langle F,Y\rangle+t\,h_H(Y)<0\)이면 모든 \(C\in\mathcal B_t\)가 \(\langle Y,C\rangle<0\)이어서 PSD일 수 없다. 단일 \(ww^T\)에 제한하지 않고 \(r\le153\)의 일반 Gram dual을 허용한다.

### 4.3 닫힌 셀의 endpoint 의미

- \(\alpha\le1\): \(\mathcal B_1\) 안의 PSD 존재가 인증된다. \(\alpha=1\)도 포함된다.
- \(\beta>1\): \(\mathcal B_1\)의 PSD 부재가 인증된다. 엄격한 부등식이다.
- \(\beta=1\): \(t_*\ge1\)일 뿐이며 \(t_*=1\)의 가능성을 배제하지 않는다.
- 두 조건을 모두 얻지 못하면 B1은 UNRESOLVED다. 별도로 얻은 유효한 거리 enclosure는 유지한다.
- 유효하다고 주장한 \(\beta>\alpha\)가 생기면 두 인증서나 입력 해석이 모순이다. tolerance로 덮지 않고 STOP_NO_ADMISSION으로 분류한다.

PHYS90의 strict lower endpoint \(\ell=34406736621/68719476736\)는 재계산 없이 \(t_*>\ell\)로 승계한다. 새 \(\beta\)는 closed lower bound다. \(\max(\ell,\beta)\)의 endpoint openness를 합성 시 보존한다. PHYS90의 pair upper endpoint를 전체 PSD upper bound로 쓰지 않는다.

## 5. Strict slack과 유리수 인증 가능성

\(t>t_*\)이면 minimizer \(C_*\)에 충분히 작은 양의 \(\epsilon I\)를 더해 positive definite 및 strict cell slack을 동시에 얻는다. 그 Cholesky factor를 유리수로 충분히 가깝게 근사한 \(Q\)는 \(QQ^T\)도 셀 내부에 있게 한다. 따라서 boundary 밖의 feasible radius에는 rational Gram primal 인증서가 존재한다.

\(t<t_*\)이면 strict separator의 음의 여유가 있다. 그 PSD factor를 유리수로 충분히 가깝게 근사해도 연속인 \(\langle F,Y\rangle+t h_H(Y)\)의 부호가 유지되므로 rational Gram dual 인증서가 존재한다. 이는 어떤 고정 denominator·유한 반복 수·현재 탐색법이 그 인증서를 찾는다는 보장이 아니다. \(t=t_*\)의 boundary는 strict slack이 없을 수 있어 유한 rational search의 종료를 주장하지 않는다.

이번 \(q=2^{48}\)은 저장 표현의 선택이며 물리 tolerance나 formatter precision에 대한 가정이 아니다. Quantization으로 인증에 실패하면 해당 후보가 실패한 것이다. 미리 동결한 \(q\), cell, budget을 사후에 바꾸지 않는다.

## 6. Upper diagonal 구성과 Schur 대안

고정 \(t\)에서 \(U_i=F_{ii}+tH_{ii}\)라 두자. PSD feasible \(C\)가 있으면
\(C+\operatorname{diag}(U_i-C_{ii})\)도 PSD이고 셀 안에 있으므로 diagonal을 \(U\)로 고정해도 **존재 문제**를 바꾸지 않는다.

\(U_i<0\)이면 \(e_ie_i^T\)가 즉시 separator다. \(U_i=0\)인 PSD 행렬의 \(i\)행은 전부0이어야 하므로 관련 off-diagonal interval이0을 포함해야 한다. 실제 양의 \(U\)일 때에는 correlation scaling을 후보 탐색에 쓸 수 있지만 최종 검사는 원 \(F,H\) 좌표에서 수행한다.

별도 constructive 충분조건으로, rational \(A\succ0\), cross block \(B\), \(D\ge0\)를 정하여
\[
C=\begin{pmatrix}A&B\\B^T&B^TA^{-1}B+D\end{pmatrix}
\]
를 만들면 Schur complement로 PSD다. 모든 entry가 셀에 들어오는지 exact 검사해야 한다. 이 대안은 이론으로 보존하며 이번 동결 실행은 Gram+diagonal 경로만 사용한다. 대안을 추가 실행하는 허용량은 없다.

## 7. 실행 가능한 유한 candidate 설계

Dykstra의 두 집합은 PSD cone과 upper diagonal을 고정한 대칭 interval box다. 반경은 \(\rho=255/256\), 이어 \(\rho=1\)로 미리 정한다. 각 최대2,048, 총4,096개의 changed-candidate projection만 허용한다. 초기행렬의 diagonal은 원 \(F_{ii}\) 대신 \(U_i=F_{ii}+\rho H_{ii}\)이며 원 raw \(F\)의 spectrum을 다시 계산하지 않는다.

Floating scaling과 eigensolve는 후보 생성만 담당한다. Positive modes로 primal factor, negative modes 전체로 general dual factor를 만든다. Dual factor는 양의 공통배율로 rescale 후 quantize할 수 있다. 매256회와 stage 끝에서 제한된 후보만 exact 검사한다. Primal의 padding은 \(d_i=\max(U_i-\sum_kV_{ik}^2/q^2,0)\)으로 정의하여 PSD를 항상 보존하고, 이에 따라 cell을 벗어난 diagonal도 exact \(\alpha\)에 반영한다.

Primary가 정확한 B1 인증서를 얻으면 남은 탐색은 즉시 중단한다. 얻지 못하더라도 유효한 Gram primal과 general dual의 exact endpoint를 남긴다. 알고리즘의 수렴, global optimum 근접도, 최소 rank, source 승인 보정을 주장하지 않는다. CPU soft stop은 numerical result의 대체가 아니다. 완료된 exact certificate와 후보 이력만 검증 대상으로 승계한다.

## 8. Zero-width와 반례 검사의 범위

\(H_{ij}=0\)이면 해당 entry는 고정이며 \(|C_{ij}-F_{ij}|/H_{ij}\)를 계산해서는 안 된다. \(h_H(Y)=0\)인 dual도 별도다. \(\langle F,Y\rangle<0\)이면 모든 유한 \(t\)를 배제하지만, 음수가 아니면 그 dual은 bound를 주지 않는다. 양의 \(H\)로 증명한 Slater·compact dual·rational interior 정리를 zero-width 입력에 무조건 적용하지 않는다.

작은 fixture는 PSD Gram의 exact 보존, 잘못된 negative padding 거부, signed trace/support, combined-entry cancellation, \(\alpha=1\)/\(\beta=1\) boundary, input identity/shape/sign/finite-token guard를 검증한다. Manufactured fixture의 결론을 실제153행렬로 옮기지 않는다. 실제153행렬의 판정에는 해당3개 pinned input과 그 행렬에서 생성·독립 검증한 인증서가 필요하다.

## 9. Named consumer와 물리적 해석

이 finite child의 \(C\)는 source 승인 stochastic covariance가 아니다. 만일 앞으로 source가 실제 covariance \(C_{\rm phys}\)의 identity·nominal binding·confidence convention을 공급하고 동일한 linear consumer map \(L\)을 승인한다면 \(K=L C_{\rm phys}L^T\succeq0\)다. Signed conservation row \(a^TL=0\)이면 \(a^TK=0\), \(Ka=0\)이다. 서로 다른 consumer가 독립적으로 covariance를 뽑는 계약은 이 공통 보존식과 다르다. PHYS90의 common-entry envelope는 그대로 재사용한다.

B1 존재 인증은 formatter가 실제 nearest rounding을 했다는 증거가 아니다. B1 부재 인증은 가정한 rounding box만 배제하며, 원 평가모형 전체나 실제 nuclear process의 불가능성을 말하지 않는다. 두 경우 모두 actual atomic→bare kernel, evaluator mass/target/electron-state deck, energy support/tail \(B_0,B_A\), named thermal/fast/radiation measure·clock·density·ownership ACK는 별도로 필요하다.

PHYS88의 signed convention carrier는 heat나 실제 electron이 아니다. Same-event carrier와 fresh bare two-body event를 합치지 않는다. 원 native153knots/152cells 보존, 네 온도의 conditional ppm 비교, 실패 artifact 및 exact 원bytes 복구 이력은 완료 근거로 재사용한다.

## 10. Claim gate와 독립 검증

NG1의 quantified object는 정확한 \(F,H,t\)가 정하는 유한 \(\mathcal B_t\)다. NG2는 Gram PSD와 signed support의 exact 부호다. NG3은 \(\mathcal B_t\) 자체가 비어 있지 않으며 실제 원행렬의 inputs를 썼는지 확인한다. NG4의 mechanism은 PSD cone과 entry cell의 분리다. NG5는 그 조건부 후보를 stochastic supplier로 쓸 수 있는지에 대한 gate이며 physical source cause를 확정하지 않는다. NG6은 interval matrix의 existential/robust 구별과 SDP strong duality의 원전과 비교한다. NG7은 별도 R6 proof 검토 및 production kernel을 import하지 않는 exact reference의 actual 검사다.

표시행렬의 원 negative witness는 이미 완료됐다. 이번에 원인 NOT_ESTABLISHED를 해소했다고 주장하지 않는다. 검색 실패·정해진 탐색의 인증 실패·runtime cap은 물리적 no-go가 아니다. Primary proposal과 exact certificate, independent reference, final artifact integrity는 서로 다른 검증 층이다.

## 11. 원전과 신규성의 위치

- L. Vandenberghe and S. Boyd, *Semidefinite Programming*, SIAM Review38(1),49–95(1996), DOI10.1137/1038003, [author PDF](https://web.stanford.edu/~boyd/papers/pdf/semidef_prog.pdf). PSD cone, trace duality와 strict feasibility의 표준 기반이다.
- M. Hladík, *Positive Semidefiniteness and Positive Definiteness of a Linear Parametric Interval Matrix* (2017), [arXiv1704.05782v2](https://arxiv.org/abs/1704.05782v2), DOI10.1007/978-3-319-61753-4_11. “어떤 행렬이 PSD”와 “모든 행렬이 PSD”를 분리한다.
- S. M. Rump, *Verification of Positive Definiteness*, BIT46,433–452(2006), [author PDF](https://www.tuhh.de/ti3/paper/rump/Ru06c.pdf). Floating 제안과 반올림 오차를 포함한 검증을 분리할 문헌 맥락이다. 이 논문의 특정 수치 criterion을 이번153행렬에 실행했다는 뜻은 아니다.

일반 duality 자체를 새 정리라고 주장하지 않는다. 이번 연구의 새 obligation은 이미 동결된 actual153-entry source에 대해 전체 PSD distance의 재현 가능한 exact primal/dual certificates를 만들고 consumer admission의 정확한 범위를 결속하는 것이다.

## 12. 불변 물리·자원 경계

Non-tilted LRS Bianchi I, metric(-+++), reacting gas \(\pi=0\), collisionless DM \(\pi_m\)은 별도다. 같은 normal orthonormal frame의 signed matter/radiation tensors를 합한 뒤 norm을 취한다. Frobenius는 \(\sqrt2\)×half-contraction이다. 동일 trajectory의 성분 분석은 species-off 인과 실험이 아니며 sampled quadrature/energy residual은 continuum certificate가 아니다.

새 ODE0, benchmark0, nuclear rate activation0, fast stopping0. HH_R10 OFF, production NOT_ISSUED, global physical completion null. 새 별도 identity의 primary1/reference1/Wolfram1만 계약으로 부여하며 완료된 모든 허용량0, budget reset=false를 유지한다. 원 공유 lease와1worker/thread를 사용하고 다른 process를 종료하지 않는다.

## 부록 A. 모든 rank-one 검사가 실패하는 4×4 manufactured fixture

독립 이론 검토자가 유도한 다음 예를 root가 식으로 검토하고 이번 계약의 exact fixture로 채택한다. 실제153행렬의 결론은 아니다.

\[
S=\begin{pmatrix}
0&1&0&-1\\1&0&1&0\\0&1&0&1\\-1&0&1&0
\end{pmatrix},\quad S^2=2I,\quad F_{\rm fx}=I+S.
\]
\(H_{\rm fx}\)는 diagonal 및 cycle edges12,23,34,41에서 \(1/10\), nonedges13,24에서1이다. \(W=I-S\), \(Y=WW^T=3I-2S\)이면
\[
\operatorname{tr}(F_{\rm fx}Y)=-4,\quad
h_{H_{\rm fx}}(Y)=14/5,\quad
\beta=10/7,\quad
\operatorname{tr}(F_{\rm fx}Y)+h(Y)=-6/5.
\]
\((I-S)(I+S)=-I\)이므로 \(W\)는 invertible이고 \(Y\)는 rank4다. 반면 네 column의 support를 각각 합하면 \(54/5\)로서, full matrix를 합한 뒤의 \(14/5\)와 다르다.

더 강하게 모든 rank-one separator가 실패한다. Nonedge에서만1이고 다른 entry는0인 \(H_0\le H_{\rm fx}\)를 두자. 임의의 \(w=D_s x\), \(x_i=|w_i|\ge0\), \(s_i\in\{\pm1\}\)에 대해 \(w^TF_{\rm fx}w+h_{H_0}(ww^T)=x^TA_sx\)다. \(A_s\)의 diagonal은1, cycle edge는 \(D_sSD_s\)의 부호, nonedge는+1이다. Signed cycle의 edge product는−1이므로 negative edge는1개 또는3개이며 forest를 이룬다. 그 forest를 two-color해 negative edge마다 \(v_iv_j=-1\)인 \(v_i\in\{\pm1\}\)를 택하면 \(A_s-vv^T\)가 entrywise nonnegative다. 따라서 \(x^TA_sx\ge(v^Tx)^2\ge0\). \(H_{\rm fx}\ge H_0\)이므로 \(w^TF_{\rm fx}w+h_{H_{\rm fx}}(ww^T)\ge0\)가 모든 \(w\)에 대해 성립한다.

이 예가 닫는 것은 rank-one-only 검색의 일반적 불충분성이다. PSD 행렬이 rank-one 합으로 분해된다는 사실만으로 support의 절댓값을 분해별 합과 교환할 수 없다. 유한 scalar/matrix identities는 이번 Wolfram과 독립 checker에서 검증하되 모든 \(w\)에 대한 명제는 위 forest 증명으로 닫는다.


