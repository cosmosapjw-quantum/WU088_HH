# HH-PHYS01: near-threshold 광이온화와 HH의 비가산 응답

2026-10-10. 상태: LOCAL_MIXED_RESPONSE_DERIVED_AND_SYMBOLICALLY_CHECKED__FINITE_STEP_REMAINDER_OPEN.

이 문서는 검색용 게시 요약이며, 전체 증명·소스·원 입력·시험·실패·재현 로그는 아래 불변 ZIP에 있다. 원 ENERGY06D/NCP 실행기, native/reference, vendor, 과학 DB, ON06G checkpoint는 변경하지 않았다. Git 요약을 ZIP의 전체 THEORY와 동일 bytes라고 주장하지 않는다.

## 새 물리 결과

동일한 초기 전체 상태에서 z'=F0(z)+lambda H(z)+S B를 사용한다. F0는 원 FT03 H/He 비광자 CI/RR/두 DR/열·팽창 및 기존 photon source를 포함한다. H=(q,0,0,-chi*q,0_photon), q=nH*(1-x)^2*kLCS(T), chi=13.598434599702eV, 추가1/2없음. B는 E*=13.7eV 광자 생성방향, S는 photons/(H s), lambda는 한 LCS provider의 강도다. 원 기체/기존광자 상태는 lambda,S와 독립이고 S=0은 기존 광자를 삭제하는 것이 아니다.

지역 smooth source-stage에서 밀도·에너지·기하를 고정한다. 서명(-+++), proper seconds, w=eV/H, P=photons/H, nH=cm^-3. 컷오프/재배치 경계를 건너지 않는다. 실제 우주론 전체에서 밀도/에너지를 고정한다는 뜻이 아니다.

I_O=O(lambda,S)-O(lambda,0)-O(0,S)+O(0,0)는 두 작용의 비가산성이다. u=1-x, Pi=1+r+x+r(y1+2y2), T=Cw/Pi, C=2eV_erg/(3kB), g=E*-chi, Tgamma=Cg, nu=dlogk/dlogT, Xi=(u/Pi)*nu*(1-Tgamma/T), A=c*nH*sigma(E*)라 두면

    I_x = -lambda*S*A*q*(4+Xi)*delta^3/6 + O(lambda*S*delta^4).

이것은 새 광자와 HH가 각각 만든 이온화를 단순합한 것보다 함께 작용한 이온화가 작아지는 국소 항이다. HH가 이온화를 감소시킨다는 뜻이 아니다. T>Tgamma이면 Xi>0이다. 관련 매끄러움과 물리영역에서 충분히 작은 delta의 부호를 얻지만, 실제 유한 timestep의 remainder나 유효 delta0는 아직 계산하지 않았다.

열 피드백은 다음 정확한 사건방향 미분에 남는다:

    dT/dJphoto=(Tgamma-T)/Pi,
    q_x+g*q_w=-2*nH*u*k+nH*u^2*k'(T)*(Tgamma-T)/Pi.

이는 u=0에서도 유한하다. 원 selected old_gas에서 T=49489.0775K, Tgamma=785.7450K, Xi=0.1769024684. HH율의 photo 방향 미분에서 열적 억제/중성수소 소모 억제의 크기 비는8.84512%다. source에 기록된 sigma를 재사용했고 새로운 단면적 fit이나 물리 uncertainty를 만들지 않았다.

## 유도와 장부

F=F0+lambda H+SB의 local Taylor에서 mixed delta^2항은 H'B=0이다. cubic항은 H'F0'B와2F0''(B,H)이며 일반 gas-only 비광자 source 도함수는 이 차수에서 구조적으로 소거된다. H/He를 제거하거나 온도를 동결해 얻은 결과가 아니다. 비광자 피드백은 다음 차수와 전체 이력에서 유지되어야 한다.

lambda*S*A*q*delta^3로 나눈 선도 계수:

    JHH: -(2+Xi)/6
    Jphoto: -1/3
    P: +1/3
    w: [chi*(2+Xi)-2g]/6

따라서 I_x=I_JHH+I_Jphoto, I_P=-I_Jphoto, I_w+chi*I_x+E*I_P=0이 leading order에서 정확히 성립한다. 실제 전체 시간장부를 이 식만으로 승인하지 않는다. 온도 혼합항에는 EOS Hessian 교차항도 포함했다.

birth시각 b의 작은 photon mass에 대한 leading local kernel:

    K_HH(b)=-A*q*(2+Xi)*(delta-b)^2/2
    K_photo(b)=-A*q*(delta^2-b^2)/2
    K_x=K_HH+K_photo
    K_x'(b)=A*q*[b+(2+Xi)*(delta-b)]>0 (Xi>=0).

이전 HH의 중성수소 감소를 태어난 광자가 만나므로 K_photo는 단순 (delta-b)^2가 아니다. 끝점 impulse 후 진화0인 연속 연산과, 끝점 birth를 넣고 길이delta BE를 적용하는 owner 수치연산을 동일시하지 않는다. 이것은 all-time certified Green function이 아니다.

같은 frozen-source subproblem에서 I_x/(lambda*S*A*q*delta^3):

    continuous: -(4+Xi)/6
    BE full: -(3+Xi)
    BE two-half: -(13/8+Xi/2)
    two-half minus full: +(11/8+Xi/2).

원 source점에 S=5e-15,delta=1.25e9s,lambda=1을 대입한 선도크기 진단은 각각 -2.0159064e-17,-9.1996470e-17,-4.9617974e-17,+4.2378496e-17이다. finite actual macro prediction/error bound가 아니며 기존 photon/background의 더 낮은 차수 HH defect를 누락해 전체오차로 쓰지 않는다.

## 실제 검산

새 unit12개(실제 assertion RED/GREEN1개, 구현 후11개), 일반 symbolic47, 별도 nonlinear-series/EOS9, causal-kernel8, 실제 저장 old-state 한 점의90자리 산술25개. Five-command fresh reproduction exit0; 네 과학 JSON이 원 출력과 byte동일. Parent6개 input/source는manifest/bytes 확인 후 계승했으며 부모 science를 재실행하지 않았다. 초기 Fraction→mpmath 직렬화 TypeError와 수정 전 원본·로그 보존. 새 native/IVP/비선형근/원자적분/NCP dispatch 모두0. 형식증명기/독립agent심사/전구간 구간상계는 수행하지 않았다.

## 다른 스레드와의 경계

REI718468dc75cb81fdfe0f2792aab5c8d0dbc54607 PHYS19는 HH-OFF 연속 birth C1..C4와 causal feedback이며 이번 HH mixed항의 수치 근거로 전용하지 않았다. HE81c1dacc1439807d41dc2684619dee499f3e06b0 E13C1은6개 frozen photon transaction으로 별도이다. CR58295e59e1c1815832a26769b05a3b5fcb96b47b은 게시된 runbook ref다. 타 owner campaign/물리율/low-temperature gas를 여기로 혼합하지 않는다.

## 코드·데이터 자율 회수

- ZIP: WU088_HH_PHYS01_PHOTO_HH_COMPETITION_20261010_v1_sha_977ac57dc2aa.zip
- bytes71498, entries67, manifest payloads66
- SHA256: 977ac57dc2aadfb15235c6c8e18edd495927ee8f7a68a62592273c7862b4c96c
- Drive ID: 1zEBmBLit6RY2fOa3JssbAv7XqXgeaFkV
- Drive parent: 1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM
- Dropbox ID: id:BSpOijBcT10AAAAAAD3uMg
- Dropbox path: /BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/WU088_HH_PHYS01_PHOTO_HH_COMPETITION_20261010_v1_sha_977ac57dc2aa.zip
- 양쪽 create-only 저장 완료와 ID/name/size/parent-path 확인(R1). 새 원격 전체 복원/bytehash 검증은 수행하지 않았다.

NCP local Codex는 이미 설정된 인증수단과 verified cache를 우선 사용해 위 한 사본을 회수하고 SHA/manifest를 검사하라. ZIP의 HH_PHYS01_20261010_v1/{THEORY_KO.md,CLAIM_LEDGER.json,NCP_LOCAL_CODEX_HANDOFF_KO.md,REPRODUCE_KO.md}를 읽어라. python -B verify_delivery.py는 입력검사이고, python -B reproduce.py --output NEW_EMPTY_DIRECTORY는 위5개 경량 명령을 재현한다. 원 sealed 폴더 내부에 새 로그를 쓰지 않는다.

다음 물리 의무는 실제 matched source의 lambda×birth mixed derivative와 fourth-order remainder를 좁히는 것이다. 기존 directional/energy source의 full/half/root-preconditioner identity를 함께 결속하고, direct binary64 네 이력의 뺄셈만으로1e-17 신호를 검증하지 않는다. source timestep/에너지·가중치/guard를 바꾸거나 coefficient를결과에맞춰조정하지 않는다. 별도 정확 승인 없는 새 heavy native/BE/272·0 dispatch는0으로 유지하고 허용된 구현·경량검산을 수행한다.

HH research ACTIVE, canonical S0 OFFcontrol, legacy24/289·265unbounded·epsilon_C/Rnull·B22OPEN_UNDETERMINED·consumedscopes, ON06G256/t3.2e11, physical/productionHOLD를 보존한다.
