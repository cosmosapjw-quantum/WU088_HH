# WU molecular R10 — 지정 owner 7개 ref 종료 시점 변경 조사

**HEAD 관찰: 2026-10-28 00:28:53 UTC (09:28:53 KST), 7개 확인 / 3개 이동 / 4개 불변 / HEAD 오류 0.** 최초 전수 조사는 2026-10-27 23:45:36–23:45:45 UTC의 51 repo·2375 heads·65 pages이며, 이를 재실행하지 않았다. 이 파일은 이후 지정 7개 ref만 확인한 부분 snapshot이다. WU 자체 진행은 제외했다.

| 저장소 / branch | 최초 SHA | 종료 snapshot SHA | 결과 |
|---|---|---|---|
| cosmosapjw-quantum/rec_bianchi / research/rec-h5-defect-bridge-independent-20261028 | `6fdf2cca545d9b44d0666bc22a3233a675e5ad03` | `6fdf2cca545d9b44d0666bc22a3233a675e5ad03` | 불변·기존 근거 재사용 |
| cosmosapjw-quantum/rei_bianchi / research/orchestration-sandbox-20261022 | `22a99cb9b1691274e74c122d54521be4f2f51ba5` | `22a99cb9b1691274e74c122d54521be4f2f51ba5` | 불변·기존 근거 재사용 |
| cosmosapjw-quantum/rei_bianchi / research/rei-causal-prefix-consumer-20261027 | `18e3bdfee44b7782d29179fa1cd9ddb873148e33` | `e77bc7ec48ae2aee8ded573e66ac0a1060017c54` | 이동 |
| cosmosapjw-quantum/bass / research/bass-b3h-restart-cocycle-20261028 | `4d6e166cf9a644392a8a2b68c4c171a1fb658240` | `f834101d3292f304681349db5d435c6f0c6b559e` | 이동 |
| cosmosapjw-quantum/vigilode / research/production-solver-closure-20261027 | `7eb2dd0ffda39afb2871d76700a720986ff09fe0` | `7eb2dd0ffda39afb2871d76700a720986ff09fe0` | 불변·기존 근거 재사용 |
| cosmosapjw-quantum/bass_cr / research/cr-he-event-union-20261028 | `65e20e40e3c1d9e8384101017dc8940b3d09de09` | `e91a0d19b13a0b3254c194e7a4863b845c271874` | 이동 |
| cosmosapjw-quantum/BASS_HE / research/he-azimuth09-20261028 | `307fee38cb65b957deea84c3308f59e972049362` | `307fee38cb65b957deea84c3308f59e972049362` | 불변·기존 근거 재사용 |

## 실제 변화와 범위

### BASS restart

과학·수행 상태는 18/20이며 R6/C9 distinct-author review가 NOT_RUN이다. FINAL_ROOT_ACK에서 게시·백업 완료 범위도 각각18/20으로 확인했다. 과학 source는 b8bd56bd5e54354dbe2a6617da33ec076467fe4e, 새 native ODE는0이며 중앙28/88, delta0이다. D archive는4,877,921 bytes, SHA256 53d8a64625a0d8a57cef5e2d2c5461d84932d599f4467bc87bf1a639c3f0ebac이고 두 provider ACK/metadata size가 기록돼 있다. 새 archive의 원격 bytes hash readback은false이다. 이 조사는 실제 원격 archive를 복원하지 않았다.

### REI finite thermal

유도5/10+코딩 설계4/10=9/20이다. R2–R5 네 문서와 C1–C4 공동설계 한 문서의 게시·dual backup, 총10 provider ACK가 새 종료 receipt로 확인됐다. 구현·수치 검증·native25·실제 source-matched bath/EOS 및 온도 갱신은 여전히 미완/null이다. 원격 backup byte download/hash는NOT_RUN이다. owner의 설계·예산 제한은 외부 사실로만 기록하며 WU 정책으로 이관하지 않는다.

### CR He event union — 새로운 조건부 과학 입력

초기 새 branch는 predecessor PR111 D commit65e20e40e3c1d9e8384101017dc8940b3d09de09를 가리켰다. 종료 head에는 별도 CR_PHYS02_HE_EVENT_UNION_V1의 계약·이론·구현 및 단계기록이 추가됐다. 유한 고정 He electron marginal에서 cross-birth-partition duplicate correction의 sharp envelope `0 <= C <= min(N/2, N - max_i n_i)`와 half-shift witness, `consume_event_union`이라는 조건부 same-state consumer를 유도·설계했다. 조건부 H1/He4,100 K,n_b=8750/47에서 correction은 HeI +C/n_b,HeIII -C/n_b, ionic charge -2C/n_b, chemical -(24.59+54.42)C eV/m³이다.

R10 theory closeout 및 C04 COMPLETE_FOR_SELECTED_STAGE를 읽었다. C03 실제 receipt가13/20이고 C04 완료 기록이 추가돼 수행/게시 source 단계는14/20으로 해석한다. frozen publication directory의 최신 dual backup receipt는C03이므로 이 read pass에서 백업14/20을 주장하지 않는다. C4 probe는PASS, measuredCPU0.114369 s/chargedCPU0.164369 s이며 scientific_status는null이다. 사전 C04 설명의 NOT_RUN 문구보다 실제 probe receipt가 우선한다. Primary/controls/independent/plot의 과학 PASS를 이 snapshot에서 확인한 것은 아니다.

실제 exclusive He event measure와 실제 C_cross, outside partner response, proton donor debit, actual EOS/T, full-source physical native25는null이다. 새 조건부 CR named consumer가 존재하지만 WU의 실제 HD reactive array나 실제 WU consumer binding 전달로 승격할 수 없다. 중앙28/88, delta0을 유지한다.

## WU 의존성 판정

이번 좁은 read pass에서 새 실제 HD reactive arrays0건, 새 실제 WU named-consumer binding0건을 관찰했다. CR 조건부 consumer 설계의 추가는 구분해 보존한다. 고정된 WU R7 source를 변경한 증거가 없으므로 현재 WU R10 실행 결과를 자동 무효화하지 않는다. 이는 모든 repo·대화·백업에 해당 입력이 없다는 전역 부재 주장이 아니다. REI central,HE AZIMUTH09,REC weighted bridge,Vigil production closure의 4 refs는 불변이며 최초 근거를 재사용한다.

## 근거와 보존

HEAD_GET_SNAPSHOT.json은7개 실제 GitHub GET 원응답을 보존한다. DIRECTORY_GET_EVIDENCE.json은 변경된 CR leaf/stages/publication의 세 실제 listing 응답이다. SOURCE_MANIFEST.json은14개 성공 source read와 BASS AGENTS.md의 단일404를 구분한다. 해당404는7개HEAD 확인의 오류0과 다른 계수다. Source14개 중11개는 실제 Git blob과 동일하고,3개 공개 receipt는 local/provider 경로를 제거한 공개 projection이다. 원격 Git blob·immutable URL·로컬 bytes/SHA256을 모두 명시했다. Private 서비스·대화·archive 내용을 새로 읽지 않았으며 외부 게시·과학 실행·리뷰 재귀를 하지 않았다.

## 재사용할 immutable 출처

- [bass FINAL_ROOT_ACK.json](https://github.com/cosmosapjw-quantum/bass/blob/f834101d3292f304681349db5d435c6f0c6b559e/research/bass_b3h_restart_cocycle_20261028/delivery/FINAL_ROOT_ACK.json)
- [rei_bianchi CONTINUATION_RECEIPT_20261028.json](https://github.com/cosmosapjw-quantum/rei_bianchi/blob/e77bc7ec48ae2aee8ded573e66ac0a1060017c54/research/rei_expanded_event_consumer/finite_thermal_endpoint_20261028/delivery/CONTINUATION_RECEIPT_20261028.json)
- [bass_cr CONTRACT.json](https://github.com/cosmosapjw-quantum/bass_cr/blob/e91a0d19b13a0b3254c194e7a4863b845c271874/research/cr_he_event_union_20261028/CONTRACT.json)
- [bass_cr C04.json](https://github.com/cosmosapjw-quantum/bass_cr/blob/e91a0d19b13a0b3254c194e7a4863b845c271874/research/cr_he_event_union_20261028/stages/C04.json)
- [bass_cr C03_RECEIPT.json](https://github.com/cosmosapjw-quantum/bass_cr/blob/e91a0d19b13a0b3254c194e7a4863b845c271874/research/cr_he_event_union_20261028/publication/C03_RECEIPT.json)
- [bass_cr R10_RESULT_KO.md](https://github.com/cosmosapjw-quantum/bass_cr/blob/e91a0d19b13a0b3254c194e7a4863b845c271874/research/cr_he_event_union_20261028/evidence/R10_RESULT_KO.md)
- [bass_cr RECEIPT.json](https://github.com/cosmosapjw-quantum/bass_cr/blob/e91a0d19b13a0b3254c194e7a4863b845c271874/research/cr_he_event_union_20261028/runs/probe_v1/RECEIPT.json)
