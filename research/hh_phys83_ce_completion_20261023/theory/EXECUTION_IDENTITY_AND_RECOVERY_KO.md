# 실행 identity와 복구 계약

과학 identity는 CONTRACT, CE rate/3상태 해/runner 구현과 원본 source bytes에서 계산한다. 런타임 버전은 ENVIRONMENT.json에 기록하되 identity에는 넣지 않는다. 버전 차이만으로 완료 계산을 다시 실행하지 않는다.

`delivery/scientific_claims/<identity>.json`을 exclusive create한 실행만 새 계산에 들어간다. 기존 완료 결과는 COMPLETE.json의 모든 payload 크기와 SHA256을 확인하고, kernel import/과학 callback 전 `SKIP_COMPLETED_IDENTITY`를 반환한다. 복원 경로가 달라도 동일 bytes를 검증한다. 완료 결과의 변조, 실패/중단 claim, 기존 미등록 output은 자동 재실행하지 않고 거절한다. 실패한 시도의 원문·부분 파일은 보존한다.

과학 실행은 rate pair 132회, steady 324회, transient 732회로 제한된다. 66개 T의 rate를 캐시하여 나머지 단계에서 재사용한다. rate 쌍은 상승·하강을 함께 반환한다. 지표 추출과 그림은 저장 CSV만 읽으며 새 과학 실행으로 집계하지 않는다.

검증은 과학 실행과 분리된다. CE verifier의 QUADPACK/80자리 expm과 nuclear Decimal 참조, mock 저장기 검증은 verification ledger에 기록한다. 완료 science 및 과거 source-check 902개를 반복하지 않는다.

## 실행 환경과 lease

`source/leased_call.py`는 보존한 공동 lease protocol만 사용한다. 1worker/1thread이며 다른 process를 종료하지 않는다. 이번 환경에는 mpmath가 없어 첫 verification import가 실패했다. 해당 시도는 계산 0으로 보존했고, mpmath 1.3.0 wheel을 작업 폴더에 설치한 후 수치 검증을 진행한다. requirements-verification.txt는 실제 사용 버전을 기록한다. 원본 wheel은 최종 복구 ZIP의 private evidence에 포함한다.

```bash
PYTHONPATH=/path/to/local/mpmath python source/leased_call.py \
  --label science_first --receipt verification/lease_science_first.json -- \
  python source/run_study.py --execute --receipt verification/science_first.json
```

이 명령은 이미 완료된 identity가 있으면 skip만 해야 한다. 재실행을 위해 claim이나 완료 결과를 지우지 않는다. 복구 ZIP을 검증할 때도 원본 bytes와 실제 추출을 검사하며 과학 커널을 호출하지 않는다.

## 범위

유한 소스·고정 T/ne·3상태·즉시 광자 탈출이라는 닫힌 모형이다. sampled residual과 독립 수치 비교는 continuum certificate가 아니다. HH_R10=OFF, production admission NOT_ISSUED.
