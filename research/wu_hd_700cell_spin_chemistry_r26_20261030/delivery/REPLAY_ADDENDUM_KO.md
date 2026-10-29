# WU088_HH R26 | P04 배포 이후 중첩 R25 의존성 복원 보정

분류: `PACKAGING/REPLAY_PROTOCOL_REPAIR`, **과학 결과 및 원본 SOURCE ZIP 수정 없음**. R26 신규 Draft PR #165 위에 새로운 additive 보정으로 추가한다. 중앙 DAG 여전히 34/49.

실제 Library에 업로드한 R26 SOURCE 원본 ZIP(2,133,825 bytes; SHA256 `2b97895ef22c8db474f75591ba65558be290f94c25d19556836f555a6fa08844`)을 깨끗한 경로로 복원할 때 `tests/test_r26.py`의 R25 token identity 테스트 1개가 `parent_R25/sources/GL2022_NATIVE_PRODUCT_GRID_R25.json` 부재로 `FileNotFoundError`를 냈다. 이 JSON의 **정확한 원본 bytes는 이미 R26 ZIP 안의** `parent_R25/WU_R25_SOURCE_ORIGINAL_20261029.zip`에 들어 있다. 직계 원본 R25 nested ZIP SHA256 `c00daeb40ae385f776c727a770ece0a3faee577496bcb621ae066294e94efca1`; 내부 JSON 3039 bytes SHA256 `c53810ebbd585a2d8d6ce46d2023644b718b8f13e2e5cfb6034ded16621bc7ad`.

따라서 original ZIP은 덮어쓰거나 새 SHA로 바꾸지 않고 **동봉된 중첩 ZIP에서 단일 JSON만 exact-byte로 꺼낸다**. `delivery/replay_parent_r25.py`는 원본 ZIP과 내부 JSON SHA, CRC를 검사하고 원본 목표가 없을 때만 exclusive-create한다. 현존 파일은 동일 SHA일 때만 통과한다.

실제 재생:

```bash
mkdir -p R26_CLEAN
unzip -q WU_R26_SOURCE_ORIGINAL_20261030.zip -d R26_CLEAN
# 현재 repo/PR #165의 delivery/replay_parent_r25.py를 R26_CLEAN/delivery/ 에 복사
cd R26_CLEAN
python delivery/replay_parent_r25.py --root .
PYTHONPATH=. python -m unittest discover -s tests -p test_r26.py -q
PYTHONPATH=. python -O -m unittest discover -s tests -p test_r26.py -q
python tests/independent_fitz_source.py
python tests/independent_sympy_commutator.py
```

초기 실패는 **원본 내부의 reference extraction omission**, 물리·수치 검증 실패가 아니다. 중첩 R25 JSON 복원 후 실제 일반/`-O` 38/38 PASS, 독립 PDF 700/700도 PASS. 과거 실패 로그는 분류해 보존한다. R6/C9 distinct-author NOT_RUN, physical_Q/owner_ACK NULL, production NOT_ISSUED, no main/foreign repo edits.
