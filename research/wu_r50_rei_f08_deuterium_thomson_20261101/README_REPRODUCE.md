# WU R50 | Original REI F08 S0 passive-D Thomson source screen

Producer: cosmosapjw-quantum/WU088_HH, read-only source owner cosmosapjw-quantum/rei_bianchi PR349, exact HEAD 58f7ffb685c3758f1fed1113ff8134a24478c3df.
Protected WU parent PR188, HEAD f5d09daf5e70baa964aadda2156cd61facf495c4.
Original S0 input is prescribed/nonobservational and contains 16,001 rows each for FLRW and Bianchi, plus 10,752 original Bianchi photon ray rows; no new REI IVP.
Python >=3.11, standard library only. First restore source_inputs/ with these five exact files from the F08 source PR349 at the locked commit:
1. S0_BI-electron_density.csv.gz
2. S0_FLRW-electron_density.csv.gz
3. science_scenario_v1.json
4. ORIGINAL_F08_S0_BIANCHI_THOMSON_SKY.csv.gz
5. SOURCE_F08_THOMSON_SKY_SUMMARY_12.csv

All four SHA256 and one Git blob hashes are hardcoded in r50_deuterium_observer_screen.py. Do not replace with unrelated F05 H/He 46k archives or non-S0 data.
Commands, from the directory holding source_inputs:

    python3 r50_deuterium_observer_screen.py --out results
    python3 -m unittest test_r50 -q
    python3 -O -m unittest test_r50 -q
    python3 audit_r50.py

Reproducible output:
- results/R50_ORIGINAL_F08_S0_D_ELECTRON_THOMSON_CAP_10752.csv.gz : all source-direction model rows, conditional upper bound on extra Thomson optical depth and visibility
- results/R50_SOURCE_SKY_SUMMARY_12.csv : all 3 grid resolutions x 4 relative-redshift windows
- results/R50_REI_OBSERVER_WITNESS_12.csv : one real ray per group, selected by largest D cap
- results/R50_RESULTS.json : source hashes, numerical findings and preserved DAG status
- results/R50_SELF_ADVERSARIAL_AUDIT.json : separate same-author source scan and Decimal calculation
- plots/R50_D_OPACITY_RMS_CEILING.png/.svg when optional figure script run

The full archive may include original REI public frozen inputs (identical bytes), derived full output, code, tests, source-keyed mathematical derivation and one full stage ledger. Public Git may contain code, 12-row summary/witness, results/receipts only. Missing original sources in the thin Git copy are expected and explicitly restored as above.

Model contract: 0<=n_D+<=eta_D*nH with assumed eta_D=2.5e-5; no D reaction kinetics, no HD cooling, no H/He/electron feedback, no new cosmological redshift history. WU canonical 34/49, REI central 28/88, working 33/88, Fast 4/7, scientific delta 0. HH_R10 OFF; no main merge, no production, AUTO_NEXT false.
