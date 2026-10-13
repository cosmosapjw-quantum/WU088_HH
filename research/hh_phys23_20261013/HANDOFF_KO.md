# PHYS24: 채널별 물리적 envelope 또는 실제 science budget 입력

출발점은 PHYS23의 DECISION.json, RESEARCH_STATE.json, report/REPORT_KO.tex, inputs/RECEIVER_BINDING.json, results/EXPOSURE_CONE.json이다. 조상 PHYS22 원본 묶음도 inputs에 있다.

완료된 내용은 cumulative exposure I(t)에 대한 Z,V 포함, 5개 명시적 처방의 interval hull, 같은 zero-tilt warm P01의 BASS 광학깊이·셀 확률 사상이다. q가 I의 적분 integrand이고, HH-only Jacobian을 전체계로 대체하지 않는다. 동일 source/geometry/IC/Case-A closure와 gas4/photon2904를 유지한다.

다음 작업은 둘 중 실제 자료가 확보되는 경로에서 진행한다.

1. H(1s)+H(1s) -> H + H+ + e_free의 미시 cross-section 또는 rate error 자료를 확보한다. H+ + H− 채널, excited associative ionization과 분리한다. COM/LAB 에너지, threshold, spin/event multiplicity, identical-pair convention, native units, 데이터 에너지 범위와 tail을 고정한다. sigma_-(E)<=sigma(E)<=sigma_+(E)에서 양의 Maxwell kernel로 k_±(T)를 계산한다. 처방 hull과 물리적 error envelope를 구분한다.
2. 실제 consumer owner가 부여한 온도·전자·tau·cell probability의 science budget을 회수한다. 지금 읽은 BASS 계약의64eps/256eps는 알고리즘 검증 기준이다. 물리적 budget으로 조용히 바꾸지 않는다. 보고서6.3의 충분조건으로 허용 A를 계산하고 source envelope와 비교하여 생략/정밀화 결정을 한다.

공급된 새로운 envelope가 기존A<=1.1을 넘으면, PHYS22 majorants를 즉시 버리지 말고 Vtube+(A-1)t_f|nu|qhi<r의 exact 조건을 먼저 검사한다. 현재 box sufficient cap은 약1.2058e8이며 실제 원자 rate 상한을 뜻하지 않는다. 바뀐 time/geometry/closure는 해당 의존성만 다시 평가한다.

Wolfram과 xAct의 현재 코드·성공 필드는 wolfram에 있다. 같은 assistant의 별도 산술을 외부 심사라고 쓰지 않는다. HH_STRICT_NATIVE, HH_SINGLET 및 전체RUX 의무는 자기 lane에 보존한다. 새 무거운 계산은0개이며, 자료가 필요한데 아직 확보되지 않았다는 이유로 새로운 no-go 결론을 만들지 않는다. 필요한 에너지 bin 오차 예산 또는 Maxwell positive-weight 계약을 실제로 산출한다.

원격 게시 및 백업 identity는 외부 최종 delivery receipt를 확인한다. 업로드 ACK와 실제 restore 검증을 구분한다.
