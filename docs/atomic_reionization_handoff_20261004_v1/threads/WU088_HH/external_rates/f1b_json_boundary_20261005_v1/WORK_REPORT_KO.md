# HH-F1B JSON 입력 경계 수정 — 2026-10-05

새 F1B source reference의 CLI 입력에서 실제 두 결함을 재현하고 별도 continuation에서 수정했다. 같은 JSON에 provider나 chi_erg가 중복되면 원 CLI는 뒤의 값을 사용해 성공 출력(exit0)을 만들었다. 최상위가 null/list/string/int/bool이면 TypeError traceback(exit1)이 나왔다. 원 source/ZIP은 변경하지 않았다.

추가한 _unique_json_object는 모든 JSON object의 decoded key 중복을 거절한다. escaped provider key도 동일 key로 판정한다. 최상위 object 확인을 더해 두 경우 모두 기존 ProviderError 경로의 exit2로 종료하며 새 출력이 없다. 수치 evaluate/direction/inputs/interval 함수의 AST는 원본과 동일하고 hh_external.py bytes/SHA8c02df302adc895be1327cb2e55bae03ebed8ec06ee7496ff4eeda20fdcdc197는 보존됐다. 복제된 수정 source의 identity는 evidence/VERIFICATION.json에 따로 기록했다. valid JSON의 float 거절, 정밀도80, fit/geometry/chi/pair/3000K cutoff와 output create-only 정책은 그대로다.

신규 고유 CLI 검사4개를 원본에 먼저 실행했다. 중복model,중복provider,non-object root의3개 testcase에서 총8개 assertion/subcase 실패를 확인했고 valid-input parity testcase는 처음부터 통과했다. 수정본 GREEN에서는4개 모두PASS, failure/error/skip0이다. 두 named provider의 valid input+direction+dt 출력은 원 CLI와 전체 byte 동일하며 기존 출력 덮어쓰기도 거절했다. RED/GREEN은 각각14개의 CLI subprocess 사례를 호출했다. Git 설치 경로에서도 frozen sibling source의 SHA를 확인하고 같은4개를 최종 실행했다. 총42개 CLI subprocess 사례를4개 고유검사로 계수한다. 최종 검사는 Git parity 경로 및 입력 identity guard를 추가한 뒤 시행했다. 이들은 제조된 algebra fixture의 source reference 계산이다. 실제 HH native field callback/primitive 적분/소비자/history/NCP 실행은0이며 기존F1B24개/F1C20개/120scalar/14symbolic/measurement 또는 legacy suite를 재실행하지 않았다.

F1B 원 ZIP61822bytes/SHA35c32326413e6bd3d9e3804d70bf325c8c8450800e9d9e38d8d9644859cced73를 양provider metadata로 확인하고 cache 부재 뒤 Dropbox에서 한 번 회수했다. 원41payload/CRC와Git의src2개/tests2개 bytes를 대조했다. Dropbox 입력RESTORE_VERIFIED=true, Drive는metadata만으로false다. 원 archive는 content-addressed cache를 symlink로 사용한다. 이번 output 원ZIP embedding은 검증된 입력1개를 보존한 것이다.

HH 처음5731c27에서 도중53983df3ff0978ad5027432198ade35e4503990d(F1C)가 도착했다. cutoff 두-root/no-root의 새 정리와 exact box guard를 읽고 보존했으며 재계산하지 않았다. 이 guard와 본 JSON 입력 수정은 서로 다른 검사다. F1C guard를 호출하거나 consumer box/root를 인증하지 않았다.

REI 처음9daef2087cbd40d67d898f8de789f9f00386affe에서 hhe_events/microstep 전체bytes를 로컬 읽기증거로 회수했다. 각각 원F03 blob57a63eee1e9d8c4aa2b5ed663dbea15619359f71/3a78b40d1823a1e1c8541538bd94481b4cab0277 및 SHA와 일치한다. F1B의 과거 connector-only read를 이번 full byte read로 소급하지 않는다. 실제 F03 RHS/BE와 FLRW02 pointwise module이 있으므로 소비자부재라고 보고하지 않는다. 이후c433eaee7b120a5bfb7c35e802c4b218315bf210(FLRW03)의 새 stage-event/birth/expanding contract를 읽었고 전체ZIP restore나 독립재검증으로 주장하지 않는다. 그 작은coupled reference와 외부84tests는 받은결과이지 이번실행이 아니다.

Canonical HH-F1=WAITING_ON_REI_DOMAIN, HH-F2=NOT_INTEGRATED. 실제 REI-F07 HH domain/distribution/constants/단일process·threshold·heat·binding owner/seam/observable·numericalbudget 결속이 다음 입력이다. 지정 science_scenario_v1.json은 9daef208의실제조회에서404이고 이후REI 증분에는그경로가없었다. F03/F1C/FLRW03 synthetic input·온도guard를 HH physical domain으로 채택하지 않았다. F04 sparse nonlinear root/interval/remainder 작업은 별도pending으로 남긴다. 새 Bianchi/thermal/ODE/REC 코드나 duplicate campaign은 만들지 않았다.

원24/289,미상계265unbounded,epsilon_C/R=null,B22OPEN_UNDETERMINED,scientific/production admission=false를 보존했다. consumed6셀/FD1/FD2 registry,FD2proposal/RETURN,B22 raw057/105 claim의7개 exactrefs를 size/SHA/mode/mtime/PIDbytes로 대조했다. marker로process원인을추정하지않았다. 원backend/worker/source/DB/PREPARED/실패tree와다른repo변경0이다.

동기화는사용자대상ChatGPT thread https://chatgpt.com/c/6abf9e0b-74c0-83e8-8170-aaa51b03415e 와같은HHbranch의 active-turn Git 인계다. 현재webcmd CLI와conversation browser tool이없어직접대화읽기/전달은UNDELIVERED다. Pages/다른스레드를대체로사용하지않고background감시도시작하지않았다. 최종Git/backup ACK는detached DELIVERY_RECEIPT에기록하며ACK+metadata와remotecontentRESTORE는구분한다.
