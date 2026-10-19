# WU088_HH PHYS66: publish prepared changes and execute only new long-tail cases

Use the installed physmath-research-loop. Do not ask the user for manual file downloads, key transfers, or solver design. First inspect backups/current repo so completed work is reused.

Remote repository: https://github.com/cosmosapjw-quantum/WU088_HH
Newest read theory PR115:445d82db9c42b4f2f81e4ac1b107dec3b69b3c24,
branch research/hh-phys66-r5-order-cutoff-20261018.
PR114 prerequisite:bad80f7729015c84c8dde27f1b1dec3a1f8b2c9f.
PHYS64 NCP20 already completed in PR113; do NOT rerun those.

The current ChatGPT invocation has NO exposed GitHub/cloud write actions. Thus the NEW C5-C8 code is NOT on origin yet. Automatically retrieve this conversation's WU088_HH_PHYS66_SOURCE_AND_EVIDENCE_20261018.zip, WU088_HH_PHYS66_ADD_ONLY.patch, PHYS66_DELIVERY_20261018.json and SHA256SUMS through available file tools. Verify hashes against the delivery. Do not pretend git clone alone retrieves these new files. If conversation artifacts cannot be accessed, report BLOCKED_ARTIFACT_ACCESS without synthesizing results or requesting that the user implement anything.

Preserve dirty worktrees, prior local PHYS65 and all NCP outputs. Read the final delivery and late-upstream synchronization note. Local commits are SOURCE-SNAPSHOT commits, NOT claimed descendants of PR115. The supplied final patch contains only new PHYS66 paths and avoids the six PR115 paths, including r5/PROOF.md and r5/NEXT_DAG.json. Work on an isolated branch based on PR115 or its inspected successor. Use git apply --check, then git apply --index and a new additive commit. Do not reset remote state to the old local snapshot or apply the old PHYS65 proof over the newer upstream proof. Check new path collisions before any mutation.

Read:
research/hh_phys66_20261018/local_verification/PROOF.md
research/hh_phys66_20261018/c5c8/REPORT_KO.md
research/hh_phys66_20261018/c5c8/NEXT_DAG.json

Exact original input:
research/hh_phys34_20261015/inputs/FROZEN_U_SUBSET.npz
SHA256 f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d.
Upstream phys65_exterior_bounds.py Git blob must be
935d8ec1b765e5f1bd7c6ad0d95c9c74acf33512 or an explicitly reviewed compatible successor.
No physical source/tolerance/production owner changes.

This implementation is complete Python, not an unimplemented Rust port. Use Python3.11+; if dependencies are absent, use an isolated venv and requirements-tested.txt, preserving the shared NCP environment.

Run the NEW focused tests:
python3 -m pytest -q tests/test_phys66_radial_budget.py tests/test_phys66_campaign_ledger.py tests/test_phys66_endpoint.py tests/test_phys66_campaign.py

Import, do not rerun, the previous NCP results:
python3 scripts/phys66_import_results.py
This verifies the existing SOURCE_RESULTS.zip SHA d7fa0b50ed803e19dfcec8f781219c03acbd21f8f3ee47fe922754f8fdb5ea79,149 manifest payloads,20 success receipts and18 extended cases. If working from the portable snapshot instead of full repo, the same archive is _intake/PHYS64_NCP_SOURCE_RESULTS.zip; pass --archive with that path.

Check hostname/nproc/free -h. On the approved NCP s1a0e5abed09,64CPU,~125GiB, run directly, not through SSH. Only when on the authorized desktop use the existing ssh -i /home/cosmosapjw/.ssh/ncp_key -o IdentitiesOnly=yes root@49.50.142.2 -p22 connection. Never copy/display private keys or disable host verification.

Actual current-host commands:
python3 scripts/phys66_ncp.py --preflight-only --out research/hh_phys66_20261018/ncp_run
python3 scripts/phys66_ncp.py --profile smoke --workers 2 --resume --out research/hh_phys66_20261018/ncp_run
python3 scripts/phys66_ncp.py --profile longtail --workers 2 --memory-gib 4 --timeout 180 --resume --out research/hh_phys66_20261018/ncp_run

Stop before longtail if tests/preflight/smoke fail. Preserve first failure logs and make only diagnosed small repairs, not tolerance widening. The new longtail profile has6 cases: L28/64, T55/65/75,m0, join39,3 orders. It never selects the old PHYS64 extended18 profile. Default two workers,4GiB per case,nice10,BLAS1 and180s case timeout preserve shared resources. Resume only exact input/code/config/runtime and hash-verified payloads. Each case carries ALL z,logp,Y1,Y2,Y3 across the join; no coefficient reset and no total-minus-first-Born cancellation.

Science: coefficient-wise radial bounds beta1=a theta, beta2=a chi theta, beta3=5a chi^2 theta/4 are exact finite-L continuum components; theta=exp[-2(T-27)]. At L64,T65 beta3<1e-78. This is not total numerical accuracy. The higher-Born remainder and excluded angular, Coulomb, angle quadrature, ODE and roundoff errors must be kept separate. Do not promote inherited result flags. PHYS63 qualitative all-angular real-axis LAP is retained. Original xi=Fy-phi, regular origin/adjoint, sigma(E), Maxwellian k_HH(T) remain open; HH_R10=OFF.

After completion inspect CAMPAIGN_smoke.json/CAMPAIGN_longtail.json, case RESULT.json/COEFFICIENTS.npz, stderr/exit/wall/RSS and SOURCE_RESULTS.zip checksum. Publish an additive branch/Draft PR through the existing authorized GitHub path. Upload source/results capsule and Git bundle to Dropbox and Google Drive using existing approved tools; independently download, hash, inspect manifests and verify bundle. Separate LOCAL_ARCHIVED,UPLOAD_ACK and RESTORE_VERIFIED. If writes are unavailable, preserve locally and explicitly record the blocker without claiming success. Return actual case counts/new vs reused, new scientific data, all error scopes, commit/tree/PR, backup readback and next READY DAG in Korean.
