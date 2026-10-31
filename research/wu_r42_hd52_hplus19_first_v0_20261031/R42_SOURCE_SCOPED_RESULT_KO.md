# WU R42 | Full HD52 H-collision radiative return, restricted HD19 proton collision

Protected immutable parent: WU Draft PR #180 HEAD `8d00eec817c1ddd0c3841f6ad1a411aac9ae1e5e`. Canonical DAG **34/49 unchanged**, R42 auxiliary **1/1 SOURCE-CONDITIONAL SCOPED**; R/C **18/20 scoped** with distinct-author R6/C9 **NOT_RUN**. No production, main merge or foreign-repository write.

## Original inputs and exact intersection

- Original EMAA HD RADEX data `HD.Rovibration.805a7aa5.radex` SHA-256 `b0db1613425e403889c3a74f6cd9e142c562a552f1ebf05e61cbf509cd429c94`, [EMAA dataset](https://doi.org/10.17178/emaa_hd_rovibration_805a7aa5).
- 52 HD source levels, 368 Einstein A radiative links; **H-atom 1326 distinct transition pairs ×15 exact original T** from Desrousseaux, Coppola & Lique, MNRAS 513,900 (2022), DOI [10.1093/mnras/stac911](https://doi.org/10.1093/mnras/stac911).
- **H+ 171 pairs ×25 T** only within original HD19, González-Lezana, Hily-Blant & Faure, JCP 157,214302 (2022), DOI [10.1063/5.0128598](https://doi.org/10.1063/5.0128598). The common exact gas temperature is **5 K only**. No temperature interpolation and no invented H+ rates above HD19.

## First-v0 source-conditional construction

For 52-level HD, define `U={v>=1}` (34 transient), `A={v=0}` (18 absorbing first-event destinations), `W={v1,J0..6}` (7 original core) and `X=U\W` (27 outside-core transient states). Column generator `K=K_H+K_Hplus+K_sp+K_stim+K_abs`; H collision uses source 52 pairs, H+ only source 19 pairs, radiation is prescribed external blackbody `T_rad=2.7255*(1+z_boundary)`, OFF retains spontaneous.

`N=(-K_UU)^-1; B^(m)=K^(m)_AU*N; tau_i=sum_u N_ui`. First exit from W into X: `F=K_XW*(-K_WW)^-1`. Exact first-return decomposition: `P_outside=1^T F e_i`, `P_return=1^T K_WX*(-K_XX)^-1 F e_i`, `P_direct_v0=1^T K_AX*(-K_XX)^-1 F e_i`; `P_outside=P_return+P_direct_v0`. Absorption into v0 is a FIRST-ARRIVAL event, not physical HD loss.

## Actual generated computation and evidence

- 15 original H-only temperatures × 4 H densities × 4 radiation boundary labels; original exact joint H+H+ 5K with 4 H densities ×2 proton densities ×4 boundaries; R41 proton-only 55K benchmark at two boundaries.
- **274 input conditions**, **1918 initial-state cases**, **172620 cause × first-v0 destination probability rows**, **1918 return decomposition rows**, **5360 indexed source-radiative support rows**. Local full private master includes executable Python source, original input RADEX, tables, 4 PNG and 4 SVG actual plots.
- R41 reference: `Tgas=55K, nHplus=1000 cm^-3, nH=0, z_boundary=300, initial HD(v1,J6)`: first outside HD19 before v0 = **0.1476229718438572**, of which **0.0444817096809390** returns to original v1 core before v0, and **0.1031412621629182** first arrives at v0 before return. Conditional return fraction of first exits **30.1319700622%**. The R41 original 0.14762297184385717 is reproduced.
- Max source-grid first outside before v0 0.7035667307071304, at H-only 3000K, nH=10^8 cm^-3, z300, initial v1J6. This is a prescribed-grid maximum, not cosmological prevalence.
- Tests **15/15 normal** and **15/15 Python -O**, original source SHA and H detailed balance; 34x34 mpmath80 independent solutions; Wolfram rational Markov return identity; first-v0 mass defect at most `5.50e-14`, energy telescoping residual at most `4.10e-33 J`. Clean isolated replay **6/6 SHA256 byte-identical**, source master **40/40 SHA256+size**, ZIP CRC PASS.
- Local master `WU_R42_FULL52_H_HPLUS_ORIGINAL_SOURCE_20261031.zip`: 2,566,994 bytes, SHA-256 `c0eefdbcbc61c4a17e7aaa8fc74827ad3dc861680c8ccea9c42b5e7bb7f51712`. Stage checkpoint ZIPs 20, phase ZIPs 4 are local and verified, **not remotely uploaded**.

## Exact present preservation status and scientific holds

This PR publishes a **compact text/representative-data checkpoint only**. The current runtime has no usable file-export/upload reference for the local ZIPs; therefore neither full master nor per-stage ZIPs has been backed up to Drive/Library in this run. The complete source-containing private archive is available from the generating ChatGPT session only. A separate [Google Drive source-scoped checkpoint](https://docs.google.com/document/d/1XUfqJZku8k3P3EJ9WHmf4OyCXn0tgybUgG49JYr6dLQ/edit) records evidence independently but **does not count as byte-exact source ZIP backup**.

Outstanding: original GL2022/EMAA 50-rate-cell author disagreement; missing H+ rates on higher HD levels; all states above source 52 excluded; full reaction S matrix and non-BO physical Q not computed; different-author R6/C9 NOT_RUN; `HH_R10=OFF`, `L4=false`, `PRODUCTION=NOT_ISSUED`, `AUTO_NEXT_NODE=false`. No branch merge.
