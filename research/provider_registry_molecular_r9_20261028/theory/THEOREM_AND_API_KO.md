# 재사용 가능한 R9 정리와 API 계약

## 조건부 셀 폐쇄 정리
같은 generator family/state order/clock에서 비음수 연속 R,E가 PROOF_KO의 Duhamel 부등식(R9.2–R9.4)을 만족한다고 하자. 비교 계수 a,b,c,g_r,g_e 및 초기 상계는 비음수이고 d는 부호를 유지한다. h는 h0=1인 비증가 uniform-all-starts 인증 커널, e와phi는 지정 scalar propagator/integral의 인증 상방값이다.

균일 닫힌 셀 I_n=[nδ,(n+1)δ]에서 과거 상계로 만든 A_n,B_n은(R9.6–R9.7)이다. D=1−δa−δbphi*c>0이면
R*_n=(A_n+δbB_n)/D,
E*_n=B_n+phi*cR*_n
은 해당 셀 전체의 상계다. 이 구성을 첫 셀부터 순차 수행할 수 있고 선행 전체 궤도의 오차 envelope는 필요 없다. 계수의 whole-domain validity와 kernel/factor 인증은 여전히 전제다.

정확한 같은 셀/시각의 다른 인증 상계와 성분별 min을 취하면 유효성이 보존된다. Endpoint식은(R9.13–R9.15), 방향 반올림은(R9.16), 독립 수치 예산은(R9.17)로 고정한다. D≤0은 이 API 충분조건을 벗어나며 물리 발산을 뜻하지 않는다. 일반 raw no-worse 및 rounded-vector discrete supersolution은 주장하지 않는다.

## 계산식–함수
`sweep(B,g,delta,initial,kernel,coarse_factors,*,binding,whole_caps=None,point_caps=None,bits=128)`는 exact Fraction 자료와 동일 provenance를 받는다. 반환값은 양 모드에 대해 powers,A_base,B_base,raw_whole_cells,whole_cells,F_upper,L_upper,raw_endpoints,endpoints를 보존한다.

현재 유한 구현 domain은1..192cells,128bits,scalar8192bit,abs(d*delta)<=16,ordered states1..16이다. Scalar/cell/family/clock 조건을 검사한다. d<=0은 e_upper<=1을 추가 요구한다. Generic API의 metadata 검사는 외부 인증 부등식 자체를 입증하지 않는다. 고정 runner는 immutable R8 원문 SHA와 실제 source pointer로 이 전제를 결속한다.

## 채택 근거와 범위
일반 증명과 독립 R6 review, 실제 source freeze, primary150/150, independent reference438/438(34590component comparisons), finalC9 PASS_SCOPED/openmaterial0에 근거한다. 새 CAS는7+4zero residuals와1True/3unreduced의 qualified corroboration이다. 실제 native9 개선은 작으며 상세값은 RESULTS_KO에 있다.

이 정리와 구현을 조건부 연구 산출물로 채택한다. Actual physical consumer/rate/density/clock admission, production readiness 또는 central completion을 부여하지 않는다.
