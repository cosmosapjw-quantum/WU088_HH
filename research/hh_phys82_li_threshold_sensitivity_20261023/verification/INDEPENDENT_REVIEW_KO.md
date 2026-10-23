# PHYS82 독립 검증: PASS_SCOPED

## 판정

새 Li7 threshold-gap 연산자와 saved-result 재실행 방지 경로에 대해 **1,924개 assertion, 미해결 실패 0개**다. 구현 변경이 필요한 결함은 발견하지 않았다. 수치 검증은 동결된 여섯 온도 `255, 777, 3200, 11000, 25370.66308424773, 50000 K`와 다섯 모델 `L0, L1, W0, W1, ZA1969`를 사용했다. 최종 기계 판독 근거는 `INDEPENDENT_VERIFICATION_FINAL.json`이다.

이 독립 worker는 생성자의 수치 구현을 읽은 뒤 별도 reference를 작성했다. PhysMath Research Loop 1.3.0의 SKILL, stage selection, policy integration, subagent mode 및 C6–C9 정의를 실제 읽고 적용했다. 추가 reviewer 또는 하위 agent를 만들지 않았다.

## 과학적 대응과 독립 reference

`CONTRACT.json`, `THRESHOLD_CONSTRUCTION_KO.md`, `threshold_gap.py`, `run_study.py`와 byte-pinned PHYS81 `finite_ci.py`를 읽었다. 양의 단면적에 대한 Maxwell flux 적분, q=1의 E-factor 상쇄, 반응 가중 평균, 고정 parameter의 `dlogK/dT=(mean/theta-3/2)/T`, prescribed-exposure 차이식이 구현과 대응한다. Chemical sink는 사건당 I이며 반응 가중 입사 에너지를 추가 열손실로 사용하지 않는다.

독립 gap reference는 `t=(E-I)/(6-I)`에서 `t^p`를 QUADPACK QAWS의 algebraic endpoint weight로 처리하고, 나머지 양의 integrand를 직접 적분했다. Flux, incident-energy moment, excess-energy moment를 각각 적분했다. Reference는 incomplete gamma, production `F_j` 공식 및 production scaled-moment 함수를 호출하지 않는다. 물리 상수와 prefactor는 보호된 literal로 따로 구성했다.

30개 frozen-model gap case를 각각 K, logK, mean, excess, dlogK/dT, dK/dT의 여섯 양으로 비교했다. 기존 baseline과 독립 gap의 직접 양의 rate/moment 합으로 total 30개를 별도로 비교했다. p–q rectangle 내부 reference 6개를 추가하여 corner ordering을 확인했다. 총 QAWS 적분은 `30×3 + 6×3 = 108`개다.

`p=1,q=0` identity는 새 `[I,6]` 한-cell PL 연산자 및 새 14-knot `[I,15]` PL 연산자를 각각 여섯 온도에서 평가하여 확인했다. 이것은 새 연산자의 identity이며, 과거 nine-temperature baseline identity의 재실행이 아니다. Baseline은 겹치는 세 온도에서 저장값을 재사용했다.

도함수는 `h/T=5e-5`인 고정된 4차 stencil 하나를 사용했다. 내부 온도는 symmetric stencil, 255 K와 50000 K는 domain 안쪽으로만 향하는 one-sided stencil이다. 여섯 중심 외의 점들은 이 stencil에 필요한 내부 점으로 한정했다. Gap/total과 logK/K 도함수에 대해 120개 비교를 수행했다.

## 오차의 관측 최대값

| 비교 | 관측 최대 오차 | 동결 gate |
|---|---:|---:|
| Gap K, QAWS 대비 상대오차 | 1.4142509577352486e-14 | 1e-10 |
| Gap logK를 rate 상대오차로 환산 | 1.4210854715201903e-14 | 1e-10 |
| Gap mean 상대오차 | 4.901945389089508e-16 | 1e-10 |
| Gap excess 상대오차 | 1.0350907081104759e-15 | 1e-10 |
| Total K, 독립 gap 합 대비 상대오차 | 2.1038780101872465e-14 | 1e-10 |
| 한-cell PL K identity 상대오차 | 3.507219292888102e-15 | 1e-10 |
| 14-knot PL K identity 상대오차 | 5.697880933875216e-14 | 1e-10 |
| logK finite-difference scaled error | 6.615020692129179e-10 | 1e-7 |
| K finite-difference scaled error | 4.2895300314704e-9 | 1e-7 |
| QAWS 자체 relative-error 추정치 | 3.051783895863011e-12 | 1e-10 |
| 고정 노출 delta-probability 상대오차 | 7.93867395428653e-13 | 1e-10 |
| `Ptotal-Pbase-deltaP` 절대 잔차 | 1.1058862159352145e-16 | 2e-15 |

도함수의 scale은 `max(abs(dlogK/dT),1/T)`이며 K 도함수에는 대응하는 `K/T`를 쓴다. 따라서 도함수가 0에 접근할 때 상대오차가 무의미해지는 문제를 피한다. QAWS 자체 오차 추정치는 별도 기록이며 연속 온도 영역에 대한 엄밀한 인증이 아니다.

## Source join, shape, 노출 및 guard

13개 CCC source knot가 원 literal과 동일하며 네 matched model은 6 eV에서 원 endpoint를 유지한다. ZA1969는 `9e-17*(6-I)`의 독립 amplitude를 그대로 사용하고 CCC 값으로 강제하지 않는다. 여섯 온도에서 ZA/L0 rate ratio가 이 amplitude ratio와 일치하며 mean과 logarithmic derivative는 동일하다.

Positivity와 support, gap/total/table mean 순서, p–q corner ordering과 내부 reference, q-factor ratio bound, scaled-moment 양성/순서 및 finite-domain temperature guard를 통과했다. Frozen model mapping, model/rate dataclass 및 반환 cross-section array에 대한 17개 immutability 검사가 통과했다. 80개 API 입력 거부 검사와 z=0 removable limit 및 derivative-underflow 보존에 대한 3개 algebraic 검사가 통과했다.

고정 노출은 30개 model/temperature pair × 세 노출 = 90개다. 80자리 Decimal과 작은 hazard의 별도 양의/교대 급수를 사용하여 probability와 delta 및 상한을 비교했다. 추가 30개 zero-exposure case도 통과했다. 모든 결과의 scope는 prescribed T/ne이다.

## 관측 callback 수

| 이번 verification에서 수행한 일 | 실제 수 |
|---|---:|
| 새 gap 평가 | 150 |
| 새 total 조합 | 150 |
| 새로운 verification 온도에서 unchanged baseline 평가 | 27 |
| 새 한-cell PL 평가 | 6 |
| 새 14-knot PL 평가 | 6 |
| 독립 QAWS 적분 | 108 |
| 명시적 scaled-moment 평가 | 12 |
| 고정 노출 평가 / zero-exposure 평가 | 90 / 30 |
| Cross-section vector / scalar 평가 | 5 / 5 |
| Nine saved-row provenance copy / 중심점 saved copy | 9 / 3 |
| No-science complete-result skip 호출 | 2 |
| No-science replay/output 거부 호출 | 5 |

150개 gap/total은 30개 중심값과 120개 stencil 값이다. Baseline 27개는 새 중심 온도 3개와 stencil 온도 24개다. 위 수는 production design의 `gap=360`, `new baseline=63`과 구별한다. 실제 production `run_study` science branch, historical completed identity 재실행, ODE, benchmark, remote mutation 및 다른 process 종료는 모두 0이다.

## Saved-run 제어 확인

Runner의 saved branch가 `saved_baseline_rate`를 사용하며 baseline evaluator가 else branch에만 있다는 AST 검사를 수행했다. 원 nine-row quantity와 parent science ID를 그대로 복사하는지 확인했다. Parent saved science ID는 `ce0c382952674e0da985d768654f1b0f1253d671ed475f26cc00d7f47eb5e014`다.

실제 `run_study`의 skip 경로는 synthetic complete artifact와 scientific-callback sentinel로 시험했다. 동일 output 및 다른 output filename 요청이 모두 `SKIPPED_IDENTICAL_COMPLETE`를 반환했다. Incomplete claim, partial sidecar, 변경된 saved origin, 변경된 parent row 및 results 밖 output을 거부했다. 이 일곱 호출의 scientific callback은 0이었다. Strict JSON duplicate/nonfinite 거부와 create-only 파일 보존도 통과했다. Fixture는 `/tmp/phys82_work_20261023/review/independent_verification_02_controls`에 있으며 과학 결과로 사용하지 않는다.

## 보존된 첫 실패와 한정된 수정

첫 실행은 모든 numerical matrix를 완료한 뒤 guard label의 `repr(b)`가 lambda-local 이름을 참조하여 NameError로 중단되었다. 첫 결과는 1,815개 assertion과 두 failure record를 보존한다. 두 record는 test harness 예외 및 그 중단에 따른 callback-count 불일치다. **수치 비교 실패는 0개**였다.

세 label을 `repr(bad)`로 고치고 미완료 API guard를 별도 함수로 추출했다. Numerical implementation과 tolerance는 변경하지 않았다. 원 verifier 전체 bytes, precise diff 및 전후 SHA를 보존했다. 후속 실행은 원 수치 evidence의 source hashes를 검증한 뒤 미완료 guard와 runner control만 수행했다. 재실행된 수치 assertion과 추가 rate/quadrature callback은 모두 0이다. 최종 1,924개 assertion은 이 두 보존된 실행의 합성 결과다.

- 첫 receipt: `LEASE_INDEPENDENT_VERIFICATION_01.json`, exit 1.
- 한정 completion receipt: `LEASE_INDEPENDENT_CONTROLS_02.json`, exit 0.
- 각 실행은 기존 PHYS78 lease interface의 0.5 GiB lease와 thread 1을 사용했다.
- 원 verifier SHA256: `4d9344bbccbcd98a82a88f87e32c7ad686f98ea2418ee272e3d73f922c7cee04`.
- 수정 verifier SHA256: `0147018056446e0a91300cec0b1ed0712371d5a53640e897590d5218fdb481e3`.

## 검토한 핵심 source identity

| 파일 | SHA256 |
|---|---|
| `CONTRACT.json` | `450b36883f78b12976dec22e0c4d1435dfb337ad1d74af70b84e8c8ef6df5f13` |
| `source/threshold_gap.py` | `384a546ccee98d69c0e224f4a8cd5bcec91a715cfa6b07b3bc26bc88c492ef90` |
| `source/run_study.py` | `cb5b7b85367aa2d35c0128576ae2a49626aee673c1463a5be405478448ae50ab` |
| `source/vendor/phys81/finite_ci.py` | `e582e83650f39fbaf38e66be848d736845b2bbf38f52613c464ae4e2c1d77674` |
| `source_data/PHYS81_LITERAL.csv` | `522fd63bd4aead4314d7b4ea87f61e5454b23df0f046b1c8e48b2f2023272dad` |
| `source_data/PHYS81_SAVED_RATE_PROFILES.json` | `131de5ea39834a3a3a3dbf4a15ebfe196d1980ebabd69bebcf3e69100e7b2d33` |

나머지 source, theory, lease 및 plot source hashes는 final JSON에 있다. 검토 중 scientific source/input bytes는 변하지 않았다. Plot source는 identity만 확인했으며 plot 실행이나 visual QA는 이 worker의 범위가 아니다.

## 남은 주장 범위

수치 결과는 선택한 finite-support 함수족의 구현을 검증한다. 실제 isotope-resolved unsmeared gap의 pointwise cross section과 uncertainty enclosure, 15 eV 위 tail의 physical coverage, coupled feedback error bound는 OPEN이다. Rectangle envelope는 physical confidence interval이 아니며 ZA1969 comparator를 그 안에 포함시키지 않는다. 여섯 온도의 binary64 검사는 전체 연속 온도 영역의 엄밀한 오차 인증이 아니다. 실제 72-temperature production 결과는 root의 별도 한 번의 과학 실행에서 확인해야 한다.

Strong no-go를 주장하지 않는다. `HH_R10=OFF`, `production_admission=NOT_ISSUED`를 유지한다. 이 review가 발견한 implementation blocker는 없으며 다음 작업은 parent의 예정된 production study 및 저장 결과 기반 후처리다.
