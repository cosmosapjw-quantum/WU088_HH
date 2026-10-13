# PHYS19 재현 진입점

이미 완료된 결과는 checks/application/run01/results/CURVATURE_RESULTS.json,
checks/application/readout02/results/CURVATURE_GEOMETRY.json에 정확한 유리수 endpoint와 외향 decimal로 있다.
현재 판정은 review/DECISION.json, 독립 심사는 checks/independent/에서 확인한다.
파일 확인을 위해 원 source/root/history 계산을 다시 실행할 필요는 없다.

## 입력 복원

연구 묶음의 dependencies/WU088_HH_PHYS18_THEORY_20261013_RESEARCH_BUNDLE.zip에는
PHYS15–18 core 입력이 원 검증 묶음의 연속 archive로 들어 있다.
아래 명령은 새 디렉터리에 네 core만 복원하고 archive identity와 23개 계약 입력을 확인한다.
기존 디렉터리는 덮어쓰지 않는다.

~~~bash
python3 HH_PHYS19_THEORY_20261013_v1/src/restore_inputs.py \
  --archive dependencies/WU088_HH_PHYS18_THEORY_20261013_RESEARCH_BUNDLE.zip \
  --output restored_inputs
~~~

## 이번에 추가한 계산만 재현

다음은 선택적으로 같은 새 순수 곡률 계산을 재현하는 명령이다.
Python 표준 라이브러리만 사용하며 restored_inputs의 원 producer 산술과 읽기 함수를 재사용한다.
reproduction_run/results는 아직 존재하지 않는 경로로 지정한다.

~~~bash
python3 HH_PHYS19_THEORY_20261013_v1/src/curvature_application.py \
  --parent15 restored_inputs/HH_PHYS15_THEORY_20261012_v1 \
  --parent16 restored_inputs/HH_PHYS16_THEORY_20261013_v1 \
  --parent17 restored_inputs/HH_PHYS17_THEORY_20261013_v1 \
  --parent18 restored_inputs/HH_PHYS18_THEORY_20261013_v1 \
  --output reproduction_run/results

python3 HH_PHYS19_THEORY_20261013_v1/src/curvature_geometry.py \
  --source reproduction_run/results/CURVATURE_RESULTS.json \
  --mixed-source restored_inputs/HH_PHYS18_THEORY_20261013_v1/checks/application/run02/results/MIXED_RESPONSE_RESULTS.json \
  --output reproduction_readout/results
~~~

원 실행에서는 main wrapper 1.569 s, 최대 RSS 55,992 KiB,
geometry readout02 0.049 s였다.
재현 경과는 환경에 따라 달라진다.
재현 비교는 실행 시각·경로·runtime 필드보다 정확한 결과 endpoint와 입력 identity를 우선한다.
독립 검산은 자체 Fraction arithmetic을 사용하며 실행 전 기록과 실제 결과를 별도로 보존했다.

## Wolfram·xAct 및 보고서

checks/wolfram/pure_curvature_checks.wl와 hessian_geometry_checks.wl는
실제 연결된 Wolfram kernel에 제출한 소스다.
같은 디렉터리의 RUN*_REQUEST.json, RUN*_RESPONSE.json에 실제 요청·응답을 저장했다.
Wolfram 15.0.1, xTensor 1.3.0, xPerm 1.2.4를 사용했다.
현재 보존된 근거 확인에 새 Wolfram 호출은 필요하지 않다.

보고서 재조판은 report/에서 다음과 같이 수행한다.
TeX 소스에 맞춘 Noto CJK subset font가 포함되어 있다.

~~~bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error WU088_HH_PHYS19_THEORY_20261013.tex
~~~

그림은 report/build_figures.py가 저장된 interval 공식에서 생성한다.
matplotlib·numpy가 필요하며, 실제 물리 함수의 표본이나 추가 source 계산을 만들지 않는다.

## 다음 과학 실행

다음 단위의 첫 행동과 입력은
theory/HH_CONSUMER_SOURCE_RESPONSE_HANDOFF_KO.md,
contracts/NEXT_CONSUMER_CONTRACT.json에 있다.
실제 이름과 identity가 결박된 rei_bianchi 소비 구간 하나에 대해
HH의 K/s와 전자 생성률을 계산하는 목표다. 해당 소비 입력은 현재 미확인 상태로 기록했다.
