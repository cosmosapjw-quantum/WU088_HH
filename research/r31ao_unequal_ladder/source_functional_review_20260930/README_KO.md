# R31AO 완료 결과의 source-functional / decision-bound 검토

## 반환 요약

- 검토 HEAD: `e89ff30f508731b8e2694d51cef1b3223794af4d`
- tree: `fc624042129ed3decd9b0e8ed2df64440886cd10`
- intake 시 remote successor 없음. 원 consumed authorization과 reviewed_commit을 보존했다.
- 기존 order-study와 원 postprocessor/tests를 재실행하지 않았다. 새 science commands/nodes=0.

| 산출물 | 내용 |
|---|---|
| [SOURCE_FUNCTIONAL_MAP](SOURCE_FUNCTIONAL_MAP.md) | Frozen107의 연속 mixed D 함수형, 실제 OD/JVP/assembly 함수와 archive/member/SHA |
| [DECISION_BOUND_DERIVATION](DECISION_BOUND_DERIVATION.md) | epsilon_C/R에서 K/Dmax로의 상계 및 원 Pareto rule에 대한 lower-gap 유도 |
| [PROOF_OBLIGATIONS_AND_STOP](PROOF_OBLIGATIONS_AND_STOP.md) | quadrature, weight, special function, tail, 조립, 진단 연산의 비중복 오차 분해와 정확한 blocker |

source 기능을 추적한 19개 실제 파일은 archive member와 일치하며 missing identity는 없다. 파일 가용성과 byte identity는 오차 인증과 별개다. epsilon_C, epsilon_R 및 eta의 실제 인증 상계는 **null**이다.

증명된 조건부 관계는 epsilon_K <= (epsilon_C+epsilon_R)/2, epsilon_Dmax <= max(epsilon_C,epsilon_R), lower_gap_j=published_gap_j-2 epsilon_j-eta_j이다. 각 비교에서 두 lower_gap>=-tol이고 하나가 >tol이면 원 Pareto support에 충분하다. eta=0을 가정한 더 보수적인 공통 block strict 예산 epsilon<0.02856621001324109/t_a는 설계 목표이며 실제 error estimate/bound가 아니다.

다섯 block의 음의 real Frobenius alignment는 현재 triplet의 positive-direction single-term 해석과 양립하지 않는다. 이는 발산, producer 결함 또는 roundoff 원인 확정이 아니다. 원 conditional p/E와 machine labels는 수정하지 않았다.

`B_ORDER_VERDICT_STABLE_OVER_128_160_192` 및 세 order의 원 PRIMARY/SECONDARY verdict는 그대로 보존한다. `SOURCE_ACCURACY_BOUND_UNAVAILABLE`, `RIGOROUS_REFERENCE_CERTIFICATION_BLOCKED_BY_MISSING_ERROR_BOUND`, rigorous=false를 유지한다. 공통 implementation bias는 order difference에서 소거될 수 있다.

O/independent dotO 진단과 R31AK model/training/knot state를 보존한다. Full-cell, fixed-Q complete-HH physical invariance, BR01/BR02, independent decision review, interval-wide/transition/trajectory/H-skip/production gate는 열지 않는다. 다음 수치 certificate workload는 별도 승인 대상이며 이 반환에서 scope를 자동 발급하지 않는다.

`RETURN.json`은 검토 identity, sidecars 및 남은 gate를 기록한다. Publication과 create-only Drive/Dropbox ACK+metadata 검증은 별도 receipt에 기록한다. Raw restore 미수행: RESTORE_VERIFIED=false. 새 백업은 이 분석 산출물 범위이며 이전 raw/runtime/provider backup을 대체하지 않는다.
