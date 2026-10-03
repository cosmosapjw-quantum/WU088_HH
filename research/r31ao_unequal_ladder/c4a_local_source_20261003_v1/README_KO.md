# WU088_HH C4A: 국소 source와 열 장부

판정: C4A_CORRELATED_LOCAL_SOURCE_AND_THERMAL_LEDGER_VERIFIED__PHYSICAL_PROVIDER_AND_TIME_UPDATE_PENDING.

이 Git 디렉터리는 exact C++ reference와51개 native 검사(8 RED/GREEN+43 regression)다. 전체66개 검사, JSON CLI,22개 source pins, 실제 HE T4 코드와 제조계 교차검산, 원 실행로그,73-table DB와SQL은 DELIVERY_INDEX.json의 전체 ZIP에 있다. Git subset만으로 전체66개를 재현했다고 하지 않는다.

상태 순서는(H0,Hstar,Hplus,Hminus,HeI,HeII,HeIII,e_th,e_nt)다. Hstar는 선택된 HH excitation label이며 모든 H 여기상태를 뜻하지 않는다. HE16 registry의HI는 명시적인 ground bookkeeping으로 lift했다. 실제 excited-population rate를 승인하지 않는다.

S=sum_alpha nu_alpha R_alpha에서 동일 사건의 rate interval을 모든 종과 에너지에 공유한다. 보존량은 먼저 w.dot(nu)를 수축하여 계산하므로 exact0이다. 독립 marginal interval의 단순합을 conservation failure로 오해하지 않는다.

Hminus를 지운6성분 mapping L에 대해 bH6 L S=-S_Hminus, charge6 L S=+S_Hminus다. 기존 Hminus state가0이어도 신규source가 비영이면 bare export를 거절한다. Extended export는 Hminus/Hstar/e_th/e_nt의 state와source를 보존한다.

같은 단원자 thermal bath에서 n_part=n_H+n_He+n_e_th, u=3 kB n_part T/2다. Tprime=2 Qth/(3 kB n_part)-T S_part/n_part를 같은 사건 계수로 조립한다. 비열적 전자를 thermal count에 더하지 않는다. HH ion-pair free-electron increment는0이다.

Homogeneous Bianchi I shared flow에서 A=3H+gamma_dot/gamma, n_dot=S/gamma-A n, u_dot=Qth/gamma-A(u+p), T_dot=Tprime/gamma-2AT/3이다. 다른Bianchi류, 비공동nonthermal current, fast-ion bath, finite-step positivity 또는 dynamical tilt closure를 승인하지 않는다.

에너지는 thermal/chemical/excitation/fast_e/fast_ion/bulk/radiation/external signed gain이며 chemical은 같은 모델의nu로 유도한다. C3A external work와 external reservoir gain의 부호는 반대다. Missing moments, photons,rate는0이 아니다. RR-total+DR, 같은 semantic owner, 바뀐snapshot/energy values는 거절한다. 실제14개 baseline rate 정의는 여전히 미확보다.

Peer: BASS_HE EOR_T4 HEAD218e646d3dd206a7a3a0d8a5a6f3ab0598aa5a4c의 조건부 소스/전자/에너지 장부만 교차 사용했다. 새NR_CX/EI_HI/R_CX 제조사례에서 coarse source=(-4,4,0,2,-2,2), thermal e=-2,fast e=4,energy8=(-6,-20,0,20,0,0,6,0)이 일치했다. Peer90개suite는 재실행하지 않았다. BASS_CR GitR4AG0d7bdbe76dc35d38668d750e6312919cecb09144 뒤 LibraryR4AH는 실제memory preflight BLOCKED이며 새로운 물리certificate가 아니다. Peer repo mutation은0이다.

실제 검증:GCC14.2.0,Boost1.83,C++20. 총66 PASS,UBSan43반복 진단0. 과거C3B/HE/CR suite와 HH적분/전파/physical rate/NCP 실행은0이다. DB67개원테이블/schema/행과원bytes를보존해73개,integrity ok,FK0,localSQLrestore논리해시일치다. Exact source algebra는 actual input/state uncertainty나 물리정확도 인증이 아니다.

```sh
g++ -std=c++20 -O1 -fno-fast-math -Wall -Wextra -Werror -pedantic tests/red_green.cpp -o /tmp/c4a_rg
/tmp/c4a_rg
g++ -std=c++20 -O1 -fno-fast-math -Wall -Wextra -Werror -pedantic tests/reference_tests.cpp -o /tmp/c4a_ref
/tmp/c4a_ref
```

다음:C4B_CONSERVATIVE_EVENT_EXTENT_AND_RESERVOIR_UPDATE. x_alpha=integral R_alpha d tau의 동일extent로 n_new=n_old+N x와 reservoir를 갱신하고 유한step positivity/잔고/once-only를 검사한다. 현재 tangent-cone 검사나 fixed-k gradient를 완성된stiff integrator/fullJacobian으로 부르지 않는다.

보존:20/289,missing269unbounded,epsilon_C/R=null,B22OPEN,R31AKfrozen,z0.75holdout,NCP6cell미소비,scientific/production/independent_science_review=false. Samebranch additive only. UPLOAD_VERIFIED와RESTORE_VERIFIED를구별한다.
