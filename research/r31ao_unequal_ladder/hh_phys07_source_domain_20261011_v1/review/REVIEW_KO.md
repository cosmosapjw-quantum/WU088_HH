# WU088_HH PHYS07 독립 최종 검토

**판정: `PROMOTE_SCOPED`.** 고정된 수학적 reference family에 관한 P07-01–05와, 별도의 매끄러운 source-rate 전개에 관한 P07-07을 명시된 범위에서 승격한다. P07-06의 유한 gas-energy 상호작용 부호, P07-08의 native 동일성·실제 root/mixed 값, P07-09의 carried second-half·paired defect·시간 및 continuum 결과는 `OPEN/HOLD`로 유지한다. 다음 단계는 패키지의 reference 결과 보고와, handoff에 한정된 새 NCP source 작업이다.

## 1. 독립성, 동결 및 증거 범위

검토자는 `/root/phys07_decision`이며 후보 코드·이론·테스트를 작성하거나 수정하지 않았다. 생성자가 보존한 첫 실행의 결과를 읽고, 원 소스와 port의 의미, 구간 알고리즘, 수학적 논증, 실행 범위와 handoff를 독립적으로 검토했다. 검토 중 과학 실행, 과학 재실행, 새 테스트 작성, nonlinear root 계산, 재귀 reviewer 호출은 모두 0이다. 검토자가 작성한 파일은 `review/DECISION.json`과 이 문서뿐이다.

동결 manifest는 `CANDIDATE_SHA256.json`이며 SHA256은 다음과 같다.

`de4465061b6c04e5b3a18da03c541d8af32019c5ca2ec59499e192470e8c66c9`

2026-10-11 01:46:51 UTC에 manifest 자체의 hash와 150개 고정 파일의 크기·SHA256을 확인했고 불일치는 없었다. 이는 bytes에 관한 검증이다. 큰 source export의 모든 유리수 endpoint를 사람이 한 줄씩 다시 읽었다는 뜻은 아니다. 구현과 이론·계약·보고·handoff의 본문, 실행 기록 및 주요 구조화 수치와 포함 부등식을 검토했고, 전체 파일의 bytes는 별도로 결박했다. 구체적인 읽기 범위와 개별 identity는 `DECISION.json`에 기록했다.

Astra v4 phase 08의 실제 비생성자 판정 요건에 따라 증거, 수학·물리적 타당성, 신규성, 검증 가능성, 강건성, 실행 가능성, 가정, 원래 동기를 각각 평가했다. 합산 점수는 사용하지 않았다. 이 평가는 보존된 모델과 source snapshot 내부의 결과에 관한 것이며, 원자 fit의 새 문헌 검증이나 proof assistant에 의한 형식 검증을 뜻하지 않는다.

## 2. Claim별 판정

| Claim | 판정 | 인정 범위와 한계 |
|---|---|---|
| P07-01 | PROMOTE | 고정 reference leaf 및 계수 vector에 대해 전체 연구 box를 포함하는 열린 실수 C² source chart. Native runtime guard의 실행 범위를 넓히는 권한은 아니다. |
| P07-02 | PROMOTE | 같은 archived COMMON point에서 출발한 full 및 first-half stage의 whole-box/centre residual, signed Jacobian, Hessian 포함. Native source tuple과의 동일성은 별도다. |
| P07-03 | PROMOTE | 활성 저잉여에너지 photo는 열에너지 변수 (w)를 늘리면서 (T)를 낮추고 HH도 (T)를 낮추는 source 방향. 전체 trajectory의 순변화를 주장하지 않는다. |
| P07-04 | PROMOTE | 각 고정 계수 vector 및 모든 (	hetain[0,1]^2)에 대해 (X) 안의 유일한 reference root와 C² parameter family. (X) 바깥의 전역 유일성은 미판정이다. |
| P07-05 | PROMOTE | 두 reference first-stage family에서 uniform (W_x<0, W_w>0, W_T>0) 및 같은 유한 unit-square interaction 부호. |
| P07-06 | OPEN/HOLD | 유한 gas-energy interaction 포함이 두 stage 모두 0을 포함한다. 실제 부호, 영값 또는 부호 변화는 결정하지 못했다. |
| P07-07 | PROMOTE | 별도 smooth source-rate family의 formal cubic 계수와 leading (x/e) 부호. Native f64 time chart의 미분이나 finite-step remainder 인증은 아니다. |
| P07-08 | OPEN/HOLD | Native libm·direction·stored CommonFamily input·PreBE tuple 동일성 및 실제 native root/U/V/W/I. 값은 `null`이다. |
| P07-09 | OPEN/HOLD | 실제 first-half terminal joint carry를 받은 second-half, full/two-half defect, 시간 및 continuum remainder. |

근거는 `CLAIM_LEDGER.json`, `SCIENTIFIC_CONTRACT.md`, 두 이론 문서와 `results/SOURCE_ANALYSIS.json`이며, 원 소스 대응은 `inputs/SOURCE_PORT_LEAF_MAPPING.json` 및 보존된 `inputs/ncp_phys06/`에서 확인했다.

## 3. Source 의미와 열린 C² 영역

연구 box는

\[
X=[0.90,0.93]\times[0.29,0.31]\times[0.59,0.61]\times[13,14],
\qquad \Theta=[0,1]^2
\]

이고 (g=(x_{\mathrm{HII}},y_{\mathrm{HeII}},y_{\mathrm{HeIII}},w))다. Full (d=1.25\times10^9\,\mathrm{s}\), first-half (d=6.25\times10^8\,\mathrm{s}\)는 모두 동일 COMMON input에서 시작한다.

Reference transport는 고정 isotropic Hubble geometry의 해석적 redshift를 사용한다. 원래 directional point stock의 정확한 합과 선언한 scalar leaf를 사용하며, 초월함수 포함의 양 endpoint가 동일한 binary64 값으로 반올림되는지를 통해 reference leaf를 정한다. 이 구조를 실제 Rust libm 결과, qhat 계산, 넓어진 angular weight, stored CommonFamily interval stock 또는 native PreBE와 동일하다고 바꾸어 읽어서는 안 된다. `intervalNbar`는 하나의 고정 vector를 포함하는 계수 box다. 정리는 이 box에 속한 **각 vector를 parameter rectangle 전체에서 동일하게 고정**해 적용한다. 네 corner마다 다른 계수를 선택하는 family는 인정 범위가 아니다.

FT03의 \(\hat f=\operatorname{exact}(n_{\rm He})/\operatorname{exact}(n_{\rm H})\)와 stage의 저장된 (f)를 구별했고, (J_{\rm norm}) 및 source의 heat leaf 계산 순서를 보존했다. Paired blanket 역시 `fl(FHE*(1±8*EPSILON))`의 반올림된 endpoint를 뜻한다. 부호가 있는 Jet derivative를 photon primal의 nonnegativity와 혼동해 잘라내지 않았다.

\[
p=1+\hat f+x+\hat f(y_1+2y_2),\qquad T=Cw/p
\]

에서 (p,w>0), strict simplex, elimination denominator의 양성 및 source temperature 범위가 열린 바깥 box에서 유지된다. 연구 box의 온도는 약 (4.6997\times10^4)–(5.1453\times10^4\,\mathrm{K})이며, 문서의 바깥 영역도 HH의 (35000<T<60000\,\mathrm{K}) 내부에 있다. Geometry와 threshold branch는 parameter 변화 동안 고정되어 있다. 이 조건은 고정 leaf의 실수 공식에 대한 열린 C² 연장을 뒷받침한다. Runtime의 ([0,1]^2) gate와 mathematical extension은 역할이 다르며, binary64 산술 자체가 매끄럽다고 가정하지 않는다. 관련 도출은 `theory/SOURCE_C2_DOMAIN_KO.md`, 실제 조건은 `results/SOURCE_ANALYSIS.json`에 있다.

## 4. 구간 및 implicit-root 논증

`src/certified_interval.py`의 exact rational outward 연산, 112 significand-bit 반올림, exp/log의 명시적 tail과 정수 square-root bracket를 검토했다. Signed gradient와 Hessian의 곱·합성 공식은 원 source의 미분을 포함한다. Primitive 첫 실행의 324개 assertion과 8개 의도된 rejection은 구현 증거다. 별도 Decimal 비교는 보조적인 수치 진단이며, 그것을 엄밀한 초월함수 oracle로 사용하지 않았다.

중심 (c=(183/200,3/10,3/5,27/2)), 반경 (r=(3/200,1/100,1/100,1/2)), (A=G_g), (Q=I-A)를 둔다. Whole source의 Jacobian과 centre source residual로 얻은

\[
\beta_i+\sum_j\operatorname{mag}(Q_{ij})r_j<r_i,
\qquad
\gamma=\max_i\frac{\sum_j\operatorname{mag}(Q_{ij})r_j}{r_i}<1
\]

은 (g\mapsto g-G(g,\theta))가 (X)를 strict interior로 보내는 contraction임을 보인다. 기록된 (gamma)는 full 약 0.00115318812, first-half 약 0.000577295870이며 모든 component margin은 양수다. 따라서 각 고정 ((\xi,\theta))에서 (X) 안의 root가 존재하고 유일하다. 열린 C² source와 nonsingular (A)에 대한 implicit function theorem을 적용하고, 국소 branch가 (X) 안의 유일성으로 일치함을 사용하면 parameter 경계를 포함한 C² reference family가 얻어진다. Nonlinear root iteration이나 corner 계산은 필요하지 않았고 실제로 실행하지 않았다.

생성자의 분석 코드는 네 Neumann 항과

\[
\frac{\gamma^4}{1-\gamma}\|s\|_r
\]

의 weighted tail을 함께 사용한다. (U=-A^{-1}G_\lambda), (V=-A^{-1}G_b) 및

\[
W=-A^{-1}\left(G_{\lambda b}+G_{g\lambda}V+G_{gb}U+G_{gg}[U,V]\right)
\]

를 구간으로 포함하며, mixed forcing의 모든 항이 들어 있다. 고정 (g)에서의 (G_{\lambda b}=0)은 root mixed derivative가 0이라는 의미가 아니다. Temperature에는 (T_gW+T_{gg}[U,V])가 필요하고 실제 계산에 포함됐다.

마지막으로 같은 고정 reference family의 관측량 (phi_d)에 대해

\[
\mathcal I_{\phi,d}=\phi_d(1,1)-\phi_d(1,0)-\phi_d(0,1)+\phi_d(0,0)
=\int_0^1\!\int_0^1\partial_{\lambda b}\phi_d\,db\,d\lambda
\]

이므로 uniform mixed 포함이 유한 interaction도 포함한다. 이는 discrete family의 정확한 항등식이며 parameter Taylor remainder를 생략한 근사가 아니다. 근 존재·매끄러움·적분의 논증과, 코드가 검사한 exact-rational 부등식의 역할을 분리해 인정했다. 상세 증거는 `diagnostics/analyze_source_exports.py`, `theory/REFERENCE_ROOT_THEOREM_KO.md`, `results/SOURCE_ANALYSIS.json`이다.

## 5. 인정되는 수치 결과와 물리 해석

다음은 정확한 endpoint를 바깥쪽으로 넓힌 이론 문서의 십진 포함값이다. 각 행은 uniform mixed derivative와 같은 unit-square 유한 interaction 모두의 포함이다. (lambda,b)는 무차원이다.

| 관측량 | Full reference stage | First-half reference stage |
|---|---|---|
| (x), fraction | ([-1.46553\times10^{-16},-4.61150\times10^{-17}]) | ([-1.83470\times10^{-17},-5.78948\times10^{-18}]) |
| (w), eV/H | ([4.22891\times10^{-16},1.37651\times10^{-15}]) | ([5.29916\times10^{-17},1.72269\times10^{-16}]) |
| (T), K | ([2.58591\times10^{-12},8.85376\times10^{-12}]) | ([3.24279\times10^{-13},1.10819\times10^{-12}]) |
| gas energy (e), eV/H | ([-1.57000\times10^{-15},7.49420\times10^{-16}]) | ([-1.96499\times10^{-16},9.35407\times10^{-17}]) |

자료: `theory/REFERENCE_ROOT_THEOREM_KO.md` §6–7 및 `results/SOURCE_ANALYSIS.json`. Gas energy는 열에너지와 이온화에너지의 합성 관측량이며, 전체 radiation/guard ledger를 뜻하지 않는다.

활성 photo의 최대 heat는 0.102 eV보다 작고 (w/p)는 6 eV보다 크다. 따라서 photo가 (w)를 올리더라도 입자 수 증가에 따른 냉각 효과가 열에너지 증가 효과를 이긴다. HH와 photo가 같은 neutral substrate를 소모하며 온도를 낮추는 방향은 음의 ionization interaction을 설명하는 source 수준 근거다. 독립적인 source directional witness와 실제 implicit reference (W) 포함은 서로 다른 논증이고, 이번 패키지는 이를 구분한다. 두 interval 표현의 overlap은 보조 진단이며 동일성 증명으로 사용하지 않았다.

(mathcal I_x<0)는 두 미래 작용을 함께 켠 효과가 각각의 변화량을 더한 예측보다 작음을 뜻한다. (mathcal I_T>0)는 결합 온도가 그 단순 가산 예측보다 높음을 뜻한다. 이를 절대 온도 증가나 전체 시간 진화의 heating으로 해석하지 않는다. (mathcal I_w>0)도 같은 가산 비교다. Energy 포함은 0을 가로지르므로 음의 leading coefficient만으로 유한 interaction을 음수로 확정할 수 없다.

특히 (x) interaction은 약 (10^{-16}) 규모다. 네 native endpoint를 실제 계산하여 차이를 관측했다는 증거가 없으며, 이 결과는 whole-domain 미분 포함과 정리에서 얻은 reference 결과다.

## 6. Formal cubic 및 수정된 finite birth leaf

독립 검토에서 finite-stage 문구의 실질적 정확도 문제가 발견됐다. Native/source 순서는 (M=\operatorname{exact}(\operatorname{fl}(dS_*)))를 먼저 만들기 때문에 일반적으로 (M=\operatorname{exact}(d)\operatorname{exact}(S_*))라는 등식은 성립하지 않는다. 생성자는 finite 식에 (B_d=M/\operatorname{exact}(d))를 사용하고 (N=\bar N+bM=\bar N+bdB_d)로 고쳤다. 원문·원 claim 및 correction을 `theory/corrections/BIRTH_LEAF_CORRECTION.json`과 snapshot에 보존했으며 코드·결과 변경과 과학 재실행은 0이다.

별도의 smooth source-rate family는 (B=S_*\delta_{j24})로 정의한다. 그 formal cubic에 대한

\[
\alpha_m=\frac{(m+1)(m+2)}{6m^2},\qquad
\beta_m=\frac{(m+1)(2m+1)}{6m^2}
\]

을 discrete perturbation recurrence로 독립 확인했다. (m=1)은 ((1,1)), (m=2)는 ((1/2,5/8))다. 이 형식적 계수와 source 방향의 부호는 인정하지만, 시간에 따른 f64 rounding chart를 미분하거나 formal 식으로 현재 유한 (d) remainder를 대신하지 않는다. 기존 photon primal과 COMMON history도 미래 switch가 꺼졌다고 사라지지 않는다.

두 추가 reviewer 지적도 동결 전에 해소됐다. Handoff의 inherited NCP 자료는 명시적인 `inputs/ncp_phys06/` 경로를 사용하여 현재 PHYS07 review와 구별한다. 정리 식 (6)의 우발적 carriage return은 문자 표현만 수정했고 최종 theorem SHA256은 `3813824e0a9bee383fa6a9048ab080d08ae7747ed8dde2cc253c4e99dba565a4`다. Paired blanket 및 이전 binary identity 문구의 수정 역시 `FAILURE_LOG.json`에 보존돼 있다.

## 7. 실제 실행 기록과 검토의 경계

| 생성자 최초 실행 | 결과 | 경과시간 | 최대 RSS | 의미 |
|---|---|---:|---:|---|
| `primitives_first` | exit 0, 324 assertions, 의도한 rejection 8 | 0.21620 s | 11,136 KiB | Rational interval/Jet primitive 진단 |
| `source_full_first` | exit 0 | 3.83699 s | 20,864 KiB | Full의 whole·centre 2회, reference provider 99 channels |
| `source_half_first` | exit 0 | 3.22962 s | 20,708 KiB | First-half의 whole·centre 2회, 고정 provider 결과 재사용 |
| `source_analysis_first` | exit 0, 122 assertions | 0.16605 s | 18,264 KiB | 저장된 source export만 사용하는 구간 산술 |

자료: 각 `evidence/*/EXECUTION.json`, 원 stdout 및 `RUN_LEDGER.json`. 제한은 primitive/analysis에 wall 30 s·address space 256 MiB, 각 source stage에 wall 45 s·384 MiB였다. 모두 제한 안에서 완료했고 bound input/code의 전후 hash가 일치한다. 새로운 과학 실패와 재실행은 없었다.

새 source reference 평가는 whole/centre 합계 4회다. Analysis 실행의 새 source callback·초월함수·nonlinear iteration은 0이다. Native endpoint, BEpoint, certificate/root producer, IVP, heavy atomic 및 과거 suite 호출은 Python dispatch와 source call graph 범위에서 0이며, 이 값을 native 계측기를 실행해 얻은 counter처럼 제시하지 않는다. 이전 NCP의 미계측 counter와 per-first-target binary hash는 `null`로 남는다. 나중의 최종 binary hash를 앞선 첫 target에 소급해 붙이지 않았다.

검토자가 동결 후 구조화 결과의 key를 표시할 때 `stages`를 dictionary로 오인한 읽기 전용 스크립트 1회가 `AttributeError`를 냈고 실제 list 형식으로 읽어 확인했다. 이는 candidate 변경이나 과학 실행을 수반하지 않았다. 생성자 쪽의 기존 orchestration 오류와 원 NCP build failure도 기록대로 유지한다.

## 8. 다음 NCP handoff 및 남은 판단

`handoff/NCP_LOCAL_CODEX_HANDOFF_KO.md`, `NCP_TASKS.json`, `NCP_RETURN_TEMPLATE.json`은 새 source 작업을 구체적으로 지정한다. 기준은 NCP head `65a36e255aa6d9911e23a9b5ced18d8a9f507606`, 새 branch는 `codex/hh-phys07-ncp-20261011`이다. 두 target `phys07_sourcebox_full_first`, `phys07_sourcebox_first_half_first`는 아직 실행되지 않은 새 작업이다.

각 stage는 PreBE 1회, whole·centre residual 각 1회, FT03/HH 각 2회, provider 198 channels를 넘지 않는다. 합계 ceiling은 PreBE 2, residual 4, FT03/HH 각각 4, provider 396이다. 기존 export만 쓰는 conditional root arithmetic은 stage당 최대 1회다. 이것은 nonlinear root producer나 native certificate 발급이 아니다. 새 mixed/finite producer나 기존 검증의 반복 실행도 허용된 새 작업에 들어 있지 않다.

NCP는 같은 source 호출에서 얻는 실제 leaf, geometry, native input history, PreBE binding 및 whole-box 포함을 기록해야 한다. Native/reference의 bit identity, interval inclusion, overlap 및 서로 다른 input scope를 구별해야 하며, 미계측 값은 `null`이어야 한다. Private permit/issuer를 만들거나 endpoint 호출로 우회하지 않는다. 이 계약은 현재의 native source gap을 다루기 위한 한정된 다음 단계로 충분하다.

패키지에는 재개에 필요한 input·source snapshot·harness·handoff가 포함돼 있다. 다만 이 판정 시점에는 이후 Git publication, detached receipt, Drive/Dropbox 실제 업로드 및 복구 행위를 검토하지 않았다. Receipt의 실제 commit/tree, archive hash, remote object/path는 실행 뒤의 관측값으로 채워져야 한다. 미래 전달 필드를 이미 확인된 완료 사실로 승인하지 않는다.

**남은 과학 범위는 분명하다.** Native source/input 동일성, 실제 native root/U/V/W/I, 실제 first-half terminal을 전달하는 second half, coupled full/two-half defect, 유한 gas-energy interaction 부호와 시간·continuum remainder는 미해결이다. 이번 독립 판정은 그 경계를 유지하면서 source-specific C², 전체 box의 reference source 미분 포함, uniform reference root, 그리고 유한 reference (x/w/T) 상호작용으로의 진전을 인정한다.
