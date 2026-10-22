# 게시 및 최종 전달 연결 — PHYS80

## 확인된 S0 science 게시

Repository: https://github.com/cosmosapjw-quantum/WU088_HH

Draft PR136: https://github.com/cosmosapjw-quantum/WU088_HH/pull/136

Branch: research/hh-phys80-sandbox-reduction-20261022

실제 부모 PR134 HEAD: 3304d16db1dc9bf868c185a8eeb6cc9dbc270e50.
Science commit: fd18c59796175191bdd5f9b7ab2981d5e92836fd.
Science root tree: 1477d47594cc48864f89a4a0acefbacc22e8c487.
Science unit tree: 77a680521b3d5b1d6ca687cecda0103270af1982.

135개 unit 파일의 원격 Git blob SHA1와 size를 로컬 bytes와 대조했다.
부모와의 비교는 추가135, 수정0, 삭제0이며 기존 역사 경로는 그대로다.
정확한 조회와 checkpoint 응답은 [게시 영수증](delivery/POST_PUBLICATION_RECEIPT.json)에 있다.

## Checkpoint와 최종본의 구별

S0 checkpoint: PHYS80_S0_CHECKPOINT_20261022_fd18c5979617.zip.
1,673,833 bytes; SHA256 11edfa379522ab79e6044307055d207014585b39219cb2abe0b95adccd824d0c.
Drive ID: 1uXuMBP1IrEpUczqY3yt6ayeOhON59r37 (upload ACK).
Dropbox ID: id:BSpOijBcT10AAAAAAD_i8w (upload/size ACK).
이 checkpoint는 원격 restore를 수행한 최종 ZIP으로 부르지 않는다.

최종 ZIP은 S1의 이 unit 파일 snapshot과 별도 post-publication receipt를 포함한다.
전체 repository/history ZIP이 아니다. 최종 HEAD/ZIP의 자신의 SHA를 그 내부에
넣으려는 자기참조를 피하기 위해 외부 PHYS80_FINAL_DELIVERY_20261022.json이
실제 S1 HEAD/root tree, ZIP SHA/byte 수, provider IDs, 각 provider의 전체 bytes,
ZIP CRC 및 모든 payload SHA 검증 결과를 연결한다. JSON 자신의 IDs/SHA는
최종 Draft PR 본문에 기록한다. 이 내부 snapshot 이후의 실제 완료 상태는
반드시 외부 JSON과 actual PR/ref를 조회해서 확인한다.

## Metadata-only 후속 단계

S1은 root 보고서·handoff·DAG/ledger와 delivery/만 갱신한다.
SCIENTIFIC_PAYLOAD_MANIFEST.json의 과학124개 entries SHA256은
09eb0ffffd9d22e5dc5c9f681c7226507e99027f450da00421f2751afde81a76이다.
source/result/theory/verification/figures/inventory bytes는 S0 그대로 유지한다.
늦은 HH135/REI222의 D event-energy component는 별도 전달 receipt에서
재사용하고, PHYS80 계산을 다시 실행하거나 새 rate로 결합하지 않는다.

source 또는 완료 계산을 재실행해 저장을 검증하지 않는다.
HH_R10=OFF. Production admission NOT_ISSUED. Draft 유지; main merge 없음.
