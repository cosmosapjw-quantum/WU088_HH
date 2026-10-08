# Finite segment preflight: mathematical assessment only

This is a future host design assessment requested after the actual W1 monolithic log-coordinate attempt returned `INTEGRATOR_NO_CONVERGENCE`. No host source changes or new integrations are part of this assessment.

The inherited outer order-1 preflight requests a finite callback enclosure over the entire fixed inner path and the whole outer complex parameter box. Failure of one large interval evaluation does not imply that the mathematical integrand lacks holomorphy there. The observed W1 call counts are compatible with repeated preflight refusal, but they do not establish that causal diagnosis without more precise refusal instrumentation.

It is sufficient to replace **only this domain preflight** by a finite exact cover of the same inner real path:

1. Choose strictly increasing exact segment endpoints, including the unchanged two path endpoints, with no gap. For the integer log endpoints currently supported, intervals of at most one log unit provide a straightforward deterministic cover. Bound the segment count before allocation or dispatch.
2. On every segment, call the same physical/log adapter at order 1 with the complete unchanged outer complex box, using an outward enclosure of the entire closed inner segment. Preserve the original strict positivity and branch guards. All dispatched calls consume the same global callback/evaluation/wall budgets.
3. Refuse the entire outer trial if any segment is nonfinite or any shared budget stops. Do not interpret a partially checked cover as success, reset counters, substitute a midpoint, or widen the allowed global budget.
4. If all segment callbacks are finite and retain the joint-holomorphy contract, the fixed source function is holomorphic on neighborhoods of the finite covered product. Compactness and the original uniform bounds justify holomorphy of the parameter integral. The source's fixed branch convention must be common to every segment.
5. Discard the preflight values. Proceed with the existing uniform inner numerical integration, still passing the whole outer parameter box and checking the achieved returned radius. The subsequent adaptive quadrature may use its own partition. A finite domain proof is not an integral-value approximation or an error estimate.

This changes a sufficient domain certification strategy, not the target function, coordinate Jacobian, quadrature tolerance or endpoint remainder. It does not guarantee numerical convergence: genuine parameter width, tight error requirements, special-function overestimation and finite resources can still cause rejection. If implemented, source binding plus a meaningful analytical enclosure/refusal regression and a newly bounded actual pilot would be required before claiming improved feasibility.
