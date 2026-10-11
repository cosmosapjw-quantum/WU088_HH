# WU088_HH PHYS09 — 유한 기체 에너지 상호작용

PHYS09는 NCP07에서 저장한 고정 소스 계열의 전체 gas/parameter box를 사용해 HH–photo 결합의 총 기체 에너지 상호작용을 포함한다. HH의 정확한 열·이온화 에너지 상쇄를 소스 식에 먼저 적용한 결과, full과 같은 COMMON에서 시작한 first_half 모두 음의 uniform mixed-energy 구간을 얻었다. 같은 C² 계열의 유한 unit-square interaction에도 이 구간이 적용된다.

이는 원 NCP07 source inclusion과 open C² 전제를 이어받은 수학적 포함 결과다. Native root 또는 native U/V/W/I를 새로 실행하거나 private certificate authority를 발급한 결과가 아니다. 두 번째 carried half와 full/two-half defect는 별도 미해결이다.

## 읽는 순서

1. `REPORT_KO.md`: 물리적 결론, 수치 구간, 실제 실행, 범위.
2. `theory/PROJECTED_ENERGY_THEOREM_KO.md`: 정의, 소스 대응, 유도, 존재·미분·적분 정리.
3. `results/projected_first/PROJECTED_RESULTS.json`와 `evidence/projected_first/EXECUTION.json`: 새 exact-rational 결과 및 최초 실행.
4. `review/DECISION.json`와 `review/REVIEW_KO.md`: 실제 비생성 독립 판정.
5. `handoff/NCP_LOCAL_CODEX_HANDOFF_KO.md`, `NCP_TASKS.json`, `GATE_INTERFACE.md`: NCP에서 수행할 저장 자료 소비기.

## 실제 새 실행

Python exact arithmetic 한 번, 0.8762889720092062 s, 최대 RSS 26,184 KiB, exit 0. 48개 assertion과 8개 의미 사례를 기록했다. 12,594개의 원본 interval input 행을 Rust consumer용으로 생성했다. Source/provider/point root/IVP/과거 suite 호출은 없다. Rust 도구 체인이 이 호스트 PATH에 없으므로 새 Rust 코드의 실행 여부는 미실행이다.

## 전달

이 디렉터리와 완료 후 생성되는 manifest/checksum, 선행 PHYS08 전체 ZIP을 하나의 새 archive로 제공한다. PHYS08 NCP 반환은 intake 조회에서 미관측이므로 NCP handoff는 선행 작업의 기존 완료 증거를 먼저 재사용하고, 없으면 한 번만 실행하도록 되어 있다. 이어 PHYS09 gate를 한 번 실행한다. 추가 사용자 첨부는 필요 없다. 실제 Git commit, archive SHA256, 양쪽 backup object ID와 ACK는 이 core 밖의 START/receipt/index에 기록된다.
