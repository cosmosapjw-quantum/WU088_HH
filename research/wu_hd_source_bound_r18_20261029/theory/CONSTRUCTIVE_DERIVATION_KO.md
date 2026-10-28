# R5 構成・유도와 source admission의 범위

1. Table2의 양의 인쇄 mantissa를 A/10^d로 해독한다. 지수표기 x는 원문 caption에 따라
   음의 지수 −x다. 정수 거듭제곱 연산으로 A/10^(d+x)를 얻으므로 부동소수점 절단이 없다.
2. 1 cm=10^(−2)m이므로 1 cm³=10^(−6)m³다. 따라서 SI 값은 정확히
   A/10^(d+x+6)이다. 초는 같은 단위다.
3. 선택 첫 셀 3.99(14)는 399/10^16 cm³/s=399/10^22 m³/s다.
   마지막 셀 2.08(10)는 13/62500000000 cm³/s=13/62500000000000000 m³/s다.
4. 10개의 유리수는 raw SQM state-to-state 출력이다. 유한 열평균 연산을 할 경우에만
   별도 p_2(T)와 홀수 spin s_1=3/4를 곱한다. raw data에 대한 double spin weighting을 하지 않는다.
5. ν=(−1,−1,1,1)에 대한 H·D 핵수 및 전하 row의 내적을 0으로 직접 계산한다.
   이는 화학양론 보존이며 실측 rate의 정확성이나 에너지 Q의 인증과 구별된다.
6. Source node는 원본 identity, 선택된 channel/10 cells의 독립 판독, 구현의 정확한 해독으로 닫는다.
   소비자의 동역학은 density/state/clock/energy/full-A 의존성이 별도로 충족된 뒤 연결한다.

이 결과는 데이터 해독·정규화·보존의 구성이다. 새 strong no-go를 주장하지 않는다.
R17A의 일반 비식별성 명제는 K>0에서 두 witness가 다르다.
K=0과 양의 가중치에서는 모든 비음수 상태율이 0이며, 정확한 교정은
reviews/r17a/K_ZERO_LEMMA_CORRECTION_KO.md에 있다. 이 교정이 source 총율 두 양수 계산을 바꾸지 않는다.

