# WU088_HH R43 | Full binary source restoration, 2026-10-31

This is a NEW recovered source master, not the same ZIP bytes as the original lost R43 master from PR182. Old historical source SHA 58c4c095d6f3601a8251cf2e94db74d1b3dbe00ac48d2b01912517c5ce62310a is retained separately.

- RECOVERED SOURCE ZIP: WU_R43_RECOVERED_HD52_EMAA_GRACKLE_SOURCE_20261031.zip, **6,953,013 bytes**, SHA256 **a715301114cfb2fd66361f9519081dc38033765e3b76b517bac5bc78fbe91a50**.
- RECOVERED FULL BUNDLE: WU_R43_RECOVERED_ALL_STAGE_AND_SOURCE_20261031.zip, **7,130,330 bytes**, SHA256 **9b9d31dbc685d7a2765b41f59eb249f9b504f57439492153b0cb45515f03f165**.
- Uploaded and separately read back at Library /WU088_HH/R43_HD52_NLTE_RECOVERY_20261031/ and Google Drive /Google Drive/WU088_HH_R43_HD52_NLTE_RECOVERY_20261031/. Both providers' master downloaded byte-exact SHA, ZIP CRC and source file manifest 35/35; both bundle downloaded byte-exact SHA, inner 25 ZIP SHA+CRC PASS.
- Per-provider 26 files exactly: 20 stage ZIP, 4 phase ZIP, 1 source master, 1 bundled master. All provider ACKs recorded, directory lists 26/26; source master 3-way byte-exact, full bundle 3-way byte-exact.
- From original EMAA H collision source: 324 physical conditions, 16,848 level-population rows, 119,232 photon line rows, 15 Grackle rates and 324 case rows: total 136,419 derived numeric rows, all in private SOURCE master.
- Fresh Python tests: 27/27 normal, 27/27 optimized PASS; clean extraction regenerate 5/5 data files byte-identical. Source original RADEX SHA256 b0db1613425e403889c3a74f6cd9e142c562a552f1ebf05e61cbf509cd429c94.
- Numerical discrepancy: historical PR182 text claimed cooling 236 and heating 88 conditions; explicit reconstructed original-grid contract gives cooling 224 / heating 100. Exact old complete grid unknown, so keep as UNRESOLVED and do not change historical claim silently.
- Git publication new source/report/derived output only, raw third-party EMAA not redistributed. Parent PR181 untouched. Canonical WU DAG remains **34/49**, R43 scoped auxiliary 1/1, R/C **18/20**, R6 and C9 distinct author NOT_RUN, HH_R10 OFF, L4 false, production HOLD, auto next false.
