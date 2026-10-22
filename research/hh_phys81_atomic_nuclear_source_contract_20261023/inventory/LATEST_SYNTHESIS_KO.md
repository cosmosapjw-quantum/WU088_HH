# PHYS81 전 최신 원격 연구 intake — 2026-10-23 KST

## 판정

PHYS80의 실제 후손 시작점은 WU088_HH Draft PR136의 `951182dd59bbb59dba454bbaab78ad56d029355a`이다. PR135의 D event-energy component와 PR134의 PHYS79 결과도 이전 고정 identity를 유지한다. 새 과학 실행을 시작하기 전에 확인된 중요한 변화는 **bass_cr C22D의 H1 finite CI 완료**, **REI221의 국소 열 RR 및 beta/RR 완료**, **REC125 THERM02 완료**, **BASS_HE 중성 수송 및 별도 finite-mass component 완료**다. 이 구성요소를 재구현하거나 이전 IVP를 다시 실행할 이유는 없다.

이 intake 자체의 ODE·과학 테스트·benchmark·source import·compile·remote mutation은 모두 0이다. GitHub exact-head 텍스트 및 보존된 PHYS80 기록만 읽었다. 다른 process를 종료하지 않았다.

## 조사 범위와 실제 근거

| 조사 | 실제 범위 | 한계 |
|---|---|---|
| Repository | owner `cosmosapjw-quantum`, authenticated search page1 51개, page2 0개 | 연결 계정에서 현재 접근 가능한 repo만 |
| Branch | 51개 repo 각각의 /branches pagination 완료, 63 API pages, 2,175 refs, 오류0 | 모든 branch의 source/results 본문까지 읽은 것은 아님 |
| 최근 PR | WU/REI/REC/HE/CR/bass/toy_bbn 각 updated-desc page1, 최대20개 | 전체 역사 PR 열람이 아닌 최근 후보 선별 |
| 본문·handoff·source | exact-head fetch 42건; 40개 nonempty 저장, 1개404, 1개 directory empty | 선택된 직접 관련 파일, 모든 repo content 감사 아님 |
| Identity | 선택 PR22개가 branch 열거 HEAD와 일치; 알려진 blob10개 직접 SHA1 일치; CCC 표 SHA256 일치 | 모든 sibling 전체 archive를 새로 복원한 것이 아님 |
| 이전 비교 | PHYS80 inventory의 비교 가능한10ref;7불변/3변경 | 옛 bounded catalog와 전체 branch 수를 차감해 신규 수로 부르지 않음 |
| 대화·외부 백업 | 이 하위 작업은 공개/권한 내 repo 기록 및 전달 pointer만 | 접근 불가 비공개 대화·미게시 실행은 미관측; provider 재검증은 별도 intake 담당 |

전체 ref 관측 마감: **2026-10-22T21:47:50.226Z**. 각 API page 및 파일 관측 시각은 manifest에 따로 저장했다. `BASS_ATOMIC_RECOMBINATION`은 이번51개 repo 열거에 존재하지 않는 이름이고, 실제 관련 repo는 `rec_bianchi`다.

완료된 전수 열거와 선택적 본문 읽기를 구분한다. ROOT의 현재 PHYS81 정책과 사용자의 중복 실행 금지는 과거 handoff의 오래된 우선순위/재실행 명령보다 우선한다.

## 실제 최신 anchor

| Repo/PR | HEAD | 확인된 실제 상태 |
|---|---|---|
| WU136 | 951182dd59bbb59dba454bbaab78ad56d029355a | PHYS80 final 불변, 다음 additive 단원의 권고 부모 |
| WU135 | 6c3b12554288893d5d7e221d77be943324285ceb | D energy/particle ledger component 불변; matched PI/RR source moments OPEN |
| WU134 | 3304d16db1dc9bf868c185a8eeb6cc9dbc270e50 | PHYS79 불변 |
| REI222 | b4b5d289aaad9ef167f683f19418b0ff87ed8425 | Oct23 successor DAG에 N1/N5/N7 완료; 예전 Oct22 handoff만 읽으면 새 상태를 놓침 |
| REI221 | 9620e1fcc4bdda76e0311206f614234926600381 | atomic adapter 이후 local thermal/beta flows 추가 완료 |
| REI219 | 6a12f3865d9ea427c1391c41caed8bb7cb7ec00d |18-family nuclear sensitivity 불변, source/closure 한계 유지 |
| REC125 | 407a280aff51abefc10374cb6e21c4224140328c | THERM028개 실제 완료; PR 본문의 pending 문장은 오래됨 |
| REC124 | e6ecef7624e39bee66b39e09d99fe355f76e2eae | native full63 Compton8 완료, REC125와 별도 cohort |
| HE88 | fd11542ea8236e3c17eeb798bcafa8956e0eb248 | HE34-SCR mechanics+neutral H/He transport 완료 |
| HE87 | 96338b7d3c04b18e31a080e56b34985d31921104 | Lorentz 다음 HE35 pseudo-Maxwell finite-mass pair component 포함 |
| CR96 | ba39fc75521aa18705ec832d789e50dd5c6565bc | C22D H1 CI4 및 C22E saved line diagnostic 완료 |
| CR C22C pointer branch | 5750489be6ad80b4e142f5712c656c33ae07f097 | CCC excitation archive의 evidence-only pointer; C22D보다 오래된 과학 범위 |
| bass181 | 797d66580448dad7fc41f2c2db31fe0eb37908bf | affine33→30 component 불변; opt-in integration 후속은 REI222가 VigilODE69e83044로 보고 |
| toy_bbn main | 908c24e478384912b0c547aade5e209b7ec2695f | 2026-01-24 cleanup, 이번10월 새 atomic/nuclear 결과 아님 |

정확한 branch/base/updated/observed 시각과 URL은 SELECTED_ACTUAL_REFS.json에 있다. PR 본문과 current source가 상충하면 파일 시점과 science receipt를 우선하며, 게시·백업 완료는 별도 receipt 범위로만 판정한다.

## C22D: H1 finite CI를 그대로 재사용할 수 있는 범위

읽은 원본: CR96 exact HEAD의 REPORT_KO.md, CONTRACT.json, ci_finite.py, sources/CCC_TICS_1S.txt, SCIENCE_ACCEPTANCE.json, THEORY_PROVENANCE_AND_COVERAGE.json, SOURCE_FREEZE.json, REMOTE_RELEASE_INDEX.json.

- CCC 저자 H I 1S→TICS 표 **87행**, 단면적 `a0^2`, incident E in eV. 추가 pi 또는 multiplicity가 없다.
- 표 범위 **13.6058–968.61 eV**, 첫 양의 점13.64 eV. SHA256 **7a87a2c9f2116ee36c0786b379dac08e1f4d92a49504fe542e6aa71cbb279bae**; 이번5754-byte text가 이 hash에 실제 일치했다.
- 저자 URL: https://atom.curtin.edu.au/CCC-WWW/index.html ; archive https://atom.curtin.edu.au/CCC-DB/H/I/ELECTRON_IMPACT/e-H_XSEC_LS.zip .
- 완성된 evaluator는 PL 단면적의 **유한 Maxwell 적분**이다. positive endpoint moments와 threshold-scaled exponent 및 log10 rate를 보존하고, 표현 범위 underflow와 미제공 source를 구분한다.
- code의 numerical T domain은1–1e8 K지만 **기존 coupled pilot의 물리 채택 범위는3<T≤20000 K, nHref≤0.01 cm^-3**다. 이 두 범위를 혼동하면 안 된다. PHYS78 Tmax25370.663 K는 기존 pilot admission 밖이다.
- `species != H1`, `full_physical_rate=True`를 거부한다. D/T/He/Li CI 및 excitation은 source unavailable이며0으로 메우지 않는다.
- physical interpolation error와 omitted high-E tail은 OPEN. 가상의 sigma cap을 입력하는 tail 표현은 premise가 입증되지 않은 조건부 식이다. 첫0.0342eV의 power1.127 대안은 sensitivity model이며 물리 오차상한이 아니다.

에너지 registry는 CCC source convention13.6058 eV를 H1/D/T의 공통 electronic threshold에 사용하고 PI support, ionic binding, PI heat, RR export, CI cooling을 일치시킨다. 기존 PH2 shape/에너지 축과 total-RR number/derivative capture fit은 유지한다. 이는 새로 선언한 혼합 constitutive model이며 Milne/LTE 또는 isotope reduced-mass closure가 아니다. NIST H1의13.598433 eV와 CCC13.6058 eV를 구별한다.

사건당 CI는 H0−1/H+ +1/e+1/총 gas particle+1, U−chi/B+chi, escaped CI energy0이다. U와 abundance를 진화시키면 입자 수에 따른 온도 항은 이미 포함되므로 T equation에 중복 추가하지 않는다. H1에만 CI가 추가된 경우 기존 H1/D 동일 ionized-fraction quotient는 깨지며, 전체 isotope 축약이 불가능하다는 일반 명제를 뜻하지 않는다.

이 단원은4개 새IVP(3BDF+1Radau), saved804/accepted8047을 이미 완료했다. local code/result를 재실행하지 않았다. full raw archive와 selected Git text scope는 다르다. release index에 원 archive48,727,596B/SHAa64bda4b…와 Library/Dropbox의 producer readback PASS가 있고 Drive는 OPEN_UNKNOWN_NO_ACK다. 이는 **생산자 영수증 재사용**이며 이번 intake에서 원격 ZIP 전체를 새로 받은 것은 아니다.

Bell Table5 B1 해결 여부는 이 C22D 파일이 제공하지 않는다. Bell closure와 CCC finite-source alternative는 다른 의무다.

## HE88와 HE87: 원자 수송 및 응력의 경계

HE88의 중성 H1/He4 first-Sonine Chapman–Enskog viscosity는 Wargnier2020 Appendix C29/C30/C35–C38, Bruno2010 Eq11/TableI, Mutation++ official pin58678c0e038eb2f078fed3b45640741fdaf167dc에 결속한다. 확보된 Q항은 H–H(2,2), H–He(1,1)/(2,2), He–He(2,2), 단위는 **Qbar=pi×1e−20×F(T) m²**, source 사용범위50–50000 K다.

2×2 선형계의 positive rational 축약은201개 저장 조성에서 독립 solve와 최대상대차6.4653146232e−16로 확인됐다. 실제 진단은 common T=20000 K와 A*m_u 질량근사다. chi_match=p_neutral/(eta H)는1.6671e4→1.5527e−3, 97/201점에서1보다 작다. 이것으로 전 구간 빠른 이완 또는 전체 플라스마 유체 no-go를 주장하지 않는다.

HE88 prescribed constant-chi mechanics, 저주파 viscosity matching p/eta, HE87 Lorentz instantaneous Grad projection rate, CI/RR/CX number rate는 서로 다른 객체다. reacting gas pi=0을 이 진단만으로 바꾸지 않는다.

HE87 최신 commit에는 HE35 finite-mass pseudo-Maxwell pair moments가 추가돼 있다. 입력 kappa는 호출자가 공급하는 m³/s model coefficient이며 empirical transport 채택은 없다. 일반 drift momentum/energy와 common-bulk STF matrix, 극단 질량비 repair를 완료했으므로 같은 대수 kernel은 재개발하지 않는다. 실제 finite-mass differential data와 reactive energy/STF source 및 physical closure는 열린 상태다.

## REC124/125: RR 열모멘트와 Compton 재사용

REC125의 실제 current HANDOFF/REPORT는 **THERM028IVP 완료**,3비교PASS,92.951497908s를 기록한다. PR본문의 pending 문구와 NEXT_DAG의 final-publication pending은 각각 기록 시점 상태다. current science files가 remote HEAD에 존재함은 관측했으나 final dual-backup 마감은 이 intake가 별도로 인증하지 않는다.

THERM02는5nominal compact34+2tight34+1full63 oracle, z20→2,193nodes,5–60eV GL4 continuum, T0=1000K다. REC124는 z7.9637 재시작/5–200eV/nativefull63/logT/109comparison nodes8개로 다른 cohort다. 실행 수 또는 speedup을 서로 합치지 않는다.

Mao-factor hybrid는 donor RR number rate를 그대로 쓰고 L_RR=kBT alpha_donor f_Mao로 kinetic loss를 구성한다. 전자factor6개를13 isotope RR channel에 대응한다. 이것은 독립적인 source-consistent 완전 RR rate/energy provider를 확보했다는 뜻이 아니다. 실제 photon monopole의 actual-hot thermal Compton과 별도 prescribed Planck reference bath는 exclusive branch다. UV moments는 실제272 GL4 nodes의 에너지 및 제곱에너지 moment로 고정해 RHS에서 재적분하지 않는다.

아직 열린 의무: actual grey field recoil/induced spectrum, radiation collision/Einstein energy backreaction, Li resonance final charge/state/energy partition. Total cross section을 final ionic yield로 바꾸지 않는다. Compton bath debit은 passive ledger이며 동적 spectral closure가 아니다.

## 핵물리와 일반 ledger: 이미 완료된 것과 다음 의무

REI221의 atomic sandbox는21 independent abundances, shared electronic blocks, exact electron-feedback Jacobian, supplied resolved unary/binary events, factorial symmetry, zero-aware derivatives, log flux와 explicit energy reservoirs를 이미 제공한다. 156baseline+별도2 source-onset checks는 생산자 완료 근거다.

같은 최신 HEAD의 `rei_coupled_local_flow_20261022`는 pureH Case-A RR의 evolving-T first integral와 escaped photon energy ledger, prescribed-T neutron beta+RR exact positive subflows/Strang/Bessel reference를 완료했다.103baseline+별도96출력검사, code SHAe32069af2f1e6178a62878bd77031f68b23379100ea74aaf83f2b67923df0c19를 재사용한다. Q_bare total release와 neutral convention Q0=Q_bare+dI, single beta owner 및 **총beta Q를기본heat로배정하지않는규칙**도 이미 있다.

REI219의18-family34directed-channel nuclear model은 all-bare, instant thermalization, passive fixed bulk의 조건부 sensitivity다. 충전핵종 S0 constant continuation 및 neutron1/v가 실제100–10000K의 실험 검증을 제공하지 않는다. D/T/neutron0은 원자 초기조건/선택연산자의 invariant property이며 실제 핵생성0의 증명이 아니다. 해당18family/DD 결과는 불변이고 이번에 재계산하지 않았다.

따라서 새 generic particle/Q ledger의 반복보다 **실제 source-resolved daughter branching, beta electron/neutrino/recoil energy partition, fast-product stopping/escape, 동일 isotope threshold와 PI/RR energy moments 결속**이 다음 유의미한 변경이다. manufactured event coefficient/Q0 검증을 물리 입력 완료로 승격하지 않는다.

toy_bbn은 main2026-01-24/student2026-01-23 고정의 교육용12reaction PRIMAT/REACLIB reference/table/surrogate와 units 모듈이다. README, PRIMAT 통합문서,9개 module 파일목록을 읽은 범위에서 범용 atomic↔nuclear mass/Q/particle ledger 완료는 확인하지 못했다. 노트북 전체 source를 감사하지 않았으므로 부재를 단정하지 않는다. 기본 T9범위[0.01,10]와 교육용 clamping은 HH 저온 source-domain 근거로 재사용할 수 없다.

## 다음 PHYS81 선택에 대한 권고

1. WU136 실제 HEAD951182dd에서 additive unit을 시작한다. WU135의 component는 별도 sibling source pin으로 유지하고 사전 근거 없이 merge하거나 다시 실행하지 않는다.
2. C22D의 H1 PL finite Maxwell kernel과 source bytes를 그대로 재사용한다. 새 source가 확보된 He/Li finite channels와 threshold/units/domain mapping, PHYS78 Tmax를 포함하는 새 선언 범위를 물리 단계에서 먼저 정한다.
3. 핵종 변환은 이미 있는 REI event ledger를 참조한다. 이번 atom CI 추가가 isotope-shared reduction 가정을 어디서 깨는지, ionic-potential 차이를 어떤 energy owner로 옮기는지 바뀐 의무만 닫는다.
4. He/LiCX, D matched PI/RR, recombination→z20 charge contract, Li inner-shell/branching/spectral contract는 계속 별도 OPEN이다.
5. 생산자 완성 과학 실행은 재사용한다. 새 검증/과학 실행/게시/백업/DAG 판정은 독립 장부로 기록한다. HH_R10=OFF, Production admission NOT_ISSUED를 유지한다.

## 파일과 오류 기록

- ALL_BRANCH_REFS.json:51repo/2175refs/63page 전체.
- REPOSITORY_SEARCH_PAGES.json: 실제2page 응답.
- SELECTED_REPOSITORIES_LATEST_PRS.json: 최근 PR 원 응답.
- SELECTED_ACTUAL_REFS.json: 직접 관련22개 PR pin과 일치.
- PRIOR_PHYS80_COMPARISON.json: 이전 comparable10ref와 fresh identity 비교.
- PINNED_TEXT_MANIFEST.json + handoffs/:40개 읽은 nonempty exact-head text/API metadata, bytes/SHA256/Git blob.
- FETCHED_TEXT_SNAPSHOTS.json / FETCHED_TEXT_SUPPLEMENT.json: fetch identity와 원 UTF-8 payload.
- 이번 전달은원격게시/백업을수행하지않은읽기전용 intake다. ROOT가새unit evidence로포함한다.

보존할 tool/intake 실패: 처음 큰 JSON을 단일 argv로 저장하려다 Argument list too long, chunked serialization로 교정했다. directory response가 empty라 PR files 목록으로 위치를 확인했다. 추정 경로 SOURCE_CONTRACT.md는404였고 실제 CONTRACT.json을 읽었다. prior comparison helper가 directory list에 dict.get을 시도해1회 실패했으며 type guard로 같은 저장 자료만 다시 처리했다. 이들은 과학 실행 실패가 아니다.
