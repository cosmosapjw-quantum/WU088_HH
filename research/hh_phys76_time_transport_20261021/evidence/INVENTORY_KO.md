# PHYS75 후속 source inventory — 2026-10-21

## 현재 identity

| 대상 | 현재 확인 HEAD | 범위 |
|---|---|---|
| WU088_HH PR128 | `92f5ab9dba531ebe05909dcb77d3740d2c68c580` | 과학적 기준: 전단 memory 및 finite-L8 8→3 재표현 |
| WU088_HH PR129 | `b76fd4b5d0dfe4850ebde66a8a10f78402d36c00` | standalone 보충 보존·인계, PR128 descendant |
| REI PR198 | `8bd35af5f11c7ea5945b656be1c013d1c1933498` | long collisionless 1,231 이력, z20→4 |
| REI PR213 | `d32cd99fa19c65aa1ca63dbc8aab8741834270e8` | C15 warm 729 이력, a0.1999→0.2 |
| REI PR214 | `98fcf3943fa54e089b0292d166c3a47becb5edb8` | ACCEL01 exact massive-moment cache 및 completed-case planner |
| BASS PR176 | `26f4a89a54462c4e7c5705f281f187f33f45166a` | REI213 counterpart |
| BASS PR177 | `4f19e6eaf50e8458d59d27ff47f03e9d8c8b22ca` | REI214 counterpart |

WU088_HH 138개 branch ref를 100+38 두 페이지로 열거했다. PHYS75 이후 PHYS76 이름의 branch/PR는 조사 시점에 발견되지 않았다. PR129 recursive tree 및 최신20 PR metadata를 읽었으며 모든138 branch의 파일을 읽었다는 뜻은 아니다. REI의 2026-10-21 갱신 PR 중 관련198·213·214의 HEAD 및 보고/DAG를 대조했다. Private conversation 검색은 실제 도구 호출에서 “Personal context is unavailable for this conversation”을 반환했다.

## 과학 범위

Long archive에는 원래 radiation625 이력, 신규 matter600 및 mixed6 이력이 있다. 각 raw NPZ는65개 표본의8-state 배열을 보존하며 총80,015개 상태다. 모든 시작점은 zbar20, 종료점은 zbar4이다. warm729의47,385개 표본과 HH74 control63의5,103개 표본은 서로 다른 계산 범위이며 합쳐서 같은 sweep으로 세지 않는다.

PR128의 `NEXT_DAG.json`에 남은 의무는 `FULL_NATIVE_COLD_EOR`, `GENERAL_NON_LRS`, `CONTINUUM_TIME_ANGULAR_CERTIFICATE`, `HH_PHYSICAL_MATCHED_XI_AND_RATE`다. Supplemental DAG는 standalone729 postprocess를 미완료로 보존하지만 이것이 PR128 scientific owner를 대체하는 경로는 아니다.

## 실제 복구·검증

REI198의 `REI_BIANCHI_MATTER_RADIATION_FINAL_20261021.tar.gz`를 Dropbox temporary download로 가져왔다.

- Dropbox ID: `id:BSpOijBcT10AAAAAAD_fYA`.
- Google Drive 대조 ID: `1i6x-HcPTctzSQwsxkET-CfTGfjpC-Dx7`; 양쪽 live metadata size 일치.
- 파일 크기:37,945,383 bytes.
- 현재 whole HTTP GET SHA256: `2c1433a92ae68c328436852b2842c9b7c51d30b9ff84a22fe2dffbd04ee4246d`.
- archive manifest가 지정한5,747 payload의 크기/SHA256 전부 일치. Manifest를 포함한5,748 tar member는 모두 regular file이며 경로 이탈/중복/누락/초과0.
- 원문은 `../upstream_inputs/REI_BIANCHI_MATTER_RADIATION_FINAL_20261021.tar.gz`; 소스·NPZ·JSON/CSV/MD3230개만 선택 추출했다.
- 실제 ODE 적분0, 과거 solver replay0, benchmark0.

추출 root:

`/workspace/scratch/61913f66989c/upstream_inputs/rei198_verified/repo_payload/research/rei_bianchi_sigma_pi_pilot_20261021`

| 용도 | 상대 경로 |
|---|---|
| 기본8-state owner | `pilot.py` |
| 독립 matter/radiation 초기화·진단 | `matter_radiation_20261021/component_pilot.py` |
| 원 kinetic owner | `vendor/canonical_fv.py`, `vendor/lrs_boltzmann.py`, `vendor/species_hierarchy.py` |
| 기준 cosmology/clock | `vendor/REI_BACKGROUND_FAMILY_LOCK.json` |
| 원625 raw8-state | `results/pilot/cases/*.npz` 및 동명 JSON |
| 원625 component 재표현 | `matter_radiation_20261021/decomposition/cases/*.npz` — state 배열은 의도적으로 없음 |
| 신규606 raw8-state·components | `matter_radiation_20261021/results/new_sweep/cases/*.npz` 및 동명 JSON |

모든1231 종료 상태와 해당 raw/receipt SHA256, 고정 massive amplitude를 `../upstream_inputs/REI198_TERMINAL_STATES.json`에 정리했다. Index SHA256은 `62f5d96fd323b1ed60c61f4b51e35ab80eb3498d2800c6c04addc1e5e2483115`다. 경로·표본 범위의 별도 기록은 `REI198_HISTORY_COVERAGE.json`이다.

8-state 순서는 `(tau=href*t, b, q=s/href, E0,E2,E4,E6,E8)`다. 이후 실제 z4→2 continuation을 선택할 경우 기존 전역 clock `x=ln(a/aref)`, `aref=1/21`, 원래 `href` 및 각 case의 `A_m`를 유지해야 한다. 첫8-vector는 저장된 종료값을 사용하며 원 initial-axis solver로 다시 초기화하지 않는다. PHYS75의3-state 표현에서는 저장된 `E_start`와 `b_start`를 기준으로 `exp[(b-b_start)M]E_start`를 사용한다. 현재 자료 자체에는 z2 표본이 없다.

## 백업 identity와 남은 전달 공백

PR129 supplemental ZIP의 Drive live metadata는952,307 bytes로 현재 receipt와 일치한다. Drive의 final delivery JSON(ID `1EWCc7WcxPoh_xpWPmsCzk916k-EwVBhW`)은 실제 다운로드된1875 bytes를 Git JSON과 직접 비교하여 byte equality를 확인했다. SHA256은 `d2f5b6b85ccd9251dfaa382525d6a25d0ca0d683e06aea77edbecba8cd58c138`이다. 이 확인은 delivery JSON의 현재 readback이며 supplemental ZIP의 이전 전체 CRC/hash 검증을 새로 시행했다고 세지 않는다.

PHYS75 S0 checkpoint는 Drive `14fNq8s4ZRQAuoDPOHQt1VdZagEQVx8E7`, Dropbox `id:BSpOijBcT10AAAAAAD_ffg`에서148,697 bytes metadata가 확인된다. PR128이 기재한 source-bound FULL archive 및 해당 DELIVERY.json은 현재 inspected Git tree/Drive parent folder/Dropbox filename search/Library title search에서 식별하지 못했다. 이 공백은 보존한다. REI198 source/raw archive 복구는 독립적으로 성공했으므로 과학 입력 재사용을 막지 않는다.

## ACCEL01 재사용 결정

[REI PR214](https://github.com/cosmosapjw-quantum/rei_bianchi/pull/214)의 `cached_context.py`, `work_plan.py`, `batch_worker.py` 및 THEORY/DAG를 실제 읽었다.

- Cache는 C15 owner의 massive three moments만 대상으로 한다. 정확한 binary64 `(x,b)` key, seed별 model lifetime, immutable bytes-backed arrays, dtype/shape/stride/layout 및 mass/params binding guard를 갖춘 bounded OrderedDict LRU다. 기존 reduction operation order를 그대로 호출한다.
- Completed-case identity는 label·grouping·host/profile을 physics identity와 분리한다. Default729는 모두 기존 완료로 인식되어 pending0, jobs0이며 같은 trajectory 재실행을 지시하지 않는다.
- Pending worker는 model/state를 case마다 새로 두고 준비 데이터만 공유한다. Case lock과 원자적 receipt/result publication, failure 보존을 구현했다.
- NCP ceiling은64CPU/128GiB이며 host/cgroup 실측 headroom과 numerical thread1을 사용한다. 이 ceiling은 현재 사용 가능한 전체 자원을 의미하지 않는다. HH의 기존16GiB reserve 및 자원 lease 계약은 별도로 유지할 수 있다.
- 이 구현을 다시 만드는 최적화는 중복이다. Long collisionless finite-L8 owner에 C15 class를 직접 이식하지 않는다. Exact-key/binding/reuse 원칙 또는 source를 참조하고 물리 owner 경계를 보존한다.

정확한 remote source는 아래 commit 고정 경로를 사용한다.

- https://github.com/cosmosapjw-quantum/rei_bianchi/tree/98fcf3943fa54e089b0292d166c3a47becb5edb8/research/rei_sigma_pi_acceleration_20261021
- https://github.com/cosmosapjw-quantum/rei_bianchi/tree/8bd35af5f11c7ea5945b656be1c013d1c1933498/research/rei_bianchi_sigma_pi_pilot_20261021/matter_radiation_20261021

모든 mutation은 임시 inventory/recovery 파일 생성뿐이다. Remote 게시·백업 업로드·NCP 실행은 수행하지 않았다.

