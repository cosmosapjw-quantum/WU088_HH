# Authorized z=0.75 one-shot result

PRIMARY: `PARETO_SUPPORTED_AT_Z075`. SECONDARY: `REFINED_PARETO_SUPPORTED_AT_Z075`.

R31AM action: `FREEZE_R31AK_LOCALLY_SUPPORTED__PIVOT_TO_REFERENCE_CERTIFICATION`.

z=0.75 a0, B192, producer tau=1.6769079292753585025 t_a. OD/JVP 각 한 번, 총 science geometry 한 개. 두 stage와 두 frozen comparator는 exit0이다. 첫 scientific checkpoint identity 생성 시 authorization consumed이며 동일 envelope rerun은 금지한다.

E_O는 무차원이며 나머지 error columns는 /t_a이다.

| Model | E_O | E_dotO | E_K | E_Dcol | E_Drow | E_Dmax |
|---|---:|---:|---:|---:|---:|---:|
| R31AK refined | 0.00957990603074 | 0.00598194686738 | 0.0525049663293 | 0.0505295929748 | 0.0545728417481 | 0.0545728417481 |
| R31Z global | 0.154933224042 | 0.156820559614 | 0.372328401985 | 0.372808409023 | 0.388029782324 | 0.388029782324 |
| R31AD coarse | 0.047266081974 | 0.124186245528 | 0.109637386456 | 0.107125797233 | 0.142393428128 | 0.142393428128 |

Refined-vs-coarse improvement fractions: {"E_O": 0.7973196501455782, "E_dotO_per_ta": 0.9518308421197873, "E_K_per_ta": 0.5211034481335647, "E_Dcol_per_ta": 0.5283153611945298, "E_Drow_per_ta": 0.6167460642983429, "E_Dmax_per_ta": 0.6167460642983429}

Direct raw-first residual 2-norm: 4.700260169972803e-19. Direct cast-first residual 2-norm: 1.15333442561526e-16. Raw maxabs: 2.5883276071860052388e-19. Frozen comparators의 서로 다른 arithmetic order를 그대로 유지했다. Residual은 source-error bound가 아니다.

같은 direct geometry를 공유하는 primary/secondary evidence count는 1이다. Fresh single-point relative comparison 및 [0.5,1] local h-refinement gain scope이며, z0.75는 training으로 소비하지 않았다. R31AK state는 freeze한다. 자동 knot, successor, 다음 node, B-order run은 실행하지 않는다.

SOURCE_ACCURACY_BOUND_UNAVAILABLE, B-order/reference certification, full-cell authority, fixed-Q complete-HH physical invariance, BR01/BR02, independent project review, production gates를 유지한다. 다음 research axis는 별도의 명시적 결정이다. Interval-wide accuracy, all-cell gain, transition error, trajectory, H-skip을 승인하지 않는다.

Raw O/D_col/D_row/dotO는 complex256으로 보존했다. Frozen source/model/rule/metadata hashes는 output 전후 동일하다. Raw restore는 수행하지 않았으며 RESTORE_VERIFIED=false다.
