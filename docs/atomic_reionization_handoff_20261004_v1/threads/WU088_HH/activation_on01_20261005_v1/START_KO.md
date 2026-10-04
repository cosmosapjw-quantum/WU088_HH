# HH-ON01: 명시적 opt-in 연구 활성화와 native HH source

사용자의 새 요청 “새 HH 활성화 연구 루프를 이어서 진행해줘.”에 따라 선택적 HH 연구를 ACTIVE로 전환했다. 기존 S0 HH OFF와 REI F08 production source는 바꾸지 않았다. 이번 완료 단위는 HH_ON01_STATIC_FT03_LCS_KS_V1의 native rate/별도 사건/typed FT03 RHS/주어진 BE endpoint residual이다. 실제 시간 적분기는 아직 연결하지 않았다.

## 이번 결과

25개 native tests는 컴파일 가능한 미구현 인터페이스에서 25개 의도된 RED 실패 후 모두 GREEN이었다. 신규 96개 상태에서 OFF의 모든 FT03 field가 bitwise 동일하고, 두 provider의 ON 192개 endpoint/RHS 반환을 얻었다. ON 중144개는 nonzero HH,48개는 완전이온화 exact zero다. 직접 regime6개를 더해 native stdout198개 JSONL이다. 독립 mpmath100의3282개 scalar 대조는 실패0, 최대차1.0360796614159013e-15, 고정 상대허용오차3e-12다. 열+binding 상쇄 잔차0. Probe는1process이며 endpoint probe의 old==new는 residual assembly 검사이지 root/accepted step/history가 아니다.

선택 창은35000..60000K, static H=0, nH=1e-4/nHe=8.3e-6cm^-3의 유한점 연구, 공통온도 등방 Maxwellian reference다. 이 창에서의 실제 원자율 정확도는 미확립이며 두 곡선은 결정론적 모형 시나리오이지 error band가 아니다. 3000K raw floor는 호출하거나 smoothing하지 않는다. helper의 zero/extreme-density 시험은 물리 domain 추가 승인이 아니다.

식은 q=nH(1-h)^2*k,R=nH*q,fHH=(q,0,0,-chi*R,0,0,0). 추가1/2와ne나눗셈이 없다. chi는 실제 consumer binding threshold다. 기존 electron-CI/RR/DR/PI/escape counter는 보존한다. Off는 HH rate/guard를 적용하지 않으며 baseline bitwise 반환이다. 이는 local adapter 계약이지 전체S0 no-load/no-callback admission은 아니다.

50000K에서 LCS/KS=100.4702058이다. h=.9,HeII=.3,HeIII=.6에서 HH/electronCI는 각각3.4988106828e-5와3.4824360665e-7이다. 순수H의 HH=eCI 경계 h*=k/(k+beta)는3.5832471183e-4와3.5677430212e-6이다. 거의중성에서 중요도가 달라지므로 raw k비교만으로 negligible을 결정하지 않는다. 이 값은 순간 충돌채널 비교이지 총net source/history오차/관측량 영향이 아니다. 이론 유도와 온도별 표는ZIP THEORY/RESULT에 있다.

## 정확한 입력과 전달

HH parent0d80ff00880569dca9db2e19d0719ad316165eef, REI pinned source7c5469101f8d6ef027c8c3119cc5c053e15ba1d9. 현FT03 source blob370fd2fa60521f2dc121ee81c7d24013a3b0d1e5와원본6module을대조했다. fullcheckout대신 byte검증된source cache와공통error정의 excerpt를조립한minimalcrate를실행했다. 원REI production source를수정하지않았고wholecrate검증은아니다. 게시직전8e8ea0c664e2ba2f2f8560e0c64266d206fbd50f는FLRW06문서8개만추가, 관련science source변경없음. 해당외부실행재검증0.

전체패키지 WU088_HH_ON01_NATIVE_ACTIVATION_20261005_v1.zip,169605bytes,68entries/67payloadfiles,SHA256902805bd31d65967393a5e2535218e817893f5c4a6a5f9712e11b7133a1da476.
Drive1pVFFEkSP_cIfUJRyxa76SItJChjOMLia(parent1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM),Dropbox id:BSpOijBcT10AAAAAADyuog, /BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/WU088_HH_ON01_NATIVE_ACTIVATION_20261005_v1.zip. 양쪽create-only저장ACK/ID/size확인,R1,새output fullremote restore=false.

ZIP에는 전체REPORT/THEORY/ACTIVATION_CONTRACT/SOURCE_BINDING/원본module/driver/oracle/실제RED-GREEN/실행로그/DAG가 있다. Git의 src/hh_optin.rs와tests/hh_tests.rs는ZIP과byte동일하지만Git의이폴더만으로컴파일되지는않는다. 원vendor와root는ZIP에서받는다. research/run_scoped.py는new-directory재현지원자이며이번에는help/syntax만검증했다. 실제 최초실행은EXECUTION_RECEIPT의직접rustc/probe/comparator명령을따랐다. 지원자의end-to-end실행을추가주장하지않는다.

## 다음 단위 HH-ON02

이미 연구활성화는명시적으로승인됐다. 다시WAIT_OPT_IN으로되돌리지않는다. 다음은actualFT03 opt-instepper에서H생성/소멸 update,열update,최종residual,HHcounter를동일provider와동일endpoint로연결한다. frozenbaseline을유지하면서별도모듈/선택형adapter로작성한다. H ionizationfrequency에 nH*(1-h_guess)*k(T_guess)를별도로더하면fixedpointsource는q다. ne로rate를위장하거나 기존constant-rate thermalupdate뒤에사후HH를더하지않는다. full/half1/half2모두일관되고수락사건은half1+half2다.

다음검증은변경된stepper에한정해OFF기준동일성,독립실제결합reference와refinement,열/핵수/전자/event회계,domain거절과rollback을실행전고정한새bounded계약으로수행한다. 이번ON01은HH-timeintegration/F04-F05 ONcertificate/F09pairedcosmology가아니다. 원F1B/C/D와FLRW06/원자suite는그대로재실행하지않는다.

상태 HH_research=ACTIVE, HH_F2=NATIVE_REFERENCE_RATE_RHS_RESIDUAL_READY__ACTUAL_STEPPER_NOT_CONNECTED. physical/production=false. legacy24/289,265unbounded,epsilon_C/Rnull,B22OPEN,consumedscopes와원DB를유지한다. 같은HHbranchappend-only/nonforce,기존Drive/Dropboxcreate-only,REIF09singleowner를유지한다.
