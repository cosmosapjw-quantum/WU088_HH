# 다음 대화에서 복사할 prompt — PHYS70 최적화 완료 이후

```text
$physmath-research-loop를 사용해 WU088_HH 연구를 이어가자.
이론/코드/검증/실제 실행/Git 게시/백업/DAG 상태를 분리하고 HH_R10=OFF를 유지하라.
먼저 연관 GitHub와 접근 가능한 모든 백업에서 새 결과를 확인하고, 이미 완료된 실행을 반복하지 마라.

Repository: https://github.com/cosmosapjw-quantum/WU088_HH
현재 PHYS70 branch: research/hh-phys70-structured-optimization-20261020
실제 parent는 PR119 efd1520dfc0643220f729307583ff0bc04b059e9이다.
최신 source commit/metadata HEAD/PR와 ZIP SHA는 최종 PHYS70_DELIVERY_20261020.json 및
research/hh_phys70_20261020/publication/의 실제 ACK를 먼저 읽어 확인하라.

자동 회수 대상:
WU088_HH_PHYS70_SOURCE_AND_EVIDENCE_20261020.zip
WU088_HH_PHYS70_NCP_READY_20261020.zip
PHYS70_DELIVERY_20261020.json
WU088_HH_PHYS70_SHA256SUMS
PHYS70_NEW_THREAD_HANDOFF_20261020.md
접근할 수 없으면 BLOCKED_ARTIFACT_ACCESS를 정확히 명시하고 가짜 복원/실행을 하지 마라.

읽기 순서: 최종 DELIVERY → PHYS70 REPORT_KO.md → theory/PROOF.md →
verification/{INDEPENDENT_REVIEW,PERFORMANCE_REVIEW,ADDITIONAL_EXECUTION_REVIEW}.json →
EXECUTION_LEDGER.json → NEXT_DAG.json → CODEX_HANDOFF_PROMPT.md.

완료한 PHYS70 기여:
- 원래 finite-L HH D2 ODE의 전체 동결 Jacobian에 대한 정확한 블록 shifted inverse.
  L<=64,r>=27,h<=.5에서 oscillator 분모>=17171964889/18225000000>0.94222029569.
- pinned VigilODEa21d573980f66fe02891bd216153443b5352f921 Rodas5P raw-U/tableau/PI 재사용.
- wide1.7.1 ordered j-lane SIMD와 rayon1.12.0 독립 작업 병렬화.
- 같은 binary/host/허용치 L28 18개 적분,31개 총 새 성능 적분은 모두 완료.
  18 paired +12 thread comparison +1 NCP용 runner의 sandbox pilot이다.
  기존 scientific campaign 재실행0, 원격 NCP 제출0.
- solve 구간 중앙값 개선98.7113x/91.1700x. Process-wall은48.0449x/71.6688x.
  rtol3e-10 및3e-12에서 새 stored D2 참 상대오차 상한은1.4728567155626935e-10,
  1.2701532252981296e-12. 이는 해당L28점의 오차 상한이며 uniform integrator certificate가 아니다.
- driver buffer256280→30632bytes; kernel52736bytes별도. RSS 감소는 측정하지 않았다.
- 4독립 trajectory를4worker로 계산한 단일batch2.01778x, 모든 state bits와순서동일.
- Rust 신규13PASS, wrapper최초19PASS+새3개/영향기존2개의 최종표적5PASS.
  distinct35개이며35개전체의단일최종suite를실행한것은아니다.
- pilotRESULTsha0ef41785793d32d47fdb63a7d12828d9d5c2f6e06e3746c65ade85d8ac23be27,
  resume는10개파일SHA/size/mtime변경0,새적분0,파일쓰기0.

Rust1.94.1을 실제 사용했다. 측정binary SHA
303efb12fb6c6169b97440a1224d30730e5194a6230c02d469a13a25b9270c13, GLIBC2.39요구.
NCP의구형glibc에서는제공된lockedsource를현지컴파일한다. Solver설계는완료되어있다.
PHYS70 L64는 사전점검만완료,actualNCP hostUNKNOWN. 신규완료본이없고host가가능하면
완성된REQUEST_L64.json으로진행하라. L28완료pilot/benchmark를반복하지마라.

원래물리:atomic B27,k7/10,E49/200Hartree,shift.7,
h=-Delta/2-1/r-(1+1/d)exp(-2d),d=|x-.7zhat|.
H+=G+iF_C,Z=+u'u^-1,eta_C=-10/7은eta=Fy,xi=Fy-phi와구분.
원본NPZsha f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d.
PHYS63질적all-angularLAP/Poisson/DtN은ESTABLISHED_REUSED로유지.
PHYS69all-angular/all-radialD2(21,20),m0=Z''(0)/2는완료:
(7.01774363281637372857673+3.20016322230539545153550i)e-48 a0^-1,
displayerror<=1.279825889920e-64,originalgoal1e-62PASS.
인증서sha965dc9e3d4a1b40fd7e379629f13480c5a7f30b382aa5b240fd7663b56ae9e29.

PHYS64NCP20,PHYS66기존pilot/smoke,PHYS67certificates,PHYS68L28/oldRust,
PHYS69j29..36/oldnative2,PHYS70완료성능31개를다시실행하지마라.
PHYS66정확한최종993317b1...ZIP은BLOCKED_ARTIFACT_ACCESS_EXACT_FINAL_VERSION이며
이전84c29...또는PHYS69복원본과혼동하지마라.

현재사용자의최적화우선순위는이전D3스케줄만최소수정했다.
기존PHYS70_ALL_ANGULAR_D3_AND_HIGHER_REMAINDER는별도OPEN으로유지한다.
남은실제의무:고차all-angularbound,전체응답의integration/Coulomb/quadrature/roundoff인증,
원래source-drivenxi,원점/incomingadjoint,sigma(E),Maxwelliank_HH(T).
완료된PHYS67–69부분인증을다시OPEN으로돌리지마라.
문서와감사만반복하지말고다음고정범위의실제유도/코드/검증을산출하라.
기존승인범위에서additive draft PR push와create-only백업을실행하고main은merge하지마라.
각단계의게시/백업/DAG를실제영수증으로기록하라.
```

이 파일은 source snapshot에 포함되는 재개 계약이다. 배포된 외부
`PHYS70_NEW_THREAD_HANDOFF_20261020.md`에는 게시 후 실제 반환된 Git HEAD와
ZIP SHA256을 덧붙인다. source commit과 metadata commit을 구분한다.
