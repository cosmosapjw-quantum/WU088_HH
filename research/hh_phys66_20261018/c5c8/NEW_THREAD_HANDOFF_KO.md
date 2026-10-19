# WU088_HH 새 대화 재개

$physmath-research-loop로 WU088_HH 연구를 이어가라. 먼저 백업에서 새 실행 결과를 확인하고 GitHub 최신 PR와 대조한다. 이미 완료된 실행을 반복하지 않는다. 매 coherent 단계마다 실제 증명/테스트, 게시, 백업, DAG 상태를 분리해 보고한다.

최신 확인 원격 기준은 PR115 445d82db9c42b4f2f81e4ac1b107dec3b69b3c24, 그 전 PR114 bad80f7729015c84c8dde27f1b1dec3a1f8b2c9f다. PR113의 PHYS64 NCP20(2smoke+18extended)은 완료되어 원본 ZIP d7fa0b50ed803e19dfcec8f781219c03acbd21f8f3ee47fe922754f8fdb5ea79에 보존되어 있다. 이번에149 payload해시,20 성공영수증,18 결과를 실제 읽고 검증했으며 재실행하지 않았다.

원래 모형은 atomic coordinates h=-Delta/2-1/r-(1+1/d)exp(-2d), d=|x-0.7zhat|, B27,k0.7,E49/200Hartree다. 원본 NPZ SHA는 f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d이며 eta=Fy,xi=Fy-phi와 Coulomb etaC=-10/7를 구분한다. HH_R10은 OFF다.

PHYS63: 실제 all-angular real-axis exterior LAP/Poisson/DtN의 질적 존재는 적용 가능한 기존 문헌 정리와 모델 대응으로 확보됐다. 이를 다시 OPEN으로 돌리지 마라. 정량 상수/인증된 수치오차/원래 source-driven 산란율은 별개 미완료다.

PR114: 유한 L<=64/all m, 실제 projected original screen, 전체 r>=27에 대해 ||P(r,t)||²<=Gamma64=32400, a=Gamma delta/2,b=Gamma/4,chi=4ab=1.57464e-14,delta3e-23. 정확한 Born 전체 나머지 <=a chi^N/(1-chi). 수치계수/누락angular 오차를 인증하지 않는다.

PR115: 계수별 방사 cutoff beta1=a theta, beta_n=Gamma sum alpha_j beta_(n-j), alpha_n=Cat_(n-1)b^(n-1)a^n,theta=e^-2(T-27). beta2=a chi theta,beta3=5a chi²theta/4. L64,T65:4.78911917745e-52,7.54113862158e-66,1.48432231489e-79. PR115 정수계수 {1,4,20,104,548}와 로컬 검산계수 {1,1,5/4,13/8,137/64}는 4^n배 차이로 정확히 같다.

이전 대화의 새 C5-C8 구현을 자동 회수한다:
WU088_HH_PHYS66_SOURCE_AND_EVIDENCE_20261018.zip
WU088_HH_PHYS66_ADD_ONLY.patch
PHYS66_DELIVERY_20261018.json
WU088_HH_PHYS66_SHA256SUMS
대화/Library 파일 도구로 이름을 검색하고 실제 접근 가능 파일을 읽는다. 이전 sandbox 링크가 새 스레드에서도 열린다고 가정하지 않는다. 이 세션에서는 GitHub 및 cloud 쓰기 함수가 노출되지 않아 새 C5-C8 push/upload는 BLOCKED/NOT_RUN이다. PR115의 기존 게시와 이번 local verification/코드 개발을 혼동하지 마라. 패키지 접근이 안 되면 BLOCKED_ARTIFACT_ACCESS를 명시하며 소스 없는 실행이나 가짜 복원을 하지 않는다.

새 코드 네 모듈: phys66_radial_budget,phys66_campaign_ledger,phys66_endpoint,phys66_campaign. 새 실행기 scripts/phys66_ncp.py는 이미 완성됐고 direct host,smoke2,longtail6(L28/64,T55/65/75),메모리/timeout,BLAS1,nice10,source/runtime hash resume,raw results와 내부 ZIP검증을 제공한다. 먼저 CODEX_HANDOFF_PROMPT.md와 REPORT_KO.md 및 최종 DELIVERY를 읽어 실제 검증 횟수·해시를 확인한다. 오래된 로컬 PHYS65 PROOF.md를 PR114/115 위에 덮지 않는다. 새add-only patch는 remote PR115의6개 경로와 겹치지 않게 구성했다.

실제 수행: 새로운 L28,T65,m0 sandbox pilot, 독립 coefficient quadrature 비교, source/config/hash-safe smoke2, resume2 with0new. 새 NCP longtail6은 아직 NOT_RUN. 전체 과거 original WU suite가 아니라 복원된 selected 회귀와 새tests를 실행했다. 첫RED실패와 원본실패영수증을 보존했다. arbitrary error=0 입력으로 total certification을 켤 수 없도록 했다.

다음 coherent 범위: 실제 새 longtail 결과가 있으면 먼저 읽어서 연구에 활용한다. 없다면 여기서 가능한 코드·수치 검증 후 완성된 runner를 NCP로 넘긴다. NCP에 solver 설계를 전가하지 않는다. numerical ODE/Coulomb/angular/quadrature/roundoff certificate와 finite-L 바깥angular bound, interior source/regular origin/incoming adjoint가 다음 과학 의무다. 다음 단계도 문서만 반복 갱신하지 말고 실제 유도·코드·검산을 산출한다.
