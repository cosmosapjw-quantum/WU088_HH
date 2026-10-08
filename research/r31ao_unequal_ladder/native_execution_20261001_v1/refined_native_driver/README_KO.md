# 재분할 가능한 범위 거절을 보존하는 추가 구현

이 드라이버는 이미 실행한 `native_driver/`와 고정된 기존 Petras 구현을 변경하지 않는다. `refining_petras.cpp`만 추가로 연결하며 기존 헤더, callback, 정확 입력, 마진 보정, baseline/cached 선택, 계산량 및 정밀도 API를 그대로 사용한다. 다른 source identity와 빌드 manifest가 필요하므로 이전 실행 파일의 기록을 재사용하지 않는다.

수정 범위는 다음 세 곳이다.

1. order 0 입력이 비정확한 공이면 전체 범위 요청이다. nonfinite 반환은 그 공을 거절하고 FLINT가 재분할하도록 허용한다. 이를 유한 값이나 중점 값으로 바꾸지 않는다.
2. 외부 매개변수 공이 비정확한 경우, 내부 적분의 nonfinite·비수렴·과도한 폭은 외부 재분할 요청으로 전달할 수 있다. 공용 예산이 이미 중단됐으면 이 경로를 사용하지 않는다.
3. 내부 절점이 정확해도 외부 공에 반지름이 있으면 매개변수 범위 요청으로 취급한다. 모든 외부 공을 원래 크기 그대로 전달한다.

order 0의 정확한 점 실패는 계속 치명적이다. 정밀도·차수·입력 계약 위반, callback 예외, 공용 평가 횟수·중첩 횟수·적분 호출 수·시간 한도는 계속 전체 중단을 일으킨다. 어떤 예산도 초기화하거나 복원하지 않는다. FLINT의 유한 구간 큐·차수·평가 한도와 최종 반환 반지름 검사는 바뀌지 않았다. 따라서 실패하는 공은 나누어 다시 시도할 수 있지만 한도 내에서 인증되지 않으면 최종 결과를 받아들이지 않는다. 비정확 GL 절점 공은 정확한 점이 아니므로 그 안의 본질적인 특이점도 보수적으로 재시도하다가 한도에 도달할 수 있다.

`analytic_box_refusals`는 order 1 거절만 센다. order 0 범위 거절은 이 분석적 공 카운터를 증가시키지 않지만 모든 실제 callback 평가를 기존 공용 카운터로 센다.

## 검증

`run_synthetic.py`는 고정 backend의 출처와 실제 링크를 확인한 뒤 해석적 시험만 컴파일·실행한다. 원본 host와 수정 host에서 같은 시험 소스, 128비트, 구간 `[2^-8,2^192]`, 상대 목표 32, 절대 요청 `2^-40`, 반환 성분 반지름 한도 `2^-20`, 20,000 평가 한도, 15초 협력 한도를 사용했다. 이는 생산 worker의 기본 오차를 변경한 것이 아니라 기존 독립 `1/t` 반례의 조건을 그대로 비교한 것이다. 외부 시험 프로세스는 512MiB 주소 공간과 20초 한도를 가진다.

원본은 `NONFINITE_CALLBACK`, 1회 평가에서 실패했다. 추가 구현은 `RADIUS_MET`, 3,240회 평가로 통과하고 정확한 적분식 `200 log(2)`의 Arb 구간과 겹쳤다. 정확한 점·예외·정밀도·차수·평가량 한도 거절, 매개변수 범위 전달, 외부 폭 거절도 함께 검사했다. red/green의 원본 stdout·stderr·컴파일 명령·링크 해시가 `analytic_red/RECEIPT.json`, `analytic_green/RECEIPT.json`에 남아 있다. Python 경계 검사는 17개 통과했다.

실제 HH 적분은 이 모듈의 검증 실행에서 수행하지 않았다. 이 수정만으로 W3 전체가 한도 내 계산된다고 주장하지 않는다. 넓은 외부 매개변수 공에서 내부 적분이 예산을 소진하면 공용 중단을 그대로 유지한다. 이후 실제 실행은 먼저 검증한 작은 창 또는 명시적 제한이 있는 넓은 창으로 수행하고 미완료를 기록해야 한다.

## 호출

이전 API와 동일하다. 다음은 create-only 새 빌드 디렉터리를 사용하는 예시다.

```sh
python -B refined_native_driver/driver.py build \
  --input-npz /absolute/FROZEN_INPUTS.npz \
  --flint-prefix /absolute/pinned/prefix \
  --backend-provenance /absolute/BACKEND_BUILD_PROVENANCE.json \
  --output-directory /absolute/new-refined-build \
  --callback-mode cached
```

실제 조립 경계에서는 `assembly_host`의 `configured_context`에 이 `driver.py`의 절대 경로와 SHA256을 전달해야 한다. 기존 hardcoded join CLI나 이전 source/build manifest를 섞지 않는다. 정확한 task/window/입력 identity와 native 반환 구간 형식은 그대로다. 소구간 결과에는 endpoint 항이 없으며, W3의 전역 endpoint와 바로 합칠 수 없다.
