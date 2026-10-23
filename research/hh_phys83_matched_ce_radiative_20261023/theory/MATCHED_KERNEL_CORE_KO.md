# PHYS83 paired finite CE kernel: source와 계산식

CCC LS 원자료의 문턱 Δ=10.20435 eV를 보존한다. 이는 NIST/HyRec fine-level gap 또는 유한질량 isotope gap과 동일시하지 않는다. g0=2, g2S=2, g2P=6. 입사 전자의 운동에너지 E=ε+Δ, θ=k_B T(eV), ε∈[0,L], L=958.40145 eV로 둔다. 단면적은 cm²로 변환한다. 등방 Maxwell 분포와 stationary-heavy-target convention을 사용한다.

## 소스 계약과 미시적 가역성

원본 excitation σ↑(E)에서 W(ε)=(ε+Δ)σ↑(ε+Δ)의 knot를 만든 뒤 ε,W에서 PL 보간한다. 따라서 모델의 σ↑=W/(ε+Δ)는 σ 자체의 PL과 다른 명시적 interpolation이다. 역방향은 ε σ↓(ε)=(g0/gi) W(ε)로 정의한다. 원본 reverse σ를 독립적으로 PL 보간하면 이 같은 finite 모델의 미시적 가역성은 일반적으로 깨진다. ε=0의 원본 reverse sample은 없으며 flux의 우극한은 forward threshold knot W(0)=0으로 정의한다. ε=0의 σ 자체를 임의로 평가할 필요가 없다.

원본 reverse451점씩은 printed rounding interval 수준의 별도 source check다. 원본 중앙값의 약10^-4~10^-3 reciprocity 차이를 물리적 상세균형 위반으로 부르지 않는다.

## Maxwell moment의 동일성

C=100 sqrt(8 eV_J/(π m_e))로 두면 q↑=C θ^(-3/2) exp(-Δ/θ) M0, q↓=C θ^(-3/2)(g0/gi)M0이고 Mj=∫_0^L ε^j W(ε)exp(-ε/θ)dε다. 이는 역방향 Maxwell 적분에서 εσ↓를 대입하고 같은 유한 support로 변수치환한 직접 결과다. 따라서 logq↑-logq↓=log(gi/g0)-Δ/θ가 정확하다. σ cm²와 C의 cm/s 변환으로 q는 cm³/s다.

평균 excess는 μe=M1/M0, 평균 입사 에너지는 μ↑=Δ+μe, μ↓=μe다. 온도독립 support와 W에 대해 dlogq↑/dT=((Δ+μe)/θ-3/2)/T, dlogq↓/dT=(μe/θ-3/2)/T. δ=Δ/(k_BT)가 클 때 작은 q↑에 exp(δ)를 곱하지 않고 공통 moment의 log로 두 rate를 별도로 만든다.

## 양의 cell 계산식

각 cell [l,l+h]에서 t=(ε-l)/h, z=h/θ, Jn(z)=∫_0^1 t^n exp(-zt)dt다. 좌/우 W 값이 WL,WR이면

M0_cell=h exp(-l/θ)[WL(J0-J1)+WR J1],
M1_cell=h exp(-l/θ){WL[l(J0-J1)+h(J1-J2)]+WR[l J1+h J2]}.

모든 weight가 비음이다. C22D/PHYS81의 byte-pinned J0,J1,J2 함수만 재사용하고 기존 CI/PHYS82 과학 callback은 호출하지 않는다. 원본유한 support 밖의 zero는 선택한 연산자의 정의이며 실제 고에너지 단면적이나 interpolation error의 certificate가 아니다.

## 에너지와 원자 population

1s↔2s,1s↔2p의 net collisional event가 내부에너지 ±Δ를 이동시키고 electron thermal ledger에는 반대 부호를 준다. spontaneous event는 원자 내부에너지 Δ를 복사로 옮긴다. optically-thin boundary 아래 그 에너지를 escaped ledger에 기록한다. 2s의 two-photon branch는 사건당 두 photons, 알려진 별도 M1 branch는 한 photon이다.2p는 한 photon이며2s pair의 총에너지 Δ만 확정한다. A2s_total=8.229+2.496e-6 s^-1로 두 branch를 모두 포함한다. 특정 half-energy monochromatic spectrum을 만들지 않는다.

고정T/ne는 local coefficient step의 입력이다. thermal ledger를 적분해도 새 coupled temperature trajectory를 푼 것이 아니다. 원자 수/전하와 normal frame을 보존한다. 원본 LINE01의 원자↔복사 ownership은 재사용하지만 gap과 optical closure가 다르므로 그 source card나 nonlinear thick map을 그대로 연결하지 않는다.
