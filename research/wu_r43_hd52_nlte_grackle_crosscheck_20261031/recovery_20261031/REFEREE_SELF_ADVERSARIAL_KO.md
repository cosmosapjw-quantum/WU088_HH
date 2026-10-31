# R43 동일 저자 적대적 검증 (별도 저자 R6/C9 아님)

1. **SSOT 분리.** EMAA RADEX는 실제 52 준위 H–HD 충돌과 방사 원본이다. Grackle fit은 실제 구현된 widely-used benchmark이나 EMAA의 미측정 충돌값을 보완하는 물리적 closure가 아니다. 두 원전의 비LTE vs fit 비교값에서 차이가 나타나도 그 자체로 상대 오류를 주장하지 않는다.
2. **온도 경계.** H collision 15 T, proton 25 T이며 공통 원전 노드는 5 K뿐이다. Joint collision은 5 K에서만 허용했다. 70 K nHplus=0은 proton 자료를 70K로 보간해서 쓰지 않았음을 의미한다.
3. **에너지 검증.** 광자 선별 signed sum과 충돌 generator 공급을 별도 계산했다. 거의 평형에서는 net-flux를 분모로 삼는 relative residual이 발산하므로, 실제 gross emitted+absorbed energy에 대해 정규화한다. 이전 최초 27-test 중 test_25가 실패한 사실은 runtime 로그에 보존; 물리 입력을 바꾸지 않고 diagnostic을 교정한 후 27/27 통과했다.
4. **양자·화학 경계.** 52준위 유한 상태 비LTE, optically thin, 외부 흑체 고정. 52보다 높은 준위, H+19 밖, 비국소 복사전달, 주어진 기체의 시간진화와 HD abundance는 고려되지 않아 cosmic full cooling을 주장할 수 없다.
5. **확률과 포지티비티.** K column sums 0, normalized steady p≥0, ∑p≈1; 이 데이터와 고정 T,density 전 범위에서 음수점유율·상태 합·에너지 대수 오류를 검증한다. 무차원 normalized stationarity, gross energy normalized residual을 사용한다.
6. **두 원전 비교.** Grackle low fit은 erg cm³/s per HD–H density product. EMAA nH=1 cm⁻³ 조건의 erg/s per HD와 비교해야 rate coefficient ratio가 된다. LTE fit은 Boltzmann level + spontaneous Einstein A의 source-derived emission과 비교한다. LTE fit의 Grackle 온도 clamp T≥10K 때문에 5K의 수치는 서로 다른 경계다.
7. **원본 R43 복원 범위.** 이전 R43 master SHA256 58c4c095... 및 bundle SHA 774dbbc9...는 이전 archive byte identities다. 현재 복원본은 별도 ZIP, 별도 SHA, 별도 explicit grid이며 기존 PR #182를 덮어쓰지 않는다. 과거 236 cooling/88 heating 기록과 복원 224/100은 unresolved grid provenance discrepancy로 표시한다.
8. **독립성.** mpmath80은 같은 소스수치에 대한 독립 선형대수 경로, Wolfram 정확 2 준위는 식의 검산. 실제 distinct-author R6/C9은 모두 NOT_RUN.
