# R31W research checkpoint: gauge covariance and affine-cell bounds

기준 b05db60ff8db75ed6bb2497bffea8b87f57617be / tree f90e638d3a33a2dcf5a44b32ab77dc1e03111f7e. R31V NCP의 134 PASS와 BR-03 preflight repair를 수용하되 BR-01/BR-02 historical gap, independent_review_admitted=false를 유지한다. 이번 노드는 감사 반복이 아니라 새 이론 유도와 저장된 point 자료의 경량 재분석이다. 기존 control/native source는 변경하지 않았다.

## 직접 유도

O>0,H=H†인 고정 차원 공간에서 i hbar O dotc=(H-i hbar D)c, N=c†Oc라 두면 dotN=c†Rc, R=dotO_actual-D-D†이다. eta=sup_x |x†Rx|/(x†Ox)=||C^-†RC^-1||2, O=C†C. 정확한 basis 정의에서는 R=0이고, 여기서는 독립 보간된 represented equation의 불일치를 검사한다.

시간의존 invertible T에 대해 O'=T†OT, H'=T†HT, D'=T†DT+T†OdotT이다. dotO'에서 product rule을 적용하면 R'=T†RT, A'=T^-1AT-T^-1dotT. Rayleigh supremum의 가역 치환으로 eta'=eta이다. 따라서 **같은 방정식의 gauge/frame 변경만으로 defect를 repair할 수 없다.** Dephase한 뒤 다른 envelope를 새로 보간하는 것은 별도 approximation이므로 이 불가능 진술의 대상이 아니지만 withheld direct/derivative 검증 없이 승인하지 않는다.

Rectangular Q에서는 o=Q†OQ, d=Q†DQ+Q†OdotQ, r=Q†RQ. ambient O>0이면 eta_reduced<=eta_full이나 등호는 보장되지 않는다. O=I2,R=diag(1,-1),Q=(1,1)^T/sqrt2이면 reduced eta=0, full eta=1. 현재 Q(z=2)의25D 결과를 arbitrary truncation/full49/global subspace의 결과로 확대하지 않는다.

## Affine endpoint 정리

한 공통 coordinate field에서 **전체** O(s)=(1-s)O0+sO1, D(s)=(1-s)D0+sD1, s∈[0,1], dt>0, O0,O1>0이라 하자. Rj=(O1-O0)/dt-Dj-Dj†이면 R(s)=(1-s)R0+sR1이다.

M=max(eta0,eta1), alpha=min_j lambda_min(Rj,Oj), beta=max_j lambda_max(Rj,Oj)라 두자. endpoint의 -M Oj<=Rj<=M Oj 및 alpha Oj<=Rj<=beta Oj를 convex combination하면 전 구간의 동일 부등식이 나온다. 끝점도 구간에 있으므로

    sup_s eta(s)=max(eta0,eta1),
    exp(alpha dt)<=N(t1)/N(t0)<=exp(beta dt).

Commuting 가정은 없다. 이는 represented ODE의 norm growth 정리이지 physical transition-error bound가 아니다. O=1,D(s)=-2s(1-s)의 nonaffine 반례에서는 endpoint eta=0, midpoint eta=1이다. 유한 노드 값만으로 실제 함수의 affineness를 추정하지 않는다. Binary64 endpoint 계산은 certified=false다.

## 실제 저장자료 재분석

입력71481 bytes, SHA256 565a9ee6d831f5f9e3e69010270f5319aa3328432950efcfda81cfabf325c079. Original extended-precision bytes 보존, complex128 진단만 수행. Kernel precision/tolerance 변경과 source repair는 없다. t_a=hbar/E_h, dt=8.943508956135245 t_a이다.

- hybrid z2의 fixed25D eta=0.6007169417167523 /t_a.
- signed spectrum real extremes=-0.4831184527967166,+0.6007169417167519 /t_a.
- 저장한 metric-normalized witness rate=+0.6007169417167527 /t_a, relative eigen residual=3.21218978042749e-16.
- 같은 자료의 full direct point eta=1.9882948883277214e-14 /t_a. Exact-zero/source enclosure 주장이 아니다.
- dotT를 포함한32회 frame 실험: max eta difference=2.6645352591003757e-15, max covariance gap=1.1751493684537895e-14.

Hybrid는 neutral47x47의 z2 direct 값·미분과 mixed/ionic endpoint 보간을 결합했다. neutral dotO max entry=0.05039674748828803 /t_a이므로 neutral O를 상수로 얼리면서 이 미분을 유지하면 actual derivative가 아니다. Complete neutral endpoints/provider derivative, 전 구간 common rank/subspace가 없어 **전체 HH affine-cell bound를 생성하지 않았다.**

다만 보존된 ionic2x2의 complete endpoints로 정의한 선형 subblock은 실제 계산 가능하다. 최소 endpoint overlap eigenvalue=0.7141697311759605, eta0=0.03680954714134556, eta1=0.011280400639589775 /t_a. 따라서 이 defined subblock의 uniform-eta numerical diagnostic은0.03680954714134556 /t_a이다. Alpha=-0.020444583569093948, beta=+0.03680954714134556 /t_a. Coupled HH 전체 upper bound나 dynamically closed ionic subspace라는 주장은 없다.

유효한 독립 source error bound epsO<1,epsR가 같은 whitening frame에서 주어질 때만 normalized witness q에 대해 eta_true>=max(0,|q|-epsR)/(1+epsO)를 쓸 수 있다. 현 HH의 eps 값은 확보하지 않았고 임의 추정하지 않았다.

## 검증 및 다음 노드

Actual new focused tests33 PASS, error/fail/skip0; py_compile/final replay exit0. 최초 missing-module RED29개와 ionic-field RED1개를 개발증거로 보존했다. 이는 기존 HH 버그 수가 아니다. Wolfram symbolic covariance/generator/norm/projection/affine-Rayleigh 검산은 예상 결과이며 첫 JSON serialization 실패도 보존했다. NCP에서 R31W 재검증은 아직 미수행이다.

다음은 CODEX_HANDOFF_KO.md의 연구용 경량 재현과, 기존 neutral provider 및 실제 미분/공통좌표를 read-only로 찾아 CELL_APPLICABILITY.json을 만드는 것이다. 자료가 없으면 정확한 missing input을 기록하고 종료한다. M3B/native preparation/새 과학 node/trajectory/M5/production/H-skip/main merge는 금지다. Historical audit gap이나 independent reviewer admission을 이 연구가 닫지 않는다.

## 원전과 provenance

[S1] Artacho/O'Regan, PRB95,115155(2017), arXiv:1608.05300v2, DOI10.1103/PhysRevB.95.115155: moving-basis connection과 basis/subspace 구분. https://arxiv.org/abs/1608.05300v2
[S2] Hladik, arXiv:1704.05782v2, DOI10.1007/978-3-319-61753-4_11: linear parametric positivity. 위 complex affine-segment 정리는 별도 직접 유도. https://arxiv.org/abs/1704.05782v2
[S3] Ture/Jang, JPCA128,2871-2882(2024), DOI10.1021/acs.jpca.3c07866, arXiv:2312.01115v2: unitary Magnus propagators. SciSpace 검색과 원전 metadata 교차확인. 구조 보존을 HH 정확도의 증거로 사용하지 않는다. https://arxiv.org/abs/2312.01115v2

Full derivation THEORY_KO.md, raw point witness, Wolfram source/result, RED/GREEN/JUnit, frozen input 및 upstream source manifest는 companion archive에 있다. Git overlay는 full repository mirror나 runtime restore image가 아니다.
