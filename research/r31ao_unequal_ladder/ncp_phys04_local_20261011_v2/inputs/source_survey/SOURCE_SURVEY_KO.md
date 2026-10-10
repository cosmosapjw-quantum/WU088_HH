# PHYS04 source delta 및 NCP 이식 조사

## 결론과 조사 범위

2026-10-10 13:10 UTC 기준 GitHub authoritative ref를 읽었다. 연구 branch research/hh-energy06d-birth-tv-20261010은 93e04c51c682216d9cb662b77a52a5783b15c71f, actual owner branch research/ncp-energy06c-owner-birth-20261009는 569b04cd71e45756e0fd476aef6643bd9434f4fa다. PHYS03 이후 owner commit delta는 0이다. 이 조사는 source reading과 provenance binding이며 새 과학 검증, BE root, native batch, old suite, remote mutation은 모두 실행하지 않았다.

PHYS03의 immutable source snapshot 11개를 재사용했다. Fresh ref/AGENTS와 NCP 실행·포팅 진입점을 확인하기 위해 문서·추가 소스 28개를 읽고 Git blob identity를 보존했다. Parent 복원 전 일부 짧은 기존 문서를 connector로 읽었으나 science checker를 다시 실행한 것은 아니다. SOURCE_LINE_BINDINGS.json의 SS01–SS25는 실제 UTF-8 source 구간, 정확한 행 범위, source 및 segment SHA-256, Git blob, origin commit를 제공한다.

## NCP의 의미

이 저장소에서 NCP는 c64-g3 cloud host와 그 위의 local Codex 작업 환경명이다. R31S README는 Codex의 역할을 NCP host-local 구현·빌드·bounded benchmark로 명시한다. 설계서는 ncloud-docs 제품자료와 연결한다. Mathematical nonlinear complementarity problem의 약어로 쓰인 근거는 없다. [SS02–SS03]

현재 HH microphysics는 photon을 제거한 coupled backward-Euler equality residual과 interval/Krawczyk 인증을 사용한다. Gas fractions, H/He simplex, 온도, photon sign, hat cell, guard는 허용영역 검사와 piecewise branch를 만든다. Complementarity multiplier나 활성제약 equation을 푸는 구현은 이 읽은 source에 없다. 따라서 PHYS04의 \(G=y_{\rm out}-y_{\rm pre}-dF=0\) 혼합 미분은 fixed branch 및 유효 domain 안의 equality sensitivity로 표현한다. Knot, cutoff, guard crossing에서는 한쪽 도함수·분기 enclosure를 별도로 다룬다. [SS12–SS15]

## 첫 구체적 수정 의무: receipt 발급의 중복 endpoint 실행

ENERGY06E paired_stage_receipt.rs의 accepted_half1_receipt는 private 미래 producer다. 현재 permit issuer는 없으며 과학 dispatch는 차단돼 있다. 그런데 함수의 34행은 next/root를 인자로 받은 뒤 actual_full(...,6.25e8)을 다시 호출하여 checkpoint parity를 검사한다. 이를 그대로 활성화하면 receipt 생성 자체가 추가 endpoint 계산을 유발한다. 이는 관찰된 실행 실패가 아니라 정적 source inspection에서 발견한 잠재적 호출예산 결함이다. [SS16]

Local Codex는 이 부분을 첫 수정으로 처리해야 한다. 같은 authorized endpoint 실행에서 얻은 returned state, root certificate, source/ABI/control identity, old/preBE/parent identity를 하나의 private typed returned object에 결속하고, receipt는 그 object를 소비하도록 바꾼다. Receipt 생성·half2 predecessor resolution 자체의 추가 endpoint 및 root 호출은 0이어야 한다. Arbitrary JSON으로 발급하거나 root field를 caller가 채워 넣는 우회 경로를 만들지 않는다.

호출 수는 top-level endpoint, conservative point solver, certificate 내부 point solve, root enclosure producer를 구분해 기록해야 한다. 현재 hh_stage_root 자체도 hh_stage_step을 내부에서 부른다. 따라서 “12 endpoint calls”를 “12 primitive point solves”와 같다고 보고하면 안 된다. 기존 solver의 이 두 경로를 성능 이유로 통합하려면 반환값의 bit parity, compensations, 원 certificate 생성 계약을 별도로 보존·검증해야 한다. [SS15]

## 실제 초기상태와 네 코너

Archived member1 seed는 이미 존재하며 owner가 다음 identity를 기록했다. [SS20–SS21]

- SHA-256: 678f967f0d50ad1fff47a73e2e63193429b708246cd84ca8ffc72191c31b522b
- bytes: 108416
- time: 160000000000 s
- archival path: /root/WU088_HH_MASTER_EXEC_20261008/inputs/on06g/HH_ON06G_20261008_v1/seed/member1.bin
- grid: 128 directions × 33 energies

이 경로는 이전 host상의 역사적 경로이며 현재 host 존재를 이번 조사에서 확인한 것은 아니다. Local Codex는 content-addressed cache 또는 이미 승인된 backup provider에서 exact bytes를 찾고 확인해야 한다. 없으면 seed 재계산 대신 missing local artifact로 기록하고 독립적인 implementation을 계속한다.

Proposed new family는 동일한 member1 물리 초기상태에서 \((\lambda,S)=(1,5\times10^{-15}),(1,0),(0,5\times10^{-15}),(0,0)\)를 비교한다. \(S=bS_*\)일 때 source amplitude b는 future birth에만 곱한다. 이전 photon stock, gas, guard, compensation을 지우지 않는다. 과거 member0/1 ON/OFF history는 서로 다른 진화 초기조건이므로 새 네 코너를 대신하지 못한다.

중요한 구현 제약이 있다. 원 HhRunIdentity는 mode, source constants를 포함하고 hh_check는 OFF 상태의 누적 HH ledger를 0으로 요구한다. 따라서 ON member1 checkpoint의 mode byte를 OFF로 덮어쓰거나 그 invariant를 풀어서 공통 family를 만들면 안 된다. Archived input의 physical state와 전체 원본 provenance를 보존하는 새로운 family initialization contract를 만들고, run identity 및 새 구간의 HH event increment ledger를 구분해야 한다. 이 계약의 byte identity와 의미 동일성을 각각 검사한다. [SS08–SS09]

현재 native_parameter_source_family_implemented=false, actual_corner_receipts=null이다. Typed accepted half1 producer도 아직 없으며 half2 저장자료는 birth weights-only다. 전체 상태가 없다는 주장과 새 family의 accepted half1 상태가 없다는 주장을 구분해야 한다. [SS17–SS20]

## Source 순서와 미분 대상

원 hh_source_endpoint는 다음 순서를 고정한다. [SS10–SS14]

1. 이전 time의 photons와 guards에 Bianchi redshift를 적용한다.
2. 이동 에너지를 fixed physical-energy grid의 hat 함수에 투영한다.
3. endpoint time의 source_weights를 이용해 13.7 eV birth를 더한다.
4. 128개 방향을 compensated sum으로 33개 energy group에 합친다.
5. 이전 gas와 새 photon groups를 조립하고 endpoint density \(n_H(t_1)=10^{-4}\exp[-(h_1+h_2+h_3)t_1]\), \(f_{\rm He}=0.083\), \(H=(h_1+h_2+h_3)/3\)를 만든다.
6. Coupled conservative BE point, root certificate, carry enclosure를 계산한다.
7. Fixed nodes의 cross sections를 이용해 방향별 흡수 결과를 돌려놓고 ledger/compensation을 운반한다.

BE에서 photon 제거는
\[
P_k=\frac{N_k}{1+d\,c\,n_H[(1-x)\sigma_{{\rm HI},k}
+f_{\rm He}(1-y_1-y_2)\sigma_{{\rm HeI},k}
+f_{\rm He}y_1\sigma_{{\rm HeII},k}]}.
\]
따라서 gas Jacobian, Hessian 및 mixed RHS에는 분모의 gas dependence가 들어간다. Photon numerator N의 기존 \(U,V,W\)와 새 birth도 보존한다. Photon derivative를 gas derivative와 독립 상수로 잘못 고정하면 full-chain Jacobian을 잃는다.

HH rate는 \(q=n_H(1-x)^2k(T)\)이며 1/2 factor가 없다.
\[
T=\frac{2\,{\rm eV}_{\rm erg}\,w}{3k_B[1+f_{\rm He}+x+f_{\rm He}(y_1+2y_2)]},
\quad k(T)=1.2\times10^{-17}T^{1.2}e^{-157800/T}.
\]
H/He free-electron/particle-number dependence가 HH 온도 감도에 들어간다. Native rate Jet은 35000–60000 K 범위를 요구한다. Heating에는 각 absorber의 \(E_k-\chi_a\), cooling/nonphoto에는 기존 FT03 모델, expansion에는 \(-2Hw\)가 들어간다. 현재 photo energy grid의 상한 20 eV 아래에서는 He cross section이 0인 좌표가 있더라도 He ionization/collision/recombination/thermal coupling을 제거하지 않는다. [SS12–SS14]

## Local Codex가 읽을 실제 구현 지점

모든 경로의 owner pin은 569b04cd71e45756e0fd476aef6643bd9434f4fa다. Base prefix E는 research/r31ao_unequal_ladder/ncp_energy06e_certificate_20261010_v1, P는 research/r31ao_unequal_ladder/ncp_phys01_mixed_contract_20261010_v1이다.

| 경로 | 함수·타입 | 현재 의미와 다음 수정 |
|---|---|---|
| E/src/paired_stage_receipt.rs | accepted_half1_receipt, resolve_half2_predecessor | 추가 endpoint 호출 없는 private receipt; same returned object 재사용 |
| E/src/owner_birth.rs | prepare_actual_birth, linked_tangent_stage, remap_lambda_fixed_theta | 원 순서 보존; first lambda-only 연결을 mixed \((\lambda,b)\)로 확장 |
| E/original_owner_dependency/src/hh_primary_extension.rs | HhMode, hh_rate_jet, hh_interval_source, hh_stage_root | 두 mode를 새 amplitude-family adapter로 lift; full parameter tube producer 분리 |
| E/original_owner_dependency/src/coupled_primary.rs | interval_rhs, inverse4, primary_stage_root | photon elimination의 전체 chain derivative; 고정 C의 source-bound provenance |
| E/original_owner_dependency/src/hh_paired_extension.rs | hh_source_endpoint, hh_checkpoint_encode/decode | 원 endpoint 순서, native bytes 및 ledger 의미 보존 |
| E/original_owner_dependency/src/paired_runtime.rs | energy_nodes, hat/hat_box, source_weights | 고정 grid/θ에서 한쪽 time jet; guard/cutoff knot 처리 |
| P/src/mixed_family.py | validate_four_corners, native_mixed_response | identity validator 재사용; native producer 부재 refusal은 실제 producer 확보 전 유지 |
| P/tests/test_mixed_family.py | MixedFamilyTests | 현재 exact synthetic two-coordinate test만 있음; full H/He oracle로 확대하지 않음 |
| E/src/main.rs, E/cargo/Cargo.toml | receipt_contract | 현재 unconditional exit77; 실제 mixed-family CLI 없음 |

## CLI와 회귀 명령의 정확한 상태

Current receipt_contract main은 인수와 무관하게 ENERGY06E_SCIENCE_DISPATCH_BLOCKED를 출력하고 exit77이다. 이는 인증·승인 부재를 숨기지 않는 예정된 refusal이며 현재 native 실행 CLI라고 안내하면 안 된다. 과거 hh_cli.rs는 --hh OFF/LCS/COMPARE, --hh-grid, --hh-steps, --scenario, --output, --resume, --pilot만 해석하고 --full을 거절한다. --lambda 또는 --source-amplitude는 구현되어 있지 않다. [SS04–SS06]

E/cargo/Cargo.toml, owner_runtime.rs, src/main.rs는 이전 /root/WU088_HH_ENERGY06E_20261010 아래 절대경로를 갖는다. E/prepare_e.py도 이전 workspace를 복사하는 역사적 packager다. 이를 current checkout에서 무작정 실행하지 않는다. 새 isolated sidecar에 wrapper만 명시적으로 relocate하고 원 original_owner_dependency는 byte-preserved read-only 입력으로 둔다. 이 relocation diff와 새 compiler/flags/binary identity를 기록한다. [SS05, SS25]

다음은 relocation 후에만 유효한 비과학 compile/선택 회귀 명령의 형태다. NCP_PHYS04_WORK는 local Codex가 새로 만든 실제 절대경로로 채우고, 기존 HOME 같은 시스템 변수를 덮어쓰지 않는다. Unchanged historical tests는 다시 실행하지 않으며 변경된 receipt 또는 adapter 의존성이 있을 때 해당 regression만 사용한다.

~~~bash
cargo check --offline --locked --manifest-path "$NCP_PHYS04_WORK/cargo/Cargo.toml" --bin receipt_contract
cargo test --offline --locked --manifest-path "$NCP_PHYS04_WORK/cargo/Cargo.toml" --bin receipt_contract --no-run
cargo test --offline --locked --manifest-path "$NCP_PHYS04_WORK/cargo/Cargo.toml" --bin receipt_contract energy06e_tests -- --test-threads=1
~~~

Energy06e_tests는 synthetic checkpoint serialization/receipt tests다. 실제 root를 호출하지 않는다. Owner actual_input_tests는 HH_SEED 디렉터리의 member*.bin을 읽는 source-only prebirth 테스트이고 coupled root 인증은 하지 않는다. 이번 조사에서는 둘 다 재실행하지 않았다. [SS22–SS24]

P의 Python identity 변경 후에는 다음처럼 관련 method만 실행할 수 있다. 이 명령도 이번 조사에서 실행하지 않았다.

~~~bash
python3 -B -Werror "$NCP_PHYS04_OWNER/research/r31ao_unequal_ladder/ncp_phys01_mixed_contract_20261010_v1/tests/test_mixed_family.py" MixedFamilyTests.test_all_shared_identity_mutations_rejected MixedFamilyTests.test_missing_and_forged_native_certificate_rejected
~~~

새 PHYS04 reference implementation에 대응하는 원 residual의 독립 미분 oracle, signed tangent guard, density/source time sampling, \(S=0\) stock 보존, linked half1→half2, duplicate-dispatch counter 및 forbidden dispatch refusal 검사는 실제 수정 결과에 맞춰 신규 target으로 만들어야 한다. 새 target이 아직 존재하지 않는 상태를 기존 command인 것처럼 표시하지 않는다.

## 권한·예산·최종 local 반환

현재 exact native budget는 dispatch=0, BE roots=0, macros=0, legacy atomic=0, retry=0이며 authorization=null이다. Native family를 구현하고 source-bound derivative/root tube와 실제 live binding을 닫은 뒤에만 미래 한 macro 제안을 concretize한다. 기존 proposal의 1 macro / 4 corners / 12 full-half-half endpoint calls / concurrency1 / retry0는 승인기록이 아니고 wall/memory 미정, request_ready=false다. 해당 경계를 유지하면서 비파괴 code 이식·build·targeted synthetic verification·archive 분석은 끝까지 진행한다. [SS19]

Native 실행 요청이 최종적으로 필요하면 source+ABI+binary+common-state+parameter rectangle+event schedule+endpoints+internal root counts+wall/memory+current cgroup+UID/reserve+출력경로를 모두 포함한 정확한 제안 한 건으로 만든다. Old consumed FD1/FD2/6cell이나 ON06G history를 재사용하는 승인으로 오인하지 않는다. Physical/production admission은 HOLD다.

반환은 다음 정보를 포함한다.

- 공통 physical initial state와 immutable source identity, amplitude/clock/birth/geometry identity.
- 변경 코드와 selective build/test의 실제 exit, stdout/stderr, 최초 실패 및 수정.
- Source-ordered full/twohalf mixed coefficients·defects와 검증된 범위.
- Full \(G_y\), Hessian/JVP, fixed C, parameter box, strict image/contraction 및 producer identity.
- Whole native half1 state와 predecessor hash; half2 incoming 및 tangent carry identity.
- Top-level endpoint와 내부 point/root 호출 수를 분리한 RUN_LEDGER.
- I, 전체 HH response D, full/twohalf HH defect, mixed defect, true continuous source-law error의 별도 object.
- 실제 finite mixed response/remainder를 구하지 못했다면 null과 구체적 missing premise.
- checkpoint 보존, 독립 판정, commit/tree 및 create-only backup ACK; remote restore는 별도.

