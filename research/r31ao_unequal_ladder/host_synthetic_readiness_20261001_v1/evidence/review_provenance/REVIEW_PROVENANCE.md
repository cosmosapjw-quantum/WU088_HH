# Provenance gate 제한 검토

범위는 `TASK_CONTRACT.json`, `provenance_gate.py`, `test_provenance_gate.py`다.
Native build, scientific data 및 이전 이론·코드는 검토하거나 실행하지 않았다.
`independent_review_admitted=false`를 유지한다.

## PROV-R01 — P1, 필수 byte identity의 fail-open

`file_identity`는 기본 `expected=None`을 hash 수집만 하는 호출로 해석한다.
그러나 `verify_backend`는 caller record의 compiler, library binary, stage-log
SHA256을 그대로 이 매개변수로 전달한다. 따라서 record에 명시적으로 `null`을
넣으면 필수 expected identity가 없는 상태에서 byte verification을 건너뛴다.

Compiler SHA, FLINT binary SHA, configure-log SHA 및 install-log SHA를 각각
null로 만들고 해당 파일의 bytes를 변경하는 합성 fixture 4건 모두
`BYTE_CHAIN_VERIFIED`를 반환했다. 최초 재현 동안 source SHA256은
`c2f689c7071f3c2c7d39d8d0b45367dfdf1e4a64ba2e50fe64638fd67c324dbd`로
변하지 않았다. 원본 archive pin 대신 작은 fixture pin table을 사용하는 기존
테스트 helper를 사용했으며, 실제 library build를 가장하지 않았다.

이는 완전한 record를 위조하면 실행을 독립 증명할 수 없다는 일반적 한계와
다르다. **필수 identity가 빠진 record 자체가 승인되는 문제**다. 최소 수정은
compiler/binary/log SHA256이 필수 64자리 hex 문자열인지 먼저 검사하고,
identity 수집을 위한 expected 인수 생략과 명시적 null을 구분하는 것이다.
Missing/null/malformed identity 회귀 테스트를 추가하면 된다.

`NULL_IDENTITY_REPRODUCTION.json`에 최초 관측을 보존했고,
`null_identity_probe.py`가 같은 네 건의 독립 재현 코드다.

## 그 밖의 대상 경계

선택한 기존 테스트 6개는 종료 코드 0으로 통과했다. 고정 archive SHA256과
정확한 길이 검사가 존재한다. Library binary의 canonical path가 sidecar prefix를
벗어나는 symlink는 거절한다. `ldd`에서 필수 backend path 교체, missing/duplicate
dependency 및 미검토 추가 dependency를 거절하며, 실제 check-time 파일 hash를
반환한다. 관련 기록은 `TARGETED_CHECKS.log`다.

Verification block은 독립 실행 증명, historical ABI admission 및 scientific
promotion을 명시적으로 부인한다. 이 claim ceiling은 적절하다. `verify_linkage`는
현재 byte hash를 반환하므로, 앞선 build record와의 cross-stage 연결과 즉시 실행
조건은 caller의 통합 책임이다. Runner는 이번 제한 검토 대상이 아니다.
