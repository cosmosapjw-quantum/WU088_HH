# WU088_HH R28 | 새로운 원본 비반응 HD 산란률 1560셀과 상태별 3경쟁 사건 수치

**기준:** WU R27 PR166 HEAD `0505e978b31f976015d7ed8d12c4a5dc4fe42989`; GL2022 JCP157 214302 (DOI 10.1063/5.0128598), 원본 SI `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`. REC HD J1..8 source PR161/162는 외부 소유의 read-only 참고. 현재 새로운 native PES 계산·실험은 수행하지 않았으며, **원저자가 계산한 실제 물리 rate 데이터를 추가 획득하여 직접 분류·재결합하는 범위**이다.

## 새로운 원본 물리 데이터
- 정확한 실물 source Tables12–28의 17개 표, **156행 × 10T = 1560셀** 두 텍스트 추출 방식 전수 일치. 원시 `(v,J,v',J',T,token)` 1560개, JSON과 CSV 생성. 1548개 구문 유효, 1개 원문 지수 outlier, 1개 괄호가 누락된 토큰, 대각 self-state 10개는 물리적인 inelastic loss에서 제외.
- 원본 Tables1–10 반응성 700셀은 R26 원본 그대로 참조하며 새 데이터를 혼합 수정하지 않는다. 자발복사 계수는 REC161의 2021 LAMDA 가시 텍스트 source transcription이며 raw 2289B 이 스레드에서 다시 취득한 것 아님.
- J=1..6 초기 HD 상태의 `J' < J` 로 내려가는 **210개 원본 수치**를 소스별 `K_down(J,T)` [cm3/s]로 합산. 60개의 J/T 지점 중 43개만 모든 세 위험률 source-valid, 나머지 17개는 NULL. source table J5 원시 표들에 중복이 있다는 이전 R26 경고 유지.

## 새로운 물리 현상: 이온 교환이 복사보다 빠른 것과 첫 사건 확률 50%는 다르다

R27에서 단일 복사 vs 교환 경계 `p0=A/Kex`는 두 위험률만 있을 때 50%를 뜻했다. 그러나 동일 초기 HD 분자가 proton inelastic rotational de-excitation을 겪을 수 있으므로 `Pex(p0)=Kex/(2Kex+Kdown)<1/2`로 수정된다. 이는 같은 초기상태, 고정온도, 고정 밀도에서 세 독립 Poisson clocks라는 모형하의 직접 유도다. 기존 R27 수치는 삭제하지 않고 **완결성의 다른 수준**으로 보존된다.

| 초기 J | 105 K K_exchange (cm3/s) | 105 K K_down (cm3/s) | 105 K P_exchange at R27 p0 |
| ---: | ---: | ---: | ---: |
| 1 | 1.3601095017625e-11 | 6.01e-10 | 0.02165082394 |
| 2 | 1.3046167002122517e-10 | 1.143e-9 | 0.09292649128 |
| 3 | 3.7524831950e-10 | 1.222e-9 | 0.19024028335 |
| 4 | 4.16947650006e-10 | 1.3753e-9 | 0.18873281597 |
| 5 | NULL source suspect | NULL admission | NULL |
| 6 | 5.53625327518e-10 | 1.6457e-9 | 0.20110252485 |

**새로운 온도 경향:** 3-경쟁 모형에서 `P_exchange`를 최초 사건의 50% 이상으로 만들 수 있는 조건은 `K_exchange>K_down`; R28의 조건부 source-grid 43행 중 **12행**(J1: 1005/2005/2505/3005 K, J2: 1505/2005/2505/3005 K, J3: 2005/3005 K, J4: 2505/3005 K)에서 존재한다. 고밀도 한계에서는 그 확률 상한이 `K_exchange/(K_exchange+K_down)`으로 수렴한다. J6의 모든 소스 수용 T에서는 이 모형의 50% 첫 사건 밀도가 없다. 이 분류는 저자 원본 표의 **인쇄된 온도 노드에 국한**되며 온도 간 보간·관측 검증이나 실제 cosmic abundance 가능성을 주장하지 않는다.

## source/단위/수치 검증

- `pdftotext -layout`와 PyMuPDF source PDF 두 독립 추출이 정확히 1560/1560 일치 (같은 원본에 대한 독립 텍스트 엔진; 원저자 독립 실험 아님).
- 소스 ID 게이트: 원본 PDF의 SHA-256/size, R27 state table SHA-256. 훼손된 원본과 잘못된 데이터 전달에 대한 음성 테스트.
- Python unittest 15/15 일반 및 `python -O` 15/15 PASS; `compileall` PASS. 최초 테스트에서 80자리 연산을 28자리 기본 Decimal 컨텍스트에서 재계산해 1e-28 반올림 잔차가 생긴 **검증 harness 구현 오류**는 테스트의 컨텍스트를 90자리로 고쳐 판정했고 원본 물리량, tolerance 1e-70은 변경하지 않았다.
- 별도 ratio-form mpmath 90자리 재구성 43행, 4종의 무차원 확률 대조 최대 상대 차이 약 5.24e-80 (같은 저자/동일 공개 데이터, 다른 계산식). Wolfram 물리적 항등식 3개 `{True,True,True}`. 중간 Wolfram 수치 테스트의 단위/스케일 전사 경고는 채택하지 않았고 마지막 기호 항등식만 인용.
- 출처는 computed SQM rate, 해당 rate의 관측 오차분포·PES-native threshold·native sigma(E) 제공 없음. `physical_Q`·reverse·bath를 만들어내지 않았다.

## DAG와 격리

실제 source-qualified 신규 자료와 과학적 물리 결과는 **R28 보조 1/1**. 그러나 R18의 34/49 canonical DAG에 추가하려면 원래 49 객체 무변경, 명시적 새 노드 수용, distinct-author R6/C9 등 근거가 필요하다. 본 실행에서 다른 저자의 R6/C9는 NOT_RUN; 원본 PES/Q와 분자반응 owner ACK는 미확보. 따라서 **중앙 DAG 34/49 유지, +0**이 과학적으로 타당하다. R28 scoped 1/1과 canonical DAG 혼동 금지. GL2022 보충자료에 원래 실려 있던 수치들을 새롭게 찾았다는 점은 진정한 데이터 진전이다.

후속작업: (1) 원본 Velilla2008 EPAPS `E-JCPSA6-129-612834` Fortran 및 isotope-specific energy-zero, (2) GL2022 또는 EQM source-native energy-resolved σ(E), (3) 2022 main Eq5 J0..8 vs SI Table11 J0..6, (4) 전자기 radiation과 상향 충돌을 함께 포함하는 **source-closed** master equation, (5) 명명된 REC/CR 분자 owner의 explicit ACK, (6) 실제 다른 저자 R6/C9. H+ + HD 비반응 inelastic를 D+ + H2 reactive 생성으로 중복 계수하지 않는다.