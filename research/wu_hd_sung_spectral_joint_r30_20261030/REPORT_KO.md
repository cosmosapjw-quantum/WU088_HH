# R30 수행 결과 보고서 (2026-10-30 KST)

연구 질문: 원본 GL2022 상태별 proton-HD SQM 반응률과 REC 소유 HD 복사율, 최신 Sung 2022/2023 측정 선 중심을 결합하면, **기존 R29이 출력하지 않았던 파장별 photon yield 및 photon-tagged H₂ 생성물 분기확률**을 실제 계산할 수 있는가?

**실제 실행:** `src/spectral.py` 계산 210 cases, 840 line-specific rows, 2100 H₂ product photon/no-photon joint probability rows. 2011 CDMS v2 energy ladder와 Sung 누적 fit energy ladder를 동일 original GL2022 source chemistry+downward rate로 독립 비교. Source rates와 Einstein A 변동 없음. 데이터는 실제 원문에서 전사된 **computed** SQM rate이며, 새 실험자료는 네 적합 line centers만 추가됨.

**성공:** 실행한 Python unittest 20/20 일반, 20/20 `python -O`, compileall, independent-method mpmath 75 digits 210/210, 840/840, 2100/2100, photon/reaction total-probability 210/210. mpmath vs float 최대 상대 차이 (5 selected aggregate metrics) 4.661576191501533e-14; 최대 photon-line 절댓값 차이 1.402509352354029e-12 (expected photons can be tens); 최대 H2 joint-probability 절댓값 차이 4.10757007206511e-14. Wolfram two-state symbolic test three identities `{True,True,True}` (same author symbolic, not distinct-author review).

**과학적 주의:** 부모 CDMS2011 인쇄 v0 J0…4 levels는 변경하지 않았다. 별도의 Sung measurement-fitting ladder를 명시적 대체 실험 가정으로 사용했다. fit 중심만 source-qualified, 원본 논문 PDF raw·공분산/전체 실험 uncertainty, H2 shift correction, EMAA original H+ data 미확보. 실험 측정 line centers를 7개 astrophysical 온도에서 '실험으로 측정한 충돌률'이라고 주장하지 않는다. 5 HD levels와 selected H2(v'=0) product만 포함하므로 radiation emitted per initial HD와 gas net cooling은 같지 않다.

**보존/출력**: 전체 출처 포함 SOURCE ZIP, R1…R10/C1…C10 20개 stage checkpoint ZIP, 4개 phase ZIP, 증거·계산 소스·진척 레코드; 각 파일의 SHA와 실제 Git/provider 영수증은 각 단계 이후 별도로 기록. 인상이나 기대만으로 원격 백업 완료를 선언하지 않는다.

**중앙 DAG 34/49, 신규 보조과학 R30 1/1 scoped.** NULL gates 유지. 다음 실제 source task는 EMAA original radex file 171×25, Velilla2008 original PES/sigma(E), 실제 REC/CR HD molecule chemical owner 및 distinct-author R6/C9다.