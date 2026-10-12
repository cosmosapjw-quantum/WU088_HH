# WU088_HH PHYS15 재개 지점

## 완료된 이론 단위

2026-10-12 KST에 시작한 다음 이론 루프를 built-in 1.0.0 THEORY R1–R10으로 수행했다. 독립 `review/DECISION.json`은 2026-10-13 KST에 **PROMOTE_SCOPED**를 판정했다. 같은 COMMON의 잔차, 광자 일곱 absorption 항, 원 source의 density/fhat bridge, 기존 Full 수축의 평균 Jacobian 전달, 유한 T/e/w/ne 및 adjoint, guard 수지와 실제 photon secant가 완성됐다.

최종 검토가 결박한 원고는 다음과 같다.

| 원고 | SHA256 |
|---|---|
| 통합 이론 | `60c9d5e52df1fa43e317c2043598e0d44ed89854c79dad4bed474aa4f200ef61` |
| 광자 이론 | `252908a82fef7c9975d442182d487163ee8cf84257eaacc6b7c8a306937c4de2` |
| 원 source 정규화 | `16e23676dbe6a1c0805728c7e01c22d7e37f97c990e892e7d75e6cd2f3718b41` |
| 기존 Full C/B/q/S 결박 | `7d0c6db4469d8947cd854378ee41319e855963b0ad3e40afa60a107cdc2a6731` |

## 다음 정확한 작업

다음 단위는 **HH_CORRELATED_ENDPOINT_ENCLOSURE**다. `contracts/ENDPOINT_ENCLOSURE_CONTRACT.json`의 입력과 식을 사용하여 실제 residual/endpoint 포함기를 구현하고 실행한다. 첫 구현의 함수는 `assemble_correlated_defect`와 `enclose_endpoint_defect`다. 별도의 실제 source나 root 재계산보다 먼저 기존 원자료에 검토된 차이식을 적용한다.

1. 같은 COMMON, ρ와 ρ², captured MF=2M, 같은 λ,b를 공유하는 입력 객체를 만든다.
2. source 시각·기체 이동 및 photon 일곱 항을 묶어 r를 계산한다. 필요하면 원 FT03의 kwHe 성분을 같은 frozen graph에서 포함한다.
3. 저장된 C,B,q,S와 r로 d를 포함하고, d∩(Cr+Ed)로 교차한다.
4. 같은 d와 유한 분모로 ΔT/e/w/ne를 평가하고 같은 inverse로 항별 기여를 계산한다.
5. 같은 dx를 사용해 실제 Full photon endpoint까지 옮긴다. Guards의 number/energy ledger를 적용한다.
6. 실제 결과 폭을 근거로 필요한 포함 개선을 선택하고, scoped numerical decision을 받는다.

현재 이론에는 새 endpoint 수치 구간을 만드는 실행이 포함되지 않았다. 다음 구현이 검증된 뒤 그 실제 명령·코드 identity·wall/CPU/RSS·exit와 출력 경로를 기록한다. 미구현 명령을 실행 완료로 기록하지 않는다.

## 재사용할 원 근거

`inputs/phys14/`에는 원 PHYS14 source·root·carry 및 입력을 그대로 보존했다. `inputs/ncp07_additions/`의 first-half SOURCE_CENTRE, HH 원 source, Full UNIFORM_ARITHMETIC은 원 NCP07 archive의 pinned member다. 기존 Full 전처리는 동일 파일의 fixed_C, B, radius 및 q=0.00011736830563768177을 함께 사용한다. C를 다시 inverse하지 않는다.

기존 source·근·첫 두 단계의 유효성은 상속 전제다. 이번에는 이 전제를 다시 실행하지 않고 정확한 leaf 대응·새 유도·판별 대수로 진행했다. PHYS14의 actual two-half와 독립 Full을 같은 고정 계열에서 비교한다. Root/pullback segment는 원 convex X의 내부에 있다.

원 파일들은 `inputs/INPUT_MANIFEST.json`, 아카이브와 Git의 연결은 `evidence/bindings/`, 새 증명·수치 검산·독립 검토는 `theory/`, `checks/`, `review/`에 있다. Git에 큰 원 입력을 넣지 않은 항목은 `INPUT_RESTORE.json`에 따라 원 archive에서 복구할 수 있다. 전체 연구 ZIP에는 실제 입력을 포함한다.

## 현행 정책과 이력

사용자가 이번에 명시한 built-in 1.0.0이 기존 v4의 기본 진입을 대체한다. 이전 규약과 과학 결과는 역사 기록으로 유지했다. 변경된 의존성부터 필요한 작업을 이어가며, 이미 결박된 승인과 근거를 재사용한다. 과거 suite·source·root·history를 다시 실행해야 할 새 조건은 현재 없다.

PHYS14의 원 Git parent는 `087a16f28d0ee4fc7ae74ae50bfcafe578716e85`이고 tree는 `61a4dc1ed1bf42530ed8fda9596a91962e9912e7`다. 이번은 이 parent 위의 additive 연구 branch다. 실제 새 commit/PR와 Drive·Dropbox ACK는 게시 후 별도 delivery receipt에 기록한다.

원 global REI DAG bytes와 기존 열 개 HH node 값은 유지했다. 현재 endpoint-defect node는 이론을 채택하고 수치 후속 node를 추가했다. Heavy queue는 비어 있으며 실행 launch는 false다. 독립 microscopic/native 경로의 고유 과학 조건은 보존한다.
