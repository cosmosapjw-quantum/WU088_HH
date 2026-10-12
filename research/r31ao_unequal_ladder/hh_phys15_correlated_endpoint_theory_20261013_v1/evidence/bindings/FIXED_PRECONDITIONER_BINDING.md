# PHYS15 — 기존 Full preconditioner와 수축 상한의 결박

## 재사용할 원본

기존 고정 \(C\)는 원 NCP07 `results/full/UNIFORM_ARITHMETIC.json::fixed_C`에 저장되어 있다. 원 ZIP의 해당 member, 원 MANIFEST, 실제 회수본의 동일성을 확인한 뒤 다음 경로에 create-only로 복사했다.

`extra_inputs/results/full/UNIFORM_ARITHMETIC.json`

- 크기: 3,918 bytes
- SHA256: `3cf8c86b445ba2be2889e5effbdaacbcf84d0dcedbabd60763124141dfbc09af`
- 원 판정: `CONDITIONAL_ROOT_ARITHMETIC_PASS`
- 같은 파일의 기본 수축 상한: \(q=0.00011736830563768177\), bits `3f1ec474231fbe16`
- 같은 파일의 radius scale: binary64 \((0.015,0.01,0.01,0.5)\)

`FIXED_PRECONDITIONER_BINDING.json`은 \(C\)의 16개 값과 scale을 original binary64 bits 및 exact dyadic rational로 모두 기록한다. JSON의 `fixed_C`는 Rust의 shortest-roundtrip decimal export이며 원 binary64로 읽은 뒤 그 dyadic 수를 정확한 고정 행렬로 사용한다.

\[
C\simeq
\begin{pmatrix}
0.9990246916891717&-4.153280360807079\!\times\!10^{-7}&-8.306644538258012\!\times\!10^{-7}&1.7565929914092142\!\times\!10^{-6}\\
-3.6618196705249815\!\times\!10^{-7}&0.9999978466324293&-2.0665827776493324\!\times\!10^{-6}&9.7142986908604\!\times\!10^{-8}\\
-7.556020843399845\!\times\!10^{-8}&-5.808928483398726\!\times\!10^{-9}&0.9999998916612085&3.2206459941029827\!\times\!10^{-9}\\
0.0010255917264521313&9.974650691027598\!\times\!10^{-6}&1.5661910694781645\!\times\!10^{-5}&0.9999508981197063
\end{pmatrix}.
\]

표시용 소수 대신 동반 JSON의 bits/exact를 계산 입력으로 재사용할 수 있다.

## 정확한 정의와 적용 범위

Full residual을
\[
H_F(g;\alpha,\lambda,b)=g-g_0-2hF_F(g;\alpha,\lambda,b)
\]
라 하고 \(S=\operatorname{diag}(r_1,r_2,r_3,r_4)\)에 원 radius의 exact binary64 값을 넣는다. 같은 원본의 `B`는
\[
|(I-C D_gH_F)_{ij}|\le B_{ij},\qquad
\max_i\sum_j B_{ij}\frac{r_j}{r_i}\le q<1
\]
을 주는 outward magnitude bound다. 따라서
\[
\boxed{\sup_{g\in X,\,(\lambda,b)\in[0,1]^2}
\|S^{-1}(I-CD_gH_F)S\|_\infty\le q.}
\]

이 상한은 기존 whole-\(X\) source inclusion과 고정 계수 \(\alpha\)의 \(C^2\) 근 계열 전제를 상속한다. PHYS14의 linked geometric isotropic 선택으로 제한할 때 \(C\), \(S\), \(q\)를 바꾸지 않는다. 원 convex \(X\) 안의 gas segment에 대한 평균 Jacobian에도 같은 상한을 적용할 수 있다.

## 원 생성 graph

1. `src/sourcebox.rs::uniform`은 고정 gas centre \(c=(0.915,0.3,0.6,13.5)\)에서 저장된 `SOURCE_CENTRE.json::A_Gg`를 읽는 원 export 경로를 사용한다. 이 centre source의 parameter 영역은 전체 \(\Theta=[0,1]^2\)다.
2. 각 Jacobian interval \([l_{ij},u_{ij}]\)에서 scalar binary64 연산 `l + (u-l)/2`로 대표 행렬 \(J_c\)를 만든다.
3. `src/uniform.rs::FixedC::from_center`는 \([J_c\mid I]\)를 만들고 partial-pivot Gauss–Jordan을 한 번 수행한다. Pivot은 최대 절댓값을 쓰고 동률에서는 먼저 선택된 행을 유지한다. Pivot row 정상화와 각 elimination의 열 순서는 0부터 7까지다.
4. 오른쪽 4×4 binary64 행렬을 `fixed_C`로 저장한다. 그 뒤 \(C\)는 \(g,\lambda,b\)에 대해 고정된다.

따라서 저장된 \(C\)를 원 \(J_c\)의 **정확한 유리수 inverse**로 바꾸는 재구성은 필요하지 않다. 저장된 approximate inverse 자체가 수축 상한의 입력이다. 생성 코드와 centre·whole-box 데이터의 실제 SHA256는 동반 binding JSON에 있다.

## 두 q export의 구분

| export | q upper | 원 누적 순서 |
|---|---:|---|
| **`UNIFORM_ARITHMETIC.json`** | **0.00011736830563768177** | `uniform.rs`에서 outward \(CA\) matrix product 후 \(I-CA\) |
| `UNIFORM_DIAGNOSTICS.json` | 0.00011736830563698944 | `sourcebox.rs`에서 \(I\)부터 각 \(CA\) 항을 차례로 subtraction |

두 export는 같은 \(C\), source Jacobian과 scale을 사용한다. Interval 연산 graph의 차이가 작은 폭 차이를 만든다. PHYS15의 기본 결박은 **ARITHMETIC 한 파일의 \(C,B,q,r\)**로 통일한다.

## 표적 검산과 실행 상태

저장된 \(C\)의 exact dyadic 값과 `SOURCE_BOX.json::A_Gg`의 exact interval endpoints로 16개 matrix entry를 Fraction 산술로 다시 구성했다. 각각 ARITHMETIC의 \(B\)가 포함하며, exact weighted row sums와 저장 \(B\)의 weighted row sums가 모두 기본 \(q\) 이하임을 확인했다.

이는 저장 preconditioner의 원 입력 대응을 확인하는 작은 대수 검산이다. 새 source, root, history, PHYS15 numerical defect 실행과 cloud write는 모두 0회다. 첫 receipt 조립에서 발생한 변수명 충돌은 최소 교정했으며, 원 script와 사건 기록은 `pinning_evidence/`에 보존되어 있다.
