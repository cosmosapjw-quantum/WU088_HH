# PHYS09 시작 시 NCP08 반환 관측

관측 시각: **2026-10-11 06:30:12 UTC (15:30:12 KST)**. 현재 확인한 Git 경로에서는 **NCP08 반환을 관측하지 못했다**. 이를 아직 조사하지 않은 모든 백업·이름·미게시 로컬 작업의 부재라고 확대하지 않는다.

## 현재 증거

- 예상 branch `codex/hh-phys08-ncp-20261011`의 exact-ref 조회는 GitHub `404 NOT_FOUND`였다.
- `refs/heads/codex/hh-phys08` prefix 조회는 빈 배열이다. 더 넓은 `refs/heads/codex/hh-` prefix에는 NCP04, NCP06, NCP07, routing의 네 branch만 있었다.
- 최근 갱신순 PR 10개를 확인했다. PHYS08 연구 PR39는 `3490c77ea548fa810443b06546ba847856a7eaea`, tree `692b8bd51963cafd26d749e63327efe71efc8033` 그대로 open이다.
- 최신 관측된 native 과학 source는 NCP07 PR37, head `4d5c18b8a6d348e2de42b5e12dc0fd4d753add7b`, tree `5f418eda6613d0e69bf5404a43d7598a60f54ded`다. 원본 bytes를 다시 다운로드하지 않았다.
- 새 routing PR38의 head는 `d0cf050cf731cc838780f2ad613afdc6a0523712`이다. 마지막 commit은 hourly PR update를 말하고, PR body의 6시간 표기는 이에 비해 뒤처져 있다. 이 routing 변경을 NCP08 과학 실행 증거나 본 연구 모델의 자동 변경 근거로 취급하지 않는다.

## 유지되는 판정

PHYS08의 exact-rational source weighted theorem과 실행 결과는 기존 `PROMOTE_SCOPED` 범위로 유지된다. Rust gate, wrapper, output consumer의 **첫 NCP 실행은 여전히 관측되지 않았다**. Compiler identity, build, gate, oracle consumer, weighted sidecar 및 NCP08 비생성자 결정은 모두 null/미관측이다. 미관측 실행 횟수를 외부 세계의 0회 실행이라고 바꾸지 않는다.

`NCP_TASKS.json`의 저장 자료 gate 과제는 별도로 pending이다. PHYS09는 저장된 NCP07 source와 PHYS08 결과를 기반으로 독립적인 물리·수학 의무를 이어갈 수 있다. Root/U/V/W/I, 유한 gas-energy 부호, carried half, paired defect, time/continuum, full49와 production은 이번 intake만으로 바뀌지 않는다. 원 node32 per-node witness의 OPEN도 유지한다.

## 원본 및 fingerprint 검증

`observations/`에는 실제 ref error, prefix 결과, 현재 commit 메타데이터와 최근 PR 요약을 보존했다. 현재 PHYS08 core directory의 Git blob metadata로 기존 로컬 `MANIFEST.json`을 결박하고, 그 manifest로 handoff/contract/후보 Rust/검사기/oracle 등 선택한 12개 로컬 파일의 SHA256와 크기를 검증했다. 직접 조회한 top-level 파일은 Git blob SHA-1/size도 일치한다. Nested 파일의 Git blob은 로컬 계산값이며 해당 개별 remote blob을 새로 조회했다고 주장하지 않는다.

새 NCP08 source payload는 0개다. 이번 intake의 원격 변경, compiler/과학/테스트/native callback 실행과 과거 NCP07 자료의 재다운로드는 모두 0이다. 이 문서는 새로운 과학 검증이나 compiler 검증 결과가 아니다. 구체적인 메타데이터와 파일별 결박은 `SOURCE_INTAKE_MANIFEST.json`, 상태는 `SOURCE_INTAKE_SUMMARY.json`에 있다.
