# PHYS03 재현

Python 3.12.14, python-flint 0.8.0/FLINT 3.3.1, Sympy 1.14.0, mpmath 1.3.0에서 새 범위의 검산을 수행했다. Smooth polynomial checker와 source identity 검사는 표준 Python만 사용한다. 나머지 두 검사는 requirements.txt의 dependency를 쓴다.

## 봉인된 파일 확인

패킷 root에서 다음 명령은 manifest의 모든 파일 길이와 SHA-256만 확인한다.

    python3 -B reproduce.py --verify-only

MANIFEST.json은 자기 자신을 제외한다. ZIP 자체의 SHA-256과 원격 publication/backup receipt는 archive 바깥의 detached delivery receipt에 있다. 서로를 자기 참조하는 hash로 만들지 않는다.

## 새 범위만 재현

이미 존재하지 않는 출력 directory를 지정한다.

    python3 -B reproduce.py --output /absolute/path/to/new_PHYS03_check

이 명령은 source identity, exact nonautonomous/formal BE coefficient, closed-form hybrid event derivative, actual-leaf remap/energy arithmetic만 실행한다. 기존 evidence는 덮어쓰지 않는다. 첫 실패의 stderr와 return code는 새 directory에 보존하고 중단한다. 실제 gas/photon trajectory, nonlinear BE root, native/NCP program 및 PHYS01/02 완료 suite를 호출하는 경로는 없다.

개별 명령은 다음과 같다.

    python3 -B inputs/source_survey/verify_source_intake.py --output /new/path/SOURCE_IDENTITY_NEW.json
    python3 -B -m unittest discover -s tests -v
    python3 -B src/analyze_chronology.py --output /new/path/CHRONOLOGY_NEW.json

Smooth checker는 script 옆에 결과를 쓰는 독립 산출물의 원본을 그대로 보존했다. 기존 결과에 덮어쓰지 않으려면 reproduce.py를 쓰거나 check_nonautonomous.py와 SOURCE_PROFILE_INPUT.json을 새 directory로 복사한 뒤 실행한다.

## 기존 결과의 의미

| evidence | 확인하는 것 |
| --- | --- |
| inputs/source_survey/SOURCE_IDENTITY_VERIFICATION.json | 원 source/record identity와 selected-stage 연결 |
| smooth_theory/NONAUTONOMOUS_EXACT_CHECK.json | 36 비자율 exact case, 10 formal BE case, causal kernel |
| logs/hybrid_initial.stderr | 8 exact event/guard 검사 |
| results/CHRONOLOGY_256.json | Arb256 real-expression enclosure와 독립 mpmath 비교 |
| independent/DECISION.json | 별도 최종 reviewer의 범위별 판정 |

Arb의 decimal lower/upper는 바깥쪽 반올림이다. exact dyadic endpoints도 저장했다. 이로써 선언한 exact-binary64-leaf real expression을 검사하며 native Rust의 각 operation rounding은 재현하지 않는다. Decimal70 source-profile 숫자는 leading coefficient의 진단값이고 interval certificate가 아니다.

Copied source와 독립 이론 packet의 원 manifest도 보존했다. 전체 PHYS03 manifest는 이 복사본과 새 root 산출물을 함께 봉인한다. Provenance에 남은 과거 절대경로는 당시 실행 위치의 기록이며 재현 시 그 경로를 열지 않는다. 필요한 PHYS01 point coefficient의 원본은 inputs/PHYS01_LOCAL_COEFFICIENTS_FINAL.json에도 포함했다.
