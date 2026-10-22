# 다음 thread 인계: PHYS79 이후 physics→coding

`$physmath-research-loop`와 Exa/SciSpace/Wolfram을 사용하여 WU088_HH의 PHYS79 이후 연구를 이어간다. 사용자 지시로 적용한 embedded skill1.0.0과 cloud1.3 기본 선택에 대한 `POLICY_OVERRIDE.json`을 보존한다. 이미 완료한 동일 identity는 재실행하지 않는다.

## 실제 기준

- Repository: https://github.com/cosmosapjw-quantum/WU088_HH
- 현재 additive Draft PR134: https://github.com/cosmosapjw-quantum/WU088_HH/pull/134
- Branch: `research/hh-phys79-collisional-closure-20261022`
- Unit: `research/hh_phys79_collisional_closure_20261022`
- S2 과학 commit: `338fb7728e8b41f49551200b1f1ba73c047fb90c`
- 외부 최종 전달 위치: `PR134 body — Final delivery / PHYS79_FINAL_DELIVERY_20261022.json`
- 외부 최종 전달 파일: `PHYS79_FINAL_DELIVERY_20261022.json`
- PHYS78 최종 부모: `91d0846a940abf7817c900102dab488ff87e6a82`
- PHYS78 과학 commit: `b001e69668b2d2c2557b51830f5f732164b56ce0`
- 과학 기준 PR128: `92f5ab9dba531ebe05909dcb77d3740d2c68c580`; supplement PR129: `b76fd4b5d0dfe4850ebde66a8a10f78402d36c00`.

**최종 HEAD·ZIP SHA·provider ID는 외부 최종 전달 JSON과 PR134 body에서 읽어 actual remote ref와 대조하라.** 이 repo 문서에 자신의 최종 HEAD와 자신의 backup hash를 재귀적으로 써 넣지 않는다. 과학 S2 commit, 최종 전달 HEAD, backup payload의 identity를 서로 구분한다.

## 연구를 시작하기 전에

현재 actual branch/PR refs, 접근 가능한 다른 repo/branch의 새 실행, backup·delivery record를 identity로 대조한다. 기존 inventory는 51 repository catalog, 142 WU branch refs, 74 최근 PR metadata, 7 sibling actual refs 및 선택된 report/receipt를 다룬다. 접근할 수 없는 비공개 대화를 전수 확인했다고 주장하지 않는다. 과거 inventory 수를 현재 시점의 전수조사로 재사용하지 않는다.

필수 읽기: `FINAL_REPORT_KO.md`, `DAG_OVERLAY.json`, `EXECUTION_LEDGER.json`, `CONTRACT.json`, `POLICY_OVERRIDE.json`, `CODEX_HANDOFF_KO.md`, `POST_PUBLICATION_HANDOFF_KO.md`, `theory/RESEARCH_LOOP_AND_CODE_MAP_KO.md`, `delivery/`, 외부 `PHYS79_FINAL_DELIVERY_20261022.json`. 과학 source를 바꾸기 전 `ATOMIC_SOURCES_PHYS79.md`, `THERMAL_CLOSURE_KO.md`, `DH_DETAILED_BALANCE_CLOSURE_KO.md`, `SAVED_TRAJECTORY_FINDINGS_KO.md`를 `theory/`에서 읽는다.

역사적 `C9_TARGETED_RECHECK.json`의 `initial_review_preserved: C9_REVIEW.json`은 패키지의 `verification/C9_INITIAL_REVIEW.json`을 가리키는 개발 파일명 alias다. 초기 receipt는 재작성하지 않고 이 대응을 사용한다.

## 완료된 범위와 재사용 identity

PHYS79는 source-domain CI와 조건부 D/H 상세평형·열 회계를 구현했다. 24개 고유 light test PASS, C9 F1/F2/N1 닫힘이다. 새 isolated ODE는 **3 성공 = 물리 control2 + 정련1**, 실패0이다. 새로운 z20→2 우주론 ODE0, 완료 identity replay0, NCP0, benchmark0이다. 동일 결과의 재개 검증도 이미 완료되어 **3 skip·새 ODE0**이다. 기존 PHYS78 P013/P030은 재적분 없이 고유322 저장점의 순간 연산자를 평가했고, dependency 수정으로 후처리만2회 했다. 현재 그림은4종 PNG/PDF다.

C01은 T0=`25370.66308424773 K`, nH=`1e-3 cm^-3`의 neutral CI+D CX control이며, C02는 T0=`300 K`, nH=`1 cm^-3`, HII/H=`0.5`, **DII/D=`1e-6`**의 D CX-only control이다. cosmological z20 전하 초기조건으로 전용하지 않는다.

| 완료 task | science ID |
|---|---|
| C01_BASE | `87b585ddcdef54dc97b13f35607d6351f8d3f8320e79942391e5813d36a00761` |
| C02_BASE | `270d221e2c86815860e8c6fa37aee61effcc635ee5b9bc630b54c010c38a542f` |
| C01_REFINED | `f698f70efed77439c95adbb14859c3f03c067a4eb4824571b04132200aa49d49` |

source-manifest SHA256은 `3ed45a27ac6688780d385f2e7833813379ceb3df9b5bc3951b9eb587222735ad`이다. NPZ hash·size와 source별 hash는 `CODEX_HANDOFF_KO.md` 및 `results/ISOLATED_COMMAND_STDOUT.json`에 있다. inherited PHYS78 ODE34=실패2+pilot31+정련1, light35 PASS는 과거 근거를 재사용한다. HH1231/REI729/HH74control63/PHYS78 및 위 PHYS79 완료 identity를 다시 실행하지 않는다.

최대 nucleus 상대 오차 `4.397502728453756e-15`, saved `u+binding` 상대 오차 `2.6645352591003757e-15`, C01 정련 차이 `4.574293383682441e-15`다. C02는 closed-energy scalar equilibrium에 접근했으며, 독립 extent-temperature 잔차 `3.410605131648481e-13 K`로 미세 D isotope heat를 확인했다. 구성상 event residual=0, sampled residual, 이 한 번의 정련 비교를 continuum certificate로 쓰지 않는다.

## 바꾸지 않을 과학 계약

non-tilted LRS Bianchi I, `(-,+,+,+)`, 같은 normal orthonormal frame을 유지한다. gas `pi=0`; 비영 `pi_m`은 collisionless DM이다. signed matter/radiation tensor를 합한 뒤 norm을 취하고 Frobenius와 half-contraction의 `sqrt(2)` 관계를 유지한다. 같은 trajectory의 성분 분석은 species-off 인과 실험이 아니다.

H1/D/T I–II, He3/He4 I–III, Li6/Li7 I–IV 및 neutron, charge-derived electron을 유지한다. 원래 PHYS78는 finite PI+RR, source18/30/60eV, HII/H=`2e-4`와 그 밖의 존재 isotope neutral이라는 탐색 초기조건이다. 현재 n/T와 LiIII/IV의 0은 해당 입력/source의 결과다. 다른 생성 경로의 물리적 불가능성으로 확장하지 않는다.

CI 6개 원소 row를 13 isotope transition에 연결했지만, 실제 Tmax 약25371K에서는 중성 H/He/Li row의 fit만 허용된다. neutral fit 하한1eV≈11604.52K, HeII/LiII/LiIII 하한3/4/5eV, 상한20keV다. 정의역 밖을0 또는 작은 외삽값으로 채우지 않는다. kernel은 거부하고 저장 분석은 NaN+false mask를 쓴다.

D CX는 Savin reverse fit에 `exp(-43K/T)`를 곱한 새 forward 모델이며 raw forward fit을 진단으로 보존했다. domain2.7–200000K, isotope별 neutral/ion mass=`A m_p`, degeneracy ratio1, hyperfine 제외, `ΔI=43k_B K`의 조건부 DB다. 원자료의 raw-fit 정확도가 새 forward에 자동 승계되지 않는다. 동일 global ionic potential을 쓰는 CI/CX만 현재 닫혔다.

비복사 event heat는 `-Δε R`, radiative CX heat는 photon moment를 분리하여 `-Δε R-Qγ`다. 전자수 변화는 `T=u/[(3/2)k_BN]`에 포함된다. F2에서 event-defect sum을 안정화했고 직접 state dot product는 진단으로 남겼다. current isolated controls는 일정 밀도·팽창0·PI/RR0·열 bath0이며 전체 cosmology와 별개다.

## 다음 선택 DAG와 구체적 행동

**다음 우선 노드: LOW_T_CI_SOURCE_COVERAGE.** 약255–11605K 및 필요한 고전하 영역의 원전 cross section/rate를 확보하고, Maxwellian 적분 또는 source를 갖춘 연결 fit의 단위·정확도·matching을 물리 단계에서 먼저 닫는다. 그 뒤 수정된 의존성에 필요한 코드·검증을 수행한다.

**HE_LI_CX_STATE_AND_PHOTON_ENERGY**는 He 비복사 final-state와 Li corrected coefficient/domain, radiative photon moment를 해결한다. total rate만으로 gas heat를 정하지 않는다. **D_PI_RR_ENERGY_ADAPTER**는 D의 단일 potential을 PI threshold, RR emission, CI/CX 에너지에 연결한다. **RECOMBINATION_TO_Z20_INITIAL_CHARGE_CONTRACT**는 별도 유지한다. 이 의무가 열려 있는 동안 기존 PI/RR에 CX heat만 붙인 full z20→2 실행을 승인하지 않는다.

Li hard-UV는 inner-shell/Auger·branching·spectral energy를 먼저 해결한다. collisional excitation/free-free/Compton, 전체 핵반응·분자·spectral transport는 OPEN이다. 이번 결과는 strong no-go가 아니다.

## 실행과 전달 규칙

`source/run_controls.py`는 무인자 또는 `--preflight`일 때 ODE0이다. 실제 실행 flag는 `--execute`, **`--resume`은 없다.** 같은 output·identity의 `--execute`는 receipt/NPZ bytes 검증 후 자동 skip하며, 실패·부분 identity를 자동 재시도하지 않는다. 이미 이 동작을 검증했으므로 단순 확인을 위해 재호출할 필요가 없다. 파일 삭제·새 output 경로로 완료 identity 재실행을 유도하지 않는다.

새로 필요한 실행만 가용 자원과 공유 `LeasePool` 안에서 worker1/thread1로 수행한다. lease가 없으면 WAITING이며 launch하지 않는다. 매 solve 호출 전 durable marker를 남기고 실패도 회계한다. 다른 process를 종료하지 않는다. 실제 remote descendant에 additive draft로 게시하고, 유도/코드/검증/과학 실행/게시/백업/DAG를 분리해 보고한다. 최종 Codex·다음-thread handoff를 갱신하고 final HEAD·backup identity는 외부 전달 JSON과 PR134 body에 결속한다.

**HH_R10=OFF. Production admission NOT_ISSUED. 전체 collisional thermal cosmology는 OPEN.**
