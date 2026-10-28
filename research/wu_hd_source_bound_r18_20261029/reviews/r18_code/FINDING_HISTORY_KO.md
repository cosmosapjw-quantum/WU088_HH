# R18 C9 source-provenance 수정 이력

이 문서는 판정의 역사이며 최종 수용 판정은 별도 `FINAL_C9_REVIEW.json`을 참조한다.

## R18-C9-F01: public constructor의 source 결속

최초 S05 source commit은 `8fd7111a1c56dbfeca10893231b16c5ea65543fc`다. 검사한 module Git blob은 `11c2cda5c5ace5d76c7fcc846095a556d22b3e85`, SHA256은 `66393aeb3e03416eef457509041a913eda3caa04081a47504f6be777bb530246`이다.

`NativeGrid`와 `PrintedCell`의 공개 생성자로 synthetic value를 만들고 원본 PDF SHA를 넣으면 `SOURCE_NATIVE_PRINTED_NOMINAL`이 직렬화되었다. 예를 들어 모든 온도에 원문에 없는 `1.00(0)`과 Fraction(1)을 넣은 객체가 원본 source label을 발급했다. CLI의 정상 loader 경로에서 얻은 원래 10개 rate는 정확했지만, 재사용 API에서는 nominal 값과 원전 evidence가 분리되어 있었다. 이는 scope 내 implementation/provenance P2다.

검토자는 52개 targeted 검사를 실제 수행했고 원래 source 행 10개·SI 변환·domain guard·extractor error 분류·CLI exclusive output은 모두 통과했다. 발견된 constructor 반례는 `S05_TARGETED_REVIEW.json`에, 실제 검사한 원문은 `frozen_native_rates_s05.py`에 보존했다.

작성자는 ordinary API loader issuance seal과 token↔Fraction, sourceSHA, pagehash, count/order/type invariant를 추가했다. 중간 수정 SHA256 `b873849b8520d2c6ead41e523a0c2e70728a2da49926e3c9ba5477ba2a2f0658`, blob `f4d826636e38b487761821f6efcaf890c76d74a3`에 대해 기존 독립 targeted 검사와 direct-constructor rejection을 합한 53개가 통과했다. 이 ordinary-API guard는 Python private/reflection을 상대로 하는 보안 경계로 해석하지 않는다.

## 같은 provenance root의 입력 파일 재개방

중간 수정은 파일 바이트를 읽고 hash한 뒤 extractor에 원래 파일 경로를 다시 넘겼다. 따라서 hash 후 path가 교체되면 hash한 바이트와 실제 추출한 바이트가 달라질 수 있었다.

검토자는 원본에 손대지 않고 temporary copy만 사용해 이 경로를 재현했다. 원본 PDF의 6쪽 selected first mantissa `3.99(14)`를 시험용 복제에서 `9.99(14)`로 바꾼 뒤, loader hash 직후 실제 Poppler subprocess가 열기 직전에 temp path를 교체했다. loader는 시험용 `9.99(14)`를 추출하면서도 원본 SHA를 가진 verified grid를 발급했다. 실제 원본 PDF는 종료 후 같은 SHA임을 다시 확인했다. `CONSTRUCTOR_REPAIR_PATH_RACE.json`과 `path_identity_race_probe.py`에 재현 근거가 있다.

수정 방법은 확인한 raw bytes를 extractor stdin으로 직접 전달하거나 동일한 바이트의 불변 private snapshot에서만 추출하는 것이다. 정확한 적용·재검증 identity는 최종 C9 판정에 기록한다. 이 문제는 source identity와 계산 입력 identity의 결합에 한정된다. 원래 수치해석이나 SQM 물리모형의 오류로 분류하지 않는다.
