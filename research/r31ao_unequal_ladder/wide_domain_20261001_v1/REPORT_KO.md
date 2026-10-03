# WU088_HH 넓은 구간 후속 구현·실행 기록 — 2026-10-01

로그 좌표 solver의 첫 W1 타일 `[1/16,1/2]²`을 실제로 계산해 성분 반경 `2^-52`를 달성했다. 중간 범위값을 잘못 거절하던 실행 경계와 내부 상대정확도 목표의 문제를 각각 계측으로 구분한 뒤 수정했다. **W1 전체, W3 전체, 최종 D·epsilon·gap 및 NCP64 production 승인은 아직 완료되지 않았다.**

계산은 고정 Frozen107 primitive 0, 107개 signed term과 합산 순서, GMP 6.3.0·MPFR 4.2.2·FLINT 3.4.0, 128비트 정밀도를 사용했다. `t=2^x, u=2^y`와 Jacobian `(log 2)^2 t u`를 전체 복소 ball에 적용하며 원래 domain guard를 유지한다. exact power-of-two 끝점만 허용한다. 중점 대체, 항 생략, float64 과학 커널 전환은 하지 않았다.

| 실제 실행 | 요구 반경 | 평가 수 | 적분 호출 수 | 결과 |
|---|---:|---:|---:|---|
| 로그 CENTRAL `[1,2]²` | `2^-48` | 6,074 | 102 | 승인. 이전 세 CENTRAL 구간과 overlap |
| 로그 W1 `[1/16,256]²` | `2^-48` | 3,084 | 126 | 비수렴, 반환 구간 없음 |
| 기존 분할 runner의 첫 타일 | `2^-52` | 1,770 | 126 | 비수렴. 나머지 15타일 미실행 |
| 같은 첫 타일의 계측 실행 | `2^-52` | 1,770 | 126 | 같은 실패·카운터 재현 |
| 수정 range host, 상대목표 64 | `2^-52` | 20,000 | 93 | 평가 한도 도달, point 반경 초과 관측 |
| 같은 수정본, 상대목표 128 | `2^-52` | 20,000 | 81 | 평가 한도 도달, point 반경 초과 0건 |
| 같은 수정본, 선언된 완료 예산 | `2^-52` | 85,915 | 308 | 승인, native 경과 시간 40.148833522초 |

이 continuation의 실제 primitive 적분 호출은 **7회, 승인 2회·거절 5회**다. 동일 primitive 0의 두 compact 창을 승인한 것이며, 서로 다른 2개 primitive 또는 full-domain 결과가 아니다. 표의 적분 호출 수는 nested 적분기 내부 호출이다. 별도 직접 HH callback query 9회, 해석적 fixture, 이전 continuation의 실제 적분 4회, 계획 파일과 DB 행은 이 7회에 합산하지 않는다. 이번 작업에서 W3·전체 2,592 primitive·MPI는 실행하지 않았다.

마지막 타일의 반환 구간에서 직접 계산한 정확 반경은 다음과 같다.

| 성분 | 정확 반경 | 근삿값 |
|---|---|---:|
| real | `371491059 / 649037107316853453566312041152512` | `5.723726e-25` |
| imag | `371490941 / 649037107316853453566312041152512` | `5.723724e-25` |

최종 실행은 평가 200,000회·적분 호출 1,024회·120초(프로세스 hard wall 125초)·1GiB·queued panel 64·degree 64로 제한했다. 정밀도 128, 상대목표 128, 최종 반경 `2^-52`, point-inner 반경 `2^-68`은 앞선 goal128 실행과 같다. 실제 실행은 이 한도 안에서 종료했다. 40.15초는 현재 호스트의 단일 관측이며 전체 solver speedup 또는 NCP64 성능 수치가 아니다.

첫 장애는 finite inner enclosure를 중간 반경 `2^20`보다 넓다는 이유로 indeterminate로 바꾸던 정책이었다. 계측 실행에서 73개의 FLINT-success 유한 구간이 이 경계에서 버려졌고, infinite-error heap 항목이 우선 처리되면서 외부 Gauss–Legendre 시도는 0회였다. 새 `range_native_driver/`는 uniform parameter 범위값에 별도 `ENCLOSURE_AVAILABLE` 상태를 부여한다. 이 상태의 `achieved_radius_accepted`는 false다. 전체 불확실성을 외부 적분기에 전달하고, point·최종 적분은 계속 엄격한 반경 검사를 거친다. FLINT 실패·nonfinite·domain/precision/order 위반·자원 초과를 승인하지 않는다.

두 번째 장애는 FLINT의 상대목표 64가 내부 point 반경 요구보다 느슨한 정지 기준을 허용하는 경우였다. 실제 수정본에서 point 반경 초과 76건을 관측했고, 상대목표를 128로 강화한 실행에서는 point 반경을 만족한 결과 64개와 반경 초과 0건을 확인했다. 마지막 완료 실행은 point-inner 284개가 모두 반경을 만족했다. 유한 uniform enclosure 23개와 외부 analytic 요청 23개가 사용되었으며, 보수적 preflight 거절 15개는 기존 재분할 경로로 처리됐다. preflight 자체를 생략하거나 수정하지 않았다.

기존 host·로그 driver·진단 driver와 모든 실패 기록은 보존했다. 로그 driver 경계 22개·native 해석 검사 7개, 진단 driver 경계 23개·native 해석 검사 9개, 수정 range driver 경계 24개가 통과했다. 별도의 동일 고진폭 다항식 검사에서는 기존 host가 비수렴하고 수정본이 132회 평가로 정확한 적분값 `9*2^38`을 포함하며 최종 반경 `2^-52`를 만족했다. 이 red/green 검사는 양쪽 모두 상대목표 128을 사용한다. 상대목표 64의 별도 fixture 실패도 보존하며 실제 driver 기본값이 자동 변경됐다고 주장하지 않는다.

최종 독립 검토자는 HH를 다시 실행하지 않고 저장된 결과의 strict validator, 정확한 dyadic 반경, 23개 source pin, 실제 build/binary/backend·입력·plan·window·명령 결합을 확인했다. 성공 결과의 원 native stdout은 wrapper의 digest로만 남고, 파싱된 결과와 wrapper를 보존하는 현재 기록 계약의 한계도 유지한다.

정확한 16타일 Cartesian coverage·dyadic 합산·입력/plan/source/build 결합·전역 반경 검사를 구현했다. collector 17개, native receipt runner 9개 계약 검사와 독립 검토가 완료됐다. **새로 승인된 타일은 수정 source의 standalone 결과**다. 기존 runner의 승인 0개·첫 실패 중단 기록은 그대로이고, 새 source를 기존 validator로 합산하지 않았다. 전체 16타일 합이나 endpoint 결합 결과는 생성하지 않았다.

MPI host에는 delegated cgroup v2의 CPU·메모리·PID 한도, `cgroup.kill`, `populated=0` readback, 세션을 분리한 descendant의 종료 검사, rank affinity·입력/실행파일 결합을 추가했다. 구현자 10개·독립 12개 경계 검사 기록을 확인했다. 실제 detached-process 반례로 process-group 종료만으로는 충분하지 않음을 확인했다. 현재 환경은 root, CPU quota 8·메모리 8GiB이고 필요한 cgroup 위임과 NCP 연결이 없다. 실제 containment·MPI 실행은 0회다. 이 guard는 이전 `native_driver`에 연결되어 있으며 새 range solver와의 결합 및 NCP 2-rank/64-core 검증이 남아 있다.

원 연구 프롬프트와 G0–G9를 다시 대조한 결과는 `STAGE_DELTA.json`에 있다. 이전 472개 파일은 모두 SHA·크기가 보존되었다. 이전 감사 SQLite의 정확 SHA를 부모로 연결하고, 새 실행 ledger에서 계획·직접 callback·nested 호출·실제 primitive 실행을 구분한다. 이전 Drive/Dropbox DB 조사와 원본 출처 공백도 이어받는다. 이번 continuation에서 광범위 cloud 재조사를 반복하지 않았으며, 원 Deep Research DB 및 v2 원본이 새로 복구됐다고 주장하지 않는다.

새 감사 DB는 별도 SQLite/SQL로 생성하며 무결성·외래 키·SQL 복원 후 논리 해시와 source snapshot 안정성을 검증한다. DB 행에는 이전·계획·실패·검사·중첩 근거가 함께 들어가므로 행 수를 과학 실행 횟수로 집계하면 안 된다. 실제 실행 집계의 근거는 `runtime/EXECUTION_LEDGER.json`이다. 게시 경로는 기존 연구 브랜치의 새 `wide_domain_20261001_v1/`이며, 큰 계획·바이너리·raw 근거는 ZIP에 포함한다. ZIP의 repo는 복구한 작업 snapshot이며 원격 저장소 전체 mirror가 아니다. 기존 backend 별도 백업은 정확한 현재 호스트 백업으로 재사용하고 NCP용 바이너리 인증으로 해석하지 않는다.

최종 DB 검증, 실제 Git commit/기존 원격 항목 보존, Drive·Dropbox 저장 식별자와 readback 결과는 별도 배포 영수증에 기록한다. cloud upload/메타데이터 readback과 local SQL 복원 검증은 구분한다. 원격 파일을 다시 내려받아 복원한 검증으로 표현하지 않는다.

남은 작업은 수정 solver의 명시적 분할/MPI adapter 결합, 나머지 W1 및 전체 W3/primitive coverage, 전역 endpoint 단일 적용, 실제 normalized D 조립, 모델 gap·epsilon·최종 동결 판정과 독립 과학 검토다. 선택한 추상 정리·component 검증과 이 두 compact 창의 성공이 전체 연구 단계를 완료한 것은 아니다. scientific/production admission은 false로 유지한다.
