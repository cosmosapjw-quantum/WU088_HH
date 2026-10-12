# WU088_HH PHYS14 보고서

`WU088_HH_PHYS14_20261012.tex`를 XeLaTeX로 두 번 컴파일하면 동봉된 9쪽 PDF를 재현할 수 있다. 작업 디렉터리는 이 README가 있는 디렉터리다.

```sh
xelatex -interaction=nonstopmode -halt-on-error WU088_HH_PHYS14_20261012.tex
xelatex -interaction=nonstopmode -halt-on-error WU088_HH_PHYS14_20261012.tex
```

표의 구간은 원 결과의 정확한 유리수 끝점에서 바깥쪽으로 반올림한 십진 표기다. 그림은 포함 구간을 나타내며 중앙값 추정치를 뜻하지 않는다. `fonts/`에는 필요한 한국어 글리프의 Noto Serif CJK KR 부분집합과 OFL 라이선스를 포함했다. 동봉된 표·그림·폰트로 컴파일할 때 과학 계산이나 그림 생성 프로그램을 실행할 필요가 없다.

전체 연구 스냅샷에서 정확한 계산 결과는 `../results/advance01/ADVANCE_RESULTS.json`, 독립 최종 판정은 `../review/DECISION.json`, 다음 DAG는 `../NEXT_DAG.json`이다. 원 실행 결과의 `CANDIDATE_COMPUTED`는 실행 당시의 상태이며, 후속 독립 판정 `PROMOTE_SCOPED`는 별도 파일에 기록했다. 보고서의 원문 근거 목록은 이 전체 스냅샷의 경로를 가리킨다.

수치 결과는 원 source inclusion 및 첫 단계의 근·C2 계열을 상속한 geometric isotropic source-aligned subfamily에 대한 결과다. 현재 half의 incoming, 분모, 잔차, 유일 근 및 미분을 새로 계산했다. 실제 Full 대 two-half endpoint 차이는 다음 연구 노드다.
