# PHYS90 최종 과학 보고 — 공분산 표시 셀과 공통 소비자 경계

## 판정

유한 자식 `COVARIANCE_FORMATTING_CELL_AND_MATCHED_CONSUMER_ENVELOPE`의 이론·구현·정확한 유한 계산을 **PASS_SCOPED_CONDITIONAL_COVARIANCE_CELL_AND_CONSUMER_ENVELOPE**로 수용한다. 선택 물리 부모 `NUCLEAR_BARE_KERNEL_SOURCE_AND_CONSUMER_CONTRACT`는 **PARTIAL_INPUT_DEPENDENCIES**다.

이 보고서는 S2 시점 **R1–R9/C1–C9=18/20** 불변 snapshot이다. R10/C10의 최종 게시·백업·인계 근거는 이후 외부 MAIN/TERMINAL, 중앙과 PR147 actual readback으로 연결한다. 전역 물리 완료율은 null이다.

## 1. 실제153군 자료에서 새로 얻은 정밀도 조건

PHYS89의 SOURCE_TABLE 및 TOKEN_ROUNDING을 원 SHA로 재사용했다. ENDF를 다시 해독하거나 기존 eigh·rate·exact witness 실행을 반복하지 않았다. F는 원 표시 fractional covariance, H는 token-specific halfULP다. t≥0에서 닫힌 대칭 셀은

\[
\mathcal B_t=\{F+\Delta:\Delta=\Delta^T,\ |\Delta_{ij}|\le tH_{ij}\}.
\]

t=1은 **조건부 nearest-formatting 모델**이다. 실제 formatter 보증과 물리 오차는 아직 공급되지 않았다.

| 검사 | 실제 결과 |
|---|---:|
| singleton |153|
| 모든 서로 다른 pair |11628|
| t=0 failed singleton / pair |0 /74|
| t=1 failed singleton / pair |0 /0|
| 저장된 exact checkpoints |42|
| exact dyadic bisection |40|
| 독립 reference |PASS_EXACT|

모든 2×2 조건이 호환되는 최소 공통 반경은

\[
\frac{34406736621}{68719476736}
<t_{\rm pair}\le
\frac{550507785937}{1099511627776},
\qquad \Delta t=2^{-40}.
\]

십진 표시로는

\[
0.5006839145935373<t_{\rm pair}\le0.5006839145944469,
\]

표시한 십진 양끝은 바깥쪽으로 반올림했다. 정확한 유리수 구간의 폭은 약9.094947017729282×10^-13이다. 판단에는 부동소수점을 사용하지 않았다. 하단은 zero-based pair(10,16)의 실패로 인증되며 그 셀에서 가능한 최대 determinant는

\[
-\frac{23113}{549755813888000000000000000000}<0.
\]

상단에서는 모든153singleton/11628pair가 통과한다. 따라서 t_pair의 bracket이 닫혔다. **t=1의 전체153×153 PSD 존재와 전체 PSD threshold는 UNRESOLVED**다.

각 pair의 정확한 조건은 a=F_ii+tH_ii,b=F_jj+tH_jj,c=max(|F_ij|−tH_ij,0)에 대해 a,b≥0,c²≤ab이다. upperdiagonal과 minimum-absoluteoff를 취하는 구성은 해당 block의 존재를 증명한다. 실제source수정행렬을발행하지않았다.

기존0,10block에 새롭게 유도한 threshold는 t*=2a/(4a−d)=8557144/17114287이다. 기존 표시행렬 반례를 재실행한 결과로 집계하지 않는다. 새 전체pair bracket은 그 단일block보다 강한 정밀도 의무를준다.

## 2. 대칭 원소 공유에서 얻는 정확한 소비자 경계

고정 u,v에 대해

\[
\sup_{\Delta\in\mathcal B_t-F}|u^T\Delta v|
=t\left[\sum_i H_{ii}|u_iv_i|+
\sum_{i<j}H_{ij}|u_iv_j+u_jv_i|\right].
\]

독립 upperentry별로 계수부호를선택하면 양쪽endpoint를실제로달성하므로 전체box의sharpbound다. PSD부분집합에도유효한outerbound이며그부분집합의sharpness는별도다. 서로다른consumerentry의endpoint를동시에실현할수있다는뜻은아니다.

같은source를받는 K=LCL^T에서 각entry에이식을적용한다. q^TL=0이면 Kq=0와q^TKq=0이모든공통C에서정확히성립한다. PHYS89 normalizedmoment의 B=(a−Mr)/Z, exactratio/remainder 및 clock·energyownership은그대로재사용하고새cellbound를고정B에적용한다.

독립fixture F=4I2,H=ones,t=1,u=(1,1),v=(1,−1)은전체box가SPD다. Sharedoffdiagonal이상쇄돼crossradius2를얻으며절댓값을먼저취한bound4보다작다. 각variance의개별max는12지만합의max는20으로(12,12)는공동달성되지않는다. L의세번째row−u−v를추가해8vertices모두에서공통source보존을검증했다. Reference는9supportentries의양끝을정확히대조했다.

두번째manufactured3×3fixture는모든pair가통과해도w=(1,1,1)에대한box상단quadratic이−21/10인사례다. 이는pairpass를전체PSDpass로승격시키는오류를구별한다. Actual153group자료에는이fixture의전역결론을옮기지않는다.

기존w=e0−e10의중심−10^-10을재사용한새조건부box범위는[−3×10^-10,10^-10]이다. 중심값은완료된parent근거이며새결과는반경2×10^-10이다. 이구간만으로fullPSD나physicalCI를판정하지않는다.

## 3. 원자료 계보를 좁힌 새 근거

[Hoblit NNDC2011](https://www.nndc.bnl.gov/meetings/nuclear-data-week-2011/Thursday/CSEWG/hoblit-71.pdf)은nativeCOMMARA MF33의직접도입을설명한다. 이번실제복원한원VII.1H1neutronmember는54513bytes/SHA5bc558ac458face9cea2a1afba7391529df7c136415f1cb5babfab2ced4c97ce,MF33/MT102 NE14=13groups다. 공개33group처리제품과현재NE154=153groups를동일객체로간주하지않는다.

[공식VII.1errata](https://www.nndc.bnl.gov/endf-b7.1/errata.html)의2013SVN610은H1scatteringcovariance교체를기록한다. [공식VIII.1changelog](https://www.nndc.bnl.gov/endf-releases/releases/B-VIII.1/neutrons/CHANGELOG.md) 원bytes122162/SHA4a28ba9249254fc02ab173105103f9d07eb60bf40846cf2112272bc62ddc05cf에는2016Halehighfidelity교체,2017nominalstandards교체와그때의MF33미갱신,이후covariancesadded가별개로기록돼있다. 어느변경이currentMT102의153group객체를생성했는지는OPEN이다.

따라서원precision요청은“33→153변환”을전제하지않고정확한currentMT102계보,nominal/parameter/groupidentity,Jacobian/normalization,formatter오차또는approvedcorrection을요구한다. GNDSXML,JENDL상속자료,30groupNJOY진단은이입력을대체하지않는다. Originalmassdeck/electron-targetstate/differentialkernel/tail과namedthermal/fast/radiationACK도여전히필요하다.

원VII.1neutronZIP은range2로member를복원했으며wholearchiveGET0이다. 두range의weakETag/LastModified차이를보존했고memberCRC를전체archive강한identity로확대하지않았다. 상세는intake/sources/의원응답과ledger에있다.

## 4. 구현·독립검토·실행

Scientific identity:
`a7107870ad5a66e3bb602115f1068ca7366444b42c539e1a6b4b83da2037513a`.

Primary는공통정수scale,reference는pair별독립정수scale와Fractionfixture를사용했다. Productionkernel을reference가import하지않는다. Frozen7files/input2가불변이다. 15guard가통과했다. R6독립유도와C9독립검토는각각reviews/에원문과identity를보존한다.

새Wolfram은evaluator1회로9scalar잔차0,all_zero=true,positive-offbranch=true를기록했다. Context1회는별도다. PHYS88의all_zero=False/별도양의branch증명및PHYS89중단전raw미복구기록은변경하지않는다. Symboliclineage는8→9이며예전허용량을reset하지않았다.

첫wrapper는child0에서ownlease를관측하지못해WAIT75로종료했다. DefaultPIDnamespace의os.getpid()와/proc가다른namespace였고,root의readonly비교와독립진단으로확인했다. HostPID실행경계에서같은frozenwrapper/원sharedlease를사용해primary1/reference1이성공했다. Gatepatch/osproxy/새lockdomain/다른process종료는0이다.

| 비용 범위 | 실제값 |
|---|---:|
| 성공scientificchildren |2|
| 총wrapperattempts |3: prelaunchchild0 WAIT1 + childsuccess2|
| childCPU합 |2.9139999999999997s|
| childlaunchwall합 |2.917763527002535s|
| wrappercoordinatorCPU합 |0.07425899999999999s|
| wrapperinclusivewall합 |3.232636796994484s|
| metadataresumeCPU합 |0.063894s|
| metadataresumewall합 |0.06465108200791292s|

Wrapperinclusivewall은childwall을포함하므로더해중복집계하지않는다. Readonlyresume는각1회SKIP이며scientificimports/callbacks/writes0,9files98380bytes의SHA/size가불변이다. Sourceparse/eigh/ODE/integral/benchmark/nuclearactivation/faststopping은모두0이다. PHYS87–90의알려진childCPU부분합은15.01791s이며전체역사총비용이아니다. 전체역사·원격CPU/금액/잔여global은null이다.

## 5. 그림

새primary가PNG51634bytes와PDF16603bytes를한번생성했다. PNG는root와독립reviewer가직접읽어축과라벨을확인했다. Stepsegment는42exactcheckpoints를잇는표시용선이다. 연속t의실패개수함수를증명한그림으로쓰지않는다. 원PHYS88의2PNG2PDFbytes와shortening원인NOT_ESTABLISHED/artifactchildexit1/원bytes복구이력은parentancestry와wholeparentarchive로보존한다.

## 6. 조사·게시·보존

Fresh51repos2254branchrefs65pages,관련6repo최근5PR씩30bodies,HHDropbox529/Drive561항목,최근Library311items/2pages를조사했다. 비공개대화전체·모든branchsource·Drive1000cap밖전수열람을주장하지않는다. 중앙은초기14976이후CRdelivery-only a28ba343으로이동했고과학입력은불변이다. 최신HE/BASS/REC/CR/HIclaim과provider한계를각owner근거로보존한다.

S0head19509c0f7d275a70326184e009b09d3836e253d4/tree54495cc562089f1cb7677c05c7049046a47ab3ce는10/20, S1head298aebe3889011d8a7f48a454cf18d1a98c8f54c/tree e67be32177ec3d64d91b8ad695f0a7fa0676ef4d는11/20이다. 둘다expectedSHA/nonforceactualref와dualACK/별도metadata를확인했고stagewholeGET0이다. S0포장시promisorblob의sandboxnetwork실패1과그뒤missingfile업로드입구실패2는science0metadata이력으로보존했다. 원treeblobID와localbytes일치후객체를채워포장했다.

최종S2/FINAL과전체archive복원은delivery/및외부MAIN/TERMINAL에actual근거를남긴다. DraftPR147,basePHYS89FINAL,mainmerge0. 중앙원40contracts/planstatus/dependencies,7authorities17edges,다른39nodes,HH기존25081B및최초11893Bprefix를보존한다.

## 7. 다음 단일 선택

선택부모는그대로다. 다음원자료의무는currentMT102의nominal-bound원precision및실제formatter/approvedcorrection을얻어153group표현과결속하는것이다. 조건부셀의전역PSD문제는exactGram/LDL^Tprimal또는exactPSDDualY certificate로닫을수있다. 자료공급과전역셀certificate는서로의물리적승인을대신하지않는다.

Baremass/electron-targetstate/differentialkernel/fullsupporttailB0/BA와namedthermal/fast/radiationmeasure·clock·reference-density·ownerACK를물리단계에서먼저닫은뒤새affectedidentity의코드를동결한다. 기존REI-L2는beta채널이며capture확장PROPOSED_UNIMPLEMENTED, BASSnuclearconsumerNOT_BOUND다.

HH_R10=OFF,productionNOT_ISSUED,non-tiltedLRS(-+++),gaspi0/DMpi_m별도,commonframesignedtensor합후norm,Frobenius=sqrt2×halfcontraction을유지한다. Trajectory분해는species-off인과실험이아니고sampledresidual은continuumcertificate가아니다.
