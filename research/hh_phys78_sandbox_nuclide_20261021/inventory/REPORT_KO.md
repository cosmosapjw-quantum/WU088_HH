# PHYS78 시작 전 최신 identity·완료 결과·열린 DAG 조사

## 판단

HH의 실제 다음 additive parent는 **PR132, `d43cf2df2c4864ae05049f44301c5b389b80a49c`**이다. PR128–131과 PR132의 branch ref는 직전 기록과 일치한다. PHYS77 과학 source/results는 `04bc4a063384b2629a323ad15bdf6618fa8c14f0`이며, 마지막 HEAD는 후속 배송 metadata를 포함한다. PHYS78이 새 sandbox 실행과 H/He/Li 확장을 수행할 때 이 부모에 별도 연구 unit으로 쌓을 수 있다.

실제 최신 조사에서 REI D9, ACCEL03, HE31, C21N offgrid4, REC tangent가 새로 확인되었다. 완료 항목을 다시 실행할 필요가 없다. **H/He/Li 동위원소·전하단계를 모두 활성화한 z20→2 coupled 실행이 이 조사에서 확인된 것은 아니다.** 기존 Li 원자계수와 H/He/D owner는 재사용 가능하지만, isotope inventory·저온 계수 범위·전자/에너지 closure를 새 provisional 모델의 명시적 계약으로 연결해야 한다. 기존 `NOT_ADMITTED` 표시는 현재 물리 완성도의 한계이며, 사용자가 허용한 새로운 이론·코드·preliminary 실행을 금지하는 일반 규칙으로 확대하지 않는다.

조사자는 과학 실행·ODE·NCP·benchmark·원격 mutation을 수행하지 않았다. 원 source 26개를 내려받아 **26/26 Git blob SHA1 일치**를 확인했다. JSON의 SHA256도 각 파일에 대응한다.

## 조사 범위

2026-10-21 14:41 UTC 이후 실제 GitHub 읽기로 여섯 저장소의 advertised branch ref **1,060개**, 각 저장소 최신 updated PR 30개씩 **180개**를 확인했다. Ref 수는 HH141, REI258, bass264, BASS_HE89, bass_cr172, rec_bianchi136이다. 이는 ref 목록 전체와 선정한 최신 결과·source 파일의 조사이며, 모든 branch의 모든 파일을 읽었다는 뜻이 아니다.

Personal Context는 `Personal context is unavailable for this conversation.`을 반환했다. 따라서 비공개 다른 대화가 전수 관찰되었다고 주장하지 않는다. Drive 검색은 현재 관련 파일을 놓쳤고 PHYS77 검색이 과거 무관 PDF를 반환하기도 했다. 그 결과0을 부재 증거로 쓰지 않았다. 알려진 정확한 file ID의 metadata는 성공했다. Dropbox 검색의 시간 필터는 더 오래된 결과도 반환했으므로 실제 반환 timestamp로 다시 분류했다. 새 archive 전체 다운로드는 0회다.

## 실제 HEAD와 역할

| 저장소 / PR | 실제 branch HEAD | 현재 결과와 활용 |
|---|---|---|
| HH128 | `92f5ab9dba531ebe05909dcb77d3740d2c68c580` | PHYS75 과학 기준 유지. Separate signed stress와 8→3 상태 축소. |
| HH129 | `b76fd4b5d0dfe4850ebde66a8a10f78402d36c00` | Explicit source mapping을 요구하는 이전 standalone 도구의 보충 보존. |
| HH130 | `535d24dbccf4fab40fd11f36330a63c4e288e24c` | Long collisionless 1,231개 z20→2 이력 완료. |
| HH131 | `ec28299fe7e81aab184b93aff787cb00a185dd2e` | 네 D8 저장 표본 bracket identity 재사용 완료. |
| HH132 | `d43cf2df2c4864ae05049f44301c5b389b80a49c` | 한 실제 finite-owner IVP의 첫 cell enclosure, 공유 runner. 전체 이력 enclosure는 미완료. |
| REI199 | `cce008b3fc32c298185b30550b2cd909d74fcd87` | 새 D9 완료. 175×153 저장 이력의 성분별 전단 적분 budget. |
| REI213 | `d32cd99fa19c65aa1ca63dbc8aab8741834270e8` | 별도 warm729 owner. |
| REI215 | `926bae816ef8339137e2813cc40f1d514b763e1f` | ACCEL02의 실제 NCP5×2-step 반환 포함. |
| REI216 | `1f32cc442ebde284bbb944455ba96066c9e0e055` | HE30 D8 consumer, 원 bracket 완료. |
| REI217 | `de73c5d6c7bd3498571e9226298040d8259e1acf` | ACCEL03 portable aggregation, derivative response, 원 NCP 수치 동등성 판정 완료. |
| bass179 | `d14652646c1da77b6513e7f97725ff5dd5c1db4e` | ACCEL03 대응 저장소. |
| BASS_HE84 | `88e415c45d8607c85cd3ab36aabeaed4378820ce` | HE31 donor census, prepared FV, 실제 z20→4 donor on/off와 reference. |
| bass_cr95 | `8dc5031b3323d4be42a7444843294200aa8887f2` | Sandbox4와 동일 입력 NCP4 수용. 129 unique 입력. |
| REC118 | `99f5f4fb57358a0347286f8299977125a2724774` | Analytic JVP/VJP와 작은 tangent 연결 확인. 전체 z20→2 tangent 3개는 미실행. |
| REI210 | `e4c8133288614638792888367ca10b2ded3138ff` | Li/C/N/O 원자계수 catalog. 전하망·동위원소 coupled 진화는 포함하지 않음. |
| REI211 | `c9deb933761a8d2593d1176aee028cd423bdbc05` | H/He/D native rate cache와 기존 thermal owner. |

두 identity 불일치를 보존한다. bass_cr95의 PR head API는 `e7729092...`를 반환했지만 실제 branch ref와 직접 읽은 commit은 `8dc5031b...`다. 해당 final commit은 accepted NCP 수용 addendum과 closeout를 포함한다. REI199 PR 본문 상단의 과거 `964b2e3c...`는 최신 HEAD가 아니다. 현재 source path의 D9 DAG·상태를 실제 `cce008b3...`에서 읽었다.

## 새 완료 결과와 다음 DAG

### REI D9

`research/rei_unified_sigma_pi_20261021/UNIFIED_DAG.json`은 D9를 complete로 기록한다. Source/results commit은 `407f2a30efcdd0c4c4afb180cbe7d31f90cc0401`이다. 175 nominal history ×153 epochs, 35 exact reference를 사용했고 새 IVP·ODE callback·moment recomputation은 0이다. 최대 sampled scaled residual은 `1.473444875767401e-6`이다. 이를 continuum certificate로 부르지 않는다.

다음 노드는 **D10_ZERO_INITIAL_MATTER_STRESS_GENERATION**, `READY_FOR_THEORY_AND_SAVED_DATA_INTAKE_NOT_RUN`이다. 초기 matter stress가0인 기존 35 history를 exact pressure-moment 식에 연결하는 것이 입력이고 최초 새 IVP 허용은0이다. D9와 D8의 이미 끝난 계산을 반복하지 않는다. 현재 문서의 미래 NCP wrapper는 실제 실행 완료와 다르다.

### ACCEL03

REI217/bass179는 hardcoded729·64step 의존성을 제거한 plan-driven aggregation과 actual-sample plot을 제공한다. NCP target의5사례×2step은 이미 완료되어 기존40gate를 통과했고, 이 단계는 warm729 endpoint와15개의 서로 다른 실제 NCP 저장 시점을 재사용했다. 범위는 C15 warm conditional `a=0.1999→0.2`다. 이를 z20→2 전체 EoR 이력으로 합치지 않는다.

Fixed-weight massive response `J2_x=-5J2+J4`, `J2_b=-G`와 vector diagnostics가 재사용 가능하다. 원 radiation closure와 생산 solver는 바뀌지 않았다. ACCEL03은 closed scoped unit이며 더 실행할 pending case가 없다.

### HE31

원 구현 pin은 `1c8a56aac89d0e40ede8770009f80ebca40a4d2c`다. 실제 donor on/off2개와 original-evaluator reference1개가 끝났다. HII/HeII/HeIII census, proper/comoving 및 SI/cgs 변환, comoving-ne PCHIP, source support 밖 extrapolation 금지, prepared canonical FV, 공유 CPU/case lease가 구현돼 있다.

실제 donor는 R15/HG97-B의 prescribed Q closure이며 z4에서 끝난다. HII+HeII이고 HeIII=0, residual electron은 없다. Photon Thomson에만 직접 적용하며 massive matter와 photon/neutrino signed stress는 따로 저장한다. **물리적으로 지원된 z20→2 H/He donor가 다음 missing dependency**다. 현재 source guard를 제거하는 것은 이 결과의 재사용이 아니다. Pilot18/joint175의 전체 NCP 실행은 prepared-not-run이다.

### C21N과 REC

C21N의 새 opposing-stress4개는 z20→4 sandbox에서 완료됐고, 동일 입력 NCP4 반환도 별도로 수용됐다. 기존125와 합쳐 unique129이지133이 아니다. 236 FP64 arrays, 52,520 values가 sandbox/NCP 간 byte-identical이라는 수용 증거를 보존했다. 이는 uncached full-ODE paired replay나 global error bound를 뜻하지 않는다.

REC117의 175×153 trajectory reuse plot은 이미 완료됐다. REC118은 40-state RHS의 JVP/VJP와160-state forward tangent를 준비했으며 synthetic tiny window의 parent/augmented ODE2개만 수행했다. 전체 z20→2 신규 sensitivity3개는 `READY_NOT_SUBMITTED`다.

### HH PHYS77

PHYS77의 실제 DAG는 finite-owner whole-cell source/residual obligation을 `PARTIAL_SCOPED`로 둔다. 한 case 한 cell만 완료됐으며 three-prefix request3개×4cell는 `READY_NOT_RUN`이다. Full-history carry-forward, 과거 constructor와 machine trajectory 관계, angular truncation, momentum quadrature continuum, full native cold EoR, non-LRS 및 HH matched physical rate는 OPEN이다. 새 sandbox 최적화·다핵종 preliminary 경로가 이를 자동으로 닫지 않는다.

## H/He/Li 구현에 즉시 재사용할 파일

`sources/`의 파일은 각각 `SOURCE_READS.json`에 remote URL·HEAD·SHA256·Git blob SHA1을 연결했다.

| 로컬 파일 | 원 source / 재사용 목적 |
|---|---|
| `RUN19_igm_rates.rs` | REI211 `research/atomic_nuclear_ssot_20261017/run19/native/owner_src/igm_rates.rs`: H/He 계수와 원 cutoff/분기. |
| `RUN19_igm_thermal.rs` | 같은 owner의 냉각·Compton·전자밀도 및 thermal ledger 연결. |
| `RUN19_atomic_provider.rs` | 원 atomic provider, threshold·단위·유효범위. |
| `RUN19_deuterium_atomic.rs` | D의 H-equality approximation과 별도 D energy owner. |
| `RUN19_deuterium_charge_exchange.rs` | Savin source 범위·방향별 CX 식. |
| `atomic_report.md`, `atomic_DAG.json` | REI210 atomic catalog와 원전·계수 valid domain. |
| `ACCEL03_moment_response.py`, `ACCEL03_THEORY.md` | Warm massive response 식과 구현. |
| `ACCEL03_diagnostics.py` | Signed component, cancellation, tensor norm 및 finite checks. |
| `ACCEL03_aggregate.py`, `ACCEL03_plot_sweep.py` | Portable saved-result accounting, 실제 표본 provenance와 그림 생성. |

REI210 catalog 원경로는 `research/dossier_ssot_sandbox_20261016/bass_reactive_performance01_20261020/brperf01/atomic_theory/`다. `catalog/src/generated.rs`, `generate_catalog.py`, `data/PROVENANCE.json` 및 original tables의 추가 회수는 code78에게 전달했다. 중복 다운로드하지 않았다.

원 catalog는 Li/C/N/O bound-electron24단계의 PI·CI,12단계 RR를 제공하며 Li I/II/III의 RR3단계를 포함한다. Li6/Li7의 isotope-specific fit이나 abundance/binding/thermal/source owner는 추가하지 않았다. Voronov CI의 Tmin은 단계별로 최소1eV≈11604K이므로 이를 차가운 EoR 전체에 검증된 fit로 외삽하지 않는다. VF RR의 해당 구간은3–1e9K이고 LiI Verner outer-shell PI의 Emax는64.39eV다. Missing coefficient와0 coefficient를 구분한다. 이 조건을 지키면서 사용자가 요청한 새 explicit provisional closure와 species ledger를 연구할 수 있다.

## 백업 확인

이번에는 정확한 provider metadata와 기존 immutable receipt를 대조했다. 아래 과거 whole-byte readback을 이번에 다시 실행했다고 쓰지 않는다.

| 자료 | bytes / SHA256 | 현재 provider 관측과 이전 검증 |
|---|---|---|
| PHYS77 final |604893 / `bdd055c454aede256afb39d297b0ea7076e348973845c65c3c425bd04ea826e9`| Drive `1eL8fzySdDWMkCju2iHJiWBd-mKjZMdEa`, Dropbox `id:BSpOijBcT10AAAAAAD_hhw` 실제 size 일치. 기존 두 whole-byte/CRC/payload 검증 재사용. |
| D9 final delta |4576719 / `bf3547dd6542626d011d51251e1a091d9ac0cca5480d6124c6faca09cfc3d679`| Drive `1V-aTSz2A74dgKwXmkOeBh-EcE03RVZ5V`, Dropbox `id:BSpOijBcT10AAAAAAD_hkA` size 일치. Pinned receipt는 두 whole GET·100 members·94 source blobs PASS. |
| HE31 P2 final |2832001 / `e7a01a46b95ae30820bde7a46a6e94f920474a6e05574b188bb084051b51e577`| Drive `1-3utJjmUyFlzhXymeCcgOurJ02ruzoxC`, Dropbox `id:BSpOijBcT10AAAAAAD_hjw` size 일치. 원 ACK+size 검증이며 post-upload whole GET는 NOT_RUN. |
| ACCEL03 C |7286437 / `049af2b058d83c997c03c092e6ec90ab0f3411c45118719b75bf3f7dc27a04e4`| Dropbox `id:BSpOijBcT10AAAAAAD_hjQ` size 일치. 원 whole GET·SHA·blockhash·CRC·379member 검증 PASS. |
| C21N sandbox |38502346 / `c5ae168f04b0fde9232237e9337e224d5d1380723cead1cda529ba6f3c4a2df9`| Dropbox `id:BSpOijBcT10AAAAAAD_hjA` size 일치. 원 provider ACK이며 remote whole-byte revalidation NOT_RUN; Drive UNKNOWN 보존. |
| C21N closeout |442823 / 이번에는 archive SHA 회수 안 함| Dropbox `id:BSpOijBcT10AAAAAAD_hkQ` 실제 object 확인. Sandbox snapshot과 별도 NCP/addendum archive. |

PHYS75 recovery의 `PHYS75_FINAL_DELIVERY_20261021.json`, `POST_PUBLICATION_HANDOFF_KO.md`, `DAG_OVERLAY.json`도 읽고 pinned HH132 tree와 각각 blob identity를 확인했다. Recovery ZIP은952307bytes, SHA256 `33cf1a493a3c5b54eea9871255606e658c0625eda8578872ec29b9d2075521c9`이며 Drive exactID `1EA7MGuAzUnFMkjOj8zsHVPr-3vXxaI1u` metadata size도 일치한다. 해당 snapshot의 Dropbox 보충 ZIP은 `NOT_UPLOADED_TOOL_SOURCE_INTERFACE_BLOCKED`로 보존된다. 나중 PHYS77 백업 성공을 과거 PHYS75 보충 ZIP 성공으로 바꾸지 않는다.

## 전달과 다음 단계

이 read-only inventory checkpoint는 로컬 완성 및 부모 agent 전달 상태다. 원격 게시·백업 mutation은 수행하지 않았으며 root의 PHYS78 stage 게시/백업과 DAG에 편입할 수 있다. `INVENTORY_RAW.json`은 ref·PR 목록, `INVENTORY_FINDINGS.json`은 선택·범위·다음 obligation, `SOURCE_READS.json`은26source결속, `BACKUP_METADATA.json`은 provider 현재 관측, `HH_INITIAL_REQUIREMENTS_READBACK.json`은 요구된 기존 문서의 pinned identity다.

같은 정규직교 normal frame에서 signed matter/radiation tensor를 별도 보존하고 total tensor를 합한 뒤 norm을 취한다. Full Frobenius는 half-contraction의 sqrt2배다. Warm729, long1231, HH74 control63, B175/237, C21N129는 다른 scope와 identity를 가진다. 동일 trajectory source attribution을 species-off causal experiment로 해석하지 않는다. `HH_R10=OFF`, production admission은 `NOT_ISSUED`다.

다음 실제 작업은 HH132 descendant에서 사용자 목적에 맞게 finite isotope/ion registry와 지원 범위를 선언한 sandbox 실행 경로를 구현하는 것이다. 이미 완료된 scoped 과학 결과는 입력·방법으로 재사용하며, 새 all-nuclide closure와 새 결과 identity를 분리해 기록한다.
