# R31V 재감사 RETURN — NCP focused 재검증

대상 remote publication은 `928470d4cc9e969dac85b5f1524375f816128489` / tree `6b4dbc30b14bfddbed5c1980bef04b0cfd95f442`였다. 새 worktree에서 시작했고 기존 worktree와 원 raw는 변경하지 않았다. 원 `REVIEWED_FILES.json`의 모든 covered byte/size는 수정 전 publication checkout과 일치했다. 수정 후 bytes는 `FINAL_SOURCE_MANIFEST.json`에 별도로 고정했다.

NCP Python 3.12.3, NumPy 2.3.5, pytest 9.1.1에서 publication 소스의 `py_compile`, 지정된 focused pytest, `describe`, raw replay가 모두 exit 0이었다. 최초 focused 결과는 133 collected / 133 pass / 0 fail / 0 skip이다. 독립 검토 BR-03의 잘못된 layout 입력은 새 focused regression test에서 1 collected / 1 fail로 재현했다. preflight 전에 create-only 시도 checkpoint를 기록하고 실패 상태를 갱신하도록 최소 수정했다. 최종 동일 범위는 134 collected / 134 pass / 0 fail / 0 skip이며 나머지 세 명령도 exit 0이다. 실제 argv, cwd, 환경, exit 및 JUnit은 `RETURN.json`과 동봉 로그에 있다.

Raw replay의 모든 검사 항목은 true이며 기존 12 측정 행의 내부 일관성을 확인한다. 이는 timed candidate 배열 독립 재계산이 아니다. 원 prepare의 명시적 reference 계산과 benchmark의 cache-only read를 다시 수행하지 않았다. root/leaf CPU 차이 음수 10건은 host 독점성 또는 타 세션 CPU 상계로 해석하지 않는다.

별도 reviewer의 최초 결과는 구현자 보고서와 새 테스트를 공개하기 전에 SHA-256으로 동결했다. `BLIND_REVIEW.json`과 `BLIND_REVIEW_KO.md`가 그 원본이다. 다른 agent 문맥에서 source-first 검토를 수행했지만 harness 신원·공식 admission은 독립적으로 증명되지 않았고, 이후 최소 patch 자체는 blind review 대상이 아니었다. 따라서 `independent_review_admitted=false`다. BR-01(원 실행의 control source 귀속)과 BR-02(prepare·benchmark cache byte 연결)는 실제 변조 관측 없이 발견된 historical evidence gap이다. 과거 실행에 대한 새 증거를 소급 생성하지 않으며, 금지된 M3B/reference rerun도 수행하지 않았다.

원 H0 authority, B160 M3A, B192 pilot, full-pair equality 및 source/build/ABI 기록은 보존했다. 이번 범위에서 native source/build 또는 과학적 배열을 변경하지 않았다. `M3A_RERUN=false`, `M3B_RERUN=false`, `NEW_SCIENTIFIC_NODES=0`, `production_admitted=false`, `provider_admitted=false`다. z=1, z=0.5, full144, trajectory, M5, CR/HE 및 다른 owner의 실행 상태를 건드리지 않았다. provider ACK와 실제 raw restore는 별도 receipt로 판정한다.
