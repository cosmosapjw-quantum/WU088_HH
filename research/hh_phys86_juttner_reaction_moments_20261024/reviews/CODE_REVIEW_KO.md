# PHYS86 독립 C9 코드 정적 검토

## 판정

**PASS_STATIC_SCOPED_GO_EXECUTE_REQUEST.** 동결된 두 request의 정적 검토를 완료했다. 수정이 필요한 P0–P3 finding은 없고, 실행 요청을 controller에게 돌려보낸다. 실제 실행은 S1 게시 및 Drive·Dropbox ACK를 확인한 뒤 root가 정확한 request에 GO를 발급하는 기존 순서를 따른다. 이 판정은 runtime PASS나 과학적 구현 채택이 아니다. 두 actual raw 결과를 받은 뒤 이 C9 검토를 이어서 완료한다.

확인한 freeze manifest SHA256은 `194e948efd03baee8fe28475a222a156fe94e87d13937a8e11e535a43651f8d2`다. Recovery request SHA256은 `3db65d4d22e610b6f8d7b1903ebaf2108a73499de6cdaa44312470cfa4c237e9`, moments request SHA256은 `41e06202ad710758187c8f771e460c5b29e28a740c91f86f64ec27e44597230d`다. Root가 이 최종 freeze를 확인했다.

## 검토의 독립성과 방법

검토자는 이 source, verifier, wrapper 또는 transport를 설계·구현하지 않았다. 지정된 내장 1.0.0 RESEARCH_POLICY, EVIDENCE_AND_HANDOFF, CODING_LOOP와 실제 rei_bianchi AGENTS.md의 tiered delegation·execution-transition·typed-identity 정책을 읽었다. 전체 CONTRACT, 전체 이론, R6 보고서, 보존 PHYS85 core, 새 source와 verifier, 두 wrapper, 공통 transport, parser, static checker, assembler 및 source_data의 생성 순서를 읽었다. 요청된 reviewer 역할은 fresh Astra이며 실제 backend identity는 UNOBSERVED다.

방법은 원문 식과 source의 직접 대조, 독립적인 기호식 부호·계수의 수작업 추적, loop/order의 정적 추적, read-only byte/hash/JSON metadata 비교다. 과학 Python 계산, 수치 계산, Wolfram/CAS, parent kernel 또는 local scientific child는 실행하지 않았다. Metadata 비교로 manifest의 15개 파일, 두 request의 정확한 코드 결합과 timeConstraint=60, immutable parent input 및 보존 core, CONTRACT와 이론의 SHA를 확인했다. 구현자의 static checker 결과도 읽었으며 이를 Wolfram syntax 실행 또는 runtime 근거로 바꾸지 않았다.

## PHYS85 새 완전 compact certificate

원래 repair01 소스의 wrapper 이전 25,893 bytes가 정확히 보존되어 있다. 새 recovery code는 이 prefix에 transport와 새 projection만 덧붙인다. 원래 event owner, independent four-vector oracle, 36개 사건·6개 ensemble·23개 guard 및 symbolic verifier를 변경하지 않았다. Frozen input의 byte identity도 일치한다.

원래 assertion 순서를 configure/fixture 2개, 사건 36×24개, 사건 수 1개, ensemble 6×13개, ensemble 수 1개, route 36개, guard 23개, symbolic 12개로 추적하여 1,017개를 확인했다. 실제 $checks의 bitstring 및 newline-joined label SHA를 내보내므로 예상 성공 bits를 새로 만드는 방식이 아니다. Expected label-order transcription은 원래 loop의 채널·fixture·owner·route 및 assertion 순서와 일치한다.

Triple projection의 row indices {1,5,9,13,17,21,25,29,33}은 channel-major/fixture-minor 순서의 9개 고유 kinematic triple이다. Covariance indices {1,3,5}는 세 채널의 첫 route다. 원래 각 route의 covariance가 검증되므로 이 3개 projection은 명시된 declared order와 일치한다. Event residual은 source/oracle energy·count 차이, 실제 closure/incidence, kinematics 및 oracle shell/boost residual의 절댓값 합이고 ensemble residual도 실제 source/oracle와 closure의 절댓값 합이다. 상쇄로 잘못 zero가 되는 signed sum을 쓰지 않는다. 원래 1,017 bits가 나머지 검증 의무도 보존한다.

23개 guard tag는 실제 Failure 객체에서 뽑고, 실패 label 및 completion 상태도 실제 실행에서 가져온다. Completion에는 PASS, 정확한 count 및 label-order match가 함께 필요하다. 이 결과는 새로 수행한 원래 core의 첫 완전 compact certificate이며 이전 truncated raw report 복구라는 주장은 없다.

## 새 finite moment source와 독립 oracle

Source는 두 one-particle weight와 event kernel을 직접 합산한다. Verifier는 독립적으로 명시한 Za, Zb, N 및 membership/daughter polynomial을 미분한다. Source의 mean/variance/covariance를 oracle 기대값 구성에 다시 사용하지 않는다. 네 pair의 순서, h 및 hKc polynomial이 고정 2×2 입력과 일치한다.

Selection은 meanS−meanA−meanB이고 q d_q log(kappa)와 비교한다. Curvature는 event variance에서 두 one-particle variance를 뺀 값이며 q d_q(q d_q log(kappa))와 비교한다. Covariance는 joint hKc moment와 S의 중심곱이며 q d_q mean(hKc)와 비교한다. 이 부호는 d_b=−q d_q와 이론에 일치한다.

Caloric source coefficient는 {−meanS+meanA+meanB+mean(hKc), −mean(h)}이며 formal uC, rate, cv를 보존한다. Verifier는 독립 partition 식에서 만든 source와 계수 identity를 비교한다. Physical daughter EOS나 rate를 임의로 수치화하지 않는다. Zero kernel은 N=kappa=0, undefined normalized moments와 source0을 반환한다. Density-driven R=0의 source 경로는 normalized moment field 접근 전에 0을 반환하며 nonpositive numeric Cv rejection이 먼저다. T>0는 finite family의 epsilon0>0, 0<q<1 및 명시된 formal source domain에서 유지된다.

qG control은 kernel만 바꿔 event moments를 다시 계산한다. Slope는 한 단위 증가하고 explicit kernel correction은 그 증가분을 빼므로 corrected residual은 zero여야 한다. 보정 없는 residual은 nonzero여야 하며 measure-unchanged 검사도 있다. 이는 실제 capture event kinematics를 새 q fixture에 부여하는 검사가 아니다.

Bessel derivative/recurrence로 ratio derivative, partition mean, heat capacity를 검사하고, 명시한 large-z coefficient series에서 NR u와 Cv 및 세 source reductions를 검사한다. Stable production Bessel numerical implementation이나 continuum quadrature를 이 검사에 포함했다고 주장하지 않는다.

Assertion 수는 q점마다 positive 1, partition/moment residual 15, source 1, kernel corrected 1, unchanged measure 1, wrong nonzero 1로 20개다. 세 q점의 60개에 campaign/zero-source 4개, guard 10개, symbolic 8개를 더해 82개가 된다. Guard의 expected tag와 실제 tag를 비교한다.

## Transport와 실제 결과 검토 경계

ExactJSON은 유리수를 numerator/denominator string으로 보존하고 integer·boolean·string을 유지한다. Transport는 compact payload p의 정확한 bytes와 SHA를 envelope에 결속한다. 전체 envelope의 ASCII 여부와 한 번 더 JSON string으로 escaped한 실제 길이 ≤8,000을 runtime에 검사한다. 크기 초과는 명시적 OUTPUT_TOO_LARGE이고 truncation·probe·split이 없다. 정적 검토는 실제 유리수 출력 길이 또는 성공한 전송을 주장하지 않는다.

Parser는 raw tool object에서 완전 envelope를 추출하고 exact payload hash/length, escaped bound, count/bits 및 기본 residual 상태를 확인한다. 문서대로 transport/scope checker이며 최종 과학적 판정자는 아니다. 계속되는 C9에서는 actual raw, exact payload, 9 triples, 3 covariance, 36+6 residuals, 23 guard tags, 82 labels/3 q rows/10 guards/8 symbolic residuals, wrong-control 값과 corrected result를 실제로 읽는다. Parser의 PASS만으로 그 의무를 대체하지 않는다.

## 예산과 다음 실행

과거 PHYS85 호출 2회와 그 잔여 cap0은 보존한다. 새 recovery 1회와 새 moment 1회, 각각 outer60초/inner55초만 허용하는 계약을 확인했다. 현 계획의 누적 상한은4회이고 optional probe0, automatic repair0, parallel kernel0, local scientific child0다. Local reserve1.5GiB+job0.5GiB는 바꾸지 않는다. 금액 장부 null은 확인되지 않은 값으로 유지한다.

**다음 행동:** S1 게시·양쪽 ACK 후 root exact-request GO → prescribed recovery 및 moments 실행과 전체 raw 보존 → 같은 C9의 실제 결과 검토. 구체적인 실패가 생기면 해당 원자료와 영향 의존성을 root에 돌려보내며 자동 재실행하지 않는다.

HH_R10=OFF, production admission=NOT_ISSUED. 실제 nuclear rate, stopping, thermochemical/spectral ODE, physical finite-T table 및 continuum certificate에 대한 채택은 이 검토 범위에 없다.
