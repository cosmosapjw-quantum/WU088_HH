# PHYS88 독립 R6 이론·계약 검토

## 판정

**PASS_SCOPED_PREIMPLEMENTATION. 열린 material finding은 0개다.** 두 실제 finding을 구현·과학 실행 전에 수정했다. 최초부터 모든 항목이 PASS였다고 기록하지 않는다. 이번 검토는 source·유도·계약·판별 기준에 대한 독립 검토이며 새 수치 결과나 production admission을 발급하지 않는다.

최신 실제 local HEAD는 `496670cf39b3c2b5ff5e208c01bb135fe96b3780`다. 검토한 계약은 revision2, SHA256 `76d1791ee6ab7ba7c86f11e04ad96bd477cfc8602cf295225b0f8826ad132b64`이고 root 유도 문서 SHA256은 `3d7e5aaf8e29d4755e52d7e33dd6d14ef56579cb2d33252362567368091c739e`다. 개별 입력·계획·symbolic script·이전 원고의 실제 bytes/SHA는 동반 JSON에 결속했다.

## 실제 finding과 최소 수정

| Finding | 대상·영향 | 수정·상태 |
|---|---|---|
| P88-R6-01, root 발견 | 독립 원전 노트 revision0가 (+---)를 써 governing metric (−+++)와 불일치했다. 그대로 채택하면 invariant 부호가 뒤섞인다. | 원문 bytes를 REVISION0로 보존하고 metric, U², W, Eb의 네 표현만 수정했다. U²=−1, W=√(−P²), Eb=−qn·qp/b−a다. Carrier의 가감식은 유지했다. CLOSED. |
| P88-R6-02, 독립 검토자 발견 | 계약 revision1의 scaled conservation/shell tolerance에 분모·노름 정의가 빠져 있었다. 결과를 본 뒤 다른 기준을 고를 여지가 있었다. | Root revision2에 normal-frame 성분 최대 잔차/전체 입출력 절댓값 에너지 합, 양의 quadratic shell scale 및 나머지 absolute/relative 정의를 고정했다. 허용오차·예산은 바꾸지 않았다. CLOSED. |

원 독립 노트 SHA `b22880ef1bed6943130c9a1fb5c6bcf19b5dbbd7fc53cf4aa534fd81afafcb67`는 보존되며, 수정본 SHA는 `a12eba0a0b2908a3420c96c6428d4ff3e2c549cb32baa544d6f33ede5b28f335`다. 과거 SOURCE_THEORY_RECEIPT는 역사적 영수증으로 그대로 유지했다. Root의 acceptance repair 기록 역시 실제로 읽었다.

## 물리 유도 검토

질량 정의 h=AWR·a, D=a+h−QS와 Qb=a+b−d에서 **QS−Qb=ΔH−ΔD=BD−BH+ρH−ρD**가 성립한다. 표시된 81.63eV는 전체 Q 차이다. 작은 isotope binding 항 BD−BH와 규약 잔차 차이를 모두 포함하므로 81.63eV 전체를 ρH−ρD, 전자 하나의 ionization energy, 실제 오차 또는 열로 부르지 않는다. NIST ASD 입력은 실제 받은 rendered H/D 원전 행이며 original HTTP bytes·전체 표 검증이 아니다. 표시 decimal의 exact algebra와 실제 질량의 정확도·상관관계는 구별한다. [S1–S3]

같은 source 사건의 H/D 속도를 유지한 bare 재표기에서 outgoing−incoming 잔차는 **C=ΔH UH−ΔD UD**다. Signed internal/convention reservoir에 −C를 두면 같은 normal frame에서 네 성분이 닫힌다. C의 시간 성분은 일반적으로 QS−Qb와 다르고 공간 성분도 남는다. 이를 on-shell electron, positive heat bath, stopping 또는 독립 응력 텐서로 채택하지 않는다.

별도로 bare incoming에서 Wb와 COM photon/daughter를 생성하는 식은 bare shell과 4-momentum을 만족한다. 이 새 닫힌 사건에 재표기 carrier를 다시 더하지 않는다. 안정화한 K 식은 가까운 큰 rest-energy의 차를 직접 빼는 문제를 피한다.

LAB_ANCHORED는 Es=Eb, FIXED_COM_K는 Kb(Eb)=Ks(Es)라는 명시적 kernel-transfer 가정이다. 후자의 dEs/dEb=bWs/(hWb)는 양수다. Source 함숫값은 항상 원 Es에서 기존 interpolation으로 평가한다. 단면적은 에너지 확률밀도가 아니므로 σ에 추가 coordinate Jacobian을 곱하지 않는다. 두 사상의 bare support를 별도로 기록하고 차이를 CI로 해석하지 않는다. Nuclear R-matrix provenance는 이 모형 선택의 근거지만 실제 charge-state 동등성의 증명은 아니다. [S1,S2]

Bare Jüttner reduction은 새 bare masses·flux·normalization과 native logEs 적분을 사용한다. 두 적분 Jacobian은 bEs/Wb와 hEs/Ws다. Invariant ds 적분의 ds=2W dW가 rate prefactor 1/4를 준다. Normalized angular law의 회전 평균이 scalar moments에서 소거되는 것은 공통 T·drift0·등방 ensemble의 범위다. Directed conditional source의 방향 정보를 없앤다는 뜻이 아니다.

G=K2/K1, G2=1+3G/z와 세 에너지 평균은 ⟨Kin⟩+Qb=⟨Kd⟩+⟨Eγ⟩를 보존한다. T와 무관한 사상·support이므로 θ dlogκ/dlogT=⟨Kin⟩−un−up에 moving-boundary 항이 없다. Centered variance/covariance와 stable six-term Bessel utility를 재사용하며 과거 integrator는 호출하지 않는다. 열/fast 수 변화, 전자 incidence0, 여섯 disjoint energy 열과 caloric 식은 서로 맞는다. Instant thermal birth 선택은 실제 fast stopping의 근거가 아니다.

## 새 판별 계획과 실행 경계

동결 계획은 **16 full+4 FD scalar 적분**, source relabel18·bare event36·owner32행이다. 별도 원문 parser와 SciPy kve/adaptive quadrature를 사용하는 reference는 최고 T에서 두 사상의 rate·세 평균, 총8개 필드를 비교한다. 이 비교는 낮은 T variance의 독립 oracle, continuum certificate 또는 물리 uncertainty 인증이 아니다. 기존 PHYS87 source153knots/152cells 양성성 witness와 저장 baseline을 identity로 재사용한다.

실제 WOLFRAM_REFERENCE.wl의 rational mass/binding tokens, (−+++) norm, carrier component, 두 Jacobian/inverse map, COM/boost shell·closure 식은 정적 검토에서 일치했다. **이 독립 검토에서는 evaluator를 호출하지 않았으며 residual0 결과를 주장하지 않는다.** Root의 별도 단 한 번 symbolic call 한도를 유지한다.

기존 evaluator4+1과 PHYS87 실제 local cost를 유지하고 old additional allowance는0이다. 새 prospective cap은 primary24CPU/60wall, reference30/60, saved figure8/30이며 각각 child1·worker1·thread1이다. 매 child의 실제 shared lease·fresh memory gate, reserve1.5GiB+job0.5GiB, auto-retry0, 타 process 종료 금지를 유지한다. 미상 금전 예산은 미상으로 남긴다.

Root는 이 R6를 근거로 theory revision2를 동결하고 구현 및 별도 symbolic dispatch를 진행할 수 있다. 현재 구현 계획은 명시적 pre-freeze 문서라 revision1을 가리키며, 실제 frozen manifest·identity·commands는 **revision2에 결속**해야 한다. 이후 C9에서 실제 코드와 저장 raw 결과를 검토해야 한다.

## Claim gate

완료 가능한 child는 질량·규약 회계, covariant relabel ledger, 조건부 bare constructor와 finite-window supplier다. 원 atomic-to-bare node 및 physical supplier 부모는 PARTIAL이다. 다음은 **NUCLEAR_BARE_KERNEL_SOURCE_AND_CONSUMER_CONTRACT**이며 실제 kernel/electron branch 적합성, covariance·tails·consumer·stopping은 OPEN이다. HH_R10=OFF, production admission NOT_ISSUED를 유지한다.

이번 검토자의 scientific/evaluator/integration/completed-identity replay는 모두0이다. Git/provider mutation도0이며 파일 읽기·metadata hash와 허용된 독립 intake 문서 작성만 수행했다. 단순 rg 검색식 오류는 literal 검색으로 고쳤으며 과학 실행과 관계없다.

## 원전 및 직접 근거

- [S1] CSEWG, ENDF-102(2023), §0.5.1.1, §3.1/3.3.2, §6.2.4, Appendix E.21. <https://www.nndc.bnl.gov/endfdocs/ENDF-102-2023.pdf>. 이전 실제 원 PDF/text와 source review 근거 재사용.
- [S2] NNDC ENDF/B-VIII.1 n-001_H_001.endf, MF1/451·MF3/102·MF6/102. <https://www.nndc.bnl.gov/endf-data/ENDF/ENDF-B-VIII.1/n-001_H_001.endf>. 원 bytes SHA3024d8f0db604b074e33ed8b05027eb9f5a738614041ba44c83f048e0d0bc1af.
- [S3] NIST ASD5.12/HDEL, 실제 rendered H/D ground rows. <https://physics.nist.gov/asd>. 정확한 query URL·raw receipt·접근 실패 경위는 SOURCE_CONTRACT와 이전 독립 원전 노트에 보존.
- 수학적 판정의 직접 대상: CONTRACT revision2 및 root ATOMIC_BARE_REMAP_KO.md; 추가 source audit나 새 source adoption은 수행하지 않았다.
