# R17A 비저자 C9 검토와 영총율 경계 교정

검토 대상은 WU088_HH의 불변 commit `d08683a50a57c7bebc8a871e0021c2f8b5520fa9` 아래 R17A다. 별도 agent가 11개 Git blob의 원본 바이트를 확인했고, 저장 결과에 대해 12개 독립 산술·경계·API 검사를 0.003902 CPU초에 수행했다. 기존 primary/reference suite와 ODE는 재실행하지 않았다.

출판 SQM 총율, 실험 중심·인쇄 오차폭, SI 환산, 차이 11/100·51/100 및 halfwidth 비율 11/20·51/20, 저자의 전온도 적합과 두 인쇄점을 지나는 지수식의 구별은 검토 범위에서 유지된다. Halfwidth는 논문에 인쇄된 폭이라는 의미만 사용한다. 확률·표준편차·개별 상태율·consumer 채택은 발급하지 않는다.

논문의 본문은 AIP 원 연구논문의 검색 인덱스 원문과 동일 DOI의 저자 원문 사본으로 대조했다. 직접 publisher PDF 조회는 현재 403이었고, supplement 원본 바이트·SHA를 확보했다는 주장은 없다. 정확한 조회 범위와 결과는 C9_REVIEW.json에 연결했다.

유일한 P2 지적은 일반 non-identification 명제의 K=0 경계다. 저장된 양의 두 총율에는 영향이 없으나, 일반 명제는 다음과 같이 고친다.

가중치 w_i≥0, 비음수 r_i, K=Σ_i w_i r_i에 대해 목표 a의 가중치가 양수이면 0≤r_a≤K/w_a다. **K>0**이고 a와 다른 b의 가중치도 양수이면 두 벡터 (K/w_a)e_a 및 (K/w_b)e_b가 같은 양의 총율과 서로 다른 목표율을 갖는다. **K=0**이면 각 비음수 항의 합이 0이므로 w_i>0인 모든 i에 대해 r_i=0이다. w_i=0인 좌표만 총율에 의해 제한되지 않는다. 따라서 양의 가중치를 갖는 목표율은 영총율에서 정확히 0으로 결정된다.

P3 지적은 내부 helper에 독립 obj·raw_bytes를 줄 수 있는 API 형태다. 지원된 read_evaluate/CLI 경로는 같은 바이트에서 obj와 SHA를 만들므로 현재 저장 결과는 영향을 받지 않는다. 이 경로의 transcription SHA도 재대조해 일치했다.

검토 판정은 **F01 교정 addendum을 통합한 범위에서 PASS_SCOPED**다. 원본의 일반 명제를 교정 없이 그대로 통과시킨 판정은 아니다. 이 검토로 WU 과학 DAG 33/48이나 HH_R10=OFF 및 production=NOT_ISSUED, L4=false를 변경하지 않는다.
