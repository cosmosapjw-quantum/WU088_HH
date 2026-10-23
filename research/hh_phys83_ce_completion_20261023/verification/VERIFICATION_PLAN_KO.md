# PHYS83 continuation 독립 검증 설계

이 문서는 새 수치 실행 전에 작성한 검증 설계다. 실행 성공 여부와 source identity는 각 create-only `START.json`, `checks.jsonl`, `RESULT.json` 및 최종 독립 검토 보고서로 판정한다.

## 원래 문제와 검증 대상

검증 대상은 source-native H I LS `1s ↔ {2s, 2p}`의 유한 CCC W-PL collision operator, 고정 `T/ne`의 ground-start star, gross excitation/deexcitation/radiative counts 및 분리된 thermal/atomic/radiation energy ledger다. 소스와 물리 계약은 S0에서 상속했다. 수치 검증을 위해 계약의 온도 범위·과학 grid·허용 오차를 바꾸지 않는다.

기존 7개 symbolic 결과와 902개 raw printed-rounding reciprocity checks는 `REUSED_NOT_REEXECUTED`다. 기존 PHYS82 및 다른 완료 identity의 science를 호출하지 않는다. 별도의 nuclear verifier는 새로 공급한 합성 scalar energy record만 사용하고 PHYS81의 실제 radiative-capture event나 rate를 호출하지 않는다.

## 독립 계산 경로

| 대상 | 구현의 경로 | 독립 reference | 동결 gate |
|---|---|---|---|
| `M0, M1` | 기존 positive normalized-cell moment helper를 사용하는 W-PL 합 | 원본 forward 파일을 별도 parser로 읽고 decimal source knot 차이를 만든 뒤 각 cell의 exponential-polynomial integrand를 직접 QUADPACK 적분 | relative `1e-10` |
| up/down rates·selected energy | common M0와 threshold Boltzmann factor | 독립 quadrature의 `M0/M1`과 명시한 단위 상수 | rate relative `1e-10`, log balance absolute `2e-12` |
| exact T derivative | moment identity | 독립 quadrature mean 및 5-point log-rate finite difference; domain 끝에서는 one-sided stencil | scaled `1e-7` |
| transient population·occupation integral | 두 감쇠 root와 안정화된 entire function/divided integrals | mpmath 80자리의 6×6 augmented 3-state generator exponential | population absolute `2e-12`, resolved relative `1e-8` |
| gross counts·energy | integrated occupation에서 구성 | 독립 augmented generator의 occupation으로 각 사건과 signed energy를 별도 구성 | resolved relative `1e-8`, gross-normalized raw energy residual `2e-11` |
| steady state | 닫힌 ratio 식 | mpmath 80자리 generator balance + nuclei sum 선형 시스템 | population absolute `2e-12`, relative `1e-8` |
| repeated/near roots | bivariate series 또는 gamma-moment expansion | mpmath 80자리 smooth-kernel 직접 적분과 exact repeated-root limit | relative `1e-10` |

`resolved`는 transient reference의 절댓값이 `1e-280` 이상인 값으로 명시한다. 따라서 macroscopic population만을 검사하는 것보다 강한 relative 조건이며, population absolute gate도 함께 적용한다. exact zero는 별도로 검사한다. 검증자가 production `_moments`, incomplete-gamma formula, production spectral solution을 reference로 호출하지 않는다.

## 경계 사례와 규모

Rate 온도는 `255, 777, 3500, 12000, 25370.66308424773, 50000 K`, 2개 channel의 총 12쌍이다. Population 관련 reference는 transient 28개, steady 6개, root-helper 6개로 총 40개다. Transient는 `3500 K`, `25370.66308424773 K`, `ne=0, 1, 1e8, 1e12, 1e18 cm^-3`와 `t=0, 1e-20, 1e-12, 1e-8, 0.1, 1e3 s` 중 사전 선택한 조합을 포함한다.

READY 후 첫 실행 전에 `FROZEN_STAR_STATIC_REVIEW_KO.md`가 지적한 실제 분기 경계 위험을 반영했다. 네 synthetic named cases 중 두 개를 각각 `fast*t=1/2`, `gap/slow=1/4`의 좌우 reference 쌍으로 변경했다. 따라서 helper reference가 최초 준비안의 4개에서 6개로 늘었으며 전체 40개는 배정된 bounded 범위 안이다. 이것은 첫 수치 실행 전의 coverage 구체화이며 kernel, 과학 grid 또는 gate 변경이 아니다.

원래 과학 실행의 `132 rate / 324 steady / 732 transient` grid는 이 verifier가 실행하지 않는다. 새 cosmological ODE, benchmark, completed science identity replay도 0이다. 이 검사 집합은 샘플에 대한 증거이며 continuum certificate가 아니다.

## 계약 guard와 물리 mutant

- 네 raw source의 SHA와 forward/reverse shape, W 구성, endpoint, source 배열 및 dataclass immutability를 확인한다. 원래 902개 reciprocal-print 검사를 반복하지 않는다.
- 온도·density·time의 scalar/domain, species/level, finite-source scope, common T, 실제 q와 log-q의 일치, underflow flag 및 radiative-owner 충돌을 거부해야 한다.
- 이미 검증된 transient 값으로 `모든 excitation을 즉시 escaped cooling으로 처리`하는 mutant와 `two-photon event가 2Δ를 방출`하는 mutant를 구별한다. 같은 값을 재사용하므로 이 점검을 위해 별도 transient를 돌리지 않는다.
- 초기 정적 검토에서 발견한 mutable-construction 경로의 q/log 불일치와 NaN-log 통과 위험은 `PREVALIDATION_GUARD_FINDING.json`과 초기 source snapshot으로 보존한다. 수정된 guard는 독립 negative-input 검사에 포함한다.

## Detached nuclear adapter

별도 `independent_verify_nuclear.py`는 Decimal 80자리 reference로 공급된 사건의 signed residual, 모든 에너지 성분의 같은 가중 평균, zero-measure 반환, huge/subnormal weight 처리를 검사한다. Fast-first capture 뒤 stopping과 잔여 에너지 assimilation을 각각 한 번 적용한 ledger가 명시적 prompt-thermal ledger와 일치해야 한다. 입자 수와 에너지는 별도로 검사한다.

Thermal EOS는 `u=(3/2) n k_B T`를 독립 미분해 단위와 number source 항을 확인한다. 조건부 NR pair energy는 COM Maxwell energy와 derivative-selected relative energy를 더해 검사한다. 이 검사는 실제 finite-T event distribution, on-shell four-vector/frame construction, isotope stoichiometry, nuclear rate 또는 stopping law를 제공하지 않는다.

## 실행·보존·수정 규칙

실행은 parent의 READY 및 shared resource lease 지정 뒤에만 한다. Worker/thread는 각각 1이다. 각 attempt directory는 create-only이고 입력 SHA, runtime, lease receipt, 개별 assertion, pass/failure 및 unfinished case를 기록한다. 실패 시 첫 failing case에서 멈추며 실패 자료를 지우거나 덮어쓰지 않는다.

수정 뒤에는 dependency가 바뀐 case와 아직 실행하지 않은 case만 선택한다. 완료된 unaffected case는 명시적인 `--reuse-passed-from`으로 identity와 원래 result SHA를 보존해 재사용할 수 있다. 이미 확인한 transient payload를 mutant 판별에 다시 쓸 수 있으므로 그 목적으로 scientific callback을 재실행하지 않는다.

HH_R10=OFF. Production admission NOT_ISSUED. Source interpolation/tail·physical uncertainty, 실제 high-density atomic completeness 및 coupled thermal/charge/geometry는 이 검증의 승인 범위 밖이다.
