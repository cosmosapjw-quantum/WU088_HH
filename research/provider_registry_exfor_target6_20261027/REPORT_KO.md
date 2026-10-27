# WU088_HH R3: target 6 EXFOR 직접 수치 자료와 원 28방향 참조 완비

## 결과

끊긴 런타임을 복구한 뒤 고정 인계 `34dd7d1d018abff8a0a4ebd1d3f3579ac46d2fad`, 완료 R2 source `71019bb469c92d1ea665155ed98c472b362d6706` 및 metadata HEAD `87933da5654bb2e4d93f7de4341df5e0fa0f8716`에서 이어갔다. 새 공식 EXFOR 원본 경로로 **⁴He(γ,d)D의 TABLE 공급자 4개·실제 수치 36행**을 회수했다. 기존 target6 정방향의 수치 source 의존성이 해소되어 **원래 19개 target ID, 28개 명시 방향 모두에 primary-source 참조가 있다.**

판정은 [SCIENTIFIC_ADMISSION.json](SCIENTIFIC_ADMISSION.json)의 `ACCEPT_SCOPED_EXFOR_TARGET6_SOURCE_REFERENCE_CLOSURE`다. 원자료 전사, 관측량 구분, 기존 target 방향의 참조 연결에 적용한다. 실제 rate·핵 Q·상태 가지·에너지 침적·consumer 승인은 모두 false다. 전체 확장 종·분자·상태 과정의 물리적 완비율을 100%라고 주장하지 않는다.

## 실제 새 공급자

공식 공급자 commit은 `IAEA-NDS/exfor_master@939a14d7bba1ddce51975cb5e8711ce96b3b0871`이다. EXFOR 원 entry 전체 bytes와 공급자가 반환한 Git blob SHA1, SHA256이 일치한다. CC-BY-4.0 license와 원 저자·논문·표 attribution을 보존했다.

| Supplier / EXFOR subentry | 실제 자료 | 에너지·관측량 | 행 수 |
|---|---|---|---:|
| `EXFOR_M0011002` | Arkatov 등, UFZ 23, 918 (1978), 저자 제공 TABLE | EN 26–65 MeV; SIG, MICRO-B, ERR-S | 14 |
| `EXFOR_M0475002` | Arends 등, Phys. Lett. B 62, 411 (1976), Table 1 | EN 213/258/330 MeV; ANG-CM 46/61/73/87도; DA, NB/SR, ERR-S | 12 |
| `EXFOR_M0475003` | 같은 Arends 실험 Table 2 | EN 201–359 MeV; SIG, NB, ERR-S | 6 |
| `EXFOR_M0826002` | Arkatov 등, YF 16, 12 (1972), Table 1; SNP 16, 6 (1973) 번역 | EN-MIN/MAX 30–75 MeV; SIG, MICRO-B, ERR-S | 4 |

원본: [M0011](https://github.com/IAEA-NDS/exfor_master/blob/939a14d7bba1ddce51975cb5e8711ce96b3b0871/exforall/M00/M0011.x4), [M0475](https://github.com/IAEA-NDS/exfor_master/blob/939a14d7bba1ddce51975cb5e8711ce96b3b0871/exforall/M04/M0475.x4), [M0826](https://github.com/IAEA-NDS/exfor_master/blob/939a14d7bba1ddce51975cb5e8711ce96b3b0871/exforall/M08/M0826.x4). 실제 36행의 124개 숫자 cell, DATA heading/units, BIB/COMMON과 1-based locator는 [PROVIDER_ROWS.json](sources/exfor/PROVIDER_ROWS.json)에 있다. 모든 수치를 공급자의 문자열로 보존했고 새로운 보간·외삽·적분은 없다.

예를 들어 M0011002의 EN=32 MeV에는 SIG=5.11 MICRO-B와 ERR-S=0.71 MICRO-B가 있고, M0475003의 EN=201 MeV에는 SIG=2.41 NB와 ERR-S=0.32 NB가 있다. M0826002의 네 bin 값은 다음과 같다. 이 예는 다른 실험을 결합한 새 계수나 오차 평가가 아니다.

| EN-MIN–EN-MAX (MeV) | DATA (MICRO-B) | ERR-S (MICRO-B) |
|---|---:|---:|
| 30–40 | 2.94 | 0.65 |
| 40–50 | 2.47 | 0.64 |
| 50–60 | 0.79 | 0.39 |
| 60–75 | 1.14 | 0.43 |

## 물리 사상의 범위

[LEXFOR 2025/05](https://nds.iaea.org/nrdc/nrdc_doc/iaea-nds-0208-202505.pdf)의 C.1/C.8/D.13/M.12를 직접 대조했다. **SIG 24행은 방출 각도·이차 에너지에 대해 적분된 단면적이고, DA 12행은 CM 미분 단면적**이다. M0826002의 입사 에너지 bin SIG는 면적 단위 자료로서 `∫σdE`에 해당하는 INT가 아니다. 실제 bin response 및 가중치가 미제공이므로 점별 σ(E)나 원하는 광자 스펙트럼의 평균을 새로 만들지 않았다.

네 main 표의 ERR-S는 통계오차다. M0826 parent에 있는 beam intensity의 ≤5% systematic bound는 그 자료에만 연결했다. 이를 정확한 Gaussian 5%로 바꾸거나 ERR-S와 합성하지 않았다. 공분산·신뢰확률·합성오차는 null이며 미제공을 0으로 취급하지 않는다. M0475002/003은 같은 실험의 두 관측량으로, 독립 실험으로 합산하지 않는다.

`M0011003`의 `EP/POLAR=2` 7행은 E2 성분이다. 별도 auxiliary에 보존하고 4개 main 공급자·36행 수 또는 전체 SIG에 더하지 않았다. `M0034005/006`, `M0826003`은 provider가 CURVE 출처로 표시하므로 전체 원 entry와 제외 locator만 보존했다. 그림 수치화는 하지 않았다.

기존 R2의 `TARGET19_PHOTONUCLEAR:06`은 He4 -1, D +2의 finite number projection이다. 조건을 갖춘 사건 flux `R`가 주어지면 material source는 `(-1,+2)R`, 흡수 광자 수는 `-R`다. 최종 D가 두 개라는 이유로 정방향 사건률에 초기 동일쌍 계수 1/2를 붙이지 않는다. 완전한 D 입자 수율의 DA라는 조건에서는 `∫dσ_D=2σ_event`지만, 선택 entry의 full/half-sphere 및 particle/event normalization은 아직 결속되지 않았다. 원 SIG/DA를 재정규화하지 않았다.

원 핵종 식별, ionic/electronic/nuclear-state binding, branch fraction, event normalization은 각각 별도다. Source의 He4/D 표기를 bare ground consumer 상태 승인으로 확대하지 않는다. Q 값·오차·질량 규약, branch fraction은 null이다. 원자–bare 질량 및 결합 에너지, 공분산, 에너지 분배, named MeV photon consumer가 남은 물리 입력이다. 자세한 유도는 [TARGET6_OBSERVABLE_MAPPING_KO.md](theory/TARGET6_OBSERVABLE_MAPPING_KO.md)에 있다.

## Registry와 완료 계산 재사용

[provider_catalog.json](registry/provider_catalog.json)은 R1의 102개 source variant·92개 species identity, R2의 26개 variant 및 R3의 4개 variant를 원 경로와 SHA로 연결한다. Isotope/isomer/charge/state/molecule/anion 및 약반응의 spectator electron·딸 상태·neutrino·Q/불확실성 기록은 R1/R2 그대로다. 서로 다른 source variant를 하나의 물리 과정으로 합치지 않는다.

[targets.json](registry/targets.json)은 원 19개 ID와 28개 방향을 유지한다. R2 target6 정방향의 **source metadata 5개 key**만 달라졌고, 원 물리 gate·branch/Q·선택 rate provider는 모두 같다. 기존 125개 R1 열 및 24개 R2 열, unchanged compiler와 249-check 결과를 재사용한다. 새 compiler 호출은 0이다. 249-check를 실제 rate·핵 Q 승인으로 확대하지 않았다.

원19 target은 원자 광이온화/재결합 세 계열, He4/He3/D/Li7 광핵 반응 여섯 계열, T와 n 약붕괴, 그리고 p(n,γ)D·D(p,γ)He3·D(D,p)T·D(D,n)He3·T(D,n)He4·He3(D,p)He4·He3(n,p)T·T(α,γ)Li7을 포함한다. 이번 source 완비 주장은 이 명시 목록의 방향에 적용한다. 추가 HD 형성·파괴, LiH 형성·비광자 파괴 및 미결속 isotope/state 자료는 기존 확대 registry의 열린 항목으로 유지한다.

## 검증과 독립 검토

- Source extraction과 overlay build는 첫 실행에서 성공했다.
- Targeted primary 검사는 **8/8군 PASS**다. 기존 target 구조·물리 필드의 보존, 11개 input SHA, 새 packet 및 source 참조, 관측량/오차 경계, 저장 사건 열의 동일성을 확인했다.
- 독립 원행 검토는 **기존 통과 8군 + 교정한 G6 = 9/9군**이다. main 36행·124 cell 및 BIB/COMMON을 실제 원본과 대조했다.
- 최초 independent01은 auxiliary E2에도 PRIMARY_SOURCE_ROW를 기대한 **checker 분류 오류**로 8/9였다. 실패 JSON/raw/argv를 보존했고 source 데이터는 변경하지 않았다. 표적 교정은 11개 조건과 5개 reuse identity guard만 실행했다. 통과한 8군과 main 36행은 다시 파싱하지 않았다.
- 별도 정적 구현 검토는 `PASS_SCOPED_STATIC_SOURCE_REFERENCE_OVERLAY_IMPLEMENTATION`, 차단 결함 0이다. 최종 [C9_FINAL.json](reviews/C9_FINAL.json)이 독립 source 및 구현 판정을 고정한다.

모든 검증은 새 입력의 전사·참조·정체성 범위다. 물리 rate의 오차·수렴, 핵 Q의 정확도 또는 실제 소비자 모델을 검증했다고 주장하지 않는다.

## 복구·예산·최신 병렬 작업

재개 당시 로컬 repo와 이전 ZIP이 사라져 있었으나 원격 R2 source/metadata 및 양쪽 backup 완료 영수증은 남아 있었다. 정확한 HEAD를 복구하고 Drive의 R2 ZIP 7,084,911 bytes를 실제 내려받아 SHA256 `43845ea085797a6d628b722d58197a64a0af6f0a34a708f3dc981a5274faa906`, CRC와 380개 파일 manifest hash를 확인했다. 이를 scientific failure나 새 계산으로 처리하지 않았다.

이번 source 단계의 측정된 bounded child는 최초 실패 포함 **5개**, CPU **0.920505 s**, wall **2.053690392 s**다. 이 합은 전체 세션 비용이 아니다. 회수·준비·정적 검토·metadata·remote 비용은 미측정이며 0이 아니다. PHYS91 primary/reference/Wolfram remaining=0, historical global CPU/money/remaining=null을 보존한다. 새 rate/Q/IVP 및 기존 science 재실행은 0이다. 전달 단계의 측정은 뒤의 별도 영수증으로 이어진다.

각 노드의 최신 root AGENTS/HEAD/백업과 병렬 작업을 확인했다. WU PR150의 시작 HEAD는 `87933da…`다. 중앙 REI `a5db4bac…`의 원88노드·27완료와 최신 미병합 작업 PR236 `ee94bef8…`의 32완료를 구분했다. 병렬 종 사영·normalized beta·native PW19/25좌표 source는 완료 근거를 재사용하며, 중앙 merge/ACK를 가정하지 않는다. 그 원자 입력을 현재 MeV 광핵 consumer로 전용하지 않는다.

[DAG.json](DAG.json)은 앞선 로컬19노드를 보존하고 R3 source 하위 노드 하나를 더한다. 원 전체 registry parent는 PARTIAL이고, 중앙 완료 노드를 새로 늘렸다는 주장은 0이다. HH_R10=OFF, production=NOT_ISSUED, L4_ready=false를 유지한다.

## 게시와 재개

사용자가 승인한 자동 게시·양쪽 백업을 이어서 수행한다. Source snapshot 시점에는 기대 부모 `87933da5654bb2e4d93f7de4341df5e0fa0f8716`에 대한 non-force 게시와 새 ZIP/Dropbox/Drive byte-readback을 준비한 상태다. 실제 성공 후 [delivery/PUBLICATION_AND_BACKUP.json](delivery/PUBLICATION_AND_BACKUP.json)에 source SHA·tree, ZIP SHA, provider ACK와 별도 metadata 자식의 의미를 기록한다. Source ZIP에는 현재 단위의 후속 전달 영수증이 들어 있다고 주장하지 않는다.

다음 과학 단계는 [NEXT_SOURCE_INTAKE_KO.md](NEXT_SOURCE_INTAKE_KO.md)를 따른다. 이 R3의 완료된 추출·빌드·검사를 다시 실행하지 말고 실제 변경된 source 또는 consumer 계약이 처음 필요한 지점에서 이어간다.
