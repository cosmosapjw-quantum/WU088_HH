# PHYS83 completion — matched H I CE, radiative ledger, nuclear ownership

## 재개 위치와 현재 범위

사용자 고정 PHYS82 최종 HEAD `ca9d53983459ea08f9992a8a24663e46b7180344`를
원본 ZIP/외부 delivery JSON과 대조했다. 현재 원격 descendant PHYS83 S0
`09289300ec2e500806aa2cb82365f00329e41c8c`가 원전·유도를 이미 게시했으므로
그 29개 파일을 보존하고 이 별도 completion subtree를 추가한다.
PHYS82 72파일은 복구 ZIP과 현재 checkout에서 동일하며 동결 science51파일도 동일하다.
과거 완료 identity의 계산을 다시 수행하지 않는다.

선택한 원자 모델은 기존 PHYS83 계약 그대로인 source-native H I LS 1s/2s/2p,
W-PL finite matched CE/deexcitation, prescribed T/ne, ground-start,
optically thin spontaneous escape다. 두 양의 eigenmode와 entire functions로
population과 누적 사건 수를 구한다. 기체 열교환, 원자 여기 에너지, 방출 에너지와
photon number를 따로 보존한다. `thermal_change_eV`와 `heat_withdrawal_eV`는
부호가 반대이며, 부모 문서의 Qth 표기 차이를 이 명명으로 해소한다.

병렬 핵 단원은 같은 normal frame에서 thermal/fast 입자수와 에너지 소유권,
finite-T reaction-selected moments의 algebraic prerequisite를 정한다.
실제 nuclear rates와 fast-product stopping은 공급하지 않는다.

## 상태의 권위

`STAGE_STATUS.json`, `EXECUTION_LEDGER.json`, `DAG_OVERLAY.json`이 단계 상태를
분리한다. 각 게시·백업은 `delivery/`의 실제 receipt로 확정한다.
최종 HEAD/ZIP 및 양쪽 raw restore 확정은 외부 final-delivery JSON과 Draft PR 본문이
소유하여 archive의 자기 hash를 내부에 기록하는 순환을 피한다.

현재 사용자 선택 PhysMath 내장1.0.0을 적용한다. 부모1.3.0 산출물의 원문과
identity는 보존한다. 현재 요청이 승인한 CE completion/nuclear prerequisite가
AGENTS의 역사적 PHYS71 scheduling보다 우선하며 과학 기준은 바뀌지 않는다.

원본 full-CCC/CHIANTI 및 논문 내용은 소유자가 제공한 공식 source와 부모 pin으로
추적한다. 부모902 source reciprocity·7 symbolic checks는 재사용하고 새 검사로
집계하지 않는다. 이번 독립 원전 대조의 Anderson corrected Υ는 별도 대안이며
active finite CCC rate에 섞지 않는다.

## 보호 조건

Non-tilted LRS Bianchi I, metric (-,+,+,+), reacting gas pi=0;
collisionless DM pi_m과 fast-particle stress는 별도다. 같은 normal orthonormal
frame의 signed tensors를 합한 뒤 norm을 취한다.
Frobenius=sqrt(2)*half-contraction. 같은 trajectory 성분 분해는 species-off
인과 실험이 아니다. 유한 표본 residual 검사는 continuum certificate가 아니다.

**HH_R10=OFF. Production admission NOT_ISSUED.**
