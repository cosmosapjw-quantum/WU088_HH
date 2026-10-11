# WU088_HH PHYS08 — 광자 가중합의 온도 방향과 HH 경쟁

**완료한 연구 범위:** 새 NCP PHYS07의 두 first-stage 저장 결과를 소비해, 전체 photo source P_N과 birth 미분 P_M 모두에 대해 가중합 냉각 및 HH/photo source 경쟁 부호를 검증했다. 원본의 모든 signed tail을 유지했다. 개별 node32 조건의 OPEN은 원본에 남아 있으며 이번 aggregate 정리는 별도 결과다.

먼저 `REPORT_KO.md`, `SCIENTIFIC_CONTRACT.md`, `RESEARCH_STATE.json`, `review/DECISION.json`을 읽는다. 정확한 수학은 `theory/WEIGHTED_PHOTO_THEOREM_KO.md`, 실제 계산은 `results/weighted_corrected/WEIGHTED_RESULTS.json`, 원 source provenance는 `inputs/ncp07/SOURCE_INTAKE_MANIFEST.json`에 있다.

## 이번 실행과 제공 코드

- 정확 유리수 Python reference: 최종 corrected run PASS, 0.3678347829991253 s, Linux max RSS 19,324 KiB. 294개 assertion은 294개 독립 테스트를 뜻하지 않는다. 2개 실제 stage × 2개 source 역할과 7개 의미 fixture, 총 11개 golden fixture를 생성했다.
- 첫 실행의 Python 역나눗셈 연산자 누락 TypeError는 `evidence/weighted_first/`에 코드 snapshot과 함께 보존했다. 계약이 허용한 한 번의 표적 수정 후 위 corrected run을 실행했다. 수학·입력·허용오차·검사 조건을 완화하지 않았다.
- `src/weighted_gate.rs`: dependency-free Rust outward interval scalar gate, **NOT_BUILT / NOT_RUN**. 연구 host에서 rustc/cargo가 없었다.
- `tests/weighted_gate_tests.rs`, `diagnostics/check_rust_output.py`, `tools/run_ncp_weighted.py`: NCP의 첫 saved-data gate 검증에 필요한 코드. 실제 NCP 실행 결과로 아직 간주하지 않는다.
- 새 PreBE/residual/FT03/HH/provider/root/IVP 및 과거 과학 suite 호출은 없다. Native 루틴을 import하지 않는 새 offline Python 산술만 실행했다. Inherited 미계측 counter의 null은 원본에 보존했다.

## 다음 NCP 작업

`handoff/NCP_LOCAL_CODEX_HANDOFF_KO.md`와 `NCP_TASKS.json`을 따른다. 백업본에는 이 문서, raw 입력, 계산 결과, Rust/Python 코드, oracle, review 및 두 canonical harness archive가 함께 있다. 별도 첨부 파일을 요구하지 않는다.

기존 runtime/완료 배열을 보존하고 아래 consumer를 새 create-only NCP 출력 경로에서 한 번 실행한다.

```sh
python3 tools/run_ncp_weighted.py --run-dir /absolute/new/path/hh_phys08_weighted_first
```

이 wrapper는 compiler identity → Rust build → 11개 saved fixture gate → exact oracle 포함 검사를 차례로 실행하고 모든 원 command/stdout/stderr/입력·binary identity를 보존한다. Source producer 두 개를 다시 실행하지 않는다. Native implicit root/U/V/W/I, finite energy interaction, carry/paired/time/continuum, full49 및 production은 여전히 OPEN이다.

## Git와 전달 식별자

이 core는 `research/hh-phys08-weighted-source-20261011`의 `research/r31ao_unequal_ladder/hh_phys08_weighted_source_20261011_v1/`에 추가된다. Core commit과 archive의 최종 SHA, 두 backup의 실제 ID는 self-hash cycle을 피하기 위해 별도의 `WU088_HH_PHYS08_START_HERE_20261011_v1.json` 및 delivery receipt/index에 기록한다. Core의 MANIFEST는 자체와 checksum sidecar를 제외한 payload를 결박한다. ACK/metadata 확인과 실제 다운로드 restore는 서로 다른 수준으로 보고한다.
