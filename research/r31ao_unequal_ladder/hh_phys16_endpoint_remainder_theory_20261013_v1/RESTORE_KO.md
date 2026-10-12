# PHYS16 재현 자료 복원

전체 snapshot의 PHYS16 디렉터리를 임의의 작업 폴더에 푼 뒤, `dependencies/WU088_HH_PHYS15_THEORY_20261013_FULL_SNAPSHOT.zip`도 같은 작업 폴더에 푼다. 그러면 `HH_PHYS16_THEORY_20261013_v1`과 `HH_PHYS15_THEORY_20261012_v1`이 형제 디렉터리가 된다. 부모 archive는 원본 그대로 포함되며 SHA256은 `3e9df6e688e8b707e50c188866e84bc7c95491e6a7bae116d6bbfc97a9e87ffe`다.

`DEPENDENCIES.json`에 원 입력·helper·부모 commit/tree를 고정했다. 실제 계산의 정확한 CLI는 `README_KO.md`와 각 `PRE_RUN.json`에 있다. 출력은 새 디렉터리에 기록하고, 동결된 원 `run01`, `application01`을 덮어쓰지 않는다. 첫 실행은 Python 표준 라이브러리의 Fraction으로 보존된 구간을 적용하고, 두 번째 실행은 endpoint/adjoint 나머지를 적용한다. 원 반응 source·비선형 근·history suite를 다시 실행할 필요가 없다.

공식 xAct 검산 코드는 `checks/wolfram/endpoint_tensor_checks.wl`, 실제 환경·패키지·최종 응답은 `WOLFRAM_XACT_EXECUTION.json`에 보존했다. 별도의 Wolfram Language 환경과 공식 xAct 1.3.0 archive가 필요한 재현이며, `$xpermQ=False`를 사용한 실제 backend 선택을 그대로 따른다.

이 과학 snapshot은 실행 당시 바이트를 고정한다. 실제 Git/Google Drive/Dropbox 식별자와 저장 완료는 snapshot 밖의 최종 전달 receipt 및 저장 후 metadata commit으로 연결한다. 공급자 acknowledgement와 실제 다운로드·전체 재실행 검증은 구별해 기록한다.
