# WU088_HH PHYS15 독립 이론 검토

## 판정

**PROMOTE_SCOPED.** 같은 COMMON과 같은 전역 \((\lambda,b)\)를 공유하는 PHYS14 geometric isotropic source-aligned 계열에서, Full과 실제 two-half의 상관된 잔차, 광자 chronology, source 시각 연결, 유한 endpoint 전달 정리를 채택한다. 근거 상태는 **derived + exact-arithmetic checked**다.

이 판정은 원 source·근·\(C^2\) 포함과 기존 Full의 고정 전처리 행렬·수축 상한을 상속한다. 새 이론은 그 자료를 이용해 \(r,d,\Delta T,\Delta e,\Delta w,\Delta Z\)를 구성하는 식과 포함 절차를 완결한다. 실제 PHYS15 endpoint 수치 구간의 평가는 `HH_CORRELATED_ENDPOINT_ENCLOSURE`의 입력·출력 계약에 연결한다.

## 검토 범위와 독립성

검토자는 `/root/hh_phys15_review`다. 후보 설계·작성·검증 설계에 참여하지 않았고 후보 파일을 수정하지 않았다. PHYS14의 원 Rust transport·reduced residual·FT03 source·HH source, PHYS11의 source-to-carry 대응, 원 captured source leaves 및 현재 세 원고를 직접 읽었다. 기존 PHYS14 과학 프로그램은 읽기만 했으며 import하거나 재실행하지 않았다.

현재 검토 대상은 다음과 같다.

- Root `theory/CORRELATED_ENDPOINT_THEORY_KO.md` 전체.
- 광자 분과 `PHOTON_DEFECT_THEOREM_KO.md` 전체.
- Source 분과 `ASSUMPTIONS_AND_BINDINGS_KO.md` 전체.
- `FIXED_PRECONDITIONER_BINDING.md/.json`과 원 Full `UNIFORM_ARITHMETIC.json`의 \(C,B,q,S\) 연결.

검토는 원 단계식에서의 별도 전개, 원 source graph의 반응별 인수 분해, 차원·부호·정의역 검토, 다른 구성의 소규모 exact Fraction 검산을 사용했다. 일반 정리의 판정은 아래 논증에 근거하며 소수의 대입 사례는 잘못된 항·순서·부호를 구별하는 보조 증거다.

## 1. 같은 COMMON과 잔차 부호

원 source의 순서는 기존 spectrum의 remap과 guard 이동, endpoint birth, 기체 implicit absorption이다. 양쪽 경로가 같은 \(g_0,Z_0,\lambda,b\)와 captured 계수 선택을 공유할 때

\[
g_2-g_0=h\mathcal B_1(g_1)+h\mathcal B_2(g_2)+V(P_1+P_2)
\]

를 직접 얻는다. Full 잔차

\[
\mathcal H_F(g)=g-g_0-2h\mathcal B_2(g)-VL_F(g)Q_F
\]

에 \(g_2\)를 대입하면 root 식 (3.1)의 \(r=h[\mathcal B_1(g_1)-\mathcal B_2(g_2)]+Vp\)가 나온다. 여기서 \(p=P_1+P_2-L_F(g_2)Q_F\)의 기준은 실제 two-half gas endpoint다.

따라서 \(d=g_2-g_F\)에 대해 \(\overline{\mathcal A}d=r\)의 부호는 양수다. \(\mathcal H_F(g_2)-\mathcal H_F(g_F)\)를 직접 전개한 결과이며, source 미분으로 옮길 때도 같은 부호가 유지된다. \(\mathcal B_1(g_1)-\mathcal B_2(g_2)\)를 source 시각 차이와 \(g_1\to g_2\)의 동일 함수 변화로 나눈 (3.2)–(3.3)도 정확하다.

## 2. Outgoing 6항과 absorption 7항

\(A_1=A+\Delta A_1\), \(Q_1=RZ_0+bJ\)를 실제 단계식에 먼저 대입한 뒤 \(RA=AR+[R,A]\)를 사용해 두 분해를 독립적으로 전개했다. 대각 항등식

\[
A^2-A_F=-C_2,\qquad A^2+A-2A_F=C_1
\]

은 \(A=(1+\tau)^{-1}\), \(A_F=(1+2\tau)^{-1}\)의 공통 분모에서 성립한다. 이를 적용하면 광자 식 (13) 및 root 식 (9.1)의 6항, 광자 식 (14) 및 root 식 (4.2)의 7항이 각각 나온다.

Integrated absorption에는 \(L(I-R)RZ_0\)가 필요하다. 첫 흡수는 실제 첫 node에서 계수 \(\epsilon_j\)로 기체에 전달되므로, 첫 흡수 뒤에 다시 redshift를 적용한 outgoing 계산과 absorption의 합은 서로 다른 배치를 갖는다. 검토자의 작은 비가환 remap 사례에서 이 항을 제거하면 등식이 깨졌고, active-active commutator를 제거해도 별도의 불일치가 발생했다.

Opacity secant

\[
\Delta A_{1,j}=h(\kappa_{2,j}-\kappa_{1,j})A_{1,j}A_j
\]

와 \(\kappa_2-\kappa_1=c\sigma_j(n_2-n_1)(1-x_2)+a_{1,j}(x_1-x_2)\)의 부호·밀도 대응도 확인했다.

## 3. Sector 부호의 적용 범위

원 captured HI cross section은 active node 16–32에서 엄격하게 감소하고 inactive node에서는 0이다. 따라서 active output으로 내려가는 edge의 \([R,A]_{j-1,j}\)는 비음수다. Threshold 아래 output은 \(L_i=0\)이므로 \(L[R,A]Q_1\ge0\)가 전체 physical \(Q_1\ge0\), \(0\le x_2\le1\)에서 성립한다. 직접 photo forcing의 \(x,w\) 성분도 비음수다.

Birth-redshift sector에서는 \(\beta_j=\eta\sigma_j/(1+\eta\sigma_j)^2\)의 차이를 직접 공통 분모로 전개했다. 원 leaves는 \((hcn_2)^2\sigma_{23}\sigma_{24}<1\), \(\epsilon_{23}\sigma_{23}<\epsilon_{24}\sigma_{24}\), \(\sigma_{23}>\sigma_{24}\)를 만족한다. 이에 따라 \(b>0,x_2<1,\alpha_{24}>0\)이면 integrated ionization sector는 양수, thermal-deposition sector는 음수다. 양의 \(w,\Pi\)에서 직접 온도 covector로의 사영도 음수다. Endpoint 기여는 원고에 정의한 같은 평균 inverse와 같은 유한 온도 covector로 계산한다.

## 4. Source 시각과 온도 정렬

원 `ft03_interval_rhs`에서 \(n_H\), stored \(n_{\rm He}\), \(n_e\), lower/upper population, H당 rate와 He 분율 rate의 나눗셈을 직접 추적했다. CI·RR·DR의 분율 source는 모두 \(n e\,k_{\rm frac}(T)\)로 인수 분해된다. Thermal source는 \(n e[k_{wH}+\widehat f k_{wHe}]\)다. 원 RR kinetic coefficient와 두 DR exponential의 열 가중치도 원고의 정의와 일치한다.

\(\Psi g=(x,y_1,y_2,w\Pi_2/\Pi_1)\)는 정확히 \(T_2(\Psi g)=T_1(g)\)를 준다. 따라서 root 식 (5.3)의 density/electron scaling과 He thermal correction, HH의 \(q_1=(n_1/n_2)q_2(\Psi g)\)가 성립한다. \(r_e-1\)과 \(\Psi_w-w\)의 작은 차이를 먼저 만든 (5.4), w 선분 평균 도함수를 적용한 (5.5)도 정확하다.

첫 source와 끝 source의 stored density ratio는 구별되어 있고, pullback은 원고가 특정한 내부 root hull과 그 연결 선분에서 사용된다. 이 범위는 원 whole-X source 도함수 포함의 적용 영역에 들어간다. Source의 \(-2Hw\) 항은 FT03 nonphoto export 밖에서 더해지며, 동일 \(H\)의 같은 g 비교에서는 소거된다.

## 5. 기존 Full 전처리 검증의 평균 Jacobian 전달

Root (6.2)의 photo 항은 잔차 \(-VL_FQ_F\)를 미분하면 얻어진다. \(dL_F/dx=-2ha/D_F^2\)이므로 잔차 Jacobian에는 \(+2h v_F e_x^T\)가 들어간다.

원 고정 \(C\)와 같은 파일의 \(B,q,S\)에서 \(|I-CD\mathcal H_F|\le B\)를 사용한다. Convex X 안의 endpoint 선분 전체를 적분하면 \(|I-C\overline{\mathcal A}|\le B\)다. \(\|S^{-1}BS\|_\infty\le q<1\)이므로 \(C\overline{\mathcal A}\)는 가역이고, 유한 정사각 행렬 \(C\)와 \(\overline{\mathcal A}\)도 각각 가역이다. Neumann 급수를 성분별 비음수 행렬 \(\widetilde B\)로 지배하면 (6.4)의 성분별 및 scalar 상계가 나온다.

검토자는 stored dyadic C와 원 `SOURCE_BOX.json::A_Gg` 끝점으로 16개 행렬 성분을 exact Fraction으로 재구성했다. 모두 같은 `UNIFORM_ARITHMETIC.json::B`에 포함됐고, 저장 radius의 weighted row sum이 같은 파일의 q 이하임을 확인했다. \(1/(1-q)<1.000118\)은 전처리 잔차 \(Cr\)의 S-scaled 노름에 대한 정확한 귀결이다.

초기 \([d]\)의 상계, \([d]\cap(C[r]+[E][d])\) 교차, 기존 root cap과의 교차는 모두 실제 해를 유지한다. 원 source/근 근거를 재사용해 새 결함을 평가하는 절차로서 닫혀 있다.

## 6. 유한 관측량, ledger 및 실제 photon endpoint

공통 endpoint normalization에서 \(\Delta e=\ell_e d\), \(\Delta n_e=n_2\ell_e d\)다. \(T_F=C_T(w_2-d_w)/(\Pi_2-d_e)\)를 직접 대입해

\[
\Delta T=(C_Td_w-T_2d_e)/(\Pi_2-d_e)
\]

를 얻었다. 이는 양의 실제 \(\Pi_F\)를 분모로 쓰는 유한 차이 식이다. 해당 endpoint covector와 \(\overline{\mathcal A}^{-T}\)를 함께 쓰면 하나의 \(\Delta T\)를 같은 inverse의 sector 기여로 정확하게 나눌 수 있다.

Guard 포함 \(\mathfrak nR=\mathfrak n\), \(\mathfrak uR=\rho\mathfrak u\)에서 number ledger를 다시 전개했다. Energy ledger에서는 첫 흡수가 둘째 redshift에 앞서므로

\[
E\cdot p=(1-\rho)(E\cdot P_1-bME_{24})-\Delta U
\]

를 얻었다. 기존 guard energy의 추가 redshift도 이 row identity에 포함된다. 원 active 17개 node 모두의 captured heat가 \(\operatorname{exact}(E_j)-\operatorname{exact}(\chi_H)\)와 같은 것을 독립 exact 비교로 확인했다. 따라서 \(\ell_H=(\chi_H,0,0,1)\) 사영과 HH 직접 source 소거가 정확하다. 이 사영의 관측량은 원고에 적힌 \(\chi_Hx+w\)다.

실제 Full photon으로 옮기는 식은 componentwise

\[
\Delta Z_j=\Delta\widehat Z_j+
\frac{2h a_{2,j}Q_{F,j}}{D_{F,j}(g_2)D_{F,j}(g_F)}d_x
\]

이며 guard의 추가항은 0이다. \(A_F(g_2)-A_F(g_F)\)의 공통 분모에서 계수와 양의 부호를 확인했다. 광자 분과의 임의 기준점 식은 대신 second-half denominator와 Q2를 사용하는 동등한 별도 배치다.

## 7. 판별 검산과 해결한 지적

`independent_theory_checks.py`는 후보 모듈을 import하지 않고 세 개의 작은 manufactured 대수계열과 원 leaf·preconditioner 대응을 계산했다. **26개 검토 항목을 모두 통과**했다. 일반 증명의 논증 검토와 함께 해석하며, 검토 항목 수를 physical case 수로 사용하지 않는다.

- 비가환 선형 remap·guard와 두 absorption 단계의 직접 계산, 여섯/일곱 sector의 별도 합, chronology 항 누락 판별.
- 원 captured source 계수의 birth·heat·cross-section 부호 및 arbitrary rational rate에 대한 density/temperature bridge.
- 닫힌 nonlinear source의 평균 Jacobian, 잔차 부호, 유한 온도·공통 adjoint·Neumann 성분별 지배.
- 실제 stored C·B·q·radius와 원 source Jacobian 포함의 연결.

Bounded wrapper의 wall time은 약 0.0511초, user CPU는 약 0.0412초, peak RSS는 12,780 KiB였다. 과학 history·source·root 실행은 0회다. 실행 전 identity와 예산은 `PRE_RUN.json`, 결과는 `INDEPENDENT_THEORY_CHECKS.json` 및 `RUN_RECORD.json`에 있다.

한 가지 수학 표기를 교정했다. Root (9.2)와 광자 (50)의 `diag[coefficient] × scalar`는 좌변 vector와 타입이 맞지 않았다. 각각 retained node의 성분식으로 바꾸고 guard를 별도로 적었다. 두 식의 계수·부호·진리조건은 유지됐다. 교정된 두 파일을 다시 읽어 이 지적을 닫았다.

**현재 이론 판정의 blocking finding은 없다.** 다음 실제 연구 단위는 이 식에 기존 joint 입력과 도함수 포함을 넣어 상관된 endpoint 결함의 수치 구간을 얻는 것이다.
