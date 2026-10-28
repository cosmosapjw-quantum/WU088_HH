# R18 — 원본 상태율의 정의와 계산 계약

확보한 DIGITAL.CSIC 저자 기관 원본 보충자료의 Table 2, PDF page 6에서
H⁺ + HD(v=0,j=2) → D⁺ + H₂(v′=0,j′=1)의 SQM 반응성 상태율을 추출한다.
소스 PDF는 273554 bytes, SHA256
a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754이다.
기관 record: https://digital.csic.es/handle/10261/305186 .
보충자료: https://digital.csic.es/bitstream/10261/305186/2/h_hd_rate_supplementary_material.pdf .

## 정의와 전제

표의 token a(x)는 a×10^(−x) cm³ s⁻¹를 뜻한다. a는 인쇄된 유한 소수 문자열이다.
따라서 a=A/10^d일 때 인쇄값의 정확한 유리수 해독은
k_print=A/10^(d+x) cm³ s⁻¹ = A/10^(d+x+6) m³ s⁻¹다.
이는 인쇄된 수의 수학적 해독이다. 원 계산의 오차나 반올림 규칙은 주어지지 않았다.

입력 PDF 바이트의 SHA256와 크기를 먼저 확인한다. 원본에서 page6을 추출하고
Table2와 다음 Table3 경계를 찾아 캡션의 product v′=0,j′=1, 온도 header,
initial (0,2) 행을 확인한다. 열 순서는
15,55,105,255,505,1005,1505,2005,2505,3005 K이다.
소스 문자열과 열·행 identity를 결과에 함께 남긴다.

## 물리적 상태와 spin

Table2의 수는 raw state-to-state k_(0j,0r)다. 원문 Eqs.(5)–(7)의 열평균은
K(T)=Σ_j p_j(T)[(1/4)Σ_(r even)k_jr(T)+(3/4)Σ_(r odd)k_jr(T)]다.
선택한 r=1의 열평균 기여는 (3/4)p_2(T)k_21(T)이며, raw table의 k 자체에
3/4를 적용하지 않는다. 이번 출력은 p_2를 구성하거나 K를 합산하지 않는다.
k_B와 T의 Boltzmann 인자는 원래 의미를 유지하며 별도 준위에너지를 가정하지 않는다.

보충자료 §3과 Tables1–10은 초기 j=0..6을 제공한다. 본문 Eq.(5)는 j=0..8을 쓴다.
Table11의 caption과 본문범위 차이는 OPEN_SOURCE_SCOPE_DIFFERENCE로 보존한다.
j7/8은 MISSING_NOT_ZERO다. 선택 j2 행은 양쪽 범위에 포함된다.

## 보존과 소비자

종 순서를 (H⁺,HD,D⁺,H₂), 반응계수를 ν=(−1,−1,+1,+1)로 둔다.
H핵 수 벡터 (1,1,0,2), D핵 수 (0,1,1,0), 전하수 (1,0,1,0)에 대해
각각 ν와의 내적은 0이다. 실제 상태밀도 n_(HD,02), n_H⁺가 주어졌을 때
사건율 J=k_21(T)n_H⁺n_(HD,02)는 m⁻³s⁻¹이며 dot(n)=νJ다.
고유시간을 다른 시간변수로 옮기려면 같은 소비자의 양의 clock Jacobian이 필요하다.
이번 원자료 출력에는 density·clock·역반응·에너지 Q를 채우지 않는다.
에너지 회계는 ΔK+ΔU_internal+ΔU_photon=0이며 필요한 source mass/level binding이 남아 있다.

## 상태

원자료 확보는 literature-supported, 유리수·단위·보존식은 derived다.
코드 실행과 독립 C9 이후에 implementation-verified를 결속한다.
실제 REC/CR 반응 소비자와 whole-A·whole-domain 오차 증명은 별도 의무다.
HH_R10=OFF, production=NOT_ISSUED, L4=false를 유지한다.

