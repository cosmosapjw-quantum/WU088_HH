# PHYS14 원자료 회수 결과

## 완료한 회수

PHYS11 `SOURCE_TO_CARRY_MAP_KO.md`가 지목한 Full·first_half의 `prebe_words.bin` 및 `prebe_input_words.bin` 네 파일을 실제 바이트로 회수했다. NCP07 원 소스와 COMMON seed, ray geometry trace, gas/source export도 같은 원 ZIP 안에 있으며 아래에 해제했다.

`/workspace/scratch/b826cbaab54f/phys14_intake/ncp07/HH_PHYS07_NCP_LOCAL_20261011_v1`

원 ZIP은 Drive ID `1NsBdq3WAvNWVOmS7Yfpcib99nDKVrZ6H`에서 실제 materialize했다. 크기는 5,644,521 bytes, SHA256은 `4ea6b7dbbc714493ac85f944a65a353a1ee75abf5742c3e7ce65a7df56cc3465`다. 회수한 실제 bytes의 Dropbox block hash `ce4106a1b9d1638550b72ae495f5d649293d275467eb3f685837ba05c2514b88`는 Dropbox peer `id:BSpOijBcT10AAAAAAD4FPg`의 현재 metadata/download-link가 반환한 크기·block hash와 일치한다. 실제 다운로드는 Drive에서 한 번 수행했다. Dropbox peer까지 별도로 다시 다운로드했다고 기록하지 않는다.

추가 요청한 PHYS11 최종 carry 결과·요약·독립 판정도 원 ZIP에서 실제 회수했다.

`/workspace/scratch/b826cbaab54f/phys14_intake/phys11/HH_PHYS11_20261011_v1`

이 ZIP의 Drive ID는 `1ZaycDIwCHO125rbcAWa_qctaVAmy_V3F`, 크기는 2,563,320 bytes, SHA256은 `946a93390a91c4dcfd5164887121954f77be74a01d8c93576f859f38dcaab90b`이며 과거 보고서의 원 archive identity와 일치한다. 최종 `results/carry_v2/CARRY_RESULTS.json`, `SUMMARY.json`, `review/DECISION.json`의 Git blob을 실제 bytes로 계산해 pinned Git tree와 대조했다. 세 파일 모두 일치했다. 최종 판정은 `PROMOTE_SCOPED`다.

## 네 바이너리의 identity

아래 경로는 NCP07 package root 기준이다. 모두 원 MANIFEST와 PHYS11 공개 source map의 크기·SHA256에 일치했다.

| 상대 경로 | bytes | SHA256 |
|---|---:|---|
| `results/full/prebe_words.bin` | 4,123,688 | `44519317341ef588d009feaec89ddf7278d3163d1519bb6c1683d376fdb82f78` |
| `results/first_half/prebe_words.bin` | 4,123,688 | `10f97267c6348c3735102c9c76a8c43e342fdeef7bcffc63ff818764a6bad1cc` |
| `results/full/prebe_input_words.bin` | 4,090,360 | `cd54a183bba2e7c2a15f7fa83f5734f6818232d20b76e395824a3fdb97c4a71c` |
| `results/first_half/prebe_input_words.bin` | 4,090,360 | `c9be883901fb0f21247146d65adf83562cf643b63c5883f9051946e0e1b5e78b` |

원 `candidate/src/phys04_mixed.rs`, `phys04_transport.rs`, `paired_runtime.rs`, `src/family.rs`, `src/sourcebox.rs`의 SHA256도 PHYS11 §7의 source identity와 각각 일치한다. 필요한 35개 파일, 합계 32,873,638 bytes의 manifest 대조를 완료했다. 근거는 `SOURCE_IDENTITY.json`, `PHYS11_IDENTITY_BRIDGE.json`이다.

## 배열 배치와 의미

`prebe_input_words.bin`은 little-endian u64 총 511,295 words다. 앞 5 words는 Hubble triplet 3개, 입력 time, dt이며, 이어 gas4·photons4224·guardN128·guardU128·birth parameter1의 4,485 Jets가 들어간다. 각 Jet는 value, gradient[7], Hessian[7][7]의 57 intervals이고 각 interval의 lo/hi를 합해 114 words다.

`prebe_words.bin`은 총 515,461 words다. 앞 6 words는 종료 time, dt, nH, fHe, Hmean, guard export count다. 이어 gas4·photons4224·guardN128·guardU128·groups33·sourceN/U2의 4,519 Jets, energy33 words, source weights128×2 words가 들어간다. 모든 interval이 유한하고 lo≤hi인 것을 확인했다. signed derivative의 subnormal tail과 zero bits를 수정하지 않았다.

바이너리의 gas는 `COMMON_INPUT_SCOPE.json::old_gas`, group/sourceN/sourceU/weights는 `PREBE.json`, energy와 nH/fHe/Hmean header는 `SOURCE_BOX.json`의 captured bits와 일치했다. 원 `prebe_source_bytes.bin`은 `paired_runtime.rs + phys04_transport.rs + interval_ad.rs + interval_math.rs`의 순서 있는 byte 연결과 일치했다. `BINARY_LAYOUT_VERIFICATION.json`은 모든 word/byte offset과 이 비교 결과를 제공한다.

이 payload의 시간적 의미는 **기존 COMMON → 첫 transport와 birth를 거친 PreBE**다. Full은 dt=1.25e9 s, first_half는 dt=6.25e8 s이고 두 input time은 모두 1.6e11 s다. 실제 post-BE gas·흡수 광자 응답은 PHYS09/PHYS11의 별도 결과에 결합해야 한다. 회수한 원 package는 carried second-half의 새로운 source-box/root 결과를 포함하지 않는다.

## PHYS11 재사용 파일

| PHYS11 상대 경로 | bytes | SHA256 | Git blob |
|---|---:|---|---|
| `results/carry_v2/CARRY_RESULTS.json` | 6,463,565 | `5e3dc0b589c5e86672664ea851e7986708e10ed73f6a3db8332b9c8084a897ca` | `a63e95b6762d21f8d5ca722532266e935bc34299` |
| `results/carry_v2/SUMMARY.json` | 3,626 | `9570ef7aadfe9a2777e79b5f1f9f3fda579db6e828a85de97a83a873ecae1522` | `bdfe8a4eb4e706fa10217cbd935ca2301674b008` |
| `review/DECISION.json` | 25,194 | `a6f3d08d099444717cbe1b32703e24b1c6f6d4ec6df4fe8b4748a4e2b2ae6d91` | `18372f3f55ce00fd7a4b48516f878da3676d9b25` |

이 결과는 Full·first_half 각각 33 photon groups의 value/U/V/W와 future-ledger carry를 제공한다. 원 독립 판정의 범위는 source-aligned 첫 단계와 상속된 fixed-coefficient source/C² premises다. 전체 PHYS11 source/theory와 원 review가 함께 materialize되었으므로 필요한 정의를 해당 원문으로 읽을 수 있다.

## 등방 축약을 위한 원문 관찰

원 Hubble triplet의 세 bits는 동일하다. `paired_runtime.rs::g_point/g_box`는 qhat과 Hubble/time으로 energy geometry를 계산하고 `phys04_prepare_family`는 각 ray의 `g_box(t+d)/g_box(t)`를 저장한다. 실수 geometry 식에서 등방 h의 공통 ratio를 유도할 수 있는 원 graph가 확보됐다.

저장된 interval ratio endpoint는 Full에서 10종, first_half에서 7종이다. 따라서 공통 ratio를 사용할 후속 유도는 그 값이 모든 기존 ray interval에 속한다는 포함 근거와 선택한 geometric subfamily를 명시해야 한다. 원 data를 평균 ratio나 한 ray의 값으로 덮어쓰지 않았다. `geometry_trace.txt`와 원 ray arrays를 모두 보존했다.

## 최신성 및 남은 실제 작업

이번 intake의 최신 HH Git 조사는 PR 목록 한 번으로 제한했다. 최상위 최신 결과는 PR48, head `36f9669b117fe7537b3fa59d4cc80f5e12154be5`, updated `2026-10-12T12:02:39Z`, open, mergeable=true다. 그 다음은 PR47·46·45다. `LATEST_HH_PRS.json`에 실제 응답을 보존했다.

이 intake에서 **ray·guard 바이트의 접근 결손은 해소**됐다. 후속 owner는 이 원 자료와 기존 post-BE 응답을 연결해 다음 transport/source의 입력 family를 구성할 수 있다. 실제 다음 implicit 단계의 source/root 포함은 그 후속 연구가 산출할 대상이다. 자료 회수 결과 자체의 지위는 implementation-verified byte/layout provenance다.

이 실행자의 scientific source callback, inverse/root, native, 과거 scientific suite 실행은 모두 0회다. 원 실행의 FIRST_CLAIM와 소스·허용오차·계약·실패 기록을 수정하지 않았다. 바이트 회수 스크립트의 경로 선택 오류와 작은 text-copy의 newline 보정은 `INTAKE_ENVIRONMENT_EVENTS.json`에 별도로 보존했다.

## 적용한 운영 범위

호스트가 지정한 GPT-6 Astra Pro에 따라 physmath research/coding harness v4.0.0의 core와 현재 PHYS13 handoff를 읽었다. 이 하위작업의 범위는 원자료 회수·해시/배치 검증이며 새 과학 후보 생성·판정 또는 외부 mutation은 하지 않았다. 기존 승인된 read/download 경로만 사용했다.
