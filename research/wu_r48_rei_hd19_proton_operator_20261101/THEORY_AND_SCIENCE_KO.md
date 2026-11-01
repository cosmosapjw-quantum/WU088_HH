# WU R48 | REI original tick160 H/H+ collision source to HD19 reversible generator

**WU science owner:** `cosmosapjw-quantum/WU088_HH`; original project goal: enable only a physically matched conditional HD module in the source-qualified REI Bianchi IGM scenario. REI provides immutable H/He/T accepted-state **model** data; no REI original source code or initial history was modified or rerun. This R48 unit is **source-conditional derived + numerically checked** and not canonical completion.

## 1. Original authority, actual state and no interpolation masquerading as source

- Protected WU parent R47 Draft PR #186: `77062bd123352dc5044dd976cf0ac6439e15ce5f`. WU routing parent #185 remains unchanged.
- Original accepted REI F05 model source ZIP: 12,591,114 B, SHA256 `48ad5c6f0922ad946a10a89ce17fefd2c7241ac956b6bac194892a42810312a7`; 46,080 unique physical grid nodes, three named source lanes **numerically identical**, tick 160 of 131072. This is not the completed original interval or reionization observational data.
- Original EMAA RADEX `HD.Rovibration.805a7aa5.radex` SHA256 `b0db1613425e403889c3a74f6cd9e142c562a552f1ebf05e61cbf509cd429c94`. Source 52 rovibrational levels and 1326 H transitions with 15 native T nodes (5–5000 K). H+ table has **all 171 pairs within the first 19 original levels only**, 25 original T nodes (5–3005 K); no proton rates above state index 19. The first 19 levels contain a mixture of original v=0 and v=1 states and are *not* simply the lowest 19 rotational quantum numbers.
- Primary papers: Desrousseaux, Coppola, Lique, *MNRAS* 513,900 (2022), DOI [10.1093/mnras/stac911](https://doi.org/10.1093/mnras/stac911); González-Lezana, Hily-Blant, Faure, *JCP* 157,214302 (2022), DOI [10.1063/5.0128598](https://doi.org/10.1063/5.0128598). The 2022 paper separately includes reactive HD+H+ ↔ D++H2 chemistry: those rates are **not** part of the 171 nonreactive excitation entries used here.

## 2. Actual WU mathematical construction

Use metric (-,+,+,+), but the local source kinetic generator below is nonrelativistic internal-level rate bookkeeping. Retain physical constants c, h, and k_B. Let `E_i=100 h c ε_i` J from original spectroscopic `ε_i` cm^-1 and original degeneracy `g_i`. Original REI H/He-only source at the accepted tick defines `x=x_HII` and conditional `n_HI=(1-x)n_H,nuc`, `n_H+=x n_H,nuc`; no molecular hydrogen carrier is present in this original H/He state. We do NOT know physical `n_H,nuc` needed for an absolute timescale.

For each of 171 original first-19 source pair transitions `u>l`, let source data supply downward `k^H_ul(T)` and `k^p_ul(T)` [cm^3/s]. At an actual source temperature between tabulated original nodes, interpolate each **positive rate** piecewise log-log. This is a separately declared derived interpolation, not author-original data. The density-normalised downward transition rates are

`d^H_ul=(1-x) k^H_ul(T), d^p_ul=x k^p_ul(T)` [cm^3/s per `n_H,nuc`].

Their REI-conditioned ratio is

`r_ul(T,x) = [x/(1-x)] [k^p_ul(T)/k^H_ul(T)]`.

At the common gas T the upward rate is supplied **by detailed balance**, not by an invented proton source table:

`d^a_lu=(g_u/g_l) exp[-(E_u-E_l)/(k_B T)] d^a_ul`, for `a∈{H,p}`.

Therefore the proton/H ratio is the same in *both* directions for each pair. The 19-state continuous-time rate matrix includes every original proton-supported pair. Its columns sum to zero; its reversible stationary vector is `π_i = g_i exp(-E_i/(k_B T)) / Q_19` (a **reference collision equilibrium**, not the actual REI HD population).

For the acceptance intervals `T∈[T_lo,T_hi]`, `x∈[x_lo,x_hi]`, `0≤x<1`, evaluate the **outer rectangle** pair bounds with the monotone function `x/(1-x)`. Between any two consecutive native temperature knots, log(kp/kH) is affine in log T, so extrema are at original interval endpoints or source knots. The calculated global lower ratio `ρ_0=min_{nodes,pairs,T,x} r_ul=108.63329689956697>1` is an exact extremum of the **declared piecewise-log-log model over those rectangles**, modulo floating-point numerical evaluation, not a rigorous uncertainty bound for the *original author rates between nodes*.

### Reversible Dirichlet-form ordering

Let `L_a f(i)=∑_{j≠i} d^a_{i→j}(f(j)-f(i))` and `π_i` the common detailed-balance equilibrium at that gas T. For each source-supported original REI state and every admissible `T,x` in its rectangular outer hull, `d^p_{i→j}≥ρ_0 d^H_{i→j}`. Thus

`ℰ_p(f,f)=1/2 ∑_{ij} π_i d^p_{i→j}(f_i-f_j)^2 ≥ ρ_0 ℰ_H(f,f)`, and with the same `Var_π(f)`,

`gap(L_p)=inf_{Var_π(f)>0} ℰ_p(f,f)/Var_π(f) ≥ ρ_0 gap(L_H)`.

This is a **derived theorem for the reversible collision-only 19-state operator under declared assumptions**, not the gap of a full 52-level photon–chemical generator. We numerically diagonalized real symmetric similarities, using per-nucleus rate units [cm^3/s], at all 5,616 source-supported node midpoints.

## 3. Actual numerical results

From 46,080 original REI accepted nodes, only **5,616** have their *whole temperature interval* inside both the H and H+ original source temperature grids; 9,216 are neutral-H only and 31,248 outside H's original T domain. Current 5,616-node joint T midpoint range ~2096.669759... to 2945.927183... K, with `x_HII` ~0.99874557 to 0.99998223. 3 source lanes share the same numerical states.

- **960,336 newly derived state×transition records** (`5616×171`), every one proton-dominated. Min midpoint ratio `108.6782040301964`, median `300140.78811278264`, max `12233780.458471283`; minimum outer-rectangle ratio `108.63329689956697`.
- **106,704 density-normalized level-exit records** (`5616×19`), all proton-dominated at midpoint. Minimum level-exit H+/H ratio `2369.7773787506917`.
- Collision-only 19-level spectral-gap ratio proton/H: min `21566.012022981602`, median `527337.4376492422`, max `2373929.7619817536`. This comparison is independent of the unknown total H-nucleus density, **but absolute rates/relaxation times are not**.
- Within the original 52-level finite EMAA spectroscopic database, the **hypothetical LTE partition weight outside the first proton-supported 19 levels** ranges 0.0457483210637 to 0.133891995750 (median 0.06980371918). Its maximum upper parent-box value is 0.1338940488568. This is a conditional LTE **coverage diagnostic**, **not a bound** on actual nonLTE excluded populations or HD52 photon-cooling error.

## 4. Physical scope and REI central purpose

This contribution demonstrates that a source-bound **H-only HD52 cooling module is not adequate to represent the 19 supported excitation channels** when evaluated at these highly ionized REI states under the stated density/species closure. It simultaneously demonstrates that a blindly truncated HD19 coupled H+ module cannot be promoted to a full HD52/nonLTE energy source without additional source coverage/closure. This is *not* a proof that physical HD cooling is large: the original REI H/He-only 26-event state has no n_HD population; no HD chemical formation/charge or reactive loss, density, full observer z/clock and proper Bianchi geometry are coupled.

The source paper's statement that in *typical* low-proton-abundance astrophysical environments H cooling may dominate is not contradicted: these original conditional REI states have `x_HII≈1`, an entirely different composition. No general cooling-dominance theorem or strong no-go is claimed.

**WU-owned output for REI:** original-source `r48` collision generator, pair-wise outer supported-domain bounds, state/transition energy and degeneracy provenance, 5,616-node admissibility/coverage table. The REI owner can reuse it only when a *named actual HD source consumer* with a valid abundance/density/clock, reactive chemistry, radiation boundary, source energy ownership and material impact exists. If it does not, WU remains an independently verified conditional source contribution and REI F05 remains the priority elsewhere.

**Canonical ledger after this scoped unit:** WU `34/49` (+0), REI central `28/88` (+0), REI working `33/88` (+0), F05 first interval `160/131072` and `[160,161]` unchanged HOLD. No source/owner mutation, no first-interval IVP, no main merge, no production, HH_R10=OFF, L4=false, AUTO_NEXT_NODE=false.
