# PHYS72 — exact audit of the original screened multiplier envelope

This independent audit reuses and verifies the existing screen majorant. It
changes neither the original potential nor its normalization. All coordinates
in this calculation are the inherited dimensionless atomic coordinates.

## Original potential and pointwise comparison

At B=27, R0=7/10, and μ∈[-1,1],

    d(r,μ)=sqrt(r²+R0²-2rR0μ),
    V(r,μ)=2(1+1/d(r,μ)) exp[-2d(r,μ)].

The triangle inequality gives d(r,μ)≥r-R0>0 for all r≥B. The function

    W(d)=2(1+1/d)exp(-2d)

is decreasing for positive d, because

    W'(d)=-2 exp(-2d)[2(1+1/d)+1/d²]<0.

Consequently

    V(r,μ)≤2(1+1/(r-R0)) exp[-2(r-R0)].

Write x=r-B≥0 and d0=B-R0=263/10. The prefactor decreases in r, so

    V(r,μ)≤2(1+1/d0) exp(-2d0) exp(-2x)
          =(546/263) exp(-263/5) exp(-2x).            (1)

This is a bound for the original off-center multiplier, uniformly in the
angular variable. It does not replace the operator by a central potential.

## Finite exact positive Taylor witness

Define the exact rational number

    S80 = Σ_(n=0)^80 (263/5)^n/n!.

Every omitted Taylor term is positive, hence exp(263/5)>S80 and

    (546/263) exp(-263/5) < 546/(263 S80).

The necessary comparison for the inherited δ=3/10^23 is the exact rational
inequality

    S80 > 182·10^23/263.                              (2)

The successful standard-library Fraction execution recorded below evaluated
(2) exactly. Its informative decimal ratio and envelope display were

    S80 / (182·10^23/263)
       =1.0085592008197680981552124671931672508361619822164…,
    546/(263 S80)
       =2.9745403121220516807002440801141471727709477708632…×10^-23.

The decimals are displays, not authoritative rational endpoints. Equations
(1)–(2), together with the exact Fraction comparison, give

    0<V(r,μ)<δ exp[-2(r-B)],    δ=3/10^23,
    r≥27, -1≤μ≤1.                                      (3)

For the weighted operator norm, r² exp[-2(r-B)] is decreasing on r≥27,
since its derivative is 2r(1-r)exp[-2(r-B)]<0. Thus

    ess sup_(r,μ) r²V(r,μ)≤B²δ=2187/10^23.              (4)

Angular multiplication on L²(S²) has its pointwise essential-supremum norm,
so (4) contains no angular channel-count factor. No centrifugal or Coulomb
constant is substituted into this multiplier bound.

## Actual already executed audit and provenance

The following exact stdin program was executed once during the current
PHYS72 lane; it was not rerun to create this note:

```python
from fractions import Fraction as Q
from decimal import Decimal, localcontext
x = Q(263, 5)
term = Q(1)
s = term
threshold = Q(182 * 10**23, 263)
first = None
for n in range(1, 81):
    term *= x / n
    s += term
    if s > threshold and first is None:
        first = n
upper = Q(546, 263) / s
print('degree', 80, 'first_degree_satisfying_delta', first,
      'exact_upper_lt_delta', upper < Q(3, 10**23))
with localcontext() as c:
    c.prec = 50
    print('S80_over_required',
          Decimal((s / threshold).numerator) /
          Decimal((s / threshold).denominator))
    print('screen_envelope_upper',
          Decimal(upper.numerator) / Decimal(upper.denominator))
```

Preserved tool output:

```text
degree 80 first_degree_satisfying_delta 71 exact_upper_lt_delta True
S80_over_required 1.0085592008197680981552124671931672508361619822164
screen_envelope_upper 2.9745403121220516807002440801141471727709477708632E-23
```

The execution used `python3` from the current primary runtime
(Python 3.12.14), standard-library Fraction/Decimal only, and cwd
`/workspace/scratch/1b90a4a1175e/WU088_HH`. Tool execution chunk ID was
`7daef6`, exit code 0, reported wall time 0.00004 seconds. The tool did not
record an execution UTC timestamp. The calculation used no radial
integration, angular quadrature, Coulomb evaluation, frozen-source evaluation,
or inherited campaign replay. The minimum qualifying degree 71 was an
additional observed arithmetic diagnostic; the proof uses the explicit S80
witness and does not require that minimum-degree result.

This note preserves the original δ rather than tightening or changing a
scientific acceptance criterion. It is an exact arithmetic audit of a
previously accepted pointwise assumption, with the derivative and triangle
inequalities supplied explicitly above.
