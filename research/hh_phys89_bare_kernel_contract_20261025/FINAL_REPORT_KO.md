# PHYS89 최종 과학 보고 — 원 covariance 진단과 공통 사건 소비자 인터페이스

## 판정과 범위

이번 유한 자식 `ENDF_MF33_PULLBACK_AND_TYPED_NUCLEAR_CONSUMER_INTERFACE`는 원 MF33 구조의 독립 복원, 정확한 표시 행렬 반례, 조건부 유한 covariance/normalization 및 같은 사건의 energy/clock 계약을 구현·검증했다. 선택 물리 노드 `NUCLEAR_BARE_KERNEL_SOURCE_AND_CONSUMER_CONTRACT`와 원 atomic-to-bare/physical finite-T supplier 부모는 **PARTIAL_INPUT_DEPENDENCIES**다. Actual mass/state/differential kernel, 현재 nominal과 covariance의 원 평가 결속, full-support tail, named consumer 구현·ACK가 아직 필요하다.

이 보고서는 S2 과학·독립 검토 시점의 **R1–R9/C1–C9=18/20 불변 snapshot**이다. 이후 FINAL ZIP 양쪽 실제 복원, MAIN/TERMINAL 원문 및 중앙 FINAL·PR146 actual readback은 별도의20/20 완료 영수증으로 결속한다. 이 문서를 미래 결과로 소급 수정하지 않는다. 전체 물리 목표 완료율은null이다.

## 1. 핵심 과학 결과: 표시된 MF33 행렬의 PSD 실패

원 ENDF671232bytes/SHA256 `3024d8f0db604b074e33ed8b05027eb9f5a738614041ba44c83f048e0d0bc1af`의 MF33/MT102는153groups/154boundaries/11781upper-triangle values다. PHYS88의153sigma knots/152cells와 다른 grid이다. Native Es 보간과 원 sigma support[1e-5,2e7]eV를 그대로 유지한다. MF33의 wider bounds[5e-6,2.025e7]eV는 sigma support를 확장하지 않는다.

Zero-based indices0,10의 실제 fractional covariance block은 다음과 같다.

\[
F_{\{0,10\}}=\begin{pmatrix}
0.0004278572&0.0004278572\\
0.0004278572&0.0004278571
\end{pmatrix}.
\]

정확한 decimal/Fraction 계산에서 determinant는

\[
-\frac{1069643}{25000000000000000000}<0.
\]

w_0=1,w_10=-1인 벡터로는 더욱 직접적으로 w^T F w=-10^-10이다. 따라서 이 표시 행렬 그대로의 joint stochastic covariance 채택은 불가능하다. Group0은 sigma-support 안에[1e-5,1.5e-5)eV의 비공허 교집합을 갖고, group10은[0.01765,0.06265)eV다. Source 밖의 행만 골라 만든 반례가 아니다.

한 번의 binary64 eigensolve는 min=-4.688696562507235e-8,max=2.8829808686931577,negative72를 관측했다. 이 개수는 spectral enclosure가 아닌 진단이다. 채택한 exact 증명은 두-bin minor와 quadratic form이다. 독립 reference는 eigenvalue를 재실행하지 않고 source tokens와 minor를 직접 확인했다. 상세 증명은 theory/DISPLAYED_COVARIANCE_WITNESS_KO.md에 있다.

원F는 수정하지 않았다. 원인은 **NOT_ESTABLISHED**다. Token ULP/반ULP는 nearest-rounding을 가정한 조건부 formatting 자료이며 실제 물리 uncertainty나 formatter 보증이 아니다. 이 결과는 현재 표시 행렬에 대한 반례이고 evaluator·물리 모델 전체의 strong no-go는 아니다.

## 2. 원 평가 출처와 미결 covariance 연결

원 MF1과 Brown2018 §III.A.2의 n-p/γ-d R-matrix 출처는 nuclear evaluation을 지지한다. Atomic AWR 관례만으로 electron-resolved neutral-atom kernel을 주장할 수 없다. 명목 unpolarized n,p 상태를 가정할 때 evaluated sigma에 추가1/4 또는3/4 spin계수를 곱하지 않는다. Exact evaluator mass deck과 empirical source-coordinate→bare 대응 및 electron/target 보정은 미결이다.[1,2]

MF1은 covariance를 COMMARA-2.0/July2011에서 가져왔다고 기록하고, nominal header는 EVAL-JUL16/REV1-NOV23이다. 공식 COMMARA 자료는 ENDF/B-VII.0 central values와 쓰는33-group NJOY1/E 제품을 설명한다. 현재153-group MF33와의 exact source identity, rebinning, nominal normalization 변환은 확인되지 않았다. 이 provenance 차이 자체를 행렬 오류의 원인으로 판정하지 않는다.[3]

Exa·SciSpace의 추가 한정 조사와1차 문헌 읽기는 intake/source_followup에 실제 raw 응답으로 보존했다. 중단 전 Exa2search+4fetch/SciSpace1 기록은 인계에서 재사용했고 당시 raw bytes는 현재 호스트에서 복구되지 않았다. Wolfram의 새 유한식 evaluator1회/7zeros와context SERVICE_ERROR1도 transcript로 보존하며 추가 호출0이다. 소진된 허용량을 되돌리지 않는다.

## 3. 닫힌 조건부 수학·인터페이스

Monotone Es=phi(Eb)에서 source fractional covariance는 F[g(phi(Eb)),g(phi(Eb'))]로 당긴다. Sigma와F에 추가 Jacobian을 곱하지 않으며 Jacobian은 적분 measure에만 들어간다. 불연속 bin은 canonical native Es/bin 또는 직접 변환한 boundary로 분류한다. Floating roundtrip과epsilon clipping을 사용하지 않는다.

유한 group coefficients r>=0,Z=sum r>0,A=sum a,M=A/Z에 대해 선형 covariance는 LFL^T, normalized sensitivity는 b=(a-Mr)/Z, 일차 mean covariance는 BFB^T다. 정확한 finite ratio변화는(deltaA-MdeltaZ)/(Z+deltaZ)이고, |deltaZ|<=rho Z,rho<1에서 일차 잔차는rho/(1-rho)|b·eta| 이하이다. 서로 다른 consumer도 같은 source F의 교차 상관을 유지한다. 옛 scalar thermal totals로 새 group weights를 추정하지 않았다.

같은 proper-volume/proper-time event measure에서 energy owner는 thermal=hKd-Kin,fast=(1-h)Kd,rest=-Qb,atomic=0,photonhandoff=rγEγ,escape=(1-rγ)Eγ이다. Event energy 보존으로 여섯 열의 합과 전파한 covariance의 합계 행이0이다. h가 event-dependent이면 joint<hKd>를 쓴다. Thermal count h-2와 caloric 식은 입사n,p가 모두 thermal reservoir 소유일 때만 허용한다.

C_V=sum_s n_s partial_T u_s>0에서 capture 기여의 온도분자는 integral[-Kin+u_n+u_p+h(Kd-u_d)]dnu다. 팽창/work/다른 과정은 별도이다. h=1은 instant caloric birth 가정이며 stopping 계산이 아니다. Photon/fast spectrum은 동일 joint measure의 pushforward가 필요하다. Tensor birth rate와 저장된 stress state도 구별한다.

Conserved reference nHref에는dotY=S/nHref, 일반 reference에는추가-Y(Theta+dotnHref/nHref)를 쓴다. Lapse는1회만 적용하며 cm^-3→m^-3와eV→J를 명시한다. Full-support tail은0<=Ztail<=B0와|Atail|<=BA가 실제 제공될 때만|(Mfull-MI)|<=(BA+|MI|B0)/ZI로 결속한다. 실제tail입력은없다.

## 4. 실제 구현과 검증

| 항목 | 실제 결과 |
|---|---|
| 원 primary |1child,exit0,27/27checks(guard15),eigh1 |
| 첫 independent reference |1child,exit1,빈 ENDF control field의int 변환에서 중단; 원문 보존 |
| 별도 reference repair1 |1child,exit0,PASS_EXACT |
| Source 대조 |154boundaries,11781packed values,23409matrix entries,rawtoken bytes exact |
| 제조된 유한 fixture | 독립 Fraction 식 전체 exact; physical rate 입력과 구별 |
| Float/정확값 |117비교,고정5e-15+5e-13|exact| 이내 |
| 원 표시 행렬 | exact negative minor 독립 확인; projection/jitter/clipping0 |
| 실제 resume | primary1+repair1reference1=2SKIP;callback/integral/rewrite0;22fileshash불변 |
| 새 적분/ODE/benchmark/rateactivation/stopping | 모두0 |

Primary identity는 `c688ab6b06ab1e94781645e174cd555423ba49fc15d6b76c31acef3890f2e8b2`다. 실패한 원reference.py를 포함한 원7개 freeze와 성공primary bytes를 보존했다. 수정한 독립 checker는 별도 identity `0f946ef3e6d2253091e50f4bdfca708ce9900a93677d0793367510b5ee2111b5`로 원primarymanifest에 결속한다. 변경되지 않은 primary/eigh의 재실행은0이다.

독립 R6는 thermal 소유권·양의C_V·capture기여한정을 명시하는 수정1건을 닫았다. Static 검토는 replay전차단, signed-energy소유권, exactzero직렬화3건을 한patch로 닫았다. 첫 static 검토가 blank-control 경로를 놓친 사실과 실제 실패를 보존하고, 새 checker의 한정 수정과C9에서 닫았다. reviews/가 권위 있는 독립 판정 원문이다.

## 5. 비용·실패·재사용

새 scientific children3=success2+preservedfailure1, childCPU0.41658999999999996s, launchwall0.4201385129999835s, coordinatorCPU0.073001s다. Metadata dispatcher의json.dumps flush 인자 오류1회는 wrapper/child0으로 별도 보존했다. Read-only resume CPU0.033745s+0.035615s 및wall0.033984227s+0.035932670s는 과학 child 비용과 구별한다. Primary/원reference/repair1/Wolfram 잔여허용량은 모두0, budgetreset=false다.

PHYS88 children4=success3+artifactfail1, CPU7.322937s/wall7.330995100001019s, metadataCPU0.0005106s를 불변 재사용한다. PDF shortening 원인NOT_ESTABLISHED, 추가artifact childexit1와최초원bytes복구 이력, 원2PNG+2PDF를 보존했다. PHYS88 Wolfram2calls와18scalarzeros/all_zeroFalse, 별도positive-branch proof, prior symboliclineage7을 유지한다. PHYS89의기록된evaluator1을포함한lineage는8이고contextfailure는별도다. 전체 역사/원격CPU·비용·금액·잔여예산 미관측값은null이다.

중단 후 원작업경로는 현호스트에서 존재하지 않았고 원인은NOT_ESTABLISHED다. PHYS88 FINAL의101files를nativeGit으로 복원하고 PHYS82 CRLF복구 ancestry를 확인했다. ParentZIP/MAIN/TERMINAL 실제Drive 원bytes/SHA를 다시 확보했다. 기존 양쪽CRC479/payload478/Git101/extract479/frozen26 완료는 재사용하며, 현재복구GET과과거finalGET을혼합하지 않는다. MAIN18/20과laterTERMINAL/PR14520/20의시점도유지한다.

## 6. 소비자와 중앙 보존

REI-L2는 기존 beta daughter/energy 계약이다. `WU89_REI_L2_NP_CAPTURE_REQUEST_V1`은 capture 확장 제안이며scope_extension_required=true,actualowner/ACK=null이다. Thermal/fast구현은PROPOSED_UNIMPLEMENTED다. BASS nuclear photon request도NOT_BOUND다. B3C coldH-Lyα14cohort는manufactured설계참고다.

중앙9600→fc159→2354의 추가HE/HI/CR결과를읽었다. 원40contracts/planstatus/deps,7authorities,17edges, WU원관측·HHhandoff prefix와다른39nodes를보존한다. HE의local+metadataACK대remoteGET미주장, CR의DriveUNKNOWN, HI의remoteGETNOT_RUN 및후속CR의18/20snapshot을그대로유지한다. 이들은nuclearcapture또는faststopping공급수용이아니다. 중앙의다른owner가쓴과거PHYS89 S0/실행0관측은당시snapshot이며본actual실행원문이후상태를대체하지않는다.

원51repo/2241branch/65terminalpage및6repo최근5PR조사는한정snapshot으로재사용했다. 비공개대화전체나Drive1000cap밖을전수조사했다고하지않는다.

## 7. 다음 실제 입력

1. 현재nominal에결속된 원 evaluator covariance identity와153group변환·normalization·원precision 또는승인된sourcecorrection.
2. 정확한massdeck/invariant-s transfer, electron/targetstate validity와physicaluncertainty.
3. Differential kernel의scatteringcoordinate/각도·mass·state covariance와sigma-support밖tailB0/BA.
4. Capture-specific thermal/fast/radiation namedconsumer의실제구현경로·측도·properclock/reference-density·ownership·ACK.

완료된153×153원행렬진단,27checks,exactreference,원PHYS78–88/HH/REI/REC/HE/C22/C23A identity는재실행하지않는다. Runtimeversion차이는재실행근거가아니다. 새로운입력으로영향받은의존성만새계약으로진행한다. 실제nuclear rates와faststopping은계속비활성이다.

Non-tilted LRS Bianchi I,metric(-+++),reactinggasπ=0/DMπ_m별도,동일normalframe의signedmatter+radiation합후norm,Frobenius=√2×half-contraction을유지한다. 동일trajectory분석은species-off인과실험이아니고sampledresidual은continuumcertificate가아니다. HH_R10=OFF,productionNOT_ISSUED.

## 출처

[1] ENDF-102(2023), §0.5.1.1,§33.2.2.2: https://www.nndc.bnl.gov/endfdocs/ENDF-102-2023.pdf
[2] Brown et al., NuclearDataSheets148(2018),§III.A.2/TableII: https://escholarship.org/content/qt2dj9p3h4/qt2dj9p3h4_noSplash_7d55137415e7004203a27c552b02b984.pdf
[3] Official2011USNDP report, COMMARA-2.0: https://www.nndc.bnl.gov/usndp/docs/USNDP-FY2011-Report.pdf ; reportrecord https://www.osti.gov/biblio/1013530
[4] Paris–Hale2017 LANL R-matrix covariance presentation: https://indico.bnl.gov/event/3580/contributions/10531/attachments/9392/11489/Paris_Hale-csewg_171107_wNJOY.pdf

직접결과의권위근거는고정ENDF원bytes,verification/의원실행/출력/실패,resume기록,theory/의정확한증명,reviews/의독립판정이다.
