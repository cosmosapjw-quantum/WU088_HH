# PHYS83 continuation: matched CE 수식–구현 연결

## 구현 identity와 완료 범위

현재 사용자 지정 `physmath-research-loop` 1.0.0의 C2–C5 구현이다.
물리적 부모는 PHYS83 S0 `09289300ec2e500806aa2cb82365f00329e41c8c`이며,
`CONTRACT.json`의 source-native gap·temperature domain·finite-support 조건을 유지한다.
S0 문서에 남은 구 구현 SHA
`4adfa426319574ac0a62e9083f5d09ce6261585f2aa860b00fc41b92bf2c08ef`와
이번 새 `source/matched_ce.py`의 bytes는 별개의 identity다.

이번 작성자는 원자료를 읽고 코드를 작성했으며 구문 compile과 AST 검사만 수행했다.
모듈 import, source loader 호출, moment/rate 평가, 수치검증, 과학 grid, ODE,
benchmark 실행 수는 모두 0이다. C6–C9 판정은 별도 검증 실행에 의존한다.
이 agent의 선행 원전 검토는 새 코드 작성 전의 source review이며 자기 코드의
독립 구현 심사로 집계하지 않는다.

## API

- `load_channels(source_directory=None)`는 `{'2S': model, '2P': model}`을 반환한다.
- `MatchedCEChannel(upper_level, source_directory=None)`는 정확히 `2S`, `2P`만 받는다.
- `model.moments(T_K)`는 frozen `MomentPair`를 반환한다. 필드는
  `temperature_K`, `M0_eV2_cm2`, `M1_eV3_cm2`, `log_M0_eV2_cm2`,
  `mean_excess_eV`, `finite_source_only`다. `M0`, `M1`, `log_M0` 읽기 property도 있다.
- `model.evaluate(T_K, *, species='H1', full_physical_rate=False)`는 frozen
  `RatePair`를 반환한다. `dataclasses.asdict`로 직렬화할 수 있다.
- `model.coverage()`는 source·domain·단위·근사와 사용 범위를 사전으로 반환한다.

자연로그 출력은 `log_q_up_cm3_s`, `log_q_down_cm3_s`, 밑10 로그는
`log10_q_up_cm3_s`, `log10_q_down_cm3_s`다. Underflow 여부는
`float64_underflow_up`, `float64_underflow_down`에 독립적으로 기록한다.
평균 에너지는 `mean_excess_eV`, `mean_incoming_up_eV`,
`mean_incoming_down_eV`다. 도함수는 `dlogq_up_dT_K_inv`,
`dlogq_down_dT_K_inv`, `dq_up_dT_cm3_s_K`, `dq_down_dT_cm3_s_K`다.

## 정의와 코드의 대응

에너지는 eV 수치, theta는 `KB_EV_K * T_K`다. 면적은 원래 a0²를
`(100*A0_M)**2`로 cm²로 변환한다. 고정된 `A0_M`, `EV_J`, `KB_EV_K`,
`ME_KG`는 byte-pinned C22D vendor에서 재사용한다.

| 계산식 | 구현 |
|---|---|
| epsilon = E - Delta, Delta = 10.20435 eV | immutable `epsilon_eV`, `gap_eV` |
| W(epsilon) = E sigma_up(E) | immutable `W_eV_cm2` |
| W-PL, common finite support 0 .. 958.40145 eV | `_left_eV`, `_width_eV`, scaled left/right W |
| J_n(z) = integral_0^1 u^n exp(-z u) du | vendor `_moments`, n = 0, 1, 2 |
| M0_cell = h exp(-l/theta) [W_L(J0-J1) + W_R J1] | `moments(): cells0` |
| M1_cell = h exp(-l/theta) {W_L[l(J0-J1)+h(J1-J2)] + W_R[l J1+h J2]} | `moments(): cells1` |
| Nonnegative cell sums | `math.fsum`, followed by restoring W scale |
| Mean excess = M1/M0 | ratio of the scaled sums |
| C = 100 sqrt(8 eV_J/(pi m_e)) | `MAXWELL_FACTOR` |
| q_up = C theta^(-3/2) exp(-Delta/theta) M0 | `common_log - gap/theta`, then `exp` |
| q_down = C theta^(-3/2) (g_g/g_u) M0 | `common_log + log(g_g/g_u)`, then `exp` |
| dlogq_up/dT = [(Delta+mean_excess)/theta-3/2]/T | `dlog_up` |
| dlogq_down/dT = [mean_excess/theta-3/2]/T | `dlog_down` |
| dq/dT = q dlogq/dT | `dq_up`, `dq_down` |

M0의 단위는 eV² cm², M1은 eV³ cm²다. 이 prefactor와 조합한 rate는 cm³/s다.
두 방향이 같은 M0를 공유하므로 matched finite model에서
`log q_up - log q_down = log(g_u/g_g) - Delta/theta`다.
작은 q_up에 큰 `exp(Delta/theta)`를 곱해 q_down을 만드는 경로는 사용하지 않는다.
비교용 reverse raw sigma를 PL 보간하는 별도 rate 경로도 없다.

## 입력 guard와 불변성

각 loader는 raw CCC 네 파일 모두의 SHA256를 확인한다. 사용하는 forward와
reverse의 header, column 의미, 452/451 row shape, 유한성, 증가하는 에너지,
정해진 endpoint, threshold zero, 다른 sigma의 양성성을 확인한다.
기존 902점 printed-reciprocity matrix를 재평가하지 않는다. Reverse row는
readonly 증거 배열로 보존하며 실제 Maxwell rate는 forward W만 사용한다.

모든 source·derived 배열은 immutable bytes owner 위의 NumPy view다.
`array.flags.writeable = True`로 쓰기 권한을 복원할 수 없다. Model과 반환 dataclass는
frozen이며, source pin mapping도 readonly다.

온도는 `numbers.Real`의 유한 scalar이며 bool/np.bool_는 배제한다.
255 <= T <= 50000 K 범위만 받는다. 문자열·배열·complex·NaN/inf·범위 밖은
명시적 error다. 다른 species, 지원하지 않는 upper level, nonbool
`full_physical_rate`, 또는 `full_physical_rate=True`도 거절한다.
음의 cell이나 비유한 moment/rate/derivative는 clipping 없이 오류로 처리한다.

이 모듈은 source-native finite operator다. 실제 interpolation uncertainty,
omitted high-energy tail, finite-mass/isotope gap, same-n LS mixing, 다른 원소의
CE 및 전체 radiation/population closure는 여기서 채택하지 않는다. 함수 호출은
오직 명시적이며 module load나 source load가 과학 grid를 실행하지 않는다.

## 정적 실행 receipt

```json
{
  "stage": "C5 static implementation only",
  "file": "source/matched_ce.py",
  "bytes": 14892,
  "sha256": "475ee6f84c5e19945324859a9c4c5e229d8ab5e92e8658ad5b3da39472c1744e",
  "syntax_compile": "PASS: compile(source_bytes, filename, 'exec')",
  "ast_parse": "PASS",
  "module_execution": 0,
  "source_loader_calls": 0,
  "moment_calls": 0,
  "rate_calls": 0,
  "numerical_tests": 0,
  "science_runs": 0,
  "historical_replays": 0,
  "vendor_sha256": "859cdf616ffa165c9fb3c3372d2202f5449e4b9a74a289a725fe456e26eb55b2"
}
```

독립 verifier가 원전·유도·다른 적분 경로로 바뀐 구현을 검사한 뒤에
implementation/numerical 판정을 갱신한다. 정적 compile 결과를 그 판정으로
대체하지 않는다.
