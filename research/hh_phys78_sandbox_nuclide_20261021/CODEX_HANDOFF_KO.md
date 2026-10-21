# PHYS78 Codex handoff

Repository: https://github.com/cosmosapjw-quantum/WU088_HH
Draft PR133: https://github.com/cosmosapjw-quantum/WU088_HH/pull/133
Branch: research/hh-phys78-sandbox-nuclide-pilot-20261021
Actual parent: d43cf2df2c4864ae05049f44301c5b389b80a49c (PR132)
Unit: research/hh_phys78_sandbox_nuclide_20261021
Final remote HEAD: read the actual ref plus the external PHYS78_FINAL_DELIVERY_20261021.json; do not substitute a stale PR snapshot.
Science source manifest SHA256: a0380fdd5cbdd9a1f22f5c09fde67ad0ef85da0ce149e043dec69684b662a6b6

먼저 최신 actual refs, 이 unit의 DAG_OVERLAY.json/FINAL_REPORT_KO.md/EXECUTION_LEDGER.json/delivery, PHYS75 final delivery와 post-publication handoff, PHYS77 DAG, 다음 provider backup의 실제 identity를 확인한다. 접근 불가능한 private conversation까지 전수 확인했다고 쓰지 않는다. PR128/129를 기준/보충 도구로 유지한다. 최신 확인은 inventory/FINAL_HEAD_REFRESH.json.

완료 상태: 이 sandbox에서 31개 z20→2 pilot, 161 epoch/point, 1개 별도 refinement, 10 PNG+10 PDF. 실제 총 ODE34=실패debug2+완료pilot31+고유refinement1. 완료 재실행0, NCP0, benchmark0. 35개 고유 light test PASS. --resume 실제 확인에서31 skip/0new ODE/93case files byte-identical. 기존 HH1231/REI729/HH74control63은 다른 범위이며 replay 금지.

과학 모형: non-tilted LRS; sigma=diag(-s,-s,2s), pi_A=diag(-p_A,-p_A,2p_A), 같은 normal orthonormal frame. Signed matter/radiation을 따로 저장한 다음 tensor sum의 norm. Full Frobenius Σ=sqrt6|s|/H, Π_A=sqrt6 κ_E|p_A|/H²; half contraction은 1/sqrt2. SI proper-second/energy-density convention에서 κ_E=8πG/c². pi_m은 collisionless nonbaryonic DM; reacting gas pi=0, UV/escape radiation pi=0. Species-off causal interpretation 금지; sampled residual→continuum certificate 승격 금지.

21 nuclear/ionic state: H1/D/T I-II, He3/He4 I-III, Li6/Li7 I-IV, n; electron charge-derived. 실제 rate는13PI+13RR. n/Tinitial0; LiIII/IVinitial0 및18/30/60eV광원에서0. 전체19핵반응·molecules·CI/CX·Compton·spectral transport는 OPEN. 주어진 isotope 이외의 모든 단명 핵종을 포함했다고 주장하지 않는다. gas Tmax25370.663K이므로 CI/CX 생략이 무시 가능하다는 주장은 미검증.

저장 결과 점검/그림만 필요하면 unit에서:
```bash
python source/run_pilot.py --output results/pilot --site local --max-workers 3 --preflight
python source/run_pilot.py --output results/pilot --site local --max-workers 3 --resume
python analysis/check_saved_results.py
python source/plot_pilot.py --input results/pilot --output figures
```
Python3.12 + requirements.txt의NumPy2.3.5/SciPy1.17.0/matplotlib3.10.8. Rust/별도컴파일 불필요. vendor atomic tables 포함. 기존완료결과로 실행시 새ODE0. 후처리 새 receipt/그림의시각metadata는변할수있지만 과학source/rawNPZ를변경하지않는다.

다음 선택 DAG는 COLLISIONAL_ATOMIC_AND_THERMAL_CLOSURE. physics단계에서 domain-valid H/He/Li CI/CX rate source·단위·energy loss/escape/detailed balance를 확보하고 현재 gray energy ledger에 맞는 방정식을 유도한다. 그 다음 coding단계에서 source identities를 새로 부여하고 작은 필요 control만 실행한다. LiIII/IV활성화는 LI_HARD_UV_INNER_SHELL_CONTRACT가 선행돼야 한다. 75.64/122.5eV이상광원을 임의로추가하지말고 LiIinner-shell/branching·spectralenergyclosure를닫는다.

자원: sandbox실제8CPU/8GiB; default3one-threadworkers, reserve1CPU/1.5GiB. NCPprofile상한64CPU/128GiB/reserve16GiB; --site ncp --max-workers64는 상한 요청이며 actualcgroup/idle/memory/공유lease가더작게제한한다. 동료process종료금지. 동료가있다는이유만으로중단하지말고가용slot으로진행한다. 완료case를NCP에서재실행할필요없다.

유도/코드/검증/과학실행/게시/백업/DAG를분리한다. actualremoteHEAD에서additivedescendantbranch를만들고draftPR만게시한다. HH_R10=OFF; production admission NOT_ISSUED. 이 handoff 자체가 새로운 admission이 아니다.
