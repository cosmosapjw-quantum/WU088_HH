# WU088_HH PHYS11 — 광자와 반응 장부의 다음 상태

## 이번에 완료한 연구

PHYS10의 기체–광자 에너지 합에서 한 단계 더 나아가, 같은 소스 계열의 **33개 광자 그룹 각각의 값·두 일차 미분·혼합 미분**을 계산했다. 두 입력은 같은 COMMON에서 따로 출발하는 Full과 first_half다. 흡수 광자 수, source number/energy, HH 사건 수와 문턱 열, 팽창 thermal work, 소스식에서 유도한 escape*의 다음 장부 증가량도 함께 계산했다. 새 source evaluation이나 root solve를 호출하지 않았다.

현재 확보한 자료와 실제 비용에서 NCP에 넘길 새 heavy 작업은 없다. `heavy_queue=[]`, `launch=false`이며, 전달문은 완료 결과를 재사용한 뒤 `NO_HEAVY_JOB_READY`를 반환하도록 한다. 실제 비용과 후속 의존성은 `EXECUTION_ROUTING_KO.md`, 실행 가능한 작업 목록은 `NCP_TASKS.json`에 있다.

과학 주장의 최종 독립 판정은 `review/DECISION.json`을 따른다. 이 보고서는 native root 또는 실제 second_half 실행의 완료를 뜻하지 않는다.

## 1. 고정한 물리 계열과 입력

미래 HH 강도와 광자 birth 강도를 각각 \(\lambda,b\in[0,1]\)로 쓴다. 과거 HH ON 이력은 그대로 유지한다. 기체 좌표는 \(g=(x_{HII},y_{HeII},y_{HeIII},w)\), \(w\)의 단위는 eV/H다. 광자 상태는 이미 photons/H이므로 에너지 합에 추가 \(n_H\) 나눗셈을 하지 않는다.

PHYS09에서 얻은 동일 고정 계수 계열의 조건부 \(U=g_\lambda,V=g_b,W=g_{\lambda b}\)를 재사용했다. PHYS10의 결과와 실제 NCP08/09 반환도 재실행 없이 사용했다. 현재 source inclusion과 동일 C² root family라는 전제는 그대로다. 서로 다른 계수 tuple을 골라 만든 네 corner를 한 interaction으로 빼지 않는다.

현재 Git 기준점은 PHYS10 C2 `7a5eb687515aa29934de764d04fd7493f289ac24`, core subtree `b7592637e565666ad92047b7ea25067a4d6bd34b`다. 51개 branch ref와 최근 updated PR 12개를 확인한 범위에서 새 NCP10 Git 반환은 관측되지 않았다. 현재 AGENTS와 필수 문서 4개, 이전 core 190개 파일의 Git blob identity를 확인했다. 상세 근거는 `inputs/current_git/`에 있다.

## 2. 광자 그룹 carry와 새 스펙트럼 결과

각 node에서 \(R_j=\sum_aR_{ja}\), \(D_j=1+d\sum_a\kappa_{ja}>0\)라 두면

\[
N_j^+=N_j^{in}-dR_j=\frac{N_j^{in}}{D_j}.
\]

저장된 33개 incoming full Jet와 99개 흡수율 full Jet를 모두 읽었다. 각 Jet의 7개 gradient와 7×7 signed Hessian을 그대로 소비하고, 양방향 forcing과 혼합 교차항을 유지했다. 소스의 구조적 0과 구간 산술의 signed tail은 따로 기록했다.

혼합 carry는

\[
W_{N_j}=\mathcal D_{\lambda b}N_j^{in}
-d\left(R_{j,g}W+R_{j,gg}[U,V]+R_{j,g\lambda}V+R_{j,gb}U+R_{j,\lambda b}\right)
\]

로 계산했다. 별도의 quotient 식

\[
(N/D)_{\lambda b}
=\frac{N_{\lambda b}}D
-\frac{N_\lambda D_b+N_bD_\lambda+ND_{\lambda b}}{D^2}
+\frac{2ND_\lambda D_b}{D^3}
\]

과 비교한 뒤, 같은 실수 함수를 포함하는 두 결과의 교집합을 저장했다. 값은 기존 source photon value 포함과도 교차했다. 단계당 165개, 전체 330개의 성분 교집합이 비지 않았다. 이 일치는 소스 전제를 독립적으로 새 인증했다는 뜻은 아니다.

두 단계 모두 node24의 혼합 응답은 양수, node16–23은 음수, 나머지 24개는 0을 포함했다. node는 0부터 센다. node24는 원 소스의 13.7 eV birth node이고, 음수인 8개 node는 13.6–13.6875 eV 구간이다. 따라서 총 잔존 광자 에너지의 양의 interaction을 모든 spectral group의 양의 interaction으로 해석할 수 없다.

| 관측량 | Full, d=1.25e9 s | first_half, d=6.25e8 s |
|---|---:|---:|
| node24의 \(I_N\), photons/H | [1.48145198e-17, 4.52213083e-17] | [1.85878139e-18, 5.66515299e-18] |
| 전체 흡수 광자 수의 \(I_N\), photons/H | [-4.51874231e-17, -1.47062278e-17] | [-5.66301893e-18, -1.85199958e-18] |
| HH 사건 수의 \(I_Q\), events/H | [-1.01309975e-16, -3.14802452e-17] | [-1.26804938e-17, -3.94195993e-18] |
| thermal work의 \(I_W\), eV/H | [1.05780552e-20, 3.44030344e-20] | [6.62576589e-22, 2.15305164e-21] |

여기서 \(I_z=z(1,1)-z(1,0)-z(0,1)+z(0,0)\)다. 표는 동일 C² 계열의 uniform mixed 구간과 단위 사각형의 이중 기본정리로 얻는 finite interaction 포함을 보수적으로 표시했다. 정확한 유리수 끝점과 binary64 바깥쪽 표시는 `results/carry_v2/CARRY_RESULTS.json`에 있다. 각 반응의 값이나 절대 효과가 음수라는 주장은 아니다. 예를 들어 음의 HH 사건 interaction은 두 forcing을 함께 바꿀 때의 비가산적 성분을 뜻한다.

## 3. 방출 에너지와 팽창 일을 포함한 소스식 수지

다음 두 helium 정규화를 구별한다.

\[
f=\operatorname{exact}(f_{He}),\qquad
\widehat f=\operatorname{exact}(n_{He,stored})/\operatorname{exact}(n_H).
\]

기체 에너지 가중치를 \(\ell_f=(\chi_H,f\chi_{HeI},f(\chi_{HeI}+\chi_{HeII}),1)\)로 놓고, nonphoto source로부터

\[
\Gamma_*=-\ell_{\widehat f}F^{np}
\]

를 정의했다. 추가 원본 `ft03_controlled.rs`와 `hhe_events.rs`의 controlled chain에서 threshold literal이 CHI와 같은 것도 확인했다. 이 exact-real 소스에서는 \(\Gamma_*\)가 radiative recombination과 dielectronic recombination의 escaping-energy 항에 대응한다. 실제 native `escaped_energy_rate`의 derivative export와 동일하다는 판정은 여전히 별도다.

그러면 이번 local absorption 단계에서 다음 항등식이 성립한다.

\[
\boxed{
\Delta e_{gas}+\Delta e_{\gamma,retained}
+d\Gamma_*+2dH_{mean}w^+
=d(J_{norm}+\Psi)
}
\]

\[
J_{norm}=(\ell_f-\ell_{\widehat f})F^{np},\qquad
\Psi=\sum_{j,a}(\widehat{heat}_{ja}+\chi_a-E_j)R_{ja}.
\]

이 식의 오른쪽을 먼저 구성한 다음 미분했다. 독립적으로 넓어진 큰 ledger 구간을 마지막에 빼서 잔차를 추정하지 않았다. HH 문턱 항, nonphoto 에너지와 thermal work의 공통 구조는 유도 과정에서 추적했다. 원 소스의 captured heat 차이를 0으로 치환하지 않았다.

| 증대 장부의 mixed/finite 잔차 | Full | first_half |
|---|---:|---:|
| \(I_{T_*}\), eV/H | [-5.78823025e-40, 6.86235794e-39] | [-6.97331191e-40, 8.26934397e-39] |
| \(|I_{T_*}|/(-I_{gas})\)의 상계 | 3.41011300e-23 | 3.26112747e-22 |
| \(f-\widehat f\) | 약3.80578359e-19 | 약7.32582782e-18 |

현재 잔차의 표시 크기는 helium 정규화 차이 항이 정한다. captured heat 차이 19개는 정확한 유리수로 비영이며, 이 입력에서 그 혼합 기여는 signed subnormal보다 작게 포함된다. 그 작은 tail도 원 결과에서 보존했다.

이 결과는 **방출·팽창 ledger를 추가한 관측량의 항등식**이다. PHYS10의 기체+광자만의 잔차와 관측량이 다르므로, 계산 정밀도가 19자리 좋아졌다거나 실제 전체 진화의 에너지 오차가 1e-39라고 말할 수 없다. 두 새 구간은 모두 0을 포함하므로 잔차의 정확한 0 또는 엄격한 부호도 증명되지 않았다. Half 쪽 정규화 leaf 차이가 더 크므로 half 잔차가 더 작지 않다. 이 비교는 시간 수렴률 검사가 아니다.

## 4. 실제 다음 단계로 넘어갈 때 필요한 항

일반 다음 단계의 incoming 광자 \(N^{in}\)은 이미 \(\lambda,b\) 모두에 의존한다. 첫 단계에서 성립한 incoming \(N_\lambda=N_{\lambda b}=0\)를 다시 적용하면 안 된다. 전체 소스가 incoming group에 선형인 구조를 이용하면 gas unknown은 4개로 유지하면서 다음 식을 사용할 수 있다.

\[
\begin{aligned}
AU^+&=U^-+d(F_N[N_\lambda]+h),\\
AV^+&=V^-+dF_N[N_b],\\
AW^+&=W^-+d\{F_{gg}[U^+,V^+]
+F_{gN}[U^+,N_b]+F_{Ng}[N_\lambda,V^+]\\
&\qquad+F_N[N_{\lambda b}]+h_gV^+\}.
\end{aligned}
\]

여기서 \(A=I-dF_g\), \(h=(q,0,0,-\chi_Hq)\)다. 별도 유도 문서는 일반 합성식, HH 소스에 대한 축약, 유한 interaction과 telescoping 조건을 제공한다. 검증에서는 첫 map의 두 mixed derivatives가 모두 0인데도 다음 map \((1+b)/(2-\lambda)\)의 finite interaction은 정확히 1/2인 반례를 사용했다. 이전 일차 carry 사이의 교차항이 필요하다는 것을 검출하는 사례다.

실제 source-aligned denominator는 ray에 독립이므로 같은 node 안에서는 ray 합과 나눗셈을 교환할 수 있다. 다만 33개 group 값만으로 4,224개 ray 분포와 128개 guard 원배열을 복원할 수 없다. 그 원 binary의 SHA와 크기는 남아 있으나 이 패키지의 가용 JSON에는 실제 배열이 없다. 이 작은 payload 가용성 문제를 heavy 계산으로 분류하지 않았다.

기존 ray 분배 helper의 \(\operatorname{fl}(\operatorname{fl}(\sigma c)n_H)\)와 residual의 별도 captured-leaf 곱도 구별한다. 두 normal IEEE nearest 곱이라는 조건 아래 얻은 **값만의** 상대 차이 상계는 Full 5.242806e-19, half 2.624551e-19 이하다. 이는 실제 native coefficient bits 측정, root 동등성 또는 derivative 동등성 인증이 아니다.

## 5. 실제 실행, 수정 및 검증

| 항목 | 실제 기록 |
|---|---|
| 첫 시도 | `carry_first`, 0.166717383 s, 19,728 KiB, exit1 |
| 첫 실패 원인 | COMMON old_gas를 bare interval로 읽었으나 원 데이터는 full Jet였음 |
| 수정 범위 | full Jet를 읽고 value를 선택; 기존 미래 partial들이 0임도 확인 |
| 완료 실행 | `carry_v2`, 4.029582590 s, 29,900 KiB, exit0 |
| 성공 실행 CPU | user3.826025 s + system0.150321 s |
| 검증 범위 | 8개 의미 사례, 168 assertions; assertions를 unique tests로 세지 않음 |
| 입력·구현 binding | 실행 전후 19개 모두 동일 |
| 새 source/native root/inverse 호출 | 각각0 |
| 이전 과학 suite 재실행 | 0 |

첫 계약과 코드 snapshot, 실패 stdout/stderr 및 종료 코드를 그대로 보존했다. 수정한 입력 형식 외에 과학 입력, 정밀도, 허용오차, source leaf를 바꾸지 않았다. 성공 후 반복 성능시험은 하지 않았다. 제한은 wall/CPU45초, address space384MiB, 파일당16MiB였고 실제 완료는 그 안이었다.

## 6. 이번 단계에서 유지하는 열린 항목

`native_authority=false`, actual native root/U/V/W/I는 모두 null이다. 실제 carried second_half, Full 대 two-half 결함, 시간·연속체 나머지, full49, production, 전체 transport/guard/escape/redshift 에너지 보존은 아직 OPEN이다. 기존 PHYS07 analytic-reference-energy 및 NCP07 node32 predicate 항목도 그대로 유지한다.

이번에 실제로 닫은 것은 원 소스 계열의 각 그룹 carry, 미래 ledger 증가량, 그 증대 수지의 포함, 그리고 다음 implicit 단계가 보존해야 할 수학적 합성 구조다. NCP를 쓸 시점은 이 의존성을 갖춘 **실제 장시간의 미완료 history 작업**이 생긴 뒤다. 별도 무거운 작업이 없는 현재는64코어/128GiB의 작업을 시작하지 않는다.

## 근거 파일

- 전체 결과와 간결한 수치: `results/carry_v2/CARRY_RESULTS.json`, `results/carry_v2/SUMMARY.json`.
- 실제 실행과 첫 실패: `evidence/carry_v2/EXECUTION.json`, `evidence/carry_first/`, `evidence/FIRST_FAILURE_AND_CORRECTION.json`.
- 소스 유도와 claim ledger: `theory/JOINT_CARRY_DERIVATION_KO.md`, `theory/JOINT_CARRY_CLAIMS.json`.
- 소스 대응·추가 threshold chain: `theory/SOURCE_TO_CARRY_MAP_KO.md`, `inputs/source_support/`.
- 고정 원 입력과 이전 결과: `inputs/ncp07/`, `inputs/phys09/`, `inputs/phys10/`, `inputs/current_git/`.
- 최종 독립 판정: `review/DECISION.json`, `review/REVIEW_KO.md`.
- 실행 분담과 전달: `NCP_TASKS.json`, `NEXT_DAG.json`, `EXECUTION_ROUTING_KO.md`, `handoff/NCP_LOCAL_CODEX_HANDOFF_KO.md`.
