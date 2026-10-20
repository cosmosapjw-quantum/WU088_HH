# PHYS70 추가 실행 근거의 독립 검토

**판정: 병렬 완주 12건과 NCP용 runner의 샌드박스 smoke 1건을 확인했다.** 기존 PERFORMANCE_REVIEW는 변경하지 않았다. 이 검토가 새로 실행한 적분·콜백·단계 검사는 0건이며 저장된 원본만 읽었다.

## 독립 궤적의 병렬화

| worker | 완료 job | batch 시간 | process wall | 1 worker 대비 batch 비율 |
|---:|---:|---:|---:|---:|
| 1 | 4/4 | 0.201385102 s | 0.216208846 s | 1.00000배 |
| 2 | 4/4 | 0.138033682 s | 0.165419341 s | 1.45896배 |
| 4 | 4/4 | 0.099805345 s | 0.115403925 s | 2.01778배 |

각 worker 수에서 **표본은 한 묶음**이다. 중앙값이나 확률적 성능 보장은 주장하지 않는다. 4개의 서로 독립적인 L28 요청은 rtol3e-9,3e-10,3e-11,3e-12이고 각 궤적의 radial carry는 순차다. 모델·seed·원본 source와 실행 파일은 기존 성능 실험과 동일하다.

12개가 모두 tau0→38, 실수 234개×2의 유한한 상태로 완료됐다. worker 2·4와 worker1의 대응 8쌍, 총3,744개 저장 성분을 IEEE-754 비트로 비교해 순서와 비트가 일치했다. 수락 단계 수는 각 요청에서436/703/1132/1819이고 거절은0이다. 상대 D2 오차 상계는 각각1.62751843e-9,1.47285672e-10,1.38569946e-11,1.27015323e-12로 네 요청의 목표보다 작다.

타이머는 pool 생성과 seed 파싱 뒤에 시작하며 각 job의 solver setup·적분·메타데이터 변환과 결과 수집을 포함한다. 마지막 batch JSON 출력과 프로세스 기동은 밖에 있다. 원시 batch 파일 해시, 정확한 입력 list 바이트, 각 결과의 요청 내용 및 출력 순서를 대조했다. 개별 요청의 digest는 native serde_json 직렬화에서 나온 값으로 분류하며 Python JSON 바이트와 동일하다고 가정하지 않는다.

## NCP용 runner의 샌드박스 실제 검증

이 pilot의 실제 hostname은 `6a4240d1fd44`이며 현재 샌드박스의 실행 파일을 사용했다. 영수증 자체의 NCP_submission은 `DIRECT_HOST_EXECUTION_ONLY_NO_REMOTE_JOB_SUBMISSION`이다. 따라서 **NCP용 runner의 샌드박스 실행 검증**으로 기록하며 원격 NCP에서 실행했다고 표시하지 않는다.

rtol3e-11/atol3e-13 요청이1,132단계로 완료됐고 D2의 상대 오차 상계1.3856994587496746e-11은 목표3e-11보다 작다. 결과 SHA256은 `0ef41785793d32d47fdb63a7d12828d9d5c2f6e06e3746c65ade85d8ac23be27`이며 저장 state는 대응 worker1 job과 비트까지 동일하다. 이 wrapper 실행은 이미 빌드된 외부 binary를 사용했다는 `EXTERNAL_BINARY_SHA_ONLY` 범위다.

완료 출력에 대한 --resume은 새 적분0·파일 쓰기0을 보고했다. 저장된 before/after와 현재 디렉터리의10개 파일을 대조해 내용 hash·크기·mtime_ns가 모두 동일함을 확인했다. resume 재실행은 하지 않았다.

## L64 및 검증·게시·백업 분리

L64는 PREFLIGHT_ONLY 영수증만 있다. child process0, special-function call0, 적분0이고 seed 및 RESULT가 생성되지 않았다. 해당 preflight 환경의 python_flint_available은 false로 기록돼 있다. 이를 L64 실행 완료나 새로운 수치 결과로 세지 않는다.

13개 추가 완료 결과에 대한 정확한 유리수 오차 기록65개와 저장 complex component Fraction26개를 다시 계산해 일치했다. manifest가 나열한 payload37개 및 실제 파일 집합도 맞았다. 모든 원본 물리 및 HH_R10=OFF를 유지하고 PHYS63은 ESTABLISHED_REUSED다.

| 항목 | 이 검토의 상태 |
|---|---|
| 실제 실행 | 기존 완료 performance12건 + 샌드박스 runner1건 재사용 |
| 독립 검증 | 원본 해시·완료·요청·state 비트·정확한 D2 점 오차 확인 |
| L64 | PREFLIGHT_ONLY; 계산 결과 없음 |
| 게시 | child가 판정하지 않음; root가 실제 Git 영수증 관리 |
| 백업 | child가 판정하지 않음; root가 실제 백업 영수증 관리 |
| DAG | 제한된 병렬 성능·runner sandbox·읽기 전용 resume 통과; L64 사전 점검 |

정확한 파일 해시와 시료별 판정은 ADDITIONAL_EXECUTION_REVIEW.json에 기록했다.
