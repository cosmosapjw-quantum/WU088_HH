# Future B128/B160 z=0.75 order-study 승인 요청 문안

이번 preflight의 execution_authorized=false, science commands=0, science nodes=0이다. 아래 예시/template 자체는 승인이 아니다.

향후 현재 user instruction에서 아래 envelope를 affirmative directive로 제공할 때만 same z=0.75에서 B128 OD+independent JVP, B160 OD+independent JVP의 bounded one-shot transaction(두 새 order node, 네 command)을 허용한다. B192는 기존 authorized output을 재사용한다.

{
  "schema": "WU088_R31AO_Z075_B128_B160_ORDER_STUDY_AUTHORIZATION_V1",
  "authorize": true,
  "action": "AUTHORIZE_R31AO_Z075_B128_B160_ORDER_STUDY",
  "scope_sha256": "b0abd297847c17741b29a67fae02b9cfd5ddb3fbbe676163867675928cf54a4c",
  "one_shot": true
}

Scope canonicalization: ASCII JSON, recursively sorted keys, separators exactly comma/colon, no whitespace, physical quantities decimal strings, no floating JSON numbers. SHA-256: `b0abd297847c17741b29a67fae02b9cfd5ddb3fbbe676163867675928cf54a4c`.

Producer/model/phase/order/tolerance, metadata adapter, raw-array comparator와 PRIMARY/SECONDARY rule locks를 output access 전에 다시 검증한다. Drift가 있으면 science command 없이 AUTHORIZATION_SCOPE_DRIFT로 반환한다. Existing complete authoritative output을 발견하면 재실행하지 않는다. 첫 새-order scientific output identity 생성 시 authorization은 consumed이며 partial failure는 partial evidence 반환으로 종료하고 자동 rerun하지 않는다.

범위 밖 H/neutral47/ionic2/full49/trajectory, 다른 geometry/order, B144 grid 생성, B256 extension, 새 knot/model tuning, M3/reference-production 작업은 승인하지 않는다. Conditional diagnostics나 finite-order verdict stability는 continuum/source certification이 아니다. 결과 publication/backups 이후 즉시 종료한다.
