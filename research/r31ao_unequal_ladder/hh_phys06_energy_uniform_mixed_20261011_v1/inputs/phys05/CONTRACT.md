# PHYS05 frozen endpoint-free component contract

Authority: controller-provided Astra READY_ENDPOINT_FREE_COMPONENT_CONTRACT.
Base commit: 36b479d509d28aade8db6c8df6a1f8e9edf1a677.
Owner commit: 569b04cd71e45756e0fd476aef6643bd9434f4fa.
Selected PHYS04 input SHA256:
26a340065a9a99d02903bf0cc008baaf6ade00d2e845beb9d2b0b7d801316494.
Only this new artifact directory may change. Original dirty checkout remains intact.

One stdlib rational checker invocation, at most one targeted repair/recheck.
No native/root/IVP/history/atomic/old-suite runs, commits or publication.
Exact rational equality, tolerance 0. Binary64 source/input leaves are interpreted
as exact real rational values; native operation rounding is outside scope.

Let g=(x,HeII,HeIII,w), lower=(1-x,fHe(1-HeII-HeIII),fHe HeII),
and r_aj=c nH sigma_ja lower_a. For packet energy E_j define
K_j=(r_H, (r_HeI-r_HeII)/fHe, r_HeII/fHe,
sum_a r_a(E_j-chi_a)). Thus photo RHS is K(g)p, K is affine,
and K_gg=0. Preserve owner interval_rhs lines 463-524.

In the PHYS04 active quotient, nodes 0..15 have zero opacity. For j>=16,
L e_j=H E_j/(E_j-E_{j-1})(e_{j-1}-e_j), with first-active outflow
outside the quotient. Do not treat this quotient as the full guard map.

The remap-specific mixed gas h2 coefficient is
-1/4 [K L Wgamma + Kg[Wg] Lp + Kg[Ug] L Vgamma + Kg[Vg] L Ugamma].
Validate using independent sparse dual-polynomial multiplication, all full gas
and photon signed unit directions, and mixed-input directions. Zero incoming
family means p=Ugamma=Vgamma=Wgamma=0. Zero primal stock alone need not make
signed gas/photon cross derivatives vanish.

Direct formal two-step BE calculation compares transport on/off, h1=0,
h2=-K Lp/4. Isolate cancellation of gas-only terms using abstract polynomial
jet witnesses, retaining named physical FT03/HH terms in the conditional equation.
These witnesses are not replacement physical rates or endpoint observations.

For Dj=1+d kappaj>0 and kj=Kj/Dj, check PHYS04 D2 arithmetic against
kj'[u]=Kj'[u]/Dj-d Kj kappaj'[u]/Dj^2,
kj''[u,v]=-d(Kj'[u]kappaj'[v]+Kj'[v]kappaj'[u])/Dj^2
+2d^2 Kj kappaj'[u]kappaj'[v]/Dj^3.
Check inactive zero opacity, zero-stock cross slots, and the HI identity
d2/dx2 [Nj Aj(1-x)/(1+d Aj(1-x))]
=-2 Nj d Aj^2/[1+d Aj(1-x)]^3.

Conditional propagation only:
A W=y0ab+d[Fgg[U,V]+Hg V+sum_j{kj'[U]Nj_b+kj'[V]Nj_a+kj Nj_ab}],
A=I-d Fg, Nj_a=R p_a, Nj_b=R p_b+d Bj, Nj_ab=R p_ab.
Here Fgg includes (F_FT03_nonphoto)gg + lambda (H_HH)gg
and the photo sum Nj kj''. Hg V is the explicit HH parameter/gas cross term.
No FT03/HH term is set to zero. Do not invert A, solve a root, infer W,
or fabricate a physical regularity tube. Admission is deferred to Astra review.

HARNESS_UNAVAILABLE: /home/cosmosapjw/.codex/bounded-work-harness/RULES.md
does not exist. This finite contract is the controller's explicit bounded unit;
no installed harness execution is claimed.
