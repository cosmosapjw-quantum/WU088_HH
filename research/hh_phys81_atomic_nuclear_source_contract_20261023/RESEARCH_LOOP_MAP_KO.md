# PHYS81 연구 루프와 계산 연결

## 선택한 질문과 후보

실제 부모 최대온도 25370.66308424773 K에서 문헌에 존재하는 전자충돌 이온화 자료를 어떤 source/energy 조건으로 계산에 사용할 수 있는가? 고정 밀도 common-T 대조계의 과학적 모델을 보존하면서 상태 수를 줄일 수 있는가? 세 방사 포획에서 방출 에너지를 광자와 핵 반동 및 지정 열 저장소로 어떻게 분리할 것인가?

원자 후보 A는 Bell의 전체 에너지 분석 fit K_Bell(T), 후보 B는 CCC 표를 정해진 에너지 구간에만 적분한 K_finite(T)다. 둘을 같은 물리 정확도라고 가정하지 않는다. B를 활성 finite operator로 선택하고 A의 동일 구간/전체 비율을 결측 구간의 모델 의존성을 드러내는 비교량으로 저장한다. A의 정확 양성은 적분의 수학 조건을 확보하지만 문턱 부근 자료 정확도는 별도다.

동역학 후보는 원래 (N1,N2,N3,X1,X2,X3,u) 7변수와 z_s=-log(N_s/N_s0)의 3변수다. 세 원자마다 다른 K_s(T)를 유지하므로 PHYS80의 isotope-shared rate 환원을 그대로 적용하지 않는다. 보존식과 에너지 첫 적분으로 7→3을 유도하고 독립 7변수 solver를 판별 기준으로 남긴다. Jacobian은 두 outer product의 합이다. 입력/좌표 환원으로 얻은 계산량 절감이며 실측 속도 향상 주장은 별도 benchmark 없이 하지 않는다.

핵 후보는 Q를 전부 즉시 열로 넣는 폐쇄와, photon+recoil 및 주어진 ζ로 에너지 소유권을 명시하는 사건 회계다. 후자를 선택한다. ζ 자체는 열적 딸핵 population이나 stopping time을 지정하지 않는다. 이 구별을 유지한 cold-COM 수식과 코드를 완성하고 실제 반응률/finite-T averaging은 원전 입력을 기다린다.

## PhysMath 단계별 상태 (최종 과학 및 전달)

| 단계 | 실제 산출물 | 상태 |
|---|---|---|
| R1 목표·계약 | CONTRACT.json, source/domain/energy/IC | 완료·범위 제한 |
| R2 문헌·재사용 | 최신 refs/backup identity, CCC/Bell/NIST 원전, C22D/PHYS80/REI 재사용 | 접근 가능한 범위 완료 |
| R3 전제 정합성 | Bell B1, Li7 isotope correction, He residual threshold, stationary-target closure | 교정 완료 |
| R4 대안 구성 | 전체 Bell vs finite CCC, 7 vs3 좌표, explicit photon/recoil ledger | 위 식과 판별량 확정 |
| R5 유도 | Maxwell moments/미분, hazard/Jacobian, capture mass shell/count | 완료·선택 모델 |
| R6 독립 검토 | atomic/nuclear fresh-context review, source pixels | 완료·해결된 finding 보존 |
| R7 기호·경량 검산 | Wolfram2, exact rational3, 독립 수치15군/핵15+45 | PASS·각 단위 구분 |
| R8 과학 판정 | source-qualified finite operator와 cold event 회계 채택 | 범위별 채택, full closure OPEN |
| R9 계산 연결 | theory/, registry, finite_ci/parcel/nuclear_recoil | 구현 연결 완료 |
| R10 연구 정리 | S0/S1/S2 보존; S3 handoff 작성, remote restore는외부영수증으로마감 | 단계별 보존 중 |
| C1–C4 기준·매핑·설계·자원 | original7 comparator, fixed gates, create-only identity/shared lease | 완료 |
| C5 구현 | finite moments, 3/7-state equations, recoil API, runner | 구현·문법 확인 |
| C6 구현 검증 | 15 atomic groups, 663 nuclear assertions | PASS |
| C7–C8 과학·수치 검증 | 새3 IVP, refinement/original7, rate profiles | 새3ODE/27profile완료, 비교PASS |
| C9 독립 코드 검토 | 계산 core/runner findings 교정, 저장결과 점검 | 완료·실제 영수증 |
| C10 배포·인계 | Draft PR137, 단계 ZIP, 최종 full restore | S0/S1/S2게시·ACK완료; S3최종fullrestore영수증으로마감 |

HH_R10=OFF는 역사적 HH admission flag다. 위 R10 연구 정리 단계와 다른 객체다. Production admission NOT_ISSUED. 전체 목표의 고정 분모가 없으므로 임의 백분율을 쓰지 않는다. 열린 DAG는 DAG_OVERLAY.json이 소유한다.
