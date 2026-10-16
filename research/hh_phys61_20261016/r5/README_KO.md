# PHYS61 R5 checkpoint

이 단계는 E=49/200+i/100 Hartree의 실제 원래 비중심 screened 외부영역을 **무한 angular**에서 다룬다. 엄밀한 DtN 차이 X→X* 상계는 <4×10^-19이고, Im E↓0 실수 산란 극한은 OPEN이다.

실행: `PYTHONPATH=src python -m pytest -q tests/test_phys61_absorptive_dtn.py`와 `PYTHONPATH=src python scripts/phys61_absorptive_dtn.py --source research/hh_phys34_20261015/inputs/FROZEN_U_SUBSET.npz --out /tmp/PHYS61.json`. 원본 NPZ SHA를 변경하지 않는다.

Source prior PR104 SHA `94908dce03b7cacf288ed33f916ab4b9f7d3efe7`; 다음 단계 C5-C8 복소 Coulomb/Whittaker 실측 진단, 이후 PHYS62 real on-shell LAP. 소비처 `rei_bianchi HH_R10=OFF`.
