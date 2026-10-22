#include "hh1_energy_adapter.h"
#include <math.h>

int hh1_d_threshold(double h, double delta, double *out) {
    if (!out || !isfinite(h) || h <= 0.0 || !isfinite(delta) || delta < 0.0)
        return HH1_BAD_INPUT;
    const double d = h + delta;
    if (!isfinite(d)) return HH1_NONFINITE_RESULT;
    *out = d;
    return HH1_OK;
}

int hh1_event(int kind, double ion, double energy, double rate, hh1_ledger *out) {
    if (!out || !isfinite(ion) || ion <= 0.0 || !isfinite(energy) ||
        energy < 0.0 || !isfinite(rate) || rate < 0.0 ||
        (kind != HH1_PI && kind != HH1_RR_CASE_A)) return HH1_BAD_INPUT;
    hh1_ledger next;
    if (kind == HH1_PI) {
        if (energy < ion) return HH1_BELOW_THRESHOLD;
        /* Form excess before multiplying: no subtraction of two large powers. */
        next.thermal = (energy-ion)*rate;
        next.binding = ion*rate;
        next.radiation = -(energy*rate);
        next.electron = rate;
        next.photon_number = -rate;
    } else {
        next.thermal = -(energy*rate);
        next.binding = -(ion*rate);
        next.radiation = (ion+energy)*rate;
        next.electron = -rate;
        next.photon_number = rate;
    }
    if (!isfinite(next.thermal) || !isfinite(next.binding) ||
        !isfinite(next.radiation)) return HH1_NONFINITE_RESULT;
    *out = next;
    return HH1_OK;
}

int hh1_temperature_rhs(double t, double n, double q, double dx,
                       double h, double kb, double *out) {
    if (!out || !isfinite(t) || t <= 0.0 || !isfinite(n) || n <= 0.0 ||
        !isfinite(q) || !isfinite(dx) || !isfinite(h) ||
        !isfinite(kb) || kb <= 0.0) return HH1_BAD_INPUT;
    /* u=(3/2) k_B T N, du/dt=-2 H u+q, dN/dt=dx_e/dt. */
    const double value = -2.0*h*t + (2.0/3.0)*(q/n)/kb - t*(dx/n);
    if (!isfinite(value)) return HH1_NONFINITE_RESULT;
    *out = value;
    return HH1_OK;
}
