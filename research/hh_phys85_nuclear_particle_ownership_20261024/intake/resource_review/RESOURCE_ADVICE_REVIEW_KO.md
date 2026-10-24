# PHYS84 자원 admission 독립 검토

## 판정

선택한 첨부 아카이브에 `POSIX_FADV_DONTNEED`를 적용하는 방안을 현재 admission 문제의 해결책으로 권하지 않는다. 어떤 cache 변경도 실행하지 않았다. 읽기 전용 metadata와 고정 wrapper/lease 코드, Linux 원 문서만 조사했다. 이 판정은 자원 부족이 영구적이라거나 해당 syscall 자체가 금지된다는 뜻은 아니다.

## 정량 근거

후보는 사용자 첨부 디렉터리에서 이름을 명시적으로 선택한 정규 archive 10개다. 총 logical bytes는 **434,725,611 bytes (0.404870 GiB)**, 4,096-byte base-page 단위로 올린 합은 **434,745,344 bytes**다. 이는 실제 residency 또는 현재 cgroup charge 측정이 아니다.

이번 점검의 memory snapshot은 `memory.max=8,589,934,592`, `memory.current=7,060,385,792` bytes였다. raw headroom은 1,529,548,800 bytes, reserve1.5GiB+job0.5GiB까지 617,934,848 bytes가 부족했다. 후보 전체 content의 page-rounded 크기를 빼도 이 간격이 닫히지 않는다. kernel metadata 등 간접 효과까지 엄밀히 제한한 메모리 상계는 아니며, 실제 admission 판정으로 사용할 수 없다. 이전 부모 관측 약8.3GB와 달리 current가 자연 감소했으므로 다음 실제 gate 시점의 값이 우선한다. 이 에이전트는 cache를 바꾸지 않았다.

| 파일 | bytes | mtime UTC |
|---|---:|---|
| 06-rust-1.94.1-x86_64-unknown-linux-gnu.tar.xz | 192,287,020 | 2026-10-24T00:40:09.295685+00:00 |
| 10-bianchirustcoreRDAGcomplete.tar.gz | 44,365 | 2026-10-24T00:39:35.647090+00:00 |
| 11-lowell_bianchi_codex_automation_kit.zip | 52,267 | 2026-10-24T00:39:35.499087+00:00 |
| 12-BASS_v1_BACKGROUND_HIGHL_HARNESS_PROJECT_SOURCE_BUNDLE_20260803-1-.zip | 418,717 | 2026-10-24T00:39:36.183103+00:00 |
| 13-xAct_1.3.0.tgz | 15,613,945 | 2026-10-24T00:39:38.463154+00:00 |
| 14-bianchireview87.tar-1-.gz | 2,298,253 | 2026-10-24T00:39:36.403108+00:00 |
| 15-GENERIC_VECTOR_JF_OFFLINE_CARGO_VENDOR_20260816-1-.zip | 112,967,859 | 2026-10-24T00:39:55.551431+00:00 |
| 17-BASS_RUSTCORE_OFFLINE_LOCKED_20260818-105221-2-.zip | 33,103,685 | 2026-10-24T00:39:43.531268+00:00 |
| 18-literatures.zip | 68,123,442 | 2026-10-24T00:39:47.255332+00:00 |
| 19-papers.zip | 9,816,058 | 2026-10-24T00:39:41.439221+00:00 |

전체 경로·inode·mtime ns는 `RESOURCE_ADVICE_DECISION.json`에 기록했다. 선택 대상 archive 내용은 읽지 않았고, mincore도 실행하지 않았다. 보이는 FD/map에서 선택 경로를 찾지 못했으나 일부 `/proc/*/maps` 접근이 거부되었다. 따라서 모든 process에 대해 미사용/비매핑이라고 확정할 수 없다. 그 관측 자체도 순간적인 snapshot이다.

## Linux 동작과 한계

Linux man-pages의 [posix_fadvise(2)](https://man7.org/linux/man-pages/man2/posix_fadvise.2.html)는 DONTNEED를 해당 영역의 cache 반환 시도로 설명한다. advisory라 반환을 강제하지 않는다. partial-page 범위는 무시될 수 있으며, dirty page의 writeback과 반환도 보장되지 않는다. 그러므로 syscall 성공만으로 memory.current 감소나 lease PASS를 기록하면 안 된다.

Linux [Memory Management APIs](https://docs.kernel.org/core-api/mm-api.html)의 `invalidate_mapping_pages` 설명은 clean·unmapped·unlocked cache만 대상으로 하며 I/O 대기를 강요하지 않는다고 명시한다. 이 내용은 일반 Linux API의 동작 설명이다. 현재 실행 커널과 filesystem의 fadvise 실제 경로를 완전히 source-match한 결과는 아니다.

명시적으로 소유하고 사용 종료를 확인한 파일에 한정한 advisory는 입력 bytes를 수정하는 작업과 다르지만, shared file cache를 줄여 다른 독자의 후속 I/O에 영향을 줄 수 있다. 지금의 확인 범위에서는 ‘다른 process 영향0’이라고 인증하지 않는다. 이 차이를 해소하려고 광범위한 cache purge, global sync, reclaim sysfs, 임의 파일 삭제를 추가하지 않는다.

## 고정 계약과 첫 숫자 실행

PHYS83 final archive에서 보존 lease source를 텍스트로 읽고 SHA256 `76ff57ba687fd9830b84c3fcff69eb8ed0e9f6ceab4551e61c67c84d3ea65124`를 확인했다. PHYS84 final archive의 현재 wrapper SHA256은 `f15ae64c40dadcee0995344c9d90d3de314e2c9689a303b1b045271878c6a752`다. 코드를 import하거나 lease를 획득하지 않았다.

`observe_resources`는 MemAvailable 및 cgroup ancestor의 실제 max-current를 이용하고 local reserve1.5GiB, job0.5GiB를 반환한다. `resource_slots`는 CPU reserve·실제 idle·live lease·memory reserve를 함께 적용한다. 따라서 단일 root cgroup 산술은 필요조건 진단이며 실행 승인 자체가 아니다. 전체 계약 기준은 그대로 유지한다.

첫 숫자 재개는 복원·source identity·actual HEAD·owner 변경 확인 이후, **원래 `source/leased_call.py`를 통한 새 targeted verification**이어야 한다. 실제 gate가 거부하면 receipt는 admission-only이며 numerical child0이다. 조건 변화 없이 거부 receipt만 반복하지 않는다. 검증 PASS와 독립 검토 다음에만 첫16row application을 진행하고, 이후 matching identity와 결과 bytes를 검증하는 resume을 수행한다. PHYS78–83의 완료 계산은 호출하지 않는다.

Inherited spend/remaining/currency는 null이다. unknown을0으로 치환하지 않는다. Verification cap30CPU/60wall seconds, application·resume cap10CPU/20wall seconds, worker/thread1, memory lease0.5GiB를 유지한다. 이 보고서의 science/test/lease/cache-action/remote-mutation 횟수는 모두0이다.

복원 checkout의 `CONTRACT.json`과 현재 `source/leased_call.py`를 추가로 읽었으며 최종 archive 원본 bytes와 각각 일치했다. 해당 readback SHA와 관측 시각은 decision JSON에 기록했다.
