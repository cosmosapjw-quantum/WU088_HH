# R14 production 저자 수동 검토 — 실행 전

이 기록은 코드 저자의 정적·수동 검토다. 과학 실행 결과, 독립 심사 PASS, 채택 판정이 아니다. Production/reference/old module import, compile, primary 실행, ODE, CAS는 각각0이다. 별도로 수행한 `author_fixed_inputs.py`는 수동으로 정한 rational text의 JSON 반복 확장·binding metadata·SHA 직렬화만 처리했다. 모델, primitive, root, weight 또는 fixture 기대값을 계산하지 않았다.

## 코드와 식의 결속

`quadratic_convolution.py`는 원래 source B2 triplet의 endpoints와 convex strict-interior minimum을 exact 검사한다. Signed middle coefficient를 그대로 허용한 뒤 gr/ge 모든 rational vertices를 union한다. `_restrict`의 de Casteljau 분할로 effective B2를 얻고 positivity를 확인한다. 원래 canonical forcing hash는 이 effective 표현으로 바꾸지 않는다.

Base event set은 effective knots+k*tau와 observations의 exact union이다. 원래 t0 이후 전체 history를 유지한다. 각 base/effective-source/age-strip 조합의 loop count와 최대192 root iterations/base를 coefficient 또는 derivative-root 구축 전에 precharge한다. 각 셀의 Simpson positive B3를 한번 구축한다. Endpoint F, 실제 R, right left limit, polynomial output, rootboxes 및 whole-cell output은 같은 저장 coefficients를 사용한다.

Normalized derivative의 degree reduction, rational vertex로 나눈 monotone branches, endpoint zero, double vertex zero, strict-sign branch의96 midpoint bisections를 구별했다. Bisection exact-zero 발견 시 해당 마지막 평가를 actual step에 포함한다. Unresolved rational root도 유한 box로 남을 수 있으며 irrational 여부를 허위 판정하지 않는다. Critical times는 E clock에 삽입하지 않는다.

Whole-R에는 exact endpoint/left-limit/critical candidates 및 rootbox de Casteljau hull을 사용한다. `M_B=3 max|B[i+1]-B[i]|`, gap<=M_B*2^-96 및 dyadic 확장<=2*2^-128를 서로 다른 출력으로 남긴다. Closed observation sup는 local max를 취한다. Supremum lower witness가 right left limit인 경우 실제 attained endpoint와 구분한다.

Positive B3 beta series는 분모 `(n+4)`, `(n+3)(n+4)`, `(n+2)(n+3)(n+4)`, `(n+1)(n+2)(n+3)(n+4)`와 분자1/3/6/6을 사용한다. 고정 Taylor96의 geometric exponential tail을 네 moment에 보수적으로 적용한다. Signed d는 exp(z)와 positive-moment reversal로 처리한다. `phi`는 네 weights의 합이다. d=0은 exp=1 및 각 weight=duration/4의 outward interval로 reduce한다.

E endpoint는 polynomial forcing으로 전파한다. Whole E에는 exact R sup upper와 ge positive quadratic hull을 사용하는 constant-forcing majorant를 쓴다. Whole upper는 left endpoint upper, polynomial right endpoint upper, majorant right upper의 max다. 다음 셀에는 polynomial endpoint interval을 넘긴다. 따라서 과도하게 느슨한 whole bound가 endpoint history를 덮어쓰지 않는다.

## 자원·identity 검토

공개 입력256bit, derived rational16384bit, original source16, observations32, effective48, base512, full blocks8, |d|*horizon<=16을 별도 검사한다. 상수250000/98304 aggregate guards는 individual count guards 아래 보수적이다. Primary의 직접 work-budget helper 검사는 실제 accepted source가512base cells를 만들었다는 주장으로 쓰지 않는다. 전체 full-capacity case는16 original/32obs/48effective/tau2/17/B8로 별도 고정했다.

모든 분수 arithmetic은 새 module의16384bit checks를 통한다. R13의8192bit helper를 import하지 않는다. R13 source/state/clock/certificate binding 구조를 `WU_R14_WHOLE_FORCING_V1`로 명시적으로 갱신했다. SHA는 declared source 함수의 identity이며 실제 물리 forcing 상계의 증명으로 승격하지 않는다. Primary는 실제 `FIXTURE_SOURCE.json` 바이트의SHA와31개 원래 payload를 대조한다.

## 의미 있는 고정 controls

31valid cases와43guard cases를 고정했다. 독립 수동 exact controls에는 s²/affine/constant reduction, 음의middle 허용, 서로 다른vertex union과동일vertex dedup, 하나/두 개 irrational extrema, golden discriminant, double root, endpoint roots, linear derivative root, constant polynomial, initial jump, 전역 memory 및 fresh q0 forcing이 있다. 정렬을 달리한 source/observation refinement는 exact R 및 E interval overlap으로 비교한다. Signed d의±16·nearzero, shifted t0, discontinuous sources, nearcoalescent/nearboundary roots, full48capacity를 포함한다.

Primary에서 surd sup는 Decimal 근사 대신 고정된 `a+b*sqrt(n)` 기대값을 exact square comparisons로 검사한다. Production coefficients를 복사해 기대값을 만드는 방식은 쓰지 않는다. Guard는 부정 source, 잘못된shape/types, bit/cell/block 한도, source/state/clock/hash/full-A/whole-domain premise mismatch, cap 부착을 거부하도록 고정했다. Code-derived structural invariants와 hand-derived analytic checks는 결과에서 별도 IDs로 남긴다.

## 초안 교정과 남은 단계

Reference 작성자와 API 조율 중 `nonempty_overlap_terms`를 positive-weight active count 대신 모든 geometric nonempty overlap count로 맞췄다. q^k=0이나 sourcezero도 geometry count에는 포함한다. Full loop precharge/실제 mathematical coefficients/전파 결과의 정의는 바뀌지 않았다. 이 교정 전에 과학 실행은 없었다. 교정 provenance는 `DRAFT_CORRECTIONS.json`과 저장한 source snapshot에 있다.

남은 단계는 root의 정적 통합·실행 파일 및 입력 freeze·S05 게시/백업 이후 허용된 단1회 primary 및 별도 reference, 독립 proof/code 심사다. 이 저자는 root의 명시 실행 허가 전에는 import/compile/실행하지 않는다. Physical INPUT_PENDING, HH_R10=OFF, production=NOT_ISSUED, L4=false, central/physical delta0은 그대로다.
