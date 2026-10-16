# WU088_HH PHYS57B: refined exact cutoff and sandbox C5-C8

Stacked on PHYS57 R5 PR #97, source commit `2721785f63910a30c89c4b432db79b723f1775a5`. **This is a second, scientifically distinct stage** retaining all prior R5 artifacts.

The earlier rigorous all-ell Coulomb shift cutoff `ell>=128` was improved to **`ell>=50`** by using the Nicholson/Erdelyi positive interval `z in [12/5,5/2]`, exact `e<87/32` from the 8th partial Taylor sum plus geometric tail, and positive integral bound `(48/725)*((12/5)ell-a)*(169/25)^ell*(32/87)^99`. All possible negative contribution at `0<=z<=a/ell` is at most `(87/32)^3*a^3/ell²`; their exact-rational ratio at ell50 is **10.466132546730515... >1**, increases thereafter. Attractive `eta_C=-10/7`, `rho=189/10`. This is a *strict analytic all-l proof*, not finite sampling.

Exceptional l=21..49 normalized Wronskian current `jstar=(7/10)/(16*50*3^122)` derived from qfloor `255143/583200>1/4`, variation `1441/23328<1/8` at T216, and lognorm D=`46115/756` from r27..216. Hence PHYS56 hybrid inverse exact bound is `(1+C_trace/c_D)^2/jstar` with `c_D=9/1000`, `C_trace=4849/16800`; magnitude `~2.0214182949259e64` (log10=64.30565619), >335 decimal orders tighter than PHYS57 R5 but still a poor physical stability estimate.

**Actual isolated Python execution:** PHYS55 original 42 tests + PHYS57 R5 15 + PHYS57B 24 = **81/81 passed**, pytest 7.82s (wall9.87s), RSS146148 KiB, exit0. Six independent mpmath Coulomb F/G real-shift and log-flux points l=21,29,49,50,64,100 were generated. Wolfram connected independent exact rational 7/7 gates PASS, with e-series upper 8877691/3265920, log10 bound64.30565619198. Full WU repository pytest and NCP heavy jobs **NOT_RUN**. Synthetic 2x2 Schur test is not the original screened exterior.

**Physical scope:** Original noncentral screened **finite collar [20,27] + CENTRAL Coulomb exterior**, all ell>=21 and all m; **NOT** physical screened exterior Z_S, not xi/incoming adjoint, sigma(E), k_HH(T); `rei_bianchi HH_R10=OFF`. No sibling mutation.

**Full executable source and exact evidence** are contained in separately uploaded provider-verified capsule (not reproduced as all individual Git blobs in this supplemental PR stage, due source-export connector session error): `WU088_HH_PHYS57B_C5C8_CHECKPOINT_20261016.zip`, **53,543 bytes**, **23 ZIP entries**, SHA256 `76c1c6b2d57b3b179c8d3d2612fce634b70cd0863a24847b15f96a6d6bea5d09`. Preserves original frozen NPZ SHA256 `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`, all new original scientific Python/test/report/receipt sources plus parent R5 sources.

**Restored two-provider bytes**: Dropbox `/WU088_HH/WU088_HH_PHYS57B_C5C8_CHECKPOINT_20261016.zip`; Google Drive `/Google Drive/WU088_HH/PHYS57_C5C8_20261016/WU088_HH_PHYS57B_C5C8_CHECKPOINT_20261016.zip`. Both upload ACK and independently materialized fresh ZIPs, byte-for-byte matching original, every manifest file SHA and ZIP CRC PASS. Portable archive restoration verified. This GitHub-stage receipt does not claim complete Git bundle backup.

**Next PHYS58:** actual noncentral screened exterior `Z_S` with low/high P/Q couplings, weighted outgoing limiting absorption/Poisson maps and Fredholm+Rellich or genuinely bounded screened DtN perturbation; avoid assuming scalar screened sup is DtN-norm. Source-driven scattering and HH_R10 still HOLD.
