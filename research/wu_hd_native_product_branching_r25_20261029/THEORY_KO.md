# WU088_HH R25 | GL2022 원본 H₂ 회전상태별 생성률 데이터와 조건부 반응 이력

2026-10-29 KST. **이론 연구 P01**, 앞선 R24 원문 Laplace-support 결과를 재해석하거나 대체하지 않는다.

## 고정된 출처와 질문

이온 반응 `H+ + HD(X,v=0,J=2) -> D+ + H2(X,v'=0,J')`에 대해 GL2022 (González-Lezana, Hily-Blant & Faure 2022, JCP 157,214302, DOI 10.1063/5.0128598) 원본 supplementary PDF의 **Table 1–10**은 최종 J'=0,...,9마다 초기 `(v,J)=(0,2)`의 10개 온도 15,55,105,255,505,1005,1505,2005,2505,3005 K 반응률을 제공한다. 원본 PDF 273554 bytes, SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`. 인쇄 `a(b)`는 `a*10^{-b} cm^3 s^{-1}`이고 괄호는 **오차 표기가 아니라 지수**다. 이는 SQM 계산된 상태별 rate이며 source numeric uncertainty는 제공되지 않는다. R24는 J'=1 단일 행만 사용했으므로 **새 물리 데이터 객체**는 10×10 모든 출력 상태의 원전 인쇄수치다.

단, 15K의 J'=6,7,8,9에서 `0.00(00)`라고 인쇄됐다. 이것은 **인쇄된 숫자 0**의 기록이며 물리적 rate가 정확히 0이라는 검증이 아니다. 이 4개는 원본 문자열을 보존하면서 `unqualified_printed_zero`로 표기한다. 나머지 96개 인쇄 셀은 양의 rate다. 높은 J'>9 및 다른 진동준위/원경로는 이 작업에 포함하지 않는다.

## 실제로 유도하는 물리량

고정한 온도 T와 **보고된 J'=0..9에 국한한** 경로의 rates `k_j(T)>=0`에 대해

`K_reported(T)=sum_{j=0}^9 k_j(T)`;
`b_{j|reported}(T)=k_j(T)/K_reported(T)`;
`b_{ortho|reported}=sum_{j odd} b_j`, `b_{para|reported}=sum_{j even} b_j`;
`<J'>_{reported}=sum_j j b_j`.

위 비율은 Table 1–10에서 같은 원전 방식과 가중치 관례를 유지한 **보고된 채널 집합에 조건부**인 branching 통계량이다. 전체 `H+ + HD`의 absolute total rate나 모든 H₂ 진동/회전 상태에 대한 확률로 승격하지 않는다. H₂에서 홀수 J'는 ortho, 짝수 J'는 para이지만, 원본 rate에 임의의 3/4 가중치, Boltzmann HD(J=2) 초기 population 또는 화학 역반응을 추가하지 않는다.

15K는 4개 출력 rate가 `unqualified_printed_zero`여서 `K_positive_printed`는 **누락된 기여가 비음수일 때의 하한**이고, 물리적 branching/평균 J와 ortho share는 `null`로 남긴다. 55–3005K의 9개 온도에서는 보고된 10개 항 전부에 양의 인쇄값이 있어 **보고된 채널 내 상대분포**를 계산할 수 있다.

## 닫힌 다중 생성물 반응의 제한적 물리 모델

반응물 밀도 N_H+, N_HD와 생성물 N_D+, N_H2,j를 공통 proper-time과 같은 **고정 부피**, 외부가 고정한 T에서 둔다. reported-only forward model:

`R_j = k_j(T) n_H+ n_HD [m^-3 s^-1]`,
`dot n_H+ = dot n_HD = -sum_j R_j`, `dot n_D+ = sum_j R_j`, `dot n_H2,j = R_j`.

초기 `n_H+(0)=n_HD(0)=n0`, 나머지 영인 제한된 시험에서, `K=K_reported(T)`가 일정하면

`n_H+(t)=n_HD(t)=n0/(1+n0 K t)`;
`xi(t)=n0-n_H+(t)=n0^2 Kt/(1+n0Kt)`;
`n_D+(t)=xi(t)`, `n_H2,j(t)=b_j xi(t)`.

서로 다른 원본 온도 노드로 이루어진 piecewise-constant 외부 T schedule에도 매 구간 잔존 n을 초기값으로 사용해 같은 식을 연결하고, **생성물별로** `Delta n_H2,j=b_j(T_segment) Delta xi_segment`를 합산한다. 따라서 총 반응 extent는 `K`만 보지만 생성물 상태 분포는 온도 이력의 영향을 받는다. 모두 원본 SQM nominal rates와 외부 지정 T/n0/duration의 **조건부 전방 계산**이다. 역반응, UV, 재결합, 다른 충돌, H₂ 내부 재분배, n_e, Hubble expansion, 실제 성간 화학, 열욕조는 포함하지 않는다.

H 핵, D 핵, 전하, 총입자수는 반응 벡터 (-1,-1,+1,+1)를 확장한 각 J' 행에 대해 각각 정확하게 보존된다. 한 J' event에서 H 수는 `-1 -1 +2=0`, D 수는 `-1 +1=0`, 전하는 `-1 +1=0`, 입자수는 `-1 -1 +1 +1=0`.

## 반드시 유지할 과학/권한 게이트

GL2022의 Velilla2008 PES에서 **직접 인증한** `HD(0,2) -> H2(0,1)` asymptotic threshold, 핵질량/비BO/동위원소 ionization correction, 원 산란 E_total/E_collision 영점, state-specific σ(E) 수치 파일은 미확보. R24 Laplace bound 15.186303821758897 meV는 조건부이고 R23 spectroscopy threshold 20.950020993840458 meV는 외부 후보다. R25 branching에는 어느 것도 rate 수정에 쓰지 않는다. `GL2022_PES_NATIVE_THRESHOLD=null`, `physical_Q=null`, `bath_heat=null`, `reverse_rate=null`, `owner_ACK=null`, `source_rate_uncertainty=null`. 

REC PR159은 CDMS/LAMDA rotational research call graph, CR PR124의 `HD_CX`는 **atomic D0+H+ exchange**다. 외부 repo mutation은 owner ACK 이전 금지. 최신 확인 WU PR163 HEAD `dc24eaf4ce8ae73635ac5debcab84ea0eaa6a28c`에서 새 자식으로 추가한다. WU R22 PR160은 read-only sibling. Central canonical WU **34/49 unchanged**, 지난 R23 workflow **18/20**, distinct-author R6/C9 `NOT_RUN`, `HH_R10=OFF`, `L4=false`, `production=NOT_ISSUED`, `full_A=null`; scoped R25 본 physical data matrix 1개 별도 보존.