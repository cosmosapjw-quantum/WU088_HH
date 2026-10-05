# HH-ON02: 실제 정적 HH 시간 적분과 남은 전구간 수지 gate

판정은 `STATIC_OPTIN_STEPPER_REFERENCE_VERIFIED__S0_GLOBAL_LEDGER_GATE_FAIL`이다. 사용자 요청에 따라 HH 연구는 ACTIVE다. 선택적 F1의 연구용 source/domain/owner 계약을 고정했고 F2의 native 정적 시간 경로를 구현·실행했다. 물리 적용 승인, live REI production 연결, 팽창 S0 또는 F09 완료는 아니다. S0 원본의 HH OFF와 모든 기준은 변경하지 않았다.

## 구현

HH-ON01의 provider를 그대로 쓰고, 고정된 실제 `ft03_implicit_step`의 positive block iteration을 별도 opt-in 경로로 확장했다. OFF는 원 FT03 함수를 직접 호출한다. ON은 per-neutral frequency에 `nH*(1-h_guess)*k(T_guess)`를 더해 fixed point에서 `nH*(1-h)^2*k`를 재현한다. ne로 나누거나 beta_e에 숨기지 않는다. HH event는 전자 CI와 별도이며 열항은 `-chi*R`, chemical은 반대 부호, 직접 photon/escape source는0이다.

모든 thermal 평가, 최종 BE residual, 전용 HH counter와 full/half1/half2가 같은 selector를 쓴다. 실제 accepted state는 half2이고 사건수는 half1+half2다. trial 전체 endpoint rate*dt로 대체하지 않는다. `try_adaptive`는 모든 검사를 통과한 뒤에만 caller state를 변경한다. 원 모듈과 ON01 source bytes는 보존했다.

연구창은 H=0, common-T Maxwellian reference, 기체 정지계, T35000..60000K, nH1e-4/nHe8.3e-6cm^-3다. LCS와 corrected-KS는 서로 다른 formula scenario이지 source 불확실성의 rigorous band가 아니다. 원 S0의 expanding13.7eV 모형과 이번 20/35/70eV 정적 FT03 control을 혼동하지 않는다.

## 실행

신규 최초14 tests 중 missing-HH 구현을 겨냥한9개가 RED,5개는 baseline controls로 이미 PASS였다. 구현 후14개 PASS. 추가한 intermediate-temperature/rollback coverage의 최초 입력35000.05K는 실제 경계를 넘지 않아 테스트 기대가 잘못됐고, 원실패와입력을 보존한 뒤35000.01K로만 수정했다. 최종15개 PASS, exit0. 15개 전부 red-first라고 하지 않는다.

3 IC(neutral_seed/near_neutral/nominal) × OFF/LCS/KS × dt1e9/5e8/2.5e8s, t_end1e11s의27개 정적 이력을 먼저 실행했다. 별도5populations+lnT좌표의 직접 연속 RHS로 DOP853/Radau9쌍, 총18개 독립 ODE를 계산했다. 두 방법의 최대 관측량차1.4210854715202004e-14, finest-grid 최대분율/lnT오차2.1156606766492558e-7, 큰오차의 refinement비는 대략0.5다. 동일sigma/상수 입력을 사용하므로 cross-section을 독립검증한 것은 아니다.

최초 residual tolerance1e-14와 단 한 번의 강화1e-15에서 각각27개 adapter 이력, 합계54회/12600acceptedmacrosteps/37800BE constituent solves를 실행했다. 추가 원 OFF shadow이력18개에서4200개 accepted-step 상태/기존event의 bitwise대조가 일치했다. 독립 ODE18개는 강화 때 재실행하지 않았다. 동일27설정을54물리시나리오로 세지 않는다.

최초 finest neutral_seed에서 OFF h=0, LCS h약2.23180e-6, KS h약2.22137e-8이다. baseline은ne=0에서 전자 CI를 시작하지 못하지만HH가 첫 전자를 만든다. nominal에서LCS-OFF h차는약2.09174e-8이다. 이는 짧은 정적 formula모형의 결과이고 expandingS0의 HH물리중요도/무시가능성은 아니다.

## 보존된 실패

사전 정적 research ledger목표1e-11은 통과했지만, 기존 S0의 더 엄격한1e-12를 별도 적용하면 최초 누적energy최대3.779126310782208e-12였다. 이 최대사례는near_neutral/OFF여서 새로운HH source오류로 단정할 수 없다. 기준을 완화하지 않고 numerical-control amendment를 기록해 residual tolerance만1e-15로 한 번 강화했다.

그 뒤에도 near_neutral/KS/dt2.5e8s의 누적energy잔차는 **1.2812803304029393e-12 > 1e-12**다.26/27설정은 이 기준을 충족하지만 전체 판정은FAIL이다. H사건수잔차최대는6.564762062745808e-13이다. `results/TIGHT_CONTROL_RESULT.json`과 check exit2를 보존한다. native 적분프로세스exit0/단위시험PASS와 전구간energy gateFAIL을 혼합하지 않는다. 실제S0 history는 실행하지 않았으므로 그 실제실패를 관측한 것이 아니다.

정적 total energy가 `E=a^T Y+E_escape`이고 source불변량이0이면 정확한 실수대수에서 `DeltaE=sum_j(a^T*r_j+r_escape,j)`다. 따라서 작은 child residual의 max만으로 수백 half-step 누적오차가 자동 제한되지 않는다. 반올림/장부합산항도 별도로 필요하다. 이 설명은 직접 유도이며 이번 실행에서 각 원인의 기여를 완전히 분해·인증한 결과는 아니다.

## 다음 단위

`HH-ON03`: 실제 child별 에너지/사건 residual을 기록하고 전구간 budget을 배분하는 stopping rule을 검증한다. 이번 실패를 최소재현으로 먼저 사용하고, 임의projection/energy refill/clipping/tolerance완화는 하지 않는다. 같은controls를 무작정 계속줄이거나새승인을요청하지 않는다. 해결후에만 actual REI source-owner가 expandingHH seam과 S0-LCS/KS 후속scenario를 연결한다. 기존F04/F05 certificate를HH-ON에이전하지 않는다.

## 재현 패키지와 provenance

Git에는 source2개와 최종15tests, 검색용요약/선택/백업기록을 둔다. 이 폴더 자체는 standalone crate가 아니다. 전체 원source6개, minimalcrate roots, exactinputs, native전체출력, 독립reference, 최초실패/강화실패/수정기록, 상세REPORT/THEORY/실행명령은 아래ZIP에 있다. `src/hh_stepper.rs`, `src/hh_optin.rs`, `tests/stepper_tests.rs`는ZIP과byte동일하다. Git요약과ZIP상세보고서는동일bytes가 아니다.

- WU088_HH_ON02_S0_SELECTION_STEPPER_20261005_v1.zip
- bytes2718639, entries157, payload156
- SHA256 b25c5e03a943376bec3b793b324daca9bcbae96ce1a1c6c8784de21c745ff4b3
- Drive ID1a7wCa_uiJv4NbNCqh7v8j_x8BL5KdubN, parent1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM
- Dropbox id:BSpOijBcT10AAAAAADzBeA
- Dropbox /BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/WU088_HH_ON02_S0_SELECTION_STEPPER_20261005_v1.zip
- 두provider완료 ACK/ID/name/size확인. 새output fullremote restore=false.

HHparent bb8cbef27b566e0e1e3bec1111ed3a251f71fb8d, REI8e8ea0c664e2ba2f2f8560e0c64266d206fbd50f를게시전다시읽었고변경없었다. FT03 blob370fd2fa60521f2dc121ee81c7d24013a3b0d1e5,S0blobe97888b06c59d63acb0f35181163d256a6894ed6를유지했다. 실제사용Rust1.94.1/LLVM21.1.8은첨부archive에서새runtime에복구했으며기존서명VALIDSIG/TRUST_UNDEFINED의범위를기록했다. 원자primitive/NCP/oldsuite/F09/fullcrate/expandinghistory/독립revieweragent실행은0이다.

Legacy24/289,265unbounded,epsilon_C/Rnull,B22OPEN_UNDETERMINED,consumedscopes보존. 연구는ACTIVE지만 S0activation,physical,production,uniformcertificate는HOLD다. 같은HHbranchnon-force,기존PR33,REI결과전달은PR83. 원TASKS/S0/REIF08source는수정하지않는다.
