# PHYS90 독립 C9 사전 정적 검토

## 판정

`PASS_STATIC_MATH_AND_EXECUTION_PATH_PENDING_T1_CLAIM_FIX`.

계산식·integer scaling·shared-source covariance·resume·원 lease API 사용에서 blocking 오류는 찾지 않았다. 실행 전 필요한 수정은 아래 한 건이다. 과학 모듈을 import하거나 실행하지 않았으며 실제 C6–C8 결과의 수용은 이후 원 출력 readback으로 판단한다.

## 필수 finding P90-C9-01 — radius 1의 인증 결과를 출력에 반영

- **대상:** `source/primary.py`의 RESULTS `full_PSD_compatibility='UNRESOLVED'` 고정값.
- **근거:** `checkpoints[1]`은 모든 singleton과 pair에 대해 t=1에서 exact 판정을 한다. 하나라도 실패하면 R6에서 확인한 필요조건에 의해 실제 B₁∩PSD=∅가 증명된다.
- **영향:** 이런 실제 결과가 발생해도 현재 출력은 확보된 유한 배제 근거를 미해결로 분류한다. 반대로 pair 모두 통과한 경우에는 전체 PSD를 미해결로 유지해야 한다.
- **최소 수정:** radius를 명시한 `at_t1_full_PSD_compatibility` 등의 필드에 실패 시 `INCOMPATIBLE_BY_PAIR_OR_SINGLETON`, 모두 통과 시 `UNRESOLVED`를 기록한다. 실패 시 exact singleton/pair witness를 함께 저장한다. Unknown global PSD threshold와 t=1 compatibility를 다른 필드로 둔다. 독립 reference에서 상태·witness가 exact t=1 scan과 일치하는지 대조한다.
- **발견 경로:** root의 초기 finding과 independent reviewer가 실제 코드를 대조해 동의했다. 이 수정은 frozen contract의 `UNRESOLVED_UNLESS_ACTUAL_CERTIFICATE`에 따른 출력 교정이며 물리 source admission을 변경하지 않는다.

## 검사한 실제 경로

### 정확한 source 판정

`load_inputs`는 부모의 원 decode 산출물 두 개를 읽으며, identity 경로가 size/SHA를 먼저 확인한다. Packed upper triangle과 matrix 대응을 exact Fraction으로 비교하고 같은 순서로 H를 대칭 배치한다. 새로운 ENDF decoder나 eigensolver는 호출하지 않는다.

`PairTable`은 F와 H의 모든 denominator의 LCM을 공통 양의 integer unit으로 사용한다. t=p/q에서 각 항은 공통 scale·q를 곱한 exact numerator다. 따라서 `z*z > x*y`는 rational determinant의 음수 여부와 동치이며 equality를 pass로 처리한다. n(n−1)/2=11628 쌍과153 singleton이 빠짐없이 생성된다. `x<0 or y<0`가 별도로 있으므로 음수 대각의 곱이 양수가 되는 경우에도 잘못 통과하지 않는다.

`bracket`은 t=0과1을 검사하고 상한4096까지 doubling한다. Zero baseline은 [0,0]으로 종료한다. Bracket이 확보되면 failed lo와 all-pair-pass hi를 보존하며40회 exact dyadic 갱신을 수행한다. 마지막 폭이 initial_width/2^40임을 exact 확인한다. 4096 실패는 lower-bound-only로 반환한다. 음수 singleton을 먼저 witness로 선택하므로 pair witness의 `maximum_determinant`는 비음수 upper diagonal 영역에서 사용된다.

### 공유 원소·보존·제조 fixture

`support`는 upper off-diagonal마다 `abs(ui*vj+uj*vi)`를 한 번 사용한다. `covariance`는 한 공통 C에 대해 LCLᵀ를 계산한다. 제조된8개 vertex에서 같은 q에 대해 모든 K row sum을 exact 확인하고, cross radius2, marginal maxima12/12, joint maximum20 및 두 maxima의 공동 불가능성을 확인한다. 별도 diagonal covariance mutation은 보존을 깨는 것으로 거부한다.

3×3 제조 fixture는 모든 pair 통과와 공통 w의 upper quadratic −21/10을 함께 확인한다. 실제153 자료의 global compatibility와 혼합하지 않는다. Actual sparse probes의 중심은 부모 완료값으로 명시적으로 재사용하고 새 support만 계산한다.

`guards`의 마지막 두 결과는 같은 primary 호출에서 먼저 수행되는 fixture assertions에 의존한다. `fixture=fixtures(); guard=guards()` 순서와 create-only final manifest 때문에 fixture 실패 시 이 guard들이 통과 산출물로 게시되지 않는다. 다른 정의역·형상·부호·identity guards는 해당 동작을 직접 호출한다.

### 독립 reference

`reference.py`는 production kernel/primary를 import하지 않는다. 각2×2 block마다 별도 LCM을 만들고 independently written determinant path로 exact 판정한다. 모든 저장 checkpoint에서 모든 pair와 singleton을 재대조하고, t=0/1의 전체 실패 목록, 마지막 bracket·witness, 새0,10 radius식, 제조8vertices와9support entries를 확인한다. Decimal100을 사용하지 않아 이전 R6의 finite-precision sign 의무가 발생하지 않는다. 여기서 reference 실행은 새 PHYS90 결과의 독립 검증이며 원 PHYS89 decode/eigh campaign의 반복이 아니다.

### 재개·출력·실행 자원

두 entrypoint는 `identity()` 후 `--resume` 분기로 먼저 들어가며 `compute`/`audit` 안의 scientific imports 전에 종료한다. `sys.dont_write_bytecode=True`와 metadata-only evidence 경로가 사용된다. Reference skip은 자신의 산출물 외에 부모 primary manifest SHA와 모든 payload도 검사한다. 새 출력 폴더와 MANIFEST는 create-only이며 실패 폴더를 덮어쓰지 않는다.

Wrapper는 원 PHYS88 vendor gate SHA 및 계약 SHA를 확인하고 원 `LeasePool`, `_lease_lock`, `_live_leases`, `_cgroups`, `release_lease`만 실행 경로에서 호출한다. 원 module의 과학 runner는 정의되지만 호출되지 않는다. 기존 `/tmp/rei-bianchi-cooperative-leases`, CPU0 child/CPU8 coordinator, child20CPU/45wall초,1worker/thread,1.5GiB reserve+0.5GiB job를 유지한다. Live peer가 관측되면 child0으로 반환하며 lease acquisition 뒤 fresh memory를 다시 확인한다. 타 owner의 process 또는 lease를 종료하지 않는다. Advisory prelaunch 관측은 이후 peer가 절대 발생하지 않는다는 전역 claim으로 사용하지 않는다.

## 검토 대상 바이트

| 파일 | SHA-256, 수정 전 정적 snapshot |
|---|---|
| `source/evidence.py` | `9ffae0badb802a02481b8659db89342c6a4e5eead88bd62c92d1c45f7262ed2e` |
| `source/kernel.py` | `ae500b266d7ec92e29ae5cf12843f607359bc052c239e53aedb6bdfca649d6ce` |
| `source/leased_call.py` | `7e19f09c27a07075089e4d47286aec463e10469ed9bc821549a8332424b22d08` |
| `source/primary.py` | `1ff36c2d05750ad70597369dc1176277a4c25a99cf25ef131b424148053eb4a5` |
| `source/reference.py` | `635a86dfb419c2b19e9faf60109ff122d09ece57be06e0350d32c2271ebd1713` |
| `implementation/MAP.md` | `f289103dffb0533d711081f290d3c27c66c00ea663f750cafbe65cd0d12e4f4d` |

FROZEN_FILES는 root의 다음 S1 작업이므로 이 정적 snapshot 시점에는 아직 없다. 최종 freeze 후 source identity와 actual 실행·산출물을 한 번 읽어 C9를 결속한다. 이번 검토 scientific 실행·원격 변경0, budget reset=false다.

## 수정 readback — P90-C9-01 CLOSED

구현자가 root 승인 아래 수정한 실제 diff를 읽었다. `primary.py`는 t=1 singleton/pair 실패 시 `at_t1_full_PSD_compatibility=INCOMPATIBLE_BY_PAIR_OR_SINGLETON`와 exact witness를 기록하고, 모두 통과 시 `UNRESOLVED`와 null witness를 기록한다. `full_PSD_threshold=UNRESOLVED`는 별도다. 독립 reference는 자신이 계산한 첫 실패 singleton/pair와 witness의 모든 정확한 수치 또는 null을 비교한다. Radius와 전체 threshold의 의미가 분리됐으며 필요한 수정이 닫혔다.

구 `hi_is_full_PSD_upper_bound=False` 필드는 제거됐고, pair bracket의 `hi_all_pair_pass=True`만 남았다. 이 수정은 알려지지 않은 global threshold의 실제 대소관계에 관한 boolean 해석을 피하며, 계약·이론의 upper-bound claim 제한을 유지한다.

| 수정 후 파일 | SHA-256 |
|---|---|
| `source/kernel.py` | `8fb7cfb9f8e424c7d71f41c1944a2ed3dde4d459ec764be95fd1f8dadd92ee01` |
| `source/primary.py` | `f0880bedef8363384f6bf5a160ec551000077828aab6253a1bedd68fb2d96e42` |
| `source/reference.py` | `f1414559cb71bde7e4976abb5ce0cf5102a625329c10decc6cec7be4c64bee1a` |
| `implementation/MAP.md` | `24dd689febda3898cf78950c47eca1ddfa6eb3cbc98efa8d974bc172bde0e420` |

`evidence.py`와`leased_call.py`는 위 최초 snapshot과 같다. 수정 전 source는 `implementation/history_preexec/t1_classification/`에 보존됐다. 과학 실행은 없다.

**최종 사전 정적 판정: `PASS_STATIC_READY_FOR_S1_FREEZE`.** 필수 finding은0개가 남았다. 최종 C9 scientific admission은 실제 결과와 독립 reference의 원 출력, 실행·resume 영수증을 받은 뒤에 판정한다.
