# Independent review of PHYS67 first Born certification

Reviewer: the Coulomb subagent, separate from the first-Born implementation
author. Target is `src/wu088_hh/phys67_first_born.py`; the exact reviewed SHA
is recorded in `FIRST_BORN_INDEPENDENT_CHECK.json`. This review does not
re-execute the target radial integration or a PHYS64/66 campaign.

## Scientific formula

With normalized spherical harmonics at m=0, the phi integration contributes
`sqrt((2l+1)(2l'+1))/2`. Multiplying the original physical `V=2S` gives

`V_l,l'(r)=sqrt((2l+1)(2l'+1))*int[-1,1]P_l(mu)P_l'(mu)(1+1/d)exp(-2d)dmu`.

Here `d^2=r^2+R^2-2rR mu`, `R=7/10`. For real `r>R`, changing from mu to d
reverses endpoints, `dmu=-d/(rR) dd`, and `d in [r-R,r+R]`. Setting `t=d-r`
then gives

`V_l,l'(r)=sqrt((2l+1)(2l'+1))/R * exp(-2r)`

`*int[-R,R](1+(t+1)/r) P_l(-t/R+(R^2-t^2)/(2Rr)) P_l'(...) exp(-2t) dt`.

This establishes the implementation's normalization, the positive Jacobian
after reversal, and both Laurent contributions (`pairs[k]` and `pairs[k+1]`).
For a power mu^j, the coefficient of r^-k is proportional to
`t^(j-k)*(R^2-t^2)^k`; expanding its latter factor gives the code's
`n=j-k+2s` and sign `(-1)^(j-k+s)`. The terminal degree is bounded by
`2(l+l')+1<=257`, consistent with the helper's degree scope.

The exact antiderivative of `t^n exp(-2t)` is minus the exponential times
`sum[j=0..n] n! t^(n-j)/((n-j)!2^(j+1))`. Its endpoint signs agree with
`exponential_moment_pair`.

The first Born term is `int[B,infinity]P(B,r)V(r)P(B,r)dr`, with a plus sign
and no complex conjugation. Its `(l,l')` entry therefore has the root code's
`H_l(r)H_l'(r)/(H_l(B)H_l'(B))` factor. At first order no intermediate
angular sum occurs: the exact single angular matrix element is shared by
every projection retaining these two external modes. The code's
`all_angular_first_order_entry` is justified for this individual entry.
It does not establish higher-order excluded-mode control.

## Independent exact arithmetic

`independent_first_born_check.py` builds Legendre polynomials by their
three-term recurrence after substituting mu(t). It forms the t polynomial
directly at a fixed exact r. Exponential moments use integration by parts,

`I_n=[(-R)^n exp(2R)-R^n exp(-2R)]/2+(n/2)I_(n-1)`.

Both coefficients of `exp(2R)` and `exp(-2R)` agree as exact rationals with
the target Laurent code for `(l,l',r)=(0,0,27),(1,0,55),(3,2,65),(21,20,27),
(21,20,65)`. This checks the actual high-degree 21/20 implementation via a
different construction. The general identity is supplied by the algebra
above, rather than inferred from five point checks.

## Certification path and acceptance

The elementary Laurent expression is analytic on `Re(r)>R`, and the outgoing
Coulomb helper is analytic on the containing domain `Re(r)>0`. The callback
checks the stronger former domain for every complex test ball; returning
indeterminate outside it is appropriate. A fixed real reference denominator
does not introduce moving-r poles. Every ball error in the angular constants,
Coulomb functions, products and radial quadrature remains in the accumulated
Acb result.

The exact dyadic real and imaginary radii are added as an L1 upper bound on
complex absolute error. Checking this *returned* bound against the requested
goal is essential and is present in the implementation. A requested FLINT
tolerance alone is not used as evidence. The analytic cutoff bound is added
afterward to both Cartesian components; this safely encloses any unknown
complex tail whose absolute value is below that bound.

The cutoff constant for `L=max(l,l')` applies to this first-order entry,
since that entry has the same exact angular integral in that projection.
The bound is inherited from PHYS65/66, whose current accepted status remains
unchanged.

Decision: **PASS_SCOPED for the derivation and implementation path reviewed.**
Actual radial error-goal acceptance is the parent execution receipt's field
`actual_numerical_goal_met`; this independent review does not replace that
execution. No blocking finding was identified in the reviewed formulas,
signs, analytic-domain handling or exact error serialization. Full xi,
origin/adjoint matching, higher Born certification and physical rates retain
their separate remaining obligations; HH_R10 remains OFF.
