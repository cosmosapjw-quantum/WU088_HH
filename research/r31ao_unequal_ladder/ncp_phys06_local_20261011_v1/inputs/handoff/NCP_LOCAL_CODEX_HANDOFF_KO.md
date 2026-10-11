# WU088_HH PHYS06 — NCP local Codex handoff

이 문서 전체를 NCP local Codex에 전달해 아래 **7개 구현 작업**을 계속한다. 별도 사용자 첨부파일은 필요 없다. PHYS06의 에너지 구조와 uniform implicit-family 충분조건을 현재 NCP v2 source에 연결하고, exporter·data adapter·interval validator를 구현한다. 이번 실행에서 actual native endpoint, point solver, nonlinear root, IVP 예산은 모두 **0**이다. 실제 root/tube, W, finite interaction 및 continuous error는 아직 null이다.

## 1. 첨부 없이 입력을 복구하는 방법

Repository는 `cosmosapjw-quantum/WU088_HH`다. PHYS06 publication branch와 directory는 다음과 같다.

- Branch: `research/hh-phys06-energy-uniform-mixed-20261011`
- Directory: `research/r31ao_unequal_ladder/hh_phys06_energy_uniform_mixed_20261011_v1/`
- Detached receipt: `WU088_HH_PHYS06_DELIVERY_RECEIPT_20261011_v1.json`
- Git delivery directory: `research/r31ao_unequal_ladder/hh_phys06_energy_uniform_mixed_20261011_v1_delivery/` (receipt와 backup 시작 안내가 이곳에 있다.)
- Google Drive backup folder ID: `1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM`
- Dropbox backup folder: `/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928`

이미 설정된 Git·Drive·Dropbox 접근 또는 동일 SHA cache에서 receipt를 읽는다. Receipt의 `publication.commit`, `publication.tree`, `archive.name`, `archive.bytes`, `archive.sha256`, `archive.manifest_sha256`, `backups.drive.object_id`, `backups.dropbox.path`가 실제 복구 identity다. 이 파일의 field 이름을 hash나 commit 값으로 해석하지 않는다. Branch tip이 나중에 이동해도 receipt가 가리키는 commit의 위 directory를 사용한다. ZIP을 사용하면 bytes/SHA 및 내부 manifest를 확인한다. 실제 복구에 사용한 경로·receipt SHA·commit·ZIP identity를 기록한다.

복구된 directory에서 다음을 먼저 읽는다: `SCIENTIFIC_CONTRACT.md`, `REPORT_KO.md`, `CLAIM_LEDGER.json`, `theory/ENERGY_COORDINATE_KO.md`, `theory/UNIFORM_MIXED_RECTANGLE_KO.md`, `src/uniform_mixed.py`, `inputs/ncp_v2/COMMIT_IDENTITY.json`, `inputs/ncp_v2/ROOT_PRECONDITIONER_BINDING.json`, `inputs/ncp_v2/SOURCE_INTAKE_KO.md`, `handoff/NCP_TASKS.json`. 현재 프로젝트의 `AGENTS.md`와 `harness/HARNESS_SELECTION.json`을 적용한다. 이미 검사된 Astra v4 research/coding ZIP 두 개가 `harness/`에 포함되어 있으므로 새 첨부나 하네스 패키지 검사 재실행을 요구하지 않는다. 실제 local model/runtime identity는 별도로 기록한다.

한 backup 경로가 불가하면 동일 identity의 다른 경로/cache를 사용한다. 접근이 모두 막히면 구체적인 누락 identity와 접근 실패를 기록하고 독립적으로 가능한 코드 작업을 완료한다. 누락값을 추정하거나 사용자에게 기존 seed 파일을 다시 첨부하라고 요구하지 않는다.

## 2. 반드시 이어받을 최신 기준선

| 항목 | 고정 identity / 상태 |
|---|---|
| NCP v2 branch | `codex/hh-phys04-ncp-20261011` |
| NCP v2 head | `4b9231a0eff113701e7178ad98624233f387dd15` |
| NCP v2 tree | `10a19c64b17352095ce7874284fb12cc5b8b0e54` |
| NCP v2 core | `892eca446ce23815d103f162dbd71c198a1e6198` |
| NCP v2 directory | `research/r31ao_unequal_ladder/ncp_phys04_local_20261011_v2/` |
| Recorded source SHA256 | `9e6612f19909f1a3f7bd30f205cd0f95608cd745a3682cbd5771734b116708cb` |
| Recorded ABI SHA256 | `efaf8c3103685c391857150b16b332a8732f3b0f6106ea47044c0833eb6d1a45` |
| Recorded binary SHA256 | `2e03e5a0941d6ad29da22b61657b3687a3aa70efbc235de9b58d03bcc1492548` |
| Common seed SHA256 / bytes | `678f967f0d50ad1fff47a73e2e63193429b708246cd84ca8ffc72191c31b522b` / 108416 |
| PHYS05 research head | `4ea15a082f9358e28af35e30a392585f4e4383c9`, PR #34 |
| PHYS04 publication | `36b479d509d28aade8db6c8df6a1f8e9edf1a677` |

위 source/ABI/binary는 **이전 NCP build의 identity**다. 변경 후 binary나 미래 live worker의 attestation으로 재사용하지 않는다. 원 owner `569b04cd71e45756e0fd476aef6643bd9434f4fa`는 계보이며, 현재 v2 변경분을 버리고 그 시점으로 되돌아가지 않는다.

완료되어 증거를 상속할 항목: immutable common seed recovery와 native decode/encode roundtrip, λ/b private same-execution receipt, full FT03/LCS second derivatives 및 signed incoming carry, source-ordered redshift/hat→endpoint birth→grouping→reduced residual, strict fixed-C linear image inclusion, v2 receipt 4개+targeted 4개 검사 및 offline/locked build. 과거 v1 7개 검사와 Decimal100 189-slot oracle도 보존된 결과를 재사용한다. 이들을 새 할 일이나 반복 검사로 만들지 않는다.

공통 seed는 과거 HH ON 이력을 포함한다. λ=0은 **미래 HH strength**, b=0은 **미래 birth**에만 작용한다. 과거 history, old photons, guards, compensation을 0으로 덮거나 ON archive를 OFF로 retag하지 않는다. old gas/photons/guards의 U,V,W를 전부 보존한다. 미분 시 clock, density leaves, fHe, d, energy/provider branch는 고정한다. Archived stored photons와 다음 단계의 pre-BE numerator는 구분한다.

## 3. 구현해야 할 물리와 수학

### A. source에 맞는 에너지 잔차

가스는 `g=(x,y1,y2,w)`이며 w는 eV/H, y1,y2는 helium당 fraction이다.

\[
e=w+\chi_Hx+f\chi_{HeI}y_1+f(\chi_{HeI}+\chi_{HeII})y_2=\ell g,
\quad \xi=Sg,\quad Q=S^{-1}.
\]

χ의 source literals는 `(13.598434599702,24.587389011,54.41776)` eV다. Provider fit cutoffs `(13.60,24.59,54.42)`를 binding energy 대신 넣지 않는다. `SH_HH`의 energy row와 그 gas first/second derivatives는 0이지만, implicit matter mixed response `ell*W`는 일반적으로 0이 아니다.

가장 안전한 source-consistent exporter는 기존 `Phys04DerivativeExport.residual` jet에 **선형 projection `ell*G`를 적용**하는 것이다. 기존 Hessian/carry를 재작성하지 않고 energy value/U/V/W와 변환된 Jacobian/Hessian을 내보낸다. `Atilde=S*A*Q`, `Htilde[u,v]=S*H[Q*u,Q*v]`, `Ctilde=S*C*Q`를 쓴다. 변환된 gas box의 interval hull과 w/T guards는 별도로 유효해야 한다. 좌표 변경이 conditioning을 개선한다고 가정하지 않는다.

현재 source graph에 아래 두 residual을 반드시 보존한다.

\[
\widehat f=\operatorname{exact}(n_{He}^{stored})/\operatorname{exact}(n_H^{stored}),\quad
J_{norm}=(f-\widehat f)[\chi_{HeI}F_{0,y1}+(\chi_{HeI}+\chi_{HeII})F_{0,y2}].
\]

\[
h_{aj}=\mathrm{fl}(E_j-\chi_a),\quad\varepsilon_{aj}=h_{aj}-(E_j-\chi_a),
\quad\delta_j=\sum_a r_{aj}\varepsilon_{aj},\quad
\Psi=\sum_j N_j\delta_j/(1+d\kappa_j).
\]

`ft03_interval.rs` uses stored-density ratio, while photo/energy uses stage.fHe. `phys04_mixed.rs` uses the pre-rounded `ic(E-CHI)` leaf. Thus

\[
Q_0=\ell F_0=-L_{escape}-2Hw+J_{norm},\qquad
R_E=e-e_0+\sum_jE_j(P_j-N_j)-d(Q_0+\Psi)
=\ell G+\sum_jE_jR_{\gamma j}.
\]

Exact photon elimination gives `R_E=ell*G`; this is always the implementation reference. A compact scalar formula must retain `J_norm`, `Psi` and their full total first/mixed derivatives. This is an exact-real lift of the interval source leaves, not bitwise equality of native f64 event sums or `energy()`. Blanket normalization or heat-kernel changes are **outside this task**.

The ideal exact-difference photo Hessian is

\[
\Phi_{gg}=-2d\sum_j E_jN_j\alpha_j\alpha_j^T/(1+d\kappa_j)^3\preceq0.
\]

General pre-rounded leaves add `Psi_gg` from theory equation (10c). On the preserved 33-node input all 17 σ-active HI leaves have ε=0; 19 nonzero ε belong to σ=0 helium channels, and all 99 N·σ·ε are zero. This supports the fixed archived branch only. A generic 100 eV HI leaf has ε=`-1/281474976710656` eV. Preserve `inputs/ncp_v2/SOURCE_DENSITY_LEAF_CORRECTION.json`, both `evidence/archived_energy_photo_leaf_*.json` and `theory/correction_history/` as chronological corrections before final review. Do not rerun these diagnostics to recreate the log.

### B. uniform implicit family → finite parameter rectangle

For actual source residual `G(y,theta)`, choose a common state box `X=yc+[-r,r]`, parameter rectangle `Theta`, and **fixed point matrix C**. Source bounds must cover all `X×Theta`, including transported incoming jets; a center sample, four corners, or `Domain` boolean is insufficient.

\[
B=\operatorname{mag}(I-C[A]),\quad
\beta=\operatorname{mag}(C[G(y_c,\Theta)]),\quad
\beta+Br<r,\quad q=\max_i(Br)_i/r_i<1.
\]

Together with C2 source regularity on an open domain, all physical/denominator guards, and correct uniform enclosures, these imply a unique C2 root in X for each theta. Uniqueness is confined to X. New validators must expose beta, B, radii, q, strict margins, interval rounding provenance and all remaining assumptions.

\[
AU=-G_\lambda,\qquad AV=-G_b,
\]
\[
AW=-(G_{\lambda b}+G_{y\lambda}V+G_{yb}U+G_{yy}[U,V]).
\]

All partials use the same incoming family and source. In particular, old incoming U,V,W and mixed photon quotient derivatives are not discarded. Signed tangents at a zero primal stock are valid algebraic inputs; they do not by themselves establish a positive two-sided physical family. Never divide by N to form derivatives.

Once a **source-bound uniform W enclosure** exists,

\[
I=y(\lambda_1,b_1)-y(\lambda_1,b_0)-y(\lambda_0,b_1)+y(\lambda_0,b_0)
=\int_\Theta W\,d\lambda\,db\in |\Theta|[W].
\]

No parameter Taylor remainder is needed for that identity. Time discretization remainder and continuous source-law error remain independent missing quantities. For a nonlinear observable include `O_g W+O_gg[U,V]` and any explicit parameter terms. Energy is linear, so use `ell*W`.

For correlated full versus two-half families at the same terminal time,

\[
A_T\Delta W=\Delta f-\Delta A\,W_F,
\qquad \Delta W=W_T-W_F.
\]

Bind both sides to the same physical seed, Theta, terminal time and paired source data; never infer a small Δ from unrelated enclosures. Reference `src/uniform_mixed.py` implements exact Fraction arithmetic only. Its `Domain`, `RootArithmetic`, flags and manufactured fixtures are not native source authority or a nonlinear root solver.

## 4. 실행 작업 7개

| ID | 코드 작업과 완료 기준 |
|---|---|
| T01 | 위 identities를 intake하고 사용자 작업을 보호하는 isolated worktree/새 branch `codex/hh-phys06-ncp-20261011`를 만든다. 새 NCP output directory `research/r31ao_unequal_ladder/ncp_phys06_local_20261011_v1/`에 최신 v2 baseline을 연결하고 additive diff를 기록한다. 이전 archive/receipt script는 보존한다. |
| T02 | 기존 `phys04_reduced_residual`/`Phys04DerivativeExport` jet을 소비하는 energy exporter와 S/Q 변환을 구현한다. `ell*G` 및 J_norm/Psi metadata와 derivatives를 내보내며, denominator/temperature/helium guards를 유지한다. Native endpoint나 추가 RHS call을 숨겨 넣지 않는다. 필요한 arithmetic call 수는 분리해 센다. |
| T03 | `CommonFamily`, `Phys04PreBE`, `BoundDerivatives`를 잇는 uniform-enclosure data adapter를 구현한다. X, Theta, center residual bound, A 및 모든 mixed partials, fixed C, source/seed/clock/density/leaf/transport identity와 domain evidence를 구조화한다. 실제 producer가 없는 항목은 typed unresolved로 둔다. 기존 private permit/same-execution receipt를 우회하는 public constructor를 만들지 않는다. |
| T04 | outward interval arithmetic으로 uniform strict inclusion/contraction과 U,V,W linear enclosure validators를 구현한다. 기존 strict fixed-C linear image 검증을 재사용할 수 있다. 조건부 arithmetic result와 trusted native certificate type을 분리한다. 참인 hash/boolean/JSON만으로 native authority를 발급하지 않는다. |
| T05 | whole-rectangle coverage를 확인하는 finite-I, observable 및 paired ΔW adapter를 구현한다. 불일치 source/family/time/Theta, point-only coverage를 거부한다. Actual source tube가 없는 지금은 native physical outputs를 null로 반환한다. |
| T06 | 변경된 코드만 대상으로 아래 6개 nonnative targeted test를 만들고 bounded build/check를 한다. 기존 complete suite는 재실행하지 않는다. First failure와 targeted repair/recheck를 시간순으로 남긴다. |
| T07 | 변경 이론/코드의 독립 focused review 1회를 받고 실제 결함만 고친다. additive commit, 정확한 return/manifest와 로그, 두 기존 backup의 create-only 사본·실제 ACK를 남긴다. `NCP_RETURN_TEMPLATE.json`을 채우고 현재 blocker 및 실행하지 않은 다음 proposal 하나를 반환한다. |

T06의 새 test names는 **TO_CREATE**이며 현재 존재하는 CLI/검사라고 가정하지 않는다.

1. `energy_source_projection`: exact synthetic jets에서 ell*G, full mixed photon derivatives, J_norm 및 nonzero heat defect를 검증한다. 기존 actual archived diagnostic 재실행은 하지 않는다.
2. `uniform_contract_binding`: 전체 X×Theta 계약과 source/clock/carry binding을 검사하고 point-only/boolean authority를 거부한다.
3. `uniform_strict_margins`: q≥1, 비엄격 inclusion, r≤0, variable-C 주장, invalid D/physical domain을 거부한다.
4. `mixed_incoming_chain`: 알려진 manufactured implicit family에서 old-stock U/V/W 및 zero-stock signed tangent chain rule을 확인한다.
5. `finite_observable_coverage`: whole-rectangle integration과 nonlinear observable Hessian 항, coverage mismatch를 확인한다.
6. `paired_difference_binding`: analytic paired witness의 Δf−ΔA W_F 및 same-family/time 거부조건, native counters 무변화를 확인한다.

사용 가능한 NCP toolchain에서만 build한다. PHYS06 ChatGPT host에는 Rust build를 했다는 증거가 없다. 원 reference tests, 하네스 패키지 tests, 18,817 PHYS05 checks, PHYS04 remap/quartic, 189-slot oracle, FD1/FD2/6-cell/G256, 기존 receipt tests는 상속하며 반복하지 않는다.

## 5. 예산과 중단 기준

| 작업 | 이번 ceiling |
|---|---|
| Native endpoint / conservative point / certificate-internal point / root / IVP / heavy atomic | 각각 0 |
| Nonnative 새 targeted tests | 6개 target, 순차 1 worker; target invocation당 wall 30 s, address space 256 MiB, output 8 MiB |
| 좁은 변경 코드 build | offline/locked, `CARGO_BUILD_JOBS=1`; wall 120 s, memory 512 MiB, swap 0, CPU 100%, output 32 MiB, 동시 1 |
| 반복 | 최초 bounded invocation 뒤 실제 결함 하나에 대한 targeted repair/recheck만 허용; 무변경 rerun·sweep 0 |
| Native authorization / authority issuer | null / missing |

빌드/각 target의 실제 command, UTC start/end, elapsed, exit, stdout/stderr, resource limits, measured counters를 저장한다. 측정하지 않은 count는 null이며 예산 0과 혼동하지 않는다. 전송/환경 실패와 계산 실패, 후보 유도 수정은 구분하되 최초 기록을 삭제하거나 PASS로 덮지 않는다. 같은 원인 무한 재시도나 새 gate만 늘리는 작업은 하지 않는다.

현재 실행하지 않을 future proposal은 inherited ceiling 그대로 보존한다: 한 macro, 4 corners `(0,0),(0,1),(1,0),(1,1)`, t0=`1.6e11 s`, full d=`1.25e9 s`, half d=`6.25e8 s`; full/half1/half2 합계 endpoint 최대 12. Conservative point, certificate-internal point, root는 각각 별도 최대 12다. Receipt를 위한 extra endpoint/root는 0. Root internal max attempts 24, point max iterations 200; wall 120 s, memory 512 MiB, swap 0, CPU 100%, output 32 MiB, concurrency 1, retry 0. **이 숫자는 지금 쓸 예산이나 uniform tube 증거가 아니다.** `request_ready=false`, authorization=null이다.

남은 구체적 전제: 실제 CommonFamily→trusted amplitude producer 연결, private `Phys04ExactPermit` issuer와 독립 exact authorization, 실제 source-bound uniform enclosure와 root/tube, future live worker의 PID/exe/maps/UID/cgroup/reserve identity. 이번에는 연결 인터페이스와 validators까지 완성하고 실제 root 실행은 하지 않는다.

## 6. 반환할 것

`NCP_TASKS.json`의 T01–T07에 actual status/evidence를 달고, `NCP_RETURN_TEMPLATE.json`에 다음을 채운다: 실제 source/ABI/diff/build identity, energy coefficient graph와 exporter, uniform contract/validator 결과와 남은 premises, 각 새 targeted check의 최초/수정 기록, measured operation counters, actual commit/ZIP/manifest/backup ACK, unresolved blockers 및 실행하지 않은 proposal 하나. Physical actual root, uniform tube, W, finite I, paired scheme defect, continuous error와 gas remainder는 source authority가 없는 한 null이다.

기존 admission `24/289`, unbounded `265`, epsilon_C/R=null, B22 OPEN, canonical S0 HH OFF, ON06G 256-macro prefix through `3.2e11 s`, physical/production HOLD를 유지한다. 회수된 source hash나 이번 validator PASS가 이 상태를 바꾸지 않는다.
