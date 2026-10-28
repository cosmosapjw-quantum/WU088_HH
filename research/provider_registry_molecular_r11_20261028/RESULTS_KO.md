# R11 저장 결과 분석

**R11 capped endpoint는 네 사례의 모든 저장 시각에서 R10 capped와 정확히 같다. 최종 R·E 상계 개선은 0%다.** 새 결과는 전체 A family에 대한 유한 블록 인증과 forcing convolution의 구현이며, 현재 저장 사례의 final upper 개선과 구별한다.

## 실제 검증과 비용

Primary 214/214 PASS. 독립 reference 900/900 PASS, component comparisons 19,195, 실패 0. Python 각 1회, 전체 OS CPU 합 1.477435초이며 import·serialization을 포함한다. 이 분석은 저장 JSON만 읽으며 solver·production module·ODE 호출은 0회다.

독립 reference는 exact Fraction kernel/convolution과 Decimal160 closed-form E moments를 사용했다. 실행 전 고정한 guard는 `1e-80*max(1,abs(reference),abs(lower),abs(upper))`다. Component 비교 수는 서로 다른 물리 시나리오 수가 아니다.

Wolfram은 15개 zero residual을 반환했고 Power/General 경고가 함께 있었다. 상태는 `QUALIFIED_SYMBOLIC_CORROBORATION`, 원인은 `NOT_ESTABLISHED`다. R10의 원래 CAS 상태와 실행 예산을 변경하지 않는다.

## Full-A 블록 계수

| 사례 | 기존 K 인증 qK | additive Duhamel | 채택 minorization upper q |
|---|---:|---:|---:|
| 무반응 2상태 | 0.625 | 0.625 | 0.625 |
| 비선형 2상태 | 0.625 | 0.628 | 0.625562078336 |
| coarse source defect 2상태 | 0.625 | 0.628 | 0.625562078336 |
| native9 K + 합성 조건부 반응 | 0.00834612146063 | 0.00845545124996 | 0.00840032863382 |

각 q는 고정 K/pi/destruction과 인증된 전체 w box의 모든 가측 경로·모든 시작시각에 적용되는 증명에 결속되어 있다. Native9의 q는 1보다 작아 full-A finite-block contraction을 제공한다. K-only q를 full A에 그대로 이식하지 않는다. Additive saturation control에서는 q_add=1이지만 minorization q=0.862045209560709…<1이다.

## 최종 endpoint 상계

| 사례 | 성분 | R10 capped | R11 raw | R11 capped | capped 개선 |
|---|---|---:|---:|---:|---:|
| 무반응 2상태 | R | 0.0557825400371 | 0.06103515625 | 0.0557825400371 | 0% |
| 무반응 2상태 | E | 0 | 0 | 0 | 0% (양쪽 0) |
| 비선형 2상태 | R | 0.060211915866 | 0.0670615623148 | 0.060211915866 | 0% |
| 비선형 2상태 | E | 0.000396434054403 | 0.00051455388969 | 0.000396434054403 | 0% |
| coarse source defect 2상태 | R | 0.060211915866 | 0.0670615623148 | 0.060211915866 | 0% |
| coarse source defect 2상태 | E | 0.00056512078897 | 0.000683240624257 | 0.00056512078897 | 0% |
| native9 K + 합성 조건부 반응 | R | 3.64476161178e-05 | 7.01971878504e-05 | 3.64476161178e-05 | 0% |
| native9 K + 합성 조건부 반응 | E | 6.19079240657e-07 | 1.19238424256e-06 | 6.19079240657e-07 | 0% |

무반응 E=0의 비율은 수학적으로 0/0이므로 JSON에서는 percent=null로 기록하고 표에서는 양쪽 0의 동일성을 표시했다. 그 밖의 최종 capped percent는 정확히 0이다.

## 원소별 raw/capped 비교

비교 기준은 **R10 capped**다. Endpoint는 사례마다 193시각×2성분=386개, whole-cell은 192닫힌 셀×2성분=384개다. 아래는 R11이 기준보다 작은/같은/큰 성분 수다.

| 사례 | raw endpoint < / = / > | raw whole < / = / > | capped endpoint < / = / > | capped whole < / = / > |
|---|---:|---:|---:|---:|
| 무반응 2상태 | 0 / 194 / 192 | 0 / 193 / 191 | 0 / 386 / 0 | 0 / 384 / 0 |
| 비선형 2상태 | 0 / 2 / 384 | 1 / 0 / 383 | 0 / 386 / 0 | 167 / 217 / 0 |
| coarse source defect 2상태 | 0 / 2 / 384 | 1 / 0 / 383 | 0 / 386 / 0 | 173 / 211 / 0 |
| native9 K + 합성 조건부 반응 | 0 / 2 / 384 | 1 / 0 / 383 | 0 / 386 / 0 | 1 / 383 / 0 |

현재 floor kernel은 첫 블록의 homogeneous age에 대해 h=1을 사용한다. 따라서 저장된 더 세밀한 R10 cap과 비교한 raw 수치는 위 표처럼 커질 수 있다. Capped는 같은 clock·point/닫힌 셀의 인증 상계와 교차한 결과다. Raw의 보편적 우위를 주장하지 않는다.

## 닫힌 셀에서 관찰된 제한된 개선

| 사례 | 개선한 E 셀 수 / 192 | 최대 whole-E 개선율 | 최대가 발생한 셀 (0-based) |
|---|---:|---:|---:|
| 무반응 2상태 | 0 / 192 | 0% | — |
| 비선형 2상태 | 166 / 192 | 0.000300669129102% | 191 |
| coarse source defect 2상태 | 172 / 192 | 0.00032721650671% | 191 |
| native9 K + 합성 조건부 반응 | 0 / 192 | 0% | — |

세 반응 사례의 첫 R whole-cell 값에는 dyadic128의 1 ulp, 즉 정확히 2^-128만큼의 감소가 하나씩 있다. 이는 반올림 수준의 차이다. 비선형 및 coarse-defect 사례의 작은 E whole-cell 개선은 위 셀들에 한정된다. Native9 E whole 및 모든 capped endpoint는 R10과 정확히 같다.

## Fresh forcing·블록 경계 판별

`q=0` late-forcing control에서 마지막 셀의 새 forcing은 h0=1로 들어가 final R=1/8, E=1/128을 얻었다. q를 새 forcing에 미리 곱하는 방식과 구별된다. Block-jump control의 닫힌 셀 R upper는 1이고 그 오른쪽 endpoint upper는 1/2다. 셀의 오른쪽 끝점에 왼쪽에서 접근한 극한을 whole-cell 인증에 포함했다.

## 저장 sample과 허용오차

독립 reference의 저장 sample 비교 3,088성분은 기존 `atol=2e-12`, `rtol=2e-10` 기준을 통과했다. 전체 strict containment는 false이며, 저장 sample이 upper를 조금 넘는 성분은 349개다. 저장 sample은 cap으로 사용하지 않았다.

R11의 Decimal 비교에서 최대 초과는 무반응 capped R의 index23에서 `4.001332174731647…e-12`, 해당 tolerance는 `4.377656370786352e-11`이다. 이는 저장된 decimal sample과 exact rational upper의 비교다. R10의 원래 binary-float 후처리 기록 `4.0013206434938575e-12`는 그대로 보존한다. 두 수치는 표현과 비교 정밀도가 다른 readout이며, 기존 허용오차를 바꾸지 않았다.

## 그림과 출처

- `figures/BOUND_ENDPOINTS.png`: endpoint 값의 연결선은 시각적 안내다. 중간 시각의 인증은 연결선에서 얻지 않는다.
- `figures/WHOLE_CELL_CERTIFICATES.png`: 각 step 높이는 정확한 닫힌 셀 전체의 인증 upper다. 공유 endpoint에는 양쪽 셀의 인증이 적용된다.
- `figures/KERNEL_CONTROL_DIAGNOSTICS.png`: full-A block age, fresh forcing, left-limit control 및 작은 whole-E 차이를 표시한다.
- 정확한 수치·비교 count·source SHA는 `analysis/SAVED_OUTPUT_SUMMARY.json`, 재생산 코드는 `analysis/plot_saved_results.py`에 있다.

Native9는 native K와 synthetic conditional reaction fixture의 조합이다. 실제 HD reactive array 및 named physical consumer/density/clock은 INPUT_PENDING이다. E=abs(eta), coarse l1=4E를 유지하고, raw lower는 chosen-q ideal comparison의 lower다. HH_R10=OFF, production=NOT_ISSUED, L4=false, physical/central delta=0이며, native v=UNSPECIFIED·MISSING_NOT_ZERO·TIQM/SQM 구별을 유지한다.
