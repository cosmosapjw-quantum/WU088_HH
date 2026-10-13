# PHYS23 이후 재개

먼저 DECISION.json, RESEARCH_STATE.json, results/PHYS23_RESULT.json을 읽는다. PHYS22의 전체 의존 묶음은 inputs/에 보존되어 있다.

이번에는 누적 사건수 Q로 정규화한 정확한 유한 응답 cone W=(I-P)^(-1)|nu|, V=PW를 증명했다. 전자 응답은 (1-ell.V)Q..(1+ell.V)Q이고 ell.V=0.03426165460392323다. 온도는 -72894.51840866Q..-70796.35234679Q K로 제한된다. 이 값과 동일 box의 P를 재사용한다. 다른 시나리오/구간에서 그대로 수치계수를 상속하지 않는다.

LCS91, HM89, HM79, D69, KS91:G15의 다섯 수학적 prescription과 convex hull을 실제 온도 box에서 평가했다. KS91:G15는 저에너지 근사식의 warm-box 평가로 표시했다. 이 집합의 spread를 실험 confidence interval로 바꾸지 않는다. D69의 보조 질량비는 0..1/1800이며 점 표는1/1837이다.

BASS PR141 revision d520c5e47ebf5cf218351082430ae3ef5e1ab3ec의 beta=0 시간/상수/선형 edge rate/유한 cell mass 정의를 읽어 정확한 해석적 전달식을 연결했다. 첫 edge depth의 상대 경계와 모든 nonzero-edge depth의 균일 상대 경계는 다르며 JSON에서 따로 보존한다. 기존 수신 tolerance는 numerical reference 비교 기준이다. 이번에 native receiver를 실행하지 않았고 이전 prelaunch hash 누락 이력도 변경하지 않았다.

다음 PHYS24_WEIGHTED_CROSS_SECTION_ENVELOPE_AND_BUDGET_BINDING에서는 NEXT_INPUT_CONTRACT.json의 실제 물리 입력을 채운다. 기존 microscopic lane에 같은 free-electron channel의 자료가 있는지 source/basis/spin/pair/energy-frame identity를 읽고 맞춘다. 양의 Maxwellian energy-bin kernel과 tail을 써 k 상하계를 만든다. 실제 온도/전자/Thomson budget이 주어지면 보고서식6.5의 역방향 rate ceiling에 대입한다. 값이 아직 없으면 어떤 입력을 추가로 구해야 하는지 정확히 유지하되, 가능한 source-bin 가중 계산을 수행한다.

완료된 warm 명목 ODE·source·tangent 캠페인을 반복하지 않는다. 원자 수치학의 관측량 필요 정밀도를 먼저 결정해 heavy 계산의 실제 목표를 고정한다. 신규 원격 게시/백업은 이번 루프에서 하지 않았다. PDF/ZIP의 실제 위치와 hash는 detached 전달 기록에 있다.
