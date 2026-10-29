# WU R29 결과 | 열적 상향 충돌을 고려한 HD 5준위 생성물·광자 분기

**물리적 새 산출물:** 원래 GL2022 2022 JCP 157,214302 인쇄 SQM rate 350 reactive / 70 nonreactive downward, REC161 4 Einstein A와 REC162 5 CDMS2011 v2 인쇄 HD 준위에 조건부 thermal detailed balance를 적용한 5-state absorbing generator. 원본 7개 온도 노드 × 2개 명시된 chemical spin 정책 × 3개 proton n/ncrit × 5 초기 J = **210** source-derived conditional cases; 210×10=**2100** H2(v'=0,J'=0..9) product branch cells. 관측자료, 실제 우주 시간진화, full vibrational product 총 분기, native PES Q를 계산하지 않음.

**강력한 구별:** 제한 조건 `T=105 K`, 초기 J2, n=ncrit_J2, Eq6-7 spin policy에서 즉각적 첫 사건 photon 확률 `0.091265045636`, 제한 반응까지 광자 ≥1개 확률 `0.473628517450`, 광자 기대수 `0.888027556749`, 평균 반응 대기시간 `173.6286 days`, 제한 H2 홀수 J' 생성비 `0.592566851212`. R28의 3-first-event 모형(상향 미포함) 첫 photon ≈0.092926은 동일 네트워크가 아니므로 등치 금지. 동일 105K 조건에서 *upward collision을 고의로 제거한 별도 반사실적 Markov*의 광자 ≥1개 확률 `0.106826008177`, 55K는 상세평형 포함 `0.755839559516` vs counterfactual `0.046087045532`다. 반사실적 down-only는 thermal equilibrium model이 아니다.

**원전 미정리 존중:** 15K 반응 표기 0, 1505K HD J1 비반응 의심 지수, 2505K 반응 J3 생성 J'7 의심 지수를 포함하는 온도는 거절한다. 인쇄 중복 J5로 인해 소스 불명확한 J5를 화학 sink로 쓰지 않으며, J6을 출발 또는 복사 이후 상태로 몰래 추가하지 않는다. 온도 보간·합성 cross section·Q 보정·다른 페이로드 보충 없음. Source-native 700/1560 표 자체의 실측 오차가 주어지지 않았으므로 원본 decimal 인쇄 오차를 physics uncertainty로 오해하지 않는다.

**실측 crosswalk:** REC163의 원저자 1984 J4−J3 `350.852±0.002 cm−1`과 REC162 2011 CDMS nominal `350.852958 cm−1` 간 차이 `+0.000958 cm−1` (1984 명시 수치 구간 내부). 2011 fit과 1984 실측은 서로 관련될 수 있어 독립 통계적 goodness-of-fit이라고 말하지 않는다. 이 검산은 `HD levels` 입력의 출처 정합에 국한되며 원본 산란 반응률 검증으로 승격하지 않는다.

**증명과 수치:** nonnegative transient generator, positive chemical sink, exact absorption identity `∑ reaction_prob=1` (제한된 반응 생성물 집합 내), collision-only Boltzmann stationary/ detailed balance, photon-count identity, first-photon-before-exchange 확률을 원래 수식에서 직접 유도. Python 20/20 normal, 20/20 `-O`, compileall, SciPy DOP853 microscopic transient reference, independent-source 210/210 mpmath75 compare max relative ~5.27e−14. Wolfram symbolic 3-level detailed-balance/absorption algebra verified. Same-author independent method, not R6/C9 different-author reviews.

**Scientific gate:** canonical original WU 34/49 UNCHANGED. R29 auxiliary conditional source science `1/1_SCOPED`. Source native sigma(E) and PES energy zero missing; physical_Q, original heat, molecular REC/CR owner ACK, full_A remain NULL. HH_R10=OFF, L4=false, production NOT_ISSUED. No main merge/foreign mutation. Native subagent tool absent, R6/C9 NOT_RUN.

All commands, per-stage source-anchored evidence and exact archive provenance in README_REPLAY, THEORY_KO, SOURCE_IDENTITY, DAG_DELTA and final detached handoff.