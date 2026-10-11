# PHYS11 독립 최종 검토

**판정: PROMOTE_SCOPED.** 검토자는 `/root/phys11_intake`이며, PHYS11에서는 Git·반환물 provenance intake만 수행했다. 후보 과학 유도, 코드, 검증 설계, 실행 배정 및 handoff 작성에는 관여하지 않았다. 이번 검토에서 후보를 변경하거나 재실행하지 않았으며 이 문서와 `review/DECISION.json`만 작성했다.

검토한 대상은 같은 고정 소스 계열의 첫 단계 33-group 광자 및 미래 ledger carry다. Full과 first_half는 같은 COMMON에서 각각 출발한다. Source inclusion과 같은 고정 계수 α의 C² root family는 기존 조건부 전제로 유지된다.

## 1. 동결 및 실제 실행 증거

- 최종 동결 manifest SHA256: `9137ddd2859c37698b4891f2d4015429f714745d1e9b22417ce16f14cb4517c4`.
- 최초 동결 177개 파일, 12,412,235 bytes의 실제 크기·SHA256를 확인했다. 최종 동결은 아래 additive 증거를 포함한 236개 파일, 13,157,225 bytes다.
- 기준 PHYS10 commit: `7a5eb687515aa29934de764d04fd7493f289ac24`; core subtree: `b7592637e565666ad92047b7ea25067a4d6bd34b`.
- `carry_v2`: 4.029582589995698 s, 최대 RSS 29,900 KiB, exit 0, timeout false. 실제 stdout은 저장된 SUMMARY와 byte 단위로 같다.
- 후보가 기록한 168 assertions / 8 semantic cases를 확인했다. Assertion 개수는 독립적인 과학 test 개수가 아니다.

최종 closeout 중 전달 완전성을 위해 이미 검증한 PHYS10 current_return의 원 NCP08/09 완료 기록 58개, 716,071 bytes가 inputs/prior_returns에 추가됐고 additive identity 기록 1개가 붙었다. 최초 177개 동결 manifest 행은 모두 그대로이며 owner의 추가 기록도 해당 원 bytes 불변을 명시한다. 이 같은 최종 검토에서 추가 59개 파일의 실제 SHA·크기를 확인하고, 그중 원 반환 58개는 기존 LOCAL_REUSE와 원 Git blob identity에 각각 대조했다. 과학 코드·입력·결과의 변경이나 과학 검산 반복은 없었다. 최종 decision은 이 236개 파일의 새 freeze에 결박한다. 최초 freeze SHA와 첫 review/decision binding의 SHA는 DECISION의 additive_completion_evidence_review에 보존했다.

첫 `carry_first`는 0.1667173830064712 s, RSS 19,728 KiB, exit 1이다. 실제 stderr는 old_gas full Jet를 bare interval로 읽어 발생한 `KeyError: lo_bits`를 보존한다. 최초 snapshot과 수정 코드를 비교하니 변경은 old_gas를 jread로 읽고 value를 선택하며 그 미래 partial들이 0임을 확인한 부분에 한정됐다. 입력·source leaf·정밀도·허용오차는 그대로다. 두 실행 각각 19개 pre/post binding과 원 snapshot, 로그 identity가 일치한다. 이는 구현 입력 형식의 수정이며 물리적 반례나 runtime 환경 실패가 아니다.

과학 실행은 최초 실패 한 번과 수정 성공 한 번이다. 성공 후 반복 성능시험을 하지 않았다. 후보 코드의 직접 읽기에서도 source/native root/inverse/과거 suite 호출 경로는 없었으며, 관련 새 호출 수 0과 일치한다.

## 2. 수학과 원 소스 대응

### 광자 quotient와 incoming carry

원 `phys04_reduced_residual`은 같은 captured leaves로 D=1+dΣκ, Nout=Nin/D, R=κNout를 구성한다. 따라서 Nout=Nin−dΣR가 같은 실수 함수의 항등식이다. κ는 gas 분율에 affine이고, λ,b에 대한 고정 단계의 c,nH,f,σ,d는 상수다. 코드에서 D의 mixed carry가 d κg W인 것은 이 구조에 맞다.

일반 소스의 전체 혼합미분은

\[
\mathcal D_{\lambda b}J=J_gW+J_{gg}[U,V]+J_{g\lambda}V+J_{gb}U+J_{\lambda b}.
\]

`joint_carry.total`은 이 다섯 항을 모두 유지한다. 저장 Hessian을 평균하거나 대칭화하지 않는다. Quotient의 식도

\[
(N/D)_{\lambda b}=N_{\lambda b}/D
-(N_\lambda D_b+N_bD_\lambda+ND_{\lambda b})/D^2
+2ND_\lambda D_b/D^3
\]

와 일치하며 두 incoming–denominator 교차항이 모두 들어 있다. 첫 단계의 구조적 Nin,λ=Nin,λb=0을 다음 단계에 재적용하지 않는 것도 명시돼 있다. 원 signed tails를 그대로 소비한 결과와 원 함수의 구조적 0을 구분한다.

일반 implicit 합성식 (20)은 Gg U+Gr rλ+Gλ=0을 b로 미분하면 얻어진다. 다음 4×4 식 (24)에는 W⁻, FN[Nλb], FgN[U⁺,Nb], FNg[Nλ,V⁺], hgV⁺가 모두 남는다. F가 incoming N에 선형이므로 FNN=0이고, photon 변수를 제거한 원 네 gas unknown을 유지하는 계산식도 정당하다. 이 유도는 실제 다음 단계의 가역성·source coverage를 새로 증명하지 않는다.

네 carry 성분은 ε²=η²=0인 혼합 jet 대수로 설명되며 mixed 슬롯에 1/2를 붙이지 않는다. 순수 λλ,bb가 저장되지 않았다는 이유로 실제 순수 이차 미분을 0이라고 선언하지 않는다. `(1+b)/(2−λ)` 사례는 두 incoming mixed 성분이 0이어도 다음 mixed와 finite interaction이 비영임을 검출한다. 이는 실제 HH history의 대용물이 아닌 적절한 합성 반례다.

### Ledger 정규화와 source-derived escape

원 photon 상태는 photons/H이므로 ΣEN은 eV/H다. κ는 s⁻¹, dR은 photons/H이고, HH event는 events/H, threshold 열과 thermal work는 eV/H다. 새 코드에 여분의 nH 나눗셈은 없다.

`ft03_interval_rhs`에서 fhat는 따로 capture한 nHe와 nH의 Jet quotient다. Photo stoichiometry의 fHe leaf와 구별해야 하며 후보는 이 차이를 Jnorm으로 보존한다. `coupled_primary::model`은 Ft03Model::controlled를 호출하고 density 두 필드만 바꾼다. controlled fixture의 threshold와 CHI의 원 literal 및 export bits를 대조했으며 세 값 모두 `402b3266051507a6`, `4038965f20504658`, `404b357928e0c9da`로 일치한다. 두 추가 source 파일은 원 NCP07 MANIFEST의 크기·SHA256와 대응한다.

따라서 Γ*=−ℓfhat Fnp는 이 exact-real 소스에서 RR binding·kinetic loss와 DR threshold·thermal loss의 합이다. 일반적인 (τ−χ)CI correction이 이번 controlled source에서 사라진다는 조건도 충족한다. 원 thermal domain에서 kinetic factor의 부호 논증은 HI/HeII slope와 HeI의 1.5−0.654>0을 사용하므로 타당하다. 값의 positivity가 signed U,V,W의 positivity를 뜻하지 않는 한계가 함께 적혀 있다.

증대 수지는

\[
\Delta e_g+\Delta e_\gamma+d\Gamma_*+2dH_{mean}w^+
=d\left[(\ell_f-\ell_{\widehat f})F^{np}+\sum_{ja}(heat_{ja}+\chi_a-E_j)R_{ja}\right]
\]

로 닫힌다. Source-defined escape를 구성할 때 nonphoto projection과 fhat를 사용했고, Jnorm을 이중으로 더하지 않았다. HH binding gain과 threshold 열이 같은 χH로 상쇄된 뒤 남는 captured heat 표현 차이도 보존한다. 공통 항을 식에서 먼저 상쇄한 오른쪽에 미분을 적용하는 계산 방식이 적절하다.

같은 α의 C² family에 대한 단위 사각형 이중 기본정리를 통해 uniform mixed 포함을 finite interaction으로 옮길 수 있다. 서로 다른 α의 네 corner를 혼합하지 않으며, pointwise ratio를 적분한 값으로 finite ratio를 대체하지 않는다. 다음 단계의 이전 gas와 incoming mixed 항은 일반적으로 0이 아니므로 유지해야 한다.

### Native·angular 경계

공통 Dj를 갖는 실제 ray family에서는 합과 quotient 및 미분을 교환할 수 있다. 하지만 group 총량은 각 ray 분포를 유일하게 정하지 않는다. 같은 group 총량을 갖는 다른 angular 분포가 후속 ray-dependent transport에서 달라지는 반례는 적절하다. 현재 없는 4,224 ray/node와 128 guard payload를 생성했다고 주장하지 않는다.

Residual의 별도 captured-leaf 곱과 distribute helper의 fl(fl(σc)nH)는 서로 다른 scalar graph다. γ₂ 상계는 두 정상 범위 IEEE nearest 곱, finite 결과와 재결합 없음이라는 조건 아래의 값 차이만 감싼다. N=0에서는 절대 차이 0이며 상대 비율은 정의하지 않는다. 이 상계로 실제 native root·derivative·escape output을 인증하지 않는다.

## 3. 저장 결과의 독립 점검

후보 module을 import하거나 후보 diagnostic을 실행하지 않고 Python 표준 라이브러리 Fraction으로 저장 결과만 확인했다. 이 점검은 한 번 실행됐고 exit 0, 내부 경과 0.42781080199347343 s였으며 실패 항목은 없었다.

- 정확한 구간 1,860개에서 lo≤hi, 외향 binary64 포함, 표시 bits와 exact sign을 확인했다.
- 66개 group의 네 carry 성분, 총 264개 저장 교집합이 실제 두 식의 교집합과 일치했다. 각 value에는 원 source photon value의 추가 포함도 적용돼 있다. 모든 저장 denominator는 양수다.
- Absorption의 종별 합, HH threshold 열의 부호와 계수, thermal work의 2dH 계수, 증대 direct ledger의 저장 항 합을 확인했다.
- Early projected ledger가 direct 포함 및 normalization+capture의 분리 포함 안에 있고, 저장 intersection과 일치했다. 각 분리 interval 끝점이 early projection 끝점과 반드시 같다고 주장하지 않았다.
- 유한 상대 잔여 상계는 exact maxabs(augmented W)/(−gas W의 상한)와 일치했다.
- 두 stage 모두 historical HH/compensation과 primal ledger/energy compensation은 원 COMMON과 같다.

이 수량은 독립 점검의 coverage이며 새 과학 test case 수가 아니다. 원 8개 의미 사례나 완료한 source/gate 실행을 반복하지 않았다.

| 채택하는 결과 | Full | 같은 COMMON의 first_half |
|---|---:|---:|
| 엄격한 양의 photon mixed node | 24 | 24 |
| 엄격한 음의 photon mixed nodes | 16–23 | 16–23 |
| 나머지 zero-containing nodes | 24개 | 24개 |
| 증대 mixed/finite 잔여, eV/H | [−5.788230243389953e−40, 6.862357933552255e−39] | [−6.9733119029796365e−40, 8.2693439649913e−39] |

두 증대 잔여는 0을 포함한다. 정확히 0이거나 엄격히 양/음이라는 판정은 내리지 않는다. Raw JSON의 `residual_bound_reduction_vs_PHYS10`는 서로 다른 관측량의 잔여 크기를 비교하는 수치다. REPORT·수치 해석·handoff가 분명히 제한한 대로 정확도 개선, 시간 수렴, 실제 적분기 오차 또는 전역 보존의 근거로 쓰면 안 된다.

동결 PNG와 plot source도 확인했다. 부호가 다른 구간을 같은 signed-log 축에 표시하고, 같은 COMMON의 두 첫 단계임과 생략한 zero-containing 24개 node를 caption에 적었다. 통계 error bar로 오인하지 않도록 표시돼 있으며 현재 이미지에서 tick 겹침은 보이지 않는다. 두 번의 render는 같은 저장 output에 대한 layout 변경이고 과학 재실행이 아니다.

## 4. 최종 채택 범위와 전달

Source-aligned 33-group value/U/V/W, 미래 absorption/source/HH/thermal/escape* ledger, 증대 수지의 조건부 포함을 **derived / numerically checked / implementation-verified** 범위에서 채택한다. 여기서 implementation-verified는 Python exact-rational 후처리다. 일반·축약 next-stage composition과 angular lift는 명시한 전제하의 **derived** 결과로만 채택한다.

Creator의 `JOINT_CARRY_CLAIMS.json`에 남은 PENDING 표시는 동결 이전 author snapshot의 상태다. 최종 numeric·decision 상태는 이 검토와 실제 `carry_v2` 및 `review/DECISION.json`의 claim별 판정을 따른다. 이 사유로 동결된 원 저작 문서를 변경할 필요는 없다.

`NCP_TASKS.json`, `NEXT_DAG.json`, 실행 배정과 handoff는 실제 비용에 맞게 PHYS08/09/10을 재사용하고 PHYS11을 COMPLETE_HERE로 연결한다. 현재 heavy_queue=[]와 launch=false, 반환 NO_HEAVY_JOB_READY가 일관된다. 작은 missing payload, coefficient check와 완료 gate를 중량 작업으로 옮기지 않는다. 미래의 56 worker/112 GiB 상한과 600초/8 family 예시는 측정된 최적값이나 자동 실행 규칙이 아니다.

다음은 계속 열린 상태다: actual native root/U/V/W/I와 issuer binding, actual ray/guard 자료, scalar product graph 및 native escape derivative, 실제 carried second_half와 full/two-half defect, 실제 normalized history, time·continuum remainder, 전역 transport/guard/redshift/escape 수지, full49·production. PHYS07 reference energy, NCP07 node32 predicate 및 PHYS08 minsubnormal 예외도 보존한다. inherited 미계측 counter는 null이다.

**추가 과학 실행이나 재귀 검토 없이 이 후보의 review를 종료한다.** 이 판정은 정해진 source-family 범위의 사용을 허용하며 새로운 native authority나 다른 물리 scope를 만들지 않는다. 원 실패·snapshot·출력과 함께 seal 및 실제 전달 증거를 완결할 수 있다.
