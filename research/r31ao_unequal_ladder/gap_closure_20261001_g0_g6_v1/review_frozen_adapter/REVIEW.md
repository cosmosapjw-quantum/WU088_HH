# Frozen input adapter 독립 artifact 검토

**B14 수정 후 synthetic adapter 검증을 수용한다.** 실제 Frozen107 bytes를
읽거나 decode하지 않았고 native compile도 하지 않았다. G2 decoder kernel은
재감사하지 않고 NPZ 경계, 코드 생성, C-order→assembly 연결부를 검토했다.
`independent_review_admitted=false`다.

## B14 — 자기 선언 record를 pinned loader로 승격하던 결함

초기 adapter SHA256는
`51efc4d02fe55a125aa7c282aa7f70f120dc084ca16e810447e575d88bf1275e`였다.
Toy NPZ를 SYNTHETIC_ONLY로 decode한 뒤 record의 scope를 FROZEN107_PINNED,
archive SHA를 공개 canonical pin으로 바꾸고 ordinary record digest를
다시 계산하면 `generate_cpp`가 `load_frozen107_rational_record`를 생성했다.
Toy donor nonzero count가 729이고 `input_byte_pin_verified=false`여도
허용됐다. `pin_scope_spoof_observed.json`이 이 관측을 보존한다.

자기 자신에 대한 digest는 record integrity일 뿐, 원본 archive에서
도출되었다는 증거가 아니다. 이 결함은 **중간 심각도의 provenance 승격
오류**로 분류했다. 과학 계산이 실제 수행되었거나 오염되었다는 뜻은 아니다.

작성자는 pinned code generation에 원본 archive bytes를 필수로 요구하고,
canonical archive SHA 및 member payload SHA를 검증하며 재decode한 전체
record와 supplied record가 같아야 하도록 수정했다. CLI는 이미 읽은 bytes를
전달한다. 수정 후 scope·archive SHA·pin flag를 모두 위조하고 digest까지
다시 계산한 같은 toy record는 (1) archive bytes가 없으면 거절되고,
(2) toy bytes를 주어도 canonical hash 불일치로 거절된다.

독립 재현 결과는 `pin_scope_spoof_after_fix.json`에 기록했다. 최종 adapter
SHA256는 `82e6e96157761be7e8423c7908c501bb66086b735374ce0679836ca1b69c7b48`다.
B14는 `RESOLVED_IMPLEMENTATION_VERIFIED`다. 실제 canonical payload의
성공 경로 실행은 이번 검토 범위에 포함되지 않았다.

## 남은 경계와 검증

작성자의 마지막 NUL filename 및 bounded CLI read 보강을 정적으로 읽은 뒤,
최종 adapter **16 tests PASS**를 독립 실행했다. 추가 toy tests는 다음을
확인했다.

- ZIP member 수를 유지한 duplicate/path traversal 사례를 거절한다.
  단순히 총 member 수가 다른 것만 검증한 것이 아니다.
- Symlink mode, aggregate size, compression ratio 및 실제 CRC corruption을
  각각 해당 경계에서 거절한다. 추출 경로를 filesystem에 쓰지 않는다.
- Record digest를 다시 계산한 뒤에도 코드 삽입 문자열, newline,
  noncanonical −0/01, non-dyadic 1/3, zero denominator 1/0을 거절한다.
- Fortran s_C/p_C를 logical C order로 변환한 뒤 `ia*12+j`로 생성한다.
  Donor C는 `(i*9+j)*9+k`로 생성하며 assembly.hpp의 배열 크기·주석과 맞는다.
- `z=3/4`를 명시적으로 생성한다. 저장된 수를 C++ float literal로 바꾸지
  않고 제한된 rational 문자열을 `Rational::set`에 전달한다.
- `scientific_authority=false`, `execution_authorized=false`를 유지한다.
  Byte pin 검증이 실행 승인이나 full scientific certificate를 뜻하지 않는다.

독립 검토 결과 파일은 `adapter_final.log`, `independent_final.log`다.
구현은 수정하지 않았으며 reviewer 디렉터리의 증거만 작성했다.
