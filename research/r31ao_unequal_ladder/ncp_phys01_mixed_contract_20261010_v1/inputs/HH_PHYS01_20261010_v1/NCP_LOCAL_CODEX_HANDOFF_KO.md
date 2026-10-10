# HH-PHYS01 물리 결과의 NCP 적용 인계

이 문서는 기존 ENERGY06E의 actual-owner root/preconditioner 및 승인 의무를 대체하지 않는다. 새 NCP native 과학 dispatch 승인은 포함하지 않는다.

## 계승할 물리 결과

같은 초기 gas/photon 상태에서 HH 강도 lambda와 단색 방출률 S의 유한 사각차이 I=x(lambda,S)-x(lambda,0)-x(0,S)+x(0,0)를 정의한다. smooth frozen source-stage의 선도항은 I= -lambda S A q(4+Xi)delta³/6이다. 여기서 Xi=(1-x)/Pi*(T k'/k)*(1-T_gamma/T), T_gamma=2(E-chi)/(3kB), A=c nH sigma다. 현재 13.7eV 및 약49489K에서는 Xi>0이다. 이 부호는 충분히 작은 delta의 물리적 비가산 억제이며 전체 HH_ON-OFF가 음수라는 뜻이 아니다.

원 BE source에 constant birth를 넣는 frozen 비교의 mixed 계수는 full=-(3+Xi), twohalf=-(13/8+Xi/2)다. 실제 time/angle-dependent owner macro의 계수라고 자동 채택하지 않는다. 코드의 source-only 항을 이 값에 강제로 맞추거나 기준을 완화하지 않는다.

## 가장 작은 다음 실제 적용

1. 현재 NCP ENERGY06C 및 후속 actual-owner 작업의 source/birth/numerical guard/authorization 상태를 먼저 읽는다. 이전 보호 파일과 consumed FD1/FD2/6cell, G256 checkpoint를 보존한다.
2. 이 패키지의 INPUT_IDENTITY, THEORY, results/LOCAL_COEFFICIENTS_FINAL, SYMBOLIC 및 CAUSAL_KERNEL을 읽는다. 이미 검증한 HH-PHYS01 전체 suite를 의례적으로 반복하지 않는다. 새 host 수입은 manifest 검사와 해당 의존성 확인만 수행한다.
3. 실제 검증할 관측량을 구분한다: 전체 HH 응답 D, 새 S와의 혼합 I, full/twohalf HH defect, 전체 source-law/time error는 다른 양이다. 네 모서리의 기준 state와 theta를 정확히 고정한다. S=0 코너는 미래 방출만0이고 기존 photon stock은 지우지 않는다.
4. 우선 frozen source의 이산 근 family에서 mixed parameter 또는 네 코너의 correlated difference를 반환하는 구현·합성시험을 한다. 방정식에 이전 gas/photon 민감도와 birth measure를 유지하며, 고정 C와 원 full chain Jacobian을 trusted certificate에 결속한다.
5. 해당 실행이 별도 정확 승인을 받고 실제 coupled tube가 닫히면, 기존 예산 안의 최소 한 macro에서 mixed remainder 또는 interval 혼합차이를 평가한다. delta³ local scale과 같은 부호/크기가 나오도록 root 폭이나 tolerance를 조정하지 않는다. 고정 h 값의 Taylor 숫자는 acceptance reference가 아니다. 기존 네 corner를 무차별 재실행하지 않는다.
6. continuous 목표는 F0+lambdaH+SB의 true flow다. Owner birth@end 뒤 full BE 노출을 t=end의 물리적 delta-kick와 같게 취급하지 않는다. 변하는 밀도·에너지·방향·threshold/hat-cell을 넣으면 실제 미분·remainder를 추가해야 한다.

현재 source의 제약이 유지되면 가장 낮은 mixed order의 각도계수는 normalized monochromatic source에서 sum weights만 의존한다. 이것을 Bianchi의 전역 1차 소거·epsilon² 정리나 cutoff 부근의 매끄러움으로 확대하지 않는다. REI PHYS19/PHYS20의 HH-OFF 연속 source·Bianchi 연구와 HE E13C1의 photon-only chronology는 별도 owner 결과다.

## 반환

MODEL_AND_CORNER_IDENTITY.json, MIXED_RESPONSE.json, REMAINDER_OR_UNRESOLVED.json, ROOT_PRECONDITIONER_BINDING.json, RUN_LEDGER.jsonl, CLAIM_LEDGER.json, 실패 원로그, 변경된 파일과 검증, 정확 예산/실행 승인 영수증, checkpoint 보존 및 두 cloud ACK를 반환한다. 물리/수학/수치/구현/실행환경/권한의 실패를 구별한다.

C1 24/289 및 265 미상계, epsilon_C/R null, B22 OPEN, canonical S0 OFF control, physical/production HOLD를 유지한다. 본 물리 결과로 legacy 원자 적분을 재개하지 않는다. Git은 기존 연구 브랜치에 비강제 추가형으로만 게시하고, Drive parent1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM 및 기존 WU088_HH Dropbox 폴더로 create-only 백업한다. R1 ACK와 실제 remote restore는 별도다.
