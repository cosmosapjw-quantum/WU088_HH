# WU R40 | 새 물리 계산 실행 보고

## 실제 수행 결과 (verified code execution)

- **SOURCE REUSE:** 업로드된 GL2022 보충자료 PDF는 R36 원본 PDF와 정확히 동일한 273,554 bytes, SHA-256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`. 별도의 미발견 source로 꾸미지 않았다.
- **원전 700개 인쇄 토큰 독립 추출:** GL2022 보충 Table 1–10의 10×7×10=700 토큰을 PDF에서 직접 파싱하여 R33 원래 source-token 배열과 **700/700 exact textual identity**. Table 11 thermal 토큰도 10/10 exact identity. 22개 printed-zero 표기는 censored로 유지. 표 1·2의 j=5 행 동일 토큰 10개 및 Table 8 j=3,j'=7, 2505K의 `6.72(16)` source anomalies 그대로 보존.
- **GL–EMAA 50개 기존 source mismatch:** R36 원본 1,560 cells vs EMAA 171×25 교차 비교 결과 50 divergent printed numbers/7 transition groups, 16 originally unprinted EMAA transition classes. 원저자 ACK 없고 corrected rate는 없음.
- **신규 first-v0 hitting Markov chain:** 10개 원본 T × 7개 v1 initial J × 12개 v0 landing J × 2 source lanes = **1,680 physically computed probability rows**, 140 case summaries and 490 independent one-source-pair lane sensitivities. GL print all-valid hybrid vs EMAA worst-case **L1 = 0.1842286866803165**, T=55K, initial HD(v1,J6). Example P(first J'=10) 0.102485 EMAA vs 0.022566 hybrid. The 8-cell GL original Table22 v1J6→v0J10 exponent mismatch drives isolated **L1=0.161330** at same T, not independently established physical error.
- **Energy and time sensitivity:** at 55 K v1J6, conditional net internal release (collision-only): EMAA 4495.531810 K×k_B and hybrid 4747.113504 K×k_B (difference 251.581694 K×k_B). Mean first-v0 time at n(H+)=1 cm^-3 9.680023×10^8 s vs 1.091778×10^9 s; this scales 1/n in the collision-only model, not an astrophysical age. Max internal release source difference 3.473460144972702×10^-21 J. Differences in v0J2→v0J0 are exactly invisible to the first-v0 stopping observable (70/70 source cases zero).
- **Distinct from R36:** R36 measured a 19-state stationary-population GL-hybrid L1 difference ≤0.00072834 under its radiation/density grid. Source choice can be substantially more consequential for a different, conditional early-hit observable. No contradiction between two different measures.
- **GL Table 11 restricted audit:** j0..6 reweighted printed cells match original Table 11 only approximately, e.g. 105K 1.72490213e-11 vs 1.73e-11, 3005K 7.1949165e-10 vs 7.22e-10 cm³/s; maximum relative difference across 10 nodes ≈2.49%. Original main Eq5 uses j0..8 vs supplementary uses j0..6 and other source/input limitations; cannot infer the authors' intended exact numerical source or fix it from the available 7-state tables.

## Verification status

- New local tests 14/14 normal, 14/14 Python -O. Includes 80-digit mpmath independent 7×7 linear algebra on 3 original T ×2 source versions ×3 initial J ×12 final J = 216 branch comparisons; max discrepancy below 1e-13 at these points. Wolfram exact two-transient absorbing-CTMC witness produces unit-normalized rational branches. These are same-author/method-independent numerical checks, not distinct-author R6/C9.
- Generator uses source 
unit check, probability normalization max |ΣP−1|=4.4408920985e−16. Source problem codes preserved; original R36/R39 artifacts unchanged.
- Separate replay and ZIP manifest evidence in archive manifest/logs. `GITHUB_CI` is NOT_RUN until an actual CI workflow is observed.

## Scope and scientific decision

`CANONICAL_DAG=34/49_UNCHANGED`; `R40_AUXILIARY=1/1_SCOPED`; `R_C_SCOPED=18/20`; `R6_DISTINCT_AUTHOR=NOT_RUN`, `C9_DISTINCT_AUTHOR=NOT_RUN`, `OWNER_ACK=NOT_OBTAINED`, `PHYSICAL_Q_FULL=NULL`, `PES_NATIVE_SCATTERING_THRESHOLD=NULL`, `HH_R10=OFF`, `L4=false`, `PRODUCTION=NOT_ISSUED`, `AUTO_NEXT_NODE=false`.

Next source-critical independent action: ask Tomás González-Lezana (corresponding author, *J. Chem. Phys.* 157, 214302 (2022), `t.gonzalez.lezana@csic.es`) for original machine-readable SQM inelastic raw numerical rate values & clarification of the 7 transition/50 temperature-cell differences versus EMAA DOI 10.17178/emaa_hd_rovibration_805a7aa5; request explicit 1v6→0J10 55–2505K exponent identity. Additional TiQM true S-matrix, if needed, through Maxence Lepers (`maxence.lepers@u-bourgogne.fr`), MNRAS 488, 4732 (2019) and 2021 erratum MNRAS 500, 430.
