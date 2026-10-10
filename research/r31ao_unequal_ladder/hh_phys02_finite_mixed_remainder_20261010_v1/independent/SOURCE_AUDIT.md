# HH-PHYS02 독립 source·implementation 감사

판정: **현재 선언된 frozen continuous source 범위에서 blocking source/implementation 오류를 발견하지 않았다.** 이 문서는 최종 decision review가 아니다. 감사자는 원 구현·검증 설계를 수행하지 않았고, owner 파일을 변경하지 않았다. 기본 cubic 결과는 PHYS01에서 계승하며 다시 감사하지 않았다.

## 대상과 근거

Canonical Astra v4 research core와 coding core, 새 `SCIENTIFIC_CONTRACT.md`, `src/frozen_source.py`, `src/jet_algebra.py`, `bound_remainder.py`, 원 source 5개와 선택 JSON을 읽었다. 핵심 확인 대상은 원 FT03/LCS 식의 전사, 52성분 hyperdual 확장계, time-series recurrence 및 유한 시간 tube/remainder 논리다. 과학 native job, BE root, ODE trajectory, 이전 parent suite 재실행, remote mutation은 모두 0회다.

검산 명령은 `python -B source_audit_checks.py`이며 최종 exit 0이다. 상세 결과는 `SOURCE_AUDIT_CHECKS.json`, 대상 파일 SHA256과 실행 기록은 `SOURCE_AUDIT.json`에 있다.

## Source 전사

| 항목 | 원 source | 새 구현 | 판정 |
|---|---|---|---|
| EOS와 전자밀도 | `hhe_events.rs` 133–159, `coupled_primary.rs` 97–131 | `frozen_source.py` 20–27, 42–45, 78 | `n_e=n_H x+n_He(y1+2y2)` 및 `Pi=1+r+x+r(y1+2y2)` 일치 |
| CI/RR fit | `ft03_rates.rs` 5–53 | 새 구현 47–65 | 세 종의 prefactor·power·exponential 일치 |
| RR thermal cooling | `ft03_rates.rs` 50, `ft03_controlled.rs` 114–119 | 새 구현 63, 88 | `k_B T alpha(3/2+dlogalpha/dlogT)`를 eV로 변환, H당 장부의 He 계수 r 보존 |
| 두 DR channel | `ft03_rates.rs` 51–61, `ft03_controlled.rs` 132–140 | 새 구현 66–71, 86–89 | HeII 소모 두 항과 서로 다른 thermal energy 일치 |
| 기체 분율 normalization | `ft03_controlled.rs` 91–147 | 새 구현 80–89, 97 | He 분율은 He당, 에너지는 H당이므로 energy에만 r가 곱해지는 구조 일치 |
| Photo source | `coupled_primary.rs` 134–213 | 새 구현 30–40, 91–96 | HI 사건율 `c n_H(1-x)sigma P`, excess heat, photon loss 일치 |
| Expansion work | `coupled_primary.rs` 239–247 | 새 구현 89 | `-2 H w` 보존 |
| HH | `hh_primary_extension.rs` 38–63, 108–111 | 새 구현 90, 93–94 | `n_H(1-x)^2 k_LCS(T)`, 추가 1/2 없음, 열 `-chi_H q` |

선택된 scalar parent 입력에는 **25개 photon bin**이 있으며 9개 active와 16개 exactly inert로 모두 보존되어 있다. 이 사실을 owner의 128×33 angular macro 전체에 대한 검증으로 확장하면 안 된다. Inert bin은 모든 원 sigma가 정확히 0이고 새 주입 bin도 아니므로, 상태를 변형하지 않는 상수 좌표의 제거다. 원 escape와 work 누적량 역시 gas/photon dynamics로 피드백하지 않으므로 x 응답 계산에 불필요하다. 이번 감사로 실제 전체 energy ledger를 인증하지 않는다.

`n_He`는 parent에 저장된 binary64 값의 exact-real 해석이다. 저장된 `n_He == binary64(n_H*f_he)`를 확인했으며, 새 모델은 `r=n_He/n_H`를 실수 연산으로 구성한다. 이를 `f_he`라는 다른 exact-real leaf로 교체하지 않은 것은 PHYS01 계약과 정합하다. 모든 숫자 literal은 먼저 같은 binary64 leaf로 읽고 이후 산술·초월함수는 Arb의 실수 enclosure로 수행한다. 원 native의 매 연산 rounding을 재현한다는 주장은 없다. DR의 compound constants도 선언된 leaf-expression 의미로 해석된다.

## 독립 실행 검산

원 Rust의 **단위 부피당 사건율을 먼저 계산하고 마지막에 분율/H당 에너지로 나누는 경로**를 mpmath 110자리로 별도 작성했다. 새 구현의 coefficient/rhs를 oracle에 재사용하지 않았다. 원 source와 숫자 계수 자체는 공통 authority이므로 물리 모형의 독립 검증은 아니다.

- 서로 다른 분율·photon stock·lambda/source를 가진 T≈35050, 49489, 59950 K의 3개 상태에서 39개 RHS 성분과 39개 coefficient 값을 검사했다. 모든 독립 reference scalar가 candidate Arb dyadic endpoint 안에 있었다.
- 두 변수의 비선형 polynomial field에 대해 SymPy exact Lie derivatives로 0–4차 time coefficients를 별도 구했다. 초기 lambda/source/mixed sensitivity를 모두 0이 아닌 값으로 설정하여, 단순 zero-seed로 가려질 수 있는 chain 항을 검사했다. 40개 scalar coefficient 검사가 통과했다.
- exp, noninteger power, reciprocal을 섞은 함수의 hyperdual 4성분을 직접 symbolic 미분과 비교했다.
- 원 6개 input/source byte identity, 25-bin partition 및 저장 density 관계를 확인했다.

총 **130개 scalar assertion**이다. 이는 130개의 독립 science test나 130개의 물리 상태를 뜻하지 않는다. 고정점 scalar comparison은 numerically checked이며 그 자체가 interval proof를 대체하지 않는다. Exact polynomial comparison은 generic algebra 구현에 대한 implementation verification이다.

최초 auditor test는 독립 scalar를 다시 같은 precision의 Arb ball로 변환하고 그 전체가 candidate ball 안에 들어갈 것을 요구하여 한 assertion에 실패했다. 이것은 reference conversion의 추가 radius를 포함하는 더 강한 조건이었다. 비교를 독립 110자리 scalar와 candidate의 exact dyadic endpoints 사이 비교로 고쳤으며 원 script와 실패를 보존했다. Candidate source는 수정하지 않았고 수정 후 모든 검사가 통과했다.

## Hyperdual·time recurrence·tube 논리

`HD` mixed slot은 factorial을 나누지 않은 `partial_lambda partial_s`다. 곱의 mixed 항에는 두 cross product가 각각 들어가고, reciprocal의 `2uv/a^3-w/a^2`, exp의 `exp(a)(w+uv)`, log의 `w/a-uv/a^2`가 올바르다. `Jet` time coefficient는 `time derivative/n!`이며 convolution·inverse·exp·log recurrence와 `z[n+1]=F[n]/(n+1)`가 이 convention과 일치한다.

HD에 parameter `(lambda,1,0,0)`, `(s,0,1,0)`를 넣으면 source forcing의 explicit derivatives와 상태 sensitivity의 chain terms가 함께 생성된다. Tube의 state/sensitivity 성분을 독립 구간으로 다루는 것은 상관관계를 버려 enclosure를 넓히는 방향이며, 필요한 실제 correlated trajectory를 제외하지 않는다.

최종 기록은 13개 동적 좌표 × 4개 HD 성분인 **52성분 모두 strict tube inclusion**, invariant-zero 예외 0개를 보고한다. 이 보고만을 PASS 근거로 삼지 않고 코드의 inclusion 의미를 확인했다. Box K 안에서 augmented field가 bounded이고 `Y0+[-1,1]|F_aug(K)|`가 K의 내부에 있으면, tau≤1인 최초 exit에서 적분식이 strict 내부를 강제하여 모순이다. 양의 T/Pi와 분율·photon domain을 유지하는 compact box에서는 source가 smooth하고 locally Lipschitz이므로 해의 존재·유일성과 tau=1까지의 continuation이 따른다. 별도의 contraction constant<1은 이 a-priori no-exit 논리의 필수 전제가 아니다.

Box에서 계산한 `jet[x][4].mixed`는 실제 mixed sensitivity의 네 번째 time derivative/4!를 포함한다. Taylor 적분 kernel은 양수이고 적분된 정규화 weight가 tau^4이므로, signed interval R4도 그대로 remainder/tau^4를 포함한다. 따라서 signed `c3+R4`와 symmetric `c3+[-B4,B4]` 두 표현 모두 타당하다. Fixed lambda/source에서 얻은 uniform sensitivity bound를 parameter rectangle에 적분하면 I/(lambda*s)의 동일 enclosure를 얻는다. lambda=0, s=0, tau=0의 정확한 0은 rectangle 정의로 별도 처리한다.

## 한계와 disposition

Blocking finding: **없음**. 이번 범위에 필요한 owner 수정 권고: **없음**. 40-digit 비방향 endpoint 문제는 owner가 이미 exact dyadic 및 outward decimal export로 수정 중이라고 전달했으며, 최종 읽은 코드에 그 수정을 확인했다. 별도 fix를 중복 수행하지 않았다.

다음 구분을 최종 보고서에 유지해야 한다: finite frozen continuous source enclosure와 실제 full/twohalf macro, time-dependent geometry/remap/birth, accepted root/family certificate, 전체 이력, atomic-rate physical adequacy는 서로 다른 주장이다. Local source에서 원점 이후 상태가 변하는 것은 허용되지만 n_H/n_He/H/E는 한 interval 동안 frozen이다. 25개 선택 scalar bin이 owner angular grid 전체를 대신하지 않는다.

최종 decision reviewer는 이 source audit를 보조 근거로 사용할 수 있으나, 이 문서 자체를 final PROMOTE 판정으로 부르지 않는다.
