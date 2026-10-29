# R22 read-only reproducibility

The R22 private full SOURCE ZIP contains original R21 parent source tree and GL2022 institution PDF. For source and code identity, use exactly the included original material, never substitute a different pdf or a thermal rate table.

```bash
unzip -q WU_R22_SOURCE_ORIGINAL_20261029.zip -d /tmp/wu_r22_restore
cd /tmp/wu_r22_restore
PYTHONPATH=. python -m unittest -q research.wu_hd_state_energy_r22_20261029.tests.test_cross_paper_energy
PYTHONPATH=. python -O -m unittest -q research.wu_hd_state_energy_r22_20261029.tests.test_cross_paper_energy
PYTHONPATH=. python -m research.wu_hd_state_energy_r22_20261029.tests.independent_reference
PYTHONPATH=. python -m research.wu_hd_state_energy_r22_20261029.figures.render_energy
PYTHONPATH=. python -m research.wu_hd_state_energy_r22_20261029.src.cross_paper_energy \
 --literal-source research/wu_hd_state_energy_r22_20261029/source/CROSS_PAPER_LITERALS.json \
 --source-pdf ORIGINAL_SOURCES/GL2022_CSIC_supplement.pdf \
 --schedule research/wu_hd_thermal_mechanical_ledger_r21_20261029/results/EXAMPLE_SCHEDULE.json \
 --output /tmp/wu_r22_output_must_not_exist.json
```

Python3.13.5, pytest/unittest, mpmath, NumPy/SciPy, matplotlib, Poppler pdftotext. No network required. CLI output is exclusive-create. This is one self-contained conditional comparison test, not a source Q admission or full-network regression.
