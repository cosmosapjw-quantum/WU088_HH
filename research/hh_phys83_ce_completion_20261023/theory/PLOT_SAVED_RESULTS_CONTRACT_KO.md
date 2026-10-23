# PHYS83 저장 결과 전용 그림 계약

`source/plot_saved_results.py`는 저장된 CSV 세 개만 읽는다. `matched_ce`와
`frozen_star`를 import하지 않고 rate, quadrature, population solution을 호출하지 않는다.
이 문서 작성 시 실제 plotting 실행은 0이며, 정적 compile과 AST import 검사가 완료됐다.

## 입력

기본 입력 경로는 unit의 `results/`다. CSV는 header를 포함해야 하며 추가 column은
허용한다. 원래 고정 연구 grid의 행 수·group 수와 중복 좌표를 검사한다.

| 파일 | 필수 column | 행 수 |
|---|---|---:|
| `rate_grid.csv` | `upper_level`, `temperature_K`, `q_up_cm3_s`, `q_down_cm3_s` | 132 = 2 × 66 |
| `steady_grid.csv` | `temperature_K`, `electron_density_cm3`, `exact_to_coronal_2s`, `exact_to_coronal_2p`, `critical_density_2s_cm3`, `critical_density_2p_cm3` | 324 = 4 × 81 |
| `transient_grid.csv` | `temperature_K`, `electron_density_cm3`, `time_s`, `atomic_excitation_eV`, `escaped_radiation_eV`, `heat_withdrawal_eV`, `thermal_change_eV`, `normalized_raw_energy_residual` | 732 = 6 × 122 |

온도와 density의 허용 grid는 동결 계약과 같다. `time_s=0`인 여섯 행은 에너지
zero를 확인한 후 log 축에서 제외한다. 로그 축의 나머지 값은 양수여야 하며
작은 값을 임의 floor로 올리거나 음의 값을 clipping하지 않는다. 기존 저장
`thermal_change_eV=-heat_withdrawal_eV`의 부호 대응도 확인한다.

## 출력과 시각적 의미

기본 출력은 `figures/`이며 아래 세 그림 각각 PNG 180 dpi와 vector PDF를 만든다.

1. `01_finite_matched_rates`: excitation과 deexcitation을 별도 두 panel에서
   log T / log rate로 표시한다. 2s와 2p는 일관된 색으로 구분한다.
2. `02_steady_coronal_suppression`: 네 고정 온도에서 2s와 2p의 stationary
   radiation/coronal-reference 비를 density의 함수로 표시한다. 같은 온도의
   `ncrit=A/qdown`은 같은 색의 dotted vertical line과 실제 저장값으로 표시한다.
   High-density 구간은 선택된 three-level star의 진단임을 caption에 명시한다.
3. `03_transient_energy_accounting`: 두 온도 × 세 density의 여섯 저장 profile을
   panel로 나눈다. Atomic storage, escaped radiation, thermal withdrawal을
   proper time의 함수로 표시하며, 양의 withdrawal과 signed thermal change를
   혼동하지 않는다. Two-photon decay의 사건당 총에너지는 Delta이고 photon 수는
   둘이라는 convention을 caption에 쓴다. 패널 내 residual은 저장된 유한 grid의
   산술 residual이다.

그림은 finite source, prescribed T/ne, optically thin spontaneous escape라는
범위를 표시한다. Interpolation/tail의 physical uncertainty band나 coupled
thermal-history boundary는 새로 만들지 않는다.

## Create-only와 실행

```bash
python3 research/hh_phys83_ce_completion_20261023/source/plot_saved_results.py
```

다른 입력·출력 경로는 `--input-directory`, `--output-directory`로 지정한다.
예상되는 그림 파일 또는 `PLOT_RUN_RECEIPT.json` 중 하나라도 이미 있으면 출력
생성 전에 거절한다. 실제 저장도 exclusive mode를 쓴다. 시각 감사 후 수정이
필요하면 이전 결과를 보존하고 새 출력 directory를 사용한다.

Receipt는 script/input/output의 bytes와 SHA256, matplotlib version, 저장 행 수,
제외한 zero-time 행, 저장 residual의 최댓값을 기록한다. 완료 직후 상태는
`PLOTS_CREATED_AWAITING_VISUAL_AUDIT`다. 출력 중 실패하면 생성된 파일을
보존하고 `FAILED_PARTIAL_OUTPUTS_PRESERVED`로 남긴다. 성공한 render 자체로
visual audit 또는 독립 scientific validation을 통과했다고 표시하지 않는다.

## 정적 receipt

```json
{
  "file": "source/plot_saved_results.py",
  "bytes": 16437,
  "sha256": "24b2194cf5262bfebf955f30cc4e794042f1831e07cdaaaab781c57c316fed78",
  "syntax_compile": "PASS",
  "ast_import_check": "PASS: no matched_ce or frozen_star imports",
  "plot_calls_executed": 0,
  "science_calls_executed": 0
}
```
