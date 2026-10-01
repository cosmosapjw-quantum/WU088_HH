# WU088_HH W1 병렬 실행 연구 기록 — 2026-10-02 KST

고정 Frozen107 primitive 0에 대해 W1 `[1/16,256]²`의 16개 타일을 모두 승인하고 정확한 구간 합산을 완료했다. 기존 타일 0을 재사용했고, 나머지 15개를 새로 계산했다. 전체 compact 구간의 최대 성분 반경은 약 `2.3350812035e-20`으로 요구 기준 `2^-48 ≈ 3.5527136788e-15`를 만족한다. 이 결과에는 endpoint·정규화가 포함되지 않으며 전체 2,592 primitive, 최종 D·epsilon·gap·Pareto 및 production 승인은 열려 있다.

새 수치 실행은 **15회, 승인 15회·거절 0회**다. 이전 타일 재사용 1회, 합산, 검증 준비 작업, synthetic 검사, DB 행은 이 실행 수에 합산하지 않는다. 신규 callback 평가는 634,459회, nested 적분 호출은 3,409회다. 모든 타일은 동일 primitive 0을 서로 다른 창에서 계산한 결과다.

| 타일 | 출처 | 평가 수 | nested 적분 호출 | native 경과 시간(초) |
|---:|---|---:|---:|---:|
| 00 | 기존 결과 재사용 | 85,915 | 308 | 40.149 |
| 01 | 신규 승인 | 66,534 | 245 | 23.744 |
| 02 | 신규 승인 | 37,895 | 140 | 11.955 |
| 03 | 신규 승인 | 37,438 | 140 | 11.053 |
| 04 | 신규 승인 | 72,897 | 386 | 33.140 |
| 05 | 신규 승인 | 65,938 | 250 | 25.509 |
| 06 | 신규 승인 | 39,456 | 175 | 15.124 |
| 07 | 신규 승인 | 19,380 | 100 | 6.541 |
| 08 | 신규 승인 | 59,976 | 418 | 24.350 |
| 09 | 신규 승인 | 35,719 | 230 | 13.308 |
| 10 | 신규 승인 | 37,734 | 200 | 12.604 |
| 11 | 신규 승인 | 30,603 | 163 | 11.002 |
| 12 | 신규 승인 | 59,279 | 414 | 26.709 |
| 13 | 신규 승인 | 24,403 | 220 | 9.445 |
| 14 | 신규 승인 | 21,100 | 176 | 8.090 |
| 15 | 신규 승인 | 26,107 | 152 | 8.539 |

현재 호스트의 실제 제한은 CPU quota 8·메모리 8GiB다. 동시에 3개 worker를 사용했고, worker와 native 각각 1GiB 주소 공간 한도 및 2GiB 여유분을 적용했다. 신규 15개 캠페인 경과 시간은 **90.299475905초**, 각 native 경과 시간의 합은 **241.115412612초**다. 이 둘의 비는 동시 실행이 겹친 정도이며, 직렬 기준 실행을 새로 측정한 speedup은 아니다. NCP 64코어·128GiB 및 MPI 실행·성능 측정은 하지 않았다. 실제 수치 커널의 peak RSS도 이번 기록에서 별도 측정하지 않았으며 메모리 상한과 혼동하지 않는다.

각 타일은 128비트·relative goal 128·최종 성분 반경 `2^-52`, 평가 200,000회·적분 호출 1,024회·120초(native hard wall 125초)·queued panel 64·degree 64로 제한했다. 정밀도 감소, tolerance 완화, 항 생략, 대칭화, 중점 대체, 합산 순서 변경은 없다. pinned range-native binary와 GMP 6.3.0·MPFR 4.2.2·FLINT 3.4.0은 그대로 사용했다. 새 host는 프로세스 실행·기록 경계만 바꾸며 수치 커널을 다시 컴파일하지 않는다.

정확한 16타일 합산 반경은 다음과 같다.

| 성분 | 정확한 반경 |
|---|---|
| imag | `496616849298501419/21267647932558653966460912964485513216` |
| real | `496616849170513807/21267647932558653966460912964485513216` |

새 adapter는 원본 입력·plan·build·binary·backend·receipt를 연결하고, 새 native stdout/stderr를 보존해 파싱 결과와 receipt를 대조한다. 기존 타일 0은 고정한 이전 receipt SHA로만 가져온다. 이전 성공 실행의 원 stdout이 digest로만 남은 기존 기록 한계는 그대로 명시한다. 재개 시 normalized 파일만으로 승인하지 않고 원본 근거를 다시 확인한다. 모든 타일이 승인된 경우에만 exact Fraction 합산과 최종 반경 검사를 수행한다.

프로세스 host는 parent-death signal과 parent PID 경합 검사, native fork/clone 금지, 자원 한도 및 직접 wait/kill을 사용한다. 독립 검사에서는 dispatcher를 강제 종료한 뒤 worker와 native의 종료를 pidfd로 확인했다. 이는 이 단일 native 프로세스 경계에 대한 검증이다. 일반 MPI descendant containment나 cgroup 전체 종료 검증으로 확대하지 않는다.

실제 계산 후, 정상 종료한 6개 작업의 claim 파일이 남아 최초 재개 검사가 거절했다. 모든 수치 결과와 정확한 합산은 별도 독립 검토를 통과했다. 알려진 여섯 claim은 원래 bytes·해시·정상 종료 근거를 보존하고, 이 완료 캠페인에만 한정한 검증 절차로 원자적으로 격리했고 strict 재개 검사가 통과했다. 처리 결과와 재개 readback은 `runtime/` 및 독립 최종 검토에 기록한다. claim 잔존의 근본 원인은 미확정이며 B22로 남긴다. 이 문제를 숨기거나 잠금만 지워 수치 실행을 반복하지 않는다.

구현자 검사 범위는 runner 13개, host 6개, DB builder 최종 17개다. 독립 pre-execution 검사 14개와 실제 저장 결과 검토는 별도 근거다. B19(프로세스 수명), B20(부모·자식 메모리 합산), B21(stdout/receipt 결합)은 해당 구현 범위에서 검증했다. 이 수를 과거 검사·수치 실행 수에 기계적으로 합산하지 않는다.

W1 compact 성공만으로 전체 영역 오차가 작아지지는 않는다. 기존 W1 endpoint 결과의 조건부 상한은 약 `2.9166e16`이며 이번에 재계산하거나 합산하지 않았다. 이 큰 bound를 모델 실패로 해석하지 않는다. 이전 W3 설계는 `[1/256,2^192]²`에서 조건부 endpoint 상한을 `2^-21` 이상 `2^-20` 미만으로 낮췄다. 다만 같은 log-step 3 균등 분할을 그대로 적용하면 67×67=4,489타일이 필요하므로, 현재 16타일 collector의 승인을 자동 확대하지 않는다. 이 비용을 줄일 검증된 비균등 분할·analytic grouping과 필요한 전체 primitive coverage, source-prescribed contraction·정규화·post-integral conjugation, actual represented model-gap과 epsilon 결합이 남아 있다.

원 프롬프트의 G0–G9 대조는 `STAGE_DELTA.json`에 보존한다. G2의 두 B192 archive·12 NPY 복호화 검증은 기존 범위대로 유지했고 재계산하지 않았다. G3 실제 model gap, G5 전체 endpoint 예산, G7 전체 D, G8 동결 판정, G9 독립 과학적 admission은 완료되지 않았다. 원 Deep Research DB 및 v2 원본 출처 공백도 그대로 남아 있다. 이번 작업은 기존 Drive/Dropbox 조사 근거를 이어받았으며 광범위 재수집을 반복하지 않았다.

새 감사 DB는 이전 wide-domain SQLite를 그대로 복사한 뒤 `w1_*` 테이블을 추가한다. 기존 표·행·스키마 보존, 정확한 source snapshot, integrity/FK 및 SQL 복원 후 논리 해시를 검사한다. 과거 receipt를 새 경로로 복사해 신규 실행으로 세는 경우도 거절한다. SQL 복원은 로컬 검사이며 cloud restore 증거가 아니다.

게시는 같은 연구 브랜치의 additive `w1_parallel_20261002_v1/`로 진행한다. 원격 기존 파일 전체 보존, 실제 END_HEAD/TREE, DB·ZIP 해시, Drive·Dropbox 업로드 및 이름·크기 readback은 별도 배포 영수증에 기록한다. ZIP은 복구한 source/evidence snapshot이며 원격 전체 mirror가 아니다. backend tar와 이전 DB의 정확 byte 복원이 필요하면 기존 배포 영수증에 연결된 백업을 사용한다. 새 ZIP의 SQL로 현재 DB를 논리 복원할 수 있고, byte-exact 새 SQLite도 별도 제공한다. Cloud `UPLOAD_VERIFIED`와 `RESTORE_VERIFIED=false`를 구분한다.

다음 연구 노드는 W1 밖 오차를 줄이기 위한 endpoint/더 넓은 compact 설계, 실제 전체 primitive 스케줄링, range solver의 MPI adapter 연결 및 NCP 측정이다. 이번 milestone의 성공은 W1 primitive 0의 compact enclosure이며 scientific/production admission은 false로 유지한다.
