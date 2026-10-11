# WU088_HH PHYS07 — 실제 소스 영역과 참조 family의 유한 혼합응답

작성일: 2026-10-11. 이전 PHYS06 연구와 NCP PHYS06 반환을 이어 진행했다. 이 문서의 연구 결과는 함께 봉인된 실행 로그·정확한 유리수 endpoint·독립 판정에 연결된다. 출판 commit과 두 백업의 실제 파일 ID는 별도 `WU088_HH_PHYS07_DELIVERY_RECEIPT_20261011_v1.json`에서 확인한다.

## 1. 이번에 닫힌 것

이번 루프에서는 실제 FT03 + HH + reduced-photo 소스식에 맞는 열린 C² 영역을 만들고, 전체 상태 상자와 매개변수 사각형에서 잔차·Jacobian·Hessian을 계산했다. 그 포함값으로 선언된 **참조 first-stage family의 해 존재·상자 안 유일성·유한 혼합효과**까지 증명했다.

참조 family의 HH–광원 혼합효과는 수소 이온화율에서 음수, 열에너지 `w`와 온도 `T`에서 양수다. 에너지 좌표 `e`의 포함구간은 0을 가로질러 부호를 확정하지 않았다. 이 결과는 full stage 및 동일 COMMON 입력에서 출발한 first-half stage 각각에 적용된다.

여기서 참조 family는 원 소스의 반응식과 상수를 유지하되, **등방 팽창의 정확실수 transport chart와 올바른 반올림을 확정한 참조 scalar leaves**를 명시적으로 사용한 수학적 family다. NCP의 native 방향별 leaf, libm 결과, 실제 `Phys04PreBE` tuple 및 기존 `CommonFamily`의 stored interval 입력과 동일하다는 주장은 아직 없다. 실제 NCP root·mixed response·full/two-half 결함은 계속 미해결이다.

핵심 근거는 `results/SOURCE_ANALYSIS.json`, `theory/SOURCE_C2_DOMAIN_KO.md`, `theory/REFERENCE_ROOT_THEOREM_KO.md`, `review/DECISION.json`이다. 앞의 JSON에 있는 numerator/denominator 쌍이 엄밀한 endpoint다. 아래 수치 포함구간은 그 endpoint를 바깥 방향으로 넓힌 십진 표시다.

## 2. 이전 NCP 반환에서 이어받은 상태

| 항목 | 고정한 입력 |
|---|---|
| Repository | `cosmosapjw-quantum/WU088_HH` |
| 이전 연구 branch/head | `research/hh-phys06-energy-uniform-mixed-20261011`, `baf23360627bc1c6d10aac5317052f23edafd1b1` |
| 최신 NCP branch/head | `codex/hh-phys06-ncp-20261011`, `65a36e255aa6d9911e23a9b5ced18d8a9f507606` |
| NCP implementation core | `927019cff541e8a4a1f0d2c8846f1466d6b70533` |
| NCP source intake | 원본 82개 파일, 499,706 bytes; Git blob/size 대조 |
| COMMON seed SHA256 | `678f967f0d50ad1fff47a73e2e63193429b708246cd84ca8ffc72191c31b522b` |

NCP PHYS06는 energy projection, uniform contract/margin, mixed incoming chain, finite observable, paired difference의 여섯 신규 target을 첫 실행에서 통과했고, 독립 판정은 `APPROVE_SCOPED_IMPLEMENTATION`이었다. 그 실행 이력과 첫 build failure, 후속 수정은 원본대로 포함했다. 최종 gradient widening 뒤에는 build와 소스 포함 논증만 수행됐으며 **그 최종 binary에서 target을 다시 실행했다는 기록은 없다.** 개별 첫 target의 binary hash는 당시 별도 계측되지 않아 null이고, 최종 build hash를 그 실행들에 소급 할당하지 않았다.

따라서 이번 생산적 다음 단계는 generic adapter를 다시 만드는 일이 아니라, 실제 소스의 전체 영역 포함과 그 입력 의미론을 채우는 일이었다. `inputs/ncp_phys06/SOURCE_INTAKE_SUMMARY.json`과 `SOURCE_BOUNDARY_AND_CHART_KO.md`에 이 판단의 근거가 있다. NCP branch에 대응하는 PR은 intake의 head-filtered 조회에서 없었고, 이전 연구 PR #35와 혼동하지 않았다.

## 3. 무엇을 고정했는가

Gas 좌표와 매개변수는 다음과 같다.

\[
g=(x_{\mathrm{HII}},y_{\mathrm{HeII}},y_{\mathrm{HeIII}},w),\qquad
\theta=(\lambda,b)\in[0,1]^2.
\]

`w`는 수소 핵당 열에너지 eV/H다. `lambda`는 이후 HH 강도, `b`는 이후 광원 강도다. 두 값이 0이라고 해서 COMMON 상태에 이미 들어 있는 과거 HH ON 이력을 지우지 않는다.

\[
X=[0.90,0.93]\times[0.29,0.31]\times[0.59,0.61]\times[13,14].
\]

이 상자의 십진 endpoint는 정확한 유리수로 입력했다. 보관된 gas point
`(0.9131385026926517, 0.300035085528747, 0.5999927594007611, 13.565646600651332)`를 포함한다. Centre는 정확히 `(183/200, 3/10, 3/5, 27/2)`이고, centre에서의 잔차 평가도 `lambda,b` 전 영역을 포함한다.

시간은 `t0=1.6e11 s`, 고정 Hubble triplet은 `(1e-14,1e-14,1e-14) s^-1`다. 새 계산은 `d=1.25e9 s`인 full과 `d=6.25e8 s`인 first-half 두 경우다. **First-half는 two-half 전체 endpoint가 아니다.** 두 번째 half의 incoming gas/photon/guard 및 signed U/V/W carry는 이번에 만들지 않았다.

참조 transport는 보관된 방향별 binary64 photon stock의 정확한 합을 사용하고, 등방 chart의 `r=exp[-H(t1-t0)]`로 fixed-hat remap한다. `Nbar`의 각 interval은 이렇게 정해진 하나의 고정 계수 벡터를 감싼다. 네 parameter corner마다 서로 다른 `Nbar`를 선택하는 family를 주장하지 않는다.

고정 scalar leaf에서는 원 소스의 binary64 연산 순서를 유지한다. `nHe=fl(nH*f)`를 보존하고, 실제 온도에는 저장된 `nHe/nH`를 쓴다. `exp`, `sqrt`, `powf` 참조 leaf는 엄밀한 구간의 두 endpoint가 같은 binary64로 반올림될 때만 채택했다. 이는 native Rust libm과의 bitwise 일치를 자동으로 뜻하지 않는다.

유한 stage의 birth amount는 `M=exact(fl(d*S_*))`, `S_*=exact(5e-15)`다. 따라서 `N(b)=Nbar+b*M`이고, rate 표기를 쓰려면 `B_d=M/exact(d)`로 정의해야 한다. 독립 검토가 이 구별의 누락을 발견해 이론을 고쳤다. 원문과 수정 기록은 `theory/corrections/`에 남아 있으며 소스 코드와 계산 결과의 변경·재실행은 없었다.

## 4. 전체 상자의 온도와 C² 영역

\[
\widehat f=\frac{n_{\rm He}^{\rm stored}}{n_H^{\rm stored}},\quad
p=1+\widehat f+x+\widehat f(y_1+2y_2),\quad
T=\frac{2\epsilon_{\rm eV}}{3k_B}\frac{w}{p}.
\]

`p`의 단조성으로 온도 극값은 상자의 corner에서 정확하게 얻는다. 두 stage의 표시 온도 범위는 동일한 자리수로 나타나지만, 저장 밀도비의 정확한 유리수는 서로 다르다.

| 검증량 | 두 first-stage 참조 family에 유효한 보수적 포함 |
|---|---:|
| 주 상자 `X`의 온도 | `[46996.71044, 51452.88422] K` |
| HH lower guard까지의 여유 | `11996.71044 K` 초과 |
| HH upper guard까지의 여유 | `8547.11578 K` 초과 |
| Neutral H 최소 | `0.07` |
| Neutral He 최소 | `0.08` |
| 모든 reduced photon denominator | `D_j >= 1` |

열린 이웃은

\[
U=(.899,.931)\times(.289,.311)\times(.589,.611)\times(12.9,14.1)
\]

로 잡았다. 그 closure에서도 대략 `46607.99–51851.18 K`이며, 더 간단한 정확실수 논증으로 `46200<T<52372 K`가 성립한다. 따라서 FT03의 strict simplex, HH의 35–60 kK gate, 양의 `p`, `T`, opacity denominator를 모두 열린 영역에서 만족한다. 고정 leaf의 함수는 그곳에서 매끄러운 합성함수이고 특히 C²다.

고정 grid energy에서 Verner cutoff는 gas·`lambda,b`의 함수가 아니며, 고정 시간·geometry의 hat coefficient도 이 매개변수들에 대해서는 상수다. `lambda,b` endpoint에서의 미분은 같은 실수식을 작은 열린 영역으로 연장해 정의한다. 이 수학적 연장은 native 입력 guard를 우회해 음수 광자를 실행하는 절차가 아니다.

Energy 좌표 `e=w+chi_H*x+f*chi_HeI*y1+f*(chi_HeI+chi_HeII)*y2`를 쓸 때에는 gas 상자를 옮긴 평행체와 그 rectangle hull을 구분해야 한다. 기존 NCP `Domain.x[3]`는 thermal `w`를 뜻하므로 `e`를 그대로 넣어 검사하면 다른 영역을 검사하게 된다. 이번 결과는 gas 좌표의 원 상자를 유지한다.

## 5. 저에너지 광자가 열에너지를 올리면서 온도를 낮추는 이유

HH source와 HI photo source를 각각

\[
H=q(1,0,0,-\chi_H),\qquad
F_{\gamma j}=R_j(1,0,0,a_j),\quad a_j=\operatorname{fl}(E_j-\chi_H)
\]

로 쓰면

\[
DT[H]=-\frac{2\epsilon_{\rm eV}}{3k_B}
\frac{q(\chi_Hp+w)}{p^2}<0,
\]

\[
DT[F_{\gamma j}]=\frac{2\epsilon_{\rm eV}}{3k_B}
\frac{R_j(a_jp-w)}{p^2}.
\]

따라서 photo가 온도를 올리는 조건은 `a_j>w/p`다. 주입된 열뿐 아니라 새 전자와 이온으로 늘어난 입자 수를 함께 봐야 한다.

이번 참조 입력의 양의 photon stock과 birth는 13.7 eV 이하에 있다. 실제로 기여하는 HI 노드는 16–24이고, HeI/HeII photo channel은 모두 0이다. 활성 열 leaf의 정확한 차도 확인했다.

| 양 | 이번 상자의 범위 |
|---|---:|
| 활성 광자의 최대 excess energy | 약 `0.101565400298 eV` |
| 입자당 열에너지 `w/p` | `[6.0747947, 6.6507998] eV` |
| Full에서 photo의 thermal source | `[4.0026076e-15, 5.7231762e-15] eV/H/s` |
| Full에서 photo 방향 온도 변화 | `[-1.7409291e-9, -1.0820307e-9] K/s` |
| Full에서 HH 방향 온도 변화 | `[-1.8643685e-14, -5.8551019e-15] K/s` |

Photo는 `w`를 증가시키지만 입자 수 증가에 비하면 excess energy가 작아서 `T`는 내려간다. HH도 열에너지를 이온화에 사용하고 입자 수를 늘려 `T`를 낮춘다. 두 과정은 neutral H를 함께 소모하므로 서로의 반응률을 줄인다. 이 소스 방향의 부호는 독립적인 닫힌식과 이미 저장된 Jet의 조합에서 각각 확인했다. 그 두 구간의 overlap은 구현 점검이고, 항등식 자체의 근거는 직접 유도다.

## 6. 샘플링 없이 얻은 uniform reference root

\[
G(g,\theta)=g-g_0-dF(g,\theta),\quad A=G_g,\quad Q=I-A.
\]

Centre `c`와 radius `r=(.015,.01,.01,.5)`에 대해 `beta_i=mag[G_i(c,Theta)]`를 계산했다. 모든 성분에서

\[
\beta_i+\sum_j\operatorname{mag}(Q_{ij})r_j<r_i,
\quad
\gamma=\max_i\frac{\sum_j\operatorname{mag}(Q_{ij})r_j}{r_i}<1
\]

이므로 `g -> g-G(g,theta)`는 같은 닫힌 상자의 strict contraction이다. 각 고정 매개변수와 고정 참조 계수 벡터마다 상자 안에 유일한 해가 있고, 해는 내부에 있다. 위 C² 영역과 가역 Jacobian으로 implicit-function 정리를 적용하고 local chart들을 유일성으로 연결하면 `Theta` 전체의 같은 C² root family를 얻는다. 전체 물리 공간에서의 유일성을 주장하지 않는다.

| 검증량 | Full `d=1.25e9 s` | First-half `d=6.25e8 s` |
|---|---:|---:|
| Weighted contraction factor 상계 | `<0.001153189` | `<0.000577296` |
| `x` strict inclusion margin | `>0.013203889` | `>0.013171223` |
| `y1` strict inclusion margin | `>0.009964442` | `>0.009964678` |
| `y2` strict inclusion margin | `>0.009992695` | `>0.009992727` |
| `w` strict inclusion margin | `>0.434708550 eV/H` | `>0.434530971 eV/H` |

이 증명은 centre residual과 whole-box Jacobian의 포함만으로 닫힌다. 비선형 point iteration이나 네 corner의 endpoint 계산을 하지 않았다. 참조 residual의 수학적 해에 대한 존재 증명과 native endpoint 호출·native certificate 발행은 서로 다른 사실이다.

## 7. 유한 혼합효과와 부호

`U=partial_lambda g`, `V=partial_b g`, `W=partial_lambda partial_b g`로 두면

\[
AU=-G_\lambda,\qquad AV=-G_b,
\]

\[
AW=-\{G_{\lambda b}+G_{g\lambda}V+G_{gb}U+G_{gg}[U,V]\}.
\]

고정 gas의 직접 `G_lambdab=0`도 실제 export에서 확인했다. 그렇더라도 나머지 세 coupling 항이 남기 때문에 root의 `W`는 0이 아니다. `A^-1`의 작용은 고정된 Neumann 네 항 `I+Q+Q^2+Q^3`과 엄밀한 tail `gamma^4*norm_r(s)/(1-gamma)`로 감쌌다.

한 scalar observable `phi`의 유한 혼합효과를

\[
I_\phi=\phi(g(1,1))-\phi(g(1,0))-\phi(g(0,1))+\phi(g(0,0))
\]

라 하면, 같은 C² family에서

\[
I_\phi=\int_0^1\!\int_0^1\partial_{\lambda b}\phi(g(\lambda,b))\,d\lambda\,db.
\]

따라서 아래의 whole-Theta mixed derivative 구간은 **단위 parameter 사각형의 유한 혼합효과도 동시에 포함**한다. `T`에서는 `grad(T)*W + Hess(T)[U,V]`를 모두 넣었다.

| Reference observable의 `W` 및 `I` 포함 | Full | First-half | 부호 |
|---|---|---|---|
| `x_HII` | `[-1.465527e-16, -4.611500e-17]` | `[-1.834697e-17, -5.789481e-18]` | 음수 |
| Thermal `w`, eV/H | `[4.228914e-16, 1.376510e-15]` | `[5.299169e-17, 1.722685e-16]` | 양수 |
| Temperature `T`, K | `[2.585919e-12, 8.853760e-12]` | `[3.242790e-13, 1.108188e-12]` | 양수 |
| Energy `e`, eV/H | `[-1.569995e-15, 7.494195e-16]` | `[-1.964984e-16, 9.354066e-17]` | 미결정 |

해석은 이 family와 상자에 한정된다. 음의 `I_x`는 HH와 photo의 이온화 효과가 서로를 억제함을 나타낸다. 양의 `I_T`는 두 cooling 경로의 결합이 단순 합보다 덜 냉각함을 뜻한다. 결합된 상태의 온도 자체가 증가한다는 주장은 아니다. Thermal `w`의 양의 interaction과 기체의 열·이온화 에너지 합 `e`의 부호는 별개다. 여기의 `e`에는 radiation/guard ledger 전체가 포함되지 않는다. `e`의 선형 projection에는 상쇄와 interval dependency가 있어, 이번 계산 결과만으로 부호를 확정할 수 없다.

수소 분율의 혼합효과는 `1e-16` 정도로 매우 작다. 상자 안 `x~0.9`에서 binary64의 한 간격은 `2^-53`이다. 이번 증거는 그 크기의 값을 corner subtraction으로 직접 측정한 것이 아니라, 전체 영역 미분 포함과 적분 항등식으로 얻은 것이다. native 구현의 동일 크기 실제 응답을 확인했다는 주장은 하지 않는다.

## 8. 기존 cubic 설명과 이번 유한 결과의 관계

COMMON incoming signed carry가 0이고, 시간 dependence를 명시적으로 smooth하게 정의한 formal chart에서는 gas `U=O(h)`, `V=O(h^2)`라서 혼합 gas 응답이 cubic에서 시작한다.

\[
[h^3]W_m=\alpha_mH_gP_B+\beta_m(P_B)_gH,
\quad
\alpha_m=\frac{(m+1)(m+2)}{6m^2},\quad
\beta_m=\frac{(m+1)(2m+1)}{6m^2}.
\]

One-full의 계수는 `(1,1)`, two-half의 계수는 `(1/2,5/8)`다. 현재 저에너지 HI source에서 각각의 leading `x/e` coefficient는 음수이고, two-half minus full의 leading coefficient는 양수다. 이전 PHYS04 유도와 식으로 대조했으며 과거 checker를 재실행하지 않았다.

이 formal 결과에는 `B=S_*`라는 smooth source rate가 들어간다. 현재 유한 stage의 `fl(d*S_*)`를 그대로 시간 변수의 매끄러운 함수로 취급하지 않는다. 또한 이번의 first-half uniform theorem에는 두 번째 half carry가 없다. 그러므로 이번 유한 구간 두 개를 빼서 actual full/two-half defect를 발표하지 않는다. 시간 적분 나머지와 continuum/source-law error도 아직 없다.

## 9. 실제 수행과 독립 판정

| 새 실행 | 결과 | 실제 경과시간 | 최대 RSS |
|---|---|---:|---:|
| 구간 primitive 및 2-Jet 독립 검산 | PASS, 324 assertions, 의도한 domain rejection 8개 | 0.2162 s | 11,136 KiB |
| Full whole-X 및 centre-times-Theta 소스 계산 | PASS, source arithmetic 2회 | 3.8370 s | 20,864 KiB |
| First-half whole-X 및 centre-times-Theta 소스 계산 | PASS, source arithmetic 2회 | 3.2296 s | 20,708 KiB |
| 저장된 export의 domain·mechanism·Banach·Neumann 분석 | PASS, 122 assertions | 0.1660 s | 18,264 KiB |

네 실행 모두 최초 실행에서 통과했고, 실행 전후 결박한 코드·입력 hash는 변하지 않았다. Full에서 새 참조 provider channel 99개를 계산했고 first-half는 그 fixed-energy 결과를 읽어 재사용했다. Native provider는 호출하지 않았다. 마지막 분석은 새 source callback이나 transcendental 평가 없이 저장된 포함값만 사용했다.

Primitive의 엄밀성 근거는 112-bit significand 방향 반올림을 하는 정수/유리수 산술, exp/log의 명시적 양의 급수 나머지, 정수 sqrt bracket이다. Decimal 85-digit 관측과 독립 미분식은 구현 오류를 찾는 검산으로 사용했다. Decimal 관측을 엄밀한 transcendental 오차 oracle로 선언하지 않았다.

이번 새 실행에는 native source callback·PreBE·endpoint·BE point·native root/certificate producer·IVP·heavy atomic·과거 과학 suite 실행이 없다. 이 0은 Python-only dispatch와 정적 호출 경계로 확인한 이번 범위의 사실이다. 이전 NCP 반환에서 따로 계측하지 않았던 counter의 `null`은 그대로 보존했다.

독립 reviewer는 후보 코드·테스트 생성에 참여하지 않았고, 새 과학 실행도 하지 않았다. 첫 지적은 finite birth amount/rate 구분이었으며 이론 수정으로 해결했다. 최종 고정 candidate의 판정과 범위는 `review/DECISION.json`, 설명은 `review/REVIEW_KO.md`에 있다. `CANDIDATE_SHA256.json`이 reviewer에게 넘긴 파일 identity를, `MANIFEST.json`과 `SHA256SUMS`가 최종 package를 결박한다.

## 10. 다음 NCP 작업

NCP는 최신 PHYS06 head `65a36e255aa6d9911e23a9b5ced18d8a9f507606`에서 `codex/hh-phys07-ncp-20261011`의 additive 작업으로 이어간다. 기존 adapter를 실제 source producer에 연결하는 데 필요한 작업은 다음과 같다.

1. PHYS07 detached receipt·ZIP manifest·소스 commit을 확인하고, 기존 `CommonFamily`의 stored interval input과 이번 point-seed reference 입력의 차이를 명시한다.
2. 공개된 `phys04_prepare_family`와 `phys04_reduced_residual`의 두 named first-stage arithmetic target에서 native scalar leaves, `Phys04PreBE` tuple, incoming values/derivatives와 전체 잔차·Jacobian·Hessian을 결박한다.
3. 실제 source-domain C² 증거와 물리·온도·denominator·hat coverage를 typed producer로 전달한다. 문자열/boolean을 썼다는 이유만으로 proof를 생성하지 않는다.
4. 이미 구현된 PHYS06 uniform/mixed/finite adapter가 같은 family와 같은 domain의 source export를 받도록 연결한다. 부족한 입력은 구체적인 OPEN 이유로 반환한다.
5. 저장한 native source arithmetic 결과로 HH–photo 방향미분을 점검하고, 독립 판정·원 실행 기록·두 백업과 attachment-free 전달문을 남긴다.

NCP의 endpoint·BE point·native root producer·IVP 등 ceiling은 계속 0이다. 이번 handoff는 공개 source arithmetic을 채우는 작업이며 private permit issuer를 새로 만들지 않는다. Native whole-source binding이 실제로 닫히면 그 범위의 수학적 포함과 현재 참조 결과의 일치를 따로 판정할 수 있다.

실행 가능한 세부 작업·예산·실패 보존·반환 schema는 `handoff/NCP_LOCAL_CODEX_HANDOFF_KO.md`, `handoff/NCP_TASKS.json`, `handoff/NCP_RETURN_TEMPLATE.json`에 들어 있다. 필요한 소스 snapshot, 원 seed, Python 구현, 계산 결과, 하네스 두 archive와 모든 전달파일을 이번 package에 포함했다. 게시 후 실제 object ID가 들어간 START/receipt/index를 기존 두 백업에 함께 둔다.

## 근거 지도

| 확인하려는 내용 | 원본 파일 |
|---|---|
| 최신 NCP source 및 계측 한계 | `inputs/ncp_phys06/SOURCE_INTAKE_SUMMARY.json` |
| Source byte identity | `inputs/ncp_phys06/SOURCE_INTAKE_MANIFEST.json` |
| C²·온도·opacity·kinetics·cubic 유도 | `theory/SOURCE_C2_DOMAIN_KO.md` |
| Uniform root·Neumann·유한 interaction 증명 | `theory/REFERENCE_ROOT_THEOREM_KO.md` |
| Source AST와 leaf mapping | `inputs/SOURCE_PORT_LEAF_MAPPING.json` |
| Full/first-half 잔차·Jacobian·Hessian | `results/full/source_box.json`, `results/first_half/source_box.json` |
| 정확한 domain/mixed/finite 포함값 | `results/SOURCE_ANALYSIS.json` |
| 첫 실행·stdout/stderr·예산·hash | `evidence/*/EXECUTION.json`, `RUN_LEDGER.json` |
| 발견 사항과 수정 | `FAILURE_LOG.json`, `theory/corrections/BIRTH_LEAF_CORRECTION.json` |
| 최종 독립 판정 | `review/DECISION.json`, `review/REVIEW_KO.md` |
| 이후 실행·반환 계약 | `handoff/` |

Host raw label은 `GPT-6 Astra Pro`이고, 이전에 선택한 Astra v4 연구·코딩 하네스를 이어 적용했다. `Pro` suffix의 programmatic alias 일치나 runtime model attestation을 주장하지 않았고 model switch도 하지 않았다. 선택 근거와 두 원본 archive hash는 `harness/HARNESS_SELECTION.json`에 있다.
