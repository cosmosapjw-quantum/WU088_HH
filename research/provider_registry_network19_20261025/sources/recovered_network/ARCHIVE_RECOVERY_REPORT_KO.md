# 연결 archive에서 원 핵반응 PNG와 19개 사용자 목표 회수

## 결과

**원 PNG를 실제로 복구하고 열람했다.** `primordial_target_network.png`는 1,856,861 bytes, SHA256 `472ba6be633d2b5fc05fc1e0e88f965ff3c0311b0697e3c35c05bbca1629e6f9`이며, 기존 고정 계약이 기록한 원본 identity와 정확히 일치한다. 같은 archive의 `source_network.png`는 byte-identical 별칭이다. 따라서 원 PNG의 `NOT_RECOVERED_NOT_READ`와 locator 미확인 상태는 이번 증거로 해소된다. 앞선 `NEXT_SOURCE_INTAKE_KO.md` §4는 연결 계약과 archive를 추가 회수하기 전의 제한된 판정이며 이 결과가 이를 대체한다.

그림 오른쪽의 19개 반응식을 직접 읽고 보존된 `TARGET_NETWORK_19.json`과 대조했다. 19개 모두 일치한다. 이 계약은 실제 사용자 목표의 보존 목록이다. 별도로 회수한 18-family 계약은 all-bare·즉시 열화·passive-reservoir 조건부 민감도 모형이다. 두 목록 모두 실제 경험적 rate·핵 Q·이온 생성물 상태·에너지 분배의 신규 승인을 뜻하지 않는다.

## 회수 경로와 정확한 identity

처음 지정된 두 ZIP은 기존 scratch에서 찾아 재사용했고, 크기와 SHA256이 모두 일치했다.

| ZIP | bytes | SHA256 |
|---|---:|---|
| `PHYS91_FINAL_20261025_2912a315aa39.zip` | 37,419,031 | `b12f946dabe2f15e242e489977102abebdd58d3ce8acf336ec0753c25c74f2b7` |
| `orchestration_20261025_S2_published_handoffs.zip` | 1,817,017 | `019a7b333587faad801992cc598f1526f51efa57497911bebd530dc1655fccaa` |

PHYS91 내부의 실제 연결 계보를 따라 PHYS90, 89, 88, 87, 86, 85, 84, 83_CONT, 82와 PHYS88에 포함된 BASS_B3C selected source ZIP을 읽었다. 중앙 S2를 포함하여 **12 ZIP / 3,171 member entries**를 조사했다. 그 14 PNG와 1 SVG의 이름은 기존 진단 figure였고, 원 network PNG는 그 archive member에 없었다. 두 보존 실패 ZIP은 이름·크기만 기록하고 열지 않았다. 정확한 archive-level identity, 전 member 이름·CRC·크기와 제한된 문서 검색 결과는 `ARCHIVE_MEMBER_INSPECTION.json` 및 `INSPECTED_MEMBERS.tsv`에 있다.

PHYS88에 내장된 `BASS_B3C_S2_FINAL_20261024.zip`의 `intake_raw/crossrepo/rei_bianchi__pulls__page001.json`에서 다음 두 참조를 찾았다.

- [고정 19반응 목표 계약](https://github.com/cosmosapjw-quantum/rei_bianchi/blob/c9deb933761a8d2593d1176aee028cd423bdbc05/research/atomic_nuclear_ssot_20261017/run19/metals/network/TARGET_NETWORK_19.json)
- [직접 연결된 최종 RUN19 aggregate](https://drive.google.com/file/d/1pRPhitdAFfEU8HrSC02uXXVXwRI1U8wk/view)

고정 계약은 원 upload 경로와 PNG 크기·SHA를 명시했다. 같은 commit의 [ARCHIVE_ONLY_FILES.json](https://github.com/cosmosapjw-quantum/rei_bianchi/blob/c9deb933761a8d2593d1176aee028cd423bdbc05/research/atomic_nuclear_ssot_20261017/run19/metals/ARCHIVE_ONLY_FILES.json)은 PNG가 Git 본문에서 제외되고 전체 archive에 보존됐음을 명시했다. 과거 upload 디렉터리는 현재 scratch에 없었다. 따라서 위 Drive의 정확한 연결 archive 하나를 회수했다.

`REI_RUN19_FINAL_T_RATE_ACCELERATION_LI_BE_20261020.zip`의 실제 크기는 25,344,988 bytes, SHA256은 `6421ead745f3e5d298286e13b9515b7f668dcbb72de11b9f86650021c92b4f62`다. 1,175개 member 이름을 기록하고 다음 원 member를 추출했다.

`research/atomic_nuclear_ssot_20261017/run19/metals/network/primordial_target_network.png`

PNG 크기·SHA는 위 source identity와 일치한다. archive에 함께 든 `TARGET_NETWORK_19.json`도 고정 Git 계약과 byte-identical이다. 원 PNG의 Git-blob identity는 `d4010bf51f7d2dc1ae7a6112826cae5a8399f739`다. 다운로드 URL의 임시 접근 서명은 receipt에 보존하지 않았다.

## 회수된 사용자 목표 19개

원 그림의 왼쪽 화살표/번호에는 오른쪽 식과의 불일치가 있으므로 고정 계약대로 **오른쪽 목록**을 target identity로 유지한다. `p`는 핵 수준 proton이며 중성 H I 생성물 상태로 자동 배치하지 않는다.

| ID | 원 그림 오른쪽 식 | source qualification |
|---:|---|---|
| 1 | H I + γ ↔ H II + e− | 전자 과정; isotope coefficient binding 별도 |
| 2 | He I + γ ↔ He II + e− | 전자 과정; isotope coefficient binding 별도 |
| 3 | He II + γ ↔ He III + e− | 전자 과정; isotope coefficient binding 별도 |
| 4 | 4He + γ ↔ 3He + n | 광핵 target; source·state·energy 결속 필요 |
| 5 | 4He + γ ↔ T + p | 광핵 target; source·state·energy 결속 필요 |
| 6 | 4He + γ ↔ D + D | 광핵 target; source·state·energy 결속 필요 |
| 7 | 3He + γ ↔ D + p | 광핵 target; ID13과 물리적 중첩 보존 |
| 8 | D + γ ↔ p + n | 광핵 target; ID12와 물리적 중첩 보존 |
| 9 | T → 3He + e− + ν̄e | β− target; daughter shell·lepton·energy 분배 별도 |
| 10 | n → p + e− + ν̄e | β− target; proton/electron/antineutrino 명시 |
| 11 | 7Li + γ ↔ 4He + T | 광핵 target; ID19와 물리적 중첩 보존 |
| 12 | p(n,γ)D | radiative capture target |
| 13 | D(p,γ)3He | radiative capture target |
| 14 | D(D,p)T | nuclear transfer target |
| 15 | D(D,n)3He | nuclear transfer target |
| 16 | T(D,n)4He | nuclear fusion target |
| 17 | 3He(D,p)4He | nuclear fusion target |
| 18 | 3He(n,p)T | nuclear transfer target |
| 19 | T(α,γ)7Li, α=4He | radiative capture target |

7/13, 8/12, 11/19의 중첩은 사용자의 19개 ID를 줄이지 않는다. 하나의 평가 event를 복수 target ID에 연결할 때는 signature/owner로 중복 계산을 방지하고 정·역 계수의 출처를 별도로 결속한다. 그림에는 n, H/D/T, He3, He4, Li7 grid가 있다. Li6는 아래 18-family 모형이 선언한 추가 closure이며 원 그림에 있었다고 기록하지 않는다. 원 그림 회수는 모든 미래 isotope/isomer/daughter·분자 확장의 완전 열거를 뜻하지 않는다.

## 18-family 계약의 의미

PHYS83_CONT_FINAL의 `private_evidence/current_delta/receipts/c23a_science_commit.json`에는 [고정 NUCLEAR_NETWORK_CONTRACT.json](https://github.com/cosmosapjw-quantum/rei_bianchi/blob/9620e1fcc4bdda76e0311206f614234926600381/research/rei_tritium_production_audit_20261022/NUCLEAR_NETWORK_CONTRACT.json)의 byte identity가 있었다. 실제 회수 파일은 11,014 bytes, SHA256 `68f69ea6288f3ba45abe4ef9416b3d0cbe507f61543a4ff045ad914061acbe3c`로 기존 receipt와 일치한다.

13개 dossier nuclear family에 선언된 Li closure 등 5개를 더한 18개 family다. 원행 ID·reactants/products·계수 literal·단위·provider label·역반응 모형은 `RECOVERED_TARGETS_AND_CONDITIONAL_FAMILIES.json`에 원행번호와 함께 보존했다. 이번 검토에서 원 supplier 논문의 수치를 새로 재평가하지 않았다.

계약의 조건은 100–10000 K, bare nuclei, 즉시 열화와 passive reservoir다. constant-S 또는 thermal 1/v continuation과 inverse 모형을 사용하는 source 계약이며, 보편적 empirical rate 승인이 아니다. Li 원자 전자결합 에너지 생략을 명시한다. Li6(n,α)의 940-barn literal은 total absorption을 우세 nα branch로 배정한 근사라고 직접 표시한다. 외부 photon inverse의 zero는 지정된 soft UV support 조건이며 핵 광분해 전체의 부재가 아니다. isomer별 원행, 생성물의 전자 상태, 계수 covariance 및 완전 beta energy partition은 제공되지 않는다. 표의 branching을 임의의 확률로 정규화하지 않았다.

## 전달 파일과 작업 범위

- `ORIGINAL_NETWORK_RECOVERY.json`: exact 원 PNG 회수·열람 receipt.
- `RECOVERED_TARGETS_AND_CONDITIONAL_FAMILIES.json`: 19 target 원행과 18 conditional source family.
- `raw/`: 고정 JSON/한국어 계약과 archive-only manifest.
- `RUN19_AGGREGATE_MEMBER_LIST.json`: 새로 회수한 정확한 aggregate의 member 이름.
- `ARCHIVE_MEMBER_INSPECTION.json`, `INSPECTED_MEMBERS.tsv`: 먼저 지정된 두 ZIP 및 내부 연결 계보의 조사 기록.

새 archive 다운로드는 정확히 1개다. PHYS91와 중앙 S2 다운로드는 0회이며 이미 가진 원본을 재사용했다. 프로젝트 코드 실행, IVP, actual rate/Q 평가, 249-check 재실행, repository/registry 수정은 모두 0이다. 기존 numerical/resource 예산과 완료 계산은 변경하지 않았다.
