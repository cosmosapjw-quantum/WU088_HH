# WU088_HH PHYS04 → NCP local Codex 실행 프롬프트

이 문서 전체를 NCP host의 local Codex에 전달한다. 현재 사용자가 요청한 작업은 PHYS04 연구 결과의 실제 source 이식, 가능한 코드·build·선택 검증, 그리고 정확한 다음 실행 계약의 완성이다. 아래 지시를 읽은 뒤 계획만 반환하지 말고, 현재 승인 안의 구현과 검증을 끝까지 수행하라.

## 0. 목표, 근거와 실행 경계

너는 WU088_HH의 NCP host-local 구현 담당자다. 이 저장소에서 NCP는 cloud host/local Codex 실행 lane이며 nonlinear complementarity problem의 뜻이 아니다. 현재 HH kernel은 photon을 제거한 backward-Euler equality residual 및 interval/Krawczyk 인증을 사용한다.

PHYS04의 source-ordered mixed quartic, opacity 가중 remap 결함, reduced-BE 혼합 감도 reference를 실제 owner의 FT03/LCS 및 H/He thermal source에 연결하라. 첫 구체적 수정은 receipt 생성 중 중복 endpoint 실행의 제거다. 그 다음 공통 초기 physical state에서의 실제 \((\lambda,b)\) family, old gas/photon \(U,V,W\) 운반, source-bound interval derivative exporter를 구현하라.

이미 승인된 범위는 source reading, 새 isolated worktree/sidecar, 비파괴 코드 구현, build, 경량 targeted synthetic checks, 필요한 기존 기록 분석, 문서·상태·Git 추가형 게시와 기존 지정 위치의 create-only 이중백업이다. Actual native science dispatch, native BE root, 새 macro, legacy atomic integral의 현재 실행예산은 모두 0이다. 이 인계문은 그 예산이나 consumed scope를 변경하지 않는다. 새 과학 실행이 필요해지면 아래 선행 작업을 먼저 완료하고 구체적인 제안 한 건을 최종 반환하라.

모델은 NCP 실행 시 호스트가 제공하는 현재 metadata와 적용 가능한 physmath-research-loop 라우팅 규칙에 따라 기록하라. 이 패킷은 host label GPT-6 Astra Pro에서 Astra research/coding v4.0.0을 사용했으며 runtime attestation은 없었다. 부모의 모델명을 네 실제 runtime의 증거로 복사하지 말라. 모델 변경만으로 완료된 과학 suite를 다시 실행하지 말라.

## 1. 정확한 intake: 오래된 원본을 되돌리지 말고 새 작업 공간을 만든다

Repository는 cosmosapjw-quantum/WU088_HH다.

| 객체 | 고정 근거 |
|---|---|
| PHYS04가 읽은 owner branch | research/ncp-energy06c-owner-birth-20261009 |
| Owner pin | 569b04cd71e45756e0fd476aef6643bd9434f4fa |
| PHYS03 연구 parent | 93e04c51c682216d9cb662b77a52a5783b15c71f |
| 연구 branch | research/hh-energy06d-birth-tv-20261010 |
| PHYS04 게시 prefix | research/r31ao_unequal_ladder/hh_phys04_ordered_quartic_20261010_v1 |

PHYS04 최종 publication commit, tree, ZIP 이름·크기·SHA-256은 함께 전달된 detached delivery receipt에서 확인하라. 이 패킷 안에 자기 자신을 포함하는 archive SHA나 publication commit를 만들어 채우지 말라. Receipt의 Git commit에서 prefix와 manifest를 읽고, 정확한 새 패킷과 독립 최종 판정의 포인터를 확인하라. Source 조사 시점의 연구 parent93e04…를 PHYS04 최종 publication commit로 오인하지 말라.

기존 checkout, mutable registry/DB, completed checkpoints, 원본 raw 배열과 ACK를 먼저 읽는다. 실제 경로는 현 host에서 찾고 NCP_PHYS04_REPO 등의 task-specific 변수에 넣는다. HOME, CODEX_HOME 또는 다른 기존 시스템 변수를 덮어쓰지 않는다. 기존 worktree의 변경을 reset/stash/rebase로 정리하지 않는다.

Git refs는 처음 한 번 갱신하고 owner pin과 delta를 기록하라. Owner가 전진했다면 달라진 관련 source만 읽고 새 commit와 보존된 baseline의 관계를 남긴다. 같은 root blocker나 unchanged source의 재감사를 반복하지 않는다. 변경이 이번 derivative/receipt 의미를 바꾸면 새 source identity로 계약을 갱신하되 옛 pin으로 강제 reset하지 않는다.

다음 명령의 경로와 변수는 현재 host에서 확인한 실제 값으로 채운다. 이는 새 worktree를 만드는 intake 예시이며 native 실행 명령이 아니다.

~~~bash
git -C "$NCP_PHYS04_REPO" status --porcelain=v1
git -C "$NCP_PHYS04_REPO" remote get-url origin
git -C "$NCP_PHYS04_REPO" fetch origin research/ncp-energy06c-owner-birth-20261009 research/hh-energy06d-birth-tv-20261010
git -C "$NCP_PHYS04_REPO" rev-parse refs/remotes/origin/research/ncp-energy06c-owner-birth-20261009
git -C "$NCP_PHYS04_REPO" rev-parse refs/remotes/origin/research/hh-energy06d-birth-tv-20261010
git -C "$NCP_PHYS04_REPO" worktree add -b "$NCP_PHYS04_BRANCH" "$NCP_PHYS04_CHECKOUT" "$NCP_PHYS04_OWNER_COMMIT"
~~~

NCP_PHYS04_BRANCH는 기존 이름과 충돌하지 않는 새 codex/hh-phys04-… branch로 정한다. NCP_PHYS04_OWNER_COMMIT은 실제 읽고 기록한 owner commit다. 별도로 회수한 PHYS04 packet은 immutable reference로 두고 source 이식은 새 candidate namespace에서 하라.

Content-addressed cache에 동일 archive SHA가 있으면 재다운로드하지 않는다. 없으면 현지에 이미 승인·설정된 Drive/Dropbox 수단 중 하나로 정확한 객체를 가져온다. 과거 /root 경로가 현재도 있다고 추정하거나 인증정보를 명령·로그·Git에 출력하지 않는다. 원격 접근 불가 시 필요한 누락 파일을 기록하고 독립 구현을 계속한다.

### 반드시 읽을 자료

1. 현재 repo AGENTS.md와 거기서 지정한 source/보존 지침.
2. 이 패킷 SCIENTIFIC_CONTRACT.md, 최종 독립 decision 및 최종 claim 포인터, NCP_TASKS.json, NCP_RETURN_TEMPLATE.json.
3. quartic/PHYS04_ORDERED_QUARTIC_KO.md의 식 (1)–(13), 최종 run_02/EXACT_CHECK.json. Frozen fixture의 근거는 수정된 run_02이며 보존된 run_01을 최종 증거로 사용하지 않는다.
4. REMAP_OPACITY_THEORY_KO.md, results/REMAP_OPACITY_EXACT_V1.json.
5. IMPLICIT_MIXED_THEORY_KO.md, src/implicit_mixed.py, tests/check_implicit_mixed.py, results/IMPLICIT_MIXED_EXACT_V1.json.
6. inputs/source_survey/SOURCE_SURVEY_KO.md, SOURCE_SURVEY.json, SOURCE_LINE_BINDINGS.json의 관련 SS01–SS25.
7. 현재 owner의 ncp_phys01_mixed_contract_20261010_v1 및 ncp_energy06e_certificate_20261010_v1에서 아래 표의 실제 source.

완료된 PHYS01/02/03/04 과학 suite는 intake 자체를 이유로 다시 실행하지 않는다. Manifest 확인은 identity 검사이며 실제 물리·수치 검증과 구분한다.

## 2. 첫 patch: 같은 실행 결과로만 typed receipt를 발급한다

현재 E/src/paired_stage_receipt.rs의 accepted_half1_receipt는 인자로 받은 next/root를 검사하면서 34행에서 actual_full(...,6.25e8)을 다시 호출한다. E는 research/r31ao_unequal_ladder/ncp_energy06e_certificate_20261010_v1이다. 현재는 private permit issuer가 없어 실행되지 않는 잠재적 호출예산 결함이다. [SS16]

다음 구조로 고쳐라.

- 한 authorized endpoint가 반환한 state, point result, root certificate, carry enclosure, source/ABI/control identity, old/preBE/parent identity를 한 private typed returned object에 묶는다.
- Receipt 생성은 이 같은 실행의 객체와 predecessor bytes를 소비한다. Receipt 생성·검사·half2 predecessor resolution의 추가 endpoint/root 호출은 정확히 0이어야 한다.
- 실제 solver 밖에서 arbitrary JSON, caller가 채운 error bar 또는 forged root object만으로 trusted receipt를 발급하지 않는다.
- Source-bound root certificate의 original box와 numerical returned point를 포함하는 carry enclosure를 분리해 보존한다. Point를 포함시키려고 원 proof box를 덮어쓰지 않는다.
- Half2는 accepted half1의 gas4, photons128×33, 모든 interval boxes, guard_N/U, ledger compensation, energy compensation, HH ledger를 그대로 받는다.

새 synthetic endpoint spy 또는 injected test producer로 “반환 1회 → receipt 1회 → resolution”에서 endpoint counter가 증가하지 않음을 검증하라. 이 fixture에서 실제 BE/root를 부르지 말라. 이 검사는 새로 만들 대상이며 기존에 통과한 시험이라고 기록하지 않는다.

호출 수를 다음처럼 구분하라.

1. Top-level endpoint dispatch.
2. Conservative BE point solver.
3. Root certificate 내부 point solver.
4. Root enclosure/certificate producer.
5. Receipt 때문에 추가된 endpoint/root 호출.
6. Synthetic fixture callback 및 source derivative 평가.

현재 hh_stage_root는 hh_stage_step을 내부 호출한다. 따라서 12 endpoint calls와 12 point solves는 같지 않다. 본 작업은 receipt의 중복 실행 제거를 요구하며, 기존 두 point 경로의 임의 합치기를 승인하지 않는다. 추가 최적화를 한다면 원 primal arrays, compensation, root/source identity의 보존을 별도 입증하라. [SS15]

## 3. 공통 초기상태와 과거 HH ledger의 의미를 먼저 닫는다

최초 제안 baseline은 같은 FLRW geometry, \(t_0=1.6\times10^{11}\) s, \(h=1.25\times10^9\) s, \(S_*=5\times10^{-15}\) photons/H/s, 13.7 eV birth, 128×33 grid다. Proposed corners는 \((\lambda,b)=(1,1),(1,0),(0,1),(0,0)\)이다.

공통 원본으로 지정된 historical member1 seed:

- SHA-256: 678f967f0d50ad1fff47a73e2e63193429b708246cd84ca8ffc72191c31b522b
- Size: 108416 bytes
- Historical path: /root/WU088_HH_MASTER_EXEC_20261008/inputs/on06g/HH_ON06G_20261008_v1/seed/member1.bin
- Clock: 160000000000 s.

이 경로는 historical source pointer다. 현재 host의 실재와 SHA/size를 확인하라. Seed가 없으면 재계산하지 말고 missing artifact로 남긴다. Current selected spectrum은 half1 preBE 조립값이며 이 raw common initial checkpoint를 대신하지 않는다. [SS20–SS21]

현재 HhRunIdentity에는 HH mode와 source constants가 들어간다. hh_check는 OFF state의 누적 HH ledger가 0일 것을 요구한다. 따라서 ON seed의 mode를 OFF로 retag하거나 그 검사를 완화하지 말라. [SS08–SS09]

새 family initializer는 다음을 분리해야 한다.

- 모든 코너가 공유하는 초기 physical gas/photon/guard/interval/compensation payload.
- 원 archived checkpoint bytes와 그 mode, 과거 HH events/heat의 provenance.
- 공통 시작시각 이후에 새 family가 적산하는 HH event/heat increment.
- 새 family의 \((\lambda,b)\), fixed θ, source law/shape, clock와 candidate source/ABI identity.

과거 누적 HH events/heat를 미래 \(\lambda=0\) 코너에서 지우지 말라. 필요하면 immutable historical offset과 새 interval increment를 별도 field로 둔다. Family 시작에서 parameter tangent를 0으로 두는 것은 이 선택된 초기 physical payload를 parameter-independent하게 정의했을 때만 허용된다. 이어지는 accepted half에서는 old \(U,V,W\)와 photon/guard derivatives를 그대로 운반한다.

\(b=0\)은 designated future birth만 0으로 만든다. 기존 photon stock, gas, guard, energy/number compensation을 0으로 만들지 않는다. Existing θ=0 tag는 source amplitude b가 아니다. 과거 member0/1 ON/OFF histories를 새 네 코너로 쓰지 않는다.

새 initializer의 synthetic tests는 다른 corner에서도 동일 physical payload와 historical offset을 유지하는지, future increment만 제어하는지 검사하라. 실제 seed가 확보되면 read-only decode/encode 및 common payload identity를 검사할 수 있으나 새 BE evolution은 실행하지 않는다.

## 4. 실제 FT03/LCS callback에 혼합 감도를 연결한다

State는 \(z=(x_{\rm HII},x_{\rm HeII},x_{\rm HeIII},w,P)\), gas \(y=(x,y_1,y_2,w)\)다. \(w\)는 eV/H, \(P\)는 photons/H, 시간은 proper seconds, 밀도는 cm^-3다. \(c,k_B\)를 유지한다. \(\lambda\)는 HH ionization와 연결된 \(-\chi_Hq\)만 곱하고, b는 future birth만 곱한다.

실제 source 순서는 redshift → fixed-grid hat remap → endpoint birth → direction grouping → endpoint density/time의 coupled BE다. Source를 birth map에 넣은 뒤 BE RHS에 다시 더하지 말라. Half2의 density/clock/source weights는 half1 결과 뒤의 시각에서 평가한다. [SS10–SS14]

Gas residual은
\[
G(y;y_0,N,\lambda)=y-y_0-d\bar F(y,N;\lambda)=0,\qquad
P_j=N_j/D_j,\qquad D_j=1+d\kappa_j(y).
\]
\(D_j>0\), fixed branch, gas/thermal domain, invertible \(G_y\)가 필요하다.

Source-bound photon elimination의 mixed derivatives를 그대로 사용하라.
\[
P_a=(N_a-PD_a)/D,\qquad
P_b=(N_b-PD_b)/D,
\]
\[
P_{ab}=(N_{ab}-PD_{ab}-P_aD_b-P_bD_a)/D.
\]
N=0에서도 signed \(N_a,N_b,N_{ab}\)를 운반한다. N 또는 old stock으로 나누거나 signed tangents를 positivity clip하지 않는다. Gas Jacobian/Hessian에 photon denominator의 미분을 빠뜨리지 않는다.

이 패킷 src/implicit_mixed.py의 D2(value,a,b,ab), make_reduced_residual, mixed_at_candidate는 arithmetic reference다. 주어진 candidate에서
\[
A U=-G_a,\qquad A V=-G_b,\qquad A W=-r_{ab},\quad A=G_y
\]
를 계산한다. \(r_{ab}\)에는 old \(y_{0,ab}\), \(N_{ab}\), gas Hessian, gas–photon cross derivative 및 HH \(H_yV\)가 포함된다. Candidate를 root로 찾거나 인증하는 API는 아니다.

실제 production formula를 별도 surrogate로 바꾸지 말고 아래 경로를 연결하라.

아래 original_owner_dependency의 원본 snapshot은 byte-preserved reference로 유지한다. 실제 callback 확장은 새 candidate source overlay에서 구현하고, frozen 원본을 직접 고치지 않는다. Overlay의 수정 source·blob·compiler/ABI identity와 원본 대비 diff를 별도로 바인딩한다. interval_ad.rs는 owner tree의 실제 파일이며 pin569b04…의 Git blob은 93f3abc33af7855719b65b839c01359ce494e2de다. 현재 host에서 그 exact source를 읽은 뒤 derivative/Hessian 구현을 연결하라.

| 실제 owner 경로 | 연결할 내용 |
|---|---|
| E/original_owner_dependency/src/coupled_primary.rs, interval_rhs | FT03 nonphoto, photon denominator, HI/HeI/HeII stoichiometry, excess heat, \(-2Hw\) |
| E/original_owner_dependency/src/hh_primary_extension.rs, hh_rate_jet / hh_interval_source | \(q=n_H(1-x)^2k(T)\), 실제 LCS rate의 first/second gas derivatives와 \((+q,-\chi_Hq)\) |
| E/original_owner_dependency/src/interval_ad.rs | 실제 Jet derivative/Hessian 슬롯과 outward interval arithmetic의 계약 |
| E/src/owner_birth.rs, linked_tangent_stage | 이전 gas/photon forcing, 기존 fixed C inclusion, λ-only 경로를 b/ab로 확장 |
| E/src/owner_birth.rs, remap_lambda_fixed_theta | 모든 signed photon/guard U,V,W 운반 |
| E/original_owner_dependency/src/paired_runtime.rs, source_weights | endpoint source profile 및 실제 fixed θ/clock 연결 |

온도는
\[
T=\frac{2E_{\rm eV}w}{3k_B[1+f_{\rm He}+x+f_{\rm He}(y_1+2y_2)]}
\]
이며 HH rate에는 1/2가 없다. \(n_H(t_1)=10^{-4}\exp[-(h_1+h_2+h_3)t_1]\), \(f_{\rm He}=0.083\), \(\chi_H=13.598434599702\) eV와 HI cutoff13.60 eV를 각각 보존한다. 35000–60000 K의 native HH guard와 원 H/He domain을 임의로 늘리지 말라.

실제 FT03/LCS callback의 경량 derivative 검산은 admissible synthetic states에서 수행하되 실제 dataset trajectory나 root 검증과 구분하라. 독립적인 analytic derivative 또는 충분한 precision의 finite-difference/complex-compatible oracle를 사용하고, 사용 가능한 domain에서 truncation과 cancellation을 구분하라. 출처가 같은 RHS와 상수를 공유하면 그 의존성을 기록한다. Polynomial surrogate만 통과한 결과를 실제 callback 검증이라고 보고하지 말라.

## 5. One-sided remap과 source-ordered quartic

기본 적용은 고정 geometry/step clock/source shape에서 \((\lambda,b)\)만 바꾸는 family다. Knot에서 양쪽 C2 매끄러움을 가정하지 않는다. 현재 FLRW active quotient에서
\[
R_A(h)=I+s(h)L_A,\qquad
s(h)=\frac{1-e^{-Hh}}H,\quad s(h)|_{H=0}=h
\]
가 같은 바로 아래 hat cell 안에서 정확하다. \(R_A=e^{hL_A}\)로 바꾸지 않는다.
\[
R_A(h/2)^2-R_A(h)=s(h/2)^2(L_A^2+HL_A).
\]

전체 raw array의 최저 E=10 eV node는 임의 h>0에서 guard로 즉시 export될 수 있어 \(R(0^+)=I\)가 아니다. Active quotient를 사용할 때는 inactive에서 active로 돌아오지 않고 모든 gas coupling이 0임을 source-bound로 확인한다. Inactive photon·guard number/energy·그 derivatives는 별도 ledger로 보존하라.

Quartic 문서 식 (5)의 \(a_1,\ldots,a_4\), 식 (7)의 extended-clock two-half 합성, 식 (8)의 total mixed derivative를 실제 source tensors에 적용하라. \(a_k\)는 raw \(h^k\) 계수이며 \(k!\)로 나눈 시간도함수라는 규약을 혼동하지 말라. Endpoint density drift는 HH와 opacity에도 들어간다. Old nonzero photons 및 \(U,V,W\)가 있으면 zero-photon 특수식을 전체 결과로 사용하지 않는다.

PHYS04 수치 결과의 용도는 다음과 같다.

- 선택된 preBE spectrum의 pure-remap opacity defect는 two-half minus full이 음수이며 relative 약 -0.23192656 ppm이다. PHYS03의 단일 cutoff column 양수 부호를 전체 spectrum에 확대할 수 없음을 보여준다.
- \(P_0=U_0=V_0=W_0=0\), frozen coefficients와 constant birth의 별도 특수화에서
  \[
  \Delta_L[h^4]W_{{\rm two},x}
  =-\frac q{16}\sum_jA_j(4+\Xi_j)(LB)_j
  \]
  이다. 이 고립된 항과 inherited two-half cubic의 비는 지정 local point에서 약 +5.30495111 ppm이다.
- 두 숫자는 actual total quartic, gas finite error, actual mixed sign, root tolerance의 acceptance target이 아니다. 이를 맞추기 위해 box width, tolerance, cutoff, source 또는 density sampling을 바꾸지 말라.
- B에는 \(S_*\)가 들어간다. 단위 packet으로 만든 coefficient를 보고할 때 실제 source amplitude와 normalization을 분리한다.

## 6. 실제 root·parameter tube와 허용된 구현 범위

Current original owner는 HhMode Off/Lcs91만 구현했고 arbitrary \(\lambda\) family와 b amplitude CLI는 없다. Compile되는 source adapter와 synthetic interval proof를 실제 uniform parameter certificate로 오인하지 말라.

원 residual의 full-chain \(G_y\), gas Hessian와 cross forcing을 원 outward arithmetic으로 export하는 코드를 구현한다. Point root certificate와 whole parameter rectangle \([0,\Lambda]\times[0,B]\) certificate는 다른 타입/claim으로 둔다. Parameter rectangle 위에서 root inclusion, invertibility/contraction, source/clock/initial family identity를 모두 확인해야 finite \(I\)를 적분해 제한할 수 있다.

Fixed C는 원 source에서 정해진 centre Jacobian의 inverse와 그 provenance에 묶는다. 임의의 JSON의 C, radius reset, 원하는 Taylor 부호에 맞춘 tolerance는 사용할 수 없다. \(G_y\)의 point Gaussian elimination이 성공했다고 interval inverse bound나 parameter tube가 닫힌 것으로 처리하지 말라.

현재 예산0 안에서는 다음을 완성할 수 있다.

- Actual FT03/LCS parameter derivative 및 Hessian exporter 코드와 compile.
- Same-execution receipt, common-state initializer, map/tangent carry, identity/refusal 경로.
- 실제 source 구조의 admissible synthetic fixture checks, independent oracle, counterfeit/replay/refusal tests.
- 사용 가능한 과거 root/checkpoint의 read-only intake 및 새 family와 다른 부분의 정확한 분류.
- Future root/tube evaluator와 실행 gate의 준비, 구체적인 missing premise 기록.

Actual native root evaluator나 macro는 호출하지 않는다. Code에 gate를 우회하는 test-only issuer를 production으로 export하지 말라.

## 7. 실제 build·test 진입점

E/src/main.rs의 현재 receipt_contract는 인수와 무관하게 ENERGY06E_SCIENCE_DISPATCH_BLOCKED를 출력하고 exit77이다. 이것이 현재의 정상 fail-closed 상태다. Historical hh_cli.rs는 --hh OFF/LCS/COMPARE 등의 과거 CLI이며 --lambda와 --source-amplitude는 아직 없다. 그런 flag가 이미 존재하는 것처럼 명령을 만들지 말라. [SS04–SS06]

E/cargo/Cargo.toml, owner_runtime.rs, src/main.rs에는 이전 /root/WU088_HH_ENERGY06E_20261010 절대경로가 있다. E/prepare_e.py도 이전 local directories를 가정하는 historical packager다. 새 sidecar에서 generated wrapper만 명시적으로 relocate하고 original_owner_dependency bytes를 보존하라. 새로운 compiler/flags/target/ABI/binary, relocation diff를 기록하라. 기존 global runtime이나 native/reference, vendor/orchestration을 수정하지 않는다.

Relocation된 candidate Cargo.toml이 receipt_contract target을 유지하는 경우 다음은 compile 및 선택된 synthetic receipt regression 명령이다. 기존 completed tests는 변경된 의존성이 있을 때만 실행한다.

~~~bash
cargo check --offline --locked --manifest-path "$NCP_PHYS04_WORK/cargo/Cargo.toml" --bin receipt_contract
cargo test --offline --locked --manifest-path "$NCP_PHYS04_WORK/cargo/Cargo.toml" --bin receipt_contract --no-run
cargo test --offline --locked --manifest-path "$NCP_PHYS04_WORK/cargo/Cargo.toml" --bin receipt_contract energy06e_tests -- --test-threads=1
~~~

Cargo dependency가 local cache에 없으면 global 설치·환경 변경을 자동 수행하지 말고 정확한 결손과 대체 가능한 독립 작업을 기록하라. Rust energy06e_tests는 synthetic receipt tests이며 actual root producer를 실행하지 않는다. Current actual_input_tests는 HH_SEED의 member*.bin이 필요하므로 일반 receipt suite와 분리한다. [SS22–SS24]

P는 research/r31ao_unequal_ladder/ncp_phys01_mixed_contract_20261010_v1이다. Identity validator가 변경된 경우만 기존 selective Python methods를 regression으로 사용할 수 있다.

~~~bash
python3 -B -Werror "$NCP_PHYS04_CHECKOUT/research/r31ao_unequal_ladder/ncp_phys01_mixed_contract_20261010_v1/tests/test_mixed_family.py" MixedFamilyTests.test_all_shared_identity_mutations_rejected MixedFamilyTests.test_missing_and_forged_native_certificate_rejected
~~~

새 target는 NCP_TASKS.json에 TO_CREATE로 표기했다. 다음 이름은 구현 후 새 test module에서 실제 존재를 확인하여 실행할 대상이며, 현재 repo에 이미 있는 명령이나 완료된 시험을 뜻하지 않는다.

- ReceiptNoRedispatch: 같은 실행의 receipt 발급·resolution에서 추가 endpoint/root0.
- CommonStateHistory: physical payload와 past HH ledger 보존, future increments 및 b=0 의미.
- ActualRhsMixedCallbacks: 실제 FT03/LCS callback의 gas/thermal Hessian과 \(\lambda,b\) chain.
- PhotonZeroStockSignedMixed: N=0에서도 signed derivatives를 유지하고 stock으로 나누지 않음.
- OrderedRemapAndGuardChart: 한쪽 hat cells, fixed-node cutoff, guard number/energy와 signed tangents.
- LinkedHalfMixedCarry: 모든 gas/photon \(U,V,W\) 및 compensation의 exact half1→half2 연결.
- RootTubeAuthority: point와 family certificate 분리, source/ABI/C/clock mismatch 거절.
- NativeBudgetRefusal: authorization null 또는 budget0에서 실제 dispatch0, no retry.

최초 실패와 최초 실행 원로그를 보존하고 mathematical/numerical/implementation/runtime/authority/permission 층을 구분하라. 실패 없는 시험을 RED였다고 쓰지 말라. 같은 미수정 실패를 반복하지 말고, 변경의 영향 범위에서만 재검사한다.

## 8. 관측량을 구분해 반환한다

같은 full initial physical family에서 \(\sigma\in\{\mathrm{full},\mathrm{twohalf}\}\)의 출력 vector를 \(Z_h^\sigma(\lambda,b)\)라 하자. 최초 비교는 \(\Lambda=B=1\)이지만 parameter rectangle과 단위는 명시한다.

\[
D_h^\sigma(b)=Z_h^\sigma(\Lambda,b)-Z_h^\sigma(0,b),
\]
\[
I_h^\sigma=D_h^\sigma(B)-D_h^\sigma(0),
\]
\[
\Delta_{\rm HH}(b)=D_h^{\rm twohalf}(b)-D_h^{\rm full}(b),\qquad
\Delta_{\rm mixed}=I_h^{\rm twohalf}-I_h^{\rm full}.
\]
별도 continuous 목표 \(\Phi_h\)와 identity가 맞을 때만
\[
E_{\rm cont}^\sigma(\lambda,b)
=Z_h^\sigma(\lambda,b)-\Phi_h(\lambda,b)
\]
를 보고한다. True continuous source-law/time error는 위 scheme difference와 같지 않다.

각 object의 state components, normalization, units, shared parameter/initial/source identity와 enclosure 종류를 기록하라. 특정 base에서의 W, local Taylor coefficient, unit-packet opacity defect를 finite four-corner I로 채우지 않는다. Actual root/tube/continuous target이 없으면 값은 null과 정확한 missing premise로 둔다.

## 9. Native 실행을 요청해야 하는 경우의 최종 제안

현재 authorization_record=null, exact native budget0이다. 이전 proposal은 같은 baseline에서 최대1 macro, 4 corners, full/half/half 최대12 endpoint calls, concurrency1, retry0이며 wall/memory/live binding이 미정이었다. Proposal은 승인기록이 아니다.

실행이 필요하면 먼저 구현·선택검증·source-bound tube 준비를 끝내고, 다음을 모두 채운 한 건의 정확한 proposal을 반환하라.

- Actual source/ABI/binary, compiler/flags, checkpoint SHA 및 common-state initialization contract.
- \((\lambda,b)\) rectangle와 evaluation schedule, full/half/half ordering, exact time/density/source identities.
- Top-level endpoint와 내부 point/root counts, receipt additional calls0, finite wall/memory/output budget.
- 실제 미래 worker의 PID/exe/maps/loader, 현재 cgroup/UID/reserve 정책과 실행영역.
- 완료된 dependency gates, 미완료된 root premise, stop condition, retries0, 결과 파일과 반환 형식.

Consumed FD1/FD2/6cell 및 ON06G256의 과거 권한을 새 family에 재사용하지 않는다. 실제 새 승인과 live binding이 없으면 proposal에서 멈추고 science dispatch0을 정확히 반환한다. 이때까지의 코드·검증·문서 작업을 누락하지 않는다.

## 10. 완료·게시·반환

NCP_TASKS.json의 DAG와 NCP_RETURN_TEMPLATE.json을 실제 증거로 채워 반환한다. PENDING/null을 완료/값으로 바꿀 때 명령 exit와 파일 identity를 붙인다. Native 실행을 하지 않은 경우 실제 관측량 null과 dispatch0을 유지한다. Reviewer가 candidate 생성 또는 검증 설계에 참여했다면 independent decision reviewer라고 표기하지 않는다.

Local 구현 결과는 새 작업 branch에 additive commit/push하고, source binding·call counters·테스트·한계·다음 최소 실행 제안과 독립 review를 함께 제공하라. Main merge/force push, old branch reset, raw archive/registry overwrite는 하지 않는다. 작업 중 owner HEAD가 또 변한 경우 publish 전에 그 delta와 충돌만 확인한다.

지정된 백업은 Google Drive parent1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM과 기존 Dropbox /BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928 이다. 동일 봉인 archive를 create-only로 올리고 provider ACK, object ID, name/size 및 가능한 checksum을 detached receipt에 기록하라. 성공 ACK와 실제 restore를 구분하고, 선택된 readback tier가 닫히면 같은 콘텐츠를 반복 다운로드하지 않는다. Connector/백업 실패는 science 실패와 분리한다.

Legacy24/289,265 unbounded, epsilon_C/R=null, B22 OPEN, canonical S0 HH OFF control, ON06G256 macros through3.2e11s와 physical/production HOLD는 이번 scoped implementation으로 변경하지 않는다. 최종 반환은 실제 완성한 코드, 유도와 연결, 신규 검증 및 최초 실패, actual 미실행/미해결, 정확한 다음 작업을 자립적으로 설명해야 한다.

