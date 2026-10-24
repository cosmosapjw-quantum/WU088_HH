# PHYS88 R6 — 실제 symbolic 실패·복구와 양의 branch 독립 검토

**PASS_SCOPED_PREIMPLEMENTATION_WITH_MANUAL_POSITIVE_BRANCH_CLOSURE. 열린 material finding 0개.** 이 문서는 앞선 R6를 보존한 채 실제 symbolic 실행 이후의 근거를 덧붙인다. 현재 권위 계약은 revision3, SHA `8f45d6a70d7cf7ffcc556b74636f25087167a3372f781eee4078f5dd00e4154d`다.

## 실제 출력과 실패 보존

첫 호출은 `Export::jsonstrictencoding`의 `Times` expression 직렬화 실패와 `$Failed`를 반환했다. 그 응답에서 잔차0을 채택하지 않았다. Root는 동일한 defining expressions에 대해 InputForm 진단 출력을 한 번 허가했다. 두 script의 output 이전 정의가 같음을 실제 파일 비교로 확인했다. 원 실패·코드·수정 허가 기록은 보존된다.

두 번째 실제 raw는 **13개 residual group 중12개, scalar component18개를0**으로 반환한다. `COM_inverse_map`은 radical expression으로 남고 `all_zero=False`다. Monotonicity도 `h+sqrt((a+b)^2+2bEb)>b`라는 predicate로 반환된다. 이 출력을19개 CAS zero 또는 자동 monotone=True로 바꾸지 않는다. [E1–E4]

## 실제 미단순화 항의 독립 증명

동결 도메인은 a,b,h,Es>0이며 h=a·awr다. Ms=a+h, Mb=a+b, Ws=√(Ms²+2hEs), K=Ws−Ms>0으로 두자. Eb=K(2Mb+K)/(2b)를 대입하면

\[
M_b^2+2bE_b=(M_b+K)^2,\qquad M_b+K>0.
\]

따라서 principal real square root는 Mb+K다. Recovered bare K는 K이며 K(2Ms+K)=2hEs에서 recovered Es=Es를 얻는다. 이 branch는 새 가정이 아니라 이미 동결한 양의 도메인으로 고정된다.

실제 raw가 돌려준 긴 항도 직접 대조했다. h=a·awr로 쓰면 잔차는 `(h−b)/h`와 `h−b−Ws+sqrt(R)`의 곱이다. 긴 radicand R은 **(Ws+b−h)²=(Mb+K)²**로 정리된다. Ws+b−h=Mb+K>0이므로 남은 bracket은 정확히0이다. 의도한 mapping 식만 확인한 것이 아니라 실제로 반환된 expression의 부호 branch까지 닫았다.

미분식 dEs/dEb=b(Ms+K)/[h(Mb+K)]는 양수다. 반환된 predicate도 √((a+b)²+2bEb)>a+b>b와 h>0에서 성립한다. 미단순화는 nonzero counterexample가 아니다. 이 증명은 추가 evaluator·numerical substitution을 쓰지 않는다.

## 수치 token 및 누적 예산

저장된 실제 출력의 nominal 분해는 다음과 같다. 이것은 표시 rational token에 대한 산술이며 physical uncertainty 또는 질량이 물리적으로 exact하다는 뜻이 아니다.

| 항 | 실제 받은 eV 값 |
|---|---:|
| QS−Qb | 81.63 |
| BD−BH | 0.003700036867 |
| ρH−ρD | 81.626299963133 |
| ΔH | 510956.383150562 |
| ΔD | 510874.753150562 |
| ρH | −28.969104838298 |
| ρD | −110.595404801431 |

새 symbolic call은 최초 실패1+명시적으로 허가한 복구1=2다. 기존5를 보존하여 lineage7, 새 잔여 allowance0·old additional allowance0이다. 예산을 reset하지 않으며 세 번째 호출을 요구하지 않는다. 이 독립 검토자의 evaluator/scientific 실행은0이다. [E3,E4]

앞선 R6의 실제 metric/acceptance finding도 그대로 보존한다. 구현은 revision3을 결속하고, 다음 C9는 실제 코드·새 수치 raw를 검토한다. Parent는 PARTIAL, empirical kernel/electron-state·consumer·stopping은 OPEN이며 production은 NOT_ISSUED다.

## 직접 근거

- [E1] `theory/WOLFRAM_ATTEMPT1_RAW.json`: 실제 최초 failure 응답.
- [E2] `theory/WOLFRAM_REPAIR1_RAW.json`: 실제 두 번째 residual associations·False·predicate·nominal output.
- [E3] `theory/WOLFRAM_RESULT.json`, `theory/POSITIVE_BRANCH_CLOSURE_KO.md`: root의 제한된 판정과 branch proof를 독립적으로 대조.
- [E4] `reviews/SYMBOLIC_REPORT_REPAIR_AUTHORIZATION.json`, `CONTRACT.json` revision3: 실패 보존 및 정확히 한 번 복구의 명시적 예산 변경.

각 실제 파일의 bytes/SHA는 동반 `R6_SYMBOLIC_RECOVERY_REVIEW.json`에 결속했다. 이전 R6 파일은 수정하지 않았다.
