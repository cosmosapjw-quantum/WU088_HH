# PHYS78 물리 구성: 유한 원자망과 에너지 보존 LRS Bianchi I 파일럿

## 1. 바로 실행할 구성

선택한 제한 모형은 **비등방 collisionless matter(DM) + 비등방 collisionless radiation + 등방 반응성 H/D/T/He3/He4/Li6/Li7 기체 + 등방 gray UV/escape radiation + 양의 방출 에너지 저장고**다. 원자망의 전자 밀도와 온도는 실제로 진화하고, 흡수·재결합·방출 에너지가 물질/복사 에너지 및 Friedmann 식에 들어간다. 이로써 열·화학·평균팽창의 양방향 결합을 구현한다.

기체의 \(\pi_{ab}\)는 isotropic perfect-fluid closure에서 0이다. 비영 \(\pi_m\)은 collisionless DM, 비영 \(\pi_r\)는 비등방 collisionless radiation에서 온다. UV/재결합 복사에는 등방 moment closure를 쓴다. 모든 기체 핵종의 비등방 collision operator, photon frequency/angle transport, molecular network를 계산했다는 결과는 아니다.

원자 계수는 실제 REI PR210 e4c8133288614638792888367ca10b2ded3138ff의 Verner96 PI 및 Verner–Ferland96 RR catalog에서 재사용한다. 당시 NO_NETWORK_ADMISSION은 당시의 주장 범위이며, 현재 사용자가 허가한 별도 exploratory network 실행을 금지하지 않는다. 아래 유도와 이번 bounded 검증을 새 모형에 붙인다. 기존 HH PR128 과학 기준 및 1231/729/63 완료 이력의 identity와 범위는 보존한다.

## 2. 실제 첨부와 finite species

첨부 PNG를 직접 열어 확인했다. 처음 missing으로 보고된 상태는 최신 파일 상태에서 해소되었다.

- PNG: upload/원시 광핵반응 및 재이온화 네트워크(2).png
- SHA256: 472ba6be633d2b5fc05fc1e0e88f965ff3c0311b0697e3c35c05bbca1629e6f9
- 그림은 n,H,D,T,He3,He4,Li7의 원자/핵반응 연결과 19개 반응을 지정한다.
- 그림의 I/II/III만으로 Li의 전하 단계가 끝나지 않으므로 Li IV(\(q=3\))와 별도 Li6을 추가한다.
- 20-report-1-.pdf는 2026-09-13 HTT 이론 compendium이다. §15는 반대 dust stream과 collisionless radiation의 제한 BI 모형이며 chemistry/rate source가 아니다.
- PDF SHA256: 9f47da1383205ae8112648d2626fc2712ec913aa5f591ec76a738e234efa9418.

| 핵종 | \(A,Z\) | 포함 전하 \(q\) | 상태 수 |
|---|---|---|---:|
| 자유 neutron | 1,0 | 0 | 1 |
| H1,D2,T3 | 1/2/3,1 | 0,1 | 6 |
| He3,He4 | 3/4,2 | 0,1,2 | 6 |
| Li6,Li7 | 6/7,3 | 0,1,2,3 | 8 |
| 자유 electron | 0,0 | -1 | 1 |

독립적으로 저장하는 nuclear/ionic population은 21개이며 자유 전자는 charge neutrality에서 유도할 수 있다. 검산 registry에서는 electron도 넣어 22개다. **열거한 핵종의 중성 및 모든 양의 원자 전하 단계**를 포함한다. H−/Li−, 분자/분자이온은 별도 scope다. 그림에도 없으며, Galli–Palla의 21종 primordial molecular chemistry와 종 목록이 다르다.

n,T의 표준 late-primordial 초기값은 0이다. 인용한 PRIMAT late abundances는 T→He3, Be7→Li7를 포함한다. 임의의 late neutron/tritium/Be7 injection에는 decay 및 neutrino/recoil energy를 추가해야 한다. Be7와 이미 decay-inclusive인 Li7을 초기 중복 계산하지 않는다.

그림의 nuclear 화살표는 원자 row의 전하를 그대로 대입하지 않는다. 정확한 weak channel은
\[
n\to{}^1{\rm H}^{+}+e^-+\bar\nu_e,\qquad
{}^3{\rm H}^{q}\to{}^3{\rm He}^{q+1}+e^-+\bar\nu_e\quad(q=0,1).
\]
이는 기존 bound electron 수를 유지하는 immediate daughter mapping이다. nuclear \(Z\)가 1 증가하고 생성 electron이 전하를 상쇄한다.

## 3. 동일 normal frame의 signed stress

부호 \((-+++)\), proper time \(t\), \(a_\perp=ae^{-\beta}\), \(a_\parallel=ae^{2\beta}\):
\[
H=\dot a/a,\quad s=\dot\beta,\quad
\sigma_{\hat a\hat b}=\operatorname{diag}(-s,-s,2s).
\]
모든 성분을 동일 정규직교 normal frame에 놓는다.
\[
\pi^{(A)}_{\hat a\hat b}=\operatorname{diag}(-p_A,-p_A,2p_A),\qquad
p_A=(P_{\parallel,A}-P_{\perp,A})/3.
\]
에너지밀도가 SI \({\rm J\,m^{-3}}\)이면 proper-second 방정식의 계수는 \(g=8\pi G/c^2\)다. Einstein tensor 식의 \(\kappa_E=8\pi G/c^4\)와 구별하여 \(g=c^2\kappa_E\)로 변환한다. \(c=1\) conventions의 \(\kappa\)를 그대로 SI에 적용하지 않는다.

\[
\Sigma_F=\sqrt6|s|/H,\quad
\Pi_{m,F}=\sqrt6g|p_m|/H^2,\quad
\Pi_{r,F}=\sqrt6g|p_r|/H^2,
\]
\[
\Pi_{{\rm tot},F}=\sqrt6g|p_m+p_r|/H^2.
\]
총 tensor를 먼저 더하고 norm을 취한다. half-contraction은 \(\sqrt3|s|\), \(\sqrt3|p_A|\)이므로 Frobenius와 정확히 \(\sqrt2\)배 차이가 있다. signed \(s,p_m,p_r\) column을 보존한다.

\[
H^2={g\epsilon_{\rm tot}\over3}+s^2+{\Lambda c^2\over3},\quad
\dot s=-3Hs+g(p_m+p_r),
\]
\[
\dot H=-{g\over2}(\epsilon_{\rm tot}+\bar P_{\rm tot})-3s^2,\quad
\dot\epsilon_A+3H(\epsilon_A+\bar P_A)+6sp_A=Q_A.
\]
새 gas/gray component에서는 anisotropic amplitude \(p_A=0\).
같은 trajectory의 \(S=S_0/I+J_m+J_r\)는 조건부 기여 분해이며 species-off 인과 실험이 아니다.

## 4. 원자 계수와 domain

Verner96 PI:
\[
x=E/E_0-y_0,\quad y=\sqrt{x^2+y_1^2},\quad
\sigma=\sigma_0[(x-1)^2+y_w^2]y^{P/2-5.5}(1+\sqrt{y/y_a})^{-P}.
\]
isotope-blind H/D/T, He3/He4, Li6/Li7 atomic rate는 isotope/finite-mass shift를 무시한다. 기존 D-specific owner와 같은 계산으로 소급하지 않는다. source fit threshold와 binding-energy convention도 고정한다.

Li I outer-shell fit 상한은 64.39eV. 18,30,60eV source와 mean-redshift gray evolution은 이 안에 머문다. 122eV를 넣어 Li III→IV PI를 켜면서 Li I fit를 그대로 호출하면 domain 밖이다. 그 확장은 pinned inner-shell source 연결이 필요하다.

기본 soft UV에서 Li II→III 및 III→IV PI는 threshold 이상 source photon이 없어서 0이다. 초기 고차 Li가 0이면 해당 slot이 0인 것도 물리적으로 의미 있다. 그림을 위해 임의 고차 population을 넣지 않는다.

VF96 Eq.(4) RR:
\[
\alpha(T)={A\over s_0(1+s_0)^{1-b}(1+s_1)^{1+b}},\quad s_i=\sqrt{T/T_i}.
\]
표 라벨은 형성되는 최종 ion: Li I/II/III 항목은 각각 Li II→I, III→II, IV→III. 원 fit 구간은 3–\(10^9\)K.

PI+RR-only는 선택한 reduced operator다. CI가 물리적으로 0이라는 뜻이 아니다. Li CI published Tmin은 stage별 1,4,5eV, 약 11604,46418,58023K로 다르다. 12000K가 모든 Li stage의 하한은 아니다. DR,CX,CE,free-free,Compton,molecules도 omitted-channel ledger에 둔다.

## 5. RR thermal closure의 구성적 유도

기존 RR 사건수만 열에너지로 치환하지 않고 Maxwellian transform에서 energy moment를 유도한다.
\[
\alpha(T)=C T^{-3/2}\int_0^\infty E\sigma(E)e^{-E/k_BT}\,dE.
\]
따라서
\[
E_{\rm cap}=k_BT\left({3\over2}+{d\ln\alpha\over d\ln T}\right).
\]
이 관계를 VF fit에 적용하여 **fit-consistent effective Maxwellian cooling closure**를 정의한다. rate fit의 미분이 정확한 microscopic cooling 데이터임을 증명한 것은 아니다.

\[
{E_{\rm cap}\over k_BT}
=1-\frac12\left[(1-b){s_0\over1+s_0}+(1+b){s_1\over1+s_1}\right]
=\frac12\left[{1-b\over1+s_0}+{1+b\over1+s_1}\right].
\]
\(T,T_i>0,\ 0\le b\le1\)이면 \(0<E_{\rm cap}<k_BT\).
binding \(\chi\)의 한 RR 사건은 gas에서 \(E_{\rm cap}\), chemical energy에서 \(\chi\)를 빼고 escape radiation에 \(\chi+E_{\rm cap}\)를 넣는다.

Wolfram은 미분식과 위 표현의 차 0, 양의 표현과의 차 0을 반환했다. 동시에 \(\sigma:\sigma=6s^2\), \(\pi_{\rm tot}:\pi_{\rm tot}=6(p_m+p_r)^2\), \(\sigma:\pi_{\rm tot}=6s(p_m+p_r)\)를 반환했다. 첫 global-symbol 호출의 경고를 보존했고, 지역 변수 형태로 고친 재호출은 clean이었다.

## 6. Gray photon–gas–source reservoir 보존

\(x=\ln(a/a_0)\), prime \(=d/dx\), \(n_H=n_{H,0}e^{-3x}\).
atomic-only run의 nuclear inventories가 보존되어 comoving reference H가 고정된다.
\(y_i=n_i/n_H,\ y_e=\sum_iq_i y_i,\ y_N=\sum_{\rm nuclei}y_i\).

다음은 eV per reference H다: \(u=\frac32k_BT(y_N+y_e)\), \(B=\sum_i y_i\chi_i^{\rm cumulative}\), photon number/H \(N_j\), photon energy/H \(U_j\), \(E_j=U_j/N_j\), RR escape energy/H \(R\), pressureless source energy/H \(Q\).

\(r_{ij}\)는 bin \(j\)가 transition \(i\)에 흡수되는 사건수/H/s,
\(r_i^{RR}\)는 RR/H/s, \(j_j\)는 photon 방출수/H/s:
\[
r_{ij}=c\,n_{\gamma,j}\sigma_i(E_j)y_i,\quad
r_i^{RR}=\alpha_i(T)n_e y_{i+1},\quad
n_{\gamma,j}=n_HN_j,\quad n_e=n_Hy_e.
\]
\[
y'_i=H^{-1}\sum_r\nu_{ir}r_r,\qquad
B'=H^{-1}\sum_i\chi_i(\sum_jr_{ij}-r_i^{RR}),
\]
\[
u'=-2u+H^{-1}\left[\sum_{ij}(E_j-\chi_i)r_{ij}
-\sum_iE_{{\rm cap},i}r_i^{RR}\right],
\]
\[
N'_j=H^{-1}(j_j-\sum_i r_{ij}),\qquad
U'_j=-U_j+H^{-1}(E_{0j}j_j-E_j\sum_i r_{ij}),
\]
\[
R'=-R+H^{-1}\sum_i(\chi_i+E_{{\rm cap},i})r_i^{RR},\qquad
Q'=-H^{-1}\sum_jE_{0j}j_j.
\]
초기 \(Q\) budget을 양수로 두고 depletion을 검사한다. 방출 history가 prescribed여도 source가 Q에서 에너지를 받으므로 전체 장부에 외부 에너지가 생기지 않는다.

합 \(D=u+B+\sum_jU_j+R+Q\)에서 모든 reaction/source 항이 쌍으로 소거된다:
\[
D'=-2u-\sum_jU_j-R.
\]
\[
\epsilon_{\rm aux}=n_HD,\quad
\bar P_{\rm aux}=n_H[2u/3+(\sum_jU_j+R)/3]
\]
이면
\[
\dot\epsilon_{\rm aux}+3H(\epsilon_{\rm aux}+\bar P_{\rm aux})=0.
\]
eV→J는 양쪽에 동일하게 곱한다. conserved nuclear/electron rest mass는 baseline density에 한 번만 넣는다.
collisionless DM/CMB를 합하면
\[
\dot\epsilon_{\rm tot}+3H(\epsilon_{\rm tot}+\bar P_{\rm tot})
+6s(p_{\rm DM}+p_{\rm CMB})=0.
\]
위 Einstein 식과 일관된다.

**범위:** UV/R은 \(P=\epsilon/3,\pi=0\)인 isotropic fluid closure다. BI의 collisionless isotropic photon distribution이 영원히 등방이라는 주장이 아니다. gray mean \(U/N\)는 여러 birth-time spectrum을 압축하므로 threshold tail 흡수가 달라질 수 있다. 에너지 보존은 spectral accuracy를 증명하지 않는다. R은 재흡수되지 않는 escape approximation이다. energy는 장부에 남지만 opacity에는 재투입하지 않는다.

## 7. 핵반응과 초기 abundance

그림 nuclear stoichiometry는 코드 registry로 보존했다. stoichiometry_check.py의 22종,43개 확장 채널에서 \(A^T\nu=0,\ q^T\nu=0\)를 integer exact arithmetic으로 확인했다. 26 atomic 채널은 isotope inventory를 보존한다. 3 beta mapping은 nuclear charge +1과 electron +1을 확인했다. 이 algebra는 reaction coefficient를 공급하지 않는다.

18/30/60eV UV와 gray redshift는 MeV photodisintegration threshold에 못 미치므로 이 UV source의 photonuclear rates는 정확 0이다. 실제 Planck CMB의 무한 tail을 exact 0이라고 부르지는 않는다. CMB-nuclear interaction 자체를 reduced reaction operator에서 생략한 근사다.

cold diffuse gas의 thermonuclear fusion 생략은 Coulomb barrier/dilution 근사다. charged fusion을 exact 0이라고 주장하지 않는다. 비열적 MeV source, cosmic-ray spallation, stellar interior는 별도 물리다. neutron capture는 Coulomb barrier가 없지만 기본 branch는 n=T=0이고 생성 채널이 비활성이다.

PRIMAT Table7의 **median**을 일관되게 사용한다:
\[
Y_p=0.24709,\quad D/H=2.460\,10^{-5},\quad
{}^3He/H=1.074\,10^{-5},
\]
\[
{}^6Li/H=1.20\,10^{-14},\quad {}^7Li/H=5.627\,10^{-10}.
\]
이는 외부 BBN scenario 입력이며 새 코드의 측정/BBN 계산이 아니다. trace mass를 포함해 \(Y_p\)를 보존하려면
\[
{}^4He/H=
{Y_p(1+2y_D+3y_{He3}+6y_{Li6}+7y_{Li7})\over4(1-Y_p)}.
\]
Fig26은 late He3에 decayed T, late Li7에 decayed Be7를 포함한다고 명시한다.

## 8. 가시적인 Sigma/Pi 범위의 허용성

\(F(\mu)=1+\eta P_2(\mu)\)는 \(-1\le\eta\le2\)에서 비음수. \(\eta=-0.8\)의 하한은 0.2, \(\eta=+0.8\)의 하한은 0.6으로 양수다. quadrature weights도 양수여야 한다.
massless shell:
\[
P_\parallel=\epsilon(1/3+2\eta/15),\quad
P_\perp=\epsilon(1/3-\eta/15),\quad p_r=\epsilon\eta/15.
\]
monokinetic massive shell의 \(\upsilon=v/c\)에는 \(p_m=\epsilon_m\upsilon^2\eta/15\). 따라서
\[
\Pi_{r,F}={\sqrt6\over5}\Omega_r|\eta_r|,\quad
\Pi_{m,F}={\sqrt6\over5}\Omega_m\upsilon^2|\eta_m|.
\]
이는 초기 analytic check이며 이후 constant speed 가정이 아니다.

signed Frobenius initial shear \(S_{F,0}=\pm0.1\)이면
\(s_0/H_0=S_{F,0}/\sqrt6\), \(S_{1/2,0}=S_{F,0}/\sqrt2\).
Hamiltonian \(1-(s/H)^2>0\)을 만족한다. \(\upsilon=0.03,0.1\)은 positive phenomenological warm-DM scenario이며 실제 EoR 관측 허용성 판정은 아니다. warm DM를 10^4K 기체 이온으로 잘못 해석하지 않는다.

signed components와 magnitude를 함께 plot하고 total tensor cancellation을 유지한다. Li6 abundance가 작다는 이유로 total stress를 인위적으로 크게 만들지 않는다.

## 9. 검증, 상태, 다음 연결

이번 physics lane 실행: stoichiometry_check.py 1회(exit0), Wolfram exact algebra 3회(첫 stress/RR 호출 warning, 지역변수 교정 후 clean, gray energy cancellation clean). ODE/science sweep/benchmark는 이 lane에서 0회다. parent의 새 science 실행은 별도 기록한다.

| 대상 | 상태 | 다음 연결 |
|---|---|---|
| finite nuclear/ion registry | DONE, PNG 직접 확인 | code78와 이름 대응 |
| 22종/43채널 charge,baryon | PASS_ALGEBRA_ONLY | rate 및 energy 통합 별도 |
| normal-frame stress/norm | DERIVED+CAS_CHECKED | signed output columns |
| VF RR capture energy | DERIVED+CAS_CHECKED | 새 effective closure 기록 |
| gray global energy | DERIVED | parent RHS residual check |
| isotope atomic network | code78 작업 | 13 PI/RR pair, shared ne/T |
| sandbox z20→2 plots | parent 작업 | bounded exploratory sweep |
| frequency/angle/nuclear full rates | OPEN | 다음 실제 physics 의무 |
| molecular/anion network | OUTSIDE_FINITE_REGISTRY | 별도 종/율 선택 |

현재 모형의 exploratory pilot은 진행 가능하다. 기존 angular/momentum continuum 또는 PHYS77 certificate를 완료로 바꾸지 않는다. HH_R10=OFF, production admission 없음.

## 10. Primary sources

1. Verner et al.1996 ApJ465,487, DOI10.1086/177435; https://www.pa.uky.edu/~verner/photo.html — PI fit/domain.
2. Verner–Ferland1996 ApJS103,467, DOI10.1086/192284; Eq4, https://arxiv.org/abs/astro-ph/9509083 ; https://www.pa.uky.edu/~verner/rec.html — RR/source label.
3. Voronov1997 ADNDT65,1, DOI10.1006/adnd.1997.0732; https://www.pa.uky.edu/~verner/col.html — inactive CI/domain.
4. Pitrou et al.2018 Physics Reports, DOI10.1016/j.physrep.2018.04.005; https://arxiv.org/html/1801.08023v3 Table7/Fig26 — fixed BBN input and decay convention.
5. Khatri–Sunyaev2011 AstronomyLetters37,367, DOI10.1134/S1063773711060041; https://arxiv.org/abs/1009.3932 — Be7 capture/recombination.
6. Fuller–Smith2010 PhysRevD82,125017, DOI10.1103/PhysRevD.82.125017; https://arxiv.org/abs/1009.0277 — weak conversion.
7. Galli–Palla1998 https://arxiv.org/abs/astro-ph/9803315 §2 Tables1–4 — molecular network differs from this finite atomic registry.
8. Switzer–Hirata2005 PhysRevD72,083002, DOI10.1103/PhysRevD.72.083002; https://arxiv.org/abs/astro-ph/0507106 — lithium initial neutral fraction sensitive to recombination spectral photons.
9. Grassi et al.2014 KROME, DOI10.1093/mnras/stu114; https://arxiv.org/abs/1311.1070 — public sparse chemistry/thermal solver candidate; not imported in this bounded task.

Exa 및 SciSpace를 실제 호출했고 원문/원저자 데이터로 identity와 식을 정리했다. SciSpace 일부 arXiv 연도는 재등록 연도이므로 journal identity를 사용했다.

## skill_context_used

physmath-research-loop1.3.0:
root path /root/.codex/plugins/cache/created-by-me-remote/physmath-research-loop/1.3.0/skills/physmath-research-loop .
SKILL.md, references/POLICY_INTEGRATION.md, references/THEORY_LOOP.md, references/SUBAGENT_MODE.md를 실제 읽고 적용했다. parent의 optimization→physics→coding 중 이 child는 R2–R7 physics 구성/경량검산 및 R9 code 연결을 맡았다. incomplete publication evidence를 계산 금지로 바꾸지 않고 실제 유도·registry·검산을 진행했다. remote publication/backup은 parent 소유다.

