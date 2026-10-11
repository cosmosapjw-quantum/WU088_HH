# WU088_HH PHYS07 — 첨부 없는 NCP 시작 안내

이 문서만으로 필요한 연구 package와 다음 NCP 실행 지시를 복구할 수 있다. 추가 사용자 첨부를 요구하지 말고, 이미 같은 identity의 Git object/cache가 있으면 그것을 재사용한다.

## 실제 고정 identity

| 항목 | 값 |
|---|---|
| Repository | cosmosapjw-quantum/WU088_HH |
| 연구 branch | `research/hh-phys07-source-domain-20261011` |
| 연구 core commit | `5cf77c2e56e9dc32596f9111620fd33de7d39e30` |
| 연구 core tree | `508291e1622bed5f6ba5fb10d9971df252bee93d` |
| Git package directory | `research/r31ao_unequal_ladder/hh_phys07_source_domain_20261011_v1/` |
| ZIP root | `HH_PHYS07_20261011_v1/` |
| ZIP | `WU088_HH_PHYS07_SOURCE_DOMAIN_MIXED_NCP_HANDOFF_20261011_v1_sha_16c39ce3526c.zip` |
| ZIP bytes | 814467 |
| ZIP SHA256 | `16c39ce3526c1776cea854a381598633529007242b49a78907da15d93e9b253e` |
| MANIFEST SHA256 | `3f88c810078287e883adb9496697862cafb023971be2fafab58871bcb0fe1ea6` |
| NCP 시작 head | `65a36e255aa6d9911e23a9b5ced18d8a9f507606` |

## 바로 읽을 수 있는 전달 파일

Receipt는 `WU088_HH_PHYS07_DELIVERY_RECEIPT_20261011_v1.json`이며 SHA256은 `7755e1d38e11e07b5ef2bad87f43cb6fa1bbf59b536576b6e8208d018cfd0a56`다.

- Drive receipt: [WU088_HH_PHYS07_DELIVERY_RECEIPT_20261011_v1.json](https://drive.google.com/file/d/1TnKihemzaQKU5MIWdcZz8zbQBS1VfxQe/view?usp=drivesdk), object ID `1TnKihemzaQKU5MIWdcZz8zbQBS1VfxQe`.
- Dropbox receipt: `/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/WU088_HH_PHYS07_DELIVERY_RECEIPT_20261011_v1.json`, object ID `id:BSpOijBcT10AAAAAAD4CVw`.
- Drive 연구 ZIP: [WU088_HH_PHYS07_SOURCE_DOMAIN_MIXED_NCP_HANDOFF_20261011_v1_sha_16c39ce3526c.zip](https://drive.google.com/file/d/1MS6ICPHiFRMMqhRDPs4xYzaippH_8LTj/view?usp=drivesdk), object ID `1MS6ICPHiFRMMqhRDPs4xYzaippH_8LTj`.
- Dropbox 연구 ZIP: `/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/WU088_HH_PHYS07_SOURCE_DOMAIN_MIXED_NCP_HANDOFF_20261011_v1_sha_16c39ce3526c.zip`, object ID `id:BSpOijBcT10AAAAAAD4CUg`.
- Drive 전체 handoff: [WU088_HH_PHYS07_NCP_LOCAL_CODEX_HANDOFF_KO.md](https://drive.google.com/file/d/1UvaxCJK_NSIl4ZM6QDxI7XGFLluX3FL8/view?usp=drivesdk), SHA256 `13693d8ec02ad1bb33ac5e74ec69454ec697a746ee2322b4286c2abc2eb409e1`.
- Git receipt 경로: `research/r31ao_unequal_ladder/hh_phys07_source_domain_20261011_v1_delivery/WU088_HH_PHYS07_DELIVERY_RECEIPT_20261011_v1.json`. Core 이후 delivery commit에 들어간다.

위 파일들은 실제 upload ACK와 provider metadata의 이름·크기·목적지 확인을 마쳤다. 이번 게시에서 remote archive를 다시 내려받아 restore 실행을 했다는 뜻은 아니다. NCP가 실제로 사용한 복구 경로와 bytes/SHA 검증을 새 intake에 기록한다.

## NCP local Codex에 줄 작업 지시

WU088_HH PHYS07의 다음 NCP local 작업을 T01–T06까지 수행하라. 계획만 반환하지 말고 구현, 허용된 최초 source 산술, 독립 판정과 반환·백업까지 완료하라.

1. 이 START와 위 receipt를 읽고 실제 SHA를 확인한다. 연구 core `5cf77c2e56e9dc32596f9111620fd33de7d39e30`의 `research/r31ao_unequal_ladder/hh_phys07_source_domain_20261011_v1/`를 사용하거나 위와 같은 SHA의 ZIP 하나를 복구한다. 모든 payload를 MANIFEST/SHA256SUMS로 확인하되 과거 과학 suite나 성공한 PHYS07 Python reference를 다시 실행하지 않는다.
2. `SCIENTIFIC_CONTRACT.md`, `REPORT_KO.md`, `review/DECISION.json`, `CLAIM_LEDGER.json`, `BLOCKERS.json`, `theory/REFERENCE_ROOT_THEOREM_KO.md`를 읽고 reference와 native의 범위를 유지한다.
3. `handoff/NCP_LOCAL_CODEX_HANDOFF_KO.md`를 전체 실행 계약으로 사용한다. `handoff/NCP_TASKS.json`과 `handoff/NCP_RETURN_TEMPLATE.json`을 함께 적용한다. 두 Astra v4 archive의 지침을 읽고 실제 host model/routing/환경 identity를 기록한다.
4. 최신 PHYS06 NCP 고정 head `65a36e255aa6d9911e23a9b5ced18d8a9f507606`에서 사용자 작업을 보호하는 isolated worktree를 사용한다. 새 branch는 `codex/hh-phys07-ncp-20261011`, 새 directory는 `research/r31ao_unequal_ladder/ncp_phys07_local_20261011_v1/`다. 이미 존재하면 삭제/reset하지 말고 같은 task의 identity와 상태를 확인한다.
5. 완료된 PHYS06 energy/uniform/mixed/finite/paired adapter에 실제 public `phys04_prepare_family`와 `phys04_reduced_residual`의 source-specific producer를 연결한다. 같은 call의 source leaves, PreBE tuple, 전체 X/Theta의 Gc/A/partials/Hessian, C² 도메인 및 HH–photo source 방향미분을 보존한다.
6. 두 named first targets만 실행한다. 총 PreBE≤2, direct residual≤4, 내부 provider channel≤396, 조건부 uniform root 산술≤2다. Native endpoint/BE point/native root or certificate producer/IVP/heavy atomic/과거 suite는 각각 0이다. 예산과 실제 계측을 별도 기록한다. 실제 resource/command/source/binary identity를 고정한 뒤 dispatch한다.
7. Point seed와 기존 CommonFamily stored interval 입력의 차이, native direction/libm/PreBE leaf 차이를 보존한다. 저장된 reference root/W/I로 actual-native field를 채우지 않는다. 기체 열·이온화 energy의 finite sign, 실제 second-half carry와 full/two-half defect는 별도 미해결 항목이다.
8. 첫 실행 실패·수정·최종 코드의 실행 coverage를 보존하고 noncreator reviewer에게 판정을 받는다. `NCP_RETURN.json`, 한국어 반환문, 다음 handoff, manifest/receipt를 완성한다. 기존 Drive folder `1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM`와 Dropbox `/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928`에 새 이름으로 package와 모든 전달파일을 올리고, 추가 첨부 없는 START를 다시 제공한다.

이미 승인된 가역적 코드 작업과 additive Git/두 백업 전달에 단계별 재확인을 끼워 넣지 않는다. 실제 권한 또는 필수 host capability가 없는 작업은 해당 action과 이유만 명시하고, 수행 가능한 독립 작업과 reviewable 산출물은 완료한다. Native private permit issuer를 새로 만들거나 실제 관측되지 않은 counter/identity를 채워 넣지 않는다.
