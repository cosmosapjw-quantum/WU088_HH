# PHYS26_FINITE_MOMENTUM_DIRECT_VERTEX

먼저 README_KO.md, DECISION.json, results/PHYS25_RESULT.json, src/sheldon_model.py 및 report/REPORT_KO.pdf의§3–4를 읽는다. 부모 PHYS24 및 local PHYS23/remote PR56의 차이는 그대로 보존한다.

S65 tagged active-electron product/plane-wave/sudden 모형, CM E/I_Ry∈[1,2], 원 singlet/triplet 퍼텐셜을 유지한다. source I_Ry=13.605693122990eV와 receiver thermal χ=13.598434599702eV를 분리한다. Tagged→대칭적인 배타적 전체사건의 adapter는 σev=2σtag이며 k=<σtag v>. 다른 provider의 normalization은 source를 읽고 별도로 맞춘다.

다음 실제 계산은 C(kappa,R)=(8π)^(−1)∫exp(−r)S(|r−R|)exp(−i kappa·r)d³r의 유한 운동량 angular average다. 원 direct amplitude S/(1+kappa²)²와 C의 interference를 보존한다. 전체 적분은 보고서p5 하단에 있다. C=0에서 원S65, kappa→0에서 이번C0와 문턱 계수비0.662920192699918을 회복한다. 이 비율을 warm near-rate에 일괄 곱하지 않는다.

성공조건: 양의 angular/radial scheme과 truncation bound, 적분 refinement, 원 source 회복과 threshold 회복, corrected near-rate interval. 원 S65의 기존512bin 계산 및 고정 P01 ODE/tangent/비교행렬 검산을 다시 돌리지 않는다. 새 입력이 바꾸는 부분만 계산한다.

물리적 calibration은 독립적 연구 항목이다. Full exchange 및 Coulomb continuum, 동일 채널의 benchmark와 오류근거를 읽는다. H+H− 또는 electron-impact 자료를 neutral free-electron 채널로 전이하지 않는다. 실제 고에너지 tail은 null이며 필요할 때 명시적인 상계 또는 supplier와 연결한다.

PHYS25의 truncated near-only P01 진단은 구간밖 rate=0이라고 따로 정의했다. 전체 H–H 반응률에는 이를 그대로 전이하지 않는다. Native64epsilon 비교는 numerical scale이고 물리적 omission budget은 null이다.

Wolfram+xAct를 실제 사용하고 submitted file identity와 관측 출력을 보존한다. 같은 assistant의 별도 경로를 외부 독립심사라고 부르지 않는다. 성공한 이전 검산을 반복하는 메타루프를 피하고 유한 운동량 vertex를 실제 산출한다. 사용자 승인된 기존 Drive/Dropbox 폴더와 additive draft PR branch에 백업/게시하며 merge·production switch는 하지 않는다.
