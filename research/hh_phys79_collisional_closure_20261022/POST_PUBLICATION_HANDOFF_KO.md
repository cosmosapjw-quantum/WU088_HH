# PHYS79 게시 후 전달 인계

## 1. 게시 계보와 authoritative 전달 기록

Repository는 https://github.com/cosmosapjw-quantum/WU088_HH, additive Draft는 https://github.com/cosmosapjw-quantum/WU088_HH/pull/134, branch는 `research/hh-phys79-collisional-closure-20261022`다. PHYS78 실제 부모 `91d0846a940abf7817c900102dab488ff87e6a82`에서 이어졌다. S0 source/derivation commit은 `77bd3cc5f482804a246a66a8b2f3b631611e3219`, S1 implementation/saved-state-analysis commit은 `b61494393532c42a12c7517408895a5cf38aea29`, S2 과학 commit은 **`338fb7728e8b41f49551200b1f1ba73c047fb90c`**이다.

외부 최종 전달 위치는 **`PR134 body — Final delivery / PHYS79_FINAL_DELIVERY_20261022.json`**, 파일명은 `PHYS79_FINAL_DELIVERY_20261022.json`이다. 최종 전달 HEAD, 그 HEAD의 tree/parent 관계, ZIP 파일명·SHA256·bytes, Drive/Dropbox의 ZIP 및 최종 JSON ID, 검증 실행의 정확한 범위는 **외부 최종 전달 JSON과 PR134 body**에서 확인한다. PR 번호나 날짜만 같다는 이유로 payload identity가 같다고 가정하지 않는다.

이 문서는 자신의 commit hash나 자신의 backup ZIP hash를 재귀적으로 담지 않는다. repo 내부 handoff를 확정한 뒤 생기는 최종 HEAD와 provider ID를 외부 JSON 및 PR body에 연결하면, 기록을 쓰는 행위가 기록 대상 commit/ZIP을 다시 바꾸지 않는다. 과학 S2는 고정된 결과의 기준이고, 후속 handoff/delivery metadata commit은 전달을 마무리하는 기준이다.

## 2. 다음 작업자가 대조할 전달 사슬

1. actual branch ref와 PR134 head를 읽고 외부 JSON의 최종 HEAD와 일치하는지 확인한다. 달라졌으면 새 descendant의 내용과 과학 의존성을 확인하며, 오래된 handoff에 맞추기 위해 ref를 되돌리지 않는다.
2. 외부 JSON이 가리키는 S2 과학 commit과 최종 HEAD의 조상 관계, `SCIENTIFIC_PAYLOAD_MANIFEST.json`, 최종 ZIP manifest를 대조한다. 과학 소스/입력/NPZ bytes와 metadata-only 변경을 구분한다.
3. Drive/Dropbox ID·size·provider hash와 ZIP 자체 SHA256을 각각 확인한다. **metadata ACK, Git blob identity 대조, 전체 원격 bytes 다운로드, ZIP CRC, payload별 SHA256 검사**는 서로 다른 확인이다. 외부 receipt에 실제로 수행된 범위만 PASS로 보고한다.
4. 외부 최종 JSON의 provider 복사본이 같은 의미와 원본 bytes를 유지하는지 receipt 범위대로 읽는다. extracted text의 덧붙은 LF나 provider block hash를 원 ZIP SHA256과 혼동하지 않는다.
5. 과학 결과의 상태는 `EXECUTION_LEDGER.json`과 실행 receipt로, 게시·backup 완료 상태는 `delivery/`와 외부 최종 전달 receipt로 판단한다. S2 snapshot의 publication/backup pending은 snapshot 당시의 상태이므로, 그것을 최신 외부 전달 판정과 섞어 쓰지 않는다.

이 절차는 identity를 읽고 확인하는 인계이며 완료된 science를 재실행하라는 지시가 아니다. 최종 전달 기록에 아직 없는 검증을 문구만으로 완료 처리하지 않는다.

역사적 alias도 보존한다. `verification/C9_TARGETED_RECHECK.json`의 `initial_review_preserved`에 적힌 `C9_REVIEW.json`은 패키지의 **`verification/C9_INITIAL_REVIEW.json`**과 대응한다. 개발 중 이름을 최종 패키지 이름으로 설명하는 것이며, 기존 receipt의 bytes나 review 내용을 변경하지 않는다.

## 3. 전달되는 완료 과학과 실행 수

현재 과학 unit은 `COLLISIONAL_SOURCE_DOMAIN_AND_CONSERVATIVE_OPERATOR`다. domain-guarded CI와 선언된 D/H DB43K closure, per-H thermal/ionic energy ledger, saved PHYS78 진단, isolated controls를 제공한다. 전체 `COLLISIONAL_ATOMIC_AND_THERMAL_CLOSURE`는 `PARTIAL_WITH_EXECUTABLE_SUBSET`이다.

| 분류 | 전달 상태 |
|---|---|
| 유도 | source domain·stoichiometry·thermal chain·D detailed balance를 조건부로 확보; 실제 Wolfram receipt 보존 |
| 코드 | CI6 elemental row/13 isotope transition, 명시적 subnetwork, finite/domain guard, projection 없음 |
| light 검증 | 24개 고유 method PASS; C9 F1/F2/N1 수정·targeted 재검토 완료 |
| 저장 상태 진단 | P013/P030 고유322 epochs; dependency 변경으로 후처리2회; 새 ODE0 |
| 새 과학 실행 | 2 isolated controls + 1 refinement = **3 성공**, 실패0 |
| 완료 재개 | 같은 identity3개 검증 후 skip; 추가 ODE0; 완료 replay0 |
| 새 cosmological ODE / NCP / benchmark | 0 / 0 / 0 |
| 그림 | 현재4종 PNG+4종 PDF; 과거 preview는 history에 별도 보존 |
| 게시·backup | 최종 actual commit/provider receipt를 외부 최종 전달 JSON에서 확인 |
| 전체 cosmological closure | OPEN; production admission 없음 |

최초 science run ID `03815a51f7d3460cb658d114e0db6599`, 재개 검증 run ID `4dc81a560b4044cb9138400affd5aec3`, source-manifest SHA256 `3ed45a27ac6688780d385f2e7833813379ceb3df9b5bc3951b9eb587222735ad`다. 완료 science identity는 다음과 같다.

| Task | science ID |
|---|---|
| C01_BASE | `87b585ddcdef54dc97b13f35607d6351f8d3f8320e79942391e5813d36a00761` |
| C02_BASE | `270d221e2c86815860e8c6fa37aee61effcc635ee5b9bc630b54c010c38a542f` |
| C01_REFINED | `f698f70efed77439c95adbb14859c3f03c067a4eb4824571b04132200aa49d49` |

raw NPZ bytes/hash와 receipt checksum은 `results/ISOLATED_COMMAND_STDOUT.json`, `results/isolated/cases/` 및 `CODEX_HANDOFF_KO.md`에서 대조한다. 최대 isotope 오차 `4.397502728453756e-15`, saved total energy 상대 오차 `2.6645352591003757e-15`, 정련 차이 `4.574293383682441e-15`, C02 extent-temperature 차이 `3.410605131648481e-13 K`다. 이 sampled 검사와 구성상 event residual을 continuum certificate로 부르지 않는다.

C02의 정확한 초기 D 전하 조건은 **DII/D=`1e-6`**이다. T0=`300 K`, nH=`1 cm^-3`, HII/H=`0.5`와 함께 `inputs/CONTROL_PLAN.json` 및 case receipt를 기준으로 읽는다.

PHYS78의 ODE34=실패2+pilot31+정련1 및 고유 light35 PASS는 inherited evidence다. HH1231/REI729/HH74control63/PHYS78와 위 PHYS79 완료 identity는 재실행하지 않는다. 후처리·plot·경량 시험·ODE·게시·복원은 별도 회계한다.

## 4. 다음 물리 DAG와 해석 경계

다음 우선 작업은 **LOW_T_CI_SOURCE_COVERAGE**다. PHYS78의 약255–25371K 이력 중 중성 CI fit은 약11604.52K 이상에서만 허용되고, HeII/LiII/LiIII fit 하한3/4/5eV는 그 Tmax보다 높다. domain 밖을0이나 작은 외삽값으로 메우지 않는다. 원전 cross section/rate의 Maxwellian 적분 또는 명시적 연결 fit을 먼저 구성한다.

**HE_LI_CX_STATE_AND_PHOTON_ENERGY**에서는 final-state branch, corrected coefficient/domain, radiative photon-energy moment를 해결한다. total rate가 gas heat를 정하지 않는다. **D_PI_RR_ENERGY_ADAPTER**에서는 43k_B K D isotope shift를 PI threshold·RR emission·CI/CX에 같은 global potential로 연결한다. 현재 Savin reverse×`exp(-43/T)` closure는 명시된 ground-state 모델이고 raw forward fit의 정확도 보장을 자동 승계하지 않는다.

**RECOMBINATION_TO_Z20_INITIAL_CHARGE_CONTRACT**, Li hard-UV inner-shell/branching·spectral energy, collisional excitation/free-free/Compton, 전체 nuclear/molecular/spectral transport는 OPEN이다. 기존 HII/H=`2e-4`와 다른 존재 isotope neutral은 탐색 초기조건이다. isolated control의 전하 초기조건을 새 cosmological 초기조건으로 대체하지 않는다. 같은 trajectory 분석은 species-off 인과 실험이 아니고, n/T 또는 LiIII/IV의 source-specific0은 모든 생성 경로의 금지가 아니다.

non-tilted LRS Bianchi I, 같은 normal orthonormal frame, gas pi=0, collisionless DM의 pi_m 소유권, signed tensor 합산 후 norm, Frobenius/half-contraction의 sqrt(2) 관계를 유지한다. 이번 부분 폐쇄의 성공은 전체 이방성·핵·복사 모델의 admission이 아니다. strong no-go를 주장하지 않는다.

## 5. 재개 interface와 접근 범위

runner는 무인자 또는 `--preflight`에서 ODE를 시작하지 않는다. 실제 실행 flag는 `--execute`이며 **`--resume`은 없다**. 동일 output에서 완료 identity의 `--execute`는 receipt·NPZ bytes를 확인하고 자동 skip한다. 실패·부분 identity 자동 재시도는 없으며, 현재3개 case의 skip 동작은 이미 실제로 확인했다. 단순 재확인을 위해 다시 실행하거나 완료 결과를 삭제하지 않는다.

필요한 새 실행만 공유 lease에서 worker1/thread1로 수행하고, lease가 없으면 WAITING이다. 모든 solve 호출 전 marker를 남기고 실패도 회계한다. 다른 process를 종료하거나 그 소유 lease를 회수하지 않는다. 새 과학 변경은 실제 remote descendant의 additive draft로 게시하며 유도/코드/검증/과학 실행/게시/backup/DAG를 분리한다.

초기 identity 조사에서는 접근 가능한 repository/branch/PR와 선택된 sibling 결과·provider metadata·외부 전달 JSON을 대조했다. 접근할 수 없는 비공개 대화 또는 모든 branch의 모든 파일을 전수 확인한 것은 아니다. PHYS78의 과거 whole-ZIP bytes/CRC/375 payload SHA PASS는 해당 과거 receipt의 근거이며, PHYS79 intake에서 새로 그 전체 복원을 수행했다는 뜻이 아니다. PHYS79 최종 backup도 외부 receipt에 기록된 실제 검증 범위를 따라 보고한다.

다음 작업자는 `CODEX_HANDOFF_KO.md`와 `NEXT_THREAD_HANDOFF_KO.md`를 읽고 변경된 과학 의존성부터 진행한다. 사용자 embedded skill1.0.0 및 현재 사용자 지시 우선 적용은 `POLICY_OVERRIDE.json`을 따른다. **HH_R10=OFF. Production admission NOT_ISSUED.**
