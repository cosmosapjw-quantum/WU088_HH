# R15 독립 reference 구현 인계 — C5

두 실행 파일의 작성과 AST 문법 확인을 완료했다. **아직 실제 계산이나 과학적 import를 실행하지 않았다.** root가 마지막으로 보고한 실제 게시·이중 백업은 S04, commit `3dae38e813f0ef952990698910d1481eee78357f`, workflow **8/20**, DAG **29/46**이다. 이 C5 작성만으로 그 진행 수나 DAG의 완료 노드를 늘리지 않는다.

## 1. 전달할 코드와 identity

| canonical mirror path | bytes | SHA256 |
|---|---:|---|
| `verification/reference_oracle.py` | 81082 | `bf8928ec3629b81563cbe10b7b0fb68cb10a398dcf2028c66207e50e3932e05e` |
| `verification/run_reference.py` | 14607 | `79206d468dec7407aac27c29a955d7847aba246ed87e672dfb5ada3bc82f8d2c` |

공유 `CASES.json`은 64835 bytes, SHA256 `89b7ebc9f86d2eff58c203e54aa6c370e7259d24f1a9414414e91fd952825619`이다. `ARITHMETIC_SOURCE.json`은 24122 bytes, SHA256 `15216b85daa09c203ee0a856db5c963e13fd89ebe0f9077f94e5ff2f9dd5b885`이다. 두 값은 실제 파일 바이트의 행정 hash 확인이다. 수치 결과를 뜻하지 않는다.

`C5_FUNCTION_MAP.json`은 18개 수용 항목을 실제 함수에 대응시킨다. `AUTHORING_AST_REPORT.json`은 허용된 import 목록, AST parse 및 fixture JSON/hash 확인을 남긴다. `C5_AUTHORING_STATUS.json`과 `C5_AUTHORING_MANIFEST.json`은 상태와 전달 identity를 보존한다.

## 2. 독립 계산 경로

`OriginalModel.F`는 원래 소스 cubic을 power basis로 바꾸고, 움직이는 정확한 overlap 끝점에서 원시함수를 적용한다. `OriginalModel.R`은 원래 t0의 staircase 초기항을 더한다. `OriginalModel.cell`은 다섯 내부 유리수 표본으로 exact quartic을 재구성하고 네 off-stencil 표본을 확인한다. 생산 코드의 Simpson overlap 구성이나 저장된 power 계수를 reference 입력으로 사용하지 않는다.

`Polynomials.nonnegative`는 자체 `U-P`에 대해 squarefree 분해, 홀수 중복도 인수, exact Sturm root count와 고정 rational probe를 사용한다. 모든 model cell의 upper를 이 경로로 확인한다. lower는 자체 다항식에서 다시 평가한 rational witness의 최대값이다. right endpoint와 approaching left-limit witness를 분리한다.

`root_diagnostic`은 미리 정한 일곱 model cell에서 중복도·끝점근·내부근·무근·상수 구조를 확인한다. 최대 깊이 320의 남은 구간은 정확한 root count가 있는 cluster로 남기며 단일근 고립이라고 부르지 않는다. 자체 Sturm 판정으로 production leaf partition에 근이 빠지지 않았는지 확인한다. 두 model의 14개 depth-sweep row는 독립 upper 부호 판정과 lower 존재 판정, gap/work 식으로 확인한다.

`DecimalReference`는 원래 normalized-u power forcing에서

\[
E_R=e^zE_L+\Delta\sum_{m=0}^{4}f_m m!\phi_{m+1}(z)
\]

를 계산한다. 시간 계수는 정확히 Delta 한 번이다. Decimal160에서 각 phi는 고정 512항이다. d=0은 별도의 exact rational 적분으로 확인한다. whole E는 exact forcing majorant 확인과 같은 signed d의 scalar majorant 교차 확인을 분리한다.

`Audit.contains`는 Decimal reference 값을 정확한 Fraction으로 변환한 뒤 저장된 exact rational 경계와 비교한다. 경계값을 Decimal로 미리 반올림하여 strict miss를 숨기지 않는다. fixed guard는 `1e-80*max(1,abs(reference),abs(lower),abs(upper))`이며 strict 위반 수와 최초 50개 예시는 guard 통과 여부와 관계없이 남긴다. pure exact 검사와 mixed exact/guarded 검사의 집계도 분리했다.

## 3. 입력·출력과 실행 경계

예정 진입점은 다음과 같다. **이 명령은 아직 실행하지 않았다.**

```text
python verification/run_reference.py --root ABS_LEAF --output ABS_OUTPUT
```

root의 OS wrapper가 process launch부터 imports·JSON 읽기·연산·serialization을 모두 포함하여 CPU 180초, wall 240초, memory 1GiB를 적용한다. reference 자체에서 subprocess, CAS, production import, 네트워크 요청을 하지 않는다. 실행 중 고정 case 경계에서 작은 progress record를 stdout으로 남긴다.

읽을 실행 입력은 root의 `verification/FROZEN_FILES.json`, `verification/CASES.json`, `verification/ARITHMETIC_SOURCE.json`, 공유 `CONTRACT.json`, 실제 `raw/PRIMARY_RESULTS.json`이다. manifest의 모든 파일은 root wrapper가 먼저 검사한다. reference는 자기 코드 두 개와 공유 입력의 바이트를 검사하고, primary의 freeze metadata를 manifest와 대조한다. production 구현 파일은 열지 않는다. manifest·입력·primary 결과가 계산 도중 바뀌지 않았는지도 마지막에 확인한다.

출력은 `WU_R15_REFERENCE_RESULTS_V1`이고, case별 PASS/FAIL, 실패 원인, exact/guarded 검사, strict miss, root diagnostics, depth rows, observed arithmetic counts 및 hash를 담는다. 선언된 21개 case는 선행 입력 실패가 있어도 결과에서 삭제하지 않는다. 출력 serialization에 문제가 생기면 모든 case/check record를 보존하면서 저장 한도를 넘은 값만 명시적 unresolved bit-length/hash record로 바꾸고 전체 결과를 FAIL로 남긴다.

기존 output 파일은 덮어쓰지 않는다. 실제 실패 후 허용된 repair를 실행하려면 root가 실패 파일을 먼저 보존하고 새 output 경로나 비워진 원래 경로를 사용해야 한다. 자동 재시도, precision/guard 조정, 실패 case 삭제는 없다.

## 4. 확정된 인터페이스와 유한 조건

- 공유 control은 **21 models, 75 base cells, overlap precharge 4811, 7 root-pattern cells, 14 depth rows**이다. 이 개수는 사전 설계이며 runtime 관측은 앞으로 얻는다.
- Qmax는 `c*exact_Rsup_upper+max(geB3)`이다. raw whole R은 dyadic supremum bounds를 사용한다.
- `overlap_terms_actual`은 모든 source/strip/basecell loop를 센다. `nonempty_overlap_terms`는 q의 0 가중치를 제외하기 전의 양의 interior overlap을 센다.
- saved outgoing E interval은 saved incoming E, exp, W interval로 만든 양의 polynomial-forcing recurrence를 outward로 포함한다. whole majorant도 같은 방향이다. 이 의미는 root와 공유 schema 작성자가 확인했으며 production 구현을 읽어 확인한 것이 아니다.
- 입력 256 bits·2048자, 저장 derived 16384 bits·10000자, reference 내부 미저장 squarefree/Sturm 1048576 bits를 분리했다. 일반 Euclid division 5회, Sturm sequence 5개, long division elimination 5회, multiplicity loop 4회 한계를 넣었다.
- standard-library만 사용한다. AST parse는 문법만 확인하며 산술·수치 동작의 PASS를 대신하지 않는다.

현재 남은 인터페이스 모호성은 없다. root의 최종 freeze, 실제 primary raw 결과, 독립 정적 심사 및 bounded reference 실행이 아직 필요하다. 이 코드는 supplied arithmetic control의 조건부 비교식을 검증한다. actual HD/physical consumer/state/density/clock의 미확보 상태, HH_R10 OFF, production NOT_ISSUED, L4 false, central/physical delta 0은 유지한다.
