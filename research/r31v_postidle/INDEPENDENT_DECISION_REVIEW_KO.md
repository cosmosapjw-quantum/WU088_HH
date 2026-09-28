# WU088_HH R31V bounded M3B 독립 decision review

기준 실행은 NCP run `20260928T132239Z_r31v`, core commit `2d352253b0e6d36b04b4e696985276508e684c77`, 게시·백업 receipt commit `ce66c4c695cb9716d76325c59aaed98a4b1e70c8`이다. 이 검토는 실행 세션과 분리하여 GitHub에 게시된 raw/result/source-build evidence와 현재 runner를 읽어 수행했다. 새 native 계산이나 새 scientific node는 실행하지 않았다.

## 판정

bounded B192/M3B 측정 자체는 **`ACCEPTED_FOR_BOUNDED_B192_PERFORMANCE_SCREEN`**으로 닫는다. 동일 ordered workload 132 tasks가 모든 layout의 3회 반복에 사용됐고 benchmark reference cache는 12/12 hit, miss 0이었다. 12개 timed row 전부 exactness와 worker affinity/OpenMP team 검사를 통과했고 throttling, swap, memory event는 기록되지 않았다. source/build/H0/seed/기존 exactness/pilot identity도 기록과 일치한다.

이 판정은 production admission이 아니다. live census에서 다른 scientific native pool은 보이지 않았지만 host isolation은 독립적으로 인증되지 않았고, shared ancestor에 다른 세션·서비스가 존재했다. 따라서 `production_admitted=false`, candidate provider 미승격, full49/trajectory/M5 잠금을 그대로 유지한다.

## 성능 해석

| layout | median tasks/s | mean tasks/s | sample CV |
|---|---:|---:|---:|
| 32x2 | 0.8240526251 | 0.8198136074 | 0.899% |
| 30x2 | 0.7988149949 | 0.7988316816 | 0.427% |
| 64x1 | 0.7482704578 | 0.7463039066 | 0.603% |
| 4x16 | 0.5528319374 | 0.5530670271 | 0.096% |

이 bounded B192 screen에서 32x2의 median은 30x2보다 3.159%, 64x1보다 10.128%, 4x16보다 49.060% 높다. 세 32x2 반복값은 세 30x2 반복값 모두보다 높았다. 따라서 **동일 host에서 exclusive B192 wall-clock throughput만 목적이라면 32x2를 현재 provisional candidate로 유지할 근거는 충분하다.**

다만 32x2를 전역적 또는 production-final configuration으로 고정할 근거는 아직 부족하다. configuration 순서가 interleaved/randomized되지 않았고 반복은 layout당 3회뿐이며 host isolation도 독립 인증이 아니다. 또 logical-slot당 throughput은 30x2가 32x2보다 약 3.40% 높으므로, wall-clock 최소화와 CPU-slot 효율은 같은 목적함수가 아니다.

R31T M3A에서는 n=160 및 다른 task-count/histogram 아래 64x1이 1.2543 pairs/s, 32x2가 1.2208 pairs/s였고, 이번 B192 fixed workload에서는 순서가 뒤집혔다. 이는 모순이 아니라 workload/n 의존성을 보여주는 증거다. M3A ranking을 B192에, 또는 B192 ranking을 다른 node에 수송하지 않는다.

## 코드 검토 finding과 수정

현재 evidence를 무효화하는 수치 오류는 찾지 못했다. 다만 pre-hardening `m3_postidle.py`의 receipt 검증은 두 곳에서 provenance binding이 더 강할 수 있었다.

1. full-pair exactness receipt의 필수 row를 `n + pair + all_exact`로 확인했지만 row의 `g=80, z=2.0`을 명시적으로 다시 묶지 않았다.
2. B192 memory pilot은 `stage/n/status/private`을 검사했지만 `g=80, z=2.0` 및 실제 1x1 exact resource-screen 세부를 모두 재검사하지 않았다.

이번 실행에 사용된 실제 두 receipt를 직접 확인하면 해당 값은 모두 올바르다. 따라서 이는 **완료된 M3B를 무효화하는 evidence mismatch가 아니라 future-reuse provenance hardening**으로 분류한다.

이를 위해 branch에 다음 commit을 추가했다.

- `45ca6b03566307f0946ee883371ff17adeb1cae6`: pilot을 B192/G80/z2 및 1x1 exact resource screen에, exactness rows를 n/g/z/pair에 명시적으로 결합.
- `830390f9bf319d8589f700ad116119c36e335407`: 새 geometry-binding tests 추가.
- `187002d7340079ea582eb841cc6ff3d600e2fd67`: pilot resource-screen rejection coverage 보강.

이 세 commit은 repository-published 상태지만 이 검토 시점에는 실제 NCP pytest를 다시 실행하지 않았다. 그러므로 **implementation hardening은 코드·테스트 작성 완료, runtime revalidation 미완료**로 기록한다. 기존 NCP의 84 PASS를 새 HEAD의 PASS로 소급하지 않는다.

## 다음 최소 행동

완료된 B192/M3B raw evidence를 보존하기 위해 heavy benchmark를 다시 돌릴 필요는 없다. 먼저 NCP에서 새 hardening에 대한 focused pytest만 재실행한다. 이것이 통과하면 bounded M3B review node는 닫을 수 있다.

실제 production layout을 이 단계에서 하나로 동결해야 하는 경우에만 32x2와 30x2 두 후보를 같은 132-task cache-only workload로 interleaved하게 재확인한다. 64x1, 4x16, M3A 또는 새 scientific node를 그 이유만으로 반복하지 않는다. production admission, shared HH/HE/CR layout, z=1/z=0.5/full144/trajectory/M5는 별도 gate로 남긴다.
