# PHYS08 실행용 정본 식별자

- Research core commit: `75be610c73bd9c10f8399851ea82b22f70f136d0`
- Core subtree: `dc4fd8777d1c9584a74fcb6b1af6caa6c3b03eb6`
- Research PR: https://github.com/cosmosapjw-quantum/WU088_HH/pull/39
- Core archive: `WU088_HH_PHYS08_WEIGHTED_SOURCE_NCP_HANDOFF_20261011_v1_sha_84ec6694a01e.zip`
- Archive size: 699371 bytes
- Archive SHA256: `84ec6694a01ec711eb2f55542f718bb1f091a5547ab4ce809503089bd18c2b9b`
- Core MANIFEST SHA256: `4631c91add9a8e226ef781967cc131d38df1bb3dd583d4d00e504cc1d6bef0dd`
- Drive archive ID: `1j37fKykEiWcHBs6H6Df17zbVGlpPLPK_`
- Dropbox archive ID: `id:BSpOijBcT10AAAAAAD4HbQ`
- Core root directory after extraction: `HH_PHYS08_20261011_v1/`
- Independent decision: PROMOTE_SCOPED; Rust build/tests and NCP wrapper/consumer are NOT_RUN.

이 식별자로 전체 archive를 직접 확보하면 추가 전달 파일 없이 아래 계약을 수행할 수 있다. 최종 delivery commit은 별도 최종 영수증에 기록되며, 이 core와 과학 결과는 변경하지 않는다. Archive는 양쪽 upload completion과 metadata identity를 확인했으며, 원격 재다운로드 restore는 수행하지 않았다.

---

# NCP local Codex handoff — WU088_HH PHYS08

WU088_HH PHYS08의 **저장된 source 자료를 소비하는 Rust weighted gate**를 이어서 수행하라. 사용자에게 추가 전달 파일을 요청하지 말고 기존 Git과 아래 두 백업 폴더에서 PHYS08 전달물을 직접 확보하라. 사용자 승인 범위는 해당 프로젝트의 읽기/쓰기, additive branch/PR, Google Drive·Dropbox 백업이며 반복 확인을 요구하지 않는다. 다른 사람에게 메시지 전송, main 병합, production 설치는 이 작업에 포함되지 않는다.

## 1. 작업 시작과 정본

- Repository: `cosmosapjw-quantum/WU088_HH`.
- 연구 PHYS08 branch: `research/hh-phys08-weighted-source-20261011`.
- 연구 core 경로: `research/r31ao_unequal_ladder/hh_phys08_weighted_source_20261011_v1/`.
- 최신 NCP07 base: `4d5c18b8a6d348e2de42b5e12dc0fd4d753add7b`, branch `codex/hh-phys07-ncp-20261011`, PR #37. NCP07 science core는 `dfa574ce2c302ff2dce38d0e487903d57f1db977`다.
- PHYS07 연구 부모는 `e9272a1ffe0bd012e4e34718b7b2576bfd26772e`다. 서로 다른 연구/NCP base를 혼동하지 않는다.
- Drive folder ID: `1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM`.
- Dropbox folder: `/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928`.
- 두 폴더에 고유한 `WU088_HH_PHYS08_START_HERE_20261011_v1.json`, `WU088_HH_PHYS08_BACKUP_INDEX_20261011_v1.json`, core ZIP, prompt 및 receipt가 있다. 최종 core/ZIP SHA와 실제 파일 ID는 START/receipt를 우선한다. PHYS07의 동명 START나 다른 프로젝트 파일을 선택하지 않는다.

현재 local checkout/runtime/dirty changes를 먼저 read-only inventory하고, 사용자의 변경을 보존한 별도 worktree 또는 additive overlay에서 진행한다. NCP07 base가 실제 local/git와 다르면 증거를 기록하고 필요한 범위를 분리한다. 완료된 native/reference, vendor/orchestration, COMMON, 과거 배열 및 원 source outputs는 bytes 그대로 유지한다.

Core archive 하나에 필요한 raw source export, provenance, theorem, 정확 계산 결과, Rust gate/tests, Python consumer/wrapper, contract, review와 canonical Astra 연구/코딩 harness ZIP 두 개가 들어 있다. ZIP path traversal·중복 경로·CRC와 core MANIFEST의 payload size/SHA를 확인한 후 사용한다. 이 검사는 연구 재실행이 아니다. Git으로 core를 얻었다면 START에 기록된 core subtree와 file manifest를 결박한다. 과거 전체 NCP archive나 큰 binary/geometry trace를 재다운로드할 필요는 없다.

## 2. 필수 읽기

Repo `AGENTS.md`와 그 필수 문서, core `README_KO.md`, `REPORT_KO.md`, `SCIENTIFIC_CONTRACT.md`, `RESEARCH_STATE.json`, `NCP_TASKS.json`, `review/DECISION.json`, `docs/WEIGHTED_GATE_IMPLEMENTATION_KO.md`를 읽는다. 필요한 정확 유도는 `theory/WEIGHTED_PHOTO_THEOREM_KO.md`, 최신 NCP 입력 identity는 `inputs/ncp07/SOURCE_INTAKE_MANIFEST.json`에 있다.

프로젝트가 채택한 canonical Astra v4 harness archive를 해시로 확인하고 적용한다. Runtime 모델명·capability는 관측 그대로 기록한다. 연구 host의 GPT-6 Astra Pro label을 programmatic router alias나 local model attestation으로 바꾸지 않는다. 미래 compiler/platform 값도 과거 보고서에서 복사하지 않는다.

## 3. 이미 완료한 물리 결과

실제 physical source P_N은 33×3 `photo_rates.value`, birth derivative P_M은 같은 자료의 `gradient[5]`다. N과 유한 M, source-rate M/dt를 구별한다. 현재 source의 고정 계수에서

\[
B(v)=p v_w-w(v_x+\widehat f v_{y_1}+2\widehat f v_{y_2}),\qquad DT[v]=C B(v)/p^2
\]

를 전체 signed vector에 적용했다. Stage fHe와 density ratio fhat를 구별했고 모든 node·He channel·subnormal tail을 유지했다. Full/first-half × P_N/P_M 네 경우에서 B, DT, (HgP)_x, (PgH)_x, ell PgH가 엄밀히 음수이며 P_x와 P_w는 양수다. ell HgP=0은 동일 CHI leaf의 정확한 reaction-vector cancellation이다.

원 NCP07 per-node witness의 OPEN을 수정하지 않는다. Node32를 0으로 대입하거나 tolerance/support clipping을 쓰지 않는다. 새로운 weighted sidecar를 별도 생성한다. Saved-Jet와 closed formula의 overlap은 consistency diagnostic이며 source identity의 증명이 아니다.

Root exact reference는 최종 PASS이고 11개의 golden fixture를 보존했다. 첫 Python 실행 실패와 한 번의 표적 수정도 남아 있다. 이 reference를 다시 실행할 의무는 없다. Rust compiler가 연구 host에 없어 Rust build/tests와 output consumer/wrapper는 아직 NOT_RUN이다. **이 미완료 실행을 NCP에서 수행하는 것이 다음 의무다.**

## 4. 허용된 실행

`NCP_TASKS.json`의 예산을 먼저 읽고, 새 create-only output 경로에서 아래를 한 번 실행한다.

```sh
python3 tools/run_ncp_weighted.py --run-dir /absolute/new/path/hh_phys08_weighted_first
```

실제 local 정책에 맞는 경로를 선택한다. 실행 전에 wrapper, Rust source/tests, oracle, TSV, exact consumer와 contract의 identity를 결박한다. Wrapper는 다음 순서만 수행한다.

1. 기존 rustc의 `-vV`와 host 정보를 저장한다. 컴파일러가 없으면 설치하지 않고 concrete blocker와 다음 방법을 반환한다.
2. Dependency-free standalone Rust gate를 offline build한다. Build 한 번, wall 60 s, address space 512 MiB, codegen unit 1이다.
3. Built-in 7개 의미 검사와 보존된 11개 fixture를 같은 binary로 한 번 실행한다. Wall 10 s, address space 128 MiB다.
4. Python consumer를 한 번 실행해 Rust B/DT 출력이 정확 유리수 oracle의 전체 구간을 포함하는지 확인한다. Wall 10 s, address space 128 MiB다. Equality/overlap으로 대체하지 않는다. Role, 부호 label, duplicate/missing rows, finite intervals와 summary를 검사한다.
5. 실제 네 source fixture의 weighted sidecar를 생성하고 입력/binary/결과를 결박한다. 이는 **archived aggregate를 사용한 Rust scalar gate 구현 증거**다. 새 native source producer 또는 implicit solver 실행으로 기록하지 않는다.

각 stdout/stderr/command/exit/time/memory와 최초 실패를 보존한다. 자동 retry는 없다. 실패 후 원인을 분류하고 필요 시 범위를 명시한 표적 수정과 새 계약을 먼저 기록한다. 성공 여부를 위해 허용오차·physics/input·signed tail·oracle sign policy를 바꾸지 않는다. NCP07의 source 두 target, 성공한 Python reference, historical suite는 다시 실행하지 않는다.

PreBE/residual/FT03/HH/provider/nonlinear root/endpoint/internal-point/IVP/mixed solver/carry/paired/full49/production의 새 실행 예산은 모두 0이다. 미계측 inherited counter는 null 그대로 남긴다. Wrapper의 source route 부재로 관측된 0과 native application의 계측 값을 구별한다.

## 5. 반환물과 판정

Actual `HOST.json`, compiler/build/gate/consumer 원 로그, `ORACLE_CHECK.json`, `WEIGHTED_SOURCE_SIDECAR.json`, `NCP_RUN.json`, source/input/binary SHA256와 scientific contract를 반환한다. 저장 원본과 exact reference 값은 새 native root/U/V/W/I 필드에 복사하지 않는다.

Native root authority, actual U/V/W/I, finite gas-energy interaction, carried second-half, full/two-half defect, time/continuum remainder, full49, production은 OPEN/null로 유지한다. 이번 반응 source의 경쟁 방향과 유한 nonlinear response는 다른 명제다.

비생성자 reviewer의 scoped 결정 후 additive `codex/hh-phys08-ncp-20261011` branch/PR에 저장하고 같은 Drive·Dropbox 폴더 모두에 전체 NCP 반환 archive와 START/index/receipt/다음 handoff를 올린다. 원격 upload ACK·metadata·다운로드 byte 검증·restore를 서로 구별해 실제 수행 수준만 적는다. Core commit과 delivery commit, archive SHA와 manifest SHA, source identity와 binary identity를 분리하고 self-hash cycle을 만들지 않는다. 사용자가 추가 파일을 전달하지 않아도 다음 루프를 이어갈 수 있게 필요한 전달 파일을 백업에 함께 넣어라.
