# R49 source-conditional REI thermal materiality screen

Source owner WU088_HH. Original REI solver inputs are immutable; data are from explicitly named archived PR347 and PR348 REI F05 model output; previous WU R48 public witness has different original-source archive identity.

Run with Python >=3.11 (standard library only):
```bash
python3 r49_materiality.py \
  --energy /private/REI_F05_ORIGINAL26_NATIVE_DISCRETE_ENERGY_46080.csv.gz \
  --increment /private/REI_ORIGINAL26_COMMON_PARENT_INCREMENT_46080.csv.gz \
  --wu-witness R48_PHYSICAL_5_WITNESS_TRANSITIONS.csv \
  --out results
python3 -m unittest test_r49 -q
python3 -O -m unittest test_r49 -q
```
Hashes hardlocked in the script. Full 46,080-row derived CSV is **not published on this Git branch**; local archive retention only. Results JSON and source-authored code + witness are publishable subsets. Both REI original source T and x and public WU R48 witness are author-owned derived model state, **not observational data**. No HD abundance/radiation state/Bianchi history is integrated. Source-archive discrepancy is deliberately preserved.

Scientific canonical status: WU **34/49**; REI central **28/88**, working **33/88**; promotion delta **0**.
NO_MAIN_MERGE; DRAFT; PRODUCTION HOLD; HH_R10 OFF; L4 false.
