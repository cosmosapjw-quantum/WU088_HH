# PHYS85 독립 C9 코드 검토

현재 판정은 **STATIC_PASS_SCOPED_RUNTIME_PENDING**이다. 동결 계약과 구현의 일치에 현재 차단 사항은 없으며, root의 S1 backup gate 이후 첫 계약된 reference 실행으로 진행할 수 있다. 이 정적 판정은 실제 실행 PASS나 새 reference 결과의 과학적 채택이 아니다. 실제 원시 결과를 읽은 뒤 이 문서와 JSON의 판정을 갱신한다.

## 검토 범위

실제 S1 HEAD `04be89e24401966770d137b115c73f66b563ef5d`, tree `20a4875a05a543a8547cf7524e2425d78817f453`의 revision2 계약, 세 WL 파일, frozen inputs, 실행 인자 및 동결 manifest를 읽었다. 새 diff는 두 연구 단위 안의33개 additive 파일이며 부모 파일의 수정은 없다. 9개 동결 파일이 manifest와 일치하고, 요청 code가 assembled WL 원문과 일치함을 bytes/metadata 수준에서 확인했다. 이 확인은 수치 실행이 아니다.

## 코드 판정

정확 유리수의 normal-frame photon/daughter boost와 초기 pair kinetic debit이 계약 식을 구현한다. Binary daughter owner가 thermal 입자수 h−2, fast 입자수1−h, electron0을 결정한다. 여섯 에너지 owner 중 방사 destination은 하나이며 emitted diagnostic은 별도 추가 에너지가 아니다. Ensemble은 joint mean(h Kc)를 유지한다.

검증기는 생산 helper의 결과를 같은 closure식으로 다시 합산하는 것에 그치지 않고 독립적인 두 four-vector의 boost matrix, daughter mass shell, photon null, 전체 에너지·운동량 및 A/Z incidence를 검사하도록 작성되어 있다. NR rate-slope 항은 thermal energy debit과 particle number를 직접 EOS chain rule에 대입하여 확인하며, covariance 항은 centered weighted product와 비교한다. 이 검증 범위는36개 조건부 사건과6개 ensemble 및 명시한 symbolic/guard controls에 한정된다. 임의 입력의 continuum 구현 certificate나 물리 질량 uncertainty를 뜻하지 않는다.

현재 차단 사항은 없다. Frozen inputs의 과거 requested-model 설명은 현재 ROLE_RECEIPT/EXECUTION_REQUEST의 실제 root 요청 gpt-6.1-sol/high/fork_none 기록보다 앞선 metadata다. 이 annotation 때문에 동결 숫자 입력을 바꾸거나 과학을 다시 실행하지 않는다.

## 남은 판단

실제 raw Wolfram 응답과 디코딩된 보고서의 완전성,36/6 행, assertions·guards·symbolic 결과, source/request identity, 실패·timeout 여부를 읽은 뒤에만 `EXACT_REFERENCE_IMPLEMENTATION_VERIFIED` 판정이 가능하다. Physical finite-T source supplier, actual nuclear rates, fast stopping, consumer/production admission은 그대로 OPEN/NOT_ISSUED다. PHYS84 local lease WAIT를 이 cloud reference가 대신하지 않는다.

검토자의 새 numerical child/Wolfram/old callback/lease/원격 mutation/source edit는 모두0이다. HH_R10=OFF, production admission NOT_ISSUED를 유지한다.

## 첫 실제 응답과 한 번의 제한 수정 승인

첫 실제 Wolfram 호출은 transport `isError=false`였지만, `reference_report`가 association/report가 아니라 평가되지 않은 `PHYS85RunVerification[...]` 문자열이었다. 원문10,477bytes, 디코딩 보고서6,764bytes와 attempt receipt를 읽었다. 반환된 구조화 event/ensemble/assertion행은0이고 COMPLETE는 없다. 이 결과를 성공한 계산이나 물리식 실패로 분류하지 않는다. 초기 정적 검토는 단일 compound expression에서의 context 연결 문제를 잡지 못했으며, 실행 전 PASS를 runtime PASS로 승격할 수 없었던 이유가 실제로 드러났다.

분류는 **IMPLEMENTATION_ENTRYPOINT_NAMESPACE_BINDING_FAILURE**다. [Wolfram 공식 context 설명](https://reference.wolfram.com/language/tutorial/ModularityAndTheNamingOfThings.html)은 complete expression의 symbol name 해석이 실행보다 먼저 이루어지고 `Begin`의 영향은 후속 complete expression에 적용된다고 설명한다. 전체 파일을 한 code expression으로 합친 뒤 일부 entrypoint만 명시적 `PHYS85Verify` context로 호출하는 현재 조립 방식과 관측된 미평가는 이 원인에 부합한다.

**GO_ONE_TARGETED_BINDING_REPAIR**: 새 `implementation/repair_01/`에서 trusted source/verifier의 context directive8줄만 제거하고, wrapper의 명시적 `PHYS85Verify` prefix3곳을 같은 flat entrypoint 이름으로 바꾼다. 이름 공간을 평탄화해도 source와 verifier의 helper 이름은 충돌하지 않는다. 원본9동결파일·첫 실패를 그대로 보존하며, 물리식·입력·검증 수학·guard·출력 schema·시간 cap은 바꾸지 않는다. 낮은 tier가 구현하고 기존 계약의 **추가 호출1회** 범위에서 실행한다. 별도 runtime probe나 새 테스트 캠페인은 필요 없다. 실제 수정 diff와 원시 결과를 읽은 뒤만 최종 scoped admission을 판정한다.

검토자는 이 수정도 직접 구현하지 않았고 새 WL/수치 계산을 실행하지 않았다.
