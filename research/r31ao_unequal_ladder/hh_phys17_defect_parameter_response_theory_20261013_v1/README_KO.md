# WU088_HH PHYS17 — 상관 매개변수 응답

**독립 판정: `PROMOTE_SCOPED`.** PHYS16의 동일 COMMON과 고정 admissible
α 계열에서 실제 two-half–Full 결함의 λ·b 응답을 구성하고 포함했다.
원 source·근·history를 다시 실행하지 않고 PHYS09/11/14의 signed carry와
PHYS16의 작은 endpoint 결함을 재사용했다.

## 결과

| 온도 결함의 1차 응답 | 원 매개변수 직사각형 전체의 포함, K |
|---|---|
| ∂λΔT | [−1.009599125635×10⁻⁸, −8.137506081166×10⁻⁹] |
| ∂bΔT | [6.776348385589×10⁻⁵, 7.185335549648×10⁻⁵] |

HH의 직접 forcing과 상태 feedback은 모두 음의 응답을 만든다. Birth의
직접 forcing은 양수이며 작은 음의 상태·opacity feedback을 포함한 뒤에도
전체 응답은 양수다. 모든 전달은 같은 Full Jacobian과 양의 유한 온도
분모를 사용한다. λ,b는 무차원이며 같은 값이 두 단계와 Full에 적용된다.
정칙성은 상속한 C² source/root family, gas 좌표는
`(x_HII,y_HeII,y_HeIII,w_eV_per_H)`다.

핵심 구성은 다음과 같다.

- 원 thermal source의 `Fw+χH Fx`에서 helium 계수를 분리하는 정확한
  항등식으로 density/time bridge의 gas 미분을 C²에서 닫았다.
- 작은 stage increment와 그 미분을 gas movement·opacity 변화에 함께
  사용하고 원 photon 일곱 sector를 같은 전역 매개변수로 미분했다.
- P2의 `H_gg[d,yθ]+H_gθ d`를 적용한 뒤 원 `C,B,q,S`로 `dθ`를 포함하고,
  P4의 유한 온도식을 사용했다.
- 같은 `J_F`의 explicit forcing/feedback과 유한 m=2 Neumann 오차를
  별도 저장 연산으로 포함했다.

## 읽을 파일

| 목적 | 파일 |
|---|---|
| 정리·유도·source 연결 | `theory/PARAMETER_RESPONSE_THEOREM_KO.md` |
| 실제 결과 | `checks/application/run02/results/PARAMETER_RESPONSE_RESULTS.json` |
| 직접 forcing/상태 feedback | `checks/application/forcing01/results/FORCING_FEEDBACK_RESULTS.json` |
| 유한 inverse 오차 | `checks/application/neumann02/results/DERIVATIVE_NEUMANN_RESULTS.json` |
| 유한 변화·등결함 곡선·혼합 contrast의 사전 포함 | `theory/PARAMETER_COROLLARIES.json` |
| 실제 적용 방법·실패 교정·실행 기록 | `evidence/intake/APPLICATION_METHOD_AND_RESULTS_KO.md` |
| 독립 판정과 별도 exact 검산 | `review/INDEPENDENT_REVIEW.json`, `review/arithmetic02/INDEPENDENT_ARITHMETIC_RESULTS.json` |
| Wolfram/xAct 실제 코드·결과 | `checks/wolfram/parameter_response_checks.wl`, `checks/wolfram/SUMMARY.json` |
| 한국어 보고서와 재컴파일 | `report/WU088_HH_PHYS17_THEORY_20261013.pdf`, `report/BUILD_KO.md` |
| 복원·재개 | `HANDOFF_KO.md`, `DEPENDENCIES.json`, `NEXT_DAG.json` |

독립 exact Fraction/Cramer 검토 29개 묶음이 모두 통과했다. 실제 Wolfram
15.0.1+xTensor 1.3.0/xPerm 1.2.4에서는 tensor 검산 6개와 scalar 9묶음의
15개 성분이 모두 정확히 0이었다. Candidate 실행 파일의
`CANDIDATE_COMPUTED` 상태는 원 실행 기록으로 보존하며 채택은 별도 심사에
연결한다. 공개·전달 상태의 실제 identity는 동봉된 detached delivery
receipt를 따른다.

## 다음 연구

다음 노드는 **`HH_DEFECT_MIXED_RESPONSE`**다. 원 U,V,W와 C² source Hessian을
사용해 `Wd=∂λb(g2−gF)`, `∂λbΔT`, 네 모서리 contrast
`I=ΔT(1,1)−ΔT(1,0)−ΔT(0,1)+ΔT(0,0)`를 포함한다. 현재 1차 결과로 확보한
`|I|≤1.958485175177039×10⁻⁹ K`를 비교 기준으로 유지한다. 실제 mixed
application은 아직 실행하지 않았으며, 시작식 M1–M16과 입력 대응은
`theory/NEXT_MIXED_RESPONSE_PROPOSAL_KO.md`에 있다.

원 PHYS16 연구 묶음에는 PHYS15 전체 스냅샷이 중첩되어 있다. 실제 ZIP
목록에서 원 U/V/W carry와 `INPUT_RESTORE.json`의 다섯 대형 입력이 모두
포함됨을 확인했다. 복원은 파일 materialization이고 과거 물리 계산의
재실행은 필요하지 않다.
