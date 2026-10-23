# PHYS83 후속 최종 보고서: matched H I CE와 복사 에너지, 핵 thermal/fast 소유권

## 1. 판정과 연구 단위

**유한 source-native H I \(1s\leftrightarrow2s,2p\)의 matched excitation/deexcitation, 고정 \(T,n_e\) 3상태 모델, 사건별 열·원자·복사 회계를 구현하고 독립 검증 및 새 과학 실행 1회를 완료했다.** 핵물리에서는 PHYS81 radiative-capture 회계를 thermal/fast 입자수, 같은 normal frame의 에너지, finite-T 사건 평균에 연결하는 algebra와 supplied-scalar adapter를 완성했다. 실제 nuclear rates, on-shell event provider, fast-product stopping과 coupled cosmological ODE는 활성화하지 않았다.

새 과학 identity: **e09e64848d545d844590c6cc733cc870109d8fa4f3b44bff796afd11c0753d0c**

실제 실행은 **요청 1 = 완료 1 + 실패 0**이다. 완료 identity의 실제 resume 1회는 **SKIP 1 / scientific callbacks 0**이었다. 기존 PHYS78–82 및 외부 완료 과학 identity의 재실행은 0이다. 새 numerical verification의 2,111 assertions와 저장 결과 readback 21개 점검군을 과학 grid 실행 횟수에 합치지 않는다.

이 단위의 판정은 **PASS_SCOPED / COMPLETE_SCOPED**다. 전체 BOUND_BOUND_CE_AND_RADIATIVE_COOLING의 full-source·다준위·다원소·수송 의무는 PARTIAL/OPEN이며, 실제 source confidence interval, coupled thermal/charge history, continuum certificate를 발급하지 않는다. **HH_R10=OFF, Production admission=NOT_ISSUED.**

## 2. 실제 remote lineage와 재사용

사용자가 지정한 PHYS82 최종 HEAD ca9d53983459ea08f9992a8a24663e46b7180344와 원본 ZIP/외부 delivery JSON을 대조했다. PHYS82 과학 결과 commit만 단독 checkout하지 않았다. 최종 PHYS82 CSV의 CRLF 원본을 보존했고 기존 72개 repo 파일 및 동결 과학 51개를 대조했다.

실제 remote에는 그 HEAD의 후손인 PHYS83 S0가 이미 있었다. 그 source/theory 단계의 identity를 읽고 재사용했다. 따라서 이번 변경은 실제 후손 위의 별도 additive Draft PR140으로 게시했다.

| 계층 | 실제 identity / 상태 |
|---|---|
| PHYS82 최종 | ca9d53983459ea08f9992a8a24663e46b7180344 / 원본 bytes 유지 |
| PHYS82 scientific identity | caae042b139373a10c516d759854ad117d807e9f7ace8c365529a1621419b73f / 재실행 0 |
| 이미 존재한 PHYS83 S0·PR139 | 09289300ec2e500806aa2cb82365f00329e41c8c / source·theory 재사용 |
| 이번 S0 recovery | 65c6751d363363cfc15eba0c7debf50eb493c1c9 |
| 검증된 S1 코드 checkpoint | cedf70d886e61fabe4e4f10f5d9cddc1b15ba3dd |
| 새 과학 결과 S2 | 1f5b11524abc351027d0f88cea009f0015dd088f |
| 최종 metadata 게시 HEAD | 외부 PHYS83_CONT_FINAL_DELIVERY_20261023.json 및 PR140 최종 본문에서 읽음 |

PR: <https://github.com/cosmosapjw-quantum/WU088_HH/pull/140>  
Branch: research/hh-phys83-ce-completion-20261023  
Base: research/hh-phys83-matched-ce-radiative-20261023  
이번 subtree: research/hh_phys83_ce_completion_20261023/

기존 PHYS83의 unposted code는 bytes를 회수할 수 없어 재사용 코드라고 주장하지 않았다. 새 구현을 별도 검증하고 위 S1 checkpoint로 고정했다. 부모의 symbolic residual 7개 및 printed-source reciprocity 902개는 기존 기록의 재사용이며 새 계산으로 집계하지 않는다. 계약·코드·source·theory·실제 결과·그림 등 57개 파일은 delivery/SCIENTIFIC_FREEZE.json으로 동결했다. 최종 인계 metadata 추가로 scientific identity를 바꾸거나 science를 다시 실행하지 않는다.

### 2.1 bounded current delta

기존 51repo/2,175branch inventory를 재사용했다. 이번에는 관련 6repo의 최근 PR 5개씩과 dependency/backup metadata를 제한적으로 읽었고, 과학 실행 전 **2026-10-23 15:00:44.912–15:02:50.279 UTC**에 6repo×최근5PR, 실제 refs 12개, 선택 파일 15개를 다시 대조했다. 원문 응답과 identity mapping은 inventory/PRE_SCIENCE_CURRENT_DELTA_REFRESH.json 및 백업의 private evidence에 보존했다.

HE37/HE38, C23A/C23B, REI ANGTHERM01/02, REI222, REC126/129 및 bass184의 접근 가능한 최신 상태를 구분했다. 특히 이전 ANGTHERM01 PREPARED_INPUTS_ONLY 상태는 현재 완료된 prescribed-background 결과와 구분했다. REI221 ANGTHERM02의 producer 실행 결과와 독립 admission PENDING, bass184의 producer 실행과 fresh independent review NOT_RUN도 동일시하지 않았다. REI222는 이번 WU CE owner completion을 OPEN으로 가리켰다. 이번 CE 완료를 다른 repo의 새 science로 중복 집계하지 않았다.

이는 접근 가능한 명시적 refs의 bounded current delta다. 접근 불가능한 비공개 대화나 모든 branch의 현재 상태를 전수 확인했다는 뜻이 아니다.

## 3. 원전과 물리 계약

CCC 원저자 데이터의 H I LS term cross section, CHIANTI의 level/branch/A-value 파일과 원전 연결을 확인했다. Exa 검색 3회, SciSpace 검색 1회를 수행했으며 검색 후보와 읽은 원문·실패한 직접 접근 경로를 보존했다. Anderson 원문 직접 HTTP 접근의 challenge를 우회하지 않았고, 접근 가능한 원문 읽기 경로와 출처를 분리했다. 검색 결과의 존재만으로 물리 계약이 닫혔다고 보지 않았다.

| 계약 | 이번 선택 |
|---|---|
| 상태 | ground \(1s\), excited LS terms \(2s,2p\); unpolarized, stationary-heavy-target |
| degeneracy | \(g_0=2,\ g_s=2,\ g_p=6\) |
| native excitation gap | 두 channel 모두 \(\Delta=10.20435\) eV |
| forward source | channel당 452개 node |
| reverse printed source | channel당 451개; 독립적인 새 보간 kernel 대신 reciprocity check에 사용 |
| incident support | \([10.20435,\ 968.6058]\) eV |
| matched excess support | \(\epsilon\in[0,\ 958.40145]\) eV |
| cross-section 단위 | \(a_0^2\); 추가 \(\pi\)나 multiplicity factor 없음 |
| 2s two-photon rate | \(A_{2\gamma}=8.229\ {\rm s}^{-1}\) |
| 2s M1 rate | \(A_{\rm M1}=2.496\times10^{-6}\ {\rm s}^{-1}\) |
| 2p E1 rate | \(A_{\rm E1}=6.26\times10^8\ {\rm s}^{-1}\) |

2s의 총 spontaneous rate는 \(A_s=8.229002496\ {\rm s}^{-1}\)다. Two-photon 사건은 **photon number 2, pair-total energy \(\Delta\)**를 갖는다. 에너지에 \(2\Delta\)를 더하지 않는다. 두 광자 각각을 \(\Delta/2\)의 단색선으로 지정한 결과도 아니다.

같은 native gap을 collision과 emission 회계에 사용해 이 유한 모델 안의 에너지를 닫았다. 실제 fine structure/Lamb shift/isotope/finite-mass 분광 에너지와 재매칭한 물리 계약은 OPEN이다. LS degeneracy에서 \(2s\leftrightarrow2p\) mixing을 임의로 끼워 넣지 않았다. Higher levels, CI/RR, photo-processes, opacity, 실제 tail/interpolation uncertainty도 이번 모델 밖이다.

원전 근거:

1. CCC author database: <https://atom.curtin.edu.au/ccc-db/index.html>.
2. CHIANTI H I level/transition data and bibliography: <https://db.chiantidatabase.org/h/h_1.html>.
3. 고정한 raw bytes와 source pins: source_data/HI_CE_SOURCE_CONTRACT.json, source_data/CCC_*, source_data/h_1.elvlc, source_data/h_1.wgfa.
4. 원전 심사와 source limitation: verification/CE_SOURCE_REVIEW_KO.md.

## 4. matched moment에서 rate·미분까지

\(\theta=k_BT\)를 eV로 쓰고, incident energy \(E=\epsilon+\Delta\)에서

\[
W(\epsilon)=(\epsilon+\Delta)\sigma_\uparrow(\epsilon+\Delta),\qquad
M_n(\theta)=\int_0^{\epsilon_{\max}}\epsilon^nW(\epsilon)e^{-\epsilon/\theta}\,d\epsilon
\]

를 정의한다. \(W\)를 같은 node 위의 piecewise-linear 함수로 보간하고

\[
\epsilon\,\sigma_\downarrow(\epsilon)=\frac{g_0}{g_i}W(\epsilon)
\]

를 사용한다. 원점을 포함한 reverse rate를 별도의 비일관적 보간으로 만들지 않고 양의 cell incomplete-gamma moments로 적분한다. 같은 단위 변환 prefactor \(C\)에 대해

\[
q_\uparrow=C\theta^{-3/2}e^{-\Delta/\theta}M_0,\qquad
q_\downarrow=C\theta^{-3/2}\frac{g_0}{g_i}M_0,\quad
\frac{q_\uparrow}{q_\downarrow}=\frac{g_i}{g_0}e^{-\Delta/\theta}.
\]

반응으로 선택된 incoming electron energy와 정확한 온도 미분은

\[
\overline E_\uparrow=\Delta+\frac{M_1}{M_0},\qquad
\overline E_\downarrow=\frac{M_1}{M_0},\qquad
\frac{d\ln q}{dT}=\frac{1}{T}\left(\frac{\overline E}{\theta}-\frac32\right)
\]

이다. \(\overline E_\uparrow\) 전체를 원자에 저장하거나 cooling debit으로 쓰지 않는다. Excitation 한 번에 저장되는 에너지는 \(\Delta\), deexcitation에서 thermal bath로 돌아오는 에너지도 \(\Delta\)다.

저온의 log representation, positive moments, units, source SHA, 지원구간 및 exact derivative를 source/matched_ce.py에 연결했다. 수치 구현과 식의 대응은 theory/MATCHED_CE_IMPLEMENTATION_MAP_KO.md에 있다.

### 4.1 저장된 rate의 결과

이번 grid는 **66개 \(T\), 255–50,000 K**다. \(T_*=25370.66308424773\) K는 이전 PHYS82 계열의 Tmax를 이어받은 anchor이며 이번 grid의 최대 온도가 아니다. 아래 수치는 저장 CSV에서 읽었으며 단위는 \({\rm cm^3\,s^{-1}}\)다.

| \(T\) [K] | \(q_\uparrow(2s)\) | \(q_\downarrow(2s)\) | \(q_\uparrow(2p)\) | \(q_\downarrow(2p)\) |
|---:|---:|---:|---:|---:|
| 10000 | 8.512547824e-14 | 1.182566623e-8 | 1.464348190e-13 | 6.780928304e-9 |
| 25370.66308424773 | 7.529257186e-11 | 8.013171083e-9 | 1.695888796e-10 | 6.016284971e-9 |
| 50000 | 5.446136446e-10 | 5.816232092e-9 | 1.744669661e-9 | 6.210765969e-9 |

255 K의 excitation rate도 각각 \(1.2039644274\times10^{-209}\), \(2.4116757887\times10^{-209}\)로 저장됐다. 값이 매우 작다는 사실과 double underflow를 구분한다. 10,000 K에서 anchor까지 up rate 증가비는 각각 884.4893, 1158.1185다. 이것은 저장된 유한 모델의 온도 의존성이며 source uncertainty 비율이 아니다.

근거: results/rate_grid.csv, verification/SAVED_RESULTS_REVIEW.json.

## 5. 고정 bath 3상태 해와 복사 회계

\(a_i=n_eq_{\uparrow i}\), \(c_i=n_eq_{\downarrow i}\), \(d_i=c_i+A_i\)라 둔다. Excited populations \(x=(p_s,p_p)^T\)와 \(p_g=1-\mathbf1^Tx\)에 대해

\[
\dot x=a-\bigl[\operatorname{diag}(d)+a\mathbf1^T\bigr]x
\]

를 ground-state 초기조건에서 푼다. 이번 구현은 2개 eigenvalue의 analytic solution, small-time 및 near-root series로 population과 time-integral을 함께 계산한다. 새 stiff/cosmological IVP를 호출하지 않는다.

\(J_i(t)=\int_0^tp_i(s)ds\), \(J_g=t-J_s-J_p\)로 두면 gross event counts는 \(C_{\uparrow i}=a_iJ_g\), \(C_{\downarrow i}=c_iJ_i\), \(C_{{\rm rad},i}=A_iJ_i\)다. 에너지와 photon number는

\[
\begin{aligned}
U_{\rm atom}&=\Delta(p_s+p_p),\\
E_\gamma&=\Delta(C_{2\gamma}+C_{\rm M1}+C_{\rm E1}),\\
N_\gamma&=2C_{2\gamma}+C_{\rm M1}+C_{\rm E1},\\
\Delta U_{\rm th}^{\rm raw}&=-\Delta\sum_i(C_{\uparrow i}-C_{\downarrow i}),\\
\Delta U_{\rm th}^{\rm stable}&=-(U_{\rm atom}+E_\gamma).
\end{aligned}
\]

Raw event subtraction과 안정적인 storage+radiation 열을 모두 보존한다. Closure로 정의한 stable 열의 항등식만을 독립 에너지 검증이라고 주장하지 않는다. 독립 검증은 별도 참조 solution과 raw gross-event 회계까지 검사했다.

### 5.1 Coronal approximation이 달라지는 두 원인

Steady state에서 \(r_i=a_i/(c_i+A_i)\), \(R=\sum_i r_i\)이므로 \(p_g=(1+R)^{-1}\), \(p_i=r_i/(1+R)\)다. \(n_{{\rm crit},i}=A_i/q_{\downarrow i}\), \(\eta_i=n_e/n_{{\rm crit},i}\)라 쓰면

\[
\frac{j_i}{j_i^{\rm cor}}=
\frac{1}{(1+\eta_i)(1+R)},\qquad
\frac{j_i^{\rm cor}-j_i}{j_i}=\eta_i+R+\eta_iR .
\]

따라서 collisional quenching과 ground depletion이 함께 coronal 차이를 만든다. \(n_{\rm crit}\)는 선택한 channel에서 \(c_i=A_i\)가 되는 crossover다. Full H I plasma의 실제 임계밀도나 항상 coronal 방출이 절반인 밀도로 쓰지 않는다.

| \(T\) [K] | \(n_{\rm crit,2s}\) [cm⁻³] | \(n_{\rm crit,2p}\) [cm⁻³] |
|---:|---:|---:|
| 5000 | 5.459740522e8 | 7.580597391e16 |
| 10000 | 6.958595257e8 | 9.231774352e16 |
| 25370.66308424773 | 1.026934582e9 | 1.040509223e17 |
| 50000 | 1.414833928e9 | 1.007927208e17 |

이 유한 모델에서 2s quenching은 2p보다 훨씬 낮은 밀도에서 중요하다. 고밀도 grid는 이 subset의 formal diagnostic이며, 생략한 mixing·ionization·opacity 등이 있는 실제 고밀도 수소 예측으로 확대하지 않는다.

### 5.2 Transient 에너지 저장을 즉시 복사로 취급할 수 없는 이유

아래는 \(T_*\)에서 CSV에 정확히 저장된 행이다. 단위는 초기 H 원자 1개당 eV, heat withdrawal \(Q_{\rm out}=-\Delta U_{\rm th}\)다. 새 보간이나 해 평가를 하지 않았다.

| \(n_e\) [cm⁻³] | \(t\) [s] | \(U_{\rm atom}\) | \(E_\gamma\) | \(Q_{\rm out}\) |
|---:|---:|---:|---:|---:|
| 1 | 1 | 9.334142148e-11 | 2.405514617e-9 | 2.498856038e-9 |
| 1e8 | 1 | 0.008500036866 | 0.2351420221 | 0.2436420590 |
| 1e8 | 1000 | 0.008501047013 | 242.8576704 | 242.8661714 |
| 1e12 | 1 | 0.09489476216 | 1715.217465 | 1715.312360 |
| 1e12 | 1000 | 0.09489476216 | 1715215.578 | 1715215.673 |

\(n_e=10^8,\ t=1\) s에서 약 3.4887%의 누적 withdrawal은 아직 atomic storage에 있다. 이 순간에 thermal loss 전체를 escaped radiation으로 붙이면 장부가 달라진다. 시간이 길어 population이 stationary에 가까워져도 bath가 고정돼 있으므로 반복 사건의 누적 에너지는 계속 증가한다. \(1.715\times10^6\) eV/H 같은 누적값은 외부에서 유지한 bath의 교환량이다. 유한 reservoir의 총 방출 한계나 실제 coupled \(T,x_e\) history의 상·하한이 아니다.

figures/01_finite_matched_rates, 02_steady_coronal_suppression, 03_transient_energy_accounting의 PNG 3개/PDF 3개를 저장 CSV만으로 생성했다. Plot science callbacks는 0이며, 실제 PNG 시각 검토와 PDF 1-page 구조·텍스트 검토를 따로 기록했다.

## 6. 핵물리: thermal/fast 입자수와 에너지를 함께 소유하기

PHYS81의 bare-ground radiative capture \(n+p\to d+\gamma\), \(n+d\to t+\gamma\), \(p+d\to h+\gamma\) mass/COM 결과를 읽어 재사용했다. 이번 핵 계산은 새 physical rate run이 아니라 사건 algebra와 supplied-scalar ownership adapter의 유도·검증이다.

Rest energies \(A=m_ac^2,\ B=m_bc^2,\ C=m_cc^2\), \(C_i=A+B,\ Q=C_i-C\), incoming invariant energy \(W=C_i+E_*\)로 쓰면

\[
e_\gamma^*=\frac{W^2-C^2}{2W},\qquad
K_c^*=\frac{(W-C)^2}{2W}.
\]

COM-to-normal boost \(\Gamma,\ \boldsymbol\beta\), photon direction \(\hat k_*\) 및 \(b=\boldsymbol\beta\cdot\hat k_*\)에 대해

\[
E_\gamma=\Gamma e_\gamma^*(1+b),\quad
K_c=\Gamma(C+K_c^*-be_\gamma^*)-C,\quad
K_{\rm in}=\Gamma W-C_i,
\]

따라서 같은 normal frame에서 \(E_\gamma+K_c-K_{\rm in}-Q=0\)이다. 이것은 isotropic emission을 전제로 하지 않는 사건 식이다. PDG의 Lorentz boost·two-body 원식을 현재 signature와 단위에 맞게 연결했다.

### 6.1 선택한 fast-first 소유권

| 사건당 변화 | Capture into fast |
|---|---:|
| thermal particle number | −2 |
| fast daughter number | +1 |
| free-electron number | 0 |
| thermal kinetic energy | \(-K_{\rm in}\) |
| fast kinetic energy | \(+K_c\) |
| emitted radiation | \(+E_\gamma\) |
| nuclear rest energy | \(-Q\) |

Stopping은 fast energy를 thermal energy로 옮기지만 그것만으로 thermal particle number를 늘리지 않는다. Assimilation number flux가 실제로 fast daughter를 bath로 넘길 때 \(+1_{\rm th},-1_F\)와 남은 실제 kinetic energy를 함께 옮긴다. 이미 stopping으로 전달한 에너지를 다시 넣지 않는다. Energy fraction \(\zeta\)로 입자수 소유권을 결정하지 않는다.

Prompt-thermal 대안은 \(\Delta N_{\rm th}=-1,\ \Delta U_{\rm th}=Q-E_\gamma\)로 별도 정의한다. 선택된 fast-first closure와 다른 열화 가정이므로 두 장부를 혼합하지 않는다.

### 6.2 finite-T event averaging과 EOS

동일한 양의 reaction measure로
\(\mathsf A=\langle\Gamma W\rangle\),
\(\mathsf B=\langle\Gamma/W\rangle\),
\(\mathsf D=\langle\Gamma e_\gamma^*b\rangle\)를 정의하면

\[
\langle E_\gamma\rangle=\frac{\mathsf A-C^2\mathsf B}{2}+\mathsf D,\quad
\langle K_c\rangle=\frac{\mathsf A+C^2\mathsf B}{2}-\mathsf D-C,\quad
\langle K_{\rm in}\rangle=\mathsf A-C_i .
\]

단일 thermal rate 또는 평균 incoming energy만으로 \(\mathsf B,\mathsf D\)를 공급할 수 없다. Rate가 0이면 모든 source는 0이고 conditional event mean은 undefined/null이다. 실제 event provider가 아직 없으므로 이 식의 physical distribution을 구현했다고 주장하지 않는다.

Equal-T, zero-drift, nonrelativistic Maxwellian reactants 및 \(T\)-independent \(\sigma(E)\)에서 \(\alpha=d\ln\langle\sigma v\rangle/d\ln T\)라 하면

\[
\overline E_{\rm relative,rxn}=k_BT(3/2+\alpha),\qquad
\langle K_{\rm in}\rangle_{\rm rxn}=k_BT(3+\alpha).
\]

Thermal bath에 실제 속한 particles에만 \(u_{\rm th}=3n_{\rm th}k_BT/2\)를 적용하면

\[
\frac32n_{\rm th}k_B\dot T=
-n_{\rm th}k_BT\Theta+\mathcal Q_{\rm th}
-\frac32k_BT S_{n_{\rm th}}.
\]

Fast-first capture에는 \(S_n=-2\mathcal R,\ \mathcal Q_{\rm th}=-\mathcal R\langle K_{\rm in}\rangle\)이므로

\[
\left.\dot T\right|_{\rm capture\to fast}
=-\frac{2\mathcal R}{3n_{\rm th}}T\alpha
\]

를 얻는다. 이 조건부 식은 실제 nuclear rate를 계산하거나 stopping heat를 공급한 결과가 아니다. Explicit screening/state temperature dependence가 있으면 rate derivative 항을 다시 분리해야 한다.

새 Wolfram evaluator 성공 2회에서 residual 10개가 모두 0이었다. Nuclear adapter는 supplied same-frame scalar energies·weights의 회계를 검증했으며 physical on-shell event construction, isotope stoichiometric source, differential measure, nuclear rate·stopping provider는 OPEN이다. theory/NUCLEAR_THERMAL_FAST_OWNERSHIP_KO.md와 theory/NUCLEAR_CODING_ADOPTION_MAP_KO.md가 정확한 적용 범위다.

원전: [PDG Kinematics](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-kinematics.pdf), [Longland et al. 2010](https://arxiv.org/abs/1004.4136), [Warshaw LLNL TDF](https://nuclear.llnl.gov/CNP/tdf/tdf.htm).

## 7. 독립 검증, 실제 실행, 실패의 구분

| 단계 | 범위 | 실제 기록 |
|---|---|---|
| CE 독립 numerical verification | direct-cell quadrature, rate derivative, mp80 augmented expm, steady linear solution, branch boundaries, physical mutants | 53 cases / 1,885 assertions PASS |
| Nuclear verification | Decimal80 독립 사건·ownership 참조, guard | 5 cases / 171 assertions PASS |
| Runner verification | create-only, identity/corruption/recovery mock cases | 13 cases / 55 assertions PASS; 실제 science callback 0 |
| 합계 | 71 named cases | **2,111 assertions PASS_SCOPED** |
| 저장 science readback | COMPLETE, identity, journal/counter, CSV 열 회계, plot provenance | **21개 점검군 READBACK_PASS_SCOPED**, 위 assertions와 별도 |
| 그림 검토 | PNG 3 시각 검토, PDF 3 구조/텍스트 | PASS_SCOPED |
| 실제 science | rate66T×2channel, steady4T×81ne, transient6×122t | paired rate132 / steady324 / transient732 |
| 실제 resume | 같은 완료 identity | 1 skip / scientific callbacks0 |

CE independent reference는 production incomplete-gamma를 그대로 호출한 mirror test가 아니다. 12개 독립 rate pairs에 대해 10,552개의 direct cell scalar integrals, 별도의 finite-difference derivative, 80-digit augmented matrix exponential 및 두 physical mutants를 사용했다. Transient reference는 population과 integral을 함께 비교했다.

| numerical 검증량 | 관측 최댓값 |
|---|---:|
| moments relative error | 8.8817841970e-15 |
| rate down relative error | 7.1054273576e-15 |
| log detailed-balance absolute residual | 2.8421709430e-14 |
| finite-difference derivative scaled discrepancy | 1.87301e-10 |
| independent population absolute discrepancy | 1.1102230246e-16 |
| event counts/integral energy relative discrepancy | 7.5495165675e-15 |

실제 science sample의 raw energy/gross residual 최대는 **2.433784209198325e-16**, nuclei residual 최대는 **1.1102230246251565e-16**이다. Negative clipping을 사용하지 않았고 초기 시각 population 0을 포함한다. 별도 저장 CSV의 Decimal80 재합산은 다른 반올림 경로에서 raw-energy/gross 최대 **2.9690244088665723e-16**을 냈다. 두 수를 같은 검산으로 덮어쓰지 않는다. 모두 finite sample의 diagnostic이며 continuum certificate 또는 net-cooling 상대오차 bound가 아니다.

실패·수정 기록도 보존했다.

- 첫 CE verification 환경 시도는 mpmath import 실패로 종료했다. Numerical callbacks 0, production import 0, science 0이었다. mpmath 1.3.0 wheel bytes를 보존하고 두 번째 환경 시도에서 첫 numerical verification을 완료했다.
- 각 해당 runtime validation 전에 q/log coherence/NaN guard와 runner completion-manifest guard의 정적 문제 2건을 수정했다. Frozen-star guard는 CE 검증 전, runner guard는 CE/nuclear 검증 후·첫 runner mock 전이었다. 이전 source와 finding을 보존했고 이미 완료된 science를 무효화하거나 재실행한 횟수는 0이다.
- Runner mock에는 의도적으로 실패시킨 callback fixture가 있다. 이는 physical science failure가 아니다.
- S2 Dropbox 첫 전송은 FETCH_FAILED였다. 대상 부재를 확인한 뒤 같은 원본 ZIP의 두 번째 전송이 완료됐다. 과학 결과 실패는 0이다.
- Native Git push 인증 미제공은 exact-base64 Git API publication으로 처리했다. 실제 remote SHA와 tree를 다시 읽어 대조했으며 강제 history rewrite를 하지 않았다.

Shared cooperative lease 아래 1 worker/thread로 numerical verification, science, resume, plotting을 순차 실행했다. 다른 process 종료는 0이다. 실제 lease와 stdout/receipt는 verification/lease_*.json에 있다.

## 8. 단계별 게시·백업과 최종 복원의 권위 기록

| 단계 | 유도/코드/검증/과학 | 게시 | 백업 판정 |
|---|---|---|---|
| S0 recovery | 부모 source/theory 재사용, 새 핵 algebra 및 실행 계약 | 65c6751d3633… | Drive+Dropbox upload ACK |
| S1 verified | 새 code + independent 2,111 assertions, science 전 | cedf70d886e6… | Drive+Dropbox upload ACK |
| S2 science | 새 science1 complete, actual resume skip, saved plots/readback | 1f5b11524abc… | Drive+Dropbox upload ACK; Dropbox transfer retry 1 |
| Final metadata | 보고서·handoff·최종 freeze 대조; scientific files 불변 | 실제 final HEAD는 외부 delivery/PR에서 확인 | 최종 ZIP 실제 양쪽 다운로드·복원은 외부 delivery의 결과로 확인 |

S0/S1/S2 ACK를 최종 전체 복원 검증이라고 부르지 않는다. 각 ACK의 원문 identity는 delivery/S0_PUBLICATION_AND_BACKUP_ACK.json, S1_PUBLICATION_AND_BACKUP_ACK.json, S2_PUBLICATION_AND_BACKUP_ACK.json에 있다.

최종 archive는 tracked UNIT의 원본 Git blob, private source/current-delta evidence, mpmath wheel, PHYS82 원본 ZIP 및 외부 JSON을 포함하며 BYTE_MANIFEST.json으로 각 payload를 명시한다. **실제 final HEAD, ZIP 크기/SHA, 양쪽 object IDs, CRC·payload SHA·원격 Git blob·실제 추출·PHYS82 51개와 새 57개 freeze 검증 결과의 최종 권위는 외부 PHYS83_CONT_FINAL_DELIVERY_20261023.json이다.** 그 JSON 자체의 양쪽 원문 readback/SHA는 PR140 최종 본문에 기록한다. 이 구조는 commit/ZIP/JSON의 자기 hash를 내부에 미리 적는 순환 참조를 피한다.

delivery/verify_archive_restore.py는 실제 다운로드된 ZIP 전체 bytes 비교, 모든 CRC와 payload SHA, manifest coverage, Git blob/tree 대조, 안전한 새 디렉터리로 실제 전체 추출, 추출 bytes 재비교를 수행한다. 과학 kernel을 import하거나 실행하지 않는다. 최종 사용자 응답은 실제 완료된 외부 증거에 따라 작성한다.

## 9. 다음 물리 계약과 유지할 OPEN

다음 준비 단계는 원전과 물리 계약을 먼저 닫은 뒤 새 identity로 sandbox code를 구현하는 순서다.

| DAG 의무 | 현재 상태 / 다음 필요 입력 |
|---|---|
| H I finite matched CE/star | COMPLETE_SCOPED; 이번 완료 identity 재실행 금지 |
| BOUND_BOUND_CE_AND_RADIATIVE_COOLING_FULL_SOURCE | OPEN/PARTIAL; 다준위·다원소·방사수송·실제 source uncertainty |
| HI_2S_2P_MIXING_AND_SPECTROSCOPIC_ENERGY_MATCH | 다음 physics contract: finite splitting, state-resolved mixing, native gap와 physical photon energy의 matching |
| NUCLEAR_THERMAL_FAST_PARTICLE_OWNERSHIP | algebra + supplied-scalar implementation COMPLETE_SCOPED |
| NUCLEAR_FINITE_T_EVENT_PROVIDER_AND_STOICHIOMETRY | OPEN: same-frame on-shell events, finite-T positive reaction measure, angular moments, isotope ownership |
| NUCLEAR_RATES_AND_FAST_PRODUCT_STOPPING | 위 provider 계약 이후; 현재 실제 rate0/stopping0 |
| HE_LI_CX_STATE_AND_PHOTON_ENERGY | 병렬 OPEN |
| Li instrument response/deconvolution/isotope/target-state/physical uncertainty | OPEN |
| RECOMBINATION_TO_Z20_INITIAL_CHARGE_CONTRACT | OPEN |
| D_PI_RR_MATCHED_SOURCE_MOMENTS | OPEN |
| LI_HARD_UV_INNER_SHELL_SPECTRAL_CONTRACT | OPEN |
| FULL_GEOMETRY_SPECTRAL_BACKREACTION | OPEN |

전체 DAG의 분모가 고정되지 않았으므로 완료율 백분율을 발명하지 않는다. 현재 단계의 bounded closure와 전체 우주론·다물리 목표의 완료를 구분한다. Runtime version 차이만으로 완료 science를 재실행하지 않는다. PHYS78/79/80/81/82, HH1231/REI729/HH74control63, C22D/E, HE34/35/36/37, ANGULAR01, C23A 및 REI·REC 완료 identity는 재사용한다.

## 10. 기하·tensor convention과 인계

Non-tilted LRS Bianchi I를 유지한다. Reacting thermal gas의 \(\pi=0\), 별도 collisionless DM의 \(\pi_m\), fast population의 tensor ownership을 혼합하지 않는다. 모든 진단에서는 **같은 normal orthonormal frame의 signed matter/radiation tensor를 먼저 합한 뒤 norm**을 취한다. Frobenius norm은 half-contraction norm의 \(\sqrt2\)배다.

동일 trajectory 안의 species/energy 성분 분석은 species-off 인과 실험이 아니다. 이번 scalar frozen-bath 결과로 geometry backreaction이나 gas STF closure를 완료하지 않았다.

Codex 작업 계약, 다음 대화용 복사 prompt, 게시 후 저장/restore 권위는 각각 CODEX_HANDOFF_KO.md, NEXT_THREAD_HANDOFF_KO.md, POST_PUBLICATION_HANDOFF_KO.md에 있다. 10개 이론 단계와 10개 코딩 단계의 근거는 RESEARCH_LOOP_MAP_KO.md에 연결했다. CONTRACT의 초기 pending snapshot과 후속 실제 상태는 STAGE_STATUS.json, EXECUTION_LEDGER.json, DAG_OVERLAY.json, 외부 final-delivery를 통해 구분한다.

**최종 과학 판정: 제한한 H I CE·radiative-event 문제와 핵 ownership prerequisite는 완료·검증됐으며, 모든 후속 물리 공급자와 production admission은 명시된 범위대로 OPEN이다.**

