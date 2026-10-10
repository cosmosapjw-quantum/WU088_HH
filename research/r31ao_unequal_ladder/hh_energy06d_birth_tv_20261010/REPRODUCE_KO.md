# ENERGY06D 재현

Python >=3.10 stdlib. 원 2026-10-09 NCP ENERGY06C에서 SHA-256으로 선택 검증한 입력 11개를 포함한다. 원 archive 전체와 원 runtime를 다시 다운로드하거나 실행할 필요는 없다.

압축 해제 후 새 빈 경로에서:

```bash
python3 -m unittest discover -s tests -v
python3 run_analysis.py --out results/reproduce-new
python3 independent_verify.py --results results/reproduce-new
sha256sum results/reproduce-new/ANGULAR_BIRTH.json results/reproduce-new/C1_SERIES_TAIL.json
```

`run_analysis.py`는 이미 존재하는 출력 directory에 덮어쓰지 않고 실패한다. `inputs/INPUT_IDENTITY.json`을 사용해 원 source byte identity를 검사하고, 원 `BIRTH_LEDGER` 12개 exact products를 모두 대조한다. 저장된 과학 결과(`results/science/`)와 새 계산 JSON은 byte identical이어야 한다. C1의 꼬리 보조정리는 selected scalar 1F1에만 유효하다. 새 BE root / HH integral/ NCP dispatcher / full49/physical admission은 실행하지 않는다.
