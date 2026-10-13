# PHYS19 완료와 PHYS20 재개

## 현재 채택

HH_DEFECT_PARAMETER_CURVATURE를 PROMOTE_SCOPED로 채택했다.
읽기 순서는 README_KO.md → review/DECISION.json →
checks/application/run01/results/SUMMARY.json →
checks/application/readout02/results/SUMMARY.json이다.
원 과학 입력과 producer 실행 snapshot은 변경하지 않았다.

Fλλ와 Fbb는 같은 fixed-alpha C² parameter rectangle에서 엄격히 음수다.
PHYS18의 mixed를 결합한 Hessian determinant는 엄격히 음수이며,
v=(1,-1/24)의 곡률은 양수다.
Corner bilinear 오차 상계는 6.145761081776e-12 K,
pure midpoint 보정은 2.892887673208e-13 K다.
명시한 finite-decimal 계수로 사용할 때는 2.892887673216e-13 K를 쓴다.
계수 중심값 모델의 전체 오차 예산 0.0001557338140092 K를 함께 유지한다.

실제 근거는 main1회, geometry readout2회(입력 field 의미 분리로 수치는 동일),
독립 checker3시도 중 최종1회 성공, Wolfram2회다.
362개 독립 검사와 입력23개가 통과했다.
현재 producer·결과를 바꾼 새 필요가 생기지 않는 한 이 완료된 검증을 재사용한다.

## 다음 첫 행동

PHYS20에서 최신 rei_bianchi 채택 entry로부터 실제 consumer interval 하나를
이름·경로·revision 또는 SHA와 함께 회수한다.
현재 consumer 결박은 이번 루프에서 확인하지 않았으므로 unverified다.
기존 기록의 WAIT_FOR_NAMED_CONSUMER_INPUT를 현재 자료 부재의 증거로 해석하지 않는다.

최소 입력과 admission은 contracts/NEXT_CONSUMER_CONTRACT.json 및
theory/HH_CONSUMER_SOURCE_RESPONSE_HANDOFF_KO.md에 구체화했다.
같은 상태·source·density/frame·clock·COMMON·geometry·closure·process ownership을 확인한 뒤,
원 HH 사건율 q_HH와 온도 quotient에서 다음을 외향 포함한다.

    dotT_HH = ((C_T e_w^T - T l_e)/Pi) nu_H q_HH
    dot e_HH = l_e nu_H q_HH
    (dot n_e)_HH = n_H dot e_HH

원 ν_H=(1,0,0,-χ_H)가 admitted되면
dotT_HH=-(C_T χ_H+T)q_HH/Pi, dot e_HH=q_HH다.
목표 표는 K/s, per H/s, electron density/s 및 같은 상태의 다른 source와 signed total을 담는다.
이는 기존 HH_DOMAIN_SCREEN → HH_MATERIALITY의 한 구간 실측 결박에 해당한다.
Finite interval·matched history는 기존 root/carry 및 RUX11 연결 조건에 맞춰 이어간다.

## 유지되는 연구 구조

NEXT_DAG.json의 첫 14개 node는 PHYS18의 원 기록을 의미상 그대로 보존했고,
15번째 curvature node만 실제 완료로 변경했다.
Global DAG SHA와 global completion 상태는 유지했다.
HH_STRICT_NATIVE와 HH_SINGLET은 자신의 원 microscopic/channel/spin 입력에서
독립적으로 진행하는 lane이다.

입력 복원이 필요하면 REPRODUCE.md의 선택적 archive 복원 명령을 사용한다.
제공 묶음에는 PHYS18 원 dependency archive와 이번 전체 scientific core가 있다.
새 호출·재실행을 완료 근거 확인의 선행 조건으로 만들지 않는다.
