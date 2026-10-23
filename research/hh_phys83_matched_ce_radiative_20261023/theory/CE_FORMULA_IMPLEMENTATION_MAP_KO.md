# PHYS83 CE 수식–구현 연결 및 정적 검사

## 역할과 증거 범위

`physmath-research-loop` v1.3.0의 CODING_LOOP C2/C3/C5를 적용한 구현 worker다. 물리 계약 SHA `afa2dfb19d4cf2dbc0112484cb898372485088f605e809cfbd9920a6955f75fa`와 `theory/MATCHED_KERNEL_CORE_KO.md`를 입력으로 사용했다. C5에서 이 worker가 수행한 것은 구문 compile 및 AST/import/SHA 정적 검사뿐이다. 독립 수치 검증, 과학 profile, ODE, benchmark는 수행하지 않았으며 그 상태를 PASS로 주장하지 않는다.

## 고정 API

- `load_channels(source_directory=None)` → `{'2S': MatchedCEChannel, '2P': MatchedCEChannel}`; source loading만 수행한다.
- `MatchedCEChannel(upper_level, source_directory=None)`에서 upper level은 정확히 `2S` 또는 `2P`다.
- `model.moments(T_K)` → frozen `MomentPair`: M0, M1, log M0, mean excess.
- `model.evaluate(T_K, *, species='H1', full_physical_rate=False)` → frozen `RatePair`; dataclasses.asdict 지원. 실제 rate 호출은 명시적이며 숨은 profiler/counter/autorun은 없다.
- `model.coverage()` → 직렬화 가능한 finite-source/source-identity 사전.
- `RatePair`의 자연로그 필드는 `log_q_up_cm3_s`, `log_q_down_cm3_s`; 밑10 필드는 `log10_q_up_cm3_s`, `log10_q_down_cm3_s`다.
- 온도 도함수는 `dlogq_up_dT_K_inv`, `dlogq_down_dT_K_inv`, `dq_up_dT_cm3_s_K`, `dq_down_dT_cm3_s_K`다.
- 평균 입사 에너지는 `mean_incoming_up_eV`, `mean_incoming_down_eV`; 공통 평균은 `mean_excess_eV`다.

## 수식 대응

| 물리식 | 구현 |
|---|---|
| ε=E−Δ; Δ=10.20435 eV | `gap_eV`, immutable `epsilon_eV` |
| σ cm² = σ a0² × (100 a0_m)² | immutable `sigma_cm2` |
| W=(ε+Δ)σ↑, Wmax scaling | immutable `W_eV_cm2`, `_W_left_scaled`, `_W_right_scaled`, `_W_scale` |
| Jn(z)=∫₀¹tⁿe^(−zt)dt, n=0,1,2 | byte-pinned vendor `_moments` only |
| M0cell=h e^(−l/θ)[WL(J0−J1)+WR J1] | `moments`: `cells0` |
| M1cell=h e^(−l/θ){WL[l(J0−J1)+h(J1−J2)]+WR[lJ1+hJ2]} | `moments`: `cells1` |
| M0/M1 endpoint sums | nonnegative cells + `math.fsum`; scale restored after sum |
| C=100√(8 eV_J/(π me)) | `MAXWELL_FACTOR` |
| q↑=C θ^(−3/2)e^(−Δ/θ)M0 | `log_up=log_common−gap/θ`; separate `math.exp` |
| q↓=C θ^(−3/2)(g0/gi)M0 | `log_down=log_common+log(g0/gi)`; separate `math.exp` |
| logq↑−logq↓=log(gi/g0)−Δ/θ | shared `log_common`; no q↑ × exp(Δ/θ) |
| μ=M1/M0, μ↑=Δ+μ, μ↓=μ | scaled ratio, named mean fields |
| dlogq↑/dT=((Δ+μ)/θ−3/2)/T | `dlog_up` |
| dlogq↓/dT=(μ/θ−3/2)/T | `dlog_down` |
| dq/dT=q dlogq/dT | `dq_up`, `dq_down` |

## 범위와 guard

네 CCC 원문 각각의 SHA를 channel pair별로 검사하고 forward452/reverse451 rows, channel header, a0² 및 eV column 의미, ascending energy, source-native endpoints, nonnegative threshold와 positive 나머지 σ를 검사한다. raw reverse σ는 증거 배열로만 보존하고 별도 rate 계산에는 쓰지 않는다. 모든 source/derived arrays는 bytes owner의 NumPy view로 저장하여 writeability 재활성화를 막으며 model attribute도 frozen이다.

온도는 finite real nonbool scalar, 255≤T≤50000 K만 받는다. 문자열, 배열, bool, NaN/inf, 범위 밖, 타 isotope/species, 다른 upper level 및 full physical rate 요청은 거절한다. 반환하는 positive moment/rate 및 모든 도함수의 finiteness를 검사한다. 고에너지 실제 tail, 물리적 interpolation error, isotope precision, LS mixing, 다른 원자 species는 OPEN/UNAVAILABLE 상태다.

## 실제 정적 receipt

```json
{
  "stage": "C2/C3 implementation; C5 static compile only",
  "file": "/tmp/phys83_work_20261023/WU088_HH/research/hh_phys83_matched_ce_radiative_20261023/source/matched_ce.py",
  "file_sha256": "4adfa426319574ac0a62e9083f5d09ce6261585f2aa860b00fc41b92bf2c08ef",
  "file_bytes": 13901,
  "syntax_compile": "PASS; compile(bytes, path, exec), no execution",
  "vendor_sha256": "859cdf616ffa165c9fb3c3372d2202f5449e4b9a74a289a725fe456e26eb55b2",
  "helper_ast_source_sha256": "a278db80ead183dd89a15a34cbac554fcba6a5edb0473d26b52697e3c1d8c416",
  "reused_imports": [
    "A0_M",
    "EV_J",
    "KB_EV_K",
    "ME_KG",
    "_moments"
  ],
  "source_load_calls_executed": 0,
  "rate_evaluations_executed": 0,
  "numerical_tests_executed": 0,
  "profiles_ode_benchmarks_executed": 0,
  "verification_owner": "root; independent numerical pass still required"
}
```
