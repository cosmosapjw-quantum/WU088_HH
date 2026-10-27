# R4 / C4: 표현 선택과 첫 구성

The inherited R4 defect is h d^T r. Differentiating r rather than postulating a relaxation time gives L=K+h(pi d^T-D), c=Kpi-piDot-h(Dpi-pi dbar). Since the columns of B=pi d^T-D sum to zero and offdiagonal entries are pi_i*d_j, L is a Markov generator. This supplies an explicit contraction coefficient and preserves the damping caused by common destruction.

The chosen comparison variables M,U,E retain total mass, state-distribution defect and the actual aggregate error separately. All three are needed: U alone needs a bound on the forcing proportional to X; E accumulates the flux defect with the coarse decay rate.

Independent first construction by r5_primary_sources used K=[[-1,2],[1,-2]], pi=(2/3,1/3), d=(1,4), h=1, x0=pi. This dimensionless mathematical fixture gives a=6, dbar=2, beta=4/3, omega=3/2. With f=0, at t=1 the actual ||r||1=0.05730673015072688 is bounded by U=0.09744018373194026 and actual aggregate error0.05748532660933281 by E=0.07973201006793723. With f=(1,0), the eventual actual error1/5 is bounded by1/4. The independent prototype evaluated56 positivity/bound checks at seven times for the two formation choices. This recorded prototype is distinct from the main exact-rational implementation run and the planned independent CAS call.

The source-based application uses the already bound REC HD supplied graph; actual missing reaction rows remain pending. New code must expose a separate mathematical-model scope and cannot silently admit a physical consumer.

The operational scheduling correction lets independently executable mathematics proceed while R4 fullZIP transport is pending. It changes no source, physics, old allowance or activation rule. The completed theory and coding node criteria stay intact.
