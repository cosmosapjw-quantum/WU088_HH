# WU088_HH R31K-B: anchor 수렴과 성능 연구 결과

## 범위와 판정

반환된 R31K-A의 다섯 positive anchor와 B160/B192 총 10개 seal을 실제 복원했다. 전체 seal SHA-256은 사용자 SUMMARY와 일치했고, 내부 1,630개 payload의 크기·해시 및 1,440개 pair의 event 해시를 확인했다. 새 heavy pair 생성과 propagation은 하지 않았다.

H의 94-entry order-comparison은 다섯 점 모두 통과했다. 이는 두 quadrature order 사이의 증분 검사이며, continuum 적분오차의 엄밀 상계나 full49 admission은 아니다.

| z / a0 | max abs(H192-H160) / Eh | 실패 / 94 |
|---:|---:|---:|
| 0 | 1.6071490552228493e-9 | 0 |
| 16 | 3.001652817274341e-10 | 0 |
| 32 | 1.3889753324213497e-10 | 0 |
| 48 | 4.1613632450898254e-11 | 0 |
| 64 | 6.680493894159928e-12 | 0 |

원 기준 2e-7 Eh를 유지했다. NaN은 성공으로 계산하지 않으며, max(abs(H))끼리 비교하는 대신 94개 대응 원소를 직접 비교했다. 입력 dtype을 binary64로 낮추지 않았다. 각 쌍의 source identity는 n과 grid hash 외에는 동일하다.

현재 반환물에는 H와 O/D가 있지만 같은 z의 독립 dotO와 ionic 2×2 provider가 없다. 복원 가능한 R31E/R31G의 해당 snapshot은 z=8용이다. 따라서 새 다섯 anchor의 full49를 이번에 승인하지 않았다. 과거 “H가 오면 full49까지 바로 닫는다”는 안내는 이러한 독립 입력 의존성을 누락했다. 다른 geometry나 D+D†를 독립 dotO로 대입하지 않는다.

## 성능 원인: 관측과 추론 구분

스크린샷은 worker 종료 후 코어가 하나씩 비는 패턴과 정합하지만, 그 자체가 원인 증명은 아니다. 소스와 실제 events를 함께 검사했다. 현 orchestrator는 최대 12개 pair를 실행한 후 가장 늦은 pair를 기다리고, pool을 닫고, 이중백업 ACK를 받은 뒤 다음 wave를 연다.

z=64/B192에서 pair 시간은 8.678–75.404초다. 기록된 pair 비용을 기존 wave 구조에 대입한 compute-slot 활용률은 45.63%다. 실제 invocation에서 보고된 compute 합계는 859.13초, queue-to-ACK 합계는 627.94초다. 후자는 순수 전송시간이 아니라 upload, raw readback, rclone/제어 overhead가 합쳐진 지연이다. 두 항만 합쳐도 24.78분이며, 별도의 초기화·final-seal 시간은 포함하지 않는다.

따라서 느린 원인은 “CPU 수를 잘못 읽었다” 하나가 아니다. 비용이 다른 pair를 같은 wave에 묶는 방식과 강한 durability barrier가 함께 작용한다. RAM 부족이나 GPU 병목을 이 자료만으로 확정하지 않았다.

B160 비용으로 순서를 정하고 관측하지 않은 B192 비용으로 평가한 held-out trace model은 다음과 같다.

| z | 기존 compute-slot 활용률 | 재정렬 모델 활용률 | compute-only 모델 속도비 |
|---:|---:|---:|---:|
| 0 | 80.63% | 94.10% | 1.167 |
| 16 | 68.45% | 89.44% | 1.307 |
| 32 | 56.42% | 92.99% | 1.648 |
| 48 | 49.39% | 93.02% | 1.883 |
| 64 | 45.63% | 92.68% | 2.031 |

이는 실제 새 scheduler의 벽시계 benchmark가 아니다. pair 시간의 순서 불변을 가정한다. z=64에서 백업 지연이 그대로라면 전체 개선은 compute-only 2배보다 작다. geometry 하나를 통째로 제외한 내부 anchor 예측에서도 모델상 이득이 있었으나 실제 midpoint 성능은 아직 측정하지 않았다.

## 이번에 구현·실행한 후보

1. 같은 12-pair/ACK 정책을 보존하는 measured-cost descending scheduler. 입력 driver/model/geometry/규격과 cost-profile provenance를 기록한다. 완료된 source state는 다시 assemble하지 않는다. 실제 ProcessPool 경로를 작은 fixture로 실행해 순서·작업예산·ACK 차단을 검사했다.
2. affinity, package/core topology, cgroup CPU quota를 반영하는 resource intake. 실제 memory와 quota를 기록하며 오래된 PC 프로필의 RAM을 사용하지 않는다. process×kernel-thread 예산 초과를 거절한다.
3. Google Drive/Dropbox 두 전송을 병렬 진행하되 양쪽 raw SHA/size 검증 전에는 ACK를 기록하지 않는 helper. 실제 provider 성능시험은 하지 않았고 CLI-boundary fixture로 동시 진입, 한쪽 실패, 잘못된 raw readback을 검사했다.
4. Gaussian factor separation 및 exact-zero mask caching을 적용하고 독립 gamma plane을 OpenMP로 계산하는 native candidate. 각 plane 내부 및 최종 h 순서의 compensated sum을 보존한다. frozen scalar recurrence, binary128 branch, even-power analytic kernel은 바꾸지 않았다.

샌드박스는 5900X가 아니라 Intel Xeon 8370C, 관측 CPU quota 4 cores다. 실제 frozen107 B32/g80, primitive(0,0)의 foreign component에서 다음 중앙 wall time을 얻었다. 조건당 2회 측정이므로 통계적 성능 인증은 아니다.

| z | reference 1 thread | candidate 1 thread | candidate 2 threads | candidate 4 threads |
|---:|---:|---:|---:|---:|
| 16 | 2.0159 s | 2.0092 s | 1.0364 s | 0.6872 s |
| 64 | 2.6040 s | 2.5737 s | 1.3721 s | 0.9216 s |

복원된 원래 .so와 같은 소스를 새로 컴파일한 reference도 이 입력에서 일치했다. candidate/reference 및 thread 수 변화 모두 값과 sumabs의 numerical-array exact equality를 유지했다. 이 결과는 H0 전체, 94개 H contraction, 160/192 science-resolution sweep 또는 전체 job throughput을 검증한 것은 아니다. 4-thread의 CPU time은 증가할 수 있으므로, 12개의 outer process 모두에 4 threads를 주지 않는다.

## 벡터화와 버린 최적화

GCC의 실제 vectorization report에서 hot long-double/complex loop에 대한 `no vectype` 및 `vectorized 0 loops`를 확인했다. NumPy longdouble은 여기서 64-bit significand이고 일부 scalar 경로는 113-bit binary128 연산이다. binary64 SIMD/GPU 경로로 바꾸어 속도만 측정하는 것은 이번 정확도 계약을 보존하지 않는다. 현재 SIMD 개선을 달성했다고 주장하지 않는다. compiler report와 SoA형 batch 경계를 보존하고 독립 작업 병렬화를 우선했다.

하나의 order-9 Boys seed를 wide complex strip 전체에 재사용하는 후보는 반례를 얻어 기각했다. x=32i의 이론적 seed-error 증폭률은 약5.23e8이며, 실제 scalar 오차는 기존 약1.12e-20에서3.86e-13으로 커졌다. 기존 독립 seed 경로를 유지한다. 상세 유도는 MATHEMATICS.md와 BOYS_RECURRENCE_COUNTEREXAMPLE.json에 있다.

## 남은 gate

- 실제 host의 process/thread throughput과 반복 성능 측정. component 개선을 전체 속도비로 승격하지 않는다.
- 새 native candidate의 science-resolution/all94 회귀와 독립 decision review. 그 전에는 production provider에 설치하지 않는다.
- 각 새 z의 독립 dotO 및 ionic provider source/array 확보, 이후 raw full49 gate.
- 그 다음에만 R31J direct midpoint, interpolation, endpoint/trajectory gate. propagation과 production admission은 계속 false다.

현재 검토는 owner self-review와 분리된 계산 경로/Wolfram 검산이다. 독립적인 최종 심사자가 검토했다고 주장하지 않는다.
