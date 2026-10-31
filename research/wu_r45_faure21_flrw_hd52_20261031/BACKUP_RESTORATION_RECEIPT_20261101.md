# R45 remote binary restoration receipt | 2026-11-01 KST

**Scope**: Source-conditional WU R45. Scientific canonical DAG **34/49 unchanged**; auxiliary R45 **1/1 SCOPED**; shared R/C 18/20; distinct-author R6/C9 **NOT_RUN**. Immutable parent R44 PR #183 HEAD `98b2a23e019694683eff114fbc1d52e552f74ac2`. No main merge, no production, no automatic next node.

Post-publication backup of **private** archives was performed separately from the original thin GitHub research publication. Both named ZIPs were uploaded to **ChatGPT Library** and **Google Drive**, and **each provider's stored bytes were downloaded back**. The locally restored files were compared to their original bytes by SHA-256 and inspected with ZIP CRC.

| Immutable archive | Bytes | SHA-256 | Library restore | Drive restore |
|---|---:|---|---|---|
| `WU_R45_FAURE21_FLRW_HD52_20261031_SOURCE_MASTER.zip` | 4,043,431 | `f013ca474161b62f4f26c1090fa594ddf8924bb776005ca100e6fbe9198a2c73` | Exact SHA / CRC PASS | Exact SHA / CRC PASS |
| `WU_R45_FAURE21_FLRW_HD52_20261031_ALL_STAGES.zip` | 8,342,206 | `bc8a089b2504beb05527b81cb844613ad4830d522c108b75315f6916d8decad4` | Exact SHA / CRC PASS | Exact SHA / CRC PASS |

The returned Google Drive aggregate was also unpacked virtually and the **20/20 R1–R10/C1–C10 nested stage ZIP files matched the immutable recorded SHA-256** and individually passed CRC. Four phase ZIPs and the complete source master are the other five members. Library and Drive also contain the original 4,643-byte copyable R45-to-R46 handoff.

**Private backup locations** (listing access controlled by the user's connected account):
- ChatGPT Library: `/WU088_HH/R45_FAURE21_FLRW_HD52_20261031/`
- Google Drive: `/WU088_HH_R45_FAURE21_FLRW_HD52_20261031/`

**Scoped scientific tests freshly rerun after restoring interrupted work:** `python -m unittest discover -s tests -p 'test_*.py' -q` 28/28 PASS and `python -O -m unittest discover -s tests -p 'test_*.py' -q` 28/28 PASS. Ten numerical CSVs total 80,796 source-conditional physical-model rows; 41/41 recorded input/output SHA checks PASS, and previous full clean regeneration 23/23 byte-exact.

Private EMAA raw source and parser are **not on GitHub**. External binary backup **does not** constitute publication of experimental data, original Faure numerical history, global WU DAG admission, production readiness, chemical Q, full Grackle12 simulation or independent-author referee certification. PR #184 remains Draft; source-authentic research code published as a thin Git subtree.

**Provenance rule:** initial README/PR text saying remote backup `NOT_DONE` describes the state **at original PR creation**, superseded for these two exact archive objects by this dated receipt. The historical R43 sign-grid conflict 236/88 vs 224/100 remains `UNRESOLVED`.
