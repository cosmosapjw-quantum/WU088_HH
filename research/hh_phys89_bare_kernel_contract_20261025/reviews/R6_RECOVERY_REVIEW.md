# PHYS89 복원 계약의 독립 R6 검토

현재 판정: **PASS_SCOPED_PREIMPLEMENTATION**. Parser·covariance·정규화·소유권의 핵심 식은 한정된 정의역에서 타당하다. 선택 물리 노드는 PARTIAL이고 실제 consumer 수용은 미발행이다.

검토자는 이론 및 코드 작성에 참여하지 않았으며 원전/원계약 대조와 직접 대수·단위 검토만 수행했다. 새 과학 child·Wolfram·적분·원격 변경은 모두0이다.

## 단일 지적 P89-R6R-01 — actual readback으로 종료

Thermal count h−2와 caloric 식은 두 입사 n,p가 thermal reservoir 소유라는 조건을 요구한다. C_V=sum_s n_s ∂u_s/∂T>0는 고정된 species densities에서 정의하고, 식의 dotT를 capture 반응 기여로 표시해야 한다. Expansion/work 및 다른 source는 전체 온도식에 별도로 들어간다. 현재 유한 fixture와 source PSD 진단은 이 명시로 수치식이 바뀌지 않는다. 이 조건을 CONTRACT와 이론에 짧게 추가한 뒤 해당 부분만 readback하면 지적을 닫는다. Tail bound의 0≤Z_tail≤B0도 같은 문맥에서 명시하면 된다.

## 독립적으로 확인한 연결

정규화 유한 변화는 (δA−MδZ)/(Z+δZ)이고 일차 변화 b·η를 뺀 잔차는 −δZ/(Z+δZ)·b·η이다. 따라서 |δZ|≤ρZ, 0≤ρ<1에서 명시된 remainder가 따른다. 같은 source field를 사용하면 LFLᵀ/BFBᵀ를 공유해야 하며, signed reward group rows의 합0은 covariance 합계 row0을 보존한다.

Source MF33는154boundaries/153groups/11781packed entries이며 cross-section153knots/152cells와 다른 grid다. Fractional covariance의 pullback은 group index를 운반하고 Jacobian은 integration measure에만 붙는다. 실제 outside-support kernel과 tail bound는 여전히 공급되지 않았다.

여섯 사건 energy columns의 합은 K_d+E_gamma−K_in−Q_b이므로 보존식 아래0이다. Species source가 (−1,−1,+h)이면 S_U−Σu_s S_n_s가 명시된 caloric numerator를 준다. Clock/reference 식은 quotient 미분과 expansion dilution을 함께 대입하여 확인했다.

REI-L2 actual beta scope를 capture 구현으로 승격하지 않고, 두 capture/radiation 요청의 owner/ACK는null로 유지했다. Displayed F에 exact negative witness가 생겨도 해당 표의 PSD 반례로만 해석하고 evaluator/physical model에 대한 strong no-go를 주장하지 않는다.

## 이어갈 절차

이 한정 조건의 readback 후 scoped preimplementation PASS로 전환한다. 실제 code 및 신규 source/fixture 실행은 별도 C 단계이며 아직 검토·수용하지 않았다. 사용한 Wolfram allowance는 원 rawbytes 소실과 별개로 보존한다.

## 한정 교정의 실제 readback

CONTRACT revision4 SHA256 `d737abf473a8ee6ef2c98262d4c6bb463e5ac800aab7eb442ed56d4e56baf663`와 이론 SHA256 `6b04e9f2f8402821a5718620924ab4baf19064e9f19faefb0df3164110df2806`를 직접 읽고 대조했다. 두 입사 thermal 소유, positive C_V, capture-only dotT, 비음수 tail 조건이 명시되었다. 원 식은 유지되며 새 과학 계산은0이다. P89-R6R-01을 CLOSED로 전환하고 preimplementation scoped PASS를 채택한다. 이후 code/실행/C9는 별도 의무다.
