# Independent artifact review: G1 and G2

검토 결론은 **G1의 명시적 전제하 수학적 implication 및 G2의 synthetic
implementation 검증을 수용**하는 것이다. 역사적 NumPy/ABI 입증과 실제 HH
값의 인증은 여전히 별도 미완료 gate다. 이 검토자는 G3 작성자이며 G1/G2
작성자와 분리되었다. 프로젝트의 admitted independent decision reviewer
자격은 입증되지 않았으므로 `independent_review_admitted=false`다.

실제 B192·prediction 값, HH 입력 상수·integrand·callback은 읽거나 실행하지
않았다. 구현은 변경하지 않았고 이 디렉터리에 재현·검토 증거만 작성했다.

## 발견 B09: 빈 Fortran 배열의 resource cap 우회 — 수정 검증 완료

초기 G2 decoder는 `shape=(2**63-1,0)`, `fortran_order=True`,
`max_elements=0`인 정상적인 빈 NPY의 header를 허용한 뒤
`itertools.product(range(huge),range(0))`를 만들었다. product는 Cartesian
product가 비어 있더라도 첫 range를 메모리 pool로 먼저 구체화한다.
그 결과 element cap이 0인데도 대규모 allocation을 시도했다.

128 MiB `RLIMIT_AS`, 5초 subprocess cap 아래의 독립 synthetic 재현에서
`MemoryError`가 발생했다. scientific wrong-value가 아니라 **중간 심각도
resource/failure-contract 구현 결함**이다. `empty_fortran_reproduction.py`
및 `.log`가 최초 재현을 보존한다. 위 숫자는 데이터 값이 아닌 synthetic
header 차원이며 실제 배열 메모리는 생성하지 않았다.

Root가 `_storage_indices`의 처음에 `element_count==0` early return을
추가하고 zero axis의 여러 위치에 대한 regression을 작성했다. 수정 후
동일한 독립 재현은 `values=[]`를 반환했다. 더 강한
`shape=(2**63-1,0,2**63-1)`도 같은 128 MiB 제한에서 정상 종료했다.
현재 decoder suite **30 tests PASS**를 별도 subprocess로 다시 확인했다.
해당 수정의 closure는 `RESOLVED_IMPLEMENTATION_VERIFIED`다.

## Decoder 검증 범위

수정 전 기존 29 tests, 수정 후 30 tests를 각각 실행했다. 추가로 서로 다른
binary64 정상 수 200개를 x87과 binary128로 독립적인 비트 확장하여,
little/big endian과 x87 의미 바이트 offset 0·3·6을 조합한 **1,600개**
정확한 값 및 canonical hash 동치 검사를 통과했다. 이는 decoder의
layout dispatch·padding 제외·endian 처리를 검증한다. NPY byte identity와
mathematical identity는 분리되어 있다. 기존 tests의 비정상 header,
payload 길이, signed zero, nonfinite, pseudo-denormal/unnormal, asymmetric
2D/3D Fortran 및 component ordering 사례도 확인했다.

`LayoutAuthority`는 호출자가 제공한 구조·SHA 형식·해당 NPY 바이트와의
결합을 확인한다. evidence 문헌이나 역사적 serializer 자체의 진위를
검증하지 않는다. Synthetic authority의 scope 문자열만
`HISTORICAL_PRODUCER_LAYOUT_REVIEWED`로 바꿔도 구조상 허용됨을 직접
확인했다. 이는 문서에 명시된 trust boundary이며 현 decoder의 결함으로
분류하지 않는다. 다만 미래 certificate runner가 이 문자열만 보고 역사적
ABI를 승인하면 인증 결함이 된다. 현재 `RAW_ABI_AUTHORITY_BLOCKED`,
`historical_layout_admitted=false` 보존은 타당하다.

## G1 정리·source 대응

기존 **15 synthetic exact tests PASS**를 독립적으로 확인했다. G1에 기록된
원본 네 source의 SHA256와 ABI 문서에 기록된 repository evidence 여덟
항목의 SHA256가 실제 bytes와 일치했다. 코드 파일은 정적으로만 읽었다.

검토한 비자명한 연결은 다음과 같다.

- h0_fused의 O/G는 UU plane과 M, M′, M″를 사용하며 G1/G2는 음의 center
  derivative다. pz polynomial derivative의 +1 항이 보존된다.
- 실제 공간의 `|r1-r2|^k`를 complex contour로 이동시키지 않고 Gaussian
  source parameter의 entire continuation으로 radial 식을 확장한다.
  Re(A), Re(B)>0이면 Re(σ)>0이며 principal power의 정의역이 유지된다.
- 1F1의 r=0,1,2 shifted derivative와 zero-Pochhammer shortcut, bilinear
  s, upper incomplete Gamma의 방향과 regularized=0 convention이 맞는다.
- post-integral conjugation, exact stored pref/v/C, τ=z/v, 유한 orbital
  contraction은 canonical source-functional map의 target과 일치한다.
- endpoint complement의 corners를 한 번만 센다. 독립 upper bound
  W−S로 interior upper를 만들지 않고, rectangle→disk 변환에는
  sqrt(rx²+ry²)가 필요하다.
- real Pareto sufficient condition은 엄격/비엄격 부등호를 보존하며
  원래 binary64 machine predicate를 자동 재현했다고 주장하지 않는다.

G1의 `PROVED`는 명시적 exact-input/domain 전제하 implication을 뜻한다.
실제 input premise, backend/code binding, uniform nested enclosure,
실제 D balls 및 feasibility까지 해결됐다는 의미는 아니다.
`REMAINING_THEOREM_OBLIGATIONS.json`이 이를 분리하고 있어 추가적인
과학적 gate 승격 오류는 발견하지 못했다. 유한 polynomial tests는 일반
해석학 정리를 증명하지 않으며, 일반성은 본문의 dominated differentiation과
analytic continuation 논증에 의존한다. 이 검토는 proof-assistant 형식 검증이
아니다.

## G3와 연결되는 K identity 주의

Root에게 전달한 계약 해석은 세 객체를 구분한다.

1. `raw_constructed_exact_K`: exact lift(C192)와 exact lift(R192)에서
   정확히 `(C192-R192†)/2`로 구성하는 새 represented reference.
2. `model_stored_prediction_K`: frozen prediction archive에 저장된 모델의
   K. predicted D에서 다시 구성하면 비교 target을 바꾸므로 금지한다.
3. `legacy_complex128_constructed_K`: 기존 comparator가 C/R를 complex128로
   변환한 뒤 rounded subtraction/division으로 구성한 diagnostic truth K.

새 direct route는 1과 2를 사용한다. Legacy eta는 old diagnostic의 cast와
K construction을 포함한 discrepancy를 한 번에 bound한다. 별도 stored raw
K가 있더라도 동치 증명이나 추가 오차 회계 없이 1을 대신할 수 없다.
이 설명은 G3 자기검토의 독립 승인으로 간주하지 않는다.
