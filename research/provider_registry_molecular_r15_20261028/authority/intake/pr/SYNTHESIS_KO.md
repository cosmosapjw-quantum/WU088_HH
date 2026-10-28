# R15 진입: 최신 PR·commit 원전 조사

## 조사 범위와 실제 완료

소유자 저장소 목록은 같은 시점에 별도 branch 조사자가 수집한 51개 owner repositories를 재사용했다. 현재 open PR은 모든 저장소에서 페이지 끝까지 읽었다. Closed/merged는 updated 내림차순으로 2026-10-28 09:03:58.811 UTC 이후 범위를 읽고, cutoff 이전 행 또는 짧은 마지막 페이지에서 종료했다. 이 cutoff는 이전 R14 branch 조사 시점이며 이전 PR 조사와 일부 겹쳐 누락을 피한다.

| 항목 | 실제 결과 |
|---|---:|
| 저장소 | 51 = public35 + private16 |
| Open PR 페이지 | 85 |
| 현재 open PR | 1,184 = public1,130 + private54 |
| Recent closed/merged 페이지 | 51 |
| Cutoff 이후 closed/merged | 0 |
| 두 목록의 terminal 확인 | 51/51 |
| Census API errors / duplicate open keys | 0 / 0 |
| Public R14 대비 | NEW4 / CHANGED5 / REMOVED0 / UNCHANGED1,121 |
| 목록 읽기 | 10:45:18.741–10:45:34.190 UTC |
| 선택 불변 source 읽기 종료 | 10:49:20.441 UTC |

이는 비원자적 live metadata snapshot이다. 모든 역사 PR·commit·archive의 모든 본문을 읽었다는 뜻이 아니다. Private repository 이름·PR 본문·개별 식별자는 public 산출물에 없고 집계만 포함했다. Current owner repository 목록과 branch 조사의 cutoff는 별도 기록이며, source read 종료 시각으로 소급 변경하지 않는다.

Public 변경 9개 중 다른 저장소의 current PR body 8개는 전문을 읽었다. WU PR150은 이번 R14 closeout section을 읽고, 부모가 이미 복구한 동일 R13/이전 이력은 재사용했다. 본문 전체 bytes는 보존하되 읽은 범위를 PR_BODY_READ_SCOPE.json에 표시했다. 실제 선택한 원전 6개는 불변 commit에서 전문을 취득하고 Git blob SHA를 모두 대조했다. 이 source-only 대조는 raw science를 새로 실행했다는 뜻이 아니다.

## 본문보다 최신 source가 중요한 두 사례

### REC electron field: point 성분의 과학 채택 완료

PR146 본문은 17/20, C8 진행 중이라고 쓰지만, census head `bc9fd57d41dcfc6aaa717bfd7f8e98846d10332e`의 RESULT_REPORT_KO.md와 SCIENTIFIC_ADMISSION.json은 C9 CLOSED/PASS_SCOPED를 담는다. 실제 채택은 명시적 signed incoming을 받는 원 HyRec FULL/H_STEADY/He-neutral/xe=xHII/fsR=meR=1의 point Fe=FH다.

고정 point와 초기화된 table에서 M X=S0+G u이고, native divisors와 Schur determinant가 0이 아니면 FH는 incoming에 대해 실수 대수상 affine이다. 이를 point 전체의 affine성이나 binary64 exact affinity로 확대하지 않는다. 132 FH·264 real·41,052 virtual 변수는 저장값과 bitwise 동일하고, Decimal80 정규화 residual 최대1.4989401807314334e-15는 고정4096eps64 기준9.094947017729282e-13 아래다. 24개 사전 거부,3개 저장값 mutation,9개 signed incoming controls가 기록돼 있다.

Native clock eta=ln(a), nH cm^-3, H s^-1, 온도eV이며 geometric query clock은 별개다. Canonical28/88 delta0,physical0/313,full-state coupled F·whole-domain total xe'·defect·e0·norm·positive tube는 미공급이다. 따라서 이 성과는 WU의 실제 HD reactive array 또는 같은 source/state/density/clock의 named physical consumer로 직접 결속할 수 없다. C10 전달 영수증은 과학 채택과 별도 상태로 읽는다.

원전: [REC 결과](https://github.com/cosmosapjw-quantum/rec_bianchi/blob/bc9fd57d41dcfc6aaa717bfd7f8e98846d10332e/research/rec_h5_electron_field_20261028/RESULT_REPORT_KO.md), [REC 과학 채택](https://github.com/cosmosapjw-quantum/rec_bianchi/blob/bc9fd57d41dcfc6aaa717bfd7f8e98846d10332e/research/rec_h5_electron_field_20261028/SCIENTIFIC_ADMISSION.json).

### CR energy sum: R01 본문을 C10 결과로 갱신해 해석

PR114 본문은 R01/20에 머물러 있지만 head `3d9818b4b91d00beef946aa88540d73c33e51dac`의 REPORT_SCIENCE_KO.md는 과학 S=`3230790ebeb2657c3a222a2bdc1d043b7d745492`를 결속하는 C10 보고서다. 고정 PHYS02 3,201 atoms에서 E_i+E_j<=K 및 diagonal2E_i<=K를 지키는 double mass d의 최댓값을 exact tail deficiency로 구성했다. Primary123/123, controls80/80, independent223/223(fresh192/reuse31), C9 PASS_SCOPED_ENERGY_SUM/open0이다. 원 primary_v1의 첫 solver 이전 fixture-ID 실패를 보존하며 all_runtime_attempts_pass=false다.

소비하는 원소·proper clock·고정 inventory는 CR의 조건부 source contract다. d 최대화와 출력 witness의 cross C는 다른 목적량이다. Actual K/exclusive kernel/outside partner/donor work/EOS/T/full physical native25는 null이고 중앙28/88 delta0다. 현재 닫힌 charge13.861533/40의 잔여26.138467은 NONTRANSFERABLE이며 WU 새 allowance에 합산하지 않는다.

원전: [CR energy-sum 최종 과학 보고서](https://github.com/cosmosapjw-quantum/bass_cr/blob/3d9818b4b91d00beef946aa88540d73c33e51dac/research/cr_he_energy_sum_20261028/REPORT_SCIENCE_KO.md).

## 새 cross-event 최적화와 post-cutoff closeout

새 PR115의 scientific source `9ec654379074b731ce20f0b7dbae05077ddf4d4b`는 다른 birth bin의 edge만 사용해 C 자체를 최대화한다. Fractional matching deficiency를 bin과 두 energy threshold로 환원하여 Cmax=(N−Delta)/2를 얻고, 같은 source marginal의 sparse attainment를 연결했다. 원3,200active atoms+ghost,12,804source fields,116small-graph cases,9native duals,3explicit primals,9,603atom marginals 및3consumer returns가 기록된다. K=3에서 Cmax/N≈0.13534610259545182, K=10/20에서≈0.3945598167204703이다.

Native K20 일반 flow exit−9 및 reservation 초과, 첫 recovery syntax failure를 보존했다. 완성된 앞8caps를 재사용하고 K20의 complete-support direct construction만 수행한 기록이다. Charge28.653943/40,science_closed=true, 잔여는 NONTRANSFERABLE이다. 실제 exclusive He event law, K, donor/EOS/T는 여전히 null이다. 이 조건부 graph는 WU molecular forcing의 실제 물리 입력이 아니다.

Backup 조사자가 구체적인 새 C10 이름을 알려 주어 단 한 번의 후속 commit read를 했다. `9c0cc44c87ed3f416e2ca37f8fa3ed82bb562698`는 실제로 위 scientific source의 직계 자식이며,15개 변경 경로는 workflow·report·handoff·publication 근거다. Report의 유도·결과는 그대로이고10줄의 delivery section이 추가됐다. SOURCE1,553,470bytes,SHA e606aea543f2dbf66832a549f4010ecb5cb51f642b45d6293ce1fd1b077f2a11와179payload에 대한 양쪽 original GET 기록을 이 owner의 문서에서 확인했다. 우리가 새 GET이나 ACK를 수행했다는 주장은 아니다.

이 단위의20개 stage checkpoint는 science 이후 closeout에 게시한 기록임을 원문이 명시한다. WU의 이번 사용자 요청은 단계마다 실제 게시·백업이므로 그 순서를 새 단위에서 직접 지켜야 한다. 남의 사후 checkpoint를 contemporaneous publication 예로 바꾸지 않는다.

원전: [CR cross 최종 보고서](https://github.com/cosmosapjw-quantum/bass_cr/blob/9c0cc44c87ed3f416e2ca37f8fa3ed82bb562698/research/cr_he_energy_cross_20261028/REPORT_KO.md).

## 다른 새·갱신 PR의 재사용 의미

| 자료 | 읽은 최신 내용 | WU에 연결할 범위 |
|---|---|---|
| REI PR244 | moving caloric knots의 방향미분·구현 준비, body15/20, runtime/CAS NOT_RUN; census에서 새 head207491…를 branch 조사자에게 전달 | derivative와 runtime 완료를 구별. WU forcing certificate를 공급하지 않음 |
| REI PR245 | 17thermal+2fast reservoirs의 비보정 external-source response,201saved epochs,7tests; 새 IVP 없음 | frozen-epoch QSS 진단이며 physical calibration·transport·timescale 미완; 같은 WU full-A forcing으로 이식하지 않음 |
| REI PR243 | 저장된17-state abundance와 별도257epoch n/T 진단, source별 clock·state를 분리 | isotope-total history를 ionic history에 splice하지 않는 원칙과 conditional source 의미 재사용 |
| REI PR222 | body의 역사87-node 제목·서술과 현재head가 다름; 새 head d742f…를 branch 조사자에게 전달 | 실제 immutable central delta가 권위이며 PR제목으로 완료 수를 갱신하지 않음 |
| BASS PR227 BF3-E | 같은 finite collocation A에 대한 retarded source memory, full initial carrier와 local final-angle weights, finite-grid convergence; 별도 policy CI failure | 기억 적분의 source/state/operator identity를 보존하는 대안 사례. Continuum kernel·finite remapping·collocation을 자동 동일시하지 않음 |
| HTT 679f2c… | reviewed P2 manuscript consumer preparation, SYNTHETIC_UNIT_FIXTURE, PREPARED_PENDING_SOURCE_QUALIFICATION | code preparation과 실제 science/MC/source qualification을 구별. WU physical input 추가 없음 |
| WU PR150 | R14FINAL20/20,DAG29/44,105-file payload와 원 과학 결과 | 현재 직접 재사용 baseline; 새 사용자 증액·후속-loop 지시는 old no-next-unit scope를 새 계약 범위에서 대체 |

BASS의 targeted13tests와 별도 inherited policy CI failure, REI의 조건부 source와 전체 physical closure, HTT의 synthetic preparation을 각각 원 상태로 보존한다. Foreign completion counts·budgets는 WU에 합산하지 않는다. HTT source는 [선택 README](https://github.com/cosmosapjw-quantum/htt_base/blob/679f2c5e434abcb78f330b540ae457b32d9f7a8a/docs/research_program/observational_publication_20261015/OBSERVABLE_BRIDGE_RECONCILIATION_20261027/products/R36-11-SCIENCE-SYNTHESIS/reviewed_p2_preparation_20261028/README.md)를 직접 읽었다. REI/BASS의 구체적 immutable source delta는 별도 branch 조사 산출물에 연결한다.

## 다음 단위에 넘길 판단

현재 선택 원전에서 WU actual HD reactive array 또는 동일 state/density/clock의 named physical consumer 입력을 확보하지 못했다. 이는 읽은 범위의 입력 상태이며 자료의 전역 부재나 불가능성 결론이 아니다. 이 PR lane만으로 DAG 노드를 닫거나 물리 승인을 늘리지 않았다.

R14의 fixed K/pi/destruction, whole-w family, all-starts zero-mass propagator, whole fine/coarse forcing 및 original-t0 memory를 보존하는 다음 조건부 방법 단위를 검토할 수 있다. 이번 결과에서 직접 넘길 교훈은 (1) point residual을 whole-domain forcing으로 승격하지 않을 것, (2) exact source representation과 threshold·clock identity를 보존할 것, (3) 원 memory operator와 비교계·참조 경로의 차이를 명시할 것, (4) 실행 전 계약과 단계별 실제 게시·백업을 수행할 것이다. 구체적 theorem/API/work/gap/precision/resource 계약은 부모가 모든 조사 결과를 종합한 뒤 고정한다.

## 수행 상태와 진단

새 과학 실행·scientific import·CAS·외부 쓰기는 모두0이다. 실제 tool 반환과 로컬 identity 대조만 수행했다. 첫 대용량 baseline 출력 truncation, baseline row의 repo 위치 차이로 인한 local helper KeyError, CR report 경로404를 별도로 기록했다. 세 문제는 읽기·schema·locator 교정으로 해결했고 census의 API error0 또는 science 결과와 섞지 않았다. 원전6개 Git blob6/6일치이며, 두 기준 snapshot과 모든 변경 PR key를 보존한다.

적용 스킬은 physmath-research-loop1.3.0의 SKILL, POLICY_INTEGRATION, THEORY_LOOP R2다. 정확한 resource·SHA와 적용 범위는 SKILL_CONTEXT.json, 원전 identity는 SOURCE_READ_IDENTITIES.json에 있다. 이 작업은 요청된 R2 근거 조사이며 새 독립 scientific audit를 수행하거나 기존 C9를 다시 승인하지 않았다.
