# R18 C9 최종 독립 판정

**PASS_SCOPED_NATIVE_PRINTED_SOURCE_API. 열린 material finding 0건.** 최종 검토한 `native_rates.py`의 Git blob은 `be2a845263b215b604f255ffe5deabe55be9dd7b`, SHA256은 `282ba390836979f051a3e80e502569df8238b2f28c734de9df2da1b88122eb60`다. Root의 게시 commit은 이 local byte identity에 별도로 결속해야 한다.

다른 작성 주체인 `/root/r17b_independent_review`가 frozen S05의 원문·code를 읽고 발견한 source-provenance P2는 두 실제 수정으로 닫혔다. 공개 constructor의 synthetic value/source label 분리는 loader issuance 및 exact cell·token·value·state·source invariants로 교정되었다. 확인한 source 파일을 hash한 뒤 같은 경로를 extractor가 다시 열던 입력 identity 차이는 **동일한 검증 raw bytes를 extractor stdin으로 전달**하여 교정되었다.

수정 후 독립 targeted 검사 **53개**가 통과했다. 이전에 실패했던 실제 temporary-path replacement 재현도 통과했다. 후자의 검사는 원문 3.99(14)를 시험용 복제에서 9.99(14)로 바꾸고 hash와 추출 사이 temp path를 교체했지만, 최종 loader는 검증된 원 바이트에서 3.99(14)를 정확히 추출했다. 실제 source PDF는 변경하지 않았고 원 SHA를 재확인했다.

Table2의 모든 10개 rate·SI 변환은 작성자 extraction을 보기 전에 독립 PDF extraction으로 고정한 oracle과 일치했다. 이산 온도·state·method guard, 잘못된 source hash, extractor 실패·timeout·encoding 분류, CLI exclusive output 및 기존 파일 보존도 확인했다. 시험으로 생성한 altered PDF는 반례 재현 fixture이며 physical rate 자료로 사용하지 않는다.

원본 S05 결과·module, 중간 constructor 수정·path-race 실패, 최종 성공 결과를 각각 보존했다. 기존 R17A/R17B suite와 physical ODE 재실행은 0회다. Root가 별도로 수행한 unittest·pypdf·Wolfram 결과는 이 검토자의 실행으로 재분류하지 않는다.

이 수용은 native **printed nominal** SQM row의 source-to-code 연결과 지원 API에 한정된다. 실제 rate uncertainty, 연속 온도 보간, HD 에너지·population, density·clock·full-A consumer의 의무는 각 계약에서 처리한다. 기존 source R6의 §3 j≤6 대 본문 Eq.(5) j≤8 차이와 j7/8 누락 기록을 그대로 재사용한다. `HH_R10=OFF`, `production=NOT_ISSUED`, `L4=false`를 유지한다. 추가 코드 수정은 요구하지 않는다.
