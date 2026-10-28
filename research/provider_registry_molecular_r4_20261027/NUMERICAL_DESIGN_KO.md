# R4 수치 설계와 구현 계약

## 계산 경로

원본 `MOLECULAR_SOURCE_PACKET.json`의 SHA를 고정한다. Native decimal 문자열과 scale은 `Fraction`으로 보존한다. 상태 표지는 원문의 aggregate·미지정·열적 혼합을 서로 다른 identity로 만든다. H1/D2/Li7과 nuclear ground는 명시적 정수 투영 convention이며 원문의 isotope 미명시까지 해소하지 않는다. 여섯 새 source variant만 기존 R1 adapter와 unchanged finite compiler로 컴파일한다. 기존149열과249검사 결과를 다시 계산하지 않는다.

두 출판 fit은 Bennett27개, GL2022 두 개의 원문 온도점에서만 평가한다. 이 표본 노드 제한은 GL2022의 계산범위5–3000K를 자동 fit 유효범위로 해석하지 않기 위한 현재 단위의 계약이다. 내부 계산은 Python binary64이며, 원문에 없는 interpolation·extrapolation은 제공하지 않는다. Bovino의 `aT exp(-bT)`는 인쇄된 b 단위가 지수 차원과 맞지 않아 이번 평가에 포함하지 않는다.

## 실제 오차와 검증 기준

원문 표 값 k_table과 출판 식 값 k_fit의 상대 잔차는 `(k_fit-k_table)/k_table`로 기록한다. Printed precision, fit residual, 계산 모델오차, physical uncertainty는 별도다. 원문의 'about5%' 또는 'up to20%'를 엄밀한 보장으로 바꾸거나 관측 잔차에 맞춰 바꾸지 않는다. GL2022의 후속 논문 fit 평가도 원 SQM point error와 구별한다.

새 구현의 반올림 오차는 독립 검토자가 작성한80자리 계산식으로29점만 비교한다. 고정 수용 기준은 상대차 `2e-14` 이하이며, 이는 native formula 구현 검사에만 적용한다. 과거 HH/PHYS91/핵반응의 정확도 목표에는 영향이 없다. 소스 표 값과 식의 차이가 크면 그 차이를 결과로 보존한다.

정수·유리수 보존량과 state-lift defect는 exact rational로 계산한다. 조건부 모델의 작은 예제는 source measurement로 표시하지 않는다. 검증은 (1)6새열의 각 isotope/charge/electron-lepton 불변량, (2)thermal particle change, (3)원표 literal 유지, (4)방법 대안·spin 중복·unknown state·온도·Q의 fail-closed 경계, (5)state-lift exact identity와 half-spread bound를 포함한다. 전체 회귀 suite 및 이전 완료 과학 결과는 재실행하지 않는다.

## 실행·그림

1. 새6열·29fit sample·rational examples를 한 primary build에서 만든다.
2. 의미 있는 변경 검증만 수행하고 실패가 있으면 첫 로그를 보존한다.
3. 독립 checker가 원 source literal과80자리 식으로 결과를 검사한다. 작성자 코드를 참조값으로 import하지 않는다.
4. 저장된 결과만 읽어 원표/fit와 상대 잔차를 그림으로 만든다. 그림 생성은 fit을 다시 평가하지 않는다.

각 child는30CPU초·120wall초·512MiB·단일worker/thread로 제한한다. Archive, network, source recovery와 계수 계산 비용을 구별한다. PHYS91 잔여0과 역사 global 비용null은 유지한다. One new Wolfram symbolic request는 matrix invariants와 lift identity만 확인하며 실제 공급자 rate·Q를 계산하지 않는다.

## 실제 소비자에 남기는 계약

현재 API의 source sample 반환은 `SOURCE_FORMULA_SAMPLE`이다. Native 식을 계산한 사실만으로 physical rate를 요청하면 거절한다. Positive lift를 실제로 쓰려면 동일 상태집합의 d, pi 및 population을 공급해야 한다. Bennett 생성 aggregate와 Bovino 파괴 aggregate를 동일 상태라고 합치지 않는다. 핵Q·분자 state Q·최종 cascade photon yield는 현재 source packet의 미결정 상태를 유지한다.
