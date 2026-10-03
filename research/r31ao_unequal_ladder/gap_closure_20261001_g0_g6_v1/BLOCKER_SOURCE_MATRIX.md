# Blocker → source → 구현 → 남은 의무

기준 HEAD: `393eb882f7fbf160cfb465849d9652c7b026b5be`. Source ID는 `catalog:`와 `source_map:` namespace를 구분한다. 아래 component 완료는 실제 HH certificate 완료가 아니다.

| Blocker | 현재 상태 | 구현·검증 포인터 | 남은 실제 gate |
|---|---|---|---|
| B01 | native draft / static reviewed | BACKEND_IDENTITY.json; CALLBACK_VERIFICATION.json; FROZEN_INPUT_ADAPTER_VERIFICATION.json | pinned host build, ABI, binary identity, native acceptance |
| B02 | generic endpoint·synthetic interior 구현 검증 | ENDPOINT_BOUND_VERIFICATION.json; FEASIBILITY_LEDGER.json | actual endpoint/interior/O/G/D balls와 epsilon |
| B03 | synthetic decoder 구현 검증 | RAW_DECODER_VERIFICATION.json; RAW_ABI_AUTHORITY.json | historical serializer-to-output ABI authority; authorized exact decode |
| B04 | exact arithmetic·separate predicates 검증 | GRAM_ENGINE_VERIFICATION.json; REPRESENTED_GAP_CONTRACT.json | actual model/raw gap intervals와 authenticated scalar trace |
| B05 | synthetic width/work/resource 측정 | INTERIOR_PILOT_REPORT.md; host_guard/README_KO.md | actual HH feasibility 및 native resource acceptance |
| B06 | IRRELEVANT_BY_SELECTED_ROUTE | continuous-target route | stored-rule alternative를 다시 선택할 때만 authority 필요 |

## Sub-obligation authority crosswalk

| 의무 | 요구사항 | 문헌 authority | 현재 상태 |
|---|---|---|---|
| B01.01 | exact_target_callback | catalog:C01, catalog:D01, catalog:D07, catalog:D08, catalog:P01, catalog:P02, catalog:C08, catalog:C09 | NATIVE_IMPLEMENTATION_AND_STATIC_CHECKS_ONLY_RUNTIME_UNVERIFIED |
| B01.02 | FLINT_3_4_0_pin | catalog:C01, catalog:D01, catalog:D07, catalog:D08, catalog:P01, catalog:P02, catalog:C08, catalog:C09 | SOURCE_ARCHIVE_IDENTITY_VERIFIED |
| B01.03 | GMP_MPFR_dependency_identity | catalog:C01, catalog:D01, catalog:D07, catalog:D08, catalog:P01, catalog:P02, catalog:C08, catalog:C09 | SOURCE_ARCHIVE_IDENTITY_VERIFIED |
| B01.04 | compiler_flags_ABI_binary_identity | catalog:C01, catalog:D01, catalog:D07, catalog:D08, catalog:P01, catalog:P02, catalog:C08, catalog:C09 | BLOCKED_HOST_BUILD_NOT_RUN |
| B01.05 | branch_domain_guards | catalog:C01, catalog:D01, catalog:D07, catalog:D08, catalog:P01, catalog:P02, catalog:C08, catalog:C09 | NATIVE_IMPLEMENTATION_AND_STATIC_CHECKS_ONLY_RUNTIME_UNVERIFIED |
| B01.06 | outward_semantics | catalog:C01, catalog:D01, catalog:D07, catalog:D08, catalog:P01, catalog:P02, catalog:C08, catalog:C09 | NATIVE_IMPLEMENTATION_AND_STATIC_CHECKS_ONLY_RUNTIME_UNVERIFIED |
| B01.07 | callback_synthetic_and_host_tests | catalog:C01, catalog:D01, catalog:D07, catalog:D08, catalog:P01, catalog:P02, catalog:C08, catalog:C09 | NATIVE_IMPLEMENTATION_AND_STATIC_CHECKS_ONLY_RUNTIME_UNVERIFIED |
| B02.01 | finite_endpoint_selection | catalog:P01, catalog:P03, catalog:P04, catalog:P06, catalog:D05, catalog:C01 | FINITE_DESIGN_CANDIDATE_PREDECLARED_NOT_EVALUATED |
| B02.02 | Hermite_Gaussian_constants | catalog:P01, catalog:P03, catalog:P04, catalog:P06, catalog:D05, catalog:C01 | GENERIC_EVALUATOR_IMPLEMENTATION_VERIFIED_SYNTHETIC_ONLY |
| B02.03 | compact_uniform_interior_enclosure | catalog:P01, catalog:P03, catalog:P04, catalog:P06, catalog:D05, catalog:C01 | SYNTHETIC_RANGE_METHOD_VERIFIED_NATIVE_PETRAS_DRAFT_UNVERIFIED |
| B02.04 | O_G_balls | catalog:P01, catalog:P03, catalog:P04, catalog:P06, catalog:D05, catalog:C01 | ACTUAL_HH_NOT_EVALUATED |
| B02.05 | source_assembly_D_entry_balls | catalog:P01, catalog:P03, catalog:P04, catalog:P06, catalog:D05, catalog:C01 | SOURCE_BOUND_ASSEMBLY_DRAFT_STATIC_CHECKED_ACTUAL_BALLS_ABSENT |
| B02.06 | epsilon_C_R | catalog:P01, catalog:P03, catalog:P04, catalog:P06, catalog:D05, catalog:C01 | ACTUAL_HH_NOT_EVALUATED |
| B03.01 | NPY_v1_v2_v3_parser | catalog:C04, catalog:D03 | IMPLEMENTATION_VERIFIED_SYNTHETIC_ONLY |
| B03.02 | historical_producer_ABI_binding | catalog:C04, catalog:D03 | RAW_ABI_AUTHORITY_BLOCKED |
| B03.03 | endian_and_component_layout | catalog:C04, catalog:D03 | IMPLEMENTATION_VERIFIED_SYNTHETIC_ONLY |
| B03.04 | padding_nonfinite_subnormal_signed_zero | catalog:C04, catalog:D03 | IMPLEMENTATION_VERIFIED_SYNTHETIC_ONLY |
| B03.05 | C_Fortran_index_mapping | catalog:C04, catalog:D03 | IMPLEMENTATION_VERIFIED_SYNTHETIC_ONLY |
| B03.06 | golden_fixtures_canonical_dyadic_hash | catalog:C04, catalog:D03 | IMPLEMENTATION_VERIFIED_SYNTHETIC_ONLY |
| B03.07 | actual_raw_decode | catalog:C04, catalog:D03 | ACTUAL_RAW_DECODE_NOT_EXECUTED |
| B04.01 | exact_Gram_accumulation | catalog:P07, catalog:P08, catalog:C04, catalog:C08 | IMPLEMENTATION_VERIFIED_SYNTHETIC_ONLY |
| B04.02 | outward_square_roots | catalog:P07, catalog:P08, catalog:C04, catalog:C08 | IMPLEMENTATION_VERIFIED_SYNTHETIC_ONLY |
| B04.03 | K_Dmax_models_gap | catalog:P07, catalog:P08, catalog:C04, catalog:C08 | IMPLEMENTATION_VERIFIED_SYNTHETIC_ONLY |
| B04.04 | direct_gminus_and_legacy_eta | catalog:P07, catalog:P08, catalog:C04, catalog:C08 | IMPLEMENTATION_VERIFIED_SYNTHETIC_ONLY |
| B04.05 | frozen_binary64_predicate_boundary | catalog:P07, catalog:P08, catalog:C04, catalog:C08 | IMPLEMENTATION_VERIFIED_SYNTHETIC_ONLY |
| B04.06 | actual_represented_gap_intervals | catalog:P07, catalog:P08, catalog:C04, catalog:C08 | ACTUAL_GAPS_NOT_EVALUATED |
| B05.01 | actual_HH_width | catalog:P01, catalog:P03, catalog:P04, catalog:P05, catalog:P06, catalog:P11 | ACTUAL_HH_UNMEASURED |
| B05.02 | endpoint_conservatism_dependency | catalog:P01, catalog:P03, catalog:P04, catalog:P05, catalog:P06, catalog:P11 | ACTUAL_HH_UNMEASURED |
| B05.03 | precision_evaluation_subdivision_caps | catalog:P01, catalog:P03, catalog:P04, catalog:P05, catalog:P06, catalog:P11 | SYNTHETIC_GUARDS_MEASURED_ACTUAL_HH_UNMEASURED |
| B05.04 | wall_memory_measurement | catalog:P01, catalog:P03, catalog:P04, catalog:P05, catalog:P06, catalog:P11 | SYNTHETIC_GUARDS_MEASURED_ACTUAL_HH_UNMEASURED |
| B05.05 | termination_and_fail_closed_inconclusive | catalog:P01, catalog:P03, catalog:P04, catalog:P05, catalog:P06, catalog:P11 | SYNTHETIC_GUARDS_MEASURED_ACTUAL_HH_UNMEASURED |
| B05.06 | selected_method_feasibility | catalog:P01, catalog:P03, catalog:P04, catalog:P05, catalog:P06, catalog:P11 | ACTUAL_HH_UNMEASURED |
| B06.01 | executed_OD_base_weight_bytes | catalog:P06, catalog:P10 | IRRELEVANT_BY_SELECTED_ROUTE |
| B06.02 | node_weight_hash | catalog:P06, catalog:P10 | IRRELEVANT_BY_SELECTED_ROUTE |
| B06.03 | measure_tensor_ordering | catalog:P06, catalog:P10 | IRRELEVANT_BY_SELECTED_ROUTE |
| B06.04 | generation_identity | catalog:P06, catalog:P10 | IRRELEVANT_BY_SELECTED_ROUTE |

문헌 보유만으로 HH adaptation/runtime 전제를 닫지 않는다. INTLAB/COSY 미확보는 현재 exact Gram/Petras 경로의 필수 blocker가 아니다. P04는 author manuscript representation으로 보존하고 publisher-final 동일성을 주장하지 않는다.
