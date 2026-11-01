# WU R49 | D charge exchange and exact electron-source ledger for REI IGM

**Scientific owner:** WU088_HH. **Consumer:** original REI Bianchi IGM (read only). This is one bounded original-source-conditioned WU study, not a full REI solver or adopted F05 history. All central science progress stays WU **34/49**, REI **28/88**, working **33/88**, delta **0**.

## Derived reaction law

Faure et al. (2024), DOI 10.1093/mnras/stae994, rates D3 and D4 in **10 K–10000 K**:
D3: D+ + H -> D + H+, k3 = 2.18e-9 (T/300 K)^0.355 cm^3/s.
D4: D + H+ -> D+ + H, k4 = k3 exp(-43 K / T).
Given *frozen original H/He model* x=xHII, f=nD+/nD,
J3=nH k3 (1-x) f, J4=nH k4 x (1-f).
`fCE*=x exp(-43/T)/(1-x+x exp(-43/T))`, and
`tCE=1/[nH(k3(1-x)+k4 x)]`.
**Crucial exact chemistry correction**: D3 and D4 transfer positive charge between H+ and D+: `d(nH+ + nD+)/dt|CE = 0` and **`dn_e/dt|CE=0`**, even if fD+ changes. The frozen-H/He additional ionic inventory epsD*f/x_e is a **counterfactual** and cannot be called actual Thomson optical-depth change.
The 43 K chemical energy budget applies *only if the D exchange enthalpy thermalizes*. It is not complete 26-event gas+photon energy conservation.

## Original input identities and actual evidence
- REI original tick160/131072 frozen 46,080 unique spatial node source, ZIP SHA256 `48ad5c6f0922ad946a10a89ce17fefd2c7241ac956b6bac194892a42810312a7`. Original node T source support 21,600/46,080. **24,480 must stay outside Faure fit**, not extrapolated or zero-filled.
- REI PR319 published-UVB H/He source witness SHA1 `aaf60834dcc095025ad6261515fa5535d5b30894`. 4 supported T/source knots, 401-point *conditional PCHIP/BDF deuterium tracer* and optional assumption Gamma_D=Gamma_HI. This **is not** the original REI native F05 source/clock, not a CMB tau prediction.
- New numerical results: native fCE*=[0.992689847,0.999992688] over supported cells, one-original-tick CE e-fold requires nH=0.0277629–0.0481938 cm^-3 (unknown in original saved F05 fields). Conditional REI319 D+ fraction reaches 0.329051725 at z8.0693. PCHIP reconstruction differs from original REI319 saved segment tau by 0.379615%, not corrected by force.
- Local tests rerun: **36/36 standard, 36/36 python -O, public 12/12**. Earlier independent full 46k + Decimal60 18 and cleanroom 5/5 byte replay preserved in full ZIP.
- Full source-free executable archive SHA256 `09176ca6de0ece57fd3c52afea4dd99016af4e396267d6246a4fcce5578bed53`, 4,540,007 bytes, ZIP CRC and 44/44 manifest file hashes PASS. The source-free archive including code, 46,080-row table, 401-row tracer, figures and validation is available as a conversation downloadable artifact, **not stored in this Git branch**. No original private native REI source ZIP/EMAA raw copied into Git.

## Restriction, claim gate, next
Keep WU R49 **EXPLORATORY_SOURCE_CONDITIONAL**; original REI F05 remains **BLOCKED [160,161]**, local full-X logT upper `2.1245050576368385e-4 > 2e-4`. No merge, production, tolerance change, main or foreign repo edits, auto-next. R6/C9 are same-model hostile checks, distinct-author NOT_RUN.
**Drift watchdog:** Past WU R43–48 had real molecular source physics but zero central completion; R49 is a direct WU→REI electron/heat source falsifier, not another rate atlas. Do not initiate R50 until an original REI consumer binds D/HD abundance, nH, proper clock, photon/energy ownership, and materiality to a named observable. The original F05 common-parent/source correlation certificate belongs to REI, not to this WU branch.
