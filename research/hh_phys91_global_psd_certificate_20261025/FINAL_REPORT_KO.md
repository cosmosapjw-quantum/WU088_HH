# PHYS91 최종 과학 보고서 — 전체 PSD 거리 인증과 미결 B1

## 1. 판정

**PASS_SCOPED_EXACT_GLOBAL_PSD_DISTANCE_B1_UNRESOLVED.** 현재 source의 153×153 표시 covariance와 조건부 half-ULP cell에 대해 전체 PSD cone까지의 거리 상·하한을 정확한 유리수 인증서로 구성했고, 독립 reference가 선택된 두 인증서를 재현했다. **B1의 PSD 존재·부재는 여전히 미결**이다.

이 보고서는 R1–R9/C1–C9 완료 **18/20**의 불변 과학 snapshot이다. 이후 S2·FINAL 게시, 양쪽 최종 복원, 외부 MAIN/TERMINAL, 중앙 actual FINAL과 PR148 readback이 R10/C10을 별도로 결속한다. 18/20을 사후20/20으로 고치지 않는다. 전체 물리 목표 완료율은 **null**이다.

물리 부모 NUCLEAR_BARE_KERNEL_SOURCE_AND_CONSUMER_CONTRACT는 PARTIAL_INPUT_DEPENDENCIES다. HH_R10은 OFF, production admission은 NOT_ISSUED이며 실제 nuclear rates/fast-product stopping은 활성화하지 않았다.

## 2. 완료 baseline과 정확한 연구 identity

|항목|확정 값|
|---|---|
|PHYS90 FINAL parent|9d32d115c0b8c5d5b2ce3a66ebc4a7f277334fcc|
|PHYS90 FINAL tree|30e3a281d81e3fbb88d26f290579085475f54235|
|PHYS89 FINAL|480baabc73ebaaba735d285d969e79177f5545ed|
|PHYS88 FINAL|92dec7cdc1cf5afeff5bdff8d6234f7f1e3dbbd8|
|PHYS91 S0|4afb530bc02bc4d611bf421eccac6d6b1ba3606e|
|PHYS91 S1 code / 실제 실행 HEAD|c9eaf283c227157067d27cecd672033d795bbe68|
|S1 tree|4e2bd383ce1afecb0bf7669f70bd02340ca11629|
|Scientific identity|4b7e3ce80c6a96373e4f0f214d63c12738d2ab5f71b9f83bc01cfbaf5bb5c376|
|Contract SHA256|361826f7940542e05c1461bf879d43808007aad092c58579c762dacce8ca5a39|
|Theory SHA256|f2ae715cc01c7489ac5e7c7f687f1a765dbbe835fb892f8f7cf2a81cd68f0b30|

Branch는 research/hh-phys91-global-psd-20261025, Draft PR148이다. FINAL descendant만 사용하며 PHYS82의 최종 CRLF 복구와 이후 완료 ancestry를 보존한다. 단독 S2 checkout은 재개 기준이 아니다. 이 보고서의 enclosing S2/FINAL SHA는 외부 실제 게시 영수증에서 결속하며 self-hash를 만들지 않는다.

입력은 PHYS89 SOURCE_TABLE.json(960400B, SHA8be5263be692e63720acbf8c9ae5b1abad85bc55c8a641d8080b125979a4a7e7), TOKEN_ROUNDING.json(296009B, SHA0c7c335054b2408f3cf241fa7acd2ef42ad4243b644fbfd0f22199482546854a), PHYS90 PAIR_SCAN.json(18666B, SHA5ac976d506c34240f454b2bcd45dfa1787dc6035828ca35ce07e493253c75d33) 세 개다.

PHYS88 cross-section의153 native knots/152 cells와 이번 covariance의153 groups/154 boundaries는 다른 데이터 구조다. 두153을 동일 interpolation grid 또는 자동 nominal binding으로 해석하지 않는다. ENDF 원문 decode, raw F eigensolve, PHYS90 pair scan 및 과거 nominal integral은 재실행0이다.

## 3. 실제 이론 구성

대칭 rational 표시행렬 F와 양의 half-ULP H에 대해

\[
\mathcal B_t=\{C=C^T: |C_{ij}-F_{ij}|\le tH_{ij}\},\qquad
t_*=\min_{C\succeq0}\max_{i\le j}\frac{|C_{ij}-F_{ij}|}{H_{ij}}
\]

로 정의했다. 실제 H의 양성은 모든 entry에서 exact 검사했다. Trace pairing에서

\[
h_H(Y)=\sum_i H_{ii}|Y_{ii}|+2\sum_{i<j}H_{ij}|Y_{ij}|,\qquad
t_*=\max_{\substack{Y\succeq0\\h_H(Y)\le1}}-\operatorname{tr}(FY).
\]

충분히 큰 t와 C=λI≻0로 strict feasible point를 직접 구성한다. 유한 t sublevel의 compactness로 primal 최소를, bounded dual set으로 dual 최대를 얻는다. Weak duality와 Slater를 연결한 증명은 theory/GLOBAL_PSD_CERTIFICATE_KO.md에 있다. 일반 SDP duality를 새 정리라고 주장하지 않으며, 이번 새 성과는 frozen actual source에 대한 구체적 exact certificates다.

정수 factor V,W와 q=2^48로

\[
C=VV^T/q^2+\operatorname{diag}(D),\quad D_i\ge0,\qquad
Y=WW^T/q^2\succeq0
\]

를 구성했다. 전체11,781 upper entries에서 α=max|C−F|/H를 구하고, β=−tr(FY)/h_H(Y)를 exact 계산한다. 그러면 β≤t_*≤α다. Full Y를 합한 뒤 entrywise absolute support를 계산해야 하며 factor별 support 합으로 바꾸지 않는다.

Closed B1에서 α≤1은 존재 인증이고 β>1은 배제 인증이다. α=1은 포함되지만 β=1만으로 배제하지 않는다. PHYS90의 strict lower 34406736621/68719476736은 재사용하며, pair upper를 전체 PSD upper로 사용하지 않는다.

## 4. 실제153 결과

선택된 두 인증서는 다음 닫힌 구간을 보증한다.

\[
\boxed{
\frac{606934757065126340229833497971012560}
{1044859134592536248071098889705557947}
\le t_*\le
\frac{1210812737265140594067745}
{1208925819614629174706176}
}
\]

정확한 정수 나눗셈으로 바깥쪽 표시한 소수 구간은

\[
0.5808771124940327\le t_*\le 1.0015608216979872
\]

이다. 이 소수 표시는 원 유리수의 읽기 편한 표현이며 인증서 재계산이 아니다.

|선택 인증서|checkpoint|factor 열 수|확인한 내용|
|---|---:|---:|---|
|General PSD dual|4|88|정확한 trace/support와 closed lower β|
|Gram + nonnegative diagonal primal|13|65|전체11781개 α, 최대 성분은0-based(22,74)|

원 결과의 rank 필드는 factor 열 개수다. Quantized Gram의 exact rank나 padding 이후 최종 C의 rank를 별도로 판정하지 않았다. 원 필드와 bytes를 보존하며 문서 표현을 구분했다.

β<1<α이므로 B1은 OPEN이다. α가1에 가깝다는 시각적·수치적 관찰은 α≤1의 exact 조건을 충족하지 않는다. 이번 구간은 전역 최적값의 enclosure이지만 최적점 도달, 최적성 gap의 작음, source-approved covariance 복구를 주장하지 않는다. 고정된4096회 탐색에서 인증 조건을 얻지 못한 것은 이론적 불가능성 증명이 아니다.

## 5. 구현과 독립 검증

Dykstra 후보 탐색은 correlation-scaled PSD cone과 upper diagonal을 고정한 symmetric box를 번갈아 사용했다. ρ=255/256과1의 두 stage에서 각각2048회, 총4096회의 changed-candidate eigensolve를 수행했다. 초기 diagonal은 U=Fii+ρHii이므로 원 raw F의 spectrum 재실행이 아니다. Primal factor에는 forward scaling, dual에는 inverse scaling을 적용했다.

각256회마다 exact checkpoint를 남겨 총16개를 보존했다. Floating score는 후보 선택에만 쓰였으며 exact α/β가 인증된 bounds를 정한다. 각 checkpoint의 factor와 exact 평가를 create-only로 저장했다. 계약의 CPU soft stop에는 도달하지 않았고 정상적인 고정 projection cap으로 종료했다. 사후 반복 수·분모·허용오차 확대는0이다.

독립 reference는 production kernel/primary를 import하지 않는 별도 standard-library integer/Fraction 구현이다. 선택된 primal과 dual 각각11,781 entries, padding, witness, trace, support, endpoint openness 및 B1 상태가 exact 일치했다. 16개 모든 checkpoint의 hash·metadata·저장된 min/max 선택도 확인했다. 선택하지 않은 모든 factor를 독립 재계산한 것은 아니다.

Primary의17개 fixture/guard 항목과 reference의20개 Boolean 검사,16개 forest sign cases를 실제 수행했다. Zero-H, zero factor, 음의 padding, 비대칭·차원·비유한 token, input identity, 경계 α=1/β=1, exact contradiction과 공통 consumer map을 검사했다. Small fixture의 결론과 actual153 결과는 분리한다.

실제 primary --resume와 reference --resume를 각각1회 수행해 두 건 모두 SKIP_COMPLETE_READ_ONLY였다. 과학 import/callback/write는각0이다. Primary/reference 전체25files/9,110,118bytes의 SHA와 size가 전후 동일했다. Frozen8과 input3도 그대로다.

독립 R6는 완료 proof를 재사용했고 C9는 한 번의 review pass를 preexecution/actual outcome으로 나누어 종료했다. Blocking0, open finding0, code repair0이다. 자세한 근거는 reviews/C9_FINAL.json과 execution/EXECUTION_SUMMARY.json에 있다.

## 6. Wolfram과 general dual의 필요성

Wolfram 새 context1/evaluator1을 사용했다. Evaluator는55개 scalar residual이모두0, all_zero=True로 끝났다. 이는4×4 manufactured fixture와 Gram 항등식이며 actual153행렬을 Wolfram에서 다시 계산한 것이 아니다. Context 응답만을 증명으로 쓰지 않는다.

Fixture의 S²=2I, F=I+S, W=I−S, Y=WWᵀ=3I−2S에서 tr(FY)=−4, h_H(Y)=14/5, β=10/7, B1 signed upper=−6/5이다. Column별 support를 더하면54/5로 약해진다. 모든 rank-one separator가 실패한다는 명제는 signed-cycle negative-edge forest의 two-color 증명으로 닫았고, CAS/scalar 또는 유한 vector sampling으로 대체하지 않았다.

Symbolic lineage는9→10이다. PHYS88 실제2calls(exporter실패1+diagnostic1),18scalar zeros/all_zero=False 및 별도 positive-branch COM 증명은 역사대로 보존한다. 새 all_zero=True를 과거 실패 기록에 덮어쓰지 않는다.

## 7. 물리 source와 consumer에 미치는 영향

이번 conditional formatting cell에는 실제 nearest formatter 보증이 없다. 원 표시 F의 non-PSD 원인은 NOT_ESTABLISHED다. 인증한 C를 실제 source covariance로 채택하지 않았고 physical confidence interval도 발급하지 않았다.

실제 source가 C_phys의 identity·nominal binding·uncertainty convention을 공급하고 동일 linear map L을 승인하면 K=L C_phys Lᵀ는 PSD이며 aᵀL=0인 signed conservation row에서 aᵀK=0, Ka=0이다. 여기서 공유 covariance와 공유 map의 owner 계약이 필요하다. 이 작업의 manufactured consumer fixture는 actual ACK가 아니다.

다음 물리 입력은 여전히 필요하다.

|물리 계약|현재 상태|필요한 결속|
|---|---|---|
|Atomic→bare kernel|미공급|명시적 kernel/사건 measure, normalization, state mapping|
|Evaluator mass·electron·target state|미공급|같은 명목 source와 사건의 질량·상태·convention|
|Covariance 원정밀도·formatter|미공급|현재 MT102와 nominal의 승인된 연결, formatter 또는 source 승인 correction|
|Energy support/tail|미공급|소비자 measure에 맞는 support와 B0/BA tail bounds|
|Thermal/fast/radiation consumer|ACK null|이름·measure·clock·density·ownership·공통 conserved map|
|Physical finite-T supplier|PARTIAL|위 부모들을 실제 history/상태와 결합한 공급 계약|

PHYS88의 signed convention carrier를 heat나 실제 electron으로 사용하지 않는다. Same-event carrier와 fresh bare two-body event는 별도다. PHYS88 Qgap81.63eV=0.003700036867eV binding차+81.626299963133eV convention-residual차, 네 T의136.189–168.788ppm 조건부 비교를 재사용한다. 그 ppm을 실제 source CI나 coupled thermal/xe history bound로 승격하지 않는다.

## 8. 조사 범위와 병렬 결과

접근 가능한 최신 metadata snapshot은51repos/2264branch refs/65pages/51terminal collections, 관련6repo1144refs와최근5PR씩30rows다. GitHub73calls/errors0의 새로운 시점 조사다. 최초51/2261/65snapshot은 관측한 뒤 raw 일부가 손실된 상태로 구분했다. 모든 branch 내용·모든 private 대화·Drive1000cap 밖을 전수 읽었다고 주장하지 않는다.

Exa search2/fetch1(batch3URLs), SciSpace search2, web3 및 관련 대화검색1의 범위와 primary-source 채택 이유는 SURVEY_SYNTHESIS_KO.md와 intake/SOURCE_RETRIEVAL.json에 있다. Vandenberghe–Boyd SDP, Hladík의 existential/robust 구별, Rump의 verified definiteness 문헌을 참고하고 이번 Slater·Gram·support 증명을 직접 구성했다. BROND MF33MT2 elastic 수정이나 과거13/33group 자료를 현재153group MT102의 승인 correction으로 쓰지 않았다.

병렬 owner 결과는 다음 한계를 유지한다.

- REC136: local[Js,Ks] COMPLETE_SCOPED, same-source norm enclosure; H5 physical history error 값null, globalH7 OPEN. Dropbox wholePASS, Drive wholeNOT_RUN.
- BASS189: manufactured/frozen22rows/162gatesPASS. 실제 B3c history/receiver와 HH nuclear consumer NOT_BOUND. 양쪽ACK와remoteGET NOT_RUN을구분.
- HE101: scoped finite-M 결과, 실제process PASS/FAIL/FAIL 및19/20/C8 OPEN/reserve0. physical_provider=false, remoteGET NOT_RUN.
- CR105: atomic H1 ground spontaneous RR의scoped20/20. Library+Dropbox wholeGET/R3PASS, Drive UNKNOWN/terminalNOT_ATTEMPTED. np nuclear capture가 아니다.
- HI: 기존4368atoms의 massive stress와 새 순간 strain response를재사용. Actual history/density/clock/collision/stopping/photon feedback은OPEN. 190e의science57와b24a9d의delivery12를보존. C811669B Library+Dropbox ACK/local64restorePASS, wholeGET NOT_RUN; owner external D receipt를이intake에서읽지않았으므로조건부20/20와불변18/20을구분.

중앙 current b24a9daee54fc0860c4cf299c4ea5f2a977c0fd4의 canonical40contracts/planstatus/dependencies,7authorities,17edges, 다른39nodes, old19WU observations와HH30594/25081/11893prefix를보존한다. 실제 중앙 게시 직전에는 다시 actual parent를 읽는다. HE/LiCX, Li instrument/deconvolution/isotope/target-state/uncertainty, recombination-to-Z20, D_PI_RR matched moments, Li hardUV inner-shell, full geometry spectral backreaction의 병렬 OPEN은 그대로다.

## 9. 자원·실패·복구 이력

|새 PHYS91 측정|CPU s|Wall s|
|---|---:|---:|
|Primary1|13.679209|13.693714398999873|
|Reference1|0.571149|0.5727001010000095|
|과학 child 합계|14.250358|14.266414499999883|
|Coordinator 별도|0.05050599999999999|14.476745541000128 wrapper inclusive|
|Metadata resume2 별도|0.091248|0.09206515599998966|

Wrapper wall에는 child가 포함되므로 child wall과 다시 더하지 않는다. Original shared lease,1worker/thread, CPU0science/CPU8coordinator, reserve1.5GiB+job0.5GiB를 실제 적용했다. 두 child 모두성공, WAIT0, retry0, 타process종료0이다. 새primary/reference/Wolfram allowance는모두0, 과거완료allowance0, budget reset=false다. 알려진PHYS87–91 child CPU부분합은29.268268s이며 전체역사CPU가아니다. 전체역사·remote CPU·금액·전역잔여예산의미관측값은null이다.

S0게시 전 파일시스템 소실의 원인은 NOT_ESTABLISHED다. 그때새science0, S0commit/archive/ACK0이었다. ParentPHYS90 원ZIP/MAIN/TERMINAL을Dropbox각1GET/retry0으로복구하여CRC118/payload117/extract118PASS, nestedrestore0을확인했다. Contract/theory/R6와독립proof5files는원SHA로exact복구했다. 초기censusraw손실과새metadata수집을구분한다.

PHYS88 PDF shortening의원인NOT_ESTABLISHED·artifactchildexit1·정확한원bytes복구와원2PNG/2PDF를보존한다. PHYS88children4=success3+artifactfail1/CPU7.322937s/wall7.330995100001019s, metadataCPU0.0005106s도그대로다. PHYS89initialreferencefailure와PHYS90prelaunchWAITchild0은과거영수증에남겨재시도성공으로지우지않는다.

## 10. 게시·백업과 재개

S0와S1의actualGit/dualACK는 delivery/에있다. S0는353639B/SHAe607d7a8cbf8206538fc86860c9a66b0508aedf377c672fb8e6d8c9d00bc89f9이고 S1은410364B/SHA80e49f6c9d70607f0e0df79515646f3a8f65d357f9044e46b344dea1b4264e8c다. S0/S1/S2 stagewholeGET는0이며 최종wholeGET와구분한다.

최종ZIP은원PHYS90 wholearchive1개를opaque bytes로보존하고nestedrestore0을유지한다. 이후양쪽실제wholeGET/원bytesSHA/모든CRC/payloadSHA/authoritativeGitidentity/실제추출/frozen8/input3를검증하고MAIN·TERMINAL원문도각provider에서실제다운로드한다. 여기서는미래성공을미리주장하지않는다.

새PNG67161B SHAba2a1ef466af73aaa53aa2ace835ce703b954f069f3220fa56e083fb7dc1175d, PDF17897B SHA9f04af1270d0662b9b5e42ac8d02db3e948cde3d6ffba912c4ea776886fc5c4e는primary안에서각1개생성했고시각검토후원bytes를보존했다. 그림은소수개요이며exact판정은인증서에따른다.

다음단일선택부모는 NUCLEAR_BARE_KERNEL_SOURCE_AND_CONSUMER_CONTRACT다. 다음작업은새source-qualified covariance/formatter/nominal binding과actualatomic→bare/state/support/consumer계약을물리단계에서확정하는것이다. 현B1미결을닫기위한추가수학작업을선택하더라도이번완료identity의4096projection/reference/resume를반복하지않고새영향범위·증명목표·누적예산을먼저동결해야한다. 이작업은다음loop를자동으로시작하지않는다.

Non-tilted LRS Bianchi I, metric(-+++), reacting gas π=0, collisionless DM π_m 별도. 같은normalorthonormalframe에서signedmatter/radiation tensors를먼저합한뒤norm을취한다. Frobenius=√2×half-contraction. 동일trajectory성분분석은species-off인과실험이아니며sampledquadrature/energyresidual은continuumcertificate가아니다. 새ODE0, benchmark0, nuclearactivation0, faststopping0을유지한다.

