# PHYS85 독립 C9 코드 검토

최종 C9 판정은 **STATIC_IMPLEMENTATION_PASS_SCOPED_REFERENCE_NOT_VERIFIED**다. 물리 계약에 대한 구현·oracle의 정적 검토는 제한된 범위에서 PASS이며, 첫 namespace 연결 문제를 수정한 두 번째 호출은 계산된 결과 조각을 반환했다. 그러나 실제 raw 응답의 중간이 생략되어 완전한 reference report를 읽을 수 없다. 따라서 **새 reference 과학 완료는 NOT_VERIFIED**, `EXACT_REFERENCE_IMPLEMENTATION_VERIFIED` 채택은 하지 않는다. 계약의 초기 호출 1회와 단 한 번의 repair 호출을 소진했으므로 추가 계산·probe·재실행 없이 불완전한 증거 checkpoint를 정확히 표시해 게시할 수 있다. 아래에는 초기 정적 판정, 첫 실패, 수정 승인, 실제 최종 결과를 순서대로 보존한다.

## 검토 범위

실제 S1 HEAD `04be89e24401966770d137b115c73f66b563ef5d`, tree `20a4875a05a543a8547cf7524e2425d78817f453`의 revision2 계약, 세 WL 파일, frozen inputs, 실행 인자 및 동결 manifest를 읽었다. 새 diff는 두 연구 단위 안의33개 additive 파일이며 부모 파일의 수정은 없다. 9개 동결 파일이 manifest와 일치하고, 요청 code가 assembled WL 원문과 일치함을 bytes/metadata 수준에서 확인했다. 이 확인은 수치 실행이 아니다.

## 코드 판정

정확 유리수의 normal-frame photon/daughter boost와 초기 pair kinetic debit이 계약 식을 구현한다. Binary daughter owner가 thermal 입자수 h−2, fast 입자수1−h, electron0을 결정한다. 여섯 에너지 owner 중 방사 destination은 하나이며 emitted diagnostic은 별도 추가 에너지가 아니다. Ensemble은 joint mean(h Kc)를 유지한다.

검증기는 생산 helper의 결과를 같은 closure식으로 다시 합산하는 것에 그치지 않고 독립적인 두 four-vector의 boost matrix, daughter mass shell, photon null, 전체 에너지·운동량 및 A/Z incidence를 검사하도록 작성되어 있다. NR rate-slope 항은 thermal energy debit과 particle number를 직접 EOS chain rule에 대입하여 확인하며, covariance 항은 centered weighted product와 비교한다. 이 검증 범위는36개 조건부 사건과6개 ensemble 및 명시한 symbolic/guard controls에 한정된다. 임의 입력의 continuum 구현 certificate나 물리 질량 uncertainty를 뜻하지 않는다.

초기 정적 검토에서 물리식·oracle 수학의 차단 사항은 관측되지 않았다. 이후 runtime namespace 연결 실패와 수정을 아래에 기록한다. Frozen inputs의 과거 requested-model 설명은 현재 ROLE_RECEIPT/EXECUTION_REQUEST의 실제 root 요청 gpt-6.1-sol/high/fork_none 기록보다 앞선 metadata다. 이 annotation 때문에 동결 숫자 입력을 바꾸거나 과학을 다시 실행하지 않는다.

## 초기 실행 전에 설정한 판단 기준

실제 raw Wolfram 응답과 디코딩된 보고서의 완전성,36/6 행, assertions·guards·symbolic 결과, source/request identity, 실패·timeout 여부를 읽은 뒤에만 `EXACT_REFERENCE_IMPLEMENTATION_VERIFIED` 판정이 가능하다. Physical finite-T source supplier, actual nuclear rates, fast stopping, consumer/production admission은 그대로 OPEN/NOT_ISSUED다. PHYS84 local lease WAIT를 이 cloud reference가 대신하지 않는다.

검토자의 새 numerical child/Wolfram/old callback/lease/원격 mutation/source edit는 모두0이다. HH_R10=OFF, production admission NOT_ISSUED를 유지한다.

## 첫 실제 응답과 한 번의 제한 수정 승인

첫 실제 Wolfram 호출은 transport `isError=false`였지만, `reference_report`가 association/report가 아니라 평가되지 않은 `PHYS85RunVerification[...]` 문자열이었다. 원문10,477bytes, 디코딩 보고서6,764bytes와 attempt receipt를 읽었다. 반환된 구조화 event/ensemble/assertion행은0이고 COMPLETE는 없다. 이 결과를 성공한 계산이나 물리식 실패로 분류하지 않는다. 초기 정적 검토는 단일 compound expression에서의 context 연결 문제를 잡지 못했으며, 실행 전 PASS를 runtime PASS로 승격할 수 없었던 이유가 실제로 드러났다.

분류는 **IMPLEMENTATION_ENTRYPOINT_NAMESPACE_BINDING_FAILURE**다. [Wolfram 공식 context 설명](https://reference.wolfram.com/language/tutorial/ModularityAndTheNamingOfThings.html)은 complete expression의 symbol name 해석이 실행보다 먼저 이루어지고 `Begin`의 영향은 후속 complete expression에 적용된다고 설명한다. 전체 파일을 한 code expression으로 합친 뒤 일부 entrypoint만 명시적 `PHYS85Verify` context로 호출하는 현재 조립 방식과 관측된 미평가는 이 원인에 부합한다.

**GO_ONE_TARGETED_BINDING_REPAIR**: 새 `implementation/repair_01/`에서 trusted source/verifier의 context directive8줄만 제거하고, wrapper의 명시적 `PHYS85Verify` prefix3곳을 같은 flat entrypoint 이름으로 바꾼다. 이름 공간을 평탄화해도 source와 verifier의 helper 이름은 충돌하지 않는다. 원본9동결파일·첫 실패를 그대로 보존하며, 물리식·입력·검증 수학·guard·출력 schema·시간 cap은 바꾸지 않는다. 낮은 tier가 구현하고 기존 계약의 **추가 호출1회** 범위에서 실행한다. 별도 runtime probe나 새 테스트 캠페인은 필요 없다. 실제 수정 diff와 원시 결과를 읽은 뒤만 최종 scoped admission을 판정한다.

검토자는 이 수정도 직접 구현하지 않았고 새 WL/수치 계산을 실행하지 않았다.

## 실제 repair diff 검토

`BINDING_ONLY_REPAIR.diff`와 `REPAIR_RECEIPT.json`을 직접 읽었다. source/verifier context directive 8줄 제거와 wrapper entrypoint prefix 3곳 제거만 있으며 나머지 code는 그대로다. 원본 9개 동결 파일과 첫 실패는 보존된다. 이 수정의 code SHA256은 `4e7562541499c15b8ec64c2818a39180c2ec677adeb2f60ccaadf563ea8a2afd`, tool arguments SHA256은 `7bc8551b9b30afd1f91d85ef69933fe1860c4d191541926aa0cc2b5a9dd4d57f`, diff SHA256은 `9d81ef389ad64f0093cc73a5ecf65914fa3a755fc7257705eb2b02adaa3d5d78`다.

**PASS_BINDING_ONLY / GO_ONE_TARGETED_BINDING_REPAIR_EXECUTION**. 수식·숫자 입력·guard·oracle 수학·schema·55/60초 cap은 변경되지 않았다. S1R 및 양쪽 ACK 후 한 번 실행하고 실제 결과를 검토한다. 이 승인은 실행 완료나 science PASS를 뜻하지 않으며 추가 자동 재시도는 승인하지 않는다.

## 두 번째 실제 결과와 최종 판정

`results/attempt_02/RAW_WOLFRAM_RESPONSE.json`, `ATTEMPT_RECEIPT.json`, `OUTPUT_PARSE_FAILURE.json`, `EVIDENCE_MANIFEST.json`을 직접 읽었다. raw·receipt·parse-failure 파일의 실제 bytes와 SHA256은 manifest와 일치한다. 실행 preflight의 S1R HEAD는 `1a8f98719fd3ec87d3acbfb27aeda9936b0bc613`이다. 원본 9개 동결 파일·첫 실패·repair 입력의 유지와 양쪽 S1R ACK는 root가 보존한 실행 receipt에 명시되어 있다.

Wolfram transport는 `isError=false`이며, raw에는 text block 하나와 `structuredContent=null`만 있다. 실제 text 길이는 10,239자다. `status=PASS`, `guard_count=23`, `failures=[]` 문자열이 보이지만, exact rational의 문자열 중간에서 ` ... `로 생략된 뒤 다른 guard 문맥으로 이어진다. 이는 표시가 짧게 보이는 문제가 아니라 저장한 raw bytes 자체의 생략이다. 정상 JSON report로 디코딩할 수 없으며 누락된 사건·ensemble·assertion 구조를 복원할 근거가 없다.

| 구분 | 최종 판정 | 범위 |
|---|---|---|
| 동결 식·입력 계약과 구현의 정적 일치 | PASS_SCOPED | exact event owner, 독립 oracle 설계, 별도 조건부 NR theorem |
| 첫 namespace 연결 수정 | entrypoint 평가 관측 | 두 번째 raw의 실제 event/oracle/guard/symbolic 조각이 평가 진입을 보여 줌 |
| 완전한 실제 reference 결과 | NOT_VERIFIED | 36개 사건·6개 ensemble 및 전체 assertions를 실제 report로 확인하지 못함 |
| 실제 검증된 event/ensemble/assertion/guard 수 | `null` | 알 수 없는 수를 0 또는 계획값으로 대체하지 않음 |
| 보이는 PASS·guard 23·failures [] | 원문 조각으로 보존 | 완전한 결과 검증이나 완료 근거로 승격하지 않음 |
| 추가 repair/probe 예산 | 0 | 총 tool 호출 2회: 초기 연결 실패 1회 + 제한 수정 1회 |
| incomplete checkpoint 게시 | 허용 | NOT_VERIFIED 상태, 실패 이력, 남은 의무를 보존 |

Raw 안에 resource link, embedded artifact, 다운로드 URL/ID, 지속 execution retrieval handle은 없다. `Out[1]`은 출력 label이며 보관 artifact의 주소가 아니다. 따라서 **현재 raw 파일 안에서 retrieval-only 복원 경로는 관측되지 않았다**. 도구 전체의 잠재적 기능까지 조사했다는 뜻은 아니며, 외부 retrieval/probe나 추가 계산을 하지 않았다. 누락 부분을 source의 기대값, 보이는 PASS, 재계산으로 메우지 않았다.

최종 scientific admission은 **NOT_ISSUED_REFERENCE_OUTPUT_INCOMPLETE**다. 정적 PASS는 finite fixtures의 실제 실행 PASS도, 전체 domain 구현 certificate도, physical uncertainty 검증도 아니다. 물리 nuclear rate·fast stopping·trajectory·consumer/production admission은 유지하여 NOT_ISSUED이며, PHYS84 local admission은 계속 별도다. HH_R10=OFF. 검토자의 numerical child·Wolfram·old science replay·lease·source edit는 모두 0이다.

### 최종 실제 증거 identity

- Raw: 13,328 bytes, SHA256 `51f4408d91e7ac6566639f3ab3c04eedb3f1e4d2f05a0abd68e7d246e1c6c9eb`.
- Attempt receipt: 3,219 bytes, SHA256 `9fa7e0c264220dd4531f0642c6c2122584e1bda717b50f85c81d7b0403be9c5e`.
- Parse failure: 1,741 bytes, SHA256 `86e4a7e2a1272ae957ab6cae34730ffebd8c1919282d4d8ae930a146f6df571c`.

초기 연결 오류와 두 번째 출력 생략은 서로 다른 결과다. 전자는 수정 후 평가 진입이 관측되었고, 후자는 현재 science 완료 채택을 차단한다. 기록된 예산은 reset하지 않으며 기존 지출·잔여 금액·currency의 미상 값은 `null`을 유지한다. 새로운 자동 실행 승인은 이 C9에 포함되지 않는다.
