# R27 source-derived reactive–radiative atlas

A new source-qualified, conditional **physical datum**: `ncrit(J,T)=A(J->J-1)/K_J(T)` for HD J=1..6 at ten printed GL2022 temperatures. Derivation in `THEORY_KO.md`. No interpolated or fabricated reaction data. No spectroscopy-driven physical Q promotion.

Source references:
- GL2022 DOI 10.1063/5.0128598; printed SQM rates 700/700, source JSON byte-identical copy from WU PR165 with hardcoded tensor hash.
- REC PR161 `5bf22a4258ba571e8aebb1cfedab9cafe7ac6481`, LAMDA A transcription source git blob `bd5a7f0e29ff6dd228cd8e927d6932b74d8cb4b9`.
- 2019 BO (DOI 10.1093/mnras/stz1797), Velilla2008 PES (DOI 10.1063/1.2973629), 2024 LTE context (DOI 10.1093/mnras/stae994).

Run:
```bash
PYTHONPATH=. python -m unittest discover -s tests -p test_reactive_radiative.py -q
PYTHONPATH=. python -O -m unittest discover -s tests -p test_reactive_radiative.py -q
python -m src.reactive_radiative --r26-source-json sources/GL2022_700_SOURCE.json --rec-reference-json sources/REC161_LAMDA_A_TRANSCRIPTION_REF.json --out results
```
Central DAG remains 34/49; R27 auxiliary 1/1 scoped; R6/C9 distinct-author NOT_RUN. No Q/native PES/owner/production claims. See `DAG_DELTA.json` and `HANDOFF_NEXT_THREAD_KO.md`.
