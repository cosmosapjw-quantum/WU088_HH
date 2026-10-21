# Codex handoff — PHYS76 완료 이력의 재사용

아래 블록을 새 Codex 세션에 복사한다. 최신 delivery metadata는 PR130의 실제 HEAD에서 읽는다.

~~~text
$physmath-research-loop로 WU088_HH의 PHYS76 이후를 이어가라.
Repo https://github.com/cosmosapjw-quantum/WU088_HH
Draft PR130, branch research/hh-phys76-time-transport-20261021.
Remote parent PR129=b76fd4b5d0dfe4850ebde66a8a10f78402d36c00;
science baseline PR128=92f5ab9dba531ebe05909dcb77d3740d2c68c580.
먼저 실제 PR130 HEAD와 research/hh_phys76_time_transport_20261021/delivery/PHYS76_FINAL_DELIVERY_20261021.json을 확인하고 source_commit와 후속 metadata commit을 구별하라.

완료 상태: 원래1231 longcollisionless z20→4 이력은 재실행0.
원래8상태 endpoint에서 신규 z4→2 tail1231개 완료, 실패0,pending0.
총97표본/case,119407표시상태. Science runner SHA256
959952f9d347bcc515410ef90b3b8dc4b36388ad4bfd2acc2bac356fafd6d97b.
Terminalindex SHA256
62f5d96fd323b1ed60c61f4b51e35ab80eb3498d2800c6c04addc1e5e2483115.
TIME_PACKET.npz SHA256
52c32bd6eb37e124e69f70d4cd6bbebeaceb2766fef760aaa0a9b7bd07763f5d.
완료 queue를 다시 submit하거나 benchmark하지 말라. 분석과그림도 완성되어 있다.

물리: same normal orthonormal frame,
sigma=diag(-s,-s,2s), pi_A=diag(-p_A,-p_A,2p_A),
proper-time K=8piG/c², S=sqrt3*s/H, P_A=sqrt3*K*p_A/H².
Frobenius=sqrt2*abs(signedhalf). Total은 signed tensor합 뒤 norm.
S=S0/I+Jm+Jr은 same-trajectory conditional attribution.
State q=s/href는 deceleration q와 다르다.
Sampled residual과 positivity를 continuum certificate로 승격하지 말라.

DAG: conditional interval transport 정리/코드 및 all-node O(KN) sampled Simpson 완료.
실제 coupled whole-cell alpha,Pm,Pr/residual enclosure와 angular truncation이 남았다.
FULL_NATIVE_COLD_EOR,GENERAL_NON_LRS,HH_PHYSICAL_MATCHED_XI_AND_RATE는 OPEN.
REI213warm729,HH74control63은 다른범위다.
최종 재조회에서 REI214/215 및 BASS177/178 cache/native moments,
REI199의 별도40/56상태 unified z20→2 pilot이 발견되었다.
FINAL_REMOTE_IDENTITY_CHECK.json의 정확한HEAD/state/grid/축을 먼저 대조하라.
다른owner 이력을 합치거나 이미완료한 계산을 반복하지 말라.

우선 다음유효단위: finite-L8 owner의 whole-cell source/residual enclosure를
실제 DAG 하위의무로 잡고 local interval lemma에 공급하라.
또는 REI199 D8 sign-reversal saved-history 분석에 source mapping으로 기여하라.
새물리목표와 원래수용기준을 먼저 고정하고 필요한부분만 검증하라.

HH_R10=OFF, production=NOT_ISSUED. 실제 remote descendant의 additive Draft PR.
64CPU/128GiB는 upper cap이며 실제affinity,cgroup,busy,availableRAM에따라배분.
HH74 LeasePool 공유,BLAS/OpenMP1thread,NCP reserve16GiB,local2worker.
다른process를 종료하지 말라. 이번NCP실행0; Desktop Commander 월간한도 때문에
SSH명령자체 미실행. 현재callable경로와credential을 실제확인하고
가능한연구를계속하되 접속불가를 서버전체불능으로 일반화하지말라.

최종 FULL ZIP을 원본그대로복원하라. archive manifest와code/inputhash를확인한뒤
남은새의무만수행하고 derivation/code/test/science/publish/backup/DAG를분리하라.
PHYS75보충ZIP Dropbox는 이번에byte검증까지복구됨.
PR128의별도 FULL archive 전달공백은 여전히별개다.
~~~

## 복원 후 필요한 경우에만 쓰는 후처리 명령

FULL packet은 repo_payload/research/ 아래 PHYS76, pinned HH74 resources와
PR128 stress_memory/OWNER_LOCK을 포함한다. inputs에는 원래 REI198 tar.gz와
terminal index가 들어 있다. 원본 tar 내부 manifest 검증 기록은 evidence/에 있다.
그림과 분석 출력이 이미 존재하므로 우선 그대로 읽는다.

분석 파일이 실제로 사라졌을 때만, 원래 archive를 별도 restored 경로에 풀고 다음과 같이
새 출력 디렉터리를 지정한다. 기존 complete 경로를 덮어쓰지 않는다.

~~~bash
PHYS76_REPO=/absolute/path/to/unpacked/repo_payload
PHYS76_OWNER=/absolute/path/to/restored/repo_payload/research/rei_bianchi_sigma_pi_pilot_20261021
PHYS76_UNIT="$PHYS76_REPO/research/hh_phys76_time_transport_20261021"

python3 "$PHYS76_UNIT/source/analyze_saved.py" \
  --old-root "$PHYS76_OWNER" \
  --tail-dir "$PHYS76_UNIT/results/tail_z4_z2" \
  --out /absolute/path/to/new_analysis_restore

python3 "$PHYS76_UNIT/source/plot_time.py" \
  --analysis-dir /absolute/path/to/new_analysis_restore \
  --out /absolute/path/to/new_figures_restore

python3 "$PHYS76_UNIT/source/plot_sweep.py" \
  --analysis-dir /absolute/path/to/new_analysis_restore \
  --out /absolute/path/to/new_figures_restore
~~~

이 명령들은 저장 데이터 후처리만 수행한다. 원래 continuation run 명령은 실행 ledger에
보존되어 있으나 새 세션의 기본 실행 지시가 아니다. 원본 절대 경로가 기록된 JSON은
당시 provenance로 유지하고, 함수 인자로 새 복원 root를 전달한다.

## 반환 형식

새 결과에는 실제 source commit/파일 SHA, input/closure/IC/단위 identity,
초기수용기준, 로그와 종료코드, CPU/wall/memory 비용, 첫실패와 수정,
scoped 과학결론, 새DAG, remote draft PR 및 Drive/Dropbox receipt를 포함한다.
제출, 실제 실행, 검증, 게시, 백업 성공을 각각 보고한다.
