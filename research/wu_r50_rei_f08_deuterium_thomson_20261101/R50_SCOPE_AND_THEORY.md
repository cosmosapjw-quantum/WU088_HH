# WU R50: original REI F08 S0 photon Thomson observable, primordial D+ electron-opacity ceiling
Date 2026-11-01. Role WU088_HH isotope source screening; REI original F08 PR349 observer physics is read-only.
**Protected WU parent:** Draft PR188 HEAD f5d09daf5e70baa964aadda2156cd61facf495c4. **Protected REI source:** Draft PR349 HEAD 58f7ffb685c3758f1fed1113ff8134a24478c3df, source pair 0a2bec874a5aa1b12f882033a08497b913b44447148b50b6082093bb354868e8.
F08 is one-cell prescribed FLRW/Bianchi S0 electron history, not actual observable EoR or full 26-event [160,161].
Input exact sha256:
S0_BI-electron_density.csv.gz 663911291bea564d314e1d46df9750c03a39fd5d9404eca6a7485776d894f723
S0_FLRW-electron_density.csv.gz 0b81cae87d6f90888d1d3def1995cd8d029625d1cc1dd11bffab94e8d30e7efa
science_scenario_v1.json c83d2d43adda663707f99af2b45576eb4478cd94d3440a21fd21eaed32b5f2c1
ORIGINAL_F08_S0_BIANCHI_THOMSON_SKY.csv.gz 41fb767cc6c826047abf3799164f9e5b6a970c9dc879566147ad036226e4588d
SOURCE_F08_THOMSON_SKY_SUMMARY_12.csv Git blob 99b951035605bbe58e8ce49b8fd611e85b72ec71
Assume passive deuterium tracer, 0<=n_D+(t)<=eta_D n_H(t), eta_D=2.5e-5 chosen upper *conditional parameter* from previous WU R49, not a measured upper confidence limit; fixed original n_H,n_e,T, metric, photon transport (no feedback).
Metric (-,+,+,+); prescribed diagonal Bianchi I, H_i=(1.01,.99,1)1e-14 s^-1, mean H=1e-14, t_observer=1e13 proper seconds. n_H(t)=n_H0 exp(-3 H t); photon proper Thomson opacity coefficient c sigma_T, 2.99792458e10 cm/s *6.6524587051e-25 cm^2.
At original F08 direction-dependent source emission time t_e(n,z_rel), tau_D^max(n)=c sigma_T eta_D n_H0 (exp(-3Ht_e)-exp(-3Ht_o))/(3H), a theorem for any passive time-varying D+ in [0,eta_D n_H].
No D+ chemical rates, density feedback, CMB z=0 LoS, HD cooling, or invented redshift/ionization histories. Directional RMS source sky perturbation bounded by max tau_D^max. Distinct original F08 sky geometric RMS from source summary, no changing original code.
**Scientific criterion:** produce 10,752 physically sourced directional upper-bound records, a conservative max effect on original observer geometry signal, source hashes/readbacks/tests; do NOT claim deuterium optical depth actually exists at that cap. WU 34/49 and REI central 28/88/working33/88, +0 until true owner admission. No main merge/production/autonext.
