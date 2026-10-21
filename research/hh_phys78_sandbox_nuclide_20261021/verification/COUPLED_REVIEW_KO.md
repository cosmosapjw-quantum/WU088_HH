# PHYS78 C9 — complementary physics/code review

## 판정

**현재 P0/P1 finding 없음. 선언된 finite/gray/PI+RR 모형의 식–코드 대응은 scoped PASS.**
새 production gate를 만들지 않는다. 이 review는 code 작성자와 다른 agent의 독립 코드 읽기와 직접 packet derivative 계산이지만, reviewer가 앞서 physics contract도 구성했으므로 독립된 외부 model validation이라고 부르지 않는다.

검토 파일: phys78_impl/source/kinetic.py, coupled_model.py, atomic_network.py.
마지막 source SHA와 해당 계산·AST 비교 receipt는 COUPLED_REVIEW.json에 고정했다.

## 실제 확인

1. Canonical massive/massless packet의 \(a_\perp=ae^{-b},a_\parallel=ae^{2b}\) momentum redshift와 normal-frame \(P_\perp,P_\parallel\) 계산이 맞다. signed \(p=(P_\parallel-P_\perp)/3\)를 보존한다.
2. Proper-second shear 식을 \(x=\ln(a/a_0)\), \(q=s/H_{\rm ref}\)로 옮긴 factor와 SI energy normalization이 맞다. 총 stress는 동일 frame에서 먼저 더하고 norm을 취한다. Frobenius와 half-contraction의 \(\sqrt2\) 차이가 output에 보존된다.
3. Nuclear inventory, charge-derived electron, gas temperature, PI/RR number/energy flux, binding energy가 파생 계약과 일치한다.
4. Source reservoir \(Q\)가 matter energy에 포함되고 photon 생성 때 감소한다. Gas+binding+gray+escape+Q의 source 교환이 정확히 상쇄된다.
5. 실제 physical RHS에서 total density continuity를 계산하고 Friedmann 식을 미분하면 Raychaudhuri와 일치한다.
6. BDF conditioning repair는 양의 고정 대각 행렬 \(D\)를 사용한 \(y=Dz\), \(z'=D^{-1}f(x,Dz)\), \(atol_z=D^{-1}atol_y\)다. 물리 IVP와 componentwise error norm이 동일하다. State projection은 없다.
7. Dormant neutron/T의 roundoff bound \(10^{-28}\)/H는 numerical acceptance만 바꾼다. raw values를 보존하며 physical population 생성으로 해석하지 않는다.

## 재실행하지 않고 final source로 연결

독립 point check는 coupled source
87c3ff897a2a20a9ae973acb624e560ea47aab74ffca735d48929ac599d62df0
에서 수행했다. 실제 보존된 source snapshot을 찾고 final source와 AST를 대조했다.

다음 여덟 method의 AST가 완전히 같다:
_initial_state, absolute_tolerances, source_per_x, environment, evaluate, rhs, arrays, postflight.

Final source
1a7ad66d5d14aac906e1f5968730efa48902b811f5bdc2861ae255072c98b781
의 추가는 대각 solver scale, domain-rejection wrapper, 그 metadata와 solve_ivp 좌표 변환이다. 기존 physical point evidence를 다시 실행하지 않고 정확한 STRUCTURAL_IDENTITY bridge로 연결했다. Frozen baseline source도 이 final hash와 같다.

## 3개 독립 point check 결과

구성한 interior states를 사용했으며 scientific trajectory나 primordial donor가 아니다. Solver/ODE를 호출하지 않았다.

| 항목 | 최대 차이 |
|---|---:|
| initial signed Frobenius shear | \(1.39\times10^{-17}\) absolute |
| massive packet continuity | \(1.48\times10^{-16}\) relative |
| massless packet continuity | \(1.16\times10^{-16}\) relative |
| 전체 density continuity | \(3.95\times10^{-16}\) relative |
| differentiated Friedmann–Raychaudhuri | \(4.15\times10^{-16}\) relative |
| gray exchange identity | \(1.17\times10^{-16}\) relative |
| isotope RHS sum | \(1.39\times10^{-17}\) /H/x absolute |

이 결과는 finite equations의 algebra/implementation correspondence다. Continuous angular/momentum certificate, IVP global error나 solver convergence를 증명하지 않는다.

## C9-P2-01 — NaN trial rejection의 조건부 한계

현재 solver_rhs docstring의 retry 설명은 qualification이 필요하다. 실제 설치된 SciPy BDF 소스를 읽으면 solve_bdf_system은 nonfinite RHS에서 Newton iteration을 중단한다. 그러나 BDF._step_impl은 current_jac가 false인 경우 step을 절반으로 줄이기 전에 predictor에서 numerical Jacobian을 새로 계산할 수 있다. predictor 자체가 domain 밖이면 numerical Jacobian도 NaN이 되어 LU 단계에서 종료될 수 있다.

따라서 **invalid Newton iterate가 언제나 자동으로 복구된다는 보장은 없다**. 이것은 실패를 통과시키는 문제는 아니며, 해당 경우 명시적으로 실패한다. 성공한 baseline은 negative stage 및 rejected-domain stage가 모두 0이므로 이 recovery 경로에 의존하지 않았다.

Parent와 code78에 즉시 전달했고, 실행된 source bytes는 그대로 보존하여 README/repair note에 이 범위를 설명하기로 했다. 실제 sweep에서 이 경로가 관찰되면 실패를 보존하고 그 defect만 고친다. 현재 완료 baseline이나 다음 정상 pilot 실행을 막는 gate는 아니다.

## 결과 설명에 유지할 scope

- source_per_x는 photon/reference-H/\(\ln a\) 입력이다. Proper-second emissivity는 \(H\)를 곱한 값이다.
- m/Tref=30인 FD packet의 초기 energy-weighted \(\langle v^2/c^2\rangle=0.014042955660121\), 제곱근은 약 0.1185다. 속도를 정확히 0.1c로 표기하지 않는다.
- \(\pi_m\)은 collisionless DM에서 온다. 반응성 H/He/Li gas는 \(\pi_{\rm gas}=0\), UV/escape radiation도 isotropic closure다.
- 21개 nuclear/ionic slot과 derived electron은 열거한 중성/양이온 원자 단계의 완전성이다. PI+RR run이 그림의 모든 nuclear rate 또는 분자/음이온 network까지 완료한 것은 아니다.
- source photons 18/30/60eV는 Li I fit domain 안이다. Li III/IV 및 n/T가 기본 run에서 0인 것을 인위적으로 변경하지 않는다.
- 동일 isotope의 여러 charge stage는 isotope-blind atomic coefficients를 쓴다. isotope shifts의 독립 예측으로 해석하지 않는다.
- sampled instantaneous energy residual은 energy integration/global/continuum certificate가 아니다.
- HH_R10=OFF; production admission 없음.

## 사용 skill와 실행 경계

physmath-research-loop1.3.0의 POLICY_INTEGRATION과 CODING_LOOP C9를 적용했다. 한 번의 complementary review pass와 관찰된 numerical repair diff만 검토했다. 이 reviewer의 추가 ODE/parameter sweep/benchmark/기존 atomic suite 재실행은 모두 0회다. 3개 pointwise equation checks만 새로 실행했다.

