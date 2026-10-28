# R13 candidate: exact nonaligned piecewise-affine forcing

Status: manually derived candidate selected by root for finite R13 design. No scientific Python, ODE, or CAS execution was performed by this author. This document extends the R12 input class; it does not re-prove or re-execute the accepted R11/R12 science. Actual HD reactive array and named physical consumer binding remain a separate intake obligation.

## 1. Retained premise and changed input

Retain the R11/R12 full-generator family: fixed column-conservative Metzler K, fixed pi and destruction d, H=pi*d^T-diag(d), A_w=K+wH over the entire certified w box. The same-family all-starts zero-mass l1 propagator certificate is <=q for every full interval tau>0; all shorter remainders are nonexpansive. Thus h(age)=q^floor(age/tau), h(0)=1, including q=0 with q^0=1. Do not substitute nominal K rho into full A.

Retain R=||r||1, E=abs(eta), coarse l1=4E, zero-mass residual forcing, and whole fine/coarse-domain forcing bounds. Retain fixed c>=0 and signed d_c over the complete sweep. The comparison equations use c as the scalar coupling coefficient, not the speed of light. No spacetime or thermal-unit convention changes occur.

The changed input is a nonnegative affine bound on each exact source cell [a_j,a_(j+1)]:

g_r(s)=r_(j,0)+(r_(j,1)-r_(j,0))*(s-a_j)/(a_(j+1)-a_j),

and analogously g_e(s), with both endpoint values nonnegative. Endpoint pairs are actual whole-domain bound functions supplied as premises; a pair of samples does not establish such a bound. Different source cells may have different one-sided values. Their measure-zero endpoint convention has no effect on the integrals. Rational source and observation partitions share exact [t0,T].

The raw ideal comparison is

Rcal(t)=h(t-t0)R0+F(t), F(t)=integral_(t0)^t h(t-s)g_r(s)ds,

Ecal(t)=exp(d_c*(t-t0))*E0+integral_(t0)^t exp(d_c*(t-s))*(c*Rcal(s)+g_e(s))ds.

Both are nonnegative. Their enclosure lower endpoints are lower bounds on this chosen-rational-q ideal comparison, not on physical error.

## 2. Exact positive overlap moments

For each source cell and age strip k, let

L_jk(t)=max(a_j,t-(k+1)*tau), U_jk(t)=min(a_(j+1),t-k*tau).

If U<=L the term is zero. Otherwise the exact integral of the affine source is

I_jk(t)=(U-L)*(g_r(L)+g_r(U))/2.

Therefore F(t)=sum_(j,k) q^k I_jk(t), with k=0..floor((T-t0)/tau). Every summand is nonnegative; this form avoids subtracting two nearly equal indefinite integrals in production. All operations through F are rational and exact. Dimensions are [I]=[g_r]*time and [F]=[R].

Proof: intersect the source cell with s in [t-(k+1)tau,t-k tau]. The kernel equals q^k almost everywhere in that strip. Integrating an affine function over the overlap equals its exact trapezoid area. Sum the disjoint strips and source cells. This preserves all forcing history from t0.

## 3. Independent primitive identity

For x_+=max(x,0), n=floor(x_+/tau), define

J0(x)=tau*sum_(k<n) q^k+q^n*(x_+-n*tau),

J1(x)=tau^2*sum_(k<n) q^k*(k+1/2)+q^n*(x_+^2-(n*tau)^2)/2.

These are integral_0^(x_+) h(v)dv and integral_0^(x_+) v*h(v)dv. For g_j(s)=alpha_j+beta_j*(s-a_j),

F_j(t)=(alpha_j+beta_j*(t-a_j))*(J0(t-a_j)-J0(t-a_(j+1)))
       -beta_j*(J1(t-a_j)-J1(t-a_(j+1))).

Proof: v=t-s transforms the affine factor into alpha_j+beta_j*(t-a_j)-beta_j*v. The displayed formula integrates it over the clipped age interval. Finite sums avoid q=0 or q=1 division singularities. A reference can construct these primitives without importing production overlap code.

## 4. Event grid and quadratic reconstruction

The base event set is the exact rational union of source knots, observation knots, initial block knots t0+k*tau, and translated source knots a_j+k*tau lying within [t0,T]. Coalesce exact duplicates. Between consecutive base events [b,b+Delta], all max/min choices in every nonempty overlap are fixed. Their endpoints are affine in t; integrating an affine function between affine endpoints yields degree at most two. The initial coefficient h(b-t0) is fixed on the open cell. Thus P(u)=Rcal(b+u) on its interior is a nonnegative quadratic.

At u=0 use the actual right-continuous point value. At u=Delta use the left limit, with the same initial coefficient h(b-t0). The actual right endpoint may have a downward initial-term jump; forcing F is continuous. Reconstruct P exactly from P(0),P(Delta/2),P(Delta). For normalized x=u/Delta and samples p0,pm,p1,

P(x)=A*x^2+B*x+C,
C=p0, A=2*(p0+p1-2*pm), B=4*pm-3*p0-p1.

This is exact algebra, not interpolating an unknown function. If A!=0 and x_*=-B/(2A) lies strictly inside (0,1), insert the rational vertex b+Delta*x_* in a second refinement. There is at most one added vertex per base cell. No new source or kernel discontinuity is introduced.

## 5. Nonnegative quadratic Bernstein representation after vertex splitting

On each final subcell, P is monotone (or constant) and nonnegative. With local coordinate u in [0,D], write

P(u)=B0*(1-u/D)^2+2*B1*(u/D)*(1-u/D)+B2*(u/D)^2,

B0=P(0), B1=P(0)+D*P'(0)/2, B2=P(D).

The nonnegative-coefficient claim does not follow merely from nonnegative polynomial values; it follows from the vertex split. If P is increasing then B1>=B0>=0. If P is decreasing then B1=P(D)-D*P'(D)/2>=B2>=0. Endpoint coefficients are nonnegative in both cases. Hence B0,B1,B2>=0. The exact closed-cell R supremum is max(B0,B2,actual right endpoint), which is max(B0,B2) when q<=1. B2 can be a left-limit value at an initial-term downward jump and need not be attained on the closed cell; the supremum remains valid. Original observation-cell suprema aggregate the gap-free final subcell suprema. Interior concave maxima attained at vertices are retained as vertex points.

The affine g_e on a final subcell elevates to degree two with coefficients [e0,(e0+e1)/2,e1], all nonnegative. Therefore the forcing polynomial c*P+g_e has nonnegative degree-two Bernstein coefficients Q_i=c*B_i+e_i^(2).

## 6. Positive signed-d_c exponential integration

For z=d_c*D and i=0,1,2 define

W_i(z,D)=D*integral_0^1 exp(z*(1-x))*binomial(2,i)*x^i*(1-x)^(2-i)dx.

Every W_i is positive for D>0 and every real z. Then

E_next=exp(z)*E_left+sum_(i=0)^2 W_i(z,D)*Q_i

is the exact raw ideal endpoint recurrence. It ignores only the measure-zero R jump at a right endpoint. At z=0, all W_i=D/3, and their sum always equals D*phi_1(z).

For x>=0, write W_i(x,D)=D*S_i(x), where

S_0(x)=sum_(n>=0) x^n/[n!*(n+3)],
S_1(x)=sum_(n>=0) 2*x^n/[n!*(n+2)*(n+3)],
S_2(x)=sum_(n>=0) 2*x^n/(n+3)!.

Proof: expand exp(x*(1-v)) and integrate each nonnegative term by the beta integral. For negative z, the substitution v->1-v gives W_i(z,D)=exp(z)*W_(2-i)(-z,D). This turns both signs into positive series and a positive exponential/reciprocal enclosure; no cancellation-prone division by d_c is needed.

For truncation after n=N=96 and 0<=x<=16, let t_(i,N+1) be the first omitted exact rational term. The ratio of each following term to its predecessor is <=x/(N+2)<1, because the beta moment decreases with n. Consequently

sum_(n=0)^N t_(i,n) <= S_i(x)
 <= sum_(n=0)^N t_(i,n)+t_(i,N+1)/(1-x/(N+2)).

The same positive Taylor tail bound applies to exp(x). The finite implementation encloses these exact rational sums by directed integer recurrences on scale S=2^128. Let x_l=floor(S*x), x_u=ceil(S*x), and start t_l=t_u=S. At step k set t_l=floor(t_l*x_l/(S*k)) and t_u=ceil(t_u*x_u/(S*k)). Induction gives t_l/S <= x^k/k! <= t_u/S. Multiplication by each positive rational beta coefficient followed by floor/ceil preserves that enclosure. The initial beta moment1/3 is also rounded in opposite directions. Add the exponential-tail bound evaluated at x_u/S to each upper moment; every beta multiplier is<=1, so this conservative common tail is valid. Summation and final dyadic conversion preserve the interval. Thus the code need not form a large exact Taylor sum before rounding.

For z<0, reciprocal bounds for exp(-z) and the swapped positive moments give the required enclosure. All interval products and sums have nonnegative inputs after the vertex lemma. This new moment proof extends the existing R11/R12 positive arithmetic pattern; it does not claim the old weight implementation already computes degree-two moments.

## 7. Closed-cell E certificate

On a final subcell, let Rmax be the exact Rcal supremum and gemax=max(e0,e1). Let Qmax=c*Rmax+gemax. For any valid E_left upper, the scalar constant-forcing majorant is

Y(u)=exp(d_c*u)*E_left+Qmax*integral_0^u exp(d_c*(u-v))dv.

It dominates E throughout the cell. Its derivative is exp(d_c*u)*(d_c*E_left+Qmax), whose sign is constant, so the cell upper is max(E_left,Y(D)). This covers signed d_c without an unproved endpoint-only rule for the actual time-dependent E. Propagate the tighter exact-polynomial endpoint upper into the next cell; calculate whole-E separately by this majorant. R remains the global comparison from t0 and is never restarted. Observation whole-cell bounds are maxima over their final refined subcells, including shared endpoints.

No generic source-cap adapter is introduced in this extension. R11 physical caps remain bound to their original forcing and source identity. Affine inputs cannot inherit them merely by sharing labels.

## 8. Analytic discriminating controls

1. Degree-zero reduction: set each forcing endpoint pair equal. Exact F, point R, and ideal E reduce to the R12 constant-source construction. Rounded bitidentity is a separate claim and is not assumed.
2. Polynomial forcing control: t0=0,T=1,q=1,tau=1,R0=E0=0,c=1,d_c=0,g_r(s)=s,g_e=0 gives R(t)=t^2/2 and E(t)=t^3/6. At T, R=1/2 and E=1/6. The same-cell supremum-constant source g_r=1 gives R=1,E=1/2. These are exact arithmetic controls, not physical-data improvements.
3. Interior maximum: q=0,tau=1,R0=0,g_r(s)=s for [0,1] and 2-s for [1,2]. On [1,2], R(t)=3t-t^2-3/2, with endpoints1/2 but interior maximum3/4 at t=3/2. This decisively tests rational vertex insertion and whole-cell versus endpoint distinction.
4. Fresh forcing: q=0 still retains all forcing of age<tau; setting every q-power to zero would fail controls2 and3.
5. Global memory: q=1/2,tau=1,g_r=1,R0=0 gives F(5/4)=9/8. Restarting R at t=1/2 as a new initial state would give5/4, changing the ideal comparison. Final/refined grids must retain the original source history.
6. Signed d_c, near-zero d_c, shifted rational t0, nonaligned observations, discontinuous affine endpoint pairs, q=0/1, source-refinement identity and observation-refinement identity are distinct finite controls. Exact ideal identity does not impose rounded bitidentity.

## 9. Monotonicity comparison and remaining scope

If g_affine<=g_sup pointwise, with common q/tau/initial/c/d_c, positivity of h and the scalar exponential implies Rcal_affine<=Rcal_sup and Ecal_affine<=Ecal_sup pointwise. Thus replacing a proved affine whole-domain bound by its cell supremum cannot improve these ideal comparisons. The actual gain depends on the supplied functions; no universal strict improvement or physical closure follows. Report ratios only when the denominator is nonzero.

Literature already provides polynomial-forcing exponential integration and phi functions. The project contribution is the exact assembly of the staircase memory kernel with affine bounds, rational translated-event/vertex refinement, positive quadratic signed moments, and finite outward enclosures under the preserved WU premises. No broad novelty theorem or strong no-go is proposed.

Remaining obligations for root: immutable latest-baseline/census acceptance; finite allowance contract; actual implementation; frozen primary/reference/CAS checks; independent proof/code review; scoped scientific adoption and stage receipts. No numerical result is asserted by this manual derivation.
