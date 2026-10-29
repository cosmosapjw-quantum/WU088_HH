# WU088_HH R19 연구 결과: source-bound 105 K 단일 반응의 정확한 해와 prescribed-volume clock

**상태:** `PASS_SCOPED_NOMINAL_EXACT_FLOW`; 과학 DAG **34/49 불변**, 별도 R19 이론/코딩 workflow **18/20** (`R6/C9` 진정한 비저자 독립심사 미실행). **물리/중앙 DAG 승격 0**, `HH_R10=OFF`, `production=NOT_ISSUED`, `L4=false`.

## 1. 원전과 상속된 입력

González-Lezana, Hily-Blant, Faure, *J. Chem. Phys.* **157**, 214302 (2022), DOI 10.1063/5.0128598. 기관 원본 supplementary Table 2, page 6, `HD(v=0,j=2)→H₂(v'=0,j'=1)` reactive SQM row의 105 K 토큰 `1.15(10)`을 사용했다. 원본 PDF SHA-256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`, R18 원본 코드 Git blob `be2a845263b215b604f255ffe5deabe55be9dd7b`가 이번 ZIP 및 Git parent에 존재하고 일치함을 확인했다. 이 source 값은 `1.15e-16 m³/s`이며 **인쇄 소수의 정확한 해독**만 보장한다. Source 물리 오차/true-rate enclosure는 미제공이다.

최신 관련 repo/PR 확인: WU #155, REC #154, REI #260, BASS #239, BASS_HE #103, bass_cr #119, vigilode #102. 이들 중 105 K의 동일 state-order, density, clock, energy를 명시적으로 채택한 REC/CR 실제 소비자는 이번 조회에서 확인되지 않았다. R18의 전체 2476 branch census와 source extraction 19/19, independent 10/10, Wolfram 15/15, nonauthor 53 checks는 identity가 같으므로 재실행하지 않았다.

## 2. 구성적 유도와 구현

상태 \(\boldsymbol n=(n_{H^+},n_{HD02},n_{D^+},n_{H201})\)는 `m⁻³`, proper time `s`, 반응 \(\nu=(-1,-1,1,1)\), flux \(J=k n_1 n_2\)는 `m⁻³s⁻¹`. 보존 공변벡터 `H=(1,1,0,2)`, `D=(0,1,1,0)`, `q=(1,0,1,0)`는 독립이며 `w·ν=0`이다.

고정 부피에서 초기 반응물 \(a,b\)에 대해 `xi' = k(a-xi)(b-xi)`를 정확히 풀었다. `a=b=m`이면 `xi=m²kt/(1+mkt)`. `m=min(a,b), M=max(a,b), delta=M-m>0, z=-expm1(-k*delta*t)`이면 `xi=m*M*z/(delta+m*z)`; survivor는 각각 `m*delta*exp(-k delta t)/(delta+m*z)` 및 `M*delta/(delta+m*z)`로 직접 평가한다. 양성성·반응 extent 단조성·한계값을 증명했다.

외부 지정 \(\Theta(t)=d\log(V/V_0)/dt\)에 대해 `v=V/V0`, `N=v n`, `tau=int_0^t ds/v(s)`로 바꾸면 동일한 exact flow를 \(N(\tau)\)에 적용한다. `theta=constant`에서는 `v=exp(theta*t)`, `tau=-expm1(-theta*t)/theta`. 이 계산은 **실제 GR geometry를 풀지 않는** prescribed-volume 모델이다. 화학 Jacobian은 rank ≤1, 비영 고유값 `-g*k*(nH+nHD)`이며, 희석 포함 고유값은 `-g*theta`(3중)와 `-g*(theta+k*(nH+nHD))`다. `d xi/d k = tau*(a-xi)*(b-xi)`는 source 불확실성이 주어졌을 때만 조건부 민감도에 사용한다.

실제 state energy defect Q는 미제공이다. `ΔE_chem=-Q*xi`, `ΔE_bath=+Q*xi`는 **형식적 ledger**이며 `Q`를 임의로 물리 승인하지 않는다.

## 3. 실제 계산 결과

고정 부피·외부 고정 105 K bath·**합성 초기조건** `nH+=nHD=1e6 m⁻³`, 생성물0, `t=1e10 s`:

- `nH+=nHD=465116.27906976745 m⁻³`
- `nD+=nH2=534883.7209302326 m⁻³`
- 초기 flux 예제 `nH+=1e6`, `nHD=2e6`에서 `J(0)=2.3e-4 m⁻³s⁻¹`.

Prescribed expansion 예제 `n0=(1e6,2e6,2e5,3e5) m⁻³`, `t=1e10s`, `theta=1e-11s⁻¹`에서는 `v=1.1051709180756477`, `tau=9.5162581964e9s`, `xi=798978.7455331144 m⁻³` (per reference volume). 이 예제의 \(\Theta\)는 실제 관측/우주론 source가 아닌 선언된 synthetic parameter다.

## 4. 검증 및 실패 보존

- `python -m pytest`: **24/24 PASS**, 실제 source PDF 검증·정확 SI·T/state/method guard·양성성·H/D/charge·Jacobian finite differences·CLI exclusive-create·prescribed expansion·수치 IVP.
- Wolfram symbolic: **9/9 PASS**, `xi` ODE, `a=b` branch, 보존 covectors rank3, Jacobian eigenvalues, effective-clock derivative/zero-expansion. 최초 별도 symbolic limit 검산 10/10은 불필요한 `Infinity` 경고를 포함했으므로 경고 없는 두 번째 9/9를 현재 유효 검산으로 사용한다.
- `mpmath` **80자리 160/160** synthetic state/clock cases: 최대 상대 오차 **2.395748762895353e-14**, 최대 절대 오차 **5.457278056685938e-06 m⁻³**, frozen thresholds 각각 `3e-9`, `2e-5 m⁻³`. 독립 SciPy `DOP853` 3 IVP 케이스 최대 절대 차이 `1.3737007975578308e-08 m⁻³` (fixed 5e-5 gate).
- 별도 figure DOP853 dense-output vs exact flow: 최대 절대 차이 **3.243330866098404e-07 m⁻³** against `5e-5 m⁻³` gate; populations 및 residual PNG/SVG를 실제로 열어 축·단위·모형 표기 확인. 이 오차는 **수치해 차이**이며 물리 source uncertainty가 아니다.
- 최초 23/24 중 `test_22` 실패: CLI의 기존 파일 재작성에서 `FileExistsError`를 사용자 계약 오류로 번역하지 않았음. 원인 구현/오류 표시. `ModelContractError` 사전 검사와 원자적 `open('x')`의 race catch를 추가해 24/24 PASS. 수학적 반례는 아님.
- R6/C9 비저자 native subagent 도구는 현재 세션에 노출되지 않아 **NOT_RUN**. Wolfram, mpmath, SciPy는 독립 알고리즘이지 독립 저자 심사가 아니다. 따라서 workflow 18/20만 완료.

실제 실행환경 Python3.13.5, NumPy2.3.5, SciPy1.17.0, pytest9.0.2, mpmath1.3.0, Matplotlib3.10.8. `PYTHON_PASS`, g++ 존재(별도 C++ scientific suite 미실행). Local parent-process CPU는 child `pdftotext`/remote Wolfram 비용을 포함하지 않으므로 전체 누적 CPU로 보고하지 않는다. 새 local 계산예산은 90 CPU-s/180 wall-s, 역사 예산 이월0이다.

## 5. 판정 및 다음 실행

이번 R19은 실제 R18 원자료에 결속된 **source-nominal isolated 4-state model**을 완성했다. 이는 원래 49-node WU DAG의 이미 부분인 `WU_HD_REACTIVE_STATE_SOURCE_NEXT`를 실제 REC/CR owner에 연결한 것은 아니다. 기존 49개 DAG 노드를 변경하거나 완료 수를 늘리지 않았다: **34/49**. 별도 R19 auxiliary model은 구현·수치 검증이 되었으나 비저자 R6/C9와 owner consumer가 남았다.

다음 실제 과제: named REC/CR owner repo/path/function/commit, state-order·number density·proper-time/clock Jacobian·온도/에너지 convention·actual full-A/thermal state를 **owner ACK**로 고정하고, source 105K에 맞는 데이터가 있을 때만 같은 반응항을 결속한다. 현재 REC 50/100/200K와 REI300K는 원 source grid와 교집합0이며, REI17state는 HD/H₂를 포함하지 않는다. 원본 PDF의 물리 오차/역반응/상태 에너지 Q와 full network는 별도 source-gated 노드다.

**자료 위치**: GitHub 독립 R19 Draft PR 및 `research/wu_hd_nominal_exchange_r19_20261029/` 아래 THEORY_KO.md, SOURCE_CONTRACT.json, src/nominal_exchange.py, tests/, results/, figures/, HANDOFF_NEXT_THREAD_KO.md, delivery/. Drive 원본 stage ZIP과 Dropbox Paper **텍스트 영수증**을 구분한다. Dropbox 원본 ZIP 업로드 성공은 도구 경로가 확보되지 않으면 주장하지 않는다.
