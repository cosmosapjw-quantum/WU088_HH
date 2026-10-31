# Original-document inspection / literal original-source status

GL2022 González-Lezana, Hily-Blant, Faure, JCP 157, 214302 (2022), DOI 10.1063/5.0128598. The user-supplied `214302_1_epaps.zip` has a single original 14-page PDF. PDF is byte-identical to the CSIC supplement used in WU R36, not a second source.

- Page 5: supplement §3 announces reaction state-to-state numerical rate tables 1–10, thermal Table 11, HD inelastic Tables 12–28; it states initial HD thermal j up to 6, whereas main JCP text Eq5 describes initial j up to 8.
- Page 6 Tables 1 and 2: the 10 entries for input HD(v0,j5) are textually identical for H2 outgoing j'=0 and 1. The 2022 raw tokens are left unchanged; owner-level validation required.
- Page 8 Table 8: HD(v0,j3)→H2(v0,j'7), T=2505 K reads literally `6.72(16)` whereas adjacent high-T values carry exponent (11). No correction assumed.
- Pages 6–9: 22 numerically printed `0.00(00)`/`.000(00)` rate tokens are source-censored, not known exact zero. In the reproduced partial thermal lower-bound sum these contribute only the nonnegative bound 0, with the unmeasured true value retained as unknown.
- Page 13 Table 22 HD(v1,J6)→HD(v0,J10): 55–2505 K source exponents `11` are inconsistent with EMAA numeric values that have exponents `10`; 8 cell ratios exactly 0.1. At 15 and 3005 K the printed tokens are 10^-10 and align with EMAA. R36 independently pinned 50 discrepant cells across 7 transitions; this session does **not** certify which representation is correct.
- Page 1-14 of main 2022 paper is not independently included; only the 9 page original user PDF main paper and the 14 page supplement plus published 2019/2021 MNRAS are source targets. All displayed screenshots are kept in private archived evidence, not public Git.

Evidence: new independent `pdftotext -layout` parser reads 700/700 reaction printed tokens and Table11 10/10 exact according to preexisting R33 source lock. Screenshot page_6.png, page_8.png, table22_page13.png visually checked. The comparison confirms reliable extraction and inherited source identity, not a newly discovered original rate table.
