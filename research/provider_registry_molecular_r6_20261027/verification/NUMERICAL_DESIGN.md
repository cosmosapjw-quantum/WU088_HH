# R6 수치 설계와 유효한 오차 방향

## 1. 계산 순서

1. SHA-256으로 고정된 source와 REC parser를 읽고 native 100 K para-H₂ literal을 선택한다.
2. 정확한 SI 상수와 source 파수로 rational (z_i)를 구성한다.
3. `exp_neg`의 outward thermal interval에서 positive weights·normalized probability intervals·direct pair ratios를 얻는다.
4. 각 source edge 구간과 column-conservative diagonal을 묶어 `GeneratorBox`를 만든다.
5. 전체 exit 상한에서 uniformization rate와 공통 `P_lower`를 만든다.
6. 고정 ((\mu,N)=(8,64),(32,128),(128,320),(256,512))에 대해 positive lower polynomial을 한 번씩 계산한다.
7. pair overlap으로 block certificate를 만들고 별도의 synthetic full-(A) fixtures에서 forced comparison 업데이트를 생성한다.

Source thermal precision은 256 bits, source polynomial precision은 512 bits이다. Synthetic controls의 polynomial은 256 bits로 계산한다. 실제 입력과 각 결과에 선택값을 기록한다.

## 2. 지수함수의 정확한 enclosure

\(z=2^s y, 0\le y\le1/2)로 줄이고 exact rational arithmetic으로 연속 odd/even Taylor 부분합을 구한다. odd sum은 하한, 바로 앞 even sum은 상한이다. 초기 Taylor gap이 (2^{-(p+16+s)}) 이하가 되면 두 endpoint를 denominator (2^p)의 dyadic으로 밖으로 반올림한다. 이후 각 제곱의 lower endpoint는 floor, upper endpoint는 ceil을 사용한다.

이 threshold는 차수와 작업량을 정한다. 최종 오차는 실제 최종 `hi-lo`이다. 교대급수 bracket의 수학적 타당성은 목표 너비 달성 여부와 별개로 유지된다. Native probability interval의 구현상 구체적 수용 기준은 최대 width (<10^{-60})이다. 이는 이번 새 입력에 선택한 기준이며, 이전 연구의 허용오차를 바꾸지 않는다.

작은 확률의 하한이 낮은 정밀도에서 0으로 반올림될 수 있다. `exp_neg`는 그 유효한 외측 구간을 반환하고, `normalize_weights`는 strictly positive lower weights가 필요한 계약에 맞춰 0 하한 입력을 거절한다.

## 3. Matrix polynomial의 하한 보존

\(S=2^p)에서 행렬은 정수 numerator로 저장한다. Nonnegative dot product의 합을 구한 뒤 `// S`를 적용하면 정확한 곱보다 크지 않다. Poisson weight는 (w_0\le e^{-\mu}), (w_{m+1}=\lfloor S w_m\mu/(m+1)\rfloor/S)로 갱신한다. 각 weighted matrix contribution도 아래로 반올림한 뒤 합산한다.

모든 성분과 항은 비음수이므로, matrix-power 반올림·weight 반올림·weighted-product 반올림·positive tail 생략이 모두 하한 방향을 보존한다. 최종 (R_{lower}\le\Phi_A(H))와 column-substochastic 성질이 따라온다. 소수 표시값은 certificate가 아니다.

Degree 증가에 따른 overlap 개선은 동일 실행의 partial-sum trace에서 기록한다. 별도 parameter sweep으로 degree나 source (H)를 반복 탐색하지 않는다. Source acceptance는 고정한 블록에서 실제 양의 (\beta)를 얻는 것이며, instantaneous coefficient 0과 finite-block (\rho<1)의 구분을 유지한다.

## 4. Full reset generator와 강제 비교식

Common killing (\kappa\le\min v)를 추출한 뒤 full (A=K+\pi(v-\kappa1)^T-\mathrm{diag}(v-\kappa1))에서 certificate를 만든다. 코어는 offdiagonal upper sums를 exit 상한으로 사용한다. 추가 simplex 개선은 구현하지 않았다.

`forced_step`은 모든 coefficient와 초기 비교값의 비음수성을 검사한다. Damping denominator는 1 이상이다. 한 블록에서 (M^*=M+F_+H), (G=q_cM^*+g)를 계산한 뒤 endpoint와 whole-block 값을 따로 반환한다. Error forcing 적분은 (H\widehat U+GH^2/2)이다. Endpoint residual을 전체 블록 적분에 넣는 경로는 없다.

Caller는 coefficient bounds의 interval-wide 유효성, certificate가 속한 전체 (A), 같은 (H), source·density·clock을 결합해야 한다. Scalar 입력만으로 이 provenance를 추정하지 않는다. 고정 primary synthetic fixtures는 full-(A) certificate와 계수·초기값을 함께 export한다.

## 5. 경계와 오류 처리

| 입력·경계 | 동작 |
|---|---|
| bool, binary float, 비유한 문자열, 0 denominator | `DomainError` |
| (z<0) 또는 (z>256), bits 범위 밖 | `DomainError` |
| weight lower (\le0), simplex를 포함하지 않는 probability boxes | `DomainError` |
| 비보존 generator, 음의 edge, diagonal coupling 불일치 | `DomainError` |
| (\kappa)가 destruction lower보다 큼, (\lambda)가 full exit보다 작음 | `DomainError` |
| (H\le0,N>512,p>768,\lambda H>256) | `DomainError` |
| source/parser hash 변경 | `DomainError` |
| (n=1) | zero-sum 공간이 0이므로 (\rho=0) 규약; column mass 1을 요구하지 않음 |
| disconnected graph | 실제 overlap 0을 허용하고 (\rho=1) 반환 |
| 큰 canonical fraction | chunk 정수 변환으로 roundtrip; 전역 Python digit-limit 변경 없음 |
| 결과 파일이 이미 존재 | create-only runner가 `FileExistsError`로 중단 |

## 6. 검증의 역할과 비용

Primary는 exact semantic controls, source bounds, lower-polynomial trace, three forced fixtures, one switched family를 한 campaign에서 실행한다. Strong no-go나 물리 consumer 판정은 생성하지 않는다. 독립 reference는 원 source의 별도 parsing과 250자리 Decimal 열계산, SciPy 행렬지수, exact Fraction overlap 검사를 사용하도록 별도 작성되었다. 두 실행의 code/input/result identity와 실제 CPU는 각각 기록한다.

Primary의 핵심 작업량은 source 네 블록의 (O(n^3\sum N)) nonnegative 정수 행렬곱이다. 중간 행렬·weight numerator를 fixed dyadic precision으로 유지해 dense Fraction matrix powers의 denominator 증가를 피한다. Core는 표준 라이브러리만 사용하며 independent reference의 numerical dependencies와 분리된다. 허용량과 중단 조건은 `CONTRACT.json` 및 `EXECUTION_PLAN.json`을 따른다. 여기에는 미관측 runtime·PASS·성능 수치를 넣지 않는다.
