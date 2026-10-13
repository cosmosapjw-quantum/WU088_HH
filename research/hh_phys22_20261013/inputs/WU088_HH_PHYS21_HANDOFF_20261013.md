# PHYS22: paired baseline과 유한 HH 응답 인증

PHYS21의 source-adapted full Jacobian, 정확한 memory/Schur 표현, 명목 tangent 실행을 재사용한다. 현재 숫자는 17-knot piecewise-linear 전체 baseline 위의 λ=0 sensitivity다. PHYS19 b_birth와 P01 b_geom을 구분하며 같은 scenario·clock·source·closure·IC를 유지한다.

다음 최소 연구 목표는 보고서 (21.35)–(21.38)의 실제 ε0,G,M2,Lh,Rδ와 tangent residual을 채워 λ∈[0,1]의 T·electron 응답을 수치 상계로 연결하는 것이다.

1. INPUTS.json의 동일 NPZ/source를 사용한다. 원 HM12 source와 background에서 baseline defect ρ0=barYdot−F0(barY)를 계산한다. 공통 fixed-q support와 per-H 광자 좌표를 유지하고 source를 0으로 대체하지 않는다.
2. positivity와 두 온도 guard를 포함하는 공통 tube를 구성한다. D_mm F=0 및 정확한 gas–photon bilinear remainder를 사용해 full dense Hessian 없이 M2와 성분별 오차상계를 만든다. 초기 IC 오차가 있으면 ε0의 초기값으로 넣는다.
3. variation-of-constants의 G 또는 같은 역할을 하는 양의 comparison propagator를 포함한다. paired error에 ε0를 단독 더하지 말고 (M2||eta||+Lh)ε0를 전달한다. 새 검증용 time representation과 tangent defect가 필요하다.
4. λ=1 finite-amplitude bootstrap과 온도의 정확한 quotient remainder를 함께 닫는다. HH fit uncertainty는 별도 source envelope로 유지한다. 종료조건은 response 오차 bound와 전제 tube가 서로 일치하는 실제 인증이다.

명목 source표·이번 complex-step·두 적분법의 변경 없는 검사를 반복하지 않는다. 새 tube/defect 인증을 위한 실행은 별개의 목적을 갖는다. 전체 photon tangent array가 필요하면 retained Wolfram source를 인증용 실행에 연결해 export한다. 현재 묶음에는 gas와 장부·광자 합계의 17점 응답만 저장되어 있다.

HH_STRICT_NATIVE, HH_SINGLET, 전체 RUX와 physical admission은 각 원 근거를 유지한다. 같은 assistant의 다른 산술 경로를 외부 심사로 기록하지 않는다. GitHub·Drive·Dropbox 게시 여부는 receipt의 실제 ACK로만 변경한다.
