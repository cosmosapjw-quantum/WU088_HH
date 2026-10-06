# HH-TH03: 생존 광자 상관관계와 terminal source 계수

상태: CORRELATED_PHOTON_SURVIVAL_AND_TERMINAL_SOURCE_BOUNDS_DERIVED__ACTUAL_GAS_ENVELOPES_OPEN.

TH02에서 남긴 실제 photon/gas 상관관계를 진행했다. 동일 cohort의 ON/OFF 생존비를 delta_h의 이력 적분으로 표현하고, positivity를 유지하는 포화 상계를 유도했다. 두 이미 인증된 shear 경계에서 실제 선택 source 상수에 결속한 계수 envelope를 계산했다. 실제 기체 연속해/부호 있는 kink/전체 A는 아직 인증하지 않았다. Native/BE/IVP/history 실행은 0이다.

읽기: THEOREMS_KO.md, RESULT_SUMMARY.json, NEXT_HANDOFF_KO.md. 이 Git 폴더는 검색용 요약이다. 전체 유도·proof script·정확한 분수 구간·원 실패와 성공 로그·선택 입력·claim/DAG는 sealed ZIP에 있다. Git 요약과 ZIP 상세 문서의 byte 동일성이나 Git 폴더 자체의 standalone 실행을 주장하지 않는다.

- ZIP: WU088_HH_TH03_SURVIVAL_MEMORY_BOUND_20261006_v1.zip
- bytes: 125421; entries: 33; manifest payloads: 32
- SHA256: 3eb594d8fdc71769a0ad06ebf2ead3d27402129056d954f9682028e90cdf92a8
- Drive ID: 1LPsIgsukJjDl7E6apjtq2l7LDIOBBja9
- Drive parent: 1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM
- Dropbox ID: id:BSpOijBcT10AAAAAADzg1w
- Dropbox path: /BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/WU088_HH_TH03_SURVIVAL_MEMORY_BOUND_20261006_v1.zip
- 양쪽 create-only 저장 완료와 이름/경로/크기 확인. R1, 새 출력 full remote restore=false.

재현: ZIP의 HH_TH03_20261006_v1에서 `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B research/verify_survival.py --output /tmp/NEW_HH_TH03_CHECKS.json`. 출력은 create-only다. 최종97개 assertion=기호14+정확유리수64+고정밀보조19, exit0/stderr0. 첫 symbolic normal form 실패와 진단, 중간95개 성공 및 최종97개 성공을 모두 보존했다. TDD/형식증명/독립심사는 주장하지 않는다.

HH parent e63d2f54f53a3efd4f667afed5ab1178017aa42b, REI read 06c16abde5df6b48da1382a6a5c56706d8d0ce3d를 게시 전 재확인했고 동일했다. REI SPEC02는 별도 prescribed-absorber/feedback 이론 문서8개이며 실제 HH gas envelope로 전용하지 않는다. 원 S0와 Verner blob은 각각 e97888b06c59d63acb0f35181163d256a6894ed6 / 843b88294972399b3f02659e83002632502d6dd6이다.

HH ACTIVE, canonical S0 OFFcontrol, legacy24/289·265unbounded·epsilon_C/Rnull·B22OPEN_UNDETERMINED·consumedscopes 보존. 다음 최소 적용은 실제 한 terminal-sector의 delta_h tube 또는 누적 S와 endpoint 상관구간이다. 새 승인 요청이나 기존 proof/history 반복으로 돌아가지 않는다. ON06의 coherent point/thermal/event/intervalJet/root/model/checkpoint 연결은 별도다.
