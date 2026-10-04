# HH-F1P: 동일 provider를 공유하는 source 차이

새 paired-source reference는 완료했지만 canonical HH-F1은 WAITING_ON_REI_DOMAIN이다. 이 Git 폴더에는 두 reference 모듈과4개 RED/GREEN subset 검사가 있다. 전체30개 검사,26개 상태쌍/3개 모델대조,증명·입력15개·실패원문·로그는 아래59-payload ZIP이 재현 기준이다. Git subset을 전체30개 검사로 부르지 않는다.

## 수학과 실제 검증

같은 analytic fit k=A*T^p*exp(-B/T)의 두 상태에서 d=p*log(Tb/Ta)+B*(Tb-Ta)/(Ta*Tb), deltak=ka*expm1(d), deltaR=10^-6*[ka*(nb-na)*(nb+na)+nb^2*deltak]를 사용한다. 정확한 십진 상태차를 Fraction으로 먼저 만들고 원80자리 directed Decimal 외포로 계산한다. 이미 float에서 사라진 차이를 복원하는 기능이 아니다.

q=(Tb-Ta)/(Tb+Ta),|q|<=1/4이면 log ratio는80항과 tail<=2|q|^161/[161(1-|q|^2)]다. |d|<=1/2이면 expm1은64항과 tail<=(132/131)|d|^65/65!다. 원 Grackle3000K 불연속은 jump와 smooth부분을 분리하고 floor를 삭제하지 않는다. 같은 상태는 대수적으로[0,0]이며 no-extra-half·공통chi·species/energy coefficient를 보존한다.

LCS,T=10000,n=2에서 deltaT=1e-96의 source 차이 약7.2112740e-124를 양의 외포로 보존했다. 밀도와 온도 효과가 상쇄하는 사례는 새 구간도0을 포함한다. 따라서 모든 경우에 좁거나 부호가 결정된다는 보증이 아니다. 측정 입력은 제조값이며 물리domain이 아니다. 고정상태에서 KS deltaR-LCS deltaR는 actual model-dependent histories의 차이가 아니다.

새 고유30 PASS(실제RED/GREEN4+후속26),26개 상태쌍과3개 모델대조의280-working-digit oracle containment를 확인했다. 내부 작은 tail의 public-input 재검사 오류와 test-only220자리 cancellation 오류를 분류·수정해 보존했다. 원F1코드와 public precision80은 유지했다. HH field/primitive/NCP/history는0회,원DB·다른repo수정0이다. 독립scientificreview·물리율승인은 미수행이다.

## Cloud-first

기존cache를 우선 확인하고 없으면 접근 가능한 provider 한 곳에서만 다운로드한다. 사용자에게 재업로드를 요구하지 않는다.

- name: WU088_HH_FAST_F1P_DELIVERY_20261004_v1.zip
- bytes: 89773
- SHA256: 35e64c16be7d8fda86f4f2b35a88fdffd0d7721276e92316f4371ae35a14c8d1
- Drive ID: 1_QCZEx050NOqoRulMsOzu9zzw-ZjRe5D
- Dropbox ID: id:BSpOijBcT10AAAAAADx7MQ
- Drive parent: 1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM
- Dropbox directory: /BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/

ZIP 검증 후 HANDOFF_KO.md,THEORY_KO.md,RESULT.json,external_rates/hh_paired_source_contract.json을 읽는다. 전체검사가 실제 필요할 때만 python3 -B -m unittest discover -s tests -v를 실행한다. CLI는표준라이브러리,tests는mpmath1.3.0이다.

## 다음 실제 의존성

최신 REI 조회6e577ec3692f6d19d8ce3a9cae0364d4439f5fcb는FT02 source/domain 연구까지이고 nextFT03_THERMAL_CLOSURE다. 지정science_scenario_v1.json과rei_model_lock.json은그commit에서404였다. 실제REI-F07 domain/observable/constants/owner/coordinate/adapterpath를소비자가결속해야한다. FT02의sample검산이나FT01toy온도를그승인으로바꾸지않는다.

REI-F07 -> HH-F1결속 -> HH-F2actualRustseam -> REI-F09유일pairedhistory -> HH-F3/F4다. HH에서는Bianchi/solver/history를복제하지않고,입력이없다고legacy적분을대신실행하지않는다. Source부품을무한히추가하기보다도착한소비자계약의필요항만결속한다.

기존24/289,265unbounded,epsilon_C/Rnull,B22OPEN,FD1/FD2/pilotconsumed는보존한다. 같은branchadditive/nonforce 및기존Drive/Dropboxcreate-only백업을유지한다. ACK/metadata,byteidentity,restore,sciencevalidation을구분한다.
