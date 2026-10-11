# PHYS08 signed rate-weighted scalar gate

## 계약과 수학적 의미

`src/weighted_gate.rs`는 외부 crate가 없는 Rust 모듈이다. 입력은 유한한 binary64
닫힌 구간 `p,w,fhat,v[4]`와 선택적 `temperature`다. 성분 순서는
`(x_HII,y_HeII,y_HeIII,w)`이며 모든 signed 성분을 보존한다. 작은 He 성분이나
구간의 음수 끝점을 버리지 않는다. `p.lo>0`, `w.lo>0`을 요구하고, 온도를
제공하면 `T.lo>0`도 요구한다. `fhat` 자체에는 부호 제한을 추가하지 않았다.
물리적으로 허용되는 abundance와 입력 상관성은 호출자가 결박해야 한다.

Rust 모듈의 일반 scalar domain은 signed `fhat`을 허용한다. 반면 동봉한
Python `exact_weighted.weighted` reference는 물리 입력 경계에서 `fhat.lo>=0`을
요구한다. 이는 두 API의 domain 차이이며, 현재 11개 golden fixture는 모두
`fhat>=0`이고 실제 source에서 온 네 fixture는 `fhat>0`이므로 그 비교에는
영향이 없다. 음의 `fhat`에 대한 Rust의 일반 scalar 동작은 이 golden oracle의
검증 범위에 포함되지 않는다.

계산하는 식은

\[
B=pv_w-w(v_x+\hat f v_{y_1}+2\hat f v_{y_2}),\qquad
DT=\frac{T}{wp}B
\]

다. 두 번째 식의 물리적 해석은 제공한 `T`가 같은 상태의
`T=Cw/p`, `C>0`를 포함한다는 조건에 따른다. `C`의 값이나 온도 identity는
이 모듈이 생산하지 않는다. `w`와 `v_w`는 프로젝트의 eV/H 단위를 유지한다.
관측량의 시간 또는 매개변수 단위는 입력 vector의 의미를 그대로 따른다.

`GateInput.role`은 `P_N`, `P_M`, `SIGNED_VECTOR` 중 하나다. 결과에 같은 label을
반환하여 물리 photo vector와 birth derivative를 구별하지만, label만으로 그
의미나 권한을 입증하지 않는다. 실제 source tuple, C² 영역, Θ 전체 coverage,
전달 identity, root, implicit mixed response 또는 native authority는 입력 및
상위 계약의 별도 의무다. source/transport/provider/root 호출이나 private permit
의존성은 없다.

`balance_sign`과 `dt_sign`은 각각 구간에 독립적으로 적용한 strict 판정이다.
상단이 0보다 작으면 `NEGATIVE`, 하단이 0보다 크면 `POSITIVE`, 그 외에는
`UNRESOLVED`다. 0을 포함하는 구간은 작은 폭이어도 strict sign으로 승격하지
않는다. B가 strict해도 DT의 underflow 포함값이 0을 가로지르면 `dt_sign`은
`UNRESOLVED`로 남는다. 별도의 양의 계수 정리를 적용하는 상위 논증과 이
수치 출력 판정을 구별한다.

## 유한 정밀도와 오류 의미

각 `+,-,*,/` 연산은 endpoint의 일반 binary64 연산 뒤에 next-down/next-up을
한 칸 적용한다. 곱과 몫은 네 endpoint 조합을 모두 사용한다. 정상 IEEE-754
binary64 연산과 gradual underflow를 전제로 정확한 실수 구간 연산의 포함값을
구성한다. `next` 연산은 signed zero와 subnormal을 bit 단위로 처리하며
FTZ, absolute-value clipping, tolerance, `unsafe`, libm 또는 fast-math를 사용하지
않는다. 연산 순서를 고정하고 합곱을 `mul_add`로 바꾸지 않았다.

`evaluate`는 매 호출 시 `black_box` 입력을 사용한 최소 underflow 및 rounding
관측으로 알려진 비표준 환경을 거절한다. 이는 플랫폼 전체에 대한 완전한
attestation은 아니다. 외부에서 FP mode를 변경하거나 비표준 fast-math 옵션을
추가한 빌드는 지원하지 않는다.

NaN/Inf/역순 입력은 `INVALID_INTERVAL`, 양성 domain 실패는 `NON_POSITIVE_*`,
0을 포함하는 분모는 `DENOMINATOR_CONTAINS_ZERO`다. 중간 산술 overflow는
`NON_FINITE_ARITHMETIC`, 유한 결과를 한 칸 넓혔을 때 infinity에 닿으면
`OUTWARD_RANGE_OVERFLOW`로 명시한다. 유한한 입력도 중간 표현 범위 때문에
거절될 수 있다. 특히 `w*p`가 너무 작아 outward 분모가 0을 포함하면 DT를
만들지 않고 오류를 반환한다. 이를 물리 domain 부정이나 냉각 부호 실패로
해석하지 않는다. `temperature=None`이면 B만 계산할 수 있다.

## 검증 프로그램과 독립 oracle 경계

아래는 예정된 실행 방법이며 작성자가 이 명령을 실행했다는 주장은 아니다.

```sh
rustc --edition=2021 tests/weighted_gate_tests.rs -o weighted_gate_tests
./weighted_gate_tests --vectors results/weighted_corrected/GATE_INPUTS.tsv
```

Standalone harness는 먼저 일곱 의미 검증 그룹을 수행한다. 저에너지 주성분에
20 eV 잉여에너지의 작은 tail을 더하면 cooling을 유지하고 큰 tail은 heating을
만드는 사례, 같은 벡터에서 `v_w>0`와 `DT<0`가 동시에 성립하는 관측량 구별,
정확한 0의 미결정, signed He 성분을 생략하면 부호가 뒤집히는 반례, 양의
스케일링의 정확 dyadic 포함, 역할 label 보존, invalid/domain/overflow 거절 및
subnormal underflow를 다룬다. 정확 dyadic 기대값은 손 유도한 scalar 값이다.
이는 전체 interval 입력에 대한 독립 rational oracle 검증을 대체하지 않는다.

외부 입력은 한 줄에 18개 whitespace-separated 필드다. 빈 줄과 `#`로 시작하는
줄은 무시한다. case ID는 영숫자 및 `_ . -`만 허용한다.

```text
case_id role p_lo p_hi w_lo w_hi fhat_lo fhat_hi vx_lo vx_hi vy1_lo vy1_hi vy2_lo vy2_hi vw_lo vw_hi T_lo T_hi
```

`role`은 `P_N|P_M|SIGNED_VECTOR`다. 모든 endpoint는 접두사 없는 16자리 hex
binary64 bit pattern으로 입력한다. T 미제공은 마지막 두 필드를 `- -`로 둔다.
NaN/Inf bit pattern이나 역순 구간도 gate rejection을 검증할 목적으로 입력할
수 있다. parser 오류는 프로세스 exit 2, 실제 gate rejection은 해당 JSONL 행의
`status=ERROR`와 명시적 error code로 보존한다.

성공 행은 `kind=gate`, `case_id`, `role`, `status=OK`, `B`, `B_sign`, `DT`,
`DT_sign`을 출력한다. B와 DT endpoint는 `lo_bits/hi_bits`로 보존하고 T가
없으면 DT와 DT_sign은 null이다. 외부 oracle의 기대 결과는 binary가 읽지
않으므로 자기 계산을 oracle로 인정하는 경로가 없다. root가 exact rational
oracle 및 saved real-input을 작성하고, build/run과 반환 endpoint 포함 검사를
별도의 보존된 실행으로 수행한다.

현재 상태는 **implemented; Rust build NOT_BUILT, Rust tests NOT_RUN**다.
Root의 현재 host 점검에서 `rustc`와 `cargo`가 PATH에 없었고 Python 3.12.14만
확인되었다. 작성자는 source 평가, Rust build/test 또는 원격 mutation을
수행하지 않았다. Root의 Python exact-rational/finite-interval 검증은 이 Rust
코드의 빌드·실행 증거를 대체하지 않는다. 저장된 golden 입력에 대한 Rust
build와 최초 실행은 다음 NCP의 구체적 의무다. 실제 루프 실행 및 독립 검토
상태는 run ledger와 판정 기록을 따른다.

## 저장된 Rust 출력의 exact-oracle consumer

`diagnostics/check_rust_output.py`의 전달 시점 상태는 **READY_NOT_RUN**이다.
Python 표준 라이브러리와 동봉한 `src/exact_weighted.py`만 사용하며 Rust build,
harness 실행, source 재계산을 호출하지 않는다. NCP에서 실제 Rust 첫 실행의
stdout을 보존한 후 아래 consumer를 한 번 실행한다. 출력 파일명은 해당 NCP
bounded-run 계약에서 고정한 실제 경로로 연결한다.

```sh
python3 diagnostics/check_rust_output.py \
  --oracle results/weighted_corrected/GOLDEN_ORACLE.json \
  --output evidence/rust_gate_first/stdout.txt \
  --report evidence/rust_gate_first/ORACLE_CHECK.json
```

Report는 create-only다. 기존 report를 덮어쓰지 않으며 validation rejection도
새 report에 보존한다. 성공은 exit 0 및 `PASS_SCOPED_OUTPUT_CONTAINMENT`,
내용 검증 거절은 exit 1, 입출력 또는 report 생성 실패는 exit 2다.

Consumer는 고정된 11개 fixture의 누락·중복·추가, role 불일치, JSON 중복 key,
비정상/추가 행, gate ERROR, 잘못된 유한 구간 및 endpoint와 맞지 않는 sign을
거절한다. 정확히 `semantic_checks` 1행, fixture 11행, 최종 `summary` 1행을
요구한다. 요약의 7개 built-in 그룹, 전체 gate 호출 26회, 의도한 gate 거절
7회는 공급된 출력의 schema로 확인하고 실제 프로세스 계측으로 승격하지 않는다.

비교는 각 binary64 endpoint를 정확한 유리수로 바꾸어
`Rust.lo <= oracle.exact.lo` 및 `oracle.exact.hi <= Rust.hi`를 모두 요구한다.
단순 overlap이나 endpoint equality를 성공 조건으로 사용하지 않는다.
`strict_match_required=true`인 사례는 oracle의 부호와도 일치해야 한다.
`minsubnormal_signed`에서만 안전한 outward 확대 때문에 strict negative가
`ZERO_CONTAINING`으로 남는 결과를 허용한다. 모든 판정에서 출력 자체의
endpoint와 `NEGATIVE/POSITIVE/UNRESOLVED` label 사이의 일치가 필요하다.

실제 Rust 실행 여부와 실행파일·입력 결박은 출력 JSONL만으로 확인할 수 없다.
Consumer report는 `rust_execution_attested=false`,
`binary_and_input_binding_attested=false`, `native_authority=false`를 유지한다.
실행 영수증이 실제 exit와 source/input/binary identity를 별도로 제공해야 한다.
Consumer의 scoped 결과도 native source 또는 root/혼합응답 인증이 아니다.
