# G4 고정판 callback 구현 초안

`callback.cpp`는 FLINT 3.4.0의 실제 acb/arb API를 호출하는 C++17 초안이다. 현재 native 컴파일·링크·실행은 하지 않았다. 따라서 Python의 exact/static test 통과를 ball backend 검증으로 해석하지 않는다. 실제 HH 자료를 읽거나 callback, 적분, endpoint 상수를 평가한 횟수는 0이다.

구현 범위는 k=0..8, r=0,1,2의 M_k 도함수, signed unweighted U_i(t), s/px/pz spatial primitive의 O/G1/G2, 그리고 107개 이하 항의 정확한 계수에 대한 유한합이다. `polynomial_field`의 출력은 `sum C_ijk U_i U_j I_field`이다. 후속 `assembly.cpp`는 별도 translation unit에서 Gaussian orbital normalization, 12×12 orbital contraction, reflection/parity, phase, D_col/D_row 조립을 구현한다. 실제 decoder→native 값 연결과 integration→assembly 연결 검증은 남아 있다. `Slice::outer_box`는 전체 외부 복소수 box다. slice는 내부 integrand만 계산하며, 내부 적분의 uniform enclosure나 중첩 적분을 구현했다고 주장하지 않는다.

반정수 파라미터는 정수와 정확한 2의 거듭제곱으로, 입력 계수·중심·wave number는 `fmpq`로 전달한다. binary64에서 부정확한 decimal 변환을 거치지 말고 decoder의 정확한 numerator/denominator를 사용해야 한다. 저장된 C/pref/v/phase_E 및 normalization authority를 재생성하면 안 된다. Complex box는 acb 입력으로 전달하며 `Re(box)-margin>0`을 arb로 증명한다. Re(t), Re(u), Re(a+t), Re(b+u), Re(sigma) 중 하나라도 엄격한 양의 여유를 증명하지 못하면 indeterminate를 반환한다. 따라서 domain 실패가 곧 수학적 함수의 특이점 증명은 아니다.

branch는 principal power다. 1F1은 `regularized=0`, s는 bilinear displacement square다. s=0으로 나누는 구현은 없고, 영 Pochhammer 계수는 정확한 0으로 단락한다. pz G1의 displacement polynomial 도함수와 G2의 반대 부호를 포함한다. callback 내부 conjugation은 없다. D_row conjugation은 실수축 적분의 enclosure 뒤에서 수행해야 한다.

현재 실행한 검사:

```bash
python -m unittest -v test_contract
python -m unittest -v test_assembly
```

이 suite는 stdlib Fraction의 terminating polynomial과 독립 Cartesian Gaussian moment 전개를 비교한다. domain boundary·잘못된 차수·static API usage도 검사한다. `TDD_RED.txt`는 구현 전 모듈 부재의 관측 결과이고 `TDD_GREEN.txt`는 구현 후 결과다. `API_PIN_CHECK.json`은 실제 사용한 함수 이름이 고정판 header에 존재함을 확인한 자료다. 이름 검사로 C++ compile/type/ABI 검증까지 주장하지 않는다.

후속 host에서만 수행할 검사:

```bash
python -m unittest -v test_high_precision_optional
```

이는 mpmath를 사용하는 synthetic point cross-check이며 ball proof가 아니다. 현재 환경에 mpmath가 없어 3개 항목은 SKIPPED이며 통과로 세지 않는다. `native_synthetic.cpp`는 FLINT의 terminating even cases, low-k 도함수, 복소수 box containment, branch/domain 거절, pz delta 항, callback order와 작업량 cap, normalization 및 post-integral assembly를 확인하도록 작성했다. 아직 컴파일하거나 실행하지 않았다.

검증된 FLINT/GMP/MPFR 설치가 준비된 host에서 `build_host.sh`를 쓸 수 있다. script는 dependency를 설치·컴파일하지 않고 callback synthetic executable만 만든다. 새 출력 경로와 backend build provenance를 반드시 지정한다. 설치된 library source-to-binary provenance는 별도로 검증된 빌드 기록을 요구한다. `verify_build_inputs.py`는 제공된 source/archive와 binary SHA를 확인하지만 그 빌드 주장을 독립적으로 증명하지는 않는다. build 완료 뒤 실제 linked library 경로/해시가 기록과 일치하는지 확인하고 synthetic executable을 실행한다.

`Contract`의 기본 precision/margin/caps는 synthetic 예시다. 실제 HH workload를 위한 endpoint·precision·work·memory·wall caps 또는 numerical authorization을 제공하지 않는다. FLINT API의 `order=1`은 함수값과 holomorphy 요청이며 radial derivative r=1이 아니다. 예상 밖 order, precision 변경, 불명확한 domain, 비유한 ball, budget 초과는 모두 fail closed다. 함수 return integer만으로 integrator failure를 전달하지 않고 결과를 indeterminate로 설정한다. 각 thread는 별도 Contract를 소유해야 한다.

추가 static review에서 order>1 거절의 모든 Taylor 출력 slot을 indeterminate로 초기화하도록 보완했고, 대응 native fixture도 실제 2-slot buffer로 수정했다. rational 입력은 텍스트 8192자, numerator/denominator 각각 16384bit, 양의 canonical denominator를 요구한다. 잘못된 문자열을 거절해도 기존 Rational 값이 보존되도록 임시 parse 후 교체한다. callback과 assembly의 hard precision 상한은 4096bit다. 이 입력 제한은 외부 wall/memory 제한이나 native 실행 검증을 대신하지 않는다.

현재 상태: `IMPLEMENTATION_DRAFT_BACKEND_RUNTIME_UNVERIFIED`. compiler/ABI/실제 binary hashes, odd-degree 검산, outward backend 실행 검증, exact-input loader 연결, assembly native 실행 검증, uniform interior integration이 남아 있다. [ASSEMBLY_INTERFACE.md](ASSEMBLY_INTERFACE.md)에 정확한 입력 순서, normalization 소유 단계, 실제 적분 ball 전제와 출력 layout을 정의했다. `certified_epsilon=null`, `certified_eta=null`, `rigorous=false`를 유지한다.
