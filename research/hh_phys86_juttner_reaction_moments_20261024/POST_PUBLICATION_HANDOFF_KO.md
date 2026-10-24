# 게시 이후 상태를 읽는 순서

## 서로 다른 identity

- Parent PHYS85 final: 696eca5cf9f1fcbf722370833535f4144af0a54a.
- PHYS86 실행 source S1: 280ef5094dd56b76ce4f5dc8f8aad7bc36172728, tree435ef54285fe1a2690cc75a9791e77e553cbe4ea.
- Scientific identity: 270d59879327809203beb5f272527724ba85ceba7b3a54989b4417d02219eaa7.
- Evidence identity: 90a2ca12e69fa11e13acb83e78093b35b3c51a38533b3866253ceb1568f02cbc.
- 최종 문서 containing HEAD/tree, ZIP bytes/SHA/IDs와 actual provider restore는 외부 PHYS86_FINAL_DELIVERY_20261024.json 및 PR143 최종 본문을 읽는다.

Git commit이 자기 SHA를 파일에 재귀적으로 포함할 수 없으므로 실행 source와 최종 containing commit을 분리한다. 외부 final JSON 역시 자기 자신의 미래 upload ACK/SHA를 담지 않고, 별도 실제 raw readback receipt와 PR 본문에서 결속한다.

## 복원과 과학 재실행의 구별

Stage S0/S1/S2 upload ACK는 provider가 파일을 받았다는 상태다. Whole ZIP raw GET, CRC, payload SHA, native Git blobs, 실제 extraction/rehash와 같지 않다. 최종 양쪽 복원은 두 provider의 서로 다른 실제 다운로드에서 얻은 파일로 검증해야 한다. delivery/TRANSPORT_AMENDMENT.json의 Drive byte-parts 경로를 쓴 경우 각 part의 full GET/SHA/길이와 순서를 먼저 확인하고 원본 ZIP으로 재조립한 뒤 전체 검증한다. 이것을 단일 ZIP-object GET으로 표시하지 않는다. Parent PHYS85 ZIP/JSON은 전체 원본 bytes를 dependency로 보존하며, 이미 검증된 역사적 nested restore나 완료 science를 새로 실행하지 않는다.

S0 Drive first call은 root가1206s stalled await를 중단한 뒤 UNKNOWN_NO_ACK로 남았다. Tool의 “aborted by user”는 실제 사용자 취소나 원격 취소의 증거가 아니다. Exact filename/folder 조회0도 원격 실패를 증명하지 않는다. 이후 actual provider ACK와 restore가 없다면 dual backup 완료로 표시하지 말고 미완료 항목을 계속 처리한다. 다른 owner의 Drive UNKNOWN을 WU backup 완료로 대체하지 않는다.

## 과학 판정은 이미 별도로 닫힘

두 실제 reference에서1017+82 assertions PASS, fresh actual-raw C9 PASS_SCOPED다. 누적calls4, 현재추가0. Parent PHYS85 실패2회/oldcap0은 변하지 않는다. 완료된 PHYS86 source/raw identity는 전달 작업을 마무리하기 위해 다시 계산할 이유가 없다. 원문 경고는 보존하며 general production stability는 미채택이다.

DAG에서 nuclear parent는PARTIAL이며 physical finite-T event supplier와 fast stopping은OPEN이다. HE-Li CX, empirical D PI/RR, Li 실험 불확실성·inner-shell, recombination-to-z20 initial-charge, full spectral/geometry coupling도OPEN이다. 다음 노드 전에 실제 최신 owner/refs/AGENTS/backup delta를 확인하되 이미 완료된 근거와 누적 예산을 재사용한다.

HH_R10=OFF. Production admission NOT_ISSUED.
