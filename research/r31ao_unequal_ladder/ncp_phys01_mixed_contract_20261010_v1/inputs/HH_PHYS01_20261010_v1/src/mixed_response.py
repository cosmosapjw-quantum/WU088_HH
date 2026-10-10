"""Local Taylor coefficients; not a production photon/gas time integrator.

The returned coefficients multiply a*q*lambda*S*duration**3.
They describe a frozen smooth source stage with constant external photon rate.
No finite-duration remainder bound, actual native root, or history is issued.
"""
from fractions import Fraction as F

# (coefficient of J^2 F, coefficient of F''[F,F], gas source S response at t^2)
WEIGHTS = {
    'continuous': (F(1,6), F(1,6), F(1,2)),
    'BE_full': (F(1), F(1,2), F(1)),
    'BE_two_half': (F(1,2), F(5,16), F(3,4)),
}

def factors(beta):
    """beta=(u/Pi)*(T k'/k)*(1-T_gamma/T); rational beta stays exact."""
    z = -2-beta  # u*(q_x+g*q_w)/q; no division by u in returned formula
    return {key:{'x': alpha*z-2*hb, 'P': 2*hb,
                 'J_HH': alpha*z, 'J_photo': -2*hb,
                 'second_gas_response': second}
            for key,(alpha,hb,second) in WEIGHTS.items()}

def energy_factor(beta, chi, excess):
    f=factors(beta)
    return {key: excess*value['J_photo']-chi*value['J_HH']
            for key,value in f.items()}

def temperature_factor(beta, chi, excess, C, T, particles, neutral):
    f=factors(beta); wf=energy_factor(beta,chi,excess)
    cross_hessian=(2*T+C*chi-C*excess)/particles**2
    return {key:(C*wf[key]-T*value['x'])/particles
            +value['second_gas_response']*neutral*cross_hessian
            for key,value in f.items()}
