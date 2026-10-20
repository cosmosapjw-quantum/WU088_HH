# NCP / Codex 인계 — PHYS71 완료 결과를 재사용

```text
WU088_HH의 PHYS71 결과를 복원·검증하고, 동일 완료본이 없는 준비된 NCP 요청만 이어서 실행하라.
Repository: https://github.com/cosmosapjw-quantum/WU088_HH
Branch: research/hh-phys71-third-born-20261020
실제 parent: PR120 HEAD31745376ca751e7c925b3b1453ef292436cd30e8.
최종 실제 source commit/metadata HEAD/PR와 ZIP SHA는 PHYS71_DELIVERY_20261020.json에서 읽어라.
예정된 push나 업로드를 완료라고 쓰지 마라. main은 merge하지 않는다.

먼저 최신 GitHub/관련 backup/실제 host process·job·result를 확인한다.
같은 request/source/seed/engine 완료본은 읽기 검증해 재사용하고 실행 중이면 관찰한다.
접근 불가한 다른 대화는 BLOCKED_CONTEXT_ACCESS, host는 UNKNOWN으로 남긴다.

PHYS71은 새로 실행할 D3 요청이 아니다. 실제 76개 패널 완료와
별도 analytic correction이 독립 검증됐다. 초기 목표 미달 pilot1개를 포함해
이 단위의 총 새 panel 호출은77이며 accepted campaign은76개다.
과거 완료 PHYS64~70 scientific campaign 재실행0, NCP 제출0이다.

먼저 DELIVERY, REPORT_KO.md, theory/PROOF.md, theory/ANGULAR_ERROR_STABILITY.md,
ANALYTIC_BOUND_CORRECTION.json, DISPLAY_RESULT.json, EXECUTION_LEDGER.json,
NEXT_DAG.json, ncp_delivery/README_KO.md와 publication 영수증을 읽어라.

완료 결과 D3(21,20),m0=Z'''(0)/6:
(2.14300135468641834333042543662+1.71865149630238869433259719024i)e-71 a0^-1,
표시 중심 기준 절대 오차 <=7.121295358370e-79, 고정 목표1e-78 PASS.
all-angular/all-radial, 단일3차계수의 결과다.
최종ALL_ANGULAR_CERTIFICATE.json SHA
f75d082e1966dd61a326c37b6ff14e8f330e010341a59a88eb4ca8d4734e6173.
원래수치CERTIFICATE.json SHA8d0d3a45196c89cecbecae70b59b0b93b72bae5ca600e24bcc3864ffab0c012f는
numerical evidence로 보존하되 analytic aggregate는 REJECTED_RADIAL_INWARD_ROUNDING이다.
요약1.484322e-79를상한으로쓰지말라. PR115의엄밀upward endpoint1.48432231489e-79를사용한다.
교정은원래76개패널을재사용한정확한후처리이며추가물리적분0이다.

capsule루트에서다음표준Python검증을실행한다:
python3 -S -B research/hh_phys71_20261020/verification/verify_saved_d3.py --root . --campaign research/hh_phys71_20261020/d3/run_l36_t65_stable_errors --display research/hh_phys71_20261020/DISPLAY_RESULT.json
이검증은새Coulomb/적분0,쓰기0이다. 복원된payload를다시생산하지마라.
현재수치campaign의radial상수는교정됐으므로원래producerfingerprint와다르다.
원래producer소스snapshot을보존하며guard를해제해수치CLI를강제resume하지마라.
완료corrected결과재사용은portableverifier또는scripts/phys71_finalize.py가담당한다.

별도 PHYS70 optimized L64는 완성된REQUEST_L64.json/runner가 있다.
먼저실제host와backup에같은완료/진행본이없는지확인하라.
없을때만전체repo또는PHYS70_NCP_READY capsule에서현지compile·작은환경수정·실행한다.
L64,m0,21/20,T65,nodes128,rtol1e-10,atol1e-12,max_step.25,block_simd.
solver설계를다시하지말라. 기존seed우선,없을때만make-seed.
Rust1.94.1/Cargo.lock/pinnedVigilODE를유지하며구형glibc에서는source를빌드한다.
구체명령은ncp_delivery/README_KO.md에완성되어있다.

물리보호: atomicB27,k7/10,E49/200Hartree,shift.7,
h=-Delta/2-1/r-(1+1/d)exp(-2d),d=abs(x-.7zhat),H+=G+iF_C,Z=+u'u^-1.
eta=Fy,xi=Fy-phi,eta_C=-10/7을구분. 원본NPZ SHA
f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d. HH_R10=OFF.
PHYS63질적존재와PHYS69D2는완료유지.
all-angularD3는완료지만4차이상/λ=1전체remainder,source-drivenxi,
원점/incomingadjoint,sigma(E),Maxwelliank_HH(T)는OPEN이다.
과거완료PHYS64NCP20,PHYS66pilot/smoke,PHYS67certs,PHYS68L28,
PHYS69band/native,PHYS70성능31개,PHYS71완료D3를반복하지마라.
PHYS70이전Driveupload는UNKNOWN_UNRESOLVED라서맹목재시도하지마라.
실제요청/결과/source/compiler/command로그와SHA를보존해반환하고,
유도/코드/검증/실행/게시/백업/DAG를별도기록하라.
```
