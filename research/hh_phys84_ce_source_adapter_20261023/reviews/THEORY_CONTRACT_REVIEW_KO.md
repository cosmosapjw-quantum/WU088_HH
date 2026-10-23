# PHYS84 이론·코딩 계약 사전 독립 검토

Reviewer: `/root/central_contract_review`. 읽기 전용 검토이며 코드 구현·과학 callback·이전 검증 재실행은 0이다. 검토 대상은 WU 새 unit `research/hh_phys84_ce_source_adapter_20261023/CONTRACT.json` 및 `theory/INSTANTANEOUS_SOURCE_DERIVATION_KO.md`다. 같은 검토자가 앞서 중앙 계약·consumer mapping을 검토했으며 이번 생산 코드의 작성자가 아니다. 이 문서는 구현 후 C9 admission을 대신하지 않는다.

## 최초 검토 identity

| 파일 | bytes | SHA256 |
|---|---:|---|
| CONTRACT.json | 8941 | 8642b5bbb77801836d2d81d838e7e6cc2b0b402b0df9736cb720b845b55f99c0 |
| theory/INSTANTANEOUS_SOURCE_DERIVATION_KO.md | 8750 | 042444e2155485ca8e3ac838286fa5c31bf29f2e9548d6af977f8be8247b992d |

## 이론과 범위 판정

**DERIVATION_PASS_SCOPED.** 원 중앙 첫 노드의 'owner completion ingest 이후 별도 consumer PR'와 맞는 WU local supplier-consumer 연결이다. PHYS83 final/과학 identity와 exact saved rows를 유지하고, 원 source의 255–50000K·finite native LS·heavy-stationary/unpolarized Maxwellian 가정을 바꾸지 않는다. 16행 application은 constructed instantaneous states와 두 장부 route이며 새 rate solve 또는 cosmological history가 아니다. REI-L1 admission을 발행하지 않는 경계가 명시되어 있다.

각 CE up column은 ground -1, upper +1, thermal -Delta, excitation +Delta다. Reverse column은 그 반대다. Radiative column은 upper -1, ground +1, excitation -Delta, 선택된 radiation destination +Delta다. 모든 열에서 nuclei/neutral-atom 수는 보존되며 free electron은 전후 같은 수이므로 net electron source=0이다. 따라서 thermal gas particle-number source도0이며, Uth=(3/2)kB Nthermal T의 사건 미분에서 Tdot=2Qthermal/(3kB Nthermal)이 따른다.

이 검토에서 식으로 확인한 핵심 대응은 (0,Delta,Delta)S=e_exc, 1^TS=0, e_th+e_exc+e_rad=0이다. Ground chemical binding은 전체 HI 수에만 비례하므로 source0인 반면, excitation은 explicit reservoir로 유지된다. Bound-bound event에 reaction-selected incoming electron energy를 추가 손실로 또 넣지 않는 것도 적절하다.

`immediate_escape`와 `emissivity_handoff`는 하나의 Qemit을 다른 destination에 배정하는 배타적 표현이다. Qemit은 진단량이며 두 destination에 동시 적립하거나 conservation sum에 추가하지 않는다. Native owner 동시 활성 거부와 explicit excited-state owner 요구는 이 물리적 double count를 직접 방지한다. 2gamma의 energy Delta와 photon count2, M1/E1의 별도 branching, spectrum 미공급 경계 모두 맞다.

Positivity 주장도 frozen nonnegative rates의 instantaneous vector field에 한정하면 맞다. 각 state가0일 때 해당 state를 소비하는 intensity가0이 되어 off-diagonal inflow만 남는다. 이 식의 positivity는 실제 적분기나 finite-step positivity를 검증했다는 뜻이 아니다.

원 saved CSV를 read-only로 확인하여 네 application T labels255.0/10000.0/25370.66308424773/50000.0이 각각 정확히 두 upper-level rows를 갖는 것을 확인했다. 이 작업은 새 rate 평가가 아니다. Wolfram 저장 응답도 읽었다. 첫 call의 nuclei7 + energy7 + differential/thermal/steady3=17 zero와 replacement syntax로 미평가된 두 항이 명확히 구별되고, targeted repair의 두 zero가 별도로 보존되어 있다.

## 코드 실행 전 닫을 최소 계약 명확화

### F1 — signed output 검증의 분모를 명시

대상: `acceptance.event_and_resolved_output_relative`, `signed_sum_error_over_gross`.

현재 문구만으로는 near-cancelled level derivative/Qthermal/Uexc_dot/Tdot에도 relative2e-12가 동시에 적용되는지 불명확하다. Signed cancellation 결과의 작은 참값으로 나눈 상대오차는 해당 source의 정확도를 잘못 거부할 수 있다. 새 허용오차를 완화할 일이 아니라, 실행 전에 본래 의도한 조건의 적용 대상을 확정해야 한다.

최소 교정: positive event intensities 및 nonnegative resolved emission/photon quantities에는 relative2e-12를 적용한다. 각 signed source는 해당 independent unsigned contribution sum을 gross로 사용해 error/gross<=2e-13을 적용한다. Tdot은 thermal-energy gross를 같은 2/(3kB Nthermal) 계수로 변환한 scale을 사용한다. Gross=0일 때는 expected/actual이 모두 exact0이라는 규칙을 명시한다. Nuclei/energy residual의 gross 정의도 exact 이름으로 고정한다.

### F2 — incremental 실행 cap과 count 분류 확정

대상: resources_and_budget, application.maximum_new_runs.

1worker/thread와0.5GiB·16rows는 명시됐지만 validation/application의 CPU/wall 상한이 없다. 중앙의 unknown inherited budget을 새 허용량으로 처리할 수 없으므로, controller가 이번 작은 algebra/guard 검증과 one application의 독립적인 incremental caps 및 중단 조건을 freeze해야 한다. 기존 science의 시간이나 금액 잔여를 새 cap으로 돌리지 않는다.

또한 production application1회와 test-only mocked guard/resume/corruption callbacks를 구별하여 maximum_new_runs=1을 해석하도록 명시한다. 실제 성공·실패·중단 비용은 각각 보존한다. 이 finding은 새 heavy campaign이나 폭넓은 검증을 요구하지 않는다.

### F3 — 여섯 energy column과 온도 평가 순서를 명시

대상: implementation.output와 positive Nthermal numerical domain.

현재 'six energy columns'의 정확한 이름·순서를 명시하면 coder가 Qemit diagnostic을 일곱 번째 에너지로 더하는 실수를 피할 수 있다. 권고 columns는 thermal, ground_binding, excitation, radiation_injected, escaped, source_reservoir다. Qemitted는 별도 diagnostic이다.

Nthermal은 모든 positive finite 값을 허용한다. subnormal Nthermal에서 `3*kB*Nthermal`을 먼저 만들면0이 될 수 있다. 계약에 안정적 순서 `Tdot=(2/(3*kB))*(Qthermal/Nthermal)` 및 Qthermal==0일 때0을 명시하거나 numerical Nthermal lower bound를 명시하면 된다. 식과 허용 physics를 바꿀 필요는 없다. Density upper1e18/Nthermal upper1e20은 event upper magnitudes를 finite 범위에 두며, tiny positive event underflow는 기존 명시적 rejection을 유지하면 된다.

### F4 — positivity 문장의 부정 오기

유도문 '모든 입력과 rates가 비음수가 아니므로 intensity는 비음수가 아니다'는 의도와 반대로 쓰였다. '모든 입력과 rates가 비음수이므로 intensity도 비음수다'로 고친다. 행렬·코드 수용 기준의 변경이 아니다.

## 사전 판정과 stopping rule

물리 유도와 중앙 scope에는 blocking contradiction이 없다. F1/F2의 실행 계약 명확화 및 F3/F4의 작은 정의·문구 교정 뒤 사전 coding freeze를 PASS_SCOPED로 닫을 수 있다. 같은 이론에 새 계산이나 원 science 재실행은 필요하지 않다. 교정된 네 위치의 readback만 수행하고, lower-tier coder에게 실제 구현/targeted checks를 넘긴다. 구현 후 fresh diff/raw outcomes 기반 C9 review는 별도다.

HH_R10=OFF, production admission=NOT_ISSUED, REI-L1 external consumer admission=NOT_ISSUED.

## Revision2 readback — 사전 gate 종료

최초 finding과 identity는 위에 그대로 보존했다. Controller가 수정한 다음 원문을 실제 다시 읽고 별도 snapshot으로 보존했다.

| 파일 | bytes | SHA256 |
|---|---:|---|
| CONTRACT_REVIEWED_REV2.json | 12459 | 01528db5b31bd27cb0a9ae623b92cd0821ac4b42bfb4b3792ce3cc56c6e8280f |
| DERIVATION_REVIEWED_REV2.md | 9223 | 11a7ce2519eb5dab598d5d14d66132d71c0d0928e696f54eb1dcf0ea8eb453d3 |

- **F1 CLOSED before implementation.** Positive event/radiation/photon relative gate2e-12가 signed source gate에서 분리됐다. G_event, G_energy, G_thermal, G_temperature, 각 signed-output 분모와 zero-gross exact-zero 규칙이 명시됐다. 물리 식과 허용오차 숫자는 바뀌지 않았다.
- **F2 CLOSED before implementation.** Verification CPU30/wall60초, one application CPU10/wall20초, resume CPU10/wall20초의 bounded child-process caps가 명시됐다. Mocked guards와 byte-verified resume를 real16row application count에서 분리하고 모든 실패 비용 보존을 유지한다. Unknown inherited monetary budget은 그대로 null이다.
- **F3 CLOSED before implementation.** Six energy columns가 `gas_thermal, chemical_binding, atomic_excitation, radiation_injected, escaped_radiation, source_reservoir`로 고정됐고 Qemitted는 별도 diagnostic이다. Qthermal=0일 때 Tdot0, 나머지는 `(2/(3*kB))*(Qthermal/Nthermal)`로 평가하며 nonfinite/positive-magnitude underflow를 거부한다. Largest-first positive product 및 exact-zero factor 규칙도 명시됐다.
- **F4 CLOSED before implementation.** Nonnegativity 문장이 의도한 양성 statement로 교정됐다.

**최종 사전 판정: PASS_SCOPED_THEORY_AND_PREIMPLEMENTATION_CONTRACT.** 남은 사전 blocking finding은0이다. Root는 이 revision2의 정확한 identity와 허용 경로/명령/자원/중단 조건을 lower-tier coding agent에 넘겨 C5–C8을 수행할 수 있다. 새 구현 자체의 admission과 실제 one application의 성공은 이 문서가 선취하지 않는다. 이후 C9는 actual diff와 raw outcomes만 검토하고 변경되지 않은 이론 검증을 반복할 필요가 없다.
