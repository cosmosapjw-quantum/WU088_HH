# 식–자료–코드 대응

이 단위는 literal thermal probability의 outward enclosure와 유한 시간 전파자 certificate를 연결한다. 원천은 고정 LAMDA HD 100 K para-H₂의 9개 준위·9개 downward pair이고, source·parser identity는 `CONTRACT.json`과 생산 결과에 함께 기록한다.

| 정의·식 | 실제 자료 또는 함수 | 입력·출력 계약 |
|---|---|---|
| (z_i=100h_Pc(\tilde\nu_i-\tilde\nu_0)/(k_BT)) | `native_hd_source` → `thermal_from_levels` | source decimal 파수, degeneracy, native (T=100\,K); exact rational exponent |
| (e^{-z}\in[e_-,e_+]) | `exp_neg`, `exp_neg_interval` | (0\le z\le256), 128–768 bits; 교대 Taylor bracket 후 outward dyadic squaring |
| (w_i=g_ie^{-z_i}), normalized weight-box extrema | `normalize_weights` | 모든 weight lower bound (>0); 실제 simplex를 포함하는 좌표별 구간 |
| (\pi_u/\pi_l=(g_u/g_l)e^{-(z_u-z_l)}) | `pair_ratio` | normalized box 재나눗셈 없이 shared Gibbs ratio 사용 |
| Source downward / (10^{-11}\,\mathrm{cm^3s^{-1}}) | `native_hd_source` | 무차원 (K), (\tau=n_{coll}\kappa_{ref}t); density는 미입력 |
| Conservative generator diagonals | `GeneratorBox`, `generator_from_offdiagonal` | lower diagonal = minus upper exit; upper diagonal = minus lower exit |
| (A=K+\pi(v-\kappa1)^T-\mathrm{diag}(v-\kappa1)) | `reset_generator_bounds` | full (A)를 구성; (\pi) simplex enclosure, (v_j^-\ge\kappa\ge0) |
| (P_-=I+A/\lambda)의 공통 성분별 하한 | `uniformization_lower` | (\lambda\ge\max\mathrm{exit}^+); 기본값은 (2\max\mathrm{exit}^+), zero-exit이면 1 |
| (R_N\le e^{-\lambda H}\sum_{m=0}^N(\lambda H)^mP_-^m/m!\) | `finite_block` | nonnegative fixed-denominator 연산을 모두 아래로 반올림; (R_N) 실제 matrix 반환 |
| (\beta=\min_{j<k}\sum_i\min(R_{ij},R_{ik}),\rho=1-\beta) | `_overlap_integer` | (n\ge2) 실제 pair overlap; (n=1)은 zero-space 규약 (\beta=1,\rho=0) |
| (M^*=M+F_+H, G=q_cM^*+g) | `forced_step` | interval-wide coefficient bounds, 정확한 source·clock binding은 caller 책임 |
| (\widehat U^+=\rho\widehat U/(1+\kappa H)+GH, \widehat U^*=\widehat U+GH) | `forced_step` | `endpoint.U`와 `whole_block.U`가 별도 출력 |
| (I_U=H\widehat U+GH^2/2, E^+=E/(1+bH)+s_+I_U) | `forced_step` | `integral_U_bound`; `whole_block.E=E+s_+I_U` |
| Constant synthetic (c=K\pi-v\pi+\pi\bar v, Qf=f-\pi F) | `constant_coefficients` | exact (q_c=\|c\|_1,g=\|Qf\|_1,k=\min v,b=\bar v,s_+=\mathrm{osc}(v)/2) |

## Claim과 실행의 연결

정리의 가정·증명은 `INTERVAL_BLOCK_PROOF_KO.md`, 단위와 runtime 입력은 `verification/PRIMARY_INPUT.json`, 코드 오차방향은 `verification/NUMERICAL_DESIGN.md`에 연결된다. `verification/run_primary.py`는 그 고정 입력을 읽고 `raw/PRIMARY_RESULTS.json`에 exact endpoints, matrix, overlap, 비교 수열, source/code/input hashes와 실제 검증 결과를 export한다.

독립 reference는 이 JSON과 원 source bytes를 읽는다. 생산 코어를 import하지 않고 고정 source의 고정밀 열확률과 별도 행렬지수로 대조한다. Numeric reference의 반올림 허용치는 rational certificate의 endpoint를 넓히는 데 사용하지 않는다.

## 적용 경계

`native_hd_source`는 기존 REC parser의 `parse_hd`만 재사용하며, binary64 `upward_rate`와 기존 diagnostics는 호출하지 않는다. Radiative frequency bridge와 그 기존 35 Hz gate는 이 graph construction의 입력이 아니다. 미제공 transition은 `MISSING_NOT_ZERO`, 진동상태는 `UNSPECIFIED`로 남는다.

실제 열확률의 shared Gibbs correlation은 (K\pi=0)을 만든다. 독립 interval box의 모든 corner를 동일 equilibrium로 취급하지 않는다. 일반 reset·forcing 함수는 공급된 coefficient bounds 아래의 수학적 certificate를 제공하며, GL2022 destruction array와 named consumer는 후속 입력 계약에 남는다.
