# PHYS18 — 혼합 implicit 응답의 문헌 대응

검색·확인일: 2026-10-13 KST. 범위는 동일한 COMMON, 고정 admissible α, 전역 (λ,b)∈[0,1]²에서 두 경로의 결함 d=g₂−gF 및 F=ΔT의 혼합 미분이다. PHYS17에서 원문 확인한 Neumaier 1989, Rump 1990, Goldsztejn 2008, Margossian–Betancourt 2022의 조건·포함 근거는 해당 문헌 검토의 exact identity로 재사용한다. 이번 검색은 2차 implicit sensitivity와 공통 관측량 covector에 집중했다.

## 1. 확인한 선행 결과

| ID | 원전과 실제 읽은 위치 | 채택하는 내용과 현재 대응 |
|---|---|---|
| SLN15 | N. Safiran, J. Lotz, U. Naumann, *Second-order Tangent Solvers for Systems of Parameterized Nonlinear Equations*, Procedia Computer Science 51 (2015), 231–238. DOI 10.1016/j.procs.2015.05.232. RWTH 원 PDF의 §§3.1–4.2, 특히 Thm 4.3, Eq. (7), 인쇄 pp.235–236. | 원 방정식의 2차 미분을 같은 state Jacobian을 쓰는 선형식으로 구성한다. 매개변수 seed를 eλ,eb로 두고 mixed parameter seed를 0으로 두면 현재 JF WF=−B(gF;UF,VF)가 된다. §4.1의 반복 Newton 코드에 대한 2차 AD가 사용하는 3차 residual derivative는 §4.2의 implicit 식에 요구되지 않는다. |
| L97 | R. M. Lewis, *A Nonlinear Programming Perspective on Sensitivity Calculations for Systems Governed by State Equations*, ICASE 97-12, NASA-CR-201659 (1997). §2.3, Thm 2.2, Eqs. (7)–(14), PDF pp.9–12. | C² Fréchet source/observable와 가역 state derivative 아래 tangent injection과 adjoint를 통해 reduced Hessian을 얻는다. 현재 유한 차원 온도 관측량의 정확한 혼합 quotient를 하나의 Full inverse/covector로 수축하는 표준 근거다. |
| P22 | F. Pacaud et al., *Batched Second-Order Adjoint Sensitivity for Reduced Space Methods*, arXiv:2201.00241v1 (2022); 관련 DOI 10.1137/1.9781611977141.6. §§4.1–4.3, Eqs. (4.10)–(4.16), Algorithm 1. | Jacobian/transpose solve와 Hessian의 bilinear contraction을 조합한다. Hessian이 출력 지수까지 포함하여 3-index tensor인 것은 미분 차수가 3이라는 뜻이 아니다. 현재 4-gas/35-photon 구성의 부호·엄밀 구간은 원 입력의 별도 포함 연산에서 얻는다. |
| X25 | T. Xue, *Implicit differentiation with second-order derivatives and benchmarks in finite-element-based differentiable physics*, arXiv:2505.12646v1 (2025). §§2.3–3.3, Eqs. (20)–(24), Algorithm 1. | Incremental state/adjoint 방정식으로 Hessian-vector product를 구하고 finite difference와 Taylor remainder로 검산한다. 현재의 signed interval certificate는 이 논문의 부동소수 검산을 그대로 이식하지 않고 원 C,B,q,S에서 직접 구성한다. |

원문 주소:

- SLN15: https://publications.rwth-aachen.de/record/569704/files/569704.pdf
- L97: https://ntrs.nasa.gov/api/citations/19970015271/downloads/19970015271.pdf
- P22: https://arxiv.org/pdf/2201.00241
- X25: https://arxiv.org/pdf/2505.12646

## 2. 현재 결과로의 직접 연결

H(gF;λ,b)=0을 두 번 미분한다. gF,λ=UF, gF,b=VF, gF,λb=WF라 쓰면

\[
J_F W_F+H_{gg}[U_F,V_F]+H_{g\lambda}V_F+H_{gb}U_F+H_{\lambda b}=0.
\]

각 gas Hessian 항은 방향 두 개를 한 번씩 수축한다. 따라서 혼합항에 Taylor 계수 1/2가 없다. 위 식은 SLN15의 표준 2차 tangent 관계다. d=g₂−gF를 사용하여 JF Wd=JF W+B(gF;UF,VF)를 얻는 단계도 정확한 차이 항등식이다.

현재 과제의 구체적인 기여는 이 식을 WU088_HH의 원 source/carry와 연결하여 작은 d,dλ,db,s,sλ,sb를 먼저 인수 분해하고, photon의 일곱 chronology sector를 같은 λ,b로 미분하며, 정확한 유한 온도 분모를 유지한 실제 외측 구간을 계산하는 데 있다. 일반 implicit Hessian 방법의 신규성은 주장하지 않는다.

## 3. C²에서 Hessian 차를 포함하는 방법

Hgg(g₂)와 Hgg(gF)의 각 성분이 같은 원 범위 [l,u]에 있으면 그 차는 [l−u,u−l]에 있다. 이 사실은 bounded signed range의 집합 차이며, Hgg를 한 번 더 미분하지 않는다. 값이 작은 d에 비례하는 Hessian-Lipschitz 상계를 이 범위만으로 추론하지 않는다. HI의 유리식은 분모 차를 정확히 인수 분해하므로 해당 부분만 명시적인 d 인자를 유지한다. Hgλ의 공간 차에는 q의 원 Hessian을 적분하여 쓸 수 있다.

## 4. Four-corner interaction의 양화

고정 α의 같은 C² 함수 F에 대해 미적분학의 기본정리를 두 번 적용하면

\[
\mathcal I=F(1,1)-F(1,0)-F(0,1)+F(0,0)
=\int_0^1\int_0^1F_{\lambda b}(\lambda,b)\,db\,d\lambda.
\]

단위 정사각형 전체의 혼합 미분 구간은 곧 I의 구간이 된다. 네 점에서 서로 다른 α를 선택하는 식에는 이 대응을 적용하지 않는다. 전역 Fλ 폭에서 얻은 PHYS17의 I 상계를 재사용하여 새 포함과 교차할 수 있다. 0 포함 여부는 실제 계산에서 판정하며, 구간에 0이 있다는 관측만으로 상호작용의 존재·부호를 배제하지 않는다.

## 5. 검색과 provenance

SciSpace의 자연어 검색 1회에서 10개 논문이 반환되었다. Exa 검색 2회의 요청 후보 수는 총 10개이며, fetch 3회를 통해 5개 URL을 요청했다. HTML 주소의 catalog 수준 응답과 실제 PDF 본문 응답을 구분하여 PDF를 채택했다. RWTH PDF는 직접 HTTP에서 HTML challenge가 돌아왔고 Exa fetch는 CRAWL_EMPTY_CONTENT였으나, web 원문 읽기에서 8쪽 본문과 Thm 4.3을 확인했다. 이 접근 실패는 해당 논문의 과학적 상태와 구별한다.

SciSpace 자동 TLDR의 Cacuci 논문 요약에 원 abstract와 반대되는 문장이 나타났다. 자동 TLDR는 채택 근거에 사용하지 않았고 위 네 원문을 직접 읽었다. Interval reachability·parameter estimation·선형 전용 adjoint 후보는 현재 nonlinear endpoint mixed forcing의 직접 의존성에 추가하지 않았다.

전문·원 검색 응답은 별도 private source cache에 보존했다. 공개 묶음은 서지, 읽기 위치, 파일 identity, 본 연구의 자체 대응을 포함한다. 실제 새로운 수치 결과와 최종 채택 범위는 `review/INDEPENDENT_REVIEW.json` 및 root decision에 결박한다.
