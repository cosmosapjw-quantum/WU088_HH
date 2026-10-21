# PHYS78 Codex handoff

Repository: https://github.com/cosmosapjw-quantum/WU088_HH
Draft PR133: https://github.com/cosmosapjw-quantum/WU088_HH/pull/133
Branch: research/hh-phys78-sandbox-nuclide-pilot-20261021
Actual parent: d43cf2df2c4864ae05049f44301c5b389b80a49c (PR132)
Verified source/results commit: b001e69668b2d2c2557b51830f5f732164b56ce0 (369/369 remote blobs matched)
S2 archive: 0075a86507fc101a48da90c9f3beb86d73740b7ffdf4a842ceae21c2144b71fa; both provider complete-byte/payload restores PASS
Unit: research/hh_phys78_sandbox_nuclide_20261021
Final remote HEAD: read the actual ref plus the external PHYS78_FINAL_DELIVERY_20261021.json; do not substitute a stale PR snapshot.
Science source manifest SHA256: a0380fdd5cbdd9a1f22f5c09fde67ad0ef85da0ce149e043dec69684b662a6b6

먼저 최신 actual refs, 이 unit의 DAG_OVERLAY.json/FINAL_REPORT_KO.md/EXECUTION_LEDGER.json/delivery, PHYS75 final delivery와 post-publication handoff, PHYS77 DAG, 다음 provider backup의 실제 identity를 확인한다. 접근 불가능한 private conversation까지 전수 확인했다고 쓰지 않는다. PR128/129를 기준/보충 도구로 유지한다. 최신 확인은 inventory/FINAL_HEAD_REFRESH.json.

완료 상태: 이 sandbox에서 31개 z20→2 pilot, 161 epoch/point, 1개 별도 refinement, 10 PNG+10 PDF. 실제 총 ODE34=실패debug2+완료pilot31+고유refinement1. 완료 재실행0, NCP0, benchmark0. 35개 고유 light test PASS. --resume 실제 확인에서31 skip/0new ODE/93case files byte-identical. 기존 HH1231/REI729/HH74control63은 다른 범위이며 replay 금지.

과학 모형: non-tilted LRS; sigma=diag(-s,-s,2s), pi_A=diag(-p_A,-p_A,2p_A), 같은 normal orthonormal frame. Signed matter/radiation을 따로 저장한 다음 tensor sum의 norm. Full Frobenius Σ=sqrt6|s|/H, Π_A=sqrt6 κ_E|p_A|/H²; half contraction은 1/sqrt2. SI proper-second/energy-density convention에서 κ_E=8πG/c². pi_m은 collisionless nonbaryonic DM; reacting gas pi=0, UV/escape radiation pi=0. Species-off causal interpretation 금지; sampled residual→continuum certificate 승격 금지.

21 nuclear/ionic state: H1/D/T I-II, He3/He4 I-III, Li6/Li7 I-IV, n; electron charge-derived. 실제 rate는13PI+13RR. n/T initial 0; Li III/IV initial 0 및 18/30/60 eV 광원에서 0. 전체 19 핵반응·molecules·CI/CX·Compton·spectral transport는 OPEN. 주어진 isotope 이외의 모든 단명 핵종을 포함했다고 주장하지 않는다. gas Tmax 25370.663 K이므로 CI/CX 생략이 무시 가능하다는 주장은 미검증.

저장 결과 점검/그림만 필요하면 unit에서:
```bash
python source/run_pilot.py --output results/pilot --site local --max-workers 3 --preflight
python source/run_pilot.py --output results/pilot --site local --max-workers 3 --resume
python analysis/check_saved_results.py
python source/plot_pilot.py --input results/pilot --output figures
```
Python 3.12 + requirements.txt의 NumPy 2.3.5 / SciPy 1.17.0 / matplotlib 3.10.8. Rust/별도 컴파일 불필요. vendor atomic tables 포함. 기존 완료 결과로 실행 시 새 ODE 0. 후처리 새 receipt/그림의 시각 metadata는 변할 수 있지만 과학 source/raw NPZ를 변경하지 않는다.

다음 선택 DAG는 COLLISIONAL_ATOMIC_AND_THERMAL_CLOSURE. physics단계에서 domain-valid H/He/Li CI/CX rate source·단위·energy loss/escape/detailed balance를 확보하고 현재 gray energy ledger에 맞는 방정식을 유도한다. 그 다음 coding단계에서 source identities를 새로 부여하고 작은 필요 control만 실행한다. Li III/IV 활성화에는 LI_HARD_UV_INNER_SHELL_CONTRACT가 선행돼야 한다. 75.64/122.5 eV 이상 광원을 임의로 추가하지 말고 Li I inner-shell/branching과 spectral energy closure를 닫는다.

자원: sandbox 실제 8 CPU/8 GiB; default 3 one-thread workers, reserve 1 CPU/1.5 GiB. NCP profile 상한 64 CPU/128 GiB/reserve 16 GiB; --site ncp --max-workers 64는 상한 요청이며 actual cgroup/idle/memory/공유 lease가 더 작게 제한한다. 동료 process 종료 금지. 동료가 있다는 이유만으로 중단하지 말고 가용 slot으로 진행한다. 완료 case를 NCP에서 재실행할 필요 없다.

유도/코드/검증/과학 실행/게시/백업/DAG를 분리한다. actual remote HEAD에서 additive descendant branch를 만들고 draft PR만 게시한다. HH_R10=OFF; production admission NOT_ISSUED. 이 handoff 자체가 새로운 admission이 아니다.

초기 전하 상태는 HII=2e-4이고 나머지 존재하는 isotope는 neutral로 둔 탐색 초기조건이다. PRIMAT nuclear abundance 표가 z20 이온 분율을 제공한 것은 아니다. 정량적 EOR 해석 전에 RECOMBINATION_TO_Z20_INITIAL_CHARGE_CONTRACT도 닫아야 한다.
