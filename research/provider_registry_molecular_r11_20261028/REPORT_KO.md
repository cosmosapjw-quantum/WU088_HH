# WU088_HH R11 종료 보고서

**Full-A uniform finite-block certificate와 forcing convolution 연구를 이론 R1–R10, 코딩 C1–C10의20/20 단위로 완료했다. 과학 DAG는23/38이며 기존36개 노드 객체는 변경하지 않았다. 새 이론·코드 노드 각1개만 조건부 채택했다.**

기존 R10의 후속 후보였던 Duhamel 상한을 모든 시작시각·전체 허용 family에서 증명했고, positive minorization을 더해 strict full-A block 인증을 구성했다. 현재 저장된 네 사례에서 capped endpoint는 R10과1544성분 전부 정확히 같으며 최종 추가 개선은0%다. 이론·구현 의무의 해결과 수치 상계의 개선을 구별한다.

Actual HD reactive array와 named physical consumer/density/clock은 INPUT_PENDING이다. HH_R10=OFF, production=NOT_ISSUED, L4=false, central/physical delta0을 유지한다.

## 1. 권위와 고정 상태

- Repository: cosmosapjw-quantum/WU088_HH.
- Branch: research/provider-registry-20261025.
- Draft PR: https://github.com/cosmosapjw-quantum/WU088_HH/pull/150 .
- R11 leaf: research/provider_registry_molecular_r11_20261028/ .
- 시작 R10 FINAL commit: c92e63787ed7f6b50cbec06dd0b8dd2a00ace518 .
- 시작 R10 FINAL tree: 56f0c7b558ac24e683a8b95713b3cbc068f1f38b .
- R11 과학 S09 commit: e1db71bade6ff94959a74d8f297ad2568c247056 .
- R11 과학 S09 tree: 9c4108ffa1fc8a4c4489bd6be19a93183cc25133 .
- R11 scientific payload: **50 files**, SHA-256 **e7e345e26142522394bc1e7b3eeccfaacf5347cf4f802bcfd344f9fbbcbfdae0**.
- 고정 C9: PASS_SCOPED_FINAL_C9, 열린 중대 지적0; SHA-256 538bc823b6aabd776abe7b2ee52a8d1c3dedb52c47786f6f31dd3d1badbf2e94.
- Admission delta: PASS_SCOPED_ADMISSION_METADATA_DELTA, 열린 중대 지적0.
- 실행 전 동결18/18 파일 일치. S09 원격 Git tree의 과학50개 blob SHA·size도 실제 바이트와 모두 일치.

R10 과학 S09 a2c62aaad2396d1720a12e74774e52374baa4c33 및41-file payload57ee9ad49afbd1a492914fadba480ed787b51e4bcefc8c0be62c31e196590fff는 보존했다. Scientific manifest/admission, workflow/DAG, 전달 receipt는 별도 권위다. 자기 참조를 피하려고 manifest/admission/DAG와 이후 admission delta는50-file payload에서 제외한다.

## 2. 전제와 직접 증명

고정 열보존 Metzler K, 고정 확률벡터 pi, 고정 비음수 destruction d에 대해 H=pi*d^T-diag(d), A_w(t)=K+w(t)H를 쓴다. 모든 가측 w 경로가 인증된 같은0<=m_w<=w<=M_w box에 속한다. K/pi/d를 한 sample이나 endpoint에서만 고정한 것으로 바꾸지 않는다.

U_w(t,s)는 양의 column-stochastic propagator이고 l1 유도노름은1이다. Z=ker(1^T)에서 rho를 정의하면 ordered Duhamel 식은

    U_w(t,s)-exp(K(t-s))
      = integral_s^t U_w(t,u) w(u) H exp(K(u-s)) du

다. 두 propagator의 Markov l1 nonexpansiveness로 모든 시작 s에서

    rho(U_w(s+tau,s)) <= q_add
    q_add = min(1, q_K + tau*M_w*||H||_1)

을 얻었다. 이 식은 R11에서 새로 증명·구현·심사했다. R10에 소급 채택하지 않는다.

b_H=max_j d_j(1-pi_j)=||H||_1/2이면 H+b_H I>=0이다. A_w+b_H w I>=K의 positive propagator 비교로

    U_w(s+tau,s) >= exp(-b_H*integral_s^(s+tau) w(u)du) exp(K*tau)

를 얻는다. 공통 stochastic 성분을 분리하면

    q_minor = 1-exp(-b_H*M_w*tau)*(1-q_K)

가 full-A block 상계다. q_K<1과 유한 b_H*M_w*tau이면 수학적으로 q_minor<1이다. 구현은 exp lower와 directed rounding으로 q upper를 만들고 저장 rational q<1 여부를 따로 판정한다. Nominal K rho를 full A로 직접 옮기는 과정은 없다.

Duhamel, Dobrushin 및 geometric-block convolution은 선행 문헌의 방법이다. [Mitrophanov2005 원전](https://files.ele-math.com/articles/mia-08-15.pdf)의 Theorem2.1·3.1과 [Gaubert–Qu 원전](https://arxiv.org/pdf/1307.4649)을 읽고 열 관례·전체 measurable family·현재 source binding에 맞게 직접 유도했다. 일반 정리의 신규 우선권이나 sharpness를 주장하지 않는다. 정식 증명은 [PROOF_KO.md](https://github.com/cosmosapjw-quantum/WU088_HH/blob/e1db71bade6ff94959a74d8f297ad2568c247056/research/provider_registry_molecular_r11_20261028/theory/PROOF_KO.md)에 있다.

## 3. Forcing, 정확한 clock와 닫힌 셀

모든 시작시각의 q 인증을 합성하여 h(u)=q^floor(u/tau), h(0)=1을 얻는다. R=||r||_1, E=abs(eta), coarse l1=4E를 유지한다. Residual forcing은 zero-mass이며 같은 whole-fine-domain에서 g_r로, scalar forcing은 같은 whole-fine/coarse-domain에서 c>=0, signed d_c, g_e로 제한된다.

    R(t) <= h(t-t0)R0 + integral_t0^t h(t-u)g_r(u)du.

Fresh forcing의 나이는 t-u다. 새 forcing에 초기 residual의 전체 나이 또는 q를 미리 곱하지 않는다. Exact t0=0, delta와 tau=m*delta를 유지한다. 현재 유한 API는 exact uniform grid와 셀별 constant forcing, sweep 안의 고정 c,d_c를 구현한다.

    h_n=q^floor(n/m)
    F_n=delta*sum_(j=0)^(n-1) h_(n-1-j) g_r,j
    R_n=h_n*R0+F_n.

셀 내부 upper는 L_n=h_nR0+F_n와 V_n=h_nR0+F_(n+1) 사이의 affine 식이다. V_n은 셀의 오른쪽 끝점에 왼쪽에서 접근한 극한이므로 whole-cell upper에서 빠뜨리지 않는다. E endpoint는 affine R을 양의 Bernstein moments W0,W1로 적분하고, whole E는 같은 셀의 Rwhole로 scalar comparison을 수행한다. Signed d_c와 zero/near-zero 경우를 모두 포함한다.

R10 cap은 같은 source SHA·JSON pointer·상태 순서·family·정확한 clock·delta·닫힌 셀의 upper일 때만 교차한다. Point와 whole cap을 섞지 않고 전역 R forcing memory를 reset하지 않는다. Array metadata만으로 scientific premise가 참이라고 가정하지 않는다. 실제 저장 원문과 원래 인증을 함께 결속했다.

수치 구현 범위는 state1..13, cells1..192, block_steps1..192, exact scalar8192bits, dyadic128/Taylor96, scaled exponential argument 절댓값<=16이다. Reference는 생산 코드를 import하지 않고 exact Fraction convolution 및 Decimal160 closed forms를 사용한다. 실행 전 고정 guard는1e-80 relative다. 세부 계약은 CONTRACT.json과 theory/THEOREM_AND_API_KO.md에 있다.

## 4. 실제 수치 결과

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


## 5. 새 실행 예산, 심사와 첫 실패 기록

Primary1회60CPU/90wall, reference1회60CPU/90wall, CAS1회30wall 계약을 실행 전에 고정했다. Primary214/214, reference900/900과19,195components에서 실패0이다. 구성은 exact11,239, Decimal4,868, saved sample3,088이며 서로 다른 물리 시나리오 수가 아니다.

두 과학 Python process의 import/serialization 포함 OS CPU는0.796703+0.680732=1.477435초다. 관리·plotting과 remote CAS CPU 또는 전체 역사 CPU는 이 합계가 아니다. R11 remaining0/0/0, R10/R9/R8/R7/R6/PHYS91 allowance 증가0, global remaining/full historical CPU=null이다. 새 ODE, native exponential, 이전 scientific replay는 모두0이다.

독립 reviewer는 proof/production/reference 저자와 별개로 한 번의 bounded R6/C9 pass를 이어갔다. F01은 float cap-cell 수를 거부하도록 실행 전에 교정했고 실제 guard가 통과했다. F02는 left-limit 접근 방향 문장을 교정했다. 둘 다 과학 실패 실행을 일으키지 않았다.

첫 PNG 절단 바이트와 원인 NOT_ESTABLISHED를 보존했고, 저장 결과만으로 atomic save 후 정상 PNG/SVG를 만들었다. 잔류 temporary PNG가 S08에 포함된 사실도 보존하고 S09에서 원격 경로를 실제 삭제했다. 최종6그림/과학파일의 변화는0이다. 마지막 source/admission delta는 별도 reviews/ADMISSION_DELTA_REVIEW.json에 기록하여 고정 C9 hash를 바꾸지 않았다.

CAS는15zero residual과 all_zero=True를 반환했지만 Power::infy3개 및 General::messages 경고가 있다. 원인은 NOT_ESTABLISHED다. 동결 코드에 전송 LF1개가 추가된 actual submission도 별도 저장했다. 판정은 QUALIFIED_SYMBOLIC_CORROBORATION이며, 전체 family 정리는 해석적 증명으로 지지한다.

## 6. 바뀐 의존성과 실제 도구 사용

지정7refs를2026-10-28 12:04:08 KST에 확인해3이동/4불변, GET오류0을 얻었다. Immutable10파일과 CR PR112 본문을 읽었으며 저장 종료는12:06:12 KST다. Immutable10개 모두 Git blob과 일치했다.

| 의존성 | 이번 관찰 | WU에 대한 의미 |
|---|---|---|
| REI central 3d8bcdb79a70… | HE HARMONIC10와 CR scoped return 반영, central28/88 | WU physical admission 변화0 |
| REI thermal 66878795aa14… | 10/20, C5 AUTHORED_NOT_EXECUTION_VERIFIED, actual runs0 | 실제 WU HD consumer 미공급 |
| CR 729cb9516469… | 수행20/20, stage dual R2 20개; scientific406783036c26… | conditional event-union consumer 범위 유지 |
| BASS f834101d3292… | 그대로18/20, 독립R6/C9 미완 | 새 완료로 승격하지 않음 |
| REC/Vigil/HE 지정refs | 불변 | 이전 근거 재사용 |

CR의 actual exclusive/Ccross/outside response/donor work/EOS/T/full-source physical native25는 원문에서 여전히null이다. CR consumer를 WU physical binding으로 올리지 않는다. 이번 확인 범위에서 실제 새 HD reactive array나 named WU physical consumer는 관찰되지 않았다. 전역 자료 부재의 주장은 아니다. Immutable 링크는 authority/intake/SYNTHESIS_KO.md에 있다.

SciSpace에서는 HD 문헌 locator와 Markov perturbation 문헌을 각각 실제 검색했다. Exa에서는 HD 검색2회·publisher 원문fetch1회, Markov 검색1회·원전2개 batch fetch1회를 수행했다. González-Lezana–Hily-Blant–Faure2022 DOI10.1063/5.0128598의 reactive SQM supplement와 nonreactive EMAA 안내를 구별했다. Actual reactive array bytes는 확보되지 않았지만 접근 실패를 자료 부재로 바꾸지 않았다. Wolfram context 조회와 신규 evaluator1회는15개 항등식 확인에 실제 사용했다.

최초 census51repos/2375heads/65pages(공개35/1892, 비공개16/483), Dropbox관련하위5193terminal, Drive과거ZIP1000cap부분목록, 첨부20개SHA/size 재사용, personal-context unavailable로다른대화원문0건이라는 이전 조사 범위를 보존한다. 이번에 전수 조사를 반복하지 않았다. 비공개 저장소는 집계만 공개한다.

## 7. 과거 과학 기록의 보존

R10 primary175/175, reference469/469,9860components,OSCPU0.511886초와 동결14/14, C9 PASS_SCOPED_FINAL_C9를 유지한다. R10의2state nonlinear 최종 capped 개선R11.1976266%,E23.2473241%는 원래 비교 기준의 기록이며 R11의 추가 개선이 아니다.

R10 Native9 instantaneous lambda(K)=0, lambda(full A)=2.085393203227482e-7과 raw가R9보다endpoint381/whole380성분에서 컸던 사실을 보존한다. R10 capped finalR동일/E0.006596392256% 개선이라는 원래 비교도 바꾸지 않는다.

R8 original reference726/727PASS+1FAIL, 별도 exactphi24/24, R10 최초 후처리 ID 실패와 DOC01/META02 종결은 원래 source에 남아 있다. R10 CAS의 Infinity/Power/General 경고, 원인 NOT_ESTABLISHED, QUALIFIED_SYMBOLIC_CORROBORATION과 원래 sample readout은 그대로다.

현재 local 입력을 복구하기 위해 R10 FINAL ZIP을 Drive에서 실제 GET하고 원래1786833bytes/SHA68b4dffac379360943442c5b5cd93e4874e030aa7053273b4caeb8ffabaaea6d 및119source members를 확인했다. 이것은 R11의 source recovery다. R10 당시 provider original GET=NOT_RUN 기록을 소급 변경하지 않는다.

## 8. 실제 게시·이중 백업

아래는 이 source 작성 시점까지 실제 완료된 **10/10 단계**다. Workflow20/20과 전달 완료는 별도로 센다.

| 단계 | workflow | 과학 DAG | source commit | ZIP bytes | 검증 |
|---|---:|---:|---|---:|---|
| S01 | 2/20 | 21/38 | 1603f2a26e82 | 1,958,933 | 양쪽 actual ACK·size MATCH |
| S02 | 4/20 | 21/38 | 1ba7a7d023ba | 1,964,793 | 양쪽 actual ACK·size MATCH |
| S03 | 6/20 | 21/38 | 0a845ee71daa | 1,971,727 | 양쪽 actual ACK·size MATCH |
| S04 | 8/20 | 21/38 | 8b87c5c4bf85 | 1,980,927 | 양쪽 actual ACK·size MATCH |
| S05 | 10/20 | 21/38 | 41d4f8a6ce39 | 2,026,673 | 양쪽 actual ACK·size MATCH |
| S06 | 12/20 | 21/38 | 149d73a0c1cf | 2,303,931 | 양쪽 actual ACK·size MATCH |
| S07 | 14/20 | 21/38 | ed8f21a30824 | 2,328,981 | 양쪽 actual ACK·size MATCH |
| S08 | 16/20 | 21/38 | f98770947a4b | 3,764,225 | 양쪽 actual ACK·size MATCH |
| S09 | 18/20 | 23/38 | e1db71bade6f | 3,725,863 | 양쪽 actual ACK·size MATCH |
| S10 | 20/20 | 23/38 | 02bcab3a457a | 3,758,651 | 양쪽 actual ACK·size MATCH |

이 source에는 S01–S10의 실제 영수증이 모두 포함된다. FINAL 자신의 commit/tree/ZIP SHA·bytes·양쪽 ACK는 이 source 밖의 PR150과 종료 응답에 둔다. 이 문서는 FINAL 자신의 사후 영수증을 선행하여 인증하지 않는다.

검증 수준은 각 로컬 ZIP CRC·모든 member SHA-256, Drive와 Dropbox 실제 provider ACK 및 양쪽 크기 일치다. R11 stage/FINAL provider original GET은 NOT_RUN이다. 상세 ID/URL/ZIP SHA는 delivery/PUBLICATION_INDEX.json과 개별 receipt에 있다.

## 9. 다음 대화

AGENTS.md 최신 entry, REPORT와 HANDOFF, SCIENTIFIC_ADMISSION/MANIFEST, DAG/WORKFLOW/LEDGER, C9와 ADMISSION_DELTA, authority/closeout_delta/CLOSEOUT_SUMMARY_KO.md, followup/NEXT_INPUT_CONTRACT.json, PUBLICATION_INDEX, PR150의 최신 FINAL 외부 영수증을 읽는다.

실제 HD reactive array 또는 physical consumer가 공급되면 같은 source family/state ordering/units/initial invariants/clock/density/whole-domain forcing과 먼저 결속한다. Native v=UNSPECIFIED, MISSING_NOT_ZERO, TIQM/SQM 구별은 공급 근거 없이 변경하지 않는다.

추가 연구가 필요하면 정확한 비정렬 셀과 forcing 주입 breakpoint를 분할하는 별도 유한 proof/code/resource 계약을 먼저 작성한다. 이것은 R11에서 실행·채택한 결과가 아니며 새 allowance는0이다. 완료한 R11 및 기존 과학·ODE·독립 심사를 재개 절차로 반복하지 않는다.
