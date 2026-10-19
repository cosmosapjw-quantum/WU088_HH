# 새 대화에서 이어갈 프롬프트

$physmath-research-loop 1.0.0과 SciSpace/Exa/Wolfram을 사용해 WU088_HH
연구를 PHYS69 완료 지점부터 이어가라. 관련 GitHub/백업의 새 실행 결과를
먼저 확인하고 완료본을 재실행하지 마라. 가능한 유도·구현·경량검증을
여기서 완성해 additive branch/draft PR로 push하고 create-only
Drive/Dropbox 백업을 수행하라. NCP에는 완성된 실행기만 전달하라.
Rust 접근 가능 시 Rust를 쓰고 접근 불가 시 Fortran으로 계산하라.
유도·코드·검증·실행·Git게시·백업·DAG 상태를 매 단계 분리하라.

Repository: https://github.com/cosmosapjw-quantum/WU088_HH
PHYS69 branch: research/hh-phys69-angular-tail-vigilode-20261019
실제 부모 PR118 metadata HEAD:2a79d961388e4fc71cbc0938f012b08af7ecf14e
부모 tree:3255eff8a21ff4b97880e34312de44281988ea23
PHYS69 science commit/최종metadataHEAD/PR 번호는 새 DELIVERY와 실제
원격 readback을 먼저 읽어 확정하라. 이 prompt가 들어 있는 science
snapshot 이후의 metadata commit을 별도로 구분하라.

먼저 회수·검증할 파일:
- WU088_HH_PHYS69_SOURCE_AND_EVIDENCE_20261019.zip
- PHYS69_DELIVERY_20261019.json 및 WU088_HH_PHYS69_SHA256SUMS
- 연구 경로 research/hh_phys69_20261019/REPORT_KO.md, NEXT_DAG.json,
  theory/PROOF.md, theory/*REVIEW.json, all_angular/CERTIFICATE.json,
  CODEX_HANDOFF_PROMPT.md와 publication/의 실제 영수증.

현재 완료된 과학:
1. PHYS63 all-angular real-axis LAP/Poisson/DtN 질적 존재는
   ESTABLISHED_REUSED다. 다시 OPEN으로 돌리지 마라.
2. PHYS69는 모든 j>=20,r>=27에 대해
   |H_j(t)/H_j(r)| <= (800/189)(j+1)를 증명했다. 이 growing bound와
   PHYS67 E10 angular analyticity를 합해 실제 DtN D2의 entrywise
   excluded-angular bound를 정확히 합했다. uniform Gamma_infinity는 없다.
3. 원래 외부(ell,p,m)=(21,20,0),B27,k7/10,E49/200에서 실제
   all-angular/all-radial D2=Z''(0)/2는
   (7.01774363281637372857673+3.20016322230539545153550i)e-48 a0^-1,
   표시반올림 포함 절대오차<=1.279825889920e-64다. 원래1e-62 목표 PASS.
   all_angular/CERTIFICATE SHA256:
   965dc9e3d4a1b40fd7e379629f13480c5a7f30b382aa5b240fd7663b56ae9e29.
4. PHYS68의 j0..28 완료 결과를 그대로 재사용하고 새 j29..36의
   16쌍/76panel만 각각1회 계산했다. 첫2개2.490811s, resume2재사용+
   74새계산44.967343s. 새 numerical radius3.164889152292244e-71.
   band CERT SHA=e123f084bea390a25162826f306c115d683b7c9fd3157b15967c88814787d0c8.
   raw78JSON ZIP SHA=538e16bb74ff5305584fbe2d42491dda55fdffdde536f9276e038bc48da561f0.
5. 오차는 old numerical + new band numerical + 공통Gamma64/T65 beta2
   한 번 + j>36 angular tail + 표시반올림이다. old full-radial total과
   beta2를 중복하지 마라. 실제 producer와 사후 guard 수정 source는
   각 producer_source/ 및 시험 영수증으로 구분되어 있다.
6. 새 고유 테스트 Python137+Rust7=144 PASS. 두 test fixture 실패와
   각1개 수정검증이 보존됐다. 마감용 전체 재실행은 하지 마라.

VigilODE 적용:
- 조사한 repo:https://github.com/cosmosapjw-quantum/vigilode
- 실제 source:a21d573980f66fe02891bd216153443b5352f921
- benchmark PR71:fa07baf27a37674848d963e30e010d54e4af3f33
- 저장CT2700행과Git CSV동일. measured8a8bd409에서sourcepin까지Rust변경0.
- num-complex0.4.6/gauss-quad0.3.2와 matrix-free RODAS5P U-form,
  analytic JVP/timepartial, tau=65-r,qscale2^80,D2scale2^160 실제 구현.
- Rust1.94.1로 native L28두건 실제완료:883steps4.312258s 및
  2277steps10.309392s. 상대 참오차 상한4.755593436e-11/3.775319802e-13.
  각각 기존 PHYS68 인증서와 exactFraction대조. 전체solver인증은 아니다.
- 초기두build ENOSPC실패는물리적분0으로보존 후복구. 두완료runresume는
  payloadSHA동일,2재사용/새적분0. 반복하지마라. L64native는NOT_RUN.

새 intake:
WU/HE/CR/REI/REC의모든branch목록과최근PR,Library/Drive/Dropbox
관련목록을확인했다. 관찰scope에서WU longtail6/L64새완료영수증은없었다.
provider cap/Dropbox현재WU경로제한은sanitized intake에있으며전체부재나
NCP host부재를뜻하지않는다. PHYS68Drive의옛UNKNOWN은실제객체다운로드로
해소:ID19zKus8f9Z8bIOMmkqd_T8P2d2heOZNMn,6546827bytes,
SHA9843e924955c9a522921d7b3a297e684ea2305fb7ea40be7bc6df55f7156b483.
재업로드하지마라. PHYS66최종993317b1...ZIP/2d08f8da...snapshot는여전히
BLOCKED_ARTIFACT_ACCESS_EXACT_FINAL_VERSION,회수된이전84c29de7과다르다.

원래 물리:
h=-Delta/2-1/r-(1+1/d)exp(-2d), d=|x-0.7zhat|,
atomic B27,k7/10,E49/200Hartree,H+=G+iF,Z=+u'u^-1.
eta=Fy,xi=Fy-phi,eta_C=-10/7을구분한다.
원본 frozen1386complex128 NPZ SHA256:
f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d.
source해시검사는원래source-driven xi를계산한것이아니다.
PR114/115원래proof를덮지마라.HH_R10=OFF.

완료재실행금지:PHYS64NCP20,PHYS66pilot/smoke,PHYS67certificates,
PHYS68L28/기존Rust2건,PHYS69j29..36/VigilODEL28두건.
완료band는읽기검증기로만확인한다. max-new-panels0의run/resume도
CERTIFICATE메타데이터를덮으므로완료디렉터리에사용하지마라.

다음 연구단위 PHYS70:
고정 외부21/20,m0의 all-angular D3 또는 higher-order remainder를
위한 두 중간지수 Green/Volterra 식과 summable angular convolution
경계를 실제 유도하라. growing C_j를 유지하며, 필요시 큰j/반경영역을
나누어 추정을 개선하라. 이미 계산된 D1/D2 profile을 재사용하는 코드로
연결하고범위가고정된새계산을수행하라. 원래source-driven xi,
origin/originalincomingadjoint,sigma(E),Maxwellian k_HH(T)는
각별도OPEN의무다. 문서·감사만반복하지마라.

NCP의PHYS66longtail6,PHYS68validatedL64,PHYS69nativeL64는이미완성된
runner와정확요청이있다. 실제host/backup에서미실행임을확인한경우만
CODEX_HANDOFF_PROMPT.md명령을사용한다. 추가solver설계를NCP에넘기지마라.
