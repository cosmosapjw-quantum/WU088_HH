# WU088_HH R31V NCP RETURN — 다음 연구 스레드 인계

## 판정

R31V opt-in adapter의 bounded B192/M3B 고정 132-task 비교를 실제 NCP VM에서 완료했다. `prepare`와 `benchmark`는 서로 다른 create-only output에서 각각 exit 0으로 끝났고, 최종 runner 상태는 `BOUNDED_COMPARISON_COMPLETE_REVIEW_REQUIRED_NOT_PRODUCTION`이다. 독립 decision review와 production/provider admission은 수행하지 않았다. 현재 결과의 최상위 중앙 throughput은 **32x2, 0.824052625 tasks/s**이다. 기존 M3A는 다른 workload이므로 이 순위를 M3A에 소급하지 않는다.

| layout | 반복 벽시계 초 | 반복 tasks/s | 중앙 tasks/s |
|---|---|---|---:|
| 64x1 | 176.407, 178.101, 176.120 | 0.748270, 0.741153, 0.749488 | 0.748270 |
| 32x2 | 160.184, 160.178, 162.701 | 0.824053, 0.824085, 0.811303 | 0.824053 |
| 30x2 | 165.948, 165.245, 164.537 | 0.795430, 0.798815, 0.802250 | 0.798815 |
| 4x16 | 238.771, 238.408, 238.829 | 0.552832, 0.553673, 0.552696 | 0.552832 |

모든 12 timed row는 동일한 ordered workload hash `a9e725ea97b26f3368f04b434e0ceb53248078451c0ecba6ad2c2f68500667b8`, 12 unique pair × 11회, 132 tasks를 실제 수행했다. 각 layout에 3회 반복을 공급했으며 timed 결과를 재사용하거나 reference cache miss에서 reference를 계산하지 않았다. 전 row에서 reference 대비 H0/H0_sumabs/foreign/foreign_sumabs가 exact이고, worker affinity·OpenMP team이 계획과 일치했다. throttling, swap, memory event는 모두 0이었다. leaf 및 공유 조상 CPU delta는 원시 row에 따로 있다. 공유 조상 사용량을 HH 전용 사용량으로 합산하지 않았다.

`prepare`에서 12 cache miss를 명시적 serial full-pair reference 계산으로 채웠고 합계 515.134초였다. `benchmark`에서는 같은 numeric context의 12개 entry가 모두 cache hit였다. 준비 12회, warmup 130회, timed 1,584회는 성능 반복용 full-pair 호출이며 **새 scientific node 0개**다. full-pair당 H0 native 2회와 foreign native 1회로 계산하면 총 5,178 native calls이다. timed wall 합계 2,225.428초, worker CPU 합계 96,723.145초이며, 전체 benchmark 명령은 약 2,419.346초 걸렸다. 서로 다른 단위의 throughput이나 공유 CPU 사용량을 더하지 않는다.

## source, host, 실패 분류

게시 기준 remote HEAD/tree는 `e7248a2b356392a47bda44d180e0d6ed4f012b20` / `ee48d47da111b46daeba6a037833ca8242c963e6`였다. 기존 R31T worktree는 건드리지 않고 별도 R31V worktree를 사용했다. baseline ancestor `ff3db87...` 도달성과 R31V 파일 manifest 14개 SHA/size를 확인했다. 실제 현재 source는 기록된 build JSON의 source hash와 같고 reference/candidate `.so` bytes, H0 binary/source, grid seed, 기존 B192 pilot 및 6개 full-pair equality receipt가 일치한다. GCC 13.3.0 strict flags, Python 3.12.3, NumPy 2.3.5, longdouble 64-bit significand/16-byte storage, FE_TONEAREST였다. CPU는 Intel Xeon Gold 5220, 허용 affinity 0–63, 보이는 quota는 max였다. 자세한 digest는 `SOURCE_BUILD_AUDIT.json`과 `RETURN.json`에 있다.

초기 시스템 `python`은 없어 exit 127, 시스템 `python3`에는 pytest가 없어 exit 1이었다. NCP venv로 수정 전 새 67 tests 및 관련 M3 14 tests가 통과했고, 좁은 수정 후 합친 84 tests가 통과했다. H0 cache 사전 검사가 `g++` symlink와 realpath의 서로 다른 version 문자열로 cache miss를 오판하는 결함을 재현해 realpath를 사용하도록 고쳤다. 또한 build source/실제 `.so` 해시 검사를 runner에 추가하고, 측정 후 gate 실패 row를 checkpoint에 남기며, 각 반복의 공유 조상 CPU delta를 기록하도록 했다. 과학적 수치 불일치, 자원 gate 실패, timeout·interrupt는 이번 새 실행에서 0건이다. 전체 repository scientific suite는 dependency 변경이 없어 반복하지 않았다.

live census는 boot ID `dd4da6c2-df05-4f9d-a7e3-7aef130569dc`의 실제 PID/PPID/명령/스레드/affinity 및 leaf·조상 cgroup/quota/memory/swap을 읽어 SHA `9ceaa8fbd31c7860ade477271483a020c8bc16959ec8ddb96242cbe315a6fed6`로 보존했다. 관측 시 다른 과학 native pool은 없었고 측정 중에도 별도 pool이 나타나지 않았다. 이 순간별 관측을 미래의 독립 host isolation 인증으로 승격하지 않는다. 다른 Codex CLI/시스템 서비스는 공유 조상에 존재하므로 측정 row의 `other_session_cpu_upper_seconds`를 별도 보존했다. grant는 만료형 `BENCHMARK_EXCLUSIVE`의 이 bounded 비교에만 적용한다.

## 보존과 다음 단계

H0 authority, B160 M3A, B192 pilot, 6 full-pair equality 및 오염된 기존 M3B 기록은 유지했다. bass_cr F1-R2와 BASS_HE resume-004는 재실행하지 않았다. z=1, z=0.5, full144, trajectory, M5, production admission, main merge 및 타 owner PID 조작은 하지 않았다. H 수렴만으로 full49를 승인하지 않았다.

원시 출력은 `m3b_132.json`, reference 이력은 `reference_prepare.json`, 반복별 검토는 `MEASUREMENT_REVIEW.json`, 실제 명령과 exits는 `COMMANDS.md`, 기계 판독 인계는 `RETURN.json`에 있다. 다음 최소 node는 이 비교와 host 독점성 증거에 대한 **독립 decision review**다. 추가 물리 node나 provider 승격은 별도 승인이 필요하다. Git 게시 및 두 provider 백업의 ACK는 별도 publication/backup receipt에 기록한다. raw readback 없이 `RESTORE_VERIFIED`라고 하지 않는다.
