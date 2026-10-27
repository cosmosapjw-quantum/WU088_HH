# R4 독립 실행 전 구현 검토

판정은 **PASS_SCOPED_PREEXECUTION_AFTER_TARGETED_STATIC_REPAIRS**입니다. 첫 과학 실행 전에 발견한 P01·P02·P03을 교정했고, 남은 blocking finding은 없습니다. 이 판정은 실제 수치 통과나 물리적 rate/Q/consumer 승인이 아닙니다.

## 최종 검토 입력

| 파일 | SHA256 |
|---|---|
| build_molecular.py | 5ba9d17f1a6c68f8fec5ac50d256448a2c502cef9114ed1f1dcb0bf285f50ff0 |
| verification/run_bounded.py | b362521e75319816498cc0e3dd9382891bfb771cf988a963dadad83d0e616bdc |
| molecular_operator.py | c11bd7240039050e0a817d698e9a82517770081e56828c7b48b4492ec98ee4c5 |
| sources/MOLECULAR_SOURCE_PACKET.json | 40e2fbd73d451c0c8116b4ca9bd4db4d2e43e4cdf8967988a2fea551f99ce35e |
| theory/CLAIMS.json | e04353625155ca0f5fab09ef638d63ae96d3ebc84f6ede3b4a2326d3cca634f1 |
| theory/STATE_LIFT_THEORY_KO.md | eb62a104974a278211c77fb5037bffd00ef4f157acd6911b6e2c46f0bd3fef68 |

최신 로컬 HEAD d87207367eda15990c34aa2db4eff69256953771, R4 AGENTS, S03 preflight와 S03 이중 업로드 영수증을 읽었습니다. S03 ZIP은 457,609 bytes, SHA256 7a5b14a1285e9210c2a3a2f8707244faae25d2c200c85c2303ba090251453fe1입니다. 이 reviewer가 클라우드 다운로드를 반복하지 않았으며, 새 노드의 실제 게시 직전 갱신은 root가 기록합니다.

## 교정된 세 발견

**P01 — 부분 출력 뒤의 불필요한 재계산.** 최초 builder는 compiled.json만 검사했습니다. species/events만 남았다면 여섯 compiler 호출과 29 fit 계산을 반복한 뒤 exclusive write에서 실패할 수 있었습니다. 수정본은 registry 아래 어떤 파일이든 있으면 source load 및 adapter/compiler import 전에 멈춥니다. 완전/부분 결과를 그대로 보존하며, 일곱 산출물을 모두 쓴 뒤 각 SHA256을 묶은 COMPLETE.json을 마지막에 씁니다. 실제 완료는 marker 존재만으로 인정하지 않고 유효한 JSON·member hash·exit status를 함께 읽습니다.

**P02 — 실패한 launch의 영수증 누락.** 최초 runner는 빈 command 검증을 attempt 디렉터리 생성 뒤에 했고 Popen/preexec 실패에 대한 receipt 경로가 없었습니다. 수정본은 입력을 먼저 검증하며, OSError/SubprocessError와 timeout을 기록하고 running child를 finally에서 수거합니다. 실제 RUSAGE_CHILDREN 차이와 wall, launch_error, 별도 coordinator 실행 구간 CPU를 기록합니다. 이는 preparation·request hash·receipt tail·외부 tool의 전체 비용 측정이 아닙니다. 미측정 비용을 0으로 해석하지 않습니다.

**P03 — primary 비방사성과 후속 cascade의 혼동.** 중간 metadata는 primary photon이 없는 exchange에 total cascade yield 0을 배정했습니다. 미해결 H2/HD 제품 상태는 후속 cascade 총수를 제공하지 않으므로, 최종본은 여섯 variant 모두 total_cascade_photon_yield=null로 둡니다. Primary emission은 RA 1, 나머지 즉시 사건 0이고 escaped count/energy는 null입니다.

세 발견의 최초·중간·최종 입력 해시와 정적 교정 근거는 JSON에 보존했습니다. 실제 child 실패나 계산을 수행한 뒤 결과를 수정한 과정은 아닙니다. Root가 작성한 최소 partial-output 및 failed-launch control의 실제 결과는 후속 receipt로 확인합니다.

Root가 마지막으로 parent_catalog를 ../provider_registry_exfor_target6_20261027/registry/provider_catalog.json으로 쓰고 path_base를 R4 leaf root로 명시한 locator 교정도 확인했습니다. 실제 읽는 원본과 계산식은 바뀌지 않았습니다. Photon 교정 직후의 0429c1a4…와 최종 5ba9d17f…를 JSON에 구분했습니다.

## 물리·수학 범위

Packet의 exact SHA와 adapter·compiler의 고정 SHA를 확인합니다. 변경 부분은 **새 여섯 event column과 27+2 source formula sample**뿐입니다. 이전 149열과 249검사를 계산하지 않습니다.

Bennett/Bovino의 LiH 상태, Honvault의 para-H2(v0,j0)와 미해결 HD 제품, GL2022의 rotational thermal HD 및 spin-weighted H2 제품은 서로 다른 identity입니다. H1/D2/Li7 및 nuclear ground는 명시적인 정수 모델 convention이며, source의 미해결 isotope/state 자격을 대신하지 않습니다. 이 14개 identity의 동시 진화는 승인하지 않습니다.

TIQM/SQM은 같은 상태·좌우·process·branch를 가져 provider ID와 무관한 동일 ownership group이 됩니다. Ortho/para 제품은 구분하고 spin 합산 정규화는 여전히 unbound입니다. Coarse reverse 열이 있다고 detailed balance를 승인하지 않습니다.

RA의 legacy gamma:escaping은 외부 입자 bookkeeping 표지라는 qualifier를 붙였습니다. 실제 escape fraction이나 radiation transport를 공급하지 않습니다. 기존 adapter는 PROVIDER_SOURCE_ONLY_NOT_EVENT_ENERGY를 전달하고 energy None 및 UNQUALIFIED:ENERGY를 검사합니다. 출력에도 energy:null을 보존합니다. Bovino의 2.258 eV는 미승인 source estimate로 남으며 epsilon·heat·nuclear Q로 들어가지 않습니다.

13개 이론 claim과 구현의 관계를 JSON에 각각 기록했습니다. 일반 선형 P의 factorization 및 formation branch total 정리는 이론 범위이며, 코드가 arbitrary-P API나 실제 branch vector를 제공한다고 주장하지 않습니다. 네 rational 예제는 실제 측정 상태율이 아닌 구성된 대수 예제입니다. 원표·식 잔차·물리적 불확실성도 구분합니다.

## 자원과 후속 검사

승인된 작업은 single-process 표준 라이브러리 연산입니다. Child는 30 CPU s, 120 wall s, 512 MiB로 제한하며 단일 worker/thread 계약을 유지합니다. 이전 PHYS91 잔여 0과 historical global unknown은 바꾸지 않습니다.

실제 primary 산출물이 나온 뒤 기존 DESIGN_REVIEW의 독립 계획에 따라 확인합니다. 독립 Decimal80 식은 정확히 29개 노드에서 저장된 binary64 결과와 상대차 2e-14 기준으로 비교합니다. 추가로 여섯 새 ledger, source77 cells, ownership, radiation/energy qualifier, 일곱 member hash와 실제 runner 영수증을 확인합니다. 이미 통과한 root의 운영 control은 재사용하며, 새로운 구체적 위험이 없으면 반복하지 않습니다.

이번 reviewer의 **생산 import 0, compiler 0, fit 평가 0, 수치 검사 0, 과거 과학 재실행 0, 원격 수정 0**입니다. 실제 수치 통과, 물리 rate/Q, 상태 lift의 실제 소비자 결속, activation 및 L4는 아직 승인하지 않았습니다.
