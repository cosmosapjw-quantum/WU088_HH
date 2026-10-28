# R11 정리와 API

PROOF_KO.md의 T1–T10 연결은 fixed K/pi/destruction, 모든 가측 w∈[m_w,M_w], 모든 [s,s+tau]에서 성립한다. Native K-only tau/rho는 입력 identity를 확인한 원래 인증을 사용하고 fullA는 q_add/q_minor로 새로 인증한다. 현재 finite API는 exact origin0, uniformdelta, tau=m*delta, c/dfixed, same-grid piecewise forcing이다.

```python
generator_certificate(K, pi, destruction, w_box, tau, rho_K, *, binding, nominal_certificate)
bernstein_weights(d, delta)
convolution_sweep(q, c, d, g_r, g_e, delta, initial, cells, block_steps, *, binding, whole_caps=None, point_caps=None, bits=128, degree=96)
sweep(K, pi, destruction, w_box, tau, rho_K, c, d, g_r, g_e, delta, initial, cells, *, binding, nominal_certificate, whole_caps=None, point_caps=None, bits=128, degree=96)
```

`convolution_sweep`는 supplied full-propagator certificate를 전제로 한 산술 API이고 `sweep`가 실제 source-bound Kcertificate에서 fullA q를 구성한다. q0 control은 이 저수준 산술 계약을 검사한다. Exact int/Fraction/rational strings만 받고 float/bool을 거부한다. n1..13,cells1..192,m1..192,input8192bits,dyadic128,Taylor96,scaledexp≤16. Singleton은 R0=g_r=0이다.

반환 q는 유리수 outer upper, h는 freshforcingh0=1, rawendpointlower는 선택q의 idealcomparisonlower이다. wholecells는 leftlimit와signeddscalarcomparison을 포함한다. Capped는 actualR10sourceSHA/pointer/state/clock/grid의upper와 교차하고lower를반환하지않는다. 동일성검사 자체는 whole-domain물리전제를입증하지않는다.

재현명령과자원은 verification/EXECUTION_PLAN.json, 실제횟수/CPU는 EXECUTION_LEDGER.json, 실제채택은 SCIENTIFIC_ADMISSION.json 및 reviews/C9_FINAL_REVIEW.json이 결정한다.
