# C1 이후 C2 실행 인계

현재 node는 C1_REPRESENTED_GAPS_VERIFIED__CONTINUOUS_TARGET_UNRESOLVED. RESULT.json → SOURCE_LOCK.json → SCOPE.json → REPORT_KO.md → authority/CONVERGENCE_PLAN.json을 읽는다. 전체 입력/코드/증거는 delivery ZIP에 있다. Git에 일부 파일만 게시되면 DELIVERY_INDEX의 SHA-bound ZIP을 먼저 복원한다.

재현: 새 디렉터리에서 `python3 -B -m unittest discover -s tests -v`. actual 결과의 재후처리가 필요한 경우만 `python3 -B exact_gap_binding.py --output <새 디렉터리>`를 실행한다. 같은 디렉터리 덮어쓰기 금지. `--require-continuous`는 epsilon 부재로 exit3를 반환해야 한다. pipeline은 stdlib-only; decoder oracle regression에만 NumPy 필요. 원 두 vendor파일을 수정하지 않는다.

C1는 31개 source pins, raw C/R exact JSON 재사용, 예측9 NPY integer decode, 독립 저장 K, exact norms9/gaps4, strict PRIMARY/SECONDARY와 tolerance bits를 연결했다. archived historical scalar replay의 fenv는 미검증이지만 해당 fixed scalars의 support는 directed bracket으로 all-mode robust다. 사후 eta를 direct route에 중복 합산하지 않는다. 실제 source epsilon/continuous cert는 없음. conditional epsilon threshold는 실행오차 허용치가 아님.

다음 canonical: C2_PORTABLE_CERTIFICATE_JOIN_AND_RETURN_INGEST.
1. 기존 primitive join/endpoint/composition/coverage 원 API를 실제로 읽는다. duplication solver 금지.
2. same-source/window/primitive 완전 coverage만 endpoint를 정확히1회 결합. partial20/289 및 missing269로 whole-domain을 만들지 못하게 한다.
3. all2592 registry와 source-prescribed normalization/sign/order/row conjugation을 보존하는 streaming contract를 연결한다. 완료되지 않은 primitive는0으로 대체하지 않는다.
4. source-bound RETURN ingestion과 claim gate를 구현하고 synthetic/기존raw로 bounded tests를 실행한다. actual epsilon이 없으면 C1 final UNRESOLVED_INPUTS를 유지한다.
5. C0 application authority/B22/physical full49/BR01/BR02/독립 review는 별도. 신규6셀 pilot/대형 HH 적분/host optimization은 NCP 대기열에 둔다.

동일 연구branch nonforce additive publication, 기존 Drive/Dropbox create-only 이중백업. 실제 remote HEAD successor를 먼저 읽고 old directory 수정/새 branch/main merge 금지. R1 ACK+identity와 restore는 구분한다. 기존 C0 DB를 수정하지 않고 additive copy에 새 테이블을 만든다.
