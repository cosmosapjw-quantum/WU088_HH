# Integration seam 및 G5 endpoint 독립 artifact 검토

결론은 **B12의 resource 분류 수정을 재검증한 synthetic integration seam과
G5 endpoint 구현을 해당 범위에서 수용**하는 것이다. 실제 HH target 또는
full certificate를 승인한 것이 아니다. 검토자는 G3 저자이므로 G3 자체의
독립 검증으로 이 보고서를 사용할 수 없다. 검토 범위는 root가 작성한 새
integration 연결부와 다른 작업자가 작성한 G5 proof/implementation이다.
`independent_review_admitted=false`를 유지한다.

## B12 — model input resource 분류 불일치, 수정 확인

수정 전, `max_entries=4`이고 raw는 2×2인 synthetic bundle에서
R31AK의 stored K만 3×2로 바꾸면 `ContractError('element cap exceeded')`가
발생했다. Raw 입력의 동일한 cap 위반은 `ResourceLimit`으로 분류됐다.
유효하지 않은 값이 통과하는 결함은 아니지만 같은 resource 실패를
입력 역할에 따라 다르게 보고하는 **낮은 심각도의 taxonomy 결함**이었다.

Root가 공통 `_decode`에 header-count precheck를 옮겼다. 수정 후 같은
독립 재현은 `ResourceLimit`을 반환했다. Root의 RED/GREEN 기록은
`certificate_pipeline/REVIEW_RED.log`, `POST_REVIEW_GREEN.log`이고,
검토자의 전체 재실행은 `pipeline_after_fix.log`에 **8 tests PASS**로
보존했다. `independent_after_resource_fix.log`도 model-only case를 확인한다.

## Integration 계약과 claim ceiling

G2의 C-order exact value 반환을 G3로 전달하고, represented gap과 target
disk-to-raw Frobenius epsilon, ε_K/ε_Dmax 전파 및 real sufficient rule로
연결하는 순서를 확인했다. target provenance, 역사적 ABI, frozen scalar
machine trace 또는 authorization을 scope 문자열만으로 승인하지 않는다.
명시적인 ACTUAL_HH mode는 거절하며 반환 certification flag는 false/null다.
물리적 입력이 synthetic라는 사실을 문자열이 증명하는 것은 아니므로
미래 실제 runner에는 외부 인증된 provenance와 실행 범위 binding이 필요하다.

모델 K가 predicted D로 몰래 재구성되지 않는지 추가로 확인했다. R31AK의
stored K만 100I로 바꾸면 PRIMARY K lower gap은 −197/2가 되고 Dmax gap은
2로 유지된다. 판정은 unresolved이며 `rigorous=false`,
`certified_epsilon=null`, `certified_eta=null`,
`target_provenance_admitted=false`, `machine_predicate_certified=false`다.
이 검사는 integration이 독립 stored K 입력을 전달하는지를 검증한다.
G3 kernel 자체에 대한 독립 승인으로 해석하지 않는다.

## G5 증명과 구현

17개 기존 endpoint tests를 독립 subprocess로 실행해 모두 통과했다.
추가로 a=4,b=9, centers=0,k=0인 synthetic 입력에서 Gaussian C_F의
여섯 closed-form 값에 대한 outward upper를 Decimal 100자리로 비교했다:

| channel/field | 정확한 majorant 식 |
| --- | --- |
| s/O | π³ |
| s/G1 | 8π^(5/2) |
| px/G1 | 3π³ |
| pz/G1 | 4π³ |
| s/G2 | 12π^(5/2) |
| px/G2 | 12π² |

세 개 추가 (μ,T) 사례에서 i=0 upper-tail 식 μ/(4√π T²)도 확인했다.
이 독립적인 수치 검산은 implementation 오류 탐지용이며 증명 authority를
대체하지 않는다.

수학적 검토에서 다음 포함관계를 확인했다.

- π의 Machin alternating bounds, exp의 reduced alternating bounds와 양의
  squaring, rational floor/ceiling quantization이 outward 방향을 보존한다.
- Γ(1/2,x)=b−Γ(−1/2,x)/2와 Γ(−1/2,x)≤Γ(1/2,x)/x로부터
  b/(1+1/(2x))≤Γ(1/2,x)≤b가 나온다. Positive half-integer recurrence의
  모든 항은 양수이므로 enclosure propagation이 유효하다.
- λ=μ²/4와 ν=i+3/2−r의 lower-tail λ^(1−ν)Γ(ν−1,λ/ℓ),
  upper-tail T^(−ν−1/2)/(ν+1/2)의 지수·방향이 맞는다.
- exp(−λ/t)t^(−ν)의 panel maximum은 λ/ν를 panel에 clamp한 지점이다.
  분모의 left-end upper와 곱해 J를 독립적으로 상계한다.
- Scaled spatial coordinates의 moments 2πΓ((n+3)/2) 및 a,b의 inverse
  square-root 계수는 source Gaussian majorant와 일치한다. pz G1의 +1이
  보존되고 normalization/donor/orbital coefficient는 별도 한 번만 적용한다.
- `C_F(E_t W_u+J_t E_u)`는 disjoint complement를 상계한다.
  잘못된 W−E subtraction이나 corner 이중합을 사용하지 않는다.

증명·구현의 validity 오류는 추가로 발견하지 못했다. 작은 양의 입력에
대한 sqrt lower가 0이 될 때의 reciprocal 거절, 보수적 gamma bounds,
algorithmic cap과 OS wall/RSS 제한의 차이는 문서에 명시돼 있다.
실제 C_F 크기, 실제 endpoint split의 유용성 및 HH feasibility는 미측정이다.

검토 중 HH 배열·상수·integral·callback 및 frozen comparator는 실행하지
않았다. 구현을 수정하지 않았으며 이 디렉터리의 검토 증거만 작성했다.
