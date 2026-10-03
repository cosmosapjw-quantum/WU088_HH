# WU088_HH AD2 실행 결과

2026-10-03 KST. AD2_FROZEN107_IONIC_CERTIFICATE_REUSED_AND_CHANNEL_DATA_ASSEMBLED.

## AD1 백업 복구

첨부 AD1 ZIP12299159bytes/SHA256 d76f9b4e3112c2c8a09c458b112a999e71cc74a0d9c6e0c91f36bfd27fcdc1eb의110개payload와CRC 및 첨부7개자료 identity를 확인했다. 기존AD1 과학/시험은 재실행하지 않았다. ZIP/DB/보고서/원deliveryreceipt를 Drive와Dropbox에 새로 저장해 양쪽 ACK·ID·이름·크기와Driveparent를 확인했다.

Dropbox 원래동명 ZIP은11716351bytes로 이번봉인본과다르다. ALREADY_EXISTS를받고기존파일을보존했으며,같은승인folder에sha_d76f9b4e3112 접미사로별도보관했다. 기존다른파일을같은버전이라추정하거나덮어쓰지않았다. 원실패receipt는역사자료로보존하고현재복구상태는AD1_BACKUP_RECOVERY_RECEIPT.json에분리했다.

Git recovery commit=fec357266c3635561bedd8d7a05b1bb96a6a3bd9,tree=6723878926e347c578f49c560ad2c2f130ef9746. 같은branch에복구index1개를추가했다. AD1의86개파일을Git작업트리에개별게시한것은아니다. 전체파일은SHA-bound이중백업ZIP으로보존됐다.

## 실제 원자 데이터

일반 CP1이라는 이름의과거패키지와실제MODEL_CLOSURE를구분해회수했다. 최종원자는WU088_HH_MODEL_CLOSURE_20260923_v1.zip,3054161bytes,SHA30b147e72e9766fd3ee76e410460eaa2af0948897cd0bce9e92d04343e185075다. 전체111payload와CRC가일치한다. 정확107항tuple,원rational/binary64stdout,원CUSPcertificate,별도좌표review출력,동결FROZEN_INPUTS를같이검사했다. 원자적분기는새로실행하지않았다.

이온에너지:
E_minus/Eh=-3290100018073463578597879486576035298751155913685/6235740319278716029180549194253744953699883661716
=-0.527619793258810251123884492787373197478370840...

- 해석적H(ground)+e 문턱 아래 trial 여유:0.02761979325881025112388449...Eh.
- AD1 finite-H ground에 대한 model affinity:0.02774093964740550702516139...Eh.
- Ground–ground→ion-pair 내부 에너지 차이:0.47213791396399923707356172...Eh.
- 기존T,V에서조립한virialdefect: -0.002706972010373702135001...Eh.

두affinity는서로다른reference를사용한다. 실제Hminus의정확한고유에너지/실험affinity로표시하지않는다. 원trial 또는Gaussian계수를조정하지않았다.

47neutral행모두에원storedRitz진단을연결했고,AD1의25bound-like행에는Rayleighsum과signeddefectinterval을채웠다. 나머지22positiveRitz행의Rayleighexpectation은null이며continuum/ionization으로해석하지않는다. 두ionicorientation은같은에너지를갖지만중복사건수가아니다.

25행중19행positive,6행negative다. 예를들어s:3(중심0)의Delta=+0.003438533269435829...Eh,s:4는-0.018982634957946049...Eh,px:3와pz:3은-0.010945522158020844...Eh다. 번호는저장radialindex이지물리적주양자수n이아니다. 음수는0으로자르지않는다. prescribed-trajectory의actualthreshold나rate로승격하지않는다.

원pref에대한새scalar정규화계산에서는N_full-1≈-2.1334487097326294e-17이다. 과거binary64평가의-1.1102230246251565e-16과계산정밀도가다르며과거기록은그대로보존했다. pref재정규화없음,ionic적분재실행없음. 새구간은90항Machin식의정확유리수상하계에서얻었다.

## 검증

고유35 tests PASS,fail0,skip0. 실제missingbehavior의assertionRED→GREEN8개,후속source/data/CLI회귀27개다. 이전AD1/C4A/CP1과학suite를추가하지않는다. CP1의독립원자review는회수된역사근거이며AD2에대한새독립심사는미수행이다.

Source24개pins와ordered107identity일치. 원Tweak=Tstrong,원T/V/N과E의정확대수일치,별도좌표출력N/T/V/E일치를확인했다. 이것은기존실행결과재사용검증이지새적분증명실행이아니다. 별도의Decimal90산술은25개채널의중성합에서직접빼기하여data와대조했다. 1e-88비교기준은이scalar진단용이며HHtolerance와무관하다.

새표생성한번:wall0.58s,maxRSS94252KiB. 전체35시험wall1.73s,maxRSS94240KiB. 이는이환경의소형실행기록이지NCP/MPI/Fortran/SIMD성능평가가아니다. Python및NumPy정확버전은evidence/FINAL_VERIFICATION.json참조. historicalnativeintegrator,2-centreHH,propagation,NCP,Bianchi/가스history는모두0회.

DB는기존79개테이블/schema/행/원본bytes를보존하고6개를추가해85개다. integrityok,FK0,로컬SQLdump복원논리identity가일치했다. 데이터오류와retrieval실패를구분한다. 초기에일반R10_CP1후보를따라137MB/38MB패키지를확인했지만해당패키지는새원자authority로사용하지않았다. 최종적합한3MBMODEL_CLOSURE만실행패키지에포함한다. 연결조회/DNS오류는원자계산오류가아니다.

## 남은 것과 다음

Physicalsigma/k/threshold/heatmoments는null이다. 기존accepted20/289,missing269unbounded,epsilon_C/Rnull,B22OPEN,scientific/productionfalse,NCPscopeunconsumed를보존한다. 구현검증과물리수치인증을분리한다.

다음AD3는실제AD1전이표를이용한finite-boundE1 branching/lifetime-factor데이터를채운다. Atomicpy성분·angular축퇴도coverage와누락high-n/continuum/multiphoton을명시한다. 원HHbasis를교체하거나없는방출채널을0으로해석하지않는다. Bianchi/가스적분기는rei_bianchi에서처리하며여기서확장하지않는다.

새Git/Drive/Dropbox최종상태는detachedAD2DELIVERY_RECEIPT에서만기록한다. Git연구게시범위와전체원자료ZIP범위를구분한다. UPLOAD_VERIFIED는RESTORE_VERIFIED가아니다.
