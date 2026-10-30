# WU R32 실행 보고서: H⁺ 충돌에 의한 HD(v=1) 첫 진동 소멸

**실제 신규 과학 산출물**: GL2022 원본 2022 supplementary 인쇄 SQM rate 890개(v=1 초기) 중 결손 `T=2005K, (1,2)→(0,5)` 토큰 `1.58(10`을 수선 없이 보류했다. 남는 9개 출처 온도에서 **801개 실제 원본 source rate**, 이 중 진동 소멸 612 및 진동 내 하향 회전 189를 사용했다. 역사판 CDMS 2011 v2 웹 표시 rotational/vibrational 준위로 상향 회전 189개를 상세평형으로 유도했다. 원본 `.egy` raw bytes 및 SPFIT covariance는 획득하지 않았다.

2가지 조건부 모드(`DB_UPWARD_V1`, `DOWN_ONLY_COUNTERFACTUAL`) ×9 온도×7 초기 HD J의 **126개 실제 계산 사례**, **1386개 최종 v=0 J'=0..10 제한적 분기**와 **3969개 v=1 내부 회전 edge 기대횟수/열에너지**를 생성했다.

- **105 K, 초기 v1 J0, detailed-balance**: 유효 진동 소멸 충돌계수 `1.449128031791665e-9 cm3/s`, mean fluence `690070151.195423 cm-3 s`, 충돌 bath gain `4.0130045803742274e-20 J = 0.25047204504258347 eV`, 기대 v1 rotational transition 수 `0.01653382150590601`; 최종 제한 분기의 상위 J'는 8(0.182530), 7(0.169429), 6(0.153581), 5(0.135664).
- **3005 K, 동일 초기 v1 J0**: `DB_UPWARD_V1`에서 k_eff `1.1145781115653034e-9 cm3/s`; downward-only counterfactual에서 `1.1624e-9 cm3/s`. 동일 온도 원천을 쓰더라도 상향 상세평형 closure가 모델에서 기대 first-passage fluence를 바꾼다는 조건부 결과다. 이것은 양자 산란 불확실성 신뢰구간이 아니다.

검증: Python unittest `14/14` 정상 및 `14/14 python -O`, compileall; 본인 작성 별도 `mpmath 85 dps` 알고리즘은 126 사례×14 비교=**1764/1764** scalar/branch 비교, 최대 scaled delta `4.785338306447596e-16`, 최대 분기 절대차 `8.987856437392545e-17`. 126개 모델의 최대 원자별 에너지 수지 잔차 `4.81482486096809e-35 J`; 흡수확률 합은 1. 사용한 모든 셀의 SHA/출처 문서와 재현 가능한 코드를 포함했다.

**해석의 한계**: 이 계산은 충돌만으로 처음 v=0 상태에 도달하는 conditional first-passage 모델이다. 실제 v1 Einstein A, reactive sink, 주변 H/H₂/He collisions, 자기일관된 n(H+)와 T evolution, v0 reverse, chemical reaction Q는 미포함이다. `EMAA HD-H+ raw171x25=NOT_ACQUIRED`, `PES_NATIVE_THRESHOLD=NULL`, `PHYSICAL_Q=NULL`, `OWNER_ACK=NOT_OBTAINED`, `R6/C9_DISTINCT_AUTHOR=NOT_RUN`, `HH_R10=OFF`, `FULL_A=NULL`, `L4=false`, `PRODUCTION=NOT_ISSUED` 유지. 정본 WU DAG `34/49` 변화 없고 R32 auxiliary `1/1 scoped` 신규 한 단위만 성립한다.

다음 안전 행동: 원본 EMAA 171×25 RADEX ASCII를 확보하여 상태/온도/단위 대응 및 GL2022 independence 없이 계수 비교. 없으면 v1 radiative Einstein A와 source-native reactive rates 원자료를 더 찾아 첫 통과 모델의 sink 누락을 실제 물리적으로 해소한다. 이후 원전 신원 검증과 명시적 chemistry owner ACK 및 distinct-author R6/C9를 수행하기 전에는 canonical DAG 승격/생산 반영 금지.
