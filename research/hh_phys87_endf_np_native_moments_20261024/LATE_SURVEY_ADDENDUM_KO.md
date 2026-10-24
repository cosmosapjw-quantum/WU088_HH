# PHYS87 최신 병렬 결과 수신 부록 — 2026-10-24 KST

## 범위와 조회 한계

초기 접근 가능한 Git inventory는 51개 repo·2234개 branch/SHA ref·65개 terminal API page다. 이전 inventory 대비 +8 new/+4 changed/0 removed이며, 관련 6개 repo의 초기 최근 PR 60개와 dependency/backup metadata를 실제 수신했다. 이후 2026-10-24 18:17 KST에 같은 관련 6개 repo의 최근 5개 PR씩 30개를 bounded delta로 확인했다. 두 PR 집합은 겹치므로 90개 고유 PR로 합산하지 않는다.

이 부록의 원전 10개는 실제 pinned bytes의 Git blob SHA 10/10 일치를 확인했다. 근거는 `intake/LATE_SOURCE_IDENTITY_READBACK.json`와 외부 ZIP의 private intake다. 최초 8개 GitHub fetch는 정규화한 파일 text를 반환했고 이를 REST base64 metadata로 해석하려던 로컬 parser가 거부했다. 그 뒤 fetch_file base64 원본으로 교정했다. 이는 과학 실행 실패가 아니며 해당 transport note를 보존한다.

다른 비공개 대화 조회는 UNAVAILABLE이다. Drive의 일부 범주는 cap/무cursor이므로 전 계정 완전성은 입증하지 못했다. Dropbox terminal page metadata 조사와 모든 backup archive 원본의 전체 복원도 구별한다. 실제 전체 복원 완료는 PHYS86 completion receipt와 이번 PHYS87 FINAL receipt에 명시한 객체에 한정한다.

## 수신 결과와 이번 계약에 미치는 영향

| 담당 결과 | 실제 최신 수신 pin | 수신 판정 | PHYS87에 적용하는 경계 |
|---|---|---|---|
| HE PR97 PWBE | final e3b2f786c7597ffa65aa6439194e7cbcae6103e7; science db91cbd3ac0f4db7908cd69c1f40e961f81051f9 | DERIVED_PWBE_MODEL_INPUT_AVAILABLE, PASS_SCOPED_SCIENCE_PRESENTATION_OPEN | exact-swapped first-Born fixed-proton H1s의 pointwise joint TDCS/조건부 상대 방위각 모형이 실제 존재한다. physical/calibrated provider·recoil·full support·consumer는 OPEN |
| REC PR133 | final c5394eccf6ff45f134e396c549844af91988aeb7; science c166b146e32fedb9e4b76e98f5f058a27d3b5e57 | 과학은 재사용, 이후 2 commits/40 files는 문서·delivery·provenance | finer h4/h2 데이터는 존재하지만 실제 목표 source-pair의 history coverage와 cosmology/frame/domain/error 계약은 별도 |
| BASS PR187 B3b2 | final 0a088e1f8fca6618107525e687f930406ca32d18; science 03101fd962ad2ce81195a2fcd3fae57834c80bd6 | 35 cells ×26 directions=910 massless packets의 stock N/T·inverse·boost covariance PASS_SCOPED | Bianchi-II builder의 INITIAL-DATA이며 LRS Bianchi-I physical history 또는 capture-photon source-rate consumer로 자동 채택하지 않는다 |
| REI HI pressure | central 79c042a15e7e29b894dadc32188e286dade73aad; admission blob9a9f30df2c1df7023b872a0fb126d75175a9e6f1 | ADMITTED_SCOPED_FINITE_POSITIVE_MEASURE_PRESSURE | 새 exact Fraction fixture의 분석·수치 근거는 존재한다. 특정 physical HI stock/EOS/history/stopping/L4를 닫지 않는다 |
| REI Bianchi stock bounds | 같은 central pin; decision blobb27e7f311a019aa9aab30db0d7c3aa5a49fc2f5c | 조건부 이론 PASS, code PREPARED_PASS_STATIC_SCOPED, numeric NOT_RUN, proposal NOT_RELEASED | 외부 prescribed C1 diagonal Bianchi-I collisionless massive positive measure의 범위다. 다른 담당자의 미실행 proposal을 이번 예산으로 실행하지 않는다 |

### HE의 식·표현·전달을 분리

독립 unpolarized spin 평균은
\[
\tfrac14|D+X|^2+\tfrac34|D-X|^2=|D|^2+|X|^2-\operatorname{Re}(DX^*)
\]
이다. 원문의 −2DX 식은 보존하되 unpolarized 결과로 채택하지 않았다. 여섯 fixed-geometry closed-v/periodic 검사는 전 각도·에너지 total cross section 적분이 아니다. 따라서 예전 “joint amplitude가 없다”는 표현은 현재 상태로 쓰지 않는다.

최초 14개 method 중 12 PASS/2 false FAIL 뒤 targeted 2 PASS가 있고 전체 14개 재실행은 없었다. 실제 child 4개는 FAIL/PASS/PASS/FAIL, CPU1.966445s·wall2.079161265s다. plot Mathtext 실패를 정적으로 수리했지만 NOT_RERENDERED이며 C8 PARTIAL/19 of20을 유지한다. reserve1은 소진됐고 B1/B2는 양쪽 ACK metadata, pinned head에서 B3 pending이다. 이번 root는 다른 담당자의 그림을 재실행하거나 예산을 이전하지 않는다.

이후 실제 PR97 최종 본문 readback은 18:20 KST의 B3 dual ACK+별도 metadata size 확인을 제시한다. 같은 D HEAD/e3b2f786…의 파일에 남은 PENDING_B3는 당시 snapshot이며 최종 PR receipt가 전달 대기를 해소한다. B3는109576bytes, SHA256 e3e57ec75562bd781154ba803f27733c2e11bd7b3ccbb2458ebe1b43d89c29d8, Drive1hUTrAqqahZfDey5SsnHnbODS96JkoXLM, Dropbox id:BSpOijBcT10AAAAAAD_9cA다. 현재 HE의 R10/C10 전달은 완료이고 C8만 PARTIAL이다. 독립 remote SHA256/전체 GET 복원은 그 receipt에서도 주장하지 않는다. 이 최신 본문 전체는 private intake/phys87_pre_s2_delta/HE97_FINAL_PR_BODY_READBACK.json으로 보존했다.

### REC의 존재·적용·불확도를 분리

수신된 finer grid 및 U4A/U4B/U5 결과를 “데이터 없음”으로 취급하지 않는다. 다만 현재 selected pair의 원래 query coverage0/313, H5 uncalibrated, physical uncertainty/order/M2 null을 보존한다. 원전 refinement 결과를 실제 physical confidence interval로 전환하지 않는다. Dropbox ACK와 Drive UNKNOWN_NO_ACK, repo whitespace CI 실패도 그대로다. 이 계보의 새 science 실행을 PHYS87 실행 수에 넣지 않는다.

### BASS의 stock과 source-rate를 분리

수신된 910-packet stock의 에너지는 E=c×saved momentum_scale이다. geometric centroid를 다시 계산해 에너지를 바꾸지 않는다. 저장 distribution은 scalar unpolarized/isotropic H-frame bootstrap INITIAL-DATA이고 coupled_macro_endpoint=false다. Source/U/J/PiRate는 제공하지 않는다. snapshot Doppler weight n′=Dn와 event-rate invariant measure는 별도이다. native incident trace·finite absorption·exclusive atomic source·coupled IVP는 OPEN이다. 그 담당자의 세 stage ACK는 전체 remote archive restore를 뜻하지 않는다.

### REI의 현재 숫자와 미실행 다음 노드를 분리

Pressure admission은 exact fixture 8/9≤functional≤1, width1/9, half-mixture17/18, NR reference4/3을 채택했다. 실제 child1회 CPU0.044765s·wall0.045155603s, exit0/retry0이다. 초기 조사 당시 pressure NOT_RUN은 역사적 snapshot이며 현재 상태로 반복하지 않는다. 다음 stock proposal은 여전히 numeric NOT_RUN/NOT_RELEASED다. 남은 실행 초는 다른 proposal에 이전하지 않는다.

## 최신 중앙 변경과 PHYS87 결정

이번 수신의 central AGENTS blob은429a5a13ee75b1222bc50627f8d5973d01dd21c4, WU AGENTS는83e41056ef39af8183152f93a32d1285bb1a7f2c다. WU PR144의 실제 S1 HEAD94d3b35bb66df184cf370035f498effbb4534cc6를 재확인했다. 중앙 PR222는 18:29 KST 조회에서 a814dab41a8f3f543dec71cde59f17e0d497fcda로 다시 진행했다. 이는 late source pins를 자동으로 최신 중앙 authority와 같게 만들지 않는다. 실제 중앙 게시 직전 최신 HEAD/AGENTS/DAG를 다시 읽고 WU observation만 additive expected-SHA 변경으로 결속한다.

위 결과는 PHYS87의 동결 ENDF source, atomic AWR/QI, 같은 사건의 Jüttner moments 입력을 바꾸지 않는다. 새 source-native child를 수치 검증 범위로 채택하고 atomic-to-bare remap·source support/covariance·named consumer를 다음 선행 의무로 남긴다. 완료 identity 재실행0, 새 ODE0, rates/stopping 활성화0. HH_R10=OFF, production NOT_ISSUED, 전체 목표 완료율null을 유지한다.

