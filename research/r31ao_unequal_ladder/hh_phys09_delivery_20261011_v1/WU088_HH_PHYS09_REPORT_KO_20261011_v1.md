# WU088_HH PHYS09 연구 결과

## 1. 이번에 닫은 수학적 의무

**HH와 미래 광자 birth를 함께 켰을 때의 유한 총 기체 에너지 상호작용은, 저장된 NCP07 고정 소스 계열의 두 first-stage 문제에서 엄격히 음수다.** 이 결론은 원 source inclusion과 open C² 증거를 전제로 한 수학적 포함 정리이며, 이번 exact-rational 후처리에서 필요한 엄격 부등식을 확인했다. 실제 비생성 독립 판정은 `review/DECISION.json`을 따른다.

PHYS08은 전체 photo source와 birth derivative의 온도 방향 및 HH와의 source-level 경쟁을 닫았다. 그 결과만으로 implicit mixed response의 에너지 부호를 선택할 수는 없었다. PHYS09는 저장한 residual Jacobian/Hessian으로 전체 parameter rectangle의 U,V,W를 포함한 다음, 에너지 보존 항등식을 먼저 적용한 별도 scalar 식에서 부호를 결정했다. 과거 reference 계열의 수치를 재실행하거나 이름만 바꾼 결과가 아니다.

2026-10-11 06:30:12 UTC intake에서는 예상 NCP08 branch와 해당 prefix, HH Codex branch prefix 및 최근 PR 범위에서 NCP08 실행 반환을 관측하지 못했다. 현재 원 과학 소스는 NCP07 head `4d5c18b8a6d348e2de42b5e12dc0fd4d753add7b`다. NCP08 compiler/build/gate/oracle/독립 결정은 미관측으로 남겼고, PHYS08 pending gate는 이번 전달 묶음에 포함했다. 조회하지 않은 이름의 branch나 게시하지 않은 local 실행까지 없다고 주장하지 않는다.

## 2. 정의와 같은 계열이라는 조건

좌표는 g=(x_HII,y_HeII,y_HeIII,w), w는 eV/H다. lambda와 b는 각각 미래 HH 및 미래 광자 birth의 무차원 세기이며 [0,1]² 전체를 사용한다. 두 문제의 d는 각각 1.25×10⁹ s와 6.25×10⁸ s다. 둘 다 동일 COMMON을 출발점으로 사용하므로 first_half는 실제 첫 단계의 결과를 이어받은 second_half가 아니다.

총 기체 에너지는

\[
e=\ell g,
\qquad
\ell=(\chi_H,f\chi_{\mathrm{HeI}},f(\chi_{\mathrm{HeI}}+\chi_{\mathrm{HeII}}),1)
\]

이다. 여기의 f는 저장된 stage helium leaf다. 온도 식의 밀도비 fhat=exact(nHe_stored)/exact(nH)와 별도로 유지했다. 광자의 전달 에너지나 guard ledger를 e에 더하지 않았다.

각 coefficient vector는 parameter rectangle 전체에서 고정한다. 네 corner마다 서로 다른 interval coefficient를 골라 같은 interaction이라고 부르지 않는다. 원 interval COMMON 및 captured photon/source coefficient가 정의하는 underlying real-source family를 대상으로 하며, binary64 실행 프로그램 자체를 C² 함수로 미분하지 않는다. Source inclusion을 생성한 원 interval kernel 전체를 이번에 새로 형식 검증하지 않았다.

## 3. 부호를 결정한 구조

Residual을 G=g−g_old−dF, 소스를 F=R+lambda H로 쓰면 HH reaction vector는

\[
H=q(1,0,0,-\chi_H),\qquad \ell H=0
\]

이다. 동일한 chi_H leaf를 쓰므로 \(\ell H_g=\ell H_{gg}=0\)도 정확하다. 따라서 에너지 소스 \(E=\ell F\)는 저장된 비광자 원자 반응, photo rate, 팽창 항으로 직접 조립할 수 있다.

\[
E=\ell F_{\mathrm{nonphoto}}
+\sum_{j=0}^{32}\sum_{a=0}^{2}
 (\mathrm{heat}_{j,a}+\chi_a)R_{j,a}
-2H_{\mathrm{mean}}w.
\]

열 잎과 threshold 잎의 정확한 합을 사용했다. 반올림된 heat를 임의로 node energy로 바꾸지 않았고, He의 매우 작은 signed 기여도 모두 넣었다. HH를 서로 무관한 interval 두 개로 만든 뒤 빼는 방식은 사용하지 않았다.

\(A=G_g\), \(U=\partial_\lambda g\), \(V=\partial_b g\), \(W=\partial_{\lambda b}g\)에 대해

\[
AU=-G_\lambda,\quad AV=-G_b,
\quad
AW=-\{G_{\lambda b}+G_{g\lambda}V+G_{gb}U+G_{gg}[U,V]\}.
\]

모든 원 signed residual 항을 보존했다. 에너지 성분은 이를 독립 성분으로 합치는 것 외에 다음 정확한 식으로도 포함된다.

\[
\boxed{W_e=d\{E_gW+E_{gg}[U,V]+E_{g\lambda}V+E_{gb}U+E_{\lambda b}\}.}
\]

Underlying source는 lambda-independent energy 식을 갖지만, 저장된 E_gλ와 E_λb의 수치 interval 꼬리도 실제 합산했다. 따라서 극소값을 0으로 치환한 뒤 얻은 부호가 아니다. 원 thermal-w box 안에서 이 식을 평가했고 새 독립 energy box를 가정하지 않았다.

## 4. 새 수치 포함값

아래 끝점은 exact rational 계산을 binary64로 바깥쪽 표시한 값이다. 각 구간은 parameter rectangle 전체의 mixed derivative를 포함한다.

| 양 | full | 같은 COMMON의 first_half |
|---|---:|---:|
| W_x | [−1.4640154020811193e−16, −4.625587031747189e−17] | [−1.8337498099688988e−17, −5.798310291160896e−18] |
| W_w, eV/H | [4.231222092446087e−16, 1.3761213726268371e−15] | [5.3006127139332743e−17, 1.722441307366423e−16] |
| W_T, K | [2.589911457894497e−12, 8.84851227942642e−12] | [3.245291906525611e−13, 1.107858848529048e−12] |
| 성분별 합 ell[W], eV/H | [−1.5677099720350667e−15, 7.471154418415632e−16] | [−1.9635516724141098e−16, 9.339628114251213e−17] |
| 먼저 투영한 W_e, eV/H | **[−6.192852956727484e−16, −2.012354998700877e−16]** | **[−7.75969827499494e−17, −2.5357316013204017e−17]** |

직접 성분 합의 0 포함은 그대로 보존했다. 별도 항등식의 포함 구간이 더 좁고 엄격히 음수인 것이 이번 진전이다. 0 포함 자체가 실제 에너지 부호 변화나 0 interaction의 증거였던 것은 아니다.

에너지 식의 각 항은 다음과 같다.

| 항, eV/H | full | first_half |
|---|---:|---:|
| d E_gb U | [−6.196321730444347e−16, −2.032723143956792e−16] | [−7.76189030116244e−17, −2.548512955641941e−17] |
| d E_g W | [4.246836604752081e−19, 1.964182354572793e−18] | [2.671001485103455e−20, 1.2318675123027164e−19] |
| d E_gg[U,V] | [−7.780628878887302e−20, 7.263217101871878e−20] | [−4.789753176036578e−21, 4.626791985119309e−21] |
| d E_gλ V | [−1.04816e−318, 1.04816e−318] | [−1.3109e−319, 1.3109e−319] |
| d E_λb | [−6.567245083251e−311, 6.567245083251e−311] | [−3.2836225416256e−311, 3.2836225416256e−311] |

음의 birth-gradient 항이 양의 feedback 및 Hessian 폭을 이긴다. 이를 PHYS08의 source 경쟁과 연결하는 고정-d 분해도 확인했다. 주항 d² ell(P_M)_g H와 나머지를 분리하면 나머지의 절댓값 상계는 주항의 엄격한 음의 여유에 비해 full에서 1.327254%, first_half에서 0.664632% 이하다. 이것은 d→0 Taylor 나머지 추정이 아니라 U=dH+(I−A)U를 사용한 동일 유한 d의 정확한 분해다.

## 5. 근 존재, C² 연결, 유한 interaction

원 native X는 centre±radius를 몇 ulp 넓힌 상자다. 정확한 centre/radius가 만드는 닫힌 Y⊂X를 확인하고 저장된 fixed_C를 exact binary64 lift로 사용했다. C의 determinant는 exact rational로 0이 아니다. K=I−CA의 radius-weighted infinity contraction 상계는

| 검사 | full | first_half |
|---|---:|---:|
| gamma의 바깥쪽 상계 | 1.173683056367391e−4 | 5.853871499248869e−5 |
| x self-map margin의 하한 | 0.013221275908576044 | 0.01317995208132721 |
| w self-map margin의 하한 | 0.43475378690754274 | 0.43455361464301717 |

이며 나머지 두 margin도 엄격히 양수다. 따라서 각 parameter와 고정 coefficient vector에 대해 Y 안에 근이 존재하고 X 안에서 유일하다. Open source chart와 nonsingular Jacobian은 같은 근을 C² 계열로 연결한다. 원 native private root issuer의 승격과는 구분되는 수학적 정리다.

역작용은 네 Neumann 항과

\[
\|\mathrm{tail}\|_r\le
\frac{\gamma^4}{1-\gamma}\|Cs\|_r
\]

을 포함했다. Full W의 weighted tail 상계는 1.8522150263604374e−30, first_half는 1.4356163974171956e−32다. Gamma나 tail을 0으로 가정하지 않았다. 온도에는 T_gW와 T_gg[U,V]를 모두 포함했다.

동일한 C² 계열의 유한 interaction은

\[
I_e=e(1,1)-e(1,0)-e(0,1)+e(0,0)
=\int_0^1\!\int_0^1 W_e(\lambda,b)\,db\,d\lambda.
\]

단위 사각형의 넓이가 1이므로 위 W_e 구간이 I_e도 포함한다. 따라서 I_e<0다. 네 corner를 수치적으로 구해 매우 작은 두 차이를 뺀 관측은 아니다. e(0,0)은 미래 두 작용이 꺼진 stage 이후 baseline이며 과거 HH/photo history를 가진 COMMON 자체와 같다고 놓지 않았다.

물리적으로 음의 I_e는 HH와 추가 광자 birth를 함께 켰을 때 얻는 기체 에너지가 각각의 단독 효과를 더한 예측보다 작다는 뜻이다. HH가 neutral substrate를 줄이면 같은 광자가 기체에 넘기는 에너지도 감소하는 source 방향과 정합한다. 양의 I_T 또는 I_w는 각각의 가산 예측에 대한 혼합 응답이며, 절대 온도 증가나 순수 heating의 주장은 아니다. 기체 e가 줄어드는 결합 효과만으로 기체·광자 전체 에너지 보존의 위반을 주장하지 않는다.

## 6. 실제 실행과 검증 범위

새 Python diagnostic의 첫 실행은 exit 0, 0.8762889720092062 s, 최대 RSS 26,184 KiB였다. Wall/CPU 45 s, address space 384 MiB, 각 output/log 16 MiB 제한 안에서 끝났다. 21개 bound file의 전후 identity가 일치했고 stderr는 비어 있다. 수정 재실행은 없다.

48개 assertion은 유일 test 개수로 부르지 않는다. 의미 사례 8개에는 실제 HH reaction-vector의 interval dependence, 비자명한 Neumann tail, 양/음/zero-touching 분류, signed minsubnormal 보존, 닫힌 식으로 풀리는 HH/photo toy의 finite FTC, 잘못된 contraction/radius 거절이 들어 있다. 두 stage에서 각각 7,096개의 원 saved interval 표현을 확인했다. Rust용 TSV는 각 stage의 108개 full Jet 및 원 고정 leaves를 담은 6,297행, 총 12,594행이다.

| 증거 | SHA256 |
|---|---|
| PROJECTED_RESULTS.json | c6329fed8c411e1592bd1a0c63ebd9ca6151e81500ed1f46fb6b40f4b7758444 |
| GOLDEN_ORACLE.json | df7b7f88b99764c4c54ae2e3ffac79e23e27cd6b01abba040f4a01cb1e406752 |
| GATE_INPUTS.tsv | a371d7f54ee4eb57bcb5095e928e6d9647e8dc2bcd7a9d3e5f5eca6225ef05da |
| analyze_projected_exports.py | 51c933ca4f85db4dc4874623e6ee8978d9cc6ce4b743cfc6594473e5d4d3d56e |

원 source code, provider input 및 full signed Jet는 `inputs/ncp07`에 그대로 보존했다. 원 과학 소스를 새로 호출하지 않았으며 원 source producer counters를 이번 wrapper의 counts로 대체하지 않았다. 새 callback, nonlinear point/root, native endpoint, IVP 및 과거 suite 실행은 없다.

## 7. 남은 의무와 NCP 전달

현재 호스트에 rustc/cargo가 없으므로 PHYS09 Rust consumer의 compile/run은 미실행이다. Python reference와 source 식은 공유된 scientific definition을 가지므로 Rust와의 일치가 독립적인 물리 모델 검증을 뜻하지 않는다. NCP의 새 의무는 원 TSV를 소비해 동일 연산을 outward binary64로 수행하고, 결과 구간이 exact rational oracle를 포함하는지 확인하는 것이다. 단순 overlap이나 표의 부호 복사는 허용하지 않는다.

PHYS08 gate의 기존 완료 증거가 NCP에 있으면 input/source identity를 확인해 재사용한다. 없으면 포함된 선행 전체 ZIP에서 한 번만 수행한다. PHYS09 gate도 one build/one execution/one consumer로 제한한다. Source producer 재실행, toolchain 설치, runtime 교체 또는 native root 실행은 없다.

Native root authority와 actual native U/V/W/I는 계속 false/null이다. Carried second_half, full/two-half paired defect, time/continuum remainder, full49와 production은 미해결이다. 이전 node32 per-node thermal witness의 OPEN도 그대로 보존한다. 이번 aggregate energy theorem이 그 원 predicate를 소급해 통과시킨 것은 아니다.

완료 전달물에는 이 보고서, 정리, claim ledger, 전체 입력과 실행 증거, review, PHYS08 predecessor ZIP, PHYS09 실행 코드·tasks·handoff가 모두 들어간다. 실제 Git 및 양쪽 backup 완료 사실은 detached START/receipt/index가 기록한다.
