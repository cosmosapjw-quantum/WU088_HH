# R4/R5 archive completion after runtime recovery

The current invocation made actual Python and C++ service probes; no filesystem process launched. Git checkpoints and exact native Drive text capsules succeeded. This protocol is prepared, not executed.

1. Probe the current execution host and Git access. Read current AGENTS.md and remote branch HEAD. Use isolated detached worktrees for each pinned source commit; preserve parallel changes.
2. R4: pin 4ea08eb3709c90285946dce2cf824f402056d645. The accepted scientific payload is 34765b943cce5a67d49a622f76c0cf9aeceb635c8cd6a3cf58b5cebb8e3c5fde. Use that commit's R4 delivery/package_checkpoint.py with --stage S10 --full. Do not rerun science.
3. R5: obtain exact S10 source commit from delivery/PUBLICATION_INDEX.json, not from an assumed branch head. Run the R5 delivery/package_checkpoint.py in that pinned worktree with --stage S10 --full. The script writes a new ZIP and uniquely named create-only receipt; it never executes research code.
4. For per-stage R5 ZIPs S01..S09, use the actual respective source commits recorded in the index. Run the final prepared packager externally with --repo pointing to the appropriate detached checkout. Its host execution remains unverified until runtime recovery. Early commits do not yet contain the packager. Do not claim an absent script exists in an early checkpoint.
5. Preserve actual archive source SHA/tree, size, SHA256, member paths/modes/git blob/SHA256, ZIP CRC, command, CPU/wall measurement, tool ACKs and actual provider object IDs. Upload actual files, create-only, to the existing WU Dropbox and Drive folders. Never pass fictitious local paths.
6. Download original bytes from both providers and recheck ZIP SHA256, all member SHA256, Git blob identity and CRC. Metadata/listing, a text capsule, a conversion/export, or an upload success alone is not original-byte readback.
7. Publish delivery receipts as a new metadata commit with expected SHA and force=false. Keep source archive identity and later metadata HEAD separate. Recheck PR150 remains draft; do not merge main.
8. Only then close the matching archive-delivery gates. R4 workflow18/20 and R5 R10/C10 full delivery remain open until their actual gates pass.

Text fallback: export the native checkpoint document as plain UTF-8 text and use recover_doc_capsules.py into a new directory. It validates capsule headers, SHA256, Git blob identities and source chain before restoring overlays. It is an overlay over the pinned parent, not a full Git clone. The recovery script has been statically prepared and has not been executed on the unavailable host.

Existing authorization covers additive publication and backups. The present blocker is execution-host availability, not a new permission request.
