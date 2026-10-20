# 새 대화에서 이어갈 prompt — PHYS71 이후

```text
$physmath-research-loop를 사용해 WU088_HH 연구를 이어가자.
먼저 다른대화/branch/GitHub/관련backup에서 새실행결과를 확인하고 완료된계산은 재사용하라.
실제유도·코드·검증·물리실행·게시·백업·DAG를분리하라. HH_R10=OFF.
문서/감사만반복하지말고 다음고정범위의실제수학·계산·코드를산출하고,
필요한코드는이곳에서완성해push하여NCP에는compile/작은환경수정/실행만남겨라.

Repository: https://github.com/cosmosapjw-quantum/WU088_HH
PHYS71branch: research/hh-phys71-third-born-20261020
실제parent는PR120HEAD31745376ca751e7c925b3b1453ef292436cd30e8이다.
현재sourcecommit,metadataHEAD,PR와실제backupACK는최종PHYS71_DELIVERY_20261020.json에서확인하라.
이source내부handoff는미래commit을예측하지않는다. 외부최종handoff에실제값이추가된다.

자동회수대상:
WU088_HH_PHYS71_SOURCE_AND_EVIDENCE_20261020.zip
WU088_HH_PHYS71_NCP_READY_20261020.zip
WU088_HH_PHYS71_METADATA_20261020.zip
PHYS71_DELIVERY_20261020.json
WU088_HH_PHYS71_SHA256SUMS
PHYS71_NEW_THREAD_HANDOFF_20261020.md
접근불가하면BLOCKED_ARTIFACT_ACCESS로표시하고가짜복원/실행을하지마라.

읽기순서: 최종DELIVERY→REPORT_KO.md→theory/PROOF.md→ANGULAR_D3.md→
ANGULAR_ERROR_STABILITY.md→ANALYTIC_BOUND_CORRECTION.json→DISPLAY_RESULT.json→
최종독립검토/EXECUTION_LEDGER/NEXT_DAG→CODEX_HANDOFF_PROMPT.md.

PHYS71실제완료:
1. D3=Z'''(0)/6의bilinear forward-response identity와exactinfiniteangularconvolution.
2. L36,T65,76panels,N80/384bit. 기존PHYS68/69 qpayload152개를그대로사용했다.
   q/CoulombTaylor재구성은새downstream평가로세고,과거q/D2적분은0회재실행했다.
3. 73angularmoments와원래직교기저의weightedcoefficienterrorbound.
   첫pilot의1.4690349306e-72반경을같은중심/같은carry/같은정밀도에서
   5.5548284227e-86으로줄였다. 2.644609e13은인증구간폭개선이며속도배율이아니다.
4. 총새panel호출77회=목표미달초기pilot1+완성수정campaign76.
   수정pilot1을재사용해나머지75만계산했다. NCP제출0,실제hostUNKNOWN.
5. 서로다른54개테스트PASS를별도표적실행으로확인했다. 단일54개통합suite를다시돌린것은아니다.
6. 최종독립감사가radial요약소수의inwardrounding을발견했다.
   1.484322e-79를엄밀상한으로쓰지말라. PR115의upward1.48432231489e-79로
   analytic후처리만교정했다. 76패널/원래producerfingerprint는불변이고추가물리적분0이다.
   원래rawCERTIFICATE의analyticaggregate는거부상태로보존한다.

최종all-angular/all-radial D3(21,20),m0:
(2.14300135468641834333042543662+1.71865149630238869433259719024i)e-71 a0^-1,
표시중심절대오차<=7.121295358370e-79,고정목표1e-78PASS.
수치오차5.73125795490702815268701e-86,
radial1.48432231489e-79,excludedangular5.63697247035361181066503e-79.
최종ALL_ANGULAR_CERTIFICATE.json SHA
f75d082e1966dd61a326c37b6ff14e8f330e010341a59a88eb4ca8d4734e6173.
원래수치CERTIFICATE SHA8d0d3a45196c89cecbecae70b59b0b93b72bae5ca600e24bcc3864ffab0c012f.
원래producercampaign.py snapshot과첫감사실패를지우지마라.

새portable verification/verify_saved_d3.py는stdlib만으로hash/carry/exactbudget/
independentangularNewtonsum/radialpositiveexpseries/printing을검사한다.
새Coulomb/적분/쓰기0이다. sourceclone만있고oldarchive가없으면capsule에서정확한
SHA의low/bandZIP을회수하라. 완료PHYS71을새로적분하지마라.
현재campaign상수는교정되어원래enginefingerprint와다르다.
완료결과는portableverifier또는scripts/phys71_finalize.py로재사용하라.
producerruntime은Python3.12.14/python-flint0.8.0/FLINT3.3.1이나읽기검증은다른reader를구분해허용한다.

보호물리: atomicB27,k7/10,E49/200Hartree,shift.7,
h=-Delta/2-1/r-(1+1/d)exp(-2d),d=abs(x-.7zhat),H+=G+iF_C,Z=+u'u^-1.
eta=Fy,xi=Fy-phi,eta_C=-10/7을구분. NPZ SHA
f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d.
PHYS63실제all-angularLAP/Poisson/DtN질적존재는ESTABLISHED_REUSED다.
PHYS69all-angularD2(21,20),m0완료결과:
(7.01774363281637372857673+3.20016322230539545153550i)e-48 a0^-1,
displayerror<=1.279825889920e-64. 완료의무를다시OPEN으로돌리지마라.

기존PHYS70_ALL_ANGULAR_D3_AND_HIGHER_REMAINDER식별자를보존한다.
상태는PARTIAL_D3_COMPLETE_HIGHER_REMAINDER_OPEN이다.
다음고정연구의무는실제outgoingCoulombDirichletGreenkernel의radial/angular가중
operatorbound를통해4차이상Bornremainder를합산하는것이다.
무한j에서다항식으로자라는C_j를Gamma64로치환하지마라.
충분조건실패를strongno-go로오인하지마라. 현재D3완료는λ=1전체응답인증이아니다.
원래source-drivenxi,원점/incomingadjoint,sigma(E),Maxwelliank_HH(T)는별도OPEN이다.

PHYS64NCP20,PHYS66oldpilot/smoke,PHYS67certs,PHYS68L28/oldRust,
PHYS69band/native,PHYS70완료성능31개,PHYS71완료D3를반복하지마라.
PHYS66longtail6/PHYS68validatedL64/PHYS69nativeL64/PHYS70optimizedL64는
새완료본이없으면READY,실제hostUNKNOWN이다. 완성된PHYS70L64runner로NCP실행가능하며
VigilODEpinnedkernel/RustSIMD/Rayon을새로설계할필요가없다.
PHYS66최종993317b1...ZIP의정확한버전접근불가와
앞선PHYS70DriveuploadUNKNOWN_UNRESOLVED를다른복원/ACK로덮어쓰지마라.
기존승인범위의additivedraftPRpush와create-onlybackup을끝까지수행하고실제ACK를기록하라.
```
