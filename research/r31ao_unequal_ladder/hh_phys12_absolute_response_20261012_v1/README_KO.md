# HH PHYS12 시작점

이 패키지는 WU088_HH의 고정 소스 계열에서 미래 HH ON/OFF에 따른 이온화
분율과 열에너지의 유한 차이를 계산한다. 신규 원 source/root solve 없이
보존된 균일 미분 포함에 FTC를 적용했다.

1. `REPORT_KO.md`: 결과·표·그림·물리적 해석.
2. `review/DECISION.json`: 독립 최종 판정과 그 조건.
3. `theory/FINITE_HH_RESPONSE_KO.md`: 정의·전제·유도·단위·반례.
4. `results/absolute_v1/ABSOLUTE_RESULTS.json`: exact rational 끝점.
5. `results/absolute_v1/OBSERVABLES.csv`: 외향 십진 수치표.
6. `evidence/absolute_v1/EXECUTION.json`: 실제 1회 실행의 비용·exit.
7. `state/RESEARCH_STATE.json`, `NEXT_DAG.json`: 완료와 미완료의 구분.
8. `NCP_TASKS.json`, `handoff/NCP_LOCAL_CODEX_HANDOFF_KO.md`: 현재 heavy job 없음.

원 PHYS11 source-inclusion/C² 전제는 유지한다. actual native나 전구간
history 인증으로 읽지 않는다. 기존 입력은 inputs/의 보존 파일이며 source
SHA256 및 parent Git blob 대응은 `inputs/SOURCE_MANIFEST.json`과
`evidence/PARENT_GIT_BINDING.json`에 있다.

Python 표준 라이브러리로 독립 재현할 경우 새 경로를 사용한다.

```bash
python3 code/analyze_absolute_hh.py --out results/independent_reproduction
```

이미 완료한 결과의 자동 재실행은 필요하지 않다. 그림 재생성에만
Matplotlib이 필요하다. NCP는 현재 `NO_HEAVY_JOB_READY`다.
