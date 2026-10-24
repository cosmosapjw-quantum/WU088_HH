# PHYS86 독립 C9 실제 raw 결과 검토

## 판정과 실제 결과

**PASS_SCOPED.** 기존 정적 C9를 이어서 두 whole raw tool response와 exact payload 및 certificate를 직접 읽었다. PHYS85 보존 core의 새 compact reference는 **36 events, 6 ensembles, 23 guards, 1,017/1,017 assertions**를 완전 반환했다. 새 finite exponential-family reference는 **3 q rows, 10 guards, 82/82 assertions**를 완전 반환했다. 실패 label은 양쪽 모두 빈 배열이며, 검사한 exact residual은 모두0이다. 수정이 필요한 P0–P3 finding은 없다.

이 판정은 고정 rounded mass inputs의 supplied-event reference와 고정 finite witness, 그리고 실행한 symbolic identities의 범위다. Root가 최종 과학적 채택·게시를 결정한다. 정적 검토와 execution-transition amendment 기록은 그대로 보존했다. 새 provider ACK 및 최종 whole-archive restore 의무의 완료를 이 과학 검토로 발급하지 않는다.

## 1. 원자료·request identity·전송

실행 GO는 `reviews/ROOT_EXECUTION_GO.json`이고 S1 source commit은 `280ef5094dd56b76ce4f5dc8f8aad7bc36172728`, tree는 `435ef54285fe1a2690cc75a9791e77e553cbe4ea`다. 두 attempt의 실제 TOOL_REQUEST_ARGUMENTS bytes를 동결 implementation request와 대조해 동일함을 확인했다.

| 실제 관측 | Recovery | Moments |
|---|---|---|
| Tool dispatch UTC | 04:44:59.979 | 04:45:37.578 |
| Tool return UTC | 04:45:15.522 | 04:45:48.070 |
| Whole raw JSON bytes | 5,698 | 6,179 |
| Exact payload p bytes | 3,791 | 2,703 |
| 실제 escaped Out string bytes | 4,512 | 4,047 |
| Tool isError | false | false |
| Actual runtime status | PASS | PASS |

두 whole raw의 `Out[1]` string을 직접 JSON decode하고 payload SHA/byte length, EXACT_PAYLOAD.txt bytes 및 COMPLETE_CERTIFICATE 객체 일치를 확인했다. 기존 parser summary만을 근거로 삼지 않았다. 실제 ASCII escaped string 길이는 각각8,000 이하이며 완전 envelope의 종료와 SHA를 확인했다. 중간 slice·truncation 또는 누락된 후반 결과를 채워 넣지 않았다.

Recovery raw SHA256은 `b0d2fc68cd3f142585d4227258bc1de527b3cf86659266d877ba7b85c7591d7c`, payload SHA256은 `003a6421a2cc3705b845eae9197fc151a71d1f4ed8b2e590f65c02451e49c338`다. Moments raw SHA256은 `d7199f23d97e3838712c60ce7383e873a4b117c84d04e338c1b5cf000e362de5`, payload SHA256은 `8674e201118bba54ee1d13699f048347af8455c063b0257a786aeec8a98560a7`다.

## 2. PHYS85 actual certificate

Actual bitstring 길이는1,017이고 전부1이다. Actual label SHA `2c238591e544c5c805d5af5a73d4c14ab3d4af2aa2bef9d0c15e464f4ee47add`는 이전에 원래 verifier loop와 대조한 source_data label order의 SHA와 일치한다. Counts는 {36,6,23,1017,1017}, complete=true다.

9개 exact (Kin,Kc,Egamma) triple의 27개 유리수 원문과 세 exact covariance를 모두 읽었다. Triple 순서는 np_dgamma, nd_tgamma, pd_hgamma 각 채널 내 noncold_1, noncold_2, noncold_3이며 동일한 route/owner 중복을 projection에서 제거한 declared order와 일치한다. 9개 triple은 서로 구별되고 모두 양의 유리수다. 세 covariance는 channel 순서의 양의 nonzero 유리수다. 원래 source/oracle 결과를 다시 수치계산하거나 재생성하지 않고, 보존된 verifier의 실제 zero residual·strict assertion과 연결해서 검토했다.

36개 actual event sum-absolute residual과6개 actual ensemble sum-absolute residual은 모두 integer0이다. 정적 검토에서 확인한 절댓값 합이므로 signed cancellation을 성공으로 읽지 않았다. Source/oracle kinematics, owner energy/count, boost/shell 및 incidence 비교와 원래 symbolic checks의 strict exact-zero bits가 완전하다.

23개 actual Failure tag를 원래 guard 순서와 직접 대조했다. Unknown channel1, exact-rational rejection3, event-domain rejection6, missing-field3, conflicting-owner2, invalid-route1, empty/length ensemble2, weight rejection3, mixed-channel1, mixed-route1의 actual ordered sequence가 원래 branch와 일치한다. Missing owner와 missing route, zeta-only/conflicting owner, nonnormalized/inexact/negative weights가 각각 지정한 guard에 대응한다. Failures=[]이다.

이 결과는 새 실행의 첫 완전 compact certificate다. 이전 두 raw attempt는 보존되며 과거 truncated report를 복구했다고 해석하지 않는다.

## 3. Finite moment actual rows

Moment vector의 순서는 {kappa, meanA, meanB, meanS, varS, selection, curvature, meanH, jointHKc, covHKcS}다. 다음 값은 actual certificate에서 읽은 exact values다.

| q | kappa | meanA | meanB | meanS | varS |
|---|---|---|---|---|---|
| 1/2 | 31/18 | 5/2 | 38/9 | 220/31 | 828/961 |
| 2/3 | 149/77 | 18/7 | 48/11 | 1098/149 | 22752/22201 |
| 3/4 | 418/205 | 13/5 | 182/41 | 1566/209 | 46866/43681 |

| q | selection | curvature | meanH | jointHKc | covHKcS |
|---|---|---|---|---|---|
| 1/2 | 209/558 | 67423/311364 | 19/31 | 54/31 | 24/961 |
| 2/3 | 4980/11473 | 24335628/131629729 | 90/149 | 252/149 | −8496/22201 |
| 3/4 | 19443/42845 | 270964284/1835694025 | 123/209 | 18/11 | −1260/2299 |

선택 평균과 분산은 유한 positive-support witness의 domain에 있고 covariance의 부호 변화도 그대로 보존된다. Covariance에 불필요한 양성성 기준을 추가하지 않았다. 각 q점의15개 actual partition/moment residual은 모두0이다. 이15개에는 각각의 one-particle variance도 들어가므로 compact vector에서 생략된 varA와 varB도 독립 polynomial oracle과 비교한 strict actual assertion에 포함된다.

세 formal retained-daughter source coefficient residual은 모두0이다. Rate, uC, Cv를 formal independent symbols로 유지한 기존 verifier의 결과이며 physical rate 또는 daughter EOS를 추정하지 않았다. zero.rate, zero.source, zero.before_means bits도1이다. 원래 source의 Cv guard 선행 및 R=0 early-return 의미가 보존된다.

Actual qG 결과는 다음과 같다.

| q | qG slope | explicit correction | 보정 없는 residual |
|---|---|---|---|
| 1/2 | 767/558 | 1 | −1 |
| 2/3 | 16453/11473 | 1 | −1 |
| 3/4 | 62288/42845 | 1 | −1 |

세 corrected-kernel assertion과 measure-unchanged assertion은 모두1이다. 보정 없는 residual은 실제로−1이므로 판별 control은 비자명하게 작동했다. Source selection은 위 slope에서1을 뺀 값과 일치하는 exact assertion을 통과했다.

82개 actual label을 고정 verifier 순서와 전부 대조했고 누락·중복·재정렬은 없다. 10개 actual guard pair는 q domain3, positive base weight2, kernel1, membership1, nonpositive Cv2, negative rate1의 명시된 expected Failure tags와 일치한다. 8개 symbolic residual은 ratio derivative, partition mean, heat capacity, NR u, NR Cv, NR source, constant sigma 및 inverse-speed 순서로 모두 integer0이다.

## 4. 실제 warning의 보존과 영향 범위

양쪽 raw에 `Symbol::undefined2` 및 `General::messages`가 있다. Moments raw에는 추가로 **`Infinity::indet`의 `(0*Infinity)` 메시지가 두 번** 있다. Warning-free run으로 보고하지 않는다. 이 메시지들의 정확한 내부 발생 위치는 현재 raw로 국소화되지 않았으며 그 원인을 추정하지 않는다.

그럼에도 최종 admitted fields에는 Indeterminate, Infinity, unevaluated residual 또는 Failure가 남지 않았다. Required residuals는 실제 integer0이고, verifier가 Together[value]===0 및 TrueQ로 기록한 전체82 bits와 symbolic8 residual이 완전하다. 따라서 내부 warning 위치 미확정과 반환된 exact reference 결과의 scoped validity를 구별한다. 이 판정의 목적은 지정한 exact certificate의 수용이며 경고가 없다는 주장이나 일반 CAS 안정성 보증이 아니다. 경고를 지우기 위한 새 evaluator 호출·rerun은 수행하거나 요청하지 않는다.

## 5. 채택 가능한 결론과 명확한 경계

이번 actual 결과는 (i) 고정 displayed mass values에 대한 PHYS85 supplied-event normal-frame energy/count/owner reference, (ii) 고정 finite exponential-family의 선택·variance·covariance·retained source 및 T-dependent kernel correction interface, (iii) 실행한 symbolic Juttner recurrence·heat-capacity·NR identities의 scoped implementation verification을 지지한다. 이론의 명시된 가정 아래 derived 지위는 기존 R6 근거와 연결된다.

Actual q fixture는 physical capture event나 Maxwell–Juttner continuum quadrature가 아니다. Physical finite-T nuclear cross sections/rates, stopping, coupled ODE 또는 spectral trajectory, 안정한 production finite-precision Bessel implementation, continuum integration certificate 및 consumer admission은 발급하지 않는다. 고정 질량의 exact arithmetic을 exact physical masses나 uncertainty certificate로 확대하지 않는다.

Observed runtime은 두 결과 모두 Wolfram `15.0.1 for Linux x86 (64-bit) (July 2, 2026)`, SystemID `Linux-x86-64`다. Requested worker model과 observed backend UNOBSERVED를 구별하며 remote hardware/scheduler를 추정하지 않는다.

## 6. 호출 장부와 마무리

두 request는 순차적으로 각각1회 실행되었다. 새2회+과거2회=누적4회이며 retry/probe0, local scientific child0, ODE0, physical rate0, stopping0이다. 이번 reviewer는 기존 raw를 읽고 JSON/byte/hash/label/record를 비교했으며 scientific evaluator, 수치 계산 또는 campaign을 다시 실행하지 않았다.

C9 actual-raw 의무는 이 scoped 결과로 완료한다. Root는 이 판정과 실제 근거에 따라 게시·handoff를 완료하고, 별도로 pending stage ACK와 final 양쪽 whole ZIP restore 및 JSON readback을 처리한다. **HH_R10=OFF; production admission=NOT_ISSUED.**
