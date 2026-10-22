#ifndef HH1_ENERGY_ADAPTER_H
#define HH1_ENERGY_ADAPTER_H

/* Proper seconds; energies eV; event rates per reference H1 per second.
 * This component maps supplied event rates to energy ledgers. It does not
 * supply D cross sections, rate coefficients or a radiation spectrum. */
enum hh1_status { HH1_OK=0, HH1_BAD_INPUT=1, HH1_BELOW_THRESHOLD=2,
                  HH1_NONFINITE_RESULT=3 };
enum hh1_kind { HH1_PI=0, HH1_RR_CASE_A=1 };
typedef struct {
    double thermal, binding, radiation, electron, photon_number;
} hh1_ledger;

int hh1_d_threshold(double hydrogen_ev, double isotope_defect_ev,
                    double *deuterium_ev);
int hh1_event(int kind, double ionization_ev, double photon_or_capture_ev,
              double rate_per_H_s, hh1_ledger *out);
int hh1_temperature_rhs(double temperature_K, double particles_per_H,
                       double heat_ev_per_H_s, double electron_per_H_s,
                       double hubble_per_s, double kb_ev_K, double *out);
#endif
