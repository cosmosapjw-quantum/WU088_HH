# PHYS66 실행 안내

입력·원격 기준·과학적 한계는 REPORT_KO.md와 NEXT_DAG.json을 읽는다.

새 로컬 snapshot의 스크립트는 완성된 Python이다. 원래 PHYS64 NCP20을 다시 실행하지 않는다.

```sh
python scripts/phys66_radial_budget.py
python scripts/phys66_import_results.py --archive _intake/PHYS64_NCP_SOURCE_RESULTS.zip
python -m pytest -q tests/test_phys66*.py
python scripts/phys66_ncp.py --preflight-only --out /tmp/phys66_preflight
python scripts/phys66_ncp.py --profile smoke --workers 2 --resume --out /tmp/phys66_run
# 마지막 실제 NCP 단계만 미실행:
python scripts/phys66_ncp.py --profile longtail --workers 2 --memory-gib 4 --timeout 180 --resume --out /tmp/phys66_run
```

최신 원격PR115를 자동으로 덮어쓰지 않는다. 새 코드의원격push/업로드는 현재 쓰기 동작 부재로 BLOCKED. 제공 patch는 새 경로만 추가한다. Git snapshot ancestry와 실제remote ancestry가 다르므로 stale HEAD로reset하지 않는다.
