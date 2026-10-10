# PHYS04 증거 확인과 선택적 재현

## 기본은 봉인된 증거의 identity 확인

~~~bash
python3 -B reproduce.py --verify-only
~~~

MANIFEST.json에 기록된 payload의 SHA-256와 bytes만 확인한다.
과학 검사, native solve 또는 이전 PHYS loop는 실행하지 않는다.
FINAL_VERIFICATION.json은 이번 제작 때 실제로 수행한 새 검사들을 요약한다.

## 새 PHYS04 검사의 명시적 재실행

재실행이 필요한 독립적 이유가 있을 때만 아직 존재하지 않는 절대 경로를 쓴다.
아래 경로는 예시이며 작업자가 자신의 새 경로로 지정한다.

~~~bash
python3 -B reproduce.py --run-new-checks --out-dir /tmp/hh_phys04_recheck_new
~~~

Python standard library만 사용한다. 검증한 input/코드 bytes를 새 workspace로
복사한 뒤, 이 패킷의 final quartic run_02 코드, remap operator 및 implicit
arithmetic만 순서대로 실행한다. 실패 로그도 새 경로에 남긴다.
봉인 패킷이나 과거 result를 덮어쓰지 않는다. 원 quartic script가 실패 기록을
script 옆에 쓰므로 반드시 복사본을 실행한다.

재현 결과에는 machine-dependent elapsed time이 있어 JSON 전체 byte가 같을
필요는 없다. Claim에 연결된 rational values, interval containment와 structural
checks를 비교한다. 재실행은 독립 최종 판정을 대체하지 않는다.
NCP actual source provider/root/trajectory는 이 명령에 포함되지 않는다.

그림은 저장된 결과로 이미 생성되어 있다. src/plot_remap.py는 선택적 표시용이며
matplotlib가 필요하다. 봉인된 evidence를 읽기만 하려면 그림을 다시 만들 필요가 없다.
