# PHYS78 이후 재개를 위한 실제 identity 대조

## 판정

현재 확인한 WU088_HH 원격 과학 기준은 사용자 전달과 일치한다. PR133은 draft/open이며 실제 branch HEAD는 `91d0846a940abf7817c900102dab488ff87e6a82`다. 이 commit의 직접 부모는 과학·결과 commit `b001e69668b2d2c2557b51830f5f732164b56ce0`, root tree는 `d22216ebb4b6799f1ce061f08aaf0ea77923dbfc`다. 두 commit 간 실제 diff는 10개 문서·전달 파일만 포함하고 source/tests/raw results/figures 변경은 없다. 기존 완료 실행과 35개 고유 경량 시험의 evidence를 이 identity 아래 재사용할 수 있다. 이번 inventory는 과학 코드를 실행하지 않았다.

PR128 `92f5ab9dba531ebe05909dcb77d3740d2c68c580`은 현재 HEAD의 실제 조상이며 compare 결과는 ahead17/behind0이다. PR129 `b76fd4b5d0dfe4850ebde66a8a10f78402d36c00`의 실제 PR head도 전달과 일치한다. PR128 비교의 파일목록은 GitHub API 300-file cap이 있어 전체 source 차이를 그 목록만으로 판정하지 않았다. 조상 관계만 채택했다.

근거: `wu_head_commit.json`, `science_to_final.json`, `wu_baseline_ancestry.json`, `wu_prs.json`, `wu_branches.json`.

## 실제 조사 범위

- 연결에 노출된 사용자 repository catalog 51개를 조회했다.
- WU088_HH branch refs는 pagination100+42, 총142개를 열람했다.
- WU088_HH20, rei_bianchi12, bass_cr12, BASS_HE12, bass12, rec_bianchi6: 총74개 최근 PR metadata를 조회했다.
- 관련 새 sibling7개는 PR metadata와 별도로 실제 `git/ref/heads/...`를 조회하여 head 일치를 확인했다.
- 선택된 과학 report/contract/summary/paired check/실행·검토 receipt를 읽었다. 모든 branch의 모든 파일, 모든 cloud backup archive를 조사한 것은 아니다.
- 별도 비공개 대화 원문은 회수하지 않았다. 이 inventory는 접근할 수 없는 대화의 전수조사를 주장하지 않는다.
- NCP, 완료 HH1231/REI729/HH74control63/PHYS78의 신규 실행 또는 재실행은0이다.

## 최종 백업·전달 identity

최종 ZIP `PHYS78_FINAL_20261021_91d0846a940a.zip`의 현재 provider metadata는 양쪽 모두10,562,602bytes이며 지정 ID와 일치한다.

- Drive: `1so8SEKteQjhW3idfuabomxJJKaQ19qNt`, modified `2026-10-21T16:10:49.058Z`.
- Dropbox: `id:BSpOijBcT10AAAAAAD_hqA`, revision `65e5bfe546cc40af03d47`, server modified `2026-10-21T16:11:02Z`.
- 전달 receipt의 ZIP SHA256: `3eca5c5f6667af5cb0acf8ac26ad7dd65e77288bb07b05df8336a027547411c4`.

외부 `PHYS78_FINAL_DELIVERY_20261021.json`을 양쪽 지정 ID에서 읽었다. Drive는 원본 raw bytes17511을 반환했고 SHA256은 `eeeedb2d026584ab536a0317bf56e8abfc80bc82db04786e6bab131227a55a7c`다. Dropbox extracted text는 끝에 LF1개를 덧붙여17512bytes가 되었지만 JSON value는 완전히 동일하다. Dropbox의 원본 metadata size는17511이고 provider content hash `10aa08af124c697568b2e34f079e3d9e5c50fd39681a0f31f7e107621c56a64a`는 Drive raw bytes로 계산한 Dropbox block hash와 일치한다. extracted-text hash와 raw-byte hash를 구별했다.

이번 조회는 ZIP 전체를 다시 다운로드하지 않았다. 2026-10-21의 양쪽 전체 ZIP bytes/CRC/375payload SHA PASS는 최종 delivery JSON의 과거 실행 receipt로 재사용한다. 새 whole-ZIP restoration을 수행한 것처럼 보고하지 않는다. 작은 JSON의 Dropbox raw GET을 한 번 시도했으나 sandbox socket 정책이 HTTP 요청 전 `PermissionError [Errno1]`로 차단했다. 따라서 그 GET은 새 원격 byte restore 근거가 아니다. provider hash·size와 읽은 JSON의 의미 일치가 현재 대조 근거다.

근거: `drive_final.json`, `dropbox_final.json`, `final_json_identity_comparison.json`, `backup_metadata_current.json`, `wu_s2_backup.json`, `wu_s2_pub.json`.

## 새 sibling 실행과 채택 범위

| 원격 기준 | 새 실제 전달 | PHYS78와의 차이 및 채택 |
|---|---|---|
| rei_bianchi PR220 `8be7533cc97b3302bf42608699d6e8313ed6af8a` | 127compact+2full62 oracle, paired 비교 저장 | 지정T100–12000K, 외부UV5–200eV, photo/RR/DR, test-fluid. CI/CX와 열·복사 closure는OPEN. 상태 축약의 수학적 구조만 참고하며 trajectory를 PHYS78와 합산하지 않는다. |
| bass PR180 `574c3af93810122af0a7977e00e34195e5251a09` | 같은 compact 연구의 mirror | 독립 실행 하나를 추가한 것으로 세지 않는다. |
| rei_bianchi PR219 `2c6aa0a14102cbe296a596b759f159a9f3d96b99` | 저장82background에서 DD·18-family nuclear passive sensitivity, 새backgroundIVP0 | All-bare·instant-thermalization·fixed-bulk 조건. 34directed채널 중8external-photon support-zero. C9 PASS_SCOPED를 실제 확인했으나 ionic/thermal coupled closure로 채택하지 않는다. |
| rei_bianchi PR218 `4c8794e6e7c4ac553cc85fee728ef9ab6fe81fa8` | 79nominal+3refinement=82 | 지정온도, UV5–60eV, photo/RR, test-fluid; CI/DR/CX와 에너지 closure는OPEN. |
| bass_cr PR96 `a5e12c5f3e6d323e211d65fefad34060ec07eff0` | 45+6조건부 pilot와 이후 byte복구·저장데이터 분석 | 원과학commit `6b6db06e8148e6826a2d5bf7dbc53d362126ca62`. prescribedT/UV, photo/Case-A RR–electron–Thomson. CI/DR/CX/thermal closure는OPEN. 최신 문서복구는 새IVP0. |
| BASS_HE PR85 `88f9957d219f71b458b3bcaf41ccdde60538379f` | 392nominal+2L24guard, 실제 recovery raw394 | 고정20000K, photo/RR만, 기체pi=0. 원자료소실 때문에 같은identity recovery394회를 별도로 회계한다. PHYS78재실행 근거로 쓰지 않는다. |
| rec_bianchi PR119 `ad93fa1c71f8a2b2a0b19836be3c7b739b11b0c7` | 고유125main+1opacity-off=126 | 62state, photo/RR/DR, prescribedT/UV, Li inner-shell one-step 근사. `THEORY_KO.md`의 필요한 순기체에너지 유도는 참고할 수 있으나 escaping-RR energy/ionic yield는 별도의미해결이다. |

REI219 최종 summary의 surviving `log10(Y_T)=-103.855771...`, `log10(Y_n)=-109.658970...`는 위 passive nuclear closure의 수치결과다. PHYS78에서 n/T가 정확히0인 것은 해당 zero-source model의 성질이며 물리적 모든 생성과정을 금지하는 명제가 아니다. 두 해석을 분리한다. 이 nuclear 결과를 이번 CI/CX branch에 자동결합하지 않는다.

## 구현 재사용 시 실제로 보존할 조건

1. REI220/HE32의21→9 동위원소 축약은 같은원소의 electronic rate와 초기charge fraction이 같을 때의 불변부분공간이다. PHYS78의 HII/H=2e-4·D중성 초기조건은 H1/D의 같은분율 조건을 만족하지 않는다. 원래 초기조건을 보존하면 이 축약을 그대로 적용할 수 없다.
2. REI219의 `nuclear_intake/RUN19_full_network.rs`는 이름과 달리 atomic photo/collisional/charge-exchange source라는 점이 계약에 명시돼 있다. 이것은 CI/CX coefficient provenance를 확인할 재사용후보이며 그 파일의 존재 자체가 source/domain/energy admission은 아니다.
3. 200eV Li inner-shell one-step 모델과 PHYS78 18/30/60eV source는 별도 identity다. hard-UV·Auger/branching·core energy 계약 없이 LiIII/IV 활성화의 근거를 옮기지 않는다.
4. 모든 비교는 같은 normal orthonormal frame에서 signed tensor를 합한뒤 norm으로 읽었다. 다른branch의 prescribedT/UV, Thomson/ne 또는 nuclear passive 결과를 PHYS78의 자기일관 thermal solution으로 대체하지 않는다.

## 직접 열람한 주요 원본

- https://github.com/cosmosapjw-quantum/WU088_HH/pull/133
- https://github.com/cosmosapjw-quantum/rei_bianchi/blob/8be7533cc97b3302bf42608699d6e8313ed6af8a/research/rei_hheli_compact_pilot_20261022/REPORT_KO.md
- https://github.com/cosmosapjw-quantum/rei_bianchi/blob/2c6aa0a14102cbe296a596b759f159a9f3d96b99/research/rei_tritium_production_audit_20261022/NUCLEAR_NETWORK_CONTRACT.md
- https://github.com/cosmosapjw-quantum/rei_bianchi/blob/2c6aa0a14102cbe296a596b759f159a9f3d96b99/research/rei_tritium_production_audit_20261022/review/NUCLEAR_NETWORK_DECISION.json
- https://github.com/cosmosapjw-quantum/bass_cr/blob/a5e12c5f3e6d323e211d65fefad34060ec07eff0/research/cr_c21o_hheli_z2_20261021/PHYSICAL_CONTRACT_KO.md
- https://github.com/cosmosapjw-quantum/BASS_HE/blob/88f9957d219f71b458b3bcaf41ccdde60538379f/research/he32_sandbox_primordial_20261021/RESULTS_KO.md
- https://github.com/cosmosapjw-quantum/rec_bianchi/blob/ad93fa1c71f8a2b2a0b19836be3c7b739b11b0c7/research/rec_rei_hheli_sandbox_20261021/THEORY_KO.md

HH_R10=OFF, Production admission NOT_ISSUED를 유지한다. 다음 과학DAG는 COLLISIONAL_ATOMIC_AND_THERMAL_CLOSURE이며 RECOMBINATION_TO_Z20_INITIAL_CHARGE_CONTRACT도OPEN이다.
