# WU088_HH PHYS06 — 백업에서 바로 시작하는 NCP local Codex 안내

이 파일과 아래 프롬프트만으로 PHYS06 전달물을 찾을 수 있다. 사용자에게 추가 첨부를 요청할 필요가 없다. 기존 계정의 Git 또는 두 백업 중 사용 가능한 경로를 이용한다.

## 고정된 연구 결과와 다음 실행 범위

독립 판정은 `PROMOTE_SCOPED`다. P06-C01–C07은 에너지 좌표 이론, 조건부 uniform mixed rectangle 정리, 정확 유리수 참조 구현과 보관 입력 성분 진단의 범위에서 채택됐다. 실제 HH의 W, finite I_h, paired mixed scheme defect, native uniform root/tube와 continuous/time remainder는 null이며 physical/production은 HOLD다.

다음 NCP 작업은 `handoff/NCP_TASKS.json`의 T01–T07이다. 현재 native endpoint, BE point solver, native root/certificate producer, IVP, heavy atomic 및 과거 science suite의 실행 ceiling은 모두 0이다. 새로 구현하는 여섯 nonnative target과 명시된 제한 안의 좁은 build만 수행한다. 과거 완료된 PHYS04/PHYS05/NCP v2 검산을 반복하지 않는다. 미래 12-call proposal의 각 최대치는 현재 실행 권한이 아니며 request_ready=false다.

## 1. 저장소에서 복구

- Repository: https://github.com/cosmosapjw-quantum/WU088_HH
- Publication branch: `research/hh-phys06-energy-uniform-mixed-20261011`
- 고정 science core commit: `3382cd0edd71bf7a6491e5f68c1768ca92819d71`
- 고정 core root tree: `ba2f5c145efaceb369157608fbd64b1b808c81b6`
- Science core prefix: `research/r31ao_unequal_ladder/hh_phys06_energy_uniform_mixed_20261011_v1/`
- Delivery prefix: `research/r31ao_unequal_ladder/hh_phys06_energy_uniform_mixed_20261011_v1_delivery/`
- PR: https://github.com/cosmosapjw-quantum/WU088_HH/pull/35
- Detached receipt filename: `WU088_HH_PHYS06_DELIVERY_RECEIPT_20261011_v1.json`

Publication branch의 후속 delivery commit은 영수증·이 안내·index를 추가한다. Receipt의 `publication.commit`은 위의 고정 science core다. Branch 최신 head와 core commit이 같아야 한다고 요구하지 않는다. Branch에서 receipt를 읽은 뒤 core commit의 지정 prefix를 별도 연구 입력 폴더로 복구하고 `MANIFEST.json`/`SHA256SUMS`를 검사한다. 고정 core와 다른 내용이 보이면 과학 검사를 다시 실행하여 덮지 말고 식별 불일치를 기록한다.

기존 작업 디렉터리의 미커밋 변경은 보존한다. NCP 구현 기반은 아래 v2 commit이며, 연구 게시 branch 자체를 native 구현 base로 혼동하지 않는다.

## 2. Google Drive에서 복구

기존 폴더: https://drive.google.com/drive/folders/1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM

| 객체 | 정확한 이름 / ID |
|---|---|
| PHYS06 ZIP | `WU088_HH_PHYS06_ENERGY_UNIFORM_MIXED_NCP_HANDOFF_20261011_v1_sha_88f9576e346c.zip` |
| ZIP file ID | `1CjoAi9QvavNFVCXnXEAcVjInI2_oJcYo` |
| Detached receipt | `WU088_HH_PHYS06_DELIVERY_RECEIPT_20261011_v1.json` |
| Receipt file ID | `1Drnc69kaal1gOkXKKCk7tIvjgOF82KPS` |

ZIP 링크: https://drive.google.com/file/d/1CjoAi9QvavNFVCXnXEAcVjInI2_oJcYo/view?usp=drivesdk

Receipt 링크: https://drive.google.com/file/d/1Drnc69kaal1gOkXKKCk7tIvjgOF82KPS/view?usp=drivesdk

## 3. Dropbox에서 복구

기존 폴더:
`/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928`

ZIP:
`/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/WU088_HH_PHYS06_ENERGY_UNIFORM_MIXED_NCP_HANDOFF_20261011_v1_sha_88f9576e346c.zip`

ZIP file ID: `id:BSpOijBcT10AAAAAAD36pA`

Receipt:
`/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/WU088_HH_PHYS06_DELIVERY_RECEIPT_20261011_v1.json`

Receipt file ID: `id:BSpOijBcT10AAAAAAD36qQ`

두 백업에는 같은 ZIP 외에 독립적인 보고서·전체 handoff·NCP 작업 목록·반환 양식·receipt·이 START·backup index를 올렸다. Index의 각 객체 ID와 SHA256으로 대응 관계를 확인한다. 현재 전달 측 확인 범위는 upload ACK와 provider metadata 및 로컬 고정본의 hash/CRC다. NCP에서 실제 내려받고 복구를 확인하기 전에는 remote restore가 실행됐다고 기록하지 않는다.

## 4. 복구 시 일치해야 하는 값

| 항목 | 값 |
|---|---|
| ZIP bytes | 498718 |
| ZIP entries | 107 |
| ZIP SHA256 | `88f9576e346c719122f1c9735eb68e71db743bf80288d3ed62821231606b3146` |
| 내부 root directory | `HH_PHYS06_20261011_v1` |
| MANIFEST.json SHA256 | `c5fd9ac164a1ab10a751b471dd1297b0aefaa9627c99007fa56bb1bc7abd50c3` |
| Detached receipt SHA256 | `63bdc0d575ecebc32e66c08e4d07acae44979b73f92d0ea03a9597eb779ea405` |
| 전체 handoff SHA256 | `1f778101ee67a13915bfe77a2fe033075db539af01d85da8f2cb9fc9ab30e2c1` |
| NCP_TASKS.json SHA256 | `fe2f3666a14c0c213e5dc63fae1eb83818858aef6d49c478574921d63104461d` |
| NCP_RETURN_TEMPLATE.json SHA256 | `8a17d713095cf799313edd6e0dfbfa2965b5350167a63cc610fdeb95e32a6222` |

압축을 안전한 새 폴더에 풀고, 복구한 package root의 `tools/verify_package.py`를 실행한다. 이 도구는 payload hash만 확인하며 연구 검산을 실행하지 않는다. Git 경로로 복구했으면 prefix 내부를 package root로 취급한다. ZIP 원본 자체 SHA와 내부 manifest SHA는 서로 다른 대상을 식별한다.

## 5. NCP 구현 base와 산출물

- 현재 고정된 NCP v2 branch: `codex/hh-phys04-ncp-20261011`
- v2 head: `4b9231a0eff113701e7178ad98624233f387dd15`
- v2 tree: `10a19c64b17352095ce7874284fb12cc5b8b0e54`
- v2 science implementation core: `892eca446ce23815d103f162dbd71c198a1e6198`
- 새 작업 branch 제안: `codex/hh-phys06-ncp-20261011`
- 새 산출물 prefix: `research/r31ao_unequal_ladder/ncp_phys06_local_20261011_v1/`

실제 로컬 상태를 먼저 읽고 base identity를 확인한 뒤 isolated worktree를 만든다. 이미 더 새 결과나 동명 작업 branch가 있으면 그 기록을 읽고 진행 중 작업을 보존한다. 오래된 source/ABI/binary hash는 historical build pin이며 새 빌드의 실제 관측값을 대신하지 않는다.

## 6. 바로 붙여넣는 실행 프롬프트

```text
WU088_HH의 PHYS06 NCP local Codex 작업을 이어서 실행해줘.
추가 사용자 첨부 없이 기존 Git/Google Drive/Dropbox에서 다음 고정 전달물을 복구해줘.

Repository: cosmosapjw-quantum/WU088_HH
Publication branch: research/hh-phys06-energy-uniform-mixed-20261011
Science core commit: 3382cd0edd71bf7a6491e5f68c1768ca92819d71
Science core tree: ba2f5c145efaceb369157608fbd64b1b808c81b6
Core prefix: research/r31ao_unequal_ladder/hh_phys06_energy_uniform_mixed_20261011_v1/
Delivery prefix: research/r31ao_unequal_ladder/hh_phys06_energy_uniform_mixed_20261011_v1_delivery/
Receipt: WU088_HH_PHYS06_DELIVERY_RECEIPT_20261011_v1.json

ZIP: WU088_HH_PHYS06_ENERGY_UNIFORM_MIXED_NCP_HANDOFF_20261011_v1_sha_88f9576e346c.zip
ZIP SHA256: 88f9576e346c719122f1c9735eb68e71db743bf80288d3ed62821231606b3146
ZIP bytes: 498718; entries: 107
MANIFEST SHA256: c5fd9ac164a1ab10a751b471dd1297b0aefaa9627c99007fa56bb1bc7abd50c3
Drive ZIP ID: 1CjoAi9QvavNFVCXnXEAcVjInI2_oJcYo
Drive receipt ID: 1Drnc69kaal1gOkXKKCk7tIvjgOF82KPS
Dropbox folder: /BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928
Dropbox ZIP ID: id:BSpOijBcT10AAAAAAD36pA
Dropbox receipt ID: id:BSpOijBcT10AAAAAAD36qQ
Receipt SHA256: 63bdc0d575ecebc32e66c08e4d07acae44979b73f92d0ea03a9597eb779ea405

복구 후 전체 handoff/NCP_LOCAL_CODEX_HANDOFF_KO.md,
handoff/NCP_TASKS.json, handoff/NCP_RETURN_TEMPLATE.json,
SCIENTIFIC_CONTRACT.md, review/DECISION.json을 읽어 실제 작업 계약으로 사용해줘.
Bundled harness와 HARNESS_SELECTION.json, 저장소의 적용되는 AGENTS.md도 읽어줘.
본 START는 전체 handoff를 대체하지 않는다.

고정 NCP 구현 기반은 codex/hh-phys04-ncp-20261011의
4b9231a0eff113701e7178ad98624233f387dd15
(core 892eca446ce23815d103f162dbd71c198a1e6198)이다.
기존 변경과 HH history를 보존하고 isolated worktree에서
codex/hh-phys06-ncp-20261011 작업 branch를 사용해줘.

T01–T07을 완료해줘:
에너지 residual/jet 직접 변환 ell*G,
Jnorm과 rounded heat-leaf Psi 및 그 total derivatives 보존,
uniform source/root-domain adapter와 interval validator,
finite rectangle 및 paired DeltaW/비선형 observable adapter,
6개 새 nonnative targeted tests, 좁은 build, 독립 판정, NCP 반환 및 기존 두 백업 게시.

현재 native endpoint / BE point solver / root certificate producer /
IVP / heavy atomic / 과거 science suite 실행 ceiling은 모두 0이다.
완료한 seed/receipt/Hessian/v2 oracle 및 PHYS04/05 검사를 다시 실행하지 말아줘.
새 generic target과 명시된 bounded build만 수행하고 첫 실행 증거와 실패를 보존해줘.
미래 proposal의 endpoint/point/root 최대치는 현재 권한이 아니다.

P06-C01–C07은 이론·reference·archived component 범위에서만 PROMOTE_SCOPED다.
actual W, finite I_h, paired mixed scheme defect, actual native uniform root/tube,
continuous/time remainder는 근거가 없으면 null/HOLD를 유지해줘.
private permit이나 issuer를 우회하거나 새 실행 권한을 만들어내지 말아줘.

NCP_RETURN_TEMPLATE의 실제 관측값, source/build pins, 실행 계수,
원본 stdout/stderr/exit/time/RSS, review, unresolved를 기록하고
새 산출물 prefix research/r31ao_unequal_ladder/ncp_phys06_local_20261011_v1/
및 기존 두 백업에 추가 저장해줘. 실제 ACK/ID/hash를 detached receipt로 연결해줘.
업로드와 로컬 검사, 실제 remote restore를 각각 수행한 범위대로 보고해줘.
```

## 함께 읽을 파일

`REPORT_KO.md`, `theory/ENERGY_COORDINATE_KO.md`,
`theory/UNIFORM_MIXED_RECTANGLE_KO.md`, `CLAIM_LEDGER.json`,
`RUN_LEDGER.json`, `FAILURE_LOG.md`, `inputs/ncp_v2/`,
`evidence/`는 모두 위 ZIP와 고정 Git core에 포함돼 있다.
