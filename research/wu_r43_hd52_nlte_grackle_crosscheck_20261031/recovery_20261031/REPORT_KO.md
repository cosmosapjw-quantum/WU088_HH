# R43 복원본 | 실제 물리 데이터 및 결과 판정

**원본 재사용:** EMAA RADEX SHA256 `b0db1613425e403889c3a74f6cd9e142c562a552f1ebf05e61cbf509cd429c94` 및 원본 parser SHA256 `c982bdd3a1dcf61bbd734295a68b2162b536068f4f65eb9e18ff188dd774252b`. 실제 널리 쓰이는 비교 구현 Grackle rate_functions.c git blob `dfbab661e7c45981eed750baebff140849917152`. 원저자 비공개 데이터나 H⁺ 상위준위 충돌률 없음.

## 실제 새 복원 계산

- 15개 원본 H 충돌온도, 4가지 원자 H 밀도와 5가지 고정 흑체 경계: 300 조건.
- H와 H⁺가 원본 온도에서 겹치는 정확한 T=5K의 24조건. 합계 **324** 조건.
- 정상상태 HD52 점유율 **16,848**행, 원본 Einstein-A 서명부호 광자 선에너지 **119,232**행, Grackle 저밀도/LTE fit **15**행과 case summary **324**행. 합계 **136,419 derived data rows**.
- 이번 explicit 그리드 부호표: 냉각 **224**, 가열 **100**, 균형 **0**. 구 R43 체크포인트 236/88과의 차이는 source grid identity 미복원으로 **UNRESOLVED**; 현 결과의 수치 자체를 소급변경하지 않음.

## 대표 물리 수치 (J/s per HD)

- Tgas=70K, nH=1e4 cm⁻³, 외부 복사 OFF: `2.89011448433220428e-29`.
- Tgas=70K, nH=1e4 cm⁻³, 흑체 z30, Trad=84.4905K: `-1.49355035599876869e-29` (**순 가열**).
- Tgas=100K, nH=1e4 cm⁻³, z30: `1.93081506923182274e-29` (**순 냉각**).
- Tgas=200K, nH=1e4 cm⁻³, z30: `2.11290624823343013e-28` (**순 냉각**).

## 그랙클 비교 (저밀도, H-only, nH=1, radiation OFF)

| Tgas K | EMAA / Grackle HDlow | EMAA / Grackle HDlte (LTE comparison) |
|---:|---:|---:|
| 70.0 | 1.00739693 | 0.88326302 |
| 100.0 | 0.93672762 | 1.00776811 |
| 400.0 | 1.04173505 | 1.15396086 |
| 2000.0 | 0.93184368 | 1.00646509 |
| 5000.0 | 0.73781091 | 0.55965383 |

## 검증

- 복원 정상 Python 테스트 **27/27 PASS**, -O **27/27 PASS**.
- source-private original bytes SHA LOCK, 52준위 368 Einstein-A, H1326×15 T, H⁺171×25 T.
- 상세평형, K 열합, 정지해 p≥0, ∑p=1, photon energy = collision gas energy, 80-digit mpmath full 52×52 sanity check.
- **clean replay 5/5 byte-identical**, 4 PNG + 4 SVG original-data plots.
- 과거 R43 master SHA256 `58c4c095d6f3601a8251cf2e94db74d1b3dbe00ac48d2b01912517c5ce62310a`와 새 source recovery master는 **byte identity 주장 불가**. 이번 범위는 새로운 source-equivalent archive identity.

Canonical WU DAG **34/49 +0**, auxiliary R43 1/1 scoped recovery. R/C 18/20 scoped, distinct author R6/C9 NOT_RUN, HH_R10=OFF, L4=false, PRODUCTION=HOLD, AUTO_NEXT_NODE=false.
