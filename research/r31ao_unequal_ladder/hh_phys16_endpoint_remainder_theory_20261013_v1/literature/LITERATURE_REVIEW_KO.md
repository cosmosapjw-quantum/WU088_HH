# WU088_HH PHYS16 — 문헌과 직접 유도의 대응

검색일: 2026-10-13 KST. 범위: PHYS15의 상관된 endpoint 잔차를 실제 endpoint Jacobian과 source Hessian 나머지로 평가하는 이론 연결. Exa 검색 5회(요청 결과 수 합계 25), SciSpace 자연어 검색 1회(실제 반환 10개 레코드)를 수행했다. Exa 반환 수는 검색 후보 수이며 서로 독립적인 논문 수가 아니다. 핵심 문헌은 아래 5개다. 검색 후보·중복·접근 결과는 SEARCH_PROVENANCE.json에 기록한다.

## 1. 판정과 실제 기여

현재 PHYS15의 잔차, 평균 Jacobian, 유한 온도식은 같은 COMMON·고정 계수 계열에서 직접 유도되어 있다. 문헌과의 대응은 다음과 같다.

- 잔차의 전처리, 평균 Jacobian, 성분별 선형 포함은 검증 수치해석의 표준 결과다.
- 관측량 covector로 residual을 가중하는 adjoint 표현은 DWR 계열의 표준 원리다.
- PHYS16이 실제로 더할 내용은 원 HH source의 정확한 Hessian·광자 유리식을 이용하여 미지 평균 Jacobian을 endpoint에서 평가한 행렬과 계산 가능한 나머지로 옮기는 구성이다.
- 같은 입력의 작은 차이를 유지하는 일곱 광자 항, 원 nonphoto/HH 정규화, 정확한 온도 분모, HI 단일 열 구조의 결합은 이 프로젝트의 직접 유도 및 적용으로 서술한다.

채택할 원고 문장: “표준 잔차 전처리와 목표 관측량 adjoint 원리를 사용하여, WU088_HH의 동일 COMMON Full–two-half 결함에 대한 endpoint 평가식과 유한 나머지 포함을 구성한다.”

이 결과의 문헌상 위치는 위 다섯 원문을 대상으로 비교했다. 본 기록은 보편적 최초성을 주장하는 근거로 사용하지 않는다. PHYS16은 현재 고정된 원 source 계열의 구성과 검증을 완료 기준으로 삼는다.

## 2. 핵심 원전 대응

| ID | 원전·읽은 위치 | 적용할 결과와 가정 | PHYS16 대응·채택 상태 |
|---|---|---|---|
| L1 | S. M. Rump, *Verification methods: Rigorous results using floating-point arithmetic*, Acta Numerica 19 (2010), 287–449. DOI 10.1017/S096249291000005X. 저자 PDF의 Thm 10.2, 10.6, 10.8, 13.1–13.3; §11.3–11.6. | 전처리 잔차에 대한 노름 상계, interval linear solve, C1 함수의 Jacobian 포함과 Krawczyk 사상. 연산은 포함성을 가져야 하며 정의역은 관련 구간을 포함해야 한다. | 원 C,B,q,S의 재사용과 endpoint 선형식의 검증 근거. 본 프로젝트의 Hessian remainder와 HH/photon 구조는 직접 유도한다. literature-supported. |
| L2 | R. Rannacher, *Adaptive Finite Element Methods for Partial Differential Equations*, arXiv:math/0305006 (2003; ICM 2002 lecture). Props 1–2, Eqs (2.1), (3.3). | 정지점과 Galerkin 조건 아래 Lagrangian의 사다리꼴 적분 표현으로 primal·dual residual 및 cubic remainder를 얻는다. 세 번째 방향 미분이 정의되고 적분 가능한 충분한 정칙성이 필요하다. | 공통 관측량 weight의 근거 계열. 현재 유한 차원 HH 문제는 C2 endpoint Taylor 식을 직접 사용하며 Galerkin 직교성을 추가 가정하지 않는다. literature-supported, 대응 완료. |
| L3 | B. Endtmayer, U. Langer, T. Wick, *Multigoal-oriented error estimates for non-linear problems*, J. Numer. Math. 27(4) (2019), 215–236. DOI 10.1515/jnma-2018-0038. RICAM-Report 2018-08의 Thm 3.1, Rems 3.2–3.4. | 임의 approximate primal/dual에 대한 residual 분해로 비선형 반복 오차와 discretization 오차를 연결한다. 정리의 표시는 C3를 가정하고, Rem 3.2는 경로상의 bounded third derivative 조건을 설명한다. | iteration residual을 별도 보존해야 한다는 설계 비교에 사용한다. 조회한 preprint Eq (6)의 부호는 아래 선형 대입과 충돌한다. 해당 표시식을 PHYS16 증명의 전제로 수입하지 않고 직접 Taylor 유도로 부호를 고정한다. |
| L4 | A. K. Alekseev, I. M. Navon, *Adjoint correction and bounding of error using Lagrange form of truncation term*, Computers & Mathematics with Applications 50 (2005), 1311–1332. DOI 10.1016/j.camwa.2005.05.004. 저자 PDF §2.1, Eqs (14)–(21). | Lagrange 형태의 truncation term을 adjoint로 보정하고 Hölder 부등식으로 남은 항을 추정한다. 제시된 실용 경계는 미분 근사 및 adjoint 정확도에 의존한다. | 보정항·남은 오차·adjoint solve error를 각각 보존하는 구조의 비교. PHYS16의 directed interval 포함은 원 HH의 C2 Hessian 및 선형 solve residual로 별도 유도한다. literature-supported 비교 문헌. |
| L5 | J. Sherman, W. J. Morrison, *Adjustment of an Inverse Matrix Corresponding to a Change in One Element of a Given Matrix*, Ann. Math. Statist. 21(1) (1950), 124–127. DOI 10.1214/aoms/1177729893. 공식 Project Euclid 서지와 원 스캔 endpoint 확인. | 한 원소의 변경에 따른 inverse update의 역사적 원전. 원 스캔은 도구에서 본문 텍스트가 추출되지 않았다. | 일반 uvᵀ update는 아래 자체 곱셈 증명을 근거로 사용한다. A0 가역성과 δ=1+vᵀA0⁻¹u≠0를 명시한다. 서지는 확인, 현재 식은 derived. |

원문:
- L1: https://www.tuhh.de/ti3/paper/rump/Ru10.pdf
- L2: https://arxiv.org/pdf/math/0305006
- L3: https://www.ricam.oeaw.ac.at/files/reports/18/rep18-08.pdf
- L3 최종 출판 서지: https://www.degruyterbrill.com/document/doi/10.1515/jnma-2018-0038/html
- L4: https://people.sc.fsu.edu/~inavon/pubs/CAM2005.pdf
- L5: https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-21/issue-1/Adjustment-of-an-Inverse-Matrix-Corresponding-to-a-Change-in/10.1214/aoms/1177729893.full

## 3. 원고에 바로 연결할 수 있는 유도

상세 식은 ENDPOINT_BRIDGE_NOTE_KO.md에 있다. 핵심은 g2의 한 번 평가를 중심으로 하는 정확한 항등식이다. J2=DH_F(g2), d=g2−gF, r=H_F(g2)라 두면

\[
0=H_F(g_2-d)=r-J_2d+\mathcal R_2(d),
\qquad
\mathcal R_2(d)=\int_0^1(1-s)D^2H_F(g_2-sd)[d,d]\,ds.
\]

따라서 J2 d=r+R2이며, v=J2⁻¹r로 정의한 선형 보정은 d=v+J2⁻¹R2를 만족한다. 이 유도는 원 C2 전제와 동일한 convex 구간에서 성립한다.

아무 approximate linear solve ṽ에 대해서도
\[
\eta=r-J_2\widetilde v,\qquad
d-\widetilde v=J_2^{-1}(\eta+\mathcal R_2)
\]
이므로 구현의 solve residual과 물리 비선형 나머지를 같이 포함할 수 있다.

고정 선형 관측량 row ℓ와 임의 approximate adjoint z̃에 대해서는
\[
\zeta=\ell^T-J_2^T\widetilde z,\qquad
\ell d=\widetilde z^Tr+\widetilde z^T\mathcal R_2+\zeta^Td.
\]
이 식은 원 endpoint 행렬·원 잔차·Hessian 상계·기존 d cap으로 계산 가능하다. 온도는 PHYS15의 정확한 유한 분모와 연결하거나 온도 자체의 C2 나머지를 별도로 포함한다.

이 세 식의 부호·정칙성은 PHYS16의 직접 증명 대상이다. L1–L4는 이를 기존 수치해석 원리와 연결하는 출처다.

## 4. 조회한 preprint 표시식의 부호 점검

L3의 RICAM-Report 2018-08, Eq (6)는 조회한 PDF text와 ar5iv의 LaTeX 표현에서 −ρ(ũ)(z̃)를 포함하고 Eq (7)은 ρ(ũ)=−A(ũ)를 정의한다. 다음 정확한 선형 대입은 이 표시식의 부호를 판별한다.

U=V=R, A(u)(v)=uv, J(u)=u, 실제 근 u=0, exact adjoint z=1, approximate 값 ũ=1,z̃=1을 선택한다. 모든 함수는 C∞이고 두 adjoint residual 및 cubic remainder는 0이다. 실제 목표 차이는 −1이다. 표시식 Eq (6)의 우변은 −ρ(1)(1)=+1이다.

따라서 조회한 preprint 표시식 그대로의 Eq (6)는 이 대입을 만족하지 않는다. L=J−A z의 정의에서 직접 전개하면 마지막 항은 +ρ(ũ)(z̃)가 된다. PHYS16의 증명은 독립적인 endpoint Taylor 식에서 시작하며 이 표시식에 의존하지 않는다.

범위: 실제 조회한 RICAM-Report 2018-08 및 arXiv 계열의 텍스트 표현. 최종 journal 본문은 인증벽으로 내용을 확인하지 못했다. PDF 이미지 확인 요청은 fetch timeout으로 끝났다. 따라서 이 지적은 조회된 preprint 식의 일관성 판정으로 기록한다. 정확한 유리수 대입의 실행 기록은 PREPRINT_SIGN_CHECK.json에 있다.

## 5. PHYS16에서 닫아야 할 구체적 의무

1. J2와 source Hessian을 원 temperature/electron normalization에서 완전히 전개한다.
2. d를 포함하는 기존 cap 및 [g2]−[d]의 경로를 원 X와 연결한다.
3. R2의 componentwise quadratic bound, photo rational remainder, 현재 solve의 η·ζ를 계산식으로 연결한다.
4. 온도의 정확한 분모, source의 chemical-energy 사영, 실제 photon secant를 동일 d와 연결한다.
5. rank-one 경로를 채택하면 A0의 가역성 및 δ의 분리 상계를 근거와 함께 확인한다. 기존 full C 경로는 별도로 그대로 유지할 수 있다.
6. 일반 정리의 채택과 실제 물리 입력에서 얻을 수치 폭을 각각 기록한다.

문헌 비교는 위 의무를 바꾸거나 원 physical source를 다시 실행하는 이유가 되지 않는다. 그대로 유지되는 PHYS15 원 잔차·source·근 및 C,B,q,S 근거는 재사용한다.

