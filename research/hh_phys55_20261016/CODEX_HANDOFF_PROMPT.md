# WU088_HH PHYS55 -> PHYS56 | 외부 Codex 자동연구 재개 프롬프트

이 프롬프트는 그대로 외부 Codex에 복사하여 사용한다. 사용자에게 파일 다운로드, 수동 키 복사, 추가 CLI 명령을 요구하지 말고 기존 repository와 연결된 승인 도구를 활용한다. 실제 권한 없는 우회는 금지한다.

## 1. 정확한 시작 상태

Repository `https://github.com/cosmosapjw-quantum/WU088_HH`.
원래 parent PR #94 HEAD `9a3054487db04feea99ff7d5714398043e15425d` (tree `6722c16f90ea0604263bcfef84ed6b86e0e7a4a6`).
**이번 최신 PHYS55 successor Draft PR**을 먼저 찾아 이 parent 위에 올라간 실체를 확인한다. 상대경로:
`src/wu088_hh/phys55_hybrid_outgoing.py`,
`scripts/phys55_hybrid_outgoing.py`,
`tests/test_phys55_hybrid_outgoing.py`,
`research/hh_phys55_20261016/REPORT_KO.md`,
`research/hh_phys55_20261016/NEXT_DAG.json`, `results/`.

Immutable original:
`research/hh_phys34_20261015/inputs/FROZEN_U_SUBSET.npz`, 1,386 original complex128 samples,
SHA256 `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`.
Hamiltonian (atomic units) `h=-Delta/2-1/r-(1+1/s)exp(-2s)`, `s=|x-(7/10)zhat|`, `k=7/10`.
Original `eta=F y`, `xi=F y-phi`; Coulomb `eta_C=-10/7` is DIFFERENT.

## 2. 먼저 기존 PHYS55의 증명 범위를 확인

이번에 새로 증명한 *unconditional infinite-ell hybrid* lemma:
- `X={g:sum_(ell>=21,m)(ell+1)|g_lm|²<infinity}`.
- 실제 noncentral `Q S Q`는 collar `[20,27]`에서 보존.
- `Lambda_D,TT` is real Hermitian and **`<g,Lambda_D,TT g> >= 9/1000 ||g||_X²`**
  via exact rational bound `delta=||2S||_(r>=20)<10^-12`, one-dimensional
  `a_ell coth(7a_ell)`, monotone `a_ell/(ell+1)`.
- `Z_C` is *central* outgoing Coulomb only for `r>=27`.
  DLMF 33.5(iv)+33.4 imply `z_ell/(ell+1)->-1/27`, so central `Z_C:X->X*`
  bounded; normalized `W^-1/2 Z_C W^-1/2+I/27` compact.
- `M_hybrid=Lambda_D,TT-Z_C` is Fredholm index0 via finite-rank
  compensation and complex Lax-Milgram. Kernel=0 by the exact positive
  outgoing Wronskian current, so **bounded inverse exists for all ell>=21/all m**.

This is NOT the **physical screened exterior**. Do NOT rename the result `Z_S`.
No numerical `||M^-1||` upper is certified. No physical lower trace `g_B`, driven
`xi`, regular origin, incoming adjoint, `sigma(E)` or Maxwellian `k_HH(T)` is supplied.
`rei_bianchi HH_R10=OFF`.

The ChatGPT isolated small-grid results are tests of code, not infinite proof.
Reported new targeted 42/42 PASS in Python3.12/NumPy2.3.5/SciPy1.17/mpmath1.3,
full original WU pytest NOT_RUN due source checkout unavailable. Connected Wolfram
exact rational inequality and recurrence principal-limit checks are separate.

## 3. 수행할 실제 PHYS56 R5 + C5-C8 작업

1. Read actual newest WU PRs, PHYS49–55 original sources, and latest REI/BASS_HE/bass_cr PRs; preserve their distinct source/clock/process ownership. Do not merge historical outputs as physical rates.
2. Verify new `PHYS55` theorem's signs, trace Sobolev duality and Fredholm argument on existing repository. Re-run targeted tests and (if suitable host/time) whole original `pytest`, preserving first failures.
3. Move to original physical exterior `S(s)` for r>=27: construct actual outgoing screened `Z_S` on *all ell/m* with noncentral `P-Q` coupling. Explore the exact resolvent identity for outgoing zero-Dirichlet exterior in appropriate LAP-weighted spaces. Prove or explicitly hold the domain/resolvent mapping before invoking the identity. Do not conflate tiny `sup|2S|` with a small weighted `Z_S-Z_C` norm.
4. Quantitatively compute an interval-correct finite-exception cutoff `L0` for `Re z_ell` and a certified bound for `||M_hybrid^-1||`, possibly using Coulomb continued-fraction intervals, barrier comparison and angular axisymmetry. Never use high-ell f64 imaginary parts as current.
5. Seek `||W^-1/2(Z_S-Z_C)W^-1/2|| < ||M_hybrid^-1||^-1`, or a substitute analytic Fredholm/unique-continuation proof with full physical angular coupling. This is the actual physical PHYS56 admission gate; if incomplete keep the exact lemma OPEN and preserve useful intermediate estimates.
6. Only after screened exterior is justified, solve actual original incoming-driven `xi=Fy-phi`, regular origin, incoming adjoint, `sigma(E)` and thermal identical neutral-H `k_HH(T)`; do not activate `HH_R10` prematurely.

Scientific controls: original H-H frozen source hash; boundary normalization and Coulomb Wronskian; m parity and noncentral coupling; weighted X/X* operator conventions; cutoff and spectral convergence; positivity, phase, energy, exact errors; no ad-hoc tolerance expansion.

## 4. Execution/computing and provenance

Default scope is mathematical theory + sandbox/small numeric. If an actual ready heavy physical batch exists and authorized execution is needed, NCP host `s1a0e5abed09` is known to have 64 CPUs/125GiB and Rust1.99, but check *current* resource competition. The user-authorized desktop SSH, when really on the desktop, is
`ssh -i /home/cosmosapjw/.ssh/ncp_key -o IdentitiesOnly=yes -o BatchMode=yes -o StrictHostKeyChecking=yes root@49.50.142.2 -p 22`.
If already on that NCP, run a new isolated local job directly, no nested SSH. Do not copy or print secrets, stop concurrent jobs or claim NCP results when only sandbox ran. Start with <=8 threads and bounded RAM/time where shared workloads exist.

## 5. Publication and double-backup

Preserve latest branch, main and all other owner worktrees. New additive branch on verified exact HEAD; create Draft PR only after real tests, no force-push or main merge.
At each completed scientific unit generate Git bundle, source capsule including original locked NPZ, logs, results, manifest SHA256, exact next DAG. Write both `dbx:` and `gdrv:` through existing authorized endpoints, independent readback/sha256 and restored bundle verification. If a provider is inaccessible, classify UPLOAD/BACKUP appropriately and retain copies in GitHub and conversation cloud archive; don't invent dual-RESTORE_VERIFIED.

Provide final concise Korean report with source branch+commit+tree+PR, theorem and remaining assumptions, actual measured tests, tested host/toolchain/resource, backup status by provider, and next ready target. Do not recurse into process-only audits. No user follow-up required; maximize actual task completion.
