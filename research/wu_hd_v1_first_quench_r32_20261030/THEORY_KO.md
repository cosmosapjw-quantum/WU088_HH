# WU R32 이론 연구: 원본 GL2022 H⁺–HD(v=1) 충돌에 의한 첫 진동 소멸

## 연구 계약과 출처

부모: WU PR #170 (HEAD `d359a8d2ecfb68c17657ba30b41c5796d3bde89c`). 전 단계 R31 완전 SOURCE ZIP SHA256 `3286e22a7663ab3114685698e7653b00ac3ea1ec439af466b5c4ae5483e42078`을 byte identity로 보존한다. 그 안의 GL2022 (González-Lezana, Hily-Blant, Faure 2022, JCP 157, 214302, DOI 10.1063/5.0128598) supplementary original PDF SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`의 이전 source-checked table 12–28 CSV 1560셀 SHA256 `58c252a1c3f62995ed748c7620e342bc98d8aabb307271bff48f7711e4f1cd7c`를 재사용한다. 별도의 측정값이 아니라 원 연구의 **SQM 계산 충돌률**이다.

EMAA DOI `10.17178/emaa_hd_rovibration_805a7aa5`는 171 H⁺ 충돌 전이×25 온도를 제공한다고 설명하지만, 원본 RADEX 숫자 파일은 이번 실행에서 **미확보**이다. EMAA 숫자의 GL2022 원문과의 동등성은 검사하지 못했고, EMAA 수치를 만들어 쓰지 않는다. CDMS 역사판 2011 v2 공식 웹 표시 `.egy`의 에너지 준위는 원문 페이지를 텍스트로 읽어 따로 보관했다. 이 파일은 **원본 byte-identified `.egy`가 아니며** SPFIT 공분산이 아니다. `sources/CDMS2011V2_RENDERED_V0V1_LEVELS.json`의 표시 6자리 cm⁻¹ 값과 변환을 사용한다.

원 출처에 등장하는 초기 HD(v=1,J=0…6)에서 동일 진동 v=1 낮은 J로의 21개 전이, v=0 J'=0…10으로의 68개 전이, 온도 T={15,55,105,255,505,1005,1505,2005,2505,3005} K의 890셀을 보존한다. 단 2005 K의 (1,2)→(0,5) 출처 토큰 `1.58(10`은 malformed로, 임의 수정 없이 **2005 K의 7 초기 상태 전부**에 대해 완전 Markov 결과를 보류한다. 남는 9개 원 출처 온도에는 9×89=801개의 정확한 출처 유효 셀(진동 소멸 612, 같은 진동 하향 회전 189)이 있다.

## 조건부 모델과 계산식

Transient 상태 `j=0,…,6`은 (v=1,J=j), 종단 상태 `b=0,…,10`은 (v=0,J'=b)이다. 원본 데이터의 아래 방향만을 따르는 `DOWN_ONLY_COUNTERFACTUAL`와 원본 하향값에 상세평형으로 **유도한** 상향 회전을 더하는 `DB_UPWARD_V1`를 별도로 계산한다. 후자의 역과정 계수는

\[
k^{(1)}_{\ell\to j}(T)=\frac{2j+1}{2\ell+1}\exp\!\left[-\frac{100hc(\tilde E_{1j}-\tilde E_{1\ell})}{k_{\mathrm B}T}\right] k^{(1)}_{j\to\ell}(T),\qquad j>\ell.
\]

원본 하향 및 비진동 소멸률 계수 단위는 cm³ s⁻¹, \(\tilde E\)는 cm⁻¹, \(h,c,k_B\)는 SI 상수, 여기서 100은 cm⁻¹→m⁻¹ 변환이다. H⁺ 수밀도 n (cm⁻³)와 시간 t(s)의 fluence 변수 \(s=\int n(t)\mathrm dt\) (cm⁻³ s)를 사용한다. 온도 고정과 계수 상수 가정하에 확률벡터의 충돌부는 \(\mathrm dp/\mathrm ds=Hp\)이며, H의 off-diagonal은 transient 채널의 각 계수, \(Q_{bj}\)는 종단 v=0 채널의 원본 계수다. 대각항은 열합이 영이 되도록 \(H_{jj}=-\sum_{i\ne j}H_{ij}-\sum_bQ_{bj}\)로 둔다.

모든 초기 상태에 적어도 하나의 출처 표기된 종단 sink가 있으므로 이 유한한 Metzler transient 생성자의 \(-H\)는 nonsingular M-matrix이고 fundamental matrix \(F=(-H)^{-1}\)가 비음수다. 따라서

\[
B=QF,\quad \mathbf{1}^{\!T}B=\mathbf{1}^{\!T},\quad
\bar s_j=\mathbf{1}^{\!T}Fe_j,\quad k^{\mathrm{eff}}_j=1/\bar s_j
\]

를 얻는다. \(B_{bj}\)는 출처에서 선택된 충돌들만 허용했을 때 첫 v=0 종단이 J'=b일 확률이다. \(\bar s_j\)는 cm⁻³ s, 유효 충돌계수는 cm³ s⁻¹이다. 외부에서 n이 일정하게 정해졌을 때만 \(\langle t\rangle=\bar s/n\)이다. 인위적인 우주론적 밀도를 삽입하지 않는다.

종단 회전/진동준위 내부 에너지를 \(E_{vb}=100hc\,\tilde E_{vb}\) J로 두고, 광자·화학반응 채널을 **모델에서 제외**한 경우, 충돌 시 bath로 넘어간 에너지의 기대값은

\[
\langle Q_{\mathrm{bath}}\rangle_j=E_{1j}-\sum_{b=0}^{10}B_{bj}E_{0b}.
\]

이것은 endpoint telescoping과 동일하며, 직접 edge별 \(\sum_{m\to n}(E_m-E_n)k_{m\to n}F_{mj}\)를 계산하여 검산한다. 결과는 초기 **단일 HD 분자당** J 또는 eV 단위이며 volume cooling/heating이 아니다. 일정한 밀도와 온도를 유지하기 위한 외부 에너지 저장고가 숨어 있고, 이 모델에는 v=0→v=1 재여기, radiative v=1→v=0, H₂로의 reactive exchange, LTE 정상상태가 없다.

## 물리 해석과 출처 경계

원본 충돌률 및 원본 온도 인덱스는 **source-verified**, detailed-balance 상향률과 위 first-passage 공식은 **derived**, 생성한 126 조건부 모형 사례와 1386 종단 확률은 **numerically checked**이다. v=1 radiative Einstein-A 전이와 v=1 reactive rate의 상대 hazard를 모르므로 이 결과는 실제 진동수명, 전체 순냉각률 또는 관측 가능한 line cooling에 승격할 수 없다. \(Q_{\rm reaction}\), PES-native threshold, EMAA raw file, 실험 공분산과 owner ACK도 여전히 NULL/미확보다.

정본 WU DAG=**34/49 unchanged**. 신규 R32 scoped auxiliary physics **1/1**은 검증한 restricted 계산만 가리킨다. 완전한 network/FULL_A/L4/production/정본 DAG 승격은 미승인이다. Wolfram은 2-state absorbing 보존/정규화/열수지 기호 항등식 `{True,1,{True,True}}`를 반환했다. 이는 같은 작성자 CAS 검산으로, 독립 작성자 R6/C9가 아니다.
