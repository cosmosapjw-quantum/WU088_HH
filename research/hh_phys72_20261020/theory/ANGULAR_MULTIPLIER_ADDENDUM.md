# PHYS72 — angular and radial weights for the original screened multiplier

This addendum gives explicit angular Sobolev bounds for the original
off-center multiplier. It supplements the radial weighted `L2` estimate
and the boundary Poisson estimate in `MULTIPLIER_REMAINDER_DRAFT.md`.
The operator in sections 3–4 below is `K=R0^+ V`; its norms are stated on
specified radial/angular spaces. The sharper `L2` sandwich bound
`||sqrt(V) R0^+ sqrt(V)|| <= q` and the previously obtained order-four
remainder remain unchanged.

## 1. Uniform angular derivative of the actual screen

Use the inherited atomic coordinates and let

\[
B=27,\quad a=\frac7{10},\quad
d(r,\mu)=\sqrt{r^2+a^2-2ra\mu},\quad
V(r,\mu)=2(1+d^{-1})e^{-2d},\quad \mu=\cos\theta.
\]

Here `grad_S` is the gradient on the unit sphere; the volume norm for the
reduced radial field uses `dr dOmega`. For every `r>=B`,

\[
|\nabla_S d|=\frac{ra\sqrt{1-\mu^2}}{d}\le a,
\]

because

\[
d^2-r^2(1-\mu^2)=(r\mu-a)^2\ge0.
\]

The formula extends continuously at the poles. Since `d>=d0=B-a=263/10`,

\[
\frac{d}{dd}\log\{2(1+d^{-1})e^{-2d}\}
=-2-\frac1{d(d+1)},
\]

and consequently

\[
|\nabla_S\log V|
\le a\left(2+\frac1{d_0(d_0+1)}\right)
=\frac{502943}{358995}<\frac32.
\tag{A1}
\]

The exact positive margin is `71099/717990`. The prior exact envelope
audit in `SCREEN_ENVELOPE_EXACT.md` supplies

\[
0<V(r,\Omega)\le v(r):=\delta e^{-2(r-B)},
\qquad \delta=3\times10^{-23}.
\tag{A2}
\]

Equations (A1)–(A2) imply `|grad_S V| <= (3/2)v(r)`. These are direct
bounds on the original noncentral function. No angular average, finite
angular cutoff, or central replacement is introduced.

## 2. Multiplication on the full angular H1 space

Define

\[
\|g\|_{H^1(S^2)}^2
=\|g\|_{L^2(S^2)}^2+\|\nabla_S g\|_{L^2(S^2)}^2
=\sum_{j,m}(1+j(j+1))|g_{jm}|^2.
\]

For fixed `r`, put `p=||g||_L2` and `t=||grad_S g||_L2`. The product rule,
the triangle inequality in `L2`, and (A1)–(A2) give

\[
\|Vg\|_{H^1}^2
\le v(r)^2\{p^2+(t+\tfrac32p)^2\}
\le4v(r)^2(p^2+t^2).
\tag{A3}
\]

The last inequality is exactly

\[
4(p^2+t^2)-\{p^2+(t+\tfrac32p)^2\}
=\tfrac34(p-2t)^2\ge0.
\]

Equivalently the shear matrix `[[1,0],[3/2,1]]` has singular values `2`
and `1/2`. Thus `||M_V(r)||_(H1->H1) <= 2v(r)`. The shear constant is
exact for this estimate; no claim is made that the norm of the actual
screen multiplier equals that upper bound.

For any angular Hilbert space `Y`, define the radial weighted spaces

\[
\|u\|_{X_-(Y)}^2=\int_B^\infty r^{-2}\|u(r)\|_Y^2\,dr,
\qquad
\|f\|_{X_+(Y)}^2=\int_B^\infty r^2\|f(r)\|_Y^2\,dr.
\]

Since `r^2 exp[-2(r-B)]` decreases for `r>=27`, (A3) yields

\[
\boxed{\|V\|_{X_-(H^1)\to X_+(H^1)}\le2B^2\delta.}
\tag{A4}
\]

This norm includes angular differentiation and the radial weight. It is
not just the scalar essential-supremum multiplication norm on `L2`.

## 3. The actual outgoing Green operator preserves angular weights

Let `J=-Delta_S`. The central Coulomb differential operator, spherical
Dirichlet boundary at `B`, and outgoing condition commute with every
angular spectral projection. Thus the actual `R0^+` commutes with
`(1+J)^(1/2)` on the finite-harmonic compact-source core. Apply the already
proved all-angular radial estimate to `(1+J)^(1/2)f` and use density:

\[
\|R_0^+f\|_{X_-(H^1)}
\le C_*\|f\|_{X_+(H^1)},\qquad C_*=\frac{253}{1000}.
\tag{A5}
\]

No commutation of `V` with `J` is used or asserted. Combining (A4)–(A5),

\[
\boxed{\|R_0^+V\|_{X_-(H^1)\to X_-(H^1)}
\le q_{H^1}:=2q=1.106622\times10^{-20},}
\quad q=C_*B^2\delta=5.53311\times10^{-21}.
\tag{A6}
\]

Therefore `|lambda| q_H1 < 1` is an explicit sufficient Neumann condition
on this radial/angular space; it includes `lambda=1`.

## 4. The inherited unbounded angular weights remain explicit

Use exactly the angular norm already specified for the Poisson bound:

\[
\|g\|_C^2=\sum_{j,m}C_j^2|g_{jm}|^2,\qquad
C_j=\begin{cases}
77,&0\le j\le28,\\
\frac{800}{189}(j+1),&j\ge29.
\end{cases}
\]

All degrees are retained. Put `w_j^2=1+j(j+1)`. The following inequalities
hold uniformly in `j`:

\[
2w_j\le C_j\le77w_j,
\qquad
2\|g\|_{H^1}\le\|g\|_C\le77\|g\|_{H^1}.
\tag{A7}
\]

For `j<=28`, the lower comparison follows from
`77^2-4(1+28*29)=2677>0`, and the upper comparison from `w_j>=1`.
For `j>=29`, use

\[
w_j^2\le(j+1)^2\le2w_j^2,\qquad
\left(\frac{800}{189}\right)^2>4,\qquad
2\left(\frac{800}{189}\right)^2<77^2.
\]

The first pair follows respectively from the nonnegative differences
`j` and `j^2+1`; hence these are inequalities for all high degrees, not
an enumeration stopped at a chosen cutoff.

Combining (A3) and (A7),

\[
\|Vg\|_C\le77\|Vg\|_{H^1}
\le154v(r)\|g\|_{H^1}
\le77v(r)\|g\|_C.
\]

Consequently,

\[
\boxed{\|V\|_{X_-(H_C)\to X_+(H_C)}\le77B^2\delta.}
\tag{A8}
\]

The operator `R0^+` also commutes with the positive spectral multiplier
`C(J)`. Applying the same core-and-density argument as in section 3 gives
its bound `C_*` between `X_+(H_C)` and `X_-(H_C)`. Therefore

\[
\boxed{\|R_0^+V\|_{X_-(H_C)\to X_-(H_C)}
\le q_C:=77q=4.2604947\times10^{-19}.}
\tag{A9}
\]

The sufficient criterion `|lambda| q_C < 1` also includes `lambda=1`.
The constants are deliberately conservative. No sharp natural
`H^(1/2)` boundary-space assertion is made.

## 5. Relation to the fourth-and-higher remainder and exact audit

Equations (A6) and (A9) are bounds for `K=R0^+V` on the specified
radial/angular spaces. They do not assert those same bounds for the
different sandwich operator on `H1` or `H_C`. The original proof already
controls the sandwich `S=sqrt(V)R0^+sqrt(V)` on unweighted bulk `L2` by
the smaller constant `q`; that proof needs no angular derivative of the
screen. Its Poisson factors and final DtN remainder therefore retain
their previous sharper constants. In particular the fixed-entry
order-four-and-higher radius still uses `q`, not `2q` or `77q`.

`implementation/angular_weights.py` evaluates the finite rational
witnesses in (A1), (A3), and (A7), and the constants in (A4), (A6), (A8),
and (A9). It does not numerically establish a continuum inequality; the
derivations above provide that implication. The existing exact screen
envelope and actual outgoing Green estimate are explicit assumptions of
that scalar audit. It performs zero physical integrations, zero Coulomb
evaluations, zero old-panel or profile replays, and keeps `HH_R10=OFF`.

The single actual evaluation is saved as
`verification/ANGULAR_WEIGHTED_BOUNDS.json`, with its command, output
hash, source identities, and execution result in
`verification/ANGULAR_WEIGHTED_EXECUTION.json`. Existing `bounds.py`, its
tests, and completed enclosure outputs are unchanged. Independent
analytical review is recorded separately in the execution provenance.
