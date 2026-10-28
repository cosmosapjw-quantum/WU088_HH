# Finite-block contraction of the provided HD graph

This certificate concerns the exact rational supplied-edge generator constructed by source_geometry.mjs. It is not an uncertainty enclosure of the true molecular generator. Native100K para-H2 source rows and relative HD energies are inherited; pi is a normalized rational approximation to the declared finite Boltzmann weights. An exact chemical destruction vector is absent.

Let lambda=2 max_j(-K_jj)>0 and P=I+K/lambda. Its columns are stochastic and every diagonal is at least1/2. The existing adjacent downward edges provide a path from each j=0,...,8 to0. Pad that path with self-transitions at0 to length8. Its probability
eta_j=P_00^(8-j) product_(k=1..j) P_(k-1,k)
is positive and lower bounds (P^8)_(0,j). With eta=min_j eta_j, every column shares at least eta mass in row0. Therefore the zero-sum L1 contraction factor of P^8 is at most1-eta.

Uniformization gives exp(Kt)=exp(-lambda t) sum_m ((lambda t)^m/m!)P^m. At t0=8/lambda, keep the m=8 overlap and use all other stochastic powers' contraction factor <=1. Since e<3, the Poisson weight has the rational lower bound 8^8/(3^8*8!). Thus
||exp(Kt0)z||1 <= rho||z||1, 1^Tz=0,
rho=1-eta*8^8/(3^8*8!)<1.

This is a finite-block certificate. It is not substituted as a prefactor-one instantaneous coefficient a in the triangular differential comparison. The instantaneous coefficient delta(K)=0 for this sparse provided graph remains the correct value. Block iteration can separately use rho^floor(t/t0) for homogeneous evolution and needs its own forcing convolution if used for an inhomogeneous equation.

The clock is tau=n_collider*kappa_ref*t, with kappa_ref=1e-11 cm^3/s; no actual collider density or physical relaxation time is assigned.
