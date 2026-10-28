# R10 정식 결과와 API

## 정리

Fine/coarse HD 공유 저장고 모형의 동일한 불변량과 whole-domain 비음수 box를 가정한다. K는 열합0 Metzler, pi는 simplex, d_i≥0이고, fixed-input 구현에서는 K,pi,d_i가 시간에 대해 고정된다. w(t)∈[m_w,M_w]다. q=Kpi−pi', branch distance 및 scalar coarse defect에 대한 원래 상계를 유지한다.

H=pi d^T−diag(d), A=K+wH는 보존적 Metzler다. Zero-sum l1 logarithmic norm은 −lambda(A)이며 lambda(A)=min_(i<j)[A_ij+A_ji+Σ_(k≠i,j)min(A_ki,A_kj)]다. 고정K,pi,d_i에서는 lambda_*=lambda(K+m_wH)가전체w구간의최소다. 원래fine-stateboxforcing g_r를그대로쓰면 R'≤−lambda_*R+g_r, E'≤cR+d_cE+g_e의상계가성립한다. E=|eta|이며coarse l1=4E다. 일반시간의존계열은같은uniformlambda와forcing증명을별도로갖추면이론을적용할수있다.

전체증명은 PROOF_KO.md에있다. 수치lower는idealcomparison해의lower이며실제오차의lower가아니다. Native9반응은조건부fixture이고실제물리consumeradmission은발행하지않았다.

## 생산 API

```python
generator_certificate(K, pi, destruction, w_box, *, binding)
flow_interval(lam, c, d, g_r, g_e, delta, *, whole=False,
              bits=128, degree=96)
sweep(K, pi, destruction, w_box, c, d, g_r, g_e, delta,
      initial, cells, *, binding, whole_caps=None, point_caps=None,
      bits=128, degree=96)
```

구현: src/full_generator_triangular.py. Python표준라이브러리Fraction과정수연산을쓴다. Float/bool을거부하고정확한유리수문자열·정수·Fraction을받는다. n=1..13,1..192cells,입력scalar8192bit,dyadic128/Taylor96,shiftedscaled∞norm≤16이구현영역이다. n=1의zero-sum공간은영벡터공간이고lambda=0을기록하는convention을쓴다.

Positive-shifted3x3양의급수에서각항내림/올림과tail을분리하고reciprocal음의지수enclosure를곱한다. Mplus의양의단조flow가whole-cell을덮는다. API는binding의필수항목/순서/clock을검사하고,고정runner는실제원본SHA와정확한JSONpointer의caps를대조한다. 외부box의과학적증명은caller의전제다.

Raw는endpoints_lower/endpoints_upper와whole_cells_upper를반환한다. Capped는R9동일영역의인증upper와min을취하고endpoints_lower=None을반환한다. Reference sample로caps를만들지않는다.

## 실제 검증과 수용

Primary175/175PASS,independent469/469PASS및9860componentcomparisons0fail이다. 두실행은각1회이며총OSCPU0.511886s다. Independentreference는productionimport없이exactEulercolumn-l1계수와Decimal160analyticflow를사용했다. 4HD×193endpoints와9analyticcontrols를검사했다. 15CASzero는실제Infinity/Power경고와함께QUALIFIED로보존했다. 처음postprocessingID실패와후속metadata교정도raw/reviews에보존한다.

Raw의보편적개선은수용기준이아니다. 고정2state사례에서개선했고, sparse native9 raw에는더큰성분이있다. Capped는모든1544endpoint성분·1536whole성분에서R9이하다. 연속시간과학보장은정리와whole-domain전제에의존하고, 저장표본비교는고정허용오차를적용한수치검사다.

## 과학 상태

새결과는특정가정아래derived+implementation-verified+numerically-checked로채택한다. 일반Dobrushin정리의신규성이나새strongno-go를주장하지않는다. 기존34DAGnode객체와원R8실패기록은그대로보존한다. 실제HDreactivearray/consumer/density/clock과L4는별개입력의무다.
