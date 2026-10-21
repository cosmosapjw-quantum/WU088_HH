# PHYS75 기존 보충 후처리의 게시·백업 복구

2026-10-21. 역사적 원본은 `PHYS75_RESUME_DELIVERY.zip` 944108 bytes, SHA256 `52b329218eef5154e00a58bb27eb30fef9eadc9509f82fc8df5aac937a72305f`이다. 원본을 수정하지 않고 별도 복구 archive로 보존한다. 이전 실행 기록은 8개의 standalone algebra/interface test PASS, Python bytecode compile PASS, NCP/ODE/benchmark 0건이며, 실제 warm729 history의 열 매핑·분석 실행은 `HISTORY_INPUT_NOT_IDENTIFIED`이었다. 당시 `git fetch` exit128/DNS 오류는 네트워크 실행환경 오류이지 이론·코드 FAIL이 아니다.

원격 최신 확인: WU088_HH PR127 HEAD 71e925938387b73958c8881a06ef387e6874fafe, 더 최신 PR128 (`research/hh-phys75-sector-memory-20261021`) HEAD `92f5ab9dba531ebe05909dcb77d3740d2c68c580`, Base PR127. PR128은 독립적인 실제 long LRS source-bound 기억 후처리, 18 focused tests, 1231 histories/80015 samples, 6 small IVPs와 3 plots의 근거를 담고 있다. 이전 standalone trapezoid 구현이 PR128의 owner-pinned Simpson 경로보다 강한 정확성 또는 더 최신의 우선 계산 경로라는 주장은 하지 않는다. 중복 계산하거나 PR128 source를 덮어쓰지 않는다.

물리: 같은 normal orthonormal frame에서 pi_m,pi_r 텐서를 별도로 유지하고 합한 다음 norm. LRS signed half-contraction S=sqrt(3)s/H, P_X=sqrt(3)(8piG/c²)p_X/H². Full Frobenius은 sqrt2 배. S'+(3+H'/H)S=P_m+P_r이므로 같은 trajectory에서 I=exp(3(N-N0))H/H0, S=S0/I+I^-1 integral I P_m + I^-1 integral I P_r. 이것은 causal ablation이 아니다. Sampled quadrature residual은 continuum error certificate가 아니다.

서로 다른 REI PR198 long collisionless z20→4, REI PR213 warm short a=.1999→.2, HH PR127 control63을 합쳐 단일 새 scientific campaign으로 계산하지 않는다. 이미 완료한 15 PHYS73 jobs, 76 PHYS71 panels, 152 profiles, 729 warm pilot, 1231 long histories, 63 control은 재실행하지 않는다. HH_R10=OFF.

이 복구 단위의 목표는 원본 package의 source·test·실패 receipt를 소실 없이 저장하고, 기존보다 최신인 PR128을 명시적 scientific authority로 지정하며, 새 실행이 필요한 경우에만 원본 schema를 source-pinned explicit mapping으로 연결하게 하는 것이다. 원격 게시와 각 클라우드 사본의 ACK·byte readback은 이 문서가 아니라 별도 delivery receipt가 소유한다.
