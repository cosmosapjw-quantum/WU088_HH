# WU088_HH R18 native SQM source 독립 검토

**판정: PASS_SCOPED_NATIVE_PRINTED_TARGET_ROW.** 다른 작성 주체 `/root/r17b_independent_review`가 작성자 extraction JSON을 읽기 전에 원 PDF를 독립적으로 `pdftotext -layout`으로 해독하고 5·6쪽을 렌더링해 읽었다. 선택된 **H+ + HD(v=0,j=2) → D+ + H2(v'=0,j'=1)** 행의 10개 printed rate와 온도 열을 확인했다.

원본은 [DIGITAL.CSIC author deposit](https://digital.csic.es/handle/10261/305186)의 [supplement PDF](https://digital.csic.es/bitstream/10261/305186/2/h_hd_rate_supplementary_material.pdf)다. 로컬 파일은 273,554bytes, 14쪽, SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`와 일치한다. institutional record의 제목·저자와 PDF 표지가 원 논문 DOI `10.1063/5.0128598`의 연구에 대응한다. publisher endpoint 원본과의 byte identity는 이 검토에서 확인하지 않았다.

## 선택 행: 인쇄 6쪽, Table2, (v,j)=(0,2), 세 번째 data row

각 토큰의 괄호 정수 x는 음의 십진 지수다. `3.99(14)`는 **3.99×10^-14 cm³/s**이고 불확실성 표기가 아니다. SI 변환은 cm³/s 값에 10^-6을 곱한다.

| T [K] | Source token | Printed rate [cm³/s] |
|---:|---:|---:|
| 15 | 3.99(14) | 3.99×10^-14 |
| 55 | 2.92(11) | 2.92×10^-11 |
| 105 | 1.15(10) | 1.15×10^-10 |
| 255 | 2.74(10) | 2.74×10^-10 |
| 505 | 3.33(10) | 3.33×10^-10 |
| 1005 | 3.18(10) | 3.18×10^-10 |
| 1505 | 2.85(10) | 2.85×10^-10 |
| 2005 | 2.55(10) | 2.55×10^-10 |
| 2505 | 2.30(10) | 2.30×10^-10 |
| 3005 | 2.08(10) | 2.08×10^-10 |

이는 10개의 이산 온도점이다. 실제 표에 15·3005 K가 있으므로 이를 article의 일반적인 5–3000 K 서술에 맞추어 5·3000 K로 바꾸면 source 오류가 된다. 연속 온도 함수, interpolation 또는 extrapolation은 이 표에서 채택하지 않는다.

## Spin 및 source 범위

Table2는 raw state-to-state SQM rate k_02,01이다. 원 논문 Eqs.(5)–(7)의 thermal operator에서 해당 홀수 최종 rotational state의 계수 3/4를 **한 번** 적용하며, 초기 HD Boltzmann 확률 p_2(T)를 별도로 곱한다. 이 spin 계수를 raw table 자체에 이미 포함된 것으로 보거나 3/4를 두 번 곱하지 않는다. 실제 nonthermal consumer의 population·nuclear-spin convention은 consumer 계약에서 추가로 결속해야 한다.

Source에서 직접 관측한 범위 차이가 있다. Supplement §3의 5쪽은 reactive tables1–10의 초기 HD j=0..6을 명시하고 thermal Table11에 대해서도 j≤6이라고 쓴다. 실제 10개 reactive table 각각에서 일곱 initial row (0,0)..(0,6)만 확인했다. 반면 main article Eq.(5)는 j≤8을 사용하며 Table11 caption은 이 main equation을 참조한다. 이 차이는 **UNRESOLVED_SOURCE_SCOPE_DIFFERENCE**로 유지한다. 누락 j=7,8은 MISSING_NOT_ZERO이고, Table11을 main article의 j≤8 thermal total과 동일하다고 선언할 근거는 이 검토에서 없다. 선택된 j=2 행의 transcription 수용에는 이 차이가 영향을 주지 않는다.

Printed decimal의 exact rational decoding은 source 문자열의 의미를 보존한다. 그것만으로 실제 SQM 계산값이나 물리적 rate의 엄밀한 uncertainty interval이 얻어지지는 않는다. 이번 source는 reactive SQM이며 nonreactive HD→HD 또는 TIQM/EQM로 바꾸지 않는다.

## 재현 근거

`independent_extract.py`는 원 PDF만 입력받고 target row를 독립 visual transcription 10개와 비교한다. 14쪽·byte hash·size, 모든 reactive table의 initial row coverage 10개, selected row 10개가 실제 실행 exit0으로 확인되었다. `INDEPENDENT_SOURCE_REVIEW.json`에는 cell별 page/table/row/column, raw token, exact cm³/s·SI rational decoding, spin 적용 및 scope discrepancy를 보존했다.

원래 suite 재실행이나 physical ODE는 수행하지 않았다. 이 결과는 source transcription·convention에 대한 독립 검토다. R18 구현의 distinct-author code review는 해당 frozen module/diff를 읽고 independent source oracle과 비교한 뒤 별도로 판정한다. Density·clock·full-A 및 whole-domain physical consumer 인증은 미발급이며 `HH_R10=OFF`, `production=NOT_ISSUED`, `L4=false`를 유지한다.
