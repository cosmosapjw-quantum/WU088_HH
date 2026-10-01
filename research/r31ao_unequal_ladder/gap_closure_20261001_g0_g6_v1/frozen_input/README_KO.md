# Exact Frozen107 input bridge

`adapter.py`는 bounded NPZ bytes를 기존 `exact_raw_decoder`로 decode하고, semantic C-index 순서의 정확한 rational string record와 `AssemblyInputs`를 채우는 결정적 C++ initializer를 만든다. 이번 검증에서는 생성한 toy NPZ만 사용했다. **실제 Frozen107 NPZ를 읽거나 값 decode·평가하지 않았다.**

`FROZEN107_HEADER_SPEC.json`은 canonical `EXACT_INPUT_AND_CALLBACK_BINDING.json`의 archive/member SHA, shape, dtype, Fortran flag만 추출한 독립 사용용 metadata다. 그 원문과 추출본의 SHA를 고정한다. actual input 값, archived exponent bits 또는 pref/v 상수를 복사하거나 새로 생성하지 않는다. 실제 실행은 별도 numerical authorization과 provenance admission을 요구한다. loader의 SHA 성공은 실행 승인이나 scientific certificate가 아니다.

검증은 `python -m unittest frozen_input.test_adapter -v`로 수행한다. fixture는 동일 shape를 가진 인공 정수 배열이며 실제 107-term donor polynomial을 모사하거나 대체하지 않는다. 테스트 fixture의 donor nonzero count는 729이고 `scope=SYNTHETIC_ONLY`, `scientific_authority=false`다. toy 결과는 native `stored_donor_terms`의 107-term admission용 입력이 아니다.

NPZ 입력 계약:

- 외부 expected archive SHA256가 반드시 필요하다. `FROZEN107_PINNED` scope는 canonical archive SHA와 각 member payload SHA까지 일치해야 한다.
- archive 1 MiB, 전체 해제량 256 KiB, member 64 KiB, 압축비 500, 정확히 11개 member 제한이다.
- canonical flat member names만 허용하며 duplicate, 경로 변형, missing/extra field, directory/symlink, encryption, 지원하지 않는 compression을 거절한다.
- NPY shape/Fortran flag와 `<f8` dtype가 metadata와 같아야 한다. NaN/Inf·잘린 payload·잘못된 header·비binary64는 기존 exact decoder에서 거절한다.
- s_C/p_C의 Fortran 저장순서는 decoder가 semantic C-order로 변환한다. 부호 있는 0은 수학적 rational `0`과 별도로 provenance에 남긴다.

native bridge mapping:

| Rational record | `AssemblyInputs` |
|---|---|
| exponents | exponents[12] |
| s_C, p_C | s_C[144], p_C[144]; index=primitive×12+orbital_column |
| C | donor_C[729]; index=(i×9+j)×9+k |
| phase_E | phase_E[49] |
| pref, v | exact Rational scalar |
| fixed geometry | z=`3/4` |

s_eps/p_eps/Q/parity는 원 record와 hash에 보존하지만 현재 O/G/D native target에 새 역할을 부여하지 않는다. Native C++ JSON parser를 만들지 않았다. `generate_cpp(record)`는 검증된 dyadic 문자열만 `.set("numerator/denominator")`에 넣으며, source injection이나 float/short decimal 변환을 허용하지 않는다. **Pinned scope의 code generation은 `source_archive_bytes`를 별도로 요구**하고, canonical archive/member 해시를 재검사한 exact decode 결과와 record 전체가 일치해야 한다. 자기기입 scope/해시/검증 flag나 다시 계산한 record digest만으로는 pinned initializer를 만들 수 없다. 생성된 header는 `assembly.hpp` include 경로를 지정한 native build에서 사용할 수 있다.

후속 승인 범위에서의 CLI 형식:

```bash
python -m frozen_input.adapter INPUT.npz --expected-sha256 SHA256 \
  --scope FROZEN107_PINNED --record-out NEW_RECORD.json --cpp-out NEW_INPUT.hpp
```

출력은 create-only다. 이 예시는 명령 형태만 제공하며 이번에 실행하지 않았다. 생성 C++는 actual input loader/runtime의 build·ABI 검증을 대신하지 않는다. 이번 bounded 단계는 Python synthetic implementation verification이고, 실제 input binding과 native initializer compile/runtime verification은 남아 있다.
