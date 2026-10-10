# 경량 재현

Python 3.10+ 및 동봉한 requirements.txt의 SymPy/mpmath를 사용한다. 이번 관측 version은 ENVIRONMENT.json에 있다. 전체 Rust/NCP/기존 이력은 실행하지 않는다.

봉인 ZIP을 새 폴더에 푼 뒤 패키지 root에서:

```bash
python -B reproduce.py --verify-only
python -B reproduce.py --output /absolute/path/to/NEW_PHYS01_OUTPUT
```

출력은 원 패키지 밖의 새 디렉터리여야 한다. 다섯 명령은 12 unit tests, 47 일반 symbolic identities, 9 별도 series/EOS identities, 8 causal kernel identities, 25개 90자리 단일 상태 계수 검사를 수행한다. 새 결과 JSON4개를 봉인 결과와 byte 대조한다. 계산된 source-state는 하나이며 고유 native 물리계산/근/시간이력 수는0이다. 재현 횟수를 독립 물리 사례로 합산하지 않는다.

실패를 보존한 파일: logs/unit_RED.stderr는 예상한 behavioral red다. failures/analyze_initial.stderr는 Fraction→mp.mpf 변환의 TypeError이며 물리식 실패가 아니다. 분석 계산을 먼저 마치고 결과를 create-only로 쓰도록 수정했다. 원 빈 실패 JSON과 코드도 남아 있다.
