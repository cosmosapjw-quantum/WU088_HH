# R7 R6 단계 독립 이론 심사

**판정: PASS_SCOPED_CONDITIONAL_GENERAL_FINITE_STATE_THEORY.** 실제 수정이 필요한 수학적 결함은 발견하지 않았다. 이 판정은 명시한 전 구간 가정 아래의 조건부 일반 유한차원 정리에 한정한다. 코드·새 실행 결과의 C9 판정과 과학 채택은 아직 수행하지 않았으며 root가 결정한다. 검토 시점 DAG는 **13/30**, 이 검토가 변경한 노드는 없다.

## 실제 검토 방법

심사자는 이론·생산 코어를 작성하지 않았다. R7 계약, 증명 전체, equation-to-code map, claims를 읽고 사영 미분, HD 저장고 불변량, 각 구간 부등식 방향, endpoint Duhamel 계산을 독립적으로 손으로 전개했다. R4 events/species/source의 HD 관련 원래 상태와 R6의 K/full-A 구분을 직접 대조했다. solver·CAS·과학 테스트·과거 과학 재실행은 **모두 0회**다. 수행한 프로그램 작업은 파일 판독과 SHA256 결속뿐이다.

검토 대상 증명 SHA256: `0390132d823cb227a8eeb7f0e8d29157acba5d50a26983d0385e72626a1ea8f3`. 계약/map/claims 및 재사용 파일의 정확한 identity는 동반 JSON에 기록했다.

## 주요 판정 근거

1. **일반 사영과 Jacobian 경계.** 식 R7.7의 lift 미분항은 정확히 `-E_lift_dot*y`이며 잔차·forcing은 kerP에 남는다. 전 구간의 공통 convex box에서 평균값 정리로 a,b,c를 얻고, coarse Jacobian의 signed l1 matrix measure로 d를 얻는 과정이 타당하다. monomial의 지수가 0이면 미분을 먼저 0으로 설정하므로 zero density에서도 부정형을 만들지 않는다.

2. **인과적 endpoint 행렬.** ordinary comparison V를 먼저 얻고, endpoint에서만 Duhamel의 초기 잔차를 rho로 줄인다. 잔여 적분은 `V1(H)-w01`이므로 `T=exp(BH)-(1-rho)e1e1^T`가 따른다. a>=0와 Metzler B 때문에 `exp(BH)11>=1`, 따라서 T>=0이다. d<0이어도 성립한다. 늦은 forcing에는 rho를 곱하지 않는다. whole-block V와 endpoint T는 문서에서 올바르게 구분한다.

3. **HD 불변량과 음의 damping.** H/D/charge의 rank3 불변량은 동일 초기 invariant class에서만 `e=s*eta`를 준다. 두 곱의 차이를 정확히 전개하면 R7.22의 damping 부호와 residual coupling이 나온다. `||e||1=4|eta|` 변환도 명시되어 있어 scalar adapter와 벡터 관측량 사이의 계수 손실이 없다.

4. **명시적 a,b,c,d,g.** `||Qpi D||1=2 max_i d_i(1-pi_i)`, `||D*pi-pi*dbar||1<=Delta_d/2` 및 zero-sum `|d^T r|<=Delta_d R/2`가 사용된 방향과 일치한다. lower density/rate는 damping의 lower에만 사용하고 이를 음수 d로 옮겼다. baseline forcing과 feedback을 분리한 R7.26–28은 중복 차감하지 않는다.

5. **K-only rho의 사용 범위.** 이 증명은 `-w Qpi D r` 전체를 aR에 포함한다. 그러므로 nominal K의 rho를 재사용할 수 있다. 그 항을 full L에 흡수한 뒤 K-only certificate를 붙이는 주장은 없으며, 해당 변경에는 full-family 인증이 필요하다고 명시한다. 실제 같은 state graph·clock·H·collider 결속은 여전히 전제다.

6. **원자료와 모델의 구별.** R4의 corrected formation은 para-H2(v0,j0), destruction은 thermal HD(v0,j0..8)와 source spin-weighted H2 제품이다. 이 차이를 실제 원문 JSON에서 확인했다. R7은 공통 pool/state/branch mapping을 별도로 요구하며, 반대 정수 방향만으로 microscopic detailed balance나 물리적 폐쇄를 승인하지 않는다. TIQM/SQM 중복 활성, aggregate rate의 임의 state vector 복제, branch=pi 기본값도 허용하지 않는다.

7. **Singular B 및 양의 Taylor 상계.** augmented Metzler matrix는 B의 역행렬 없이 forcing 적분을 포함한다. nonnegative shift 이후의 entrywise Taylor partial sum과 induced-norm scalar tail, `N+2>z` 조건, outward `exp(-sigma H)` upper의 곱은 올바른 상계다. T를 얻는 exact subtraction도 방향을 보존한다. B=0, diagonal, nilpotent 경우의 식도 일치한다.

## 범위와 다음 단계

발견한 material finding **0**, 필수 수정 **없음**. 이 판정은 새 기본 정리의 우선권이나 strong no-go를 주장하지 않는다. GL2022 state-to-state 배열, 실제 formation branch, density/history, physical clock, x0와 named consumer를 공급하지도 않는다.

생산 코드와 계약된 단일 primary/reference 결과가 준비되면, **같은 독립 심사 pass의 C9 후반부**에서 기존 guard·산술 방향·판별 사례의 구현 연결을 확인하면 된다. 추가 원문 추적, 이전 과학 재실행, 재귀적인 별도 audit는 요구하지 않는다.

