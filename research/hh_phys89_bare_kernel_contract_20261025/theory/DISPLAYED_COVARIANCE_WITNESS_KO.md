# 원 MF33 표시 행렬의 정확한 국소 반례

## 결론과 입력

PHYS88에서 보존한 원 ENDF SHA256 `3024d8f0db604b074e33ed8b05027eb9f5a738614041ba44c83f048e0d0bc1af`의 MF33/MT102, LS1/LB5 fractional covariance를 원 decimal token 그대로 해석하면153×153행렬 F는 positive semidefinite가 아니다. Primary의 원 parser와 별도 Decimal/Fraction reference가154boundaries,11781packed values,23409matrix entries 및 raw token bytes를 정확히 일치시켰다. 아래 반례는 고정된 표시 행렬에 대한 결과이며 source의 underlying full-precision covariance, 물리 모형, evaluator 전체를 배제하지 않는다.

## 정확한 증명

Zero-based group0과10의2×2principal block은

F_sub = [[a,a],[a,a-d]],
a=4.278572×10^-4=1069643/2500000000,
d=10^-10.

두 번째 diagonal은4.278571×10^-4=4278571/10000000000이다. 따라서

det(F_sub)=-a*d=-1069643/25000000000000000000 < 0.

더 직접적으로153차원 벡터 w에서 w_0=1,w_10=-1,나머지0이면

w^T F w = a+(a-d)-2a = -10^-10 < 0.

Covariance 행렬이라면 w^T F w=Var(w·eta)>=0이어야 하므로, 이 정확한 표시 행렬의 stochastic covariance 채택은 허용되지 않는다. 같은 벡터의 Rayleigh quotient는 -5×10^-11이므로 최소 eigenvalue의 음수성도 exact하게 따른다. 이는 sampled quadrature residual 또는 continuum 추정이 아닌 유한 행렬의 직접 대수 증명이다.

Group0의 원구간은[5×10^-6,1.5×10^-5)eV이고 sigma support와의 교집합은[10^-5,1.5×10^-5)eV다. Group10은[0.01765,0.06265)eV다. 두 구간 모두 sigma support와 겹치므로 covariance support만의 바깥쪽 행을 골라 생긴 반례가 아니다.

## 진단과 해석 경계

Primary의 단 한 번 binary64 eigh는 min=-4.688696562507235e-8, max=2.8829808686931577과72개의 음수 진단값을 냈다. 이72개라는 개수에 interval spectral certificate를 붙이지 않는다. 정확한 채택 근거는 위2×2minor와 w의 음수 quadratic form이다. Independent reference는 eigenvalue를 재계산하지 않고 모든 source tokens와 이 minor를 exact Fraction으로 확인했다.

원F에 jitter, clipping, nearest-PSD projection을 가하지 않았다. 표시 token의 마지막 자리 ULP/반ULP 자료는 nearest-rounding을 가정한 조건부 formatting model이다. Full-precision 원 covariance와 실제 변환 과정이 없으므로 원인을 반올림으로 확정하지 않으며 cause=NOT_ESTABLISHED를 유지한다. 현재 단면적에 결속된 원 평가 covariance, normalization/rebinning, 원 precision 및 승인된 source correction이 필요하다.

## Strong no-go 범위 심사

NG1의 대상과 양화는 이 고정된 finite matrix로 한정했고, NG2의 증명은 위 exact 대수로 닫혔다. NG3의 실제 두 source-support 구간은 비공허하며, NG4의 장애는 음의 quadratic form이다. NG5의 직접 귀결은 raw F를 physical source CI에 사용할 수 없다는 admission 제한이다. NG6의 문헌 대비 새로운 보편적 기여는 주장하지 않는다. NG7은 source/independent reference 및 C9의 scoped review에 한정한다. 따라서 결과 분류는 DISPLAYED_MATRIX_COUNTEREXAMPLE이며 strong no-go 성과는 NOT_CLAIMED다.

새 thermal rate, coupled history, 실제 nuclear activation 또는 fast stopping은 계산하지 않았다. 선택 물리 노드는 PARTIAL_INPUT_DEPENDENCIES이다.
