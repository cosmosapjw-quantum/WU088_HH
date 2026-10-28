# R15 production API and shared reference interface — C2

Status: authored input/output contract before implementation or scientific execution. Root owns canonical adoption, freeze and runs. Unit contract: WU_CUBIC_BERNSTEIN_FORCING_R15, parent R14 FINAL6ca324dbc5d3c4b5c064f7621730eb0d6ee5eb51. Workflow1.0.0 with integrated policy1.3.0.

## Input and exact representation

The public calculation is `run_case(case)` in the planned `src/cubic_convolution.py`. Its input keys preserve R14 naming:

    states, q, tau, c, d, initial, source_knots, observation_knots,
    g_r, g_e, binding, certificate

`d` means signed scalar d_c. `c>=0` is the comparison coupling. `initial=[R0,E0]` is nonnegative. Source and observation knots strictly increase and share t0/T. Each g_r/g_e row contains exactly four nonnegative Bernstein-B3 coefficients in the original source cell's normalized coordinate. This explicitly supplied coefficient cone is the input domain. There is no source-vertex preprocessing or assertion that every nonnegative cubic belongs to this cone.

JSON scalars are integers or ASCII signed integer / signed p/q strings of at most2048characters. Booleans, floats, whitespace, decimal and exponent text are rejected before numerical conversion. Numerator/denominator input bit length is at most256; denominator must be nonzero. Internal Fraction inputs may be accepted by the Python API with the same bound. Derived exact rationals are at most16384bits per component. The dedicated process uses finite integer string limit6000; emitted derived rational strings are at most10000characters and are reduced integer or p/q strings.

States lie in1..13. A singleton zero-mass model requires R0=0 and all g_r coefficients=0. Source cells<=16; observation cells<=32; base cells<=512; floor((T-t0)/tau)<=8; abs(d)*(T-t0)<=16. Tau>0,0<=q<=1. The `caps`, `cap`, `point_caps` and `whole_caps` fields are rejected: no cap adapter is part of R15.

## Binding and certificate

Binding identity fields are source_id,clock_id,clock_unit,full_A_family_id,source_locator,source_sha256,whole_forcing_source_sha256,scientific_status,state_order,whole_forcing_hash_format. The certificate repeats these fields exactly. Scientific status is ARITHMETIC_CONTROL_PREMISE or CERTIFIED_FULL_A_BLOCK; declared metadata never manufactures physical source verification.

`whole_forcing_hash_format` is WU_R15_WHOLE_FORCING_V1. The hash payload is

    {schema,source_id,clock_id,clock_unit,state_order,source_knots,g_r,g_e}

with scalar arrays normalized to reduced rational strings. Hash bytes are UTF-8 `json.dumps(payload,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n'`. The schema value is WU_R15_WHOLE_FORCING_V1. The source ID, clock and state order therefore participate in the forcing identity.

The certificate generator is `A=K+wH;H=pi*d^T-diag(d)`. Required true flags are fixed_K_pi_d,full_w_box,all_start_times,zero_mass_residual,short_remainder_nonexpansive,forcing_whole_fine_coarse_domain. Certificate q,tau,t0,T equal the input; w_box is an ordered nonnegative exact pair. Fixed K/pi/destruction, whole-w/all-starts and original source/state/clock retain the parent premise semantics.

## Base clock and comparison quantities

The exact base grid is the sorted union of observation knots and original source knots+k*tau inside[t0,T], k=0..B. This includes all initial kernel jumps. Extrema subdivision points do not enter this clock.

    h(age)=q^floor(age/tau), h(0)=1 including q=0
    R(t)=h(t-t0)*R0+integral[t0,t] h(t-s)*g_r(s)ds
    E(t)=exp(d*(t-t0))*E0+integral[t0,t]exp(d*(t-s))*(c*R(s)+g_e(s))ds

R uses the original t0 history. E=abs(eta); coarse l1=4E. Both R and E lower endpoints enclose the ideal comparison functions defined by the supplied bound-forcing. They are not lower bounds on an actual physical error or residual. No universal raw/capped/physical gain follows. The full-A q/tau certificate is an input prerequisite; this API neither recomputes it nor substitutes a nominal-K contraction rate. The symbol c is comparison coupling and is unrelated to the speed-of-light symbol.

## Result record

The result has parameters,source,requested_times,base_times,refined_times,exact,raw,weights,work,certificate_status,input_scientific_status,source_provenance,R_history,cap_application,arithmetic. `refined_times==base_times`; the redundant name preserves the existing result interface.

`exact` contains F_at_refined,R_at_refined,kernel_at_refined,R_quartic_cells,observation_R_suprema. F is the continuous convolution part without initial hR0. Each R_quartic_cells record has:

| Field | Meaning |
|---|---|
| left,right | Physical base-cell times |
| bernstein | Five exact B4 coefficients of the continuous cell extension |
| coefficients_normalized | Five ascending power coefficients on u=(t-left)/(right-left) |
| initial_piece | h(left-t0)R0, constant in the cell interior |
| F_bernstein | Five convolution-only B4 coefficients |
| right_left_limit | bernstein[4] |
| actual_right_endpoint | h(right-t0)R0+F(right), right-continuous value |
| ge_bernstein | Four B3 coefficients restricted to this base cell |
| forcing_bernstein | Five B4 coefficients of cR+g_e after degree elevation |
| subdivision | Exact derivative-variation partition and work counters |
| supremum | Exact and dyadic closed-cell supremum enclosure |
| whole_E_majorant | Constant-forcing E upper construction for this cell |

### Subdivision certificate

`subdivision` contains method=BERNSTEIN_DERIVATIVE_VARIATION_V1,depth_limit=96,derivative_bernstein[4],splits_actual,nodes_visited,max_depth,terminal_leaves,depth_limit_leaves,max_unresolved_width,leaves.

The leaves form a complete nonoverlapping partition of normalized[0,1], sharing endpoints. Each leaf has left,right,depth,variation,kind,endpoint_values[2],lower,upper. Kinds are CONSTANT,NONDECREASING,NONINCREASING,DEPTH_LIMIT. Variation counts sign changes after deleting exact zeros. At V=0, a nonzero derivative has one weak sign; all-zero derivative is CONSTANT. Those leaves use exact endpoint extrema, not a Bernstein hull overestimate.

A DEPTH_LIMIT leaf additionally has midpoint,midpoint_value,bernstein[5]; its lower is the maximum of its endpoints and midpoint, its upper is the restricted B4 maximum. Its depth is96 and normalized width2^-96. These are unresolved leaves, not individually claimed isolating rootboxes. Critical roots at dyadic split boundaries can be endpoints of monotone leaves. Independent root coverage must allow those boundary roots and multiplicities. No false claim of one root per unresolved leaf is made.

The complete partition is retained compactly: monotone leaves need no repeated coefficient arrays. Per-cell splits<=288,nodes<=577; all source/build and subdivision precharges occur before their loops. Global leaf count is not an independent unbounded allocation.

`supremum` fields are exact_lower,exact_upper,exact_gap,M_B,Cmax,proved_gap_bound,dyadic_lower,dyadic_upper. Exact endpoints, every leaf lower, actual_right_endpoint and every leaf upper participate in their respective maxima. M_B=4max|B[i+1]-B[i]|, Cmax=max B. For model B>=0, proved_gap_bound=M_B*2^-96<=4Cmax*2^-96. Exact_gap<=proved_gap_bound. Dyadic interval width adds at most2*2^-128. These are upper/lower bounds on a closed-cell supremum; lower is not a pointwise lower envelope.

### Scalar intervals and observations

Every interval is `[lower,upper]`, both exact rational strings. `weights` has one row per base cell, left,right,z,exp,phi,W0,W1,W2,W3,W4. z=d*duration, exp encloses exp(z), phi encloses duration*integral[0,1]exp(z*(1-u))du. Wi encloses the corresponding B4 exponential moment including duration.

`raw` preserves endpoint and whole-cell matrices:

    endpoints_lower/upper                  shape Nobs+1 by2 (R,E)
    whole_cells_lower/upper                shape Nobs by2 (supR,supE)
    refined_endpoints_lower/upper          shape Nbase+1 by2 (R,E)
    refined_whole_cells_lower/upper        shape Nbase by2 (supR,supE)

Endpoint R is exact in both columns; E is outward. Whole-cell E lower is max(left E lower,right E lower); upper is max(endpoint upper,constant-forcing majorant endpoint upper). Qmax=c*Rsup_upper+max(restricted geB3). The majorant starts from left E upper and uses the same signed d. Its derivative has fixed sign, so its endpoint maximum covers the whole cell. The sharper polynomial E endpoint is propagated to the next cell. Observation whole-cell bounds are maxima of contained base-cell bounds. Endpoint connectors are not whole-cell certificates.

## Shared fixed fixtures and primary serialization

`verification/CASES.json` has schema WU_R15_FIXED_CASES_V1,cases:[{id,input,expected}],extrema_cases:[{id,bernstein,expected}]. Case id is outside the run_case input. Every full model is ARITHMETIC_CONTROL_PREMISE. Expected rational controls are symbolic design targets, not pre-execution outcomes. The eventual fixed file is frozen before either campaign.

`verification/run_primary.py --root ABS_LEAF --output ABS_OUTPUT` writes schema WU_R15_PRIMARY_RESULTS_V1,status PASS_SCOPED or FAIL,summary,valid_cases,extrema_controls,guard_cases,checks,frozen_files,arithmetic. Each valid case is `{id,status,result:<run_case result>}`. Each extrema component is `{id,status,bernstein,result:<supremum/subdivision certificate>}`. Each guard is `{id,status,exception_type,message}`. Explicit check records determine summary.checks/passed/failed; sample-point counts do not inflate the number of semantic checks. The independent reference reads raw/PRIMARY_RESULTS.json and the same immutable CASES.json, without importing production code.

Root supplies the resource wrapper and renderer. Production author supplies complete core, CLI, primary and fixed inputs only after C5 authorization. All entry points explicitly set the finite6000 digit policy before parsing or serialization.
