# T5 최종 entry enclosure → 오차·gap 조합기

이 모듈은 G7–G8 사이의 실제 수치 조합 부품이다. 고정된 47×2/2×47 raw/model 행렬과 **이미 계산된 최종 entry 복소 disk**를 받아 exact rational Gram 계산으로 source discrepancy와 모델 비교의 조건부 구간을 반환한다. HH 적분기, 최종 disk 생산기, native/ABI 인증기 또는 완성된 production HH solver는 아니다. 실제 HH 입력·적분 실행은 이번 검증에 포함되지 않았다.

## 실행

저장소 root에서 Python 표준 라이브러리만 필요하다. 이전 frozen Gram 파일은 아래 고정 위치에 있어야 한다.

```bash
COMPONENT=research/r31ao_unequal_ladder/production_solver_20261001_v1/composition
RUN_DIR=$(mktemp -d)
python "$COMPONENT/adapter.py" \
  --input "$COMPONENT/evidence_final/SYNTHETIC_INPUT.json" \
  --output "$RUN_DIR/T5_RESULT.json"
python "$COMPONENT/test_composition.py"
```

`--output`을 생략하면 단일 JSON이 stdout으로 나온다. 파일 출력은 create-only atomic link로 게시하며 기존 파일을 대체하지 않는다. 실패는 exit 2와 stderr JSON으로 반환한다. dependency source hash 불일치는 수치 실행 전에 import를 거부한다. 출력 파일을 생성한 뒤 전원 차단 복구성까지 검증한 것은 아니다.

API는 `adapter.compose(request_dict)` 또는 `adapter.compose(adapter.parse_request(utf8_bytes))`이다. 성공 반환물은 JSON으로 직렬화할 수 있는 dict이고 malformed input과 resource 초과는 각각 `ContractError`, `ResourceLimit`이다. 입력 parser를 통하면 중복 key, JSON float, NaN/Infinity가 모두 거부된다. dict API의 경우 caller가 dict를 만들기 전 발생한 메모리 비용은 이 모듈이 제한할 수 없다.

## 입력 계약

root 필수 key는 `schema`, `inputs`다. schema는 `WU088_T5_COMPOSITION_REQUEST_V1`이다. 선택 key는 `precision`, `limits`, `evidence_refs`뿐이며 다른 key를 거부한다.

`inputs`는 정확히 `raw`, `models`, `target_disks`다. 각각 `{"sha256":"<lowercase 64 hex>","data":...}` envelope이며 SHA는 `json.dumps(data, sort_keys=True, separators=(',', ':'), ensure_ascii=True, allow_nan=False).encode('utf-8')`의 SHA-256이다. `adapter.bind(data)`가 같은 envelope를 생성한다. hash가 일치해도 자료의 역사적 출처나 과학적 의미가 인증되지는 않는다.

| data object | 정확히 요구하는 내용 |
|---|---|
| raw | `D_col`: 47×2, `D_row`: 2×47 |
| models | `R31AK`, `R31Z`, `R31AD`; 각각 `D_col`:47×2, `D_row`:2×47, **독립 저장 `K`:47×2** |
| target_disks | `D_col`:47×2, `D_row`:2×47; cell은 `{"center":["re","im"],"radius":"r"}` |

각 exact complex cell은 두 rational string의 list다. canonical token은 `"0"`, `"-3"`, `"1/2"`처럼 기약분수·양의 분모를 쓴다. `"2/4"`, `"1/1"`, `"-0"`, decimal string, JSON integer/float/bool 값은 rational cell에서 거부한다. disk radius는 음수가 아니어야 한다. 모든 배열은 명시적 row-major nested list이며 shape 추론·transpose·symmetrization은 하지 않는다.

`evidence_refs`에는 `target_binding_sha256`, `historical_abi_sha256`, `final_entry_certificate_sha256`, `model_identity_sha256`의 SHA string만 기록할 수 있다. 이 필드는 단순 문서 참조이며 admission flag를 받지 않는다. 어떠한 입력으로도 이 모듈의 `rigorous`, `project_certification`, `production_admitted`가 true가 되지 않는다.

기본 `precision=128`은 **radical의 절대 dyadic grid 2^(-128)**을 뜻한다. 전체 matrix norm의 128-bit 상대 정확도를 보장하는 표기가 아니다. `limits`는 다음 hard cap을 낮출 수만 있다: `max_precision=4096`, `max_integer_bits=8192`, `max_work_bits=32768`, `max_operations=150000`. document 크기는 2 MiB 이하이다. exact 연산 budget은 모든 source/model norm과 조합을 통틀어 하나를 공유한다. 한도를 넘기면 tolerance 완화나 binary64 대체 없이 실패한다. wall-clock hard timeout은 외부 host runner가 별도로 제공해야 한다.

## 수식과 출력의 대응

T5의 `A=D0-c`, `rho=sqrt(sum(r_ij^2))`를 사용해 exact two-column/two-row Gram norm `[s-,s+]`을 계산하고 `[max(0,s--rho_upper),s++rho_upper]`를 반환한다. Frobenius는 disk uncertainty에만 적용한다. 비영 center residual을 Frobenius norm으로 대체하지 않는다.

raw `K0=(C0-R0†)/2`와 target disk `cK=(cC-conj(cRᵀ))/2`, `rK=(rC+rRᵀ)/2`를 구성한다. 따라서 고정 center residual의 K cancellation이 보존된다. `epsilon.D_col=UC`, `epsilon.D_row=UR`, `epsilon.K=min(UK,(UC+UR)/2)`, `epsilon.Dmax=max(UC,UR)`이다. 모델 K는 입력값을 그대로 사용한다.

각 모델의 target error interval, represented raw error interval을 따로 계산한다. PRIMARY는 R31Z−R31AK, SECONDARY는 R31AD−R31AK이다. 각 K/Dmax gap에 대해 direct target interval과 represented gap±2epsilon의 **교집합**을 반환한다. 빈 교집합은 실패다. legacy eta나 X0…X8를 다시 더하지 않는다.

real sufficient condition은 교집합의 lower endpoint를 사용한 `모든 gap >= -tol` 및 `적어도 하나 gap > tol`이다. tol은 frozen binary64 token `0x3ddb7cdfd9d7bdbb`의 **정확한 실수값**이다. strict equality는 improvement가 아니다. 이 real predicate는 원 archived floating predicate의 연산별 rounding replay와 별도다. conditional sufficient / conditional not-supported / unresolved를 구별한다.

결과는 `source_residuals`, `epsilon`, `represented_model_errors`, `target_model_errors`, `comparisons`, `identity`, `arithmetic`, `admission`, `execution`을 포함한다. 모든 interval endpoint는 exact rational string이다. 입력 envelope identity와 전체 canonical request hash, adapter/Gram source hash, 실제 사용 exact-operation count가 들어간다.

## 의존성과 검증 범위

frozen source: `gap_closure_20261001_g0_g6_v1/exact_gram/engine.py`, SHA-256 `e10f206d63be1a99a441780108619574605014a9b01b3b327e21fecb18c5b9cc`. 전체 연산 budget을 공유하려고 이 **고정 구현**의 `_Work`, `_norm`, `_subtract`, `_sqrt`, `_k`를 사용한다. 이 결합은 version/hash로 제한되며 임의 최신 engine과 호환된다고 가정하지 않는다.

수학적 근거: `theory_closure_20261001_v1/T5_SHARP_RESIDUAL_CERTIFICATE.md`, SHA-256 `c1c4a372e83ea161065f580f75f20e705780797d0ce59b4a372d1f5c6746992a`. 이번에는 정리를 새로 주장하거나 재증명하지 않고 조합 경로를 구현했다.

검증은 47×2/2×47 analytic synthetic fixtures의 `aI₂` spectral/Frobenius 반례, 비영 disk radius, K cancellation, independent model K, 복소 conjugation, 직접 gap 교집합, frozen real tolerance 경계, identity·schema·resource·create-only 거부 동작이다. 기존 59개 테스트나 HH science suite를 재실행하지 않았다. 실제 최종 disk 생성, historical ABI, source input binding, native backend 및 독립 최종 decision review는 외부 gate로 남는다.
