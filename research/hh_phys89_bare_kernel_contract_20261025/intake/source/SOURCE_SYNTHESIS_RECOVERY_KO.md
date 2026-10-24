# PHYS89 원전·수신 계약 복구

## 상태와 근거 경계

선택 노드 `NUCLEAR_BARE_KERNEL_SOURCE_AND_CONSUMER_CONTRACT`는 **PARTIAL_INPUT_DEPENDENCIES**다. PHYS88 FINAL `92dec7cdc1cf5afeff5bdff8d6234f7f1e3dbbd8`의 물리 결과를 재사용했다. 이번 복구에서 과학 코드, Wolfram, 적분, ODE, benchmark를 실행하지 않았다.

이전 PHYS89 scratch가 사라져 이전 SOURCE_PHYSICS_FINDINGS_KO.md 및 계약 원bytes는 확보되지 않았다. 이 문서는 대화에 보존된 이미 완료된 유도와 새로 읽은 고정 Git/원전 자료로 만든 **새 복구 산출물**이다. 이전 파일 SHA와 동일하다고 주장하지 않는다. 이전 Exa2search+4fetch, SciSpace1, web6 기록은 대화 요약에서 재사용했고 원 raw 응답은 복구되지 않았다. 추가 읽기는 GitHub7calls와 web3calls(open2문헌, find4항목, open3구간)이며 Exa/SciSpace/Wolfram 추가 호출은0이다.

## 원전에서 채택하는 범위

ENDF의 AWR는 target material에 atomic-mass convention을 사용한다. 이 형식 규칙은 전자가 분해된 neutral-atom reaction kernel을 뜻하지 않는다. 이 파일의 MF1은 n-p capture 및 역 deuteron photodisintegration을 N-N R-matrix 분석에 포함했다고 설명한다. Brown2018 TableII도 p+p, n+p, gamma+d, n+n 채널을 사용한다. 따라서 핵반응 평가 자료라는 출처는 채택할 수 있고, 원 평가의 정확한 mass deck과 electron/target 보정은 별도 입력으로 남는다. [1,2,3]

Brown2018은 capture86점, inverse88점과 thermal332.58mb를 보고한다. Fit은50MeV까지이지만 배포 cross-section은20MeV까지다. 원 파일 MF1의332.0mb 설명과 COMMARA-2.0/July2011 covariance 출처는 역사 기록으로 보존한다. 서로 다른 provenance 시점을 임의로 같게 만들지 않는다. [2,3]

Bare 상태는 unpolarized n,p의 명시적 가정 `(I2/2)⊗(I2/2)`으로 둔다. 이를 채택한 evaluated cross-section에 spin1/4 또는3/4를 다시 곱하지 않는다. LAB_ANCHORED와 FIXED_COM_K는 PHYS88의 조건부 사상으로 유지한다. 같은 사건의 signed carrier를 새 bare 사건에 추가하거나 heat/실제 electron으로 해석하지 않는다.

## Cross-section과 covariance grid

| 항목 | 고정 내용 |
|---|---|
| Source | MAT125, n-001_H_001.endf; SHA2563024d8f0db604b074e33ed8b05027eb9f5a738614041ba44c83f048e0d0bc1af |
| MF3/MT102 | 원153knots/152cells, native LAB Es 보간, support[1e-5,2e7]eV |
| MF33/MT102 | NL1, MAT1=0, MT1=102, NC0, NI1, LS1, LB5, NT11935, NE154 |
| Covariance | 153groups,154boundaries,11781upper-triangle tokens; row별 diagonal부터 저장 |
| Covariance support | [5e-6,2.025e7]eV; sigma의 유효 support 확장이 아님 |
| Raw record 범위 | 6836–8828,1993records; header/current boundary excerpts 재읽기 |
| PSD | 이번 source 복구에서 계산하지 않음; 후속 새 affected code의 별도 결과 필요 |

LB5는 energy-bin fractional covariance이다. `Cov[σ(E),σ(E′)]=σ(E)σ(E′)F[g(E),g(E′)]`이며153sigma knots에 F를 보간하지 않는다. 두 grid의 공통 refinement를 sigma support 안에서 사용한다. [1,3]

`Es=phi(Eb)`라면 fractional covariance는 `F[g(phi(Eb)),g(phi(Eb′))]`로 당긴다. Jacobian은 적분 measure를 바꿀 때만 붙인다. Bin 경계는 canonical native Es/bin 또는 직접 변환한 covariance boundary로 분류한다. 부동소수점 roundtrip과 epsilon clipping으로 경계 소속을 정하지 않는다.

## 이미 유도된 유한 함수 관계의 복구

Group weights가 `r_g>=0, Z=sum(r)>0`이고 rewards가 `a_ag`이면 `A_a=sum(a_ag), M_a=A_a/Z`다. 같은 fractional source perturbation eta에 대해 `deltaZ=r·eta, deltaA=a·eta`이며 선형 출력 covariance는 `LFL^T`다. Mean의 일차 계수는 `b=(a-Mr)/Z`, covariance는 `BFB^T`다.

정확한 유한 변화는 `DeltaM=(DeltaA-M DeltaZ)/(Z+DeltaZ)`다. `|DeltaZ|<=rho Z, rho<1`이면 선형화 잔차는 `rho/(1-rho)|b·eta|` 이하이다. 이 관계는 일차 covariance 전파를 실제 physical CI나 nonlinear coupled-history bound로 승격하지 않는다. 모든 consumer/map/T에 같은 source field를 사용한다. Event variance, source epistemic covariance, shot noise는 서로 다른 입력이다. 원 thermal scalar totals만으로 group weights를 복원할 수 없으므로 옛 적분은 재실행하지 않는다.

원 F에 대한 PSD projection, jitter, clipping은 허용하지 않는다. 표시된 decimal tokens에 exact negative minor가 발견되더라도 해당 표시 행렬의 범위에서만 해석한다. 반올림 half-ULP 상자는 별도 조건부 formatting model이며 실제 물리 uncertainty가 아니다.

## 실제 수신 의무

현재 중앙 HEAD9600a605f6380bc2262d0cfce5ff00290e594a5a의 원 REI authority contracts를 실제 읽고 확인했다. REI-L2는 beta daughter/energy accounting이며 allowed_paths는 research/rei_beta_resolved_energy/**다. Capture에 연결할 요청 `WU89_REI_L2_NP_CAPTURE_REQUEST_V1`은 `PROPOSED_CAPTURE_EXTENSION_OF_REI_L2_BOOKKEEPING`이며 scope extension이 필요하다. Thermal/fast 구현과 owner ACK는 null이다. BASS B3C의 cold H-Lyalpha14cohort manufactured 사례는 proper clock 및 newborn bookkeeping의 설계 참고이며 nuclear photon consumer는 NOT_BOUND다.

공통 사건 measure는 같은 normal orthonormal frame의 proper volume/proper time에 정의한다. Distinct n,p이므로 identical-pair1/2가 없다. Energy owner6열은 `hKd-Kin, (1-h)Kd, -Qb, 0, rgamma Egamma, (1-rgamma)Egamma`다. Event conservation을 먼저 만족하고, caloric 식은 particle-count 변화까지 포함한다. `h=1`은 즉시 thermal birth 가정이며 stopping 결과가 아니다. Event-dependent h는 joint mean `<hKd>`로 보존한다.

Photon/fast spectrum에는 같은 joint event measure의 pushforward가 필요하다. Mean energy만으로 spectrum을 구성했다고 하지 않는다. `q^mu q^nu/q^0`를 사건 measure에 적분한 것은 birth RATE이며 accumulated tensor STATE가 아니다. Four-momentum conservation은 spatial-stress 합0을 함의하지 않는다. Conserved reference density이면 `dotY=S/nHref`; 일반 reference에서는 `-Y(Theta+dotnHref/nHref)`항이 필요하다. Coordinate clock 전환의 lapse는1회 적용한다.

실제 tail은 omitted mass B0와 omitted absolute reward moment BA를 요구한다. 이미 유도된 `|Mfull-MI|<=(BA+|MI|B0)/ZI`의 입력이 아직 없다. 단순 Boltzmann suppression과50MeV fit 언급은 이 입력을 대신하지 않는다.

## 유지되는 gate

Non-tilted LRS Bianchi I, metric(-+++), reacting gas pi=0, collisionless DM pi_m 별도를 유지한다. Signed matter/radiation tensor를 같은 frame에서 합한 뒤 norm을 취한다. Frobenius=sqrt(2)×half-contraction. Same-trajectory 성분 분해를 species-off causal experiment로 쓰지 않는다.

HH_R10=OFF, production NOT_ISSUED, 전체 물리 완료율null. 새 ODE0, benchmark0, nuclear rate activation0, fast stopping0, old completed identity replay0. 소진된 허용량을 재설정하지 않는다. 실제 source-state/mass/uncertainty 및 named consumer 계약이 닫히기 전까지 선택 물리 노드와 원 physical supplier 부모는 PARTIAL이다.

## 원전

복원된 parent ENDF671232bytes의 SHA256과 Gitblob4770d7f18ef275c9a72cc779391a07c1bfc7cbea를 실제 로컬 원bytes로 다시 확인했다. 이는 읽기/identity 검증이며 covariance 계산이 아니다. 현재 REI authority16380bytes SHA256c618a2296eb5a6ad8f4f14ee8e93cd382f3364af1843cb4342489f0a6f407958도 확인했다.

[1] ENDF-6 Formats Manual, ENDF-102 (2023), §0.5.1.1 및 §33.2.2.2, PDFp42,p302–303: https://www.nndc.bnl.gov/endfdocs/ENDF-102-2023.pdf

[2] D. A. Brown et al., Nuclear Data Sheets148(2018)1–142, §III.A.2/TableII, DOI10.1016/j.nds.2018.02.001: https://escholarship.org/content/qt2dj9p3h4/qt2dj9p3h4_noSplash_7d55137415e7004203a27c552b02b984.pdf

[3] Pinned PHYS88 source: https://github.com/cosmosapjw-quantum/WU088_HH/blob/92dec7cdc1cf5afeff5bdff8d6234f7f1e3dbbd8/research/hh_phys88_atomic_bare_remap_20261024/source_data/n-001_H_001.endf

