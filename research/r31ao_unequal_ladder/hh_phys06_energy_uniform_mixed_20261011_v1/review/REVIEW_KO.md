# PHYS06 독립 판정

**판정: P06-C01–C07은 명시된 연구·수학·reference 범위에서 PROMOTE, P06-C08과 실제 물리/production은 HOLD다.** 고정 후보의 과학적 주장과 전달 계약에서 남은 blocking finding은 없다. 이 판정은 실제 HH endpoint, uniform tube 또는 finite interaction 수치를 승인한 것이 아니다.

## 1. 독립성과 고정 후보

Reviewer는 `/root/phys06_decision`이다. 후보 이론·코드·시험의 작성 또는 설계를 하지 않았으며, 원본 후보를 수정하지 않았다. 원본 코드와 증거를 읽고 수학적 전제를 독립적으로 검토했다. 검토 중 발견한 잘못된 evidence 경로와 rank 표현은 owner가 freeze 전에 고쳤다. 밀도 및 heat leaf 정정은 creator/source 담당이 발견한 수정이며 이 reviewer의 새 발견으로 표시하지 않는다.

고정 후보는 `CANDIDATE_SHA256.json`, SHA256
`14d1ed9720cca377587e0083fa0327d2e60099b967b9c09a3e305b26b133b771`에 바인딩했다.
**100개 frozen file 모두 실제 bytes와 SHA256이 일치했고 mismatch는 0개였다.**
Hash 확인과 내용 정독 범위는 구분한다. 실제 읽은 파일/부분은
`review/SOURCE_HASHES.json`에 기록했다. 상세 기계 판정은 `review/DECISION.json`에 있다.

Astra v4의 phase08 independent decision gate를 읽고 적용했다. 이 리뷰는 실제 분리된 reviewer의 판정이며 owner의 역할 전환이 아니다. 별도 model/runtime attestation은 주장하지 않는다.

## 2. Claim별 판정

| Claim | 판정 범위 | 근거와 한계 |
|---|---|---|
| P06-C01 | PROMOTE — exact-real 에너지 항등식 | 상수 energy row의 HH 소거와 source residual의 직접 선형변환은 성립한다. Photo `Eκ` 항등식은 exact excess-energy 차 또는 해당 defect가 소거된 branch에 한정하며 일반 leaf에는 δ/Ψ를 남긴다. |
| P06-C02 | PROMOTE — 조건부 fixed-N photo 곡률 | `−2d Σ EN ααᵀ/D³`는 음의 준정부호다. N 또는 α가 0인 항은 rank0일 수 있고 다른 두 방향의 contraction은 양·음 모두 가능하다. Rounded heat graph 전체의 부호 정리는 아니다. |
| P06-C03 | PROMOTE — archived point scalar 진단 | 33-node 입력에서 17개 HI-positive σ, 그중 9개 positive-stock contributor와 두 duration의 rank1/음수 xx 성분이 기록된 검산에 연결된다. Stored stock 및 Python provider 전사본이라는 한계를 유지한다. |
| P06-C04 | PROMOTE — source normalization 정정 | `ell_f−ell_fhat`가 주는 Jnorm의 부호·형태가 실제 밀도 construction과 일치한다. 세 비영 rational 차이를 보존했지만 Jnorm의 실제 rate/미분/tube bound는 계산되지 않았다. |
| P06-C05 | PROMOTE — uniform family 충분조건 | 실제 whole-domain enclosure와 C²/admissibility를 가정하면 strict invariance·수축·A의 가역성·X 안의 유일한 family가 따른다. 비교행렬의 exact solve도 유효하다. JSON/domain flag는 전제의 증명이 아니다. |
| P06-C06 | PROMOTE — finite rectangle 및 paired identity | 정확한 discrete C² family의 W를 적분하면 네 모서리 차이가 된다. Paired 차분 선형식은 정확하다. Whole-rectangle coverage, nonlinear observable Hessian 및 half1 carry를 유지해야 한다. |
| P06-C07 | PROMOTE — reference 검증 범위 | 전체 Python source/tests를 읽고 최초 275 assertions·17 expected rejection 및 독립 oracle 결과를 대조했다. 이 reviewer가 새로 275개를 실행한 것은 아니며 Rust build도 하지 않았다. |
| P06-C08 | HOLD — 실제 물리 값 | Trusted source producer, uniform root/tube, actual W/I_h/paired defect, continuous source-law 및 시간 나머지의 증거가 없다. 해당 값은 null이다. |

## 3. 핵심 수학 검토

`β+Br<r`에서 `B≥0`, `r>0`이므로 `q=max_i(Br)_i/r_i<1`이다. 고정 θ에 대한 `Tθ(y)=y−CG(y,θ)`는 convex box를 그 내부로 보내고 weighted maximum norm에서 수축한다. 실제 `CA`는 Neumann 논증으로 가역이고 C와 A도 가역이므로 fixed point가 실제 `G=0`이다. C² domain과 내부 root를 사용한 implicit function theorem의 국소 family는 X 안의 유일성으로 서로 이어진다. 이 논증이 X 밖의 전역 유일성이나 실제 source enclosure의 존재를 증명하지 않는다는 제한이 문서와 코드에 있다.

선형 포함에서는 실제 오차 `e=z−zc`가 `|e|≤B|e|+η`를 만족하므로
`ρ=(I−B)⁻¹η`가 유효한 성분별 상계다. 코드가 exact rational Gaussian solve를 수행하는 대상은 이 작은 비교행렬이며 실제 nonlinear root가 아니다. 고정 C, interval products, signed center, 비음수 inverse 및 dimension 검사를 읽었고 이 범위의 결함을 찾지 못했다.

Mixed forcing에는 `G_λb`, `G_yλ V`, `G_yb U`, `G_yy[U,V]`가 모두 있다. Polynomial witness는 이 중 chain 항 세 종류를 비영으로 사용하며, radical implicit family는 root/U/V/W와 finite corner를 별도 식으로 검산한다. Finite integration은 정확한 discrete W 전체를 포함할 때만 parameter Taylor remainder 없이 성립한다. 점의 W나 formal h²/h⁴ 계수는 이 전제를 대신하지 못한다.

Paired 식 `A_T ΔW=Δf−ΔA W_F`의 부호는 맞다. 다만 ΔA/Δf의 작은 폭은 같은 parameter/source 계산에서 얻어야 한다. 이를 개별 box의 독립 subtraction보다 항상 좋다고 보장하지 않으며, 이론과 handoff는 그런 보장을 하지 않는다.

## 4. 에너지 source 및 수정 이력

기체 분율의 H/He normalization, χ의 누적 helium binding, eV/H 단위와 온도 복원이 서로 일치한다. HH 직접 energy row가 0이어도 total implicit mixed energy가 0일 필요는 없다. Photo 곡률은 fixed N 성분의 구조이며 incoming N derivatives, nonphoto Hessian, inverse Jacobian 및 다른 source를 소거하지 않는다.

실제 `model(stage)`는 `nHe=fl(nH*fHe)`를 저장하고 FT03 interval source는 저장된 density의 비를 사용한다. 따라서 Jnorm을 남기는 수정은 필요하다. 보존된 inline density 실행 기록은 독립 UTC/stderr capture가 없음을 명시하고 있으며, saved script를 다시 실행한 것처럼 꾸미지 않았다.

`phys04_mixed.rs`의 `ic(E−CHI)`는 뺄셈 후의 binary64 leaf다. 최종 이론의 `Ψ=ΣNδ/D` 및 affine quotient Hessian 보정의 부호·형태를 확인했다. 100 eV의 HI에 ε=−2⁻⁴⁸ eV라는 반례가 있어 일반 spectrum에 이상적 `Eκ` 항등식을 적용하는 확대를 막는다. 현재 33-node에는 σ·ε가 모두 0이라는 별도 기록이 있으므로 기존 frozen-stock 곡률 진단을 수정해 다시 돌릴 필요는 없다. 19개 비영 ε는 inactive helium 항이다.

S는 명시적으로 정의한 exact-real 좌표다. Native `energy()`의 미리 반올림한 합·곱과 bitwise 동일하다고 주장하지 않으며, outward coefficient construction과 original event evaluation rounding은 실제 NCP exporter의 책임으로 남긴다. 이 두 source 정정 때문에 원래 kernel이나 normalization을 조용히 바꾸지 않았다.

## 5. 검산·실행 기록의 대조

| 기록 | 대조한 실제 범위 |
|---|---|
| `reference_first` | 최초 exit0, 약0.1158s, 275 assertions, 17 deliberate invalid-input rejections, 7 case groups |
| `archived_energy_run01` | 최초 exit0, 약0.1152s, 198 group equalities와 6 aggregate equalities, 2 energy balance 및 2 rank factorization cases |
| Heat-leaf 원본·addendum | 99 subtraction 비교를 보존·재사용하고, 99 weighted checks와 3개의 generic100eV leaf 비교를 분리 |
| Density source 및 theory 확인 | 각각3개 scalar case, inline provenance의 제한과 최초 수정 기록을 보존 |
| 이 reviewer의 과학 재실행 | 0 — 문서·source·로그·hash 검토만 수행 |
| Actual native endpoint/point/root/IVP 및 과거 suite 재실행 | 모두0으로 유지 |

Reviewer는 최초 과학 실행을 직접 새로 관측한 실행자가 아니다. 보존된 실행·결과 파일, 일치하는 script/input hashes 및 코드 정독으로 판단했다. 과거 PHYS05 18,817 검사, NCP189-slot oracle 또는 PHYS04 suite를 반복해서 얻은 판단이라고 표시하지 않는다. 단위·수학 항등식의 independent review와 새 native physics evidence는 서로 다른 상태다.

## 6. NCP handoff 및 남은 완료 작업

최종 prompt, task JSON, return template 전체를 읽었다. T01–T07의 순서와 완료기준, 새로 만들 6개 nonnative target, resource ceilings, 과거 완료 항목 재사용 및 private permit 우회 금지가 서로 일치한다. Source/ABI/binary hash는 이전 NCP build에 바인딩된 값이며 미래 worker attestation이 아니다. Current native ceiling은0이고, return template의 실제 측정값은 null로 시작해 ceiling과 measurement를 혼동하지 않는다.

Inherited future proposal의 endpoint12, conservative point12, certificate-internal point12, root12는 별도 최대치이며 실행 승인이 아니다. 네 모서리 실행 자체도 uniform family의 증거가 되지 않는다. 실제 source-bound enclosures, typed producer/permit 및 필요한 live binding은 여전히 OPEN이다.

복구 계약은 Git과 두 backup 위치의 detached receipt를 읽고 실제 commit/tree/ZIP/manifest/object identity를 사용하도록 되어 있다. Field 이름을 실제 hash로 오해하지 않으며 새 사용자 첨부파일을 요구하지 않는다. **이 독립 과학 리뷰는 이후의 publication 및 backup ACK 완료를 관측한 기록이 아니다.** Owner는 additive publication과 두 backup 전달을 실제로 마치고 concrete receipt를 남겨야 한다. 그 운영 결과를 증거 없이 현재 완료했다고 표시해서는 안 된다.

이 결과는 기존 물리 ledger를 새 closure로 바꾼 성과가 아니라, source의 정확한 에너지 구조·미세한 coefficient 불일치와 유한 혼합 차이로 가는 조건부 경로를 명료하게 한 성과다. Actual HH interaction이나 연속시간 정확성은 별도 증거가 생길 때까지 HOLD다.
