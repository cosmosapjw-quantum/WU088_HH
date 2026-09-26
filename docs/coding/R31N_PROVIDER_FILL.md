# R31N source-bound provider fill

## One-command local execution

```bash
export WORK=/mnt/sn850x2t/hh_heavy_manual_20260926
export RUNTIME="$WORK/runtime/WU088_HH_LOCAL_RUNTIME_SEED_20260926_v2"
source "$WORK/venv/bin/activate"
cd "$HOME/WU088_HH"

export GDRIVE_RCLONE_REMOTE='gdrv:'
export DROPBOX_RCLONE_REMOTE='dbx:'

bash scripts/r31n_run_provider_fill.sh
```

No browser/manual ZIP download is needed. `r31n_restore_cp4.sh` downloads the three immutable CP4 split parts from the existing Dropbox durable location, checks each part hash, reconstructs the parent ZIP, requires exact SHA `c10c932a...17cd9`, runs ZIP CRC verification, and extracts a disposable working copy.

`r31n_provider_fill.py` then computes only:

- OD192 at z=16,32,48,64;
- JVP192 at z=48.

It uses 12 physical cores as 12 independent serial pair workers. Existing pair files are resumed, not recomputed. Each completed node is sealed and backed up to Drive + Dropbox using raw SHA-256/size readback.

Expected final status:

`R31N_PROVIDER_FILL_COMPLETE_DURABLE`

The summary is written to

`$WORK/r31n_provider_fill/R31N_PROVIDER_FILL_SUMMARY.json`.

Do not delete the source split archive or completed H anchor states. Do not substitute the R31K H O/D arrays for the CP4 O/D provider.
