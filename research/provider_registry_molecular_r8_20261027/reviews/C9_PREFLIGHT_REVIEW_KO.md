# R8 C9 사전 정적 검토

**판정: PASS_STATIC_CORE_CALLER_AND_REFERENCE_PENDING_ACTUAL_RESULTS.** 현재 읽은 고정 소스에서 실행 전에 수정해야 할 실질적 결함은 발견하지 않았다. 이 문서는 같은 R8 독립 심사의 정적 단계이며, 실제 실행 PASS나 최종 C9 채택을 선언하지 않는다.

## 실제 검토 범위

S03의 일반 지연 커널 증명과 production core, S04의 독립 Decimal80 reference, 환경 복구 후 재구성된 실제 primary runner를 읽었다. 원본 텍스트·선택한 동결 결과 필드·파일 SHA256을 확인했으며, 심사자가 과학 코드를 실행하거나 import하거나 AST를 실행한 횟수는 모두 0이다. 새 조사나 외부 쓰기도 수행하지 않았다.

Primary의 실제 SHA256은 `19aa784543bf75343e70ba76f9696cca0ecce7396e03d2c5c4206827dcf8250a`다. 과거 미게시 초안의 `483dcd…`는 실행 권위가 아니며 authoring recovery 기록으로만 보존한다. Core·input·reference는 기존 고정 해시와 일치한다.

R6/R7의 원본 SHA, native K의 interval midpoint, 공통 λ와 P_lower, 정확한 H/ρ, 상태 순서, R6 all-starts 증명 결속을 확인했다. 세 macroblock은 동일 B/g와 clock을 사용하며 초기·끝점 상계가 연결된다. 전체 3H에서는 최초 초기 오차를 유지한다.

192개 초기 cell 상계는 실제 저장 whole_block_upper를 복제한다. 15개 query와 세 true endpoint는 실제 source pointer·값·절대시각으로 결속되며 exact grid membership을 요구한다. Point cap을 whole cell에 적용하지 않고, 마지막 min 뒤에 재반올림하지 않아 원본 Fraction보다 커지지 않는다. Current-cell forcing은 계수 1을 유지한다.

독립 reference는 production core를 import하지 않고 Decimal80 직접 합산과 다섯 analytic control의 별도 닫힌식을 사용한다. 네 HD·다섯 control의 실제 primary 출력 schema와 일치한다. 저장된 binary64 궤적은 표본 확인 자료이며 새로운 연속 ODE 인증이나 cap의 근거로 사용하지 않는다.

## PRE01 및 CAS

Root가 먼저 발견한 PRE01은 수정된 실제 소스에서 확인했다. Exact no-worse는 Decimal80로 반올림된 cap 대신 원본 `cap_provenance.upper`를 Fraction으로 비교한다. 정적 수정 수용 상태이며, runtime 종료는 예정된 한 번의 reference 결과에서 확인한다.

CAS 최초 호출은 JSON export에 실패하여 실제 `$Failed`를 반환했다. 승인된 export-only repair 한 번에서 scalar 7/7과 kernel 9/9의 0, 부호식 4/6의 True가 반환되었고 두 식은 symbolic 상태다. 두 식의 수동 근거는 기존 일반 증명의 R8.14와 R8.12에 있다. 실제 Power/Infinity 경고를 보존하고 원인은 NOT_ESTABLISHED로 둔다. 따라서 CAS는 qualified partial corroboration이며 전체 CAS PASS나 warning-free로 표현하지 않는다. 최초·수정 예산은 모두 소진되었고 심사자는 추가 호출하지 않았다.

## 남은 판정 조건

최종 C9는 실제 S05 고정 runner, 한 번의 primary 및 한 번의 independent reference 결과와 원본 해시, imports·serialization·shutdown을 포함한 외부 process CPU 영수증에 근거해 같은 심사 안에서 마감한다. 현재 물리 consumer·reactive array·collider density/physical clock 결속은 미결이다. 조건부 estimator의 채택이 이 입력을 대체하지 않는다.

