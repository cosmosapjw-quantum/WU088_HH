# PHYS78 최적화 선행 감사 — C1–C4

## 결과

현재 샌드박스에서 끝까지 실행할 수 있는 가장 짧은 경로는 **이미 설치된 NumPy/SciPy를 이용한 작은 결합계**다. 코드/원문은 준비되어 있고 새로운 ODE·benchmark·NCP 실행은 이 감사에서 0회다. 원래 과학적 baseline 또는 production 코드를 변경하지 않았다.

실제 cgroup 한도는 8 CPU, 8 GiB다. 64 CPU/128 GiB는 별도 NCP 자원이며 현재 sandbox 수치로 대체하지 않는다. Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, Matplotlib 3.10.8이 설치되어 있다. rustc/cargo는 PATH에 없지만 Rust 1.94.1 tar가 현재 첨부 디렉터리에 존재한다. 설치하지 않았다. 초기 인계의 `missing` 관찰은 현재 파일 존재로 갱신하며 tar 무결성/실행을 확인했다고 주장하지 않는다.

`ps`는 namespace 관련 library error로 실패했으나 `/proc/*/status` 읽기로 두 Codex 프로세스와 공용 서비스들을 확인했다. 외부 또는 다른 namespace의 작업 부재는 추론하지 않는다. 프로세스 종료·재설정은 하지 않았다.

## 원본 코드 경로

| 경로/owner | 실제 구현 | 현재 재사용 범위 |
|---|---|---|
| REI198 `vendor/canonical_fv.py` | 비음수 고정 canonical momentum packets, finite mass collisionless moments, chunked NumPy diagnostic batch | geometry에 따른 nonbaryonic warm component의 rho/Pperp/Pparallel; 원래 packet 규칙 보존 |
| REI198 `pilot.py`, `component_pilot.py` | finite-L8 even radiation moments, shear/metric 결합; 물질·복사 signed stress 분리 | algebraic/source reference; 기존 1231 이력 재실행 금지 |
| REI217 ACCEL03 `moment_response.py` | owner가 제공한 quadrature arrays에 대한 직접 J2, analytic x/b derivatives | source-independent array interface, Jacobian·local conservation control 후보 |
| REI211 RUN19 `igm_rates.rs` | Grackle3.4.1 exact source literals를 이용한 H/He CI/RR/DR/cooling; prepared-T 재사용 | Python port 시 동일 units/domain/floor/cap 보존 |
| REI211 RUN19 `deuterium_atomic.rs` | threshold-corrected H-equality D approximation, point number/energy RHS | isotope approximation 명시, D charge-exchange와 분리 |
| REI211 RUN19 `deuterium_charge_exchange.rs` | Savin2002 2.7–200000K D/H 교환 | 두 양의 event flux와 signed energy defect 보존 |
| REI210 atomic catalog | Verner96 PI, Voronov97 CI, VF96 RR original author tables | exact pinned data 재사용; 기존 catalog는 coefficient-only이며 자체 network admission이 아님 |

REI210 원본 `photo.dat`, `cfit.dat`, `rec_table1.dat` 세 파일을 exact head `e4c8133288614638792888367ca10b2ded3138ff`에서 받았고 원문 manifest SHA256과 일치했다. `H_HE_LI_COEFFICIENT_INVENTORY.json`은 Z=1,2,3의 여섯 bound-ion transition row를 원문에서 파싱한 것이다. fully stripped ion은 더 위 photo/CI channel이 없고 아래 ion으로의 RR parent가 된다. `rr_toward`의 N은 포획 후 전자 수이며 q+1→q 계수다.

H/He/D를 공통 prepared temperature bundle로 평가할 수 있지만 D fraction을 H fraction과 동치로 없애면 안 된다. 별도 D↔H charge exchange, threshold 차이 및 초기분율이 있기 때문이다. He3/4 또는 Li6/7의 rate 계수 공유도 isotope-specific atomic calculation과 구분한다.

## 실제 범위와 온도 경계

Li I/II/III Voronov CI의 최소온도는 각각 1/4/5 eV(약 11604/46418/58023 K)다. 12000K gas라고 해서 전체 Li CI를 켤 수 없다. 낮은 온도에서 근거 없는 외삽이나 0-rate를 원본 물리처럼 넣지 않는다. PI+RR exploratory closure를 선택하면 CI 제외를 명시적인 물리 근사로 기록한다.

Li I outer-shell PI fit Emax는64.39eV이고 threshold는5.392eV다. 64.39eV를 넘는 hard spectrum에 그대로 외삽할 수 없다. soft UV cutoff를 선택하면 LiII/III ionization threshold(75.64/122.5eV) 위 광자는 없어서 그 photo flux는 정확히 0이다. 높은 charge stage가 초기조건에서0이고 상승반응이 없으면 이후도0이며 이를 새로운 dynamic ionization 증거로 부풀리지 않는다. 높은 charge 초기 seed의 RR evolution은 별도의 조건부 초기값 계산이다.

Scalar charge-state abundances는 그 자체로 anisotropic stress가 아니다. 각 종의 pressure closure를 명시해야 한다. Perfect-fluid baryon species면 pi_species=0이라는 닫힘이 필요하고, nonzero baryon stress를 보고하려면 해당 종의 실제 kinetic/angular state 또는 검증된 pressure moment equation이 필요하다. 기존 0.1Omega_m warm nonbaryonic moment를 H/He/Li baryonic stress로 다시 명명하면 안 된다.

## 선택할 구현 최적화

1. 불변 q², mu², positive packet weights, reference normalization과 radiation coupling matrix를 모델마다 한 번 만든다. 원래24×12 cells, Gauss3는2592 subcell packets이며 작은 contiguous arrays로 충분하다.
2. 고정 spectrum shape가 선택되면 각 photo channel의 Gamma 및 excess-heating 적분을 한 번 계산한다. 시간의존 amplitude만 RHS에서 곱한다. 실제 spectral shape/transport가 변할 때만 다시 평가한다.
3. 공통 온도에서 H/He/D 및 Li 계수들을 벡터로 준비한 후 isotope charge flux assembly에서 재사용한다. 수치표 보간을 먼저 추가할 필요는 없다. 원문 direct 함수의 소수 채널이 먼저 정확하게 연결되어야 한다.
4. isotope×charge fractions와 stoichiometry를 dense 작은 arrays로 두고 `up/down` flux를 이용해 합이 정확히 상쇄되도록 조립한다. isotopes별 conserved nuclei와 global electron neutrality를 출력한다. zero-abundance species는 실제 RHS가 0인 경우에만 구조적으로 제거/복원한다.
5. geometry+thermal+charge+gamma/nu state를 동일 adaptive IVP에 연결한다. Stiffness가 있는 chemistry에는 SciPy Radau 또는 BDF를 사용하고 temperature/energy 및 trace-isotope fractions에 component-wise tolerances를 부여한다. `solve_ivp(vectorized=True)`는 여러 독립 trajectories를 자동 병렬 적분하지 않는다는 점을 유지한다.
6. 독립 sweep cases는 BLAS/OMP 각1thread, 낮은 우선순위의 bounded worker pool로 나눈다. local 기본4workers 이하, reserve1.5GiB/job0.5GiB 정도의 명시 budget에서 실제 cgroup/free-memory/load와 협력 lease를 반영한다. NCP에서는 CPU<=64/RAM<=128GiB와 site reserve16GiB를 별도 적용한다. peer가 있다는 이유만으로 모든 작업을 중단하지 않는다.
7. 진행/완료 case identity와 NPZ+receipt를 원자적으로 저장하고 동일 identity의 COMPLETED 이력은 재사용한다. 오래된 species-off/chemistry-off 이력을 신규 allspecies 실행으로 합산하지 않는다.

이는 연산구조/메모리 설계이며 실측 속도 향상을 주장하지 않는다. 사용자는 상세 benchmark를 요청하지 않았다.

## 최소 acceptance

- signed matter/radiation stress를 같은 orthonormal normal frame에서 저장하고 tensor sum 후 norm 계산; cancellation control 포함.
- half-contraction norm=sqrt(3)|p|, Frobenius=sqrt(6)|p|로 sqrt2 변환을 저장하고 모든 axes/caption에서 동일 규약 사용.
- ion-stage stoichiometry가 isotope nuclei를 보존하며 electron neutrality와 number/thermal energy ledger를 직접 확인.
- 원문 rate units/domain 및 photo-threshold를 확인하고 Li fit Emax 초과를 거절.
- zero radiation anisotropy+zero shear limit, no reaction/constant rates limit 및 선택한 source import/reference 비교.
- 1개 대표 coupled trajectory를 두 tolerance로 비교하거나 적절한 독립 solver로 비교하여 exploratory plot의 numerical stability를 제한된 범위로 점검. 완성된 historical campaigns를 재실행하지 않는다.
- 실제 z20→2 coverage/positivity/finite states를 검사하고 raw curves에서 실제 Σ·Π dynamic range를 읽는다. visualization 때문에 physical tensor를 인위적으로 증폭하지 않는다.
- plots를 실제 렌더링해 axis normalization, signed cancellation, clipped tails, isotope legend와 작은 abundance의 log-scale 가독성을 읽는다.

## 첨부 코드 archive 감사

10/11/12번 묶음은 DAG·자동화·background/high-l harness가 중심이고 filename inventory에는 atomic chemistry implementation 후보가 없다. 14번 `bianchireview87`의 species는 photon/neutrino/CDM/baryon/fluid 공통 carrier이며 `q/rate.py`는 external electron history→Thomson rate 연결이다. 17번 locked Rust core에는 kinetic multipoles·Thomson collision·geometry·EOS dof 코드가 있지만 H/He/Li reaction network를 제공하지 않는다. 15번은 generic/offline vendor package이며 chemistry 증거가 아니다. 모든 archive members를 실행하거나 과거 통합 suite를 재검증하지 않았다. Inventory/selected content audit 결과는 `ARCHIVE_AUDIT.json` 및 archive별 inventory에 저장했다.

## DAG/보존/다음 단계

C1 source identity, C2 code-path mapping, C3 bounded solver/array design, C4 sandbox resource plan을 기록했다. code implementation·targeted verification·new scientific sweep·publication·backup은 부모가 독립 상태로 진행한다. 다음 노드는 physics78의 chemistry/energy/stress closure contract를 입력으로 **새 additive unit의 runnable Python 구현**이다. HH_R10=OFF, production admission 미발급, sampled/finite numerical residual은 continuum certificate가 아니다.

`skill_context_used`: physmath-research-loop1.3.0의 실제 SKILL.md, references/POLICY_INTEGRATION.md, references/CODING_LOOP.md, references/SUBAGENT_MODE.md를 읽었다. C1–C4 읽기 전용 하위업무를 수행했고 bound exploratory computation의 허용과 scientific claim admission의 구분을 적용했다. 루트가 아직 코드 편집 권한을 할당하지 않았으므로 canonical path 수정·ODE 실행은 하지 않았다.
