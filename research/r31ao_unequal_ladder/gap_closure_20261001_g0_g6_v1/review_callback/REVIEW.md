# G4 callback/assembly 별도 artifact review

이 검토자는 G1의 analytic formula 설계에 참여했다. 따라서 **theory-design 독립성은 없다**. G4 담당자가 작성한 C++ artifact를 별도로 읽고 원본 source 및 pinned primary headers와 대조한 검토다. `independent_review_admitted=false`이며 프로젝트의 independent final scientific decision review를 대신하지 않는다.

Native compiler, FLINT binary, HH input, 실제 callback/integrand 또는 scientific array는 실행하지 않았다. 아래의 확인은 **static source comparison**이다. 최종 검토 대상 hashes와 수정 finding의 상태는 `REVIEW.json`이 authoritative하다.

## 대조한 authority

Source-functional map의 S01 `od_run.py`, S02 `h0_backend.py`, S03 `h0_fused.cpp`, S05 `exact_laplace_weights.py`를 source_snapshot에서 읽고 각각 map의 SHA256와 비교했다. 모두 일치했다. FLINT 3.4.0 C01 archive SHA256 `108ab51a4dd33918ff3308f0c63a63616ae30a2c174d50c9188676e85011346f`를 확인하고 local `acb.h`, `arb.h`, `acb_hypgeom.h`, `fmpq.h`, `fmpz.h`를 해당 archive members와 byte comparison했다. API name lookup 외에 radial special-function, exact-rational conversion, power, conjugation 및 integer setters의 signatures도 읽었다. Headers/API matching은 linked-binary identity나 compilation 성공을 뜻하지 않는다.

## 수학적·source 의미 대조

| 대상 | static 검토 결과 |
|---|---|
| Radial M_k, r=0,1,2 | shifted half-integer parameters와 Pochhammer prefactor가 G1 식과 일치; `regularized=0`; 정확히 0인 even-degree derivatives를 조기 반환 |
| σ와 s | σ=(1/A+1/B)/2; s=Σδ_j²로 bilinear; Hermitian norm·sqrt(s)·1/s 사용 없음 |
| Complex domain | t,u,A,B,σ 전체 ball의 real lower margin을 검사; midpoint positivity만으로 통과시키지 않음 |
| Primitive Gaussian | complete-square means/base와 fixed real q가 S03에 대응; right-half-plane principal powers의 domain proof가 유지됨 |
| O/G derivatives | s/px/pz의 E, derivative, G=-base(log′E+E′)가 S03 der[4]/der[5]와 일치; pz delta 항 포함 |
| Hermite U_i | signed finite Hermite coefficients, μ powers, t half-powers 및 exp(-μ²/(4t))/√π가 S05의 unweighted ideal density에 대응 |
| Polynomial contraction | direct stored C coefficient를 signed U_i U_j field에 한 번 적용; GL weights/Jacobian 없음; 1…107 term cap |
| Normalization | √2 pref (2a/π)^(3/4)(2b/π)^(3/4), p channel의 2√a가 S02에 대응; exact lifted parameters를 outward 평가 |
| Primitive array | [active,field,orbital,ia,ib]의 2×3×3×12×12=2592개, angular normalization 및 orbital contraction 전의 whole real-domain 적분으로 선언 |
| Registry/coefficient | ch0…23→center0 j0…23, ch24…46→center1 j1…23; left coefficient[ia,j%8]×ground[ib,0]; Fortran storage는 decoder가 semantic index로 해석해야 함 |
| Reflection | active XOR cusp; p cusp1 minus; 모든 G cusp1 추가 minus가 S01과 일치 |
| Phase | k_c=±v/2,c_z=±z/2, τ=z/v; phase=exp(i[2k_c c_z+(E_N−E_I)τ]); z=3/4 exact guard |
| D_col | k_c(G1+G2)+i[k_c(2k_c−k_a−k_b)−E_I]O, 47×2 row-major output |
| D_row | −k_a conjugate(G1)−k_b conjugate(G2)−iE_N conjugate(O), 2×47 indexing; conjugation은 post-integral, post-phase assembly에만 존재 |
| Input conversion | C++ source에 host double conversion 없이 fmpq→acb outward conversion 사용; rational denominator와 size guard는 수정 후 재검토 대상 |

Ideal source algebra를 bound하는 코드 구조다. S02의 과거 binary64 normalization 또는 S01의 과거 rounded τ와 새 exact-target 값을 bitwise 같다고 주장하지 않는다. 그 차이는 나중의 continuous-target enclosure 대 immutable raw comparison에 포함된다. Primitive-integral 구조체를 만들었다는 이유로 그 bytes가 실제 whole-domain enclosure가 되지는 않는다. G7 wrapper가 source/input/hash/entry ordering, endpoint와 interior의 한 번 합산, actual authority를 별도로 결박해야 한다.

## 발견 사항과 수정 확인 범위

초기 `INITIAL_FINDINGS.json`에 보존한 CB01은 unsupported order=n>1에서 out[0]만 indeterminate로 바꾸고 나머지 Taylor coefficient slots를 남기던 문제다. FLINT의 기본 integrate route는 order0/1만 쓰므로 그 route의 formula에는 영향이 없지만, higher-order fail-closed 계약에는 맞지 않았다.

CB02는 Rational text/bit length 및 hard precision ceiling이 없어 입력 규모에 의한 무제한 계산을 허용하던 resource contract 공백이다. CB03은 native synthetic test가 order2 호출에 단일 acb_t를 전달해, CB01을 올바르게 고치면 test가 잘못된 buffer 범위를 쓰게 되는 잠재 결함이다. 구현 담당자에게 이 세 건과 rational setter의 강한 exception-safety 권고를 전달했다. 최종 소스에서 실제 반영된 내용만 `REVIEW.json`의 resolved 항목으로 처리한다. Native negative fixtures를 수정했더라도 native 실행 전에는 runtime-verified라 하지 않는다.

## 남은 독립 gate

- Pinned backend/dependencies의 실제 source-to-binary provenance, compiler/ABI, linked libraries와 native synthetic execution.
- Scalar odd moments·complex input balls·derivative property 및 native complete assembly fixtures의 실제 실행 결과.
- Slice callback은 inner integrand adapter다. Outer whole parameter box에 uniform한 nested **integral** enclosure implementation을 대신하지 않는다.
- 고정 positive margin에 비해 σ가 작은 유효한 실제 domain은 안전하게 거절될 수 있다. Margin/precision/partition 선택의 실제 비용·폭은 미측정이다.
- Exact Frozen107 input binding, actual endpoint/interior/full-D balls, exact represented gap, epsilon 및 decision certificate.
- Project-admitted final decision review.

`certified_epsilon=null`, `certified_eta=null`, `rigorous=false`를 유지한다.
