# WU088_HH R20 연구 결과 | 2026-10-29

**질문:** R19의 105 K 한 점 반응 정확 해를 GL2022 원본의 **이산 온도 격자**에서 외부 지정 비자율 온도·부피 경로로 확장하고, 실제 CR `proper_dt` clock 인터페이스와 연결 가능한 부분을 확인할 수 있는가?

**결과:** 한 채널의 comoving 질량작용 벡터장은 `α(t)F` 꼴이므로 서로 교환한다. `A=∫ k(T)/v dt`를 먼저 계산하면 온도 점프와 균질 팽창·수축을 포함한 4종 반응 해는 `Φ_A` 하나로 정확하게 표현된다. 각 구간의 `k_i`는 원본 PDF에서 검증된 `NativeGrid.lookup(T_i)`만 사용하고, 외부 열분포·핵스핀을 중복 적용하지 않는다. `T_i`는 **10개 원문 격자점만** 허용한다.

**예시:** 합성 초기 `H+=HD02=10^6 m^-3`, 생성물0, `v=1`, `105 K` 5×10⁹ s 후 `255 K` 5×10⁹ s. 원문 `k_105=1.15×10^-16 m³/s`, `k_255=2.74×10^-16 m³/s`. 총 exposure `1.945×10^-6 m³`, 최종 반응물 각각 `339558.5738539898 m^-3`, 생성물 각각 `660441.4261460102 m^-3`. 이 값은 실제 우주론적 온도·밀도 이력이 아니다.

**검증:** `pytest` **25/25**, Wolfram 9/9 exact, 별도 mpmath 80자리 survivor-ratio 160/160 (최대 abs `5.960464477539063e-08 m^-3`, 최대 relative-floor-1 `3.051806267813985e-14`), SciPy DOP853 2/8/24/48구간 4/4 (최대 abs `4.307366907596588e-09 m^-3`). 독립 *알고리즘*은 수행했으나 독립 *저자* R6/C9는 NOT_RUN. CLI exclusive-create·변조 원본·격자 외 온도·state/source label forging 등 부정 검사 포함. 초기 테스트의 source PDF 경로 오류, 독립 reference 스크립트의 `__future__` import 위치 오류, source-label 생성자 위조 위험을 발견·교정했으며 최종 명령은 다시 실행했다.

**수치 정확도·속도:** source PDF 파싱을 양쪽에서 제외하고 같은 입력·허용오차로 측정한 로컬 Python wall 비율 DOP853/exact는 2,8,24,48 구간에서 `results/NUMERICAL_BENCHMARK.json`의 실제 값으로 약 **139,203,219,215배**. DOP853 `rtol=2e-12,atol=1e-7 m^-3`. 이는 작은 단일 채널의 조건부 비교로, 전체 Einstein–Boltzmann solver 속도 향상을 주장하지 않는다.

**실제 owner 조사:** REC PR155 `HDDataset.downward_rate`는 LAMDA 비반응성 HD 50/100/200 K로 source-grid와 불일치. CR PR120 `proper_dt(model,a0,a1,q)`는 Hubble clock의 GL2 적분이며, R20은 그 **수식과 호출 시그니처를 독립 재현**한다. 실제 CR owner module/model/state를 실행·결속한 것은 아니다. 올바른 source-grid 노출은 `k∫ d ln a/(Hv)`이므로 `k Δt/v_mid`와 일반적으로 다르다. 합성 H constant, v∝a³에서 GL2 노출 오차 `0.00379545`, GL8 `1.059e-15` 상대. 이 수치는 전역 오차 인증이 아니다.

**원전:** González-Lezana et al., *JCP* **157**, 214302 (2022), DOI [10.1063/5.0128598](https://doi.org/10.1063/5.0128598); 기관 원본 [DIGITAL.CSIC](https://digital.csic.es/handle/10261/305186), PDF SHA-256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`. R18 source 10개 값은 보존했고 원본 rate의 물리적 오차모형은 없음.

**Claim gate:** WU 정식 DAG **34/49 불변**, R20 보조 연구 workflow **18/20** (R6/C9 비저자 심사 미실행), 실제 REC/CR 4종 HD chemistry owner ACK 없음, source true-rate uncertainty/Q-event/역반응/full-A 미해결. `HH_R10=OFF`, `production=NOT_ISSUED`, `L4=false`. 다른 repo mutation·main merge·기존 R16–R19 full suite 재실행 없음.

세부 유도는 `THEORY_KO.md`, source pin과 소비자 gap은 `authority/OWNER_INTERFACE_AUDIT.json`, 실행 기록과 단계별 Git/백업은 `delivery/`을 보라.
