# PHYS72 R1–R10 / C1–C10

Workflow: physmath-research-loop 1.0.0. Fixed unit: actual outgoing Coulomb
Dirichlet Green, original screen, weighted all-angular/all-radial bounds,
orders >=4 and lambda=1. The PHYS71 loop remains complete and reused.

## Theory loop

| Step | Work and evidence | Status at scientific source freeze |
|---|---|---|
| R1 연구 위치·계약 | CONTRACT.json; original Hamiltonian, fixed B/k/E, actual parent and user scope | complete |
| R2 근거·재사용 | DELIVERY/RECOVERY first; post-cutoff reconciliation; PHYS63/69/71 identities | complete |
| R3 주장·전제 정렬 | THEOREM_AND_MODEL_MAP.md defines weighted spaces, outgoing condition, source/Coulomb symbols | complete |
| R4 가설·표현 탐색 | actual Green kernel; shifted radial multiplier and independent Gram-transfer route | complete |
| R5 구성적 유도 | full shifted identity including Coulomb infinity term, screen norm, boundary sandwich, all-order tail | complete |
| R6 독립 검증 | independent Green derivation and operator-composition review; sign/density/adjoint checks | complete |
| R7 판별 검증 | exact arithmetic, Wolfram, four manufactured fields and actual Coulomb point checks | complete |
| R8 결과 판정 | q<1; exact tail; sufficient-radius failure remains undecided, no strong no-go adopted | complete |
| R9 정식 결과·코딩 연결 | theorem-to-code table, Fraction API, D3-plus-tail hash-bound output, Fortran cross-check | complete |
| R10 종료·재개 | successor DAG and reproducible source; final publication/backup closure recorded separately | scientific scope complete; delivery recorded in publication |

## Coding loop

| Step | Work and evidence | Status at scientific source freeze |
|---|---|---|
| C1 목표·baseline | actual Git descendant; byte-locked NPZ/D3/display; acceptance inequalities | complete |
| C2 식–데이터–코드 | exact formula map in theorem document and implementation docstrings | complete |
| C3 수치 설계 | exact Fraction decisions, upward Decimal display, strict contraction, no discretization claim | complete |
| C4 실행 DAG·자원 | independent derivation/intake/code lanes; light local checks; no physical campaign required | complete |
| C5 구현 | bounds.py, third_and_higher.py, native Fortran and create-only runner | complete |
| C6 구현 검증 | 14 final unit tests, 22 independent audit checks, input identity/create-only behavior | complete |
| C7 과학 검증 | actual A0, factors and units; outgoing Green signs; Coulomb boundary flux | complete |
| C8 수치·재현성 | exact authority, recorded native compile and comparisons; failure/version logs retained | complete |
| C9 독립 검토 | code audit plus final integration review; specific findings and closure recorded | complete after cited closure |
| C10 판정·인계 | exact artifacts, NCP commands, DAG; remote and backup ACKs tracked separately | scientific scope complete; delivery recorded in publication |

## Seven distinct state axes

| Axis | Scientific source snapshot | Final closure location |
|---|---|---|
| Derivation | derived, independently checked | theory/ and verification/ |
| Code | implemented | implementation/, native/, ncp_delivery/ |
| Verification | pass_scoped for new code and stated diagnostics | EXECUTION_LEDGER.json |
| Scientific execution | exact bounds executed; physical campaign not needed and not run | verification/ receipts |
| Publication | authorized, queued after final source review | publication/REMOTE_PUBLICATION.json |
| Backup | authorized, queued for frozen source capsule | publication/BACKUP_ACK.json and external DELIVERY |
| DAG | new quantitative exterior nodes complete; physical source nodes open | NEXT_DAG.json |

## Corrections and boundaries

1. Frozen PHYS71 M/PENDING is superseded by the already read external DELIVERY;
   no completion campaign or old numerical run was reopened.
2. Actual parent is PR123, two commits after PR121, preserving its finite-L64
   diagnostic. Earlier status files remain historical snapshots.
3. The absent Rust compiler and failed Rust attachment delivery prompted the
   requested Fortran-first fallback. Initial isolated-compiler link-path failure
   is environmental; the corrected run is recorded separately.
4. Native CLI/result-contract findings do not alter the exact mathematical
   certificate. Their minimal fixes and focused checks are recorded in the
   final integration review before source acceptance.
5. Strong no-go NG1–NG7 adoption is not applicable: this cycle proves a positive
   sufficient bound. Failure of an optional bound is never promoted to no-go.
6. PHYS63, PHYS69 and PHYS71 remain complete; HH_R10 remains OFF. No change to
   project-wide policy, original physical target or protected source is made.
