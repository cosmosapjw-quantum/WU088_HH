# PHYS68 연구 전 회수·대조

새 과학 실행 전에 PR117, 대상 백업 폴더와 회수한 PHYS67 배포본을 확인했다. `GITHUB_BASE.json`은 원격 기준과 실제 선후 관계를, `BACKUP_INTAKE.json`은 검사 범위와 파일 정체성을, `PROTECTED_INPUTS_CHECKED.json`은 원본 NPZ 및 PR114/115 관련 9개 경로의 byte/hash 보존을 기록한다.

검사한 백업 범위에서 새 longtail 결과는 발견되지 않았다. NCP 호스트는 이 intake에서 관찰하지 않았으므로 호스트의 실제 실행 여부를 단정하지 않는다. PHYS64 NCP20 및 완료된 PHYS66/67 실행은 재사용했다.

요청된 최종 PHYS66 ZIP `993317b1…`은 여전히 `BLOCKED_ARTIFACT_ACCESS_EXACT_FINAL_VERSION`이다. PR117에서 회수·검증한 이전 ZIP `84c29de7…` 및 이번에 다시 회수한 PHYS67 배포본과 버전을 혼동하지 않는다. 이 접근 제한은 접근 가능한 PR117 소스와 증거를 사용하는 새 PHYS68 유도·계산을 가짜 복원으로 바꾸지 않는다.

이 파일들은 과학 시작 전 관측 기록이다. 새 PHYS68 게시와 백업 성공 여부는 `../publication/`의 실제 응답 영수증으로 확인한다.
