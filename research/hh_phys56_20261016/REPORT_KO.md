# PHYS56 — 실제 비중심 screened exterior DtN의 구성 의무

## 판정

`CONDITIONAL_OPERATOR_CONSTRUCTION_ONLY` — PHYS55의 collar + 중앙 Coulomb
hybrid 가역성을 실제 screened exterior의 정리로 승격하지 않았다.
`rei_bianchi HH_R10=OFF`를 유지한다.

## 고정 입력과 실행 범위

- 원래 spectator Hamiltonian은
  \(h=-\frac12\Delta-r^{-1}-(1+s^{-1})e^{-2s}\),
  \(s=|\mathbf x-\frac7{10}\hat z|\) 그대로다.
- `FROZEN_U_SUBSET.npz`의 SHA-256은
  `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`로
  source gate를 통과해야 한다. 배열을 재생성하거나 바꾸지 않았다.
- `eta=Fy`, `xi=Fy-phi`와 Coulomb parameter `eta_C=-10/7`를 혼동하지
  않았다. 이 단계는 driven source, \(\sigma(E)\), \(k_{HH}(T)\)를 계산하지 않는다.
- 표준 라이브러리 Python 경량 검증만 실행한다. NCP 대형 계산은 이 구성식 단계에
  필요하지 않아 `NOT_RUN_NOT_REQUIRED`이다.

## 실제 all-angular 구성식

외부 \(r\ge27\)에서 Coulomb 기준 연산자 \(A_C\)와 원래 screened 곱셈
\(V=2(1+s^{-1})e^{-2s}\)를 둔다. \(0<a<1\)에서
\(H_{\pm a}=L^2(e^{\pm2a(r-27)}drd\Omega)\)를 사용한다. 다음 네 가지가
독립적으로 증명되었다고 **가정할 때만**:

1. outgoing Coulomb Dirichlet LAP
   \(R_C^+:H_{+a}\to H_{-a}\),
2. weighted boundary Poisson bounds and the unweighted-volume-pairing dual
   transpose \((P_C^-)^*:H_{+a}\to X^*\),
3. \(I-R_C^+V\)의 가역성 (또는 Fredholm+uniqueness),
4. 해당 resolvent domain에서 Green identity의 trace 정칙성,

Lippmann--Schwinger 방정식과 DtN 차이는

\[
 u_S=(I-R_C^+V)^{-1}P_C^+g,
 \qquad
 (Z_S-Z_C)g=(P_C^-)^*V(I-R_C^+V)^{-1}P_C^+g.
\]

이다. \(u=r\psi\), \(Z=+\partial_r\) convention에서
\(A_S=A_C-V\)로 쓰면 Green identity가 표시된 `+` 부호를 준다.
여기서 \((P_C^-)^*\)는 \(H_{-a}\)의 weighted Hilbert adjoint라고 부르지 않는다.
\(Vu\in H_{+a}\)에 작용하는 unweighted volume pairing의 dual transpose다.
이는 조건부 보조정리의 정확한 연산자 표현이며, 위 네 항목은 아직 PHYS56에서
증명되지 않았다.

경계 밖에서 \(t=r-27\ge0\), \(s\ge26.3+t\) 이므로 pointwise
\(e^{2at}V(r,\Omega)\le\delta_0e^{-2(1-a)t}\) (`0<a<1`)다. 따라서
\(\|V:H_{-a}\to H_{+a}\|=\sup_{r,\Omega}e^{2at}V\le\delta_0\)이고, 실제 물리식만으로

\[
 \|V\|_\infty\le2(1+1/26.3)e^{-52.6}
 \approx2.97404\times10^{-23}
\]

을 얻는다. 그러나 이것은 DtN 차이의 smallness가 아니다. 독립적으로 인증된
\(C_R,C_{P^-},C_{P^+}\)가 있고 \(q=C_R\|V\|_\infty<1\)일 때에만

\[
 \|W^{-1/2}(Z_S-Z_C)W^{-1/2}\|
 \le {C_{P^-}C_{P^+}\|V\|_\infty\over1-q},
 \qquad W_\ell=\ell+1
\]

가 따라온다. 코드의 단위 상수 평가는 이 함의의 산술 검사일 뿐, 상수의
certificate가 아니다.

## 비중심 \(P\)-\(Q\) 결합을 보존한 식

\(P=\{\ell\le20\}\), \(Q=\{\ell\ge21\}\)로 둔다. 축대칭 displaced
potential은 \(m\)을 보존하지만 \(\ell\)은 결합한다. 따라서
\(V_{PQ}\)와 return coupling \(V_{QP}\)를 생략할 수 없다. (실수 potential의
\(m\leftrightarrow-m\) conjugation symmetry도 보존한다.) 정확한 Feshbach 형태는

\[
 V^{\rm eff}_Q=V_{QQ}+V_{QP}(I-R_PV_{PP})^{-1}R_PV_{PQ},
\]
\[
 (Z_S)_{QQ}=Z_{C,Q}+(P_Q^-)^*V^{\rm eff}_Q
 (I-R_QV^{\rm eff}_Q)^{-1}P_Q^+.
\]

이다. 이 축소식은 \(I-R_PV_{PP}\)와 Q Schur factor의 가역성을 각각 가정한다.
따라서 Q-only collar는 원래 full exterior matching의 증명이 아니다.
full 경계 연산자 \(M\)에서 \(M_{PP}\)가 가역임을 별도 증명한 뒤
\(M_{QQ}-M_{QP}M_{PP}^{-1}M_{PQ}\)를 사용해야 한다. 이 low-block 접합도 OPEN이다.

## 실행 증거

`src/wu088_hh/phys56_screened_exterior.py`는 source hash, 실제 exterior
multiplication bound, 조건부 Neumann 함의, scalar Feshbach 및 full Schur identity를
직접 검사한다. `scripts/phys56_screened_exterior.py`는 결과 JSON을 만든다.
`tests/test_phys56_screened_exterior.py`는 hash/단조성, \(q\) gate, return coupling과
Schur 보존을 검사한다. 결과 JSON은 numerical diagnostic이며 rigorous certificate와
구별한다. JSON의 `neumann_q_lt_one`은 제공된 수가 유한하고 \(q<1\)이라는 산술
predicate일 뿐이며, `operator_constants_certified=false`는 operator norm의 독립
certificate가 아직 없음을 명시한다.

## PHYS55 의존성과 다음 의무

PHYS55는 only `Lambda_D,TT-Z_C` (screened collar + central exterior)의
weighted hybrid 가역성이다. PHYS56가 이를 재사용하는 지점은 target trace weight와
central reference뿐이며, `Z_S`의 존재/유계성/가역성은 새 전제다.

다음 READY DAG는 (i) weighted Coulomb exterior LAP/trace mapping, (ii) screened
Fredholm uniqueness 또는 certified norm, (iii) finite P block 및 full matching Schur,
(iv) 그 뒤에야 original driven source와 observables 순서다.
