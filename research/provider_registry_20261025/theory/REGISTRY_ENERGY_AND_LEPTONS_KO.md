# 공급자 registry에서 유한 사건 연산자로: 수·전하·lepton·에너지 계약

2026-10-25. 이 노트의 결과는 아래 정의와 선택한 반응 모형에서 직접 유도한 유한 연산자 항등식이다(derived). 실제 공급자 원행의 복구는 입력 identity를 확정한다. 그 원행의 온도·에너지·상태·frame·정규화와 consumer가 결속되어야 실제 rate 또는 Q의 물리적 사용 범위가 결정된다. 여기서는 rate·Q 수치평가, 새 uncertainty interval 또는 radiation integral을 수행하지 않았다.

재사용 기준은 중앙 commit 641a725ada4be27473069c2c35005a94c2ab0248의 [finite compiler](https://github.com/cosmosapjw-quantum/rei_bianchi/blob/641a725ada4be27473069c2c35005a94c2ab0248/research/rei_chem_ledger_20261025/chem_ledger.py)이며 해당 파일 SHA256은 60a502895266b6feb96964abc4b24db61c2faed2344db0f7d12f16bb47ed62af다. 그 compiler의 conservation/source 부분과 SYNTHETIC_EXACT energy qualification을 구분하여 사용한다.

## 1. 원행을 수 연산자로 보내는 사상

종 \(s\)의 nuclear composition을 \(C_{\kappa s}\in\mathbb N_0\)로 쓴다. 여기서 \(\kappa=(Z,A,\iota)\)는 원 isotope와 nuclear-state/isomer 식별자다. 전자·광자·중성미자의 해당 열은 영이다. 전하 \(q_s\)는 양전하 단위 \(e>0\)로 측정한 순전하이므로 자유전자는 \(q_e=-1\), 양전자는 \(q_{e^+}=+1\)이다.

반응 \(r\)의 양변에 실제 기재된 multiplicity를 \(\alpha_{sr}\), \(\beta_{sr}\)라 두면

\[
 \nu_{sr}=\beta_{sr}-\alpha_{sr},\qquad
 \mathcal C_s=\sum_r\nu_{sr}\mathcal R_r .
 \tag{1}
\]

\(\mathcal R_r\)는 단위 proper volume·proper time당 사건수 \([\mathrm{m^{-3}s^{-1}}]\)다. 같은 종이 여러 번 나타나면 양변에서 먼저 multiplicity를 합한다. 양변에 남는 collider는 \(\nu_{sr}=0\)이어도 \(\alpha_{sr}\)와 rate의 density dependence에서 지워지지 않는다.

각 chemical 사건의 \(C\nu_r=0,\ q^\mathsf T\nu_r=0\)를 검사하면 유한 선형결합에 의해

\[
 C\mathcal C=\sum_r(C\nu_r)\mathcal R_r=0,\qquad
 q^\mathsf T\mathcal C=0 . \tag{2}
\]

이 항등식은 각 \(\mathcal R_r\)의 크기·모형에 독립적이다. 따라서 실제 원행의 구조 검사는 rate를 평가하지 않고도 수행할 수 있다. 역으로 식(2)는 source coefficient의 신뢰도·정의역·정규화를 결정하지 않는다.

Nuclear transmutation에는 서로 다른 isotope가 생성·소멸하므로 \(C\nu_r=0\)를 요구하지 않는다. 대신 \(b_s=\sum_\kappa A_\kappa C_{\kappa s}\)로 정의하여 선택한 baryon-conserving network에서

\[
 b^\mathsf T\nu_r=0,\qquad q^\mathsf T\nu_r=0 \tag{3}
\]

를 검사한다. 고정 compiler는 chemical 사건에서 \((Z,A,\iota)\)까지 보존한다. 핵 isomer 전이는 같은 \((Z,A)\)를 갖더라도 \(\iota\)가 변하는 nuclear 사건으로 분리한다. Isomer excitation이 이미 종의 질량에 들어 있다면 뒤에서 별도 Q 보정으로 두 번 넣지 않는다. NUBASE 원행은 ground/isomer/level/resonance 표지, excitation, decay mode와 uncertainty를 분리 제공한다([원파일 정의](https://www-nds.iaea.org/amdc/ame2020/nubase_4.mas20.txt), [평가 설명](https://amdc.impcas.ac.cn/web/nubase_en.html)).

현재 compiler의 rate 정규화는 reference nucleus당 proper second의 사건수다. \(dV/d\tau=\theta V\), \(dn_*/d\tau+\theta n_*=0\)인 보존된 기준 밀도 \(n_*>0\)와 \(x_s=n_s/n_*\)를 택하면

\[
 \frac{dn_s}{d\tau}+\theta n_s=\mathcal C_s,\quad
 R_r=\frac{\mathcal R_r}{n_*},\quad
 \frac{dx_s}{d\tau}=\sum_r\nu_{sr}R_r . \tag{4}
\]

마지막 식이 기존 source 함수의 의미다. \(n_*\)가 보존되지 않으면 우변에
\(-x_s(dn_*/d\tau+\theta n_*)/n_*\)가 추가된다. 기준 밀도와 clock은 값의 단위만 보고 생략할 수 없다.

## 2. Bound electrons를 포함한 lepton 수

핵의 양전하 수 \(Z_s=\sum_\kappa Z_\kappa C_{\kappa s}\)를 정의한다. 보통의 전자·핵으로 이루어진 material species의 bound-electron 수는

\[
 N_{b,s}=Z_s-q_s,\qquad \ell_s=N_{b,s}. \tag{5}
\]

음이온도 같은 식을 따른다. 예를 들어 H와 H−의 \(N_b\)는 각각 1과 2다. 자유전자, 양전자, 전자중성미자와 반중성미자는 별도 particle identity로

\[
 \ell_{e^-}=+1,\quad \ell_{e^+}=-1,\quad
 \ell_{\nu_e}=+1,\quad \ell_{\bar\nu_e}=-1,\quad \ell_\gamma=0
 \tag{6}
\]

를 갖는다. 여기서 \(\ell\)은 선택한 전자형 약반응 vertex의 signed lepton ledger다. 다른 flavor의 운반·진동을 포함하는 모형은 그 species와 flavor convention을 별도로 확장한다. 전체 우주에서 electron-family number가 항상 보존된다는 가정은 사용하지 않는다.

전자 ionization
\(X^q\to X^{q+1}+e^-\)에서 순전하는 \((q+1)-1-q=0\), lepton 변화는
\([Z-(q+1)]+1-[Z-q]=0\)이다. 즉 bound/free electron 이동은 실제 전자를 한 번만 세면 닫힌다. Charge neutrality에서 자유전자를 다시 생성하면 이 이동을 중복 계산한다.

선택한 beta-minus vertex
\[
 n\to p+e^-+\bar\nu_e
\]
는 \(b^\mathsf T\nu=0,\ q^\mathsf T\nu=0,\ \ell^\mathsf T\nu=0\)를 동시에 만족한다. Atomic bookkeeping의 한 예인
\[
 {}^3\mathrm H^0\to{}^3\mathrm{He}^{+}+e^-+\bar\nu_e
 \tag{7}
\]
에서도 bound electron은 양변에 하나씩이고, 새 electron과 antineutrino의 lepton 수가 상쇄된다. 이것은 charge/lepton identity 예시이며 실제 daughter electronic-state branch의 채택은 아니다. Shake-off electron을 포함하는 branch는 그만큼 daughter charge와 bound-electron 수를 함께 바꿔야 한다.

기존 compiler가 직접 허용하는 pool은 material 및 thermal/fast electron이다. 따라서 photon·neutrino를 거짓 nuclear composition으로 encoding하지 않는다. 이 확장 registry의 별도 particle sidecar에서 전체 \(q,b,\ell\) 합을 확인하고, compiler가 이미 다루는 material/electron 투영을 그대로 재사용한다. Electron-free nuclear label만으로는 실제 atomic weak event의 \(\ell\) 검사가 완결되지 않는다.

## 3. Atomic mass, bare mass와 event Q

같은 isotope·isomer의 bare-nucleus 질량을 \(M_N\), neutral-atom 질량을 \(M_0\), neutral atom의 총 전자 binding energy를 \(B_0>0\)라 하면

\[
 M_0=M_N+Zm_e-\frac{B_0}{c^2}. \tag{8}
\]

전하 \(q\) 상태의 bound electrons가 \(Z-q\)개이고 그 상태의 binding energy가 \(B_q\)이면

\[
 M_q=M_N+(Z-q)m_e-\frac{B_q}{c^2}
     =M_0-qm_e+\frac{B_0-B_q}{c^2}. \tag{9}
\]

\(q=Z,\ B_Z=0\)에서 \(M_N=M_0-Zm_e+B_0/c^2\)가 복원된다. 양이온의 \(B_0-B_q\)는 해당 상태까지 전자를 제거한 에너지이며, 음이온에는 추가 전자 affinity와 선택된 bound state가 필요하다. NIST CODATA의 atom–ion observational relation과 removal-energy 정의가 같은 부호를 준다([Tiesinga et al., 2021, Eqs.64–65](https://physics.nist.gov/cuu/pdf/RevModPhys.93.025010.pdf)). 이 문헌은 변환식의 근거이며 이번 원 질량 입력은 고정 CODATA2022 record를 유지한다.

분자 \(s\)에도 동일하게
\[
 M_s=\sum_\kappa C_{\kappa s}M_{N,\kappa}
       +(Z_s-q_s)m_e-\frac{B_s}{c^2} \tag{10}
\]
를 쓸 수 있다. \(B_s\)는 분리된 bare nuclei와 자유전자를 기준으로 해당 electronic/rovibrational state가 갖는 총 chemical binding이다. 원자·분자 excitation과 결합 에너지를 이 정의에 포함하면 별도 thermal reservoir에 재차 넣지 않는다.

고정된 실제 initial/final species에 대해

\[
 Q_r=c^2\!\left(\sum_s\alpha_{sr}M_s-\sum_s\beta_{sr}M_s\right)
     =-c^2\nu_r^\mathsf T M . \tag{11}
\]

\(Q_r>0\)는 rest energy 감소다. 공급자 atomic masses를 bare species mass 자리에 직접 넣으면 식(9)의 electron mass·binding 항이 빠진다. 전자 없는 strong nuclear reaction에서 \(\sum\nu Z=0\)이면 electron rest-mass 항은 소거되지만
\[
 Q_{\rm bare}=Q_{\rm atom}-\sum_s\nu_s B_{0,s} \tag{12}
\]
의 binding 차이는 남는다. Weak branch에서는 실제 outgoing electron/positron과 daughter charge를 포함한 식(11)을 먼저 사용한다. 표의 beta-Q를 모든 charge/isomer/state branch의 Q로 복제하지 않는다.

에너지 보존은 일관된 state와 reservoir convention에서
\[
 \Delta E_{\rm thermal}+\Delta E_{\rm fast}
 +\Delta E_{\rm radiation}+\Delta E_{\nu}
 +\Delta E_{\rm external}=Q_r \tag{13}
\]
로 쓸 수 있다. \(\Delta E\)는 식(11)에 이미 포함한 rest energy를 제외한 사건 후−전의 에너지 증가다. 따라서 incoming photon absorption은 radiation reservoir에 음의 기여를 갖는다. Neutrino rest mass를 식(11)에 포함했다면 \(\Delta E_\nu\)도 그것을 제외한 운반 에너지이며, 명시적 massless 근사에서는 전체 neutrino energy와 같다. Neutrino의 이 에너지는 실제 추적하는 neutrino/escape owner에 기록한다. Q 전체를 즉시 열로 넣는 것은 식(13)의 별도 deposition 가정이다. 원 compiler의 네 synthetic reservoir와 실제 neutrino 항 사이의 사상은 확장 consumer 계약이 정한다.

## 4. Covariance가 필요한 Q uncertainty

동일한 평가·state convention의 질량 vector \(M\)에 covariance \(C_M\)가 있고 \(\nu_r\)가 고정되어 있으면, 식(11)의 선형성으로

\[
 u^2(Q_r)=c^4\nu_r^\mathsf T C_M\nu_r. \tag{14}
\]

질량 단위가 kg이면 \(C_M\)는 kg², 결과는 J²다. 질량 대신 rest-energy vector를 쓰면 그 energy covariance에 \(c^4\)를 다시 곱하지 않는다. Species masses가 공통 \(m_e\), bare masses 또는 binding data에서 유도되었다면 그 상관도 \(C_M\)에 들어간다.

개별 standard uncertainty만 주어진 상태에서 off-diagonal covariance를 0으로 채우는 것은 independence 가정이다. 이번 고정 mass packet은 joint covariance를 회수하지 않았으므로 실제 \(u(Q)\)는 미평가 상태다. AME도 atomic masses·reaction energies와 별도의 covariance 자료를 구별하여 제공한다([AME2020](https://amdc.impcas.ac.cn/web/masseval.html)).

각 marginal \(u(M_s)\)가 알려졌다는 조건만 쓰면 \(L^2\) 삼각부등식으로
\[
 u(Q_r)\le c^2\sum_s|\nu_{sr}|u(M_s) \tag{15}
\]
의 보수적 상한은 직접 따른다. 이 식은 상관을 알지 못할 때의 조건부 algebraic bound이며, 수치 적용·confidence interval 또는 원 공급자의 uncertainty qualification은 이번 노트에 포함하지 않는다.

## 5. Coefficient에서 사건 flux로: 단위와 동일 입자

선택한 elementary mass-action 모형과 source coefficient convention이 주어졌을 때
\[
 \mathcal R_r=\eta_r k_r^{\rm SI}\prod_{s\in\mathcal D_r} n_s^{\alpha_{sr}}
 \tag{16}
\]
로 정의한다. \(\mathcal D_r\)는 이 coefficient 정의에서 명시적으로 density가 곱해지는 reactant 집합이며 PHOTON/CRP/CRPHOT 같은 prescribed driver token을 자동 포함하지 않는다. 여기서 \(\eta_r\)는 source coefficient가 pair counting·symmetry factor를 포함하는 방식을 나타내는 상수이며 provider definition에서 확정한다. 차수 \(m_r=\sum_{s\in\mathcal D_r}\alpha_{sr}\)이면
\[
 [k_r^{\rm SI}]=\mathrm{m}^{3(m_r-1)}\mathrm{s}^{-1}.
\]
Binary coefficient의 cm³s⁻¹→m³s⁻¹ 변환은 \(10^{-6}\)이다. One-body \(\Gamma\)는 s⁻¹이고 사건 flux는 \(\Gamma n_s\)다. Net stoichiometry \(\nu_r\)만으로 rate order나 collider density를 복구하지 않는다.

예를 들어 동일 reactant \(2A\to\cdots\)의 coefficient가 unordered-pair encounter \(\langle\sigma v\rangle\)라면 \(\mathcal R=\tfrac12\langle\sigma v\rangle n_A^2\)다. 반면 source가 \(-dn_A/d\tau=k_{\rm loss}n_A^2\)로 loss coefficient를 정의했다면 \(\mathcal R=\tfrac12k_{\rm loss}n_A^2\)이고, \(\mathcal R=k_{\rm event}n_A^2\)로 정의했으면 추가 \(\tfrac12\)는 없다. 따라서 reactant multiplicity를 보았다는 이유로 모든 source에 factorial을 일괄 곱하지 않는다.

이번 실제 UMIST 원행은 coefficient·temperature interval·method·accuracy code를 보존한다. Binary 법칙, CP/CR/PH의 서로 다른 normalization은 [Millar et al.,2024 §2.1–2.2](https://umistdatabase.uk/files/UDfA2024.pdf)에서 확인했다. 특히 Arrhenius \(\gamma\)는 Q가 아니며 PH/CR은 임의 incident spectrum에 대한 differential cross section이 아니다. 보존된 gap, isotope/state 미지정, consumer clock과 normalization을 해결한 뒤 식(16)의 물리적 flux를 활성화한다.

## 6. Total RR coefficient와 photon ledger

서로 다른 recombined state \(j\)에 대한 계수를 \(\alpha_j(T)\)라 하면 total coefficient는
\[
 \alpha_{\rm RR}(T)=\sum_j\alpha_j(T),\qquad
 \mathcal R_j=\alpha_j(T)n_e n_{\rm ion}. \tag{17}
\]

단일 광자를 내는 elementary free-bound capture라는 정의 아래 각 사건은 primary photon 하나를 낸다. 그 뒤의 cascade와 재흡수까지 포함한 photon 수·스펙트럼은 별도 상태 자료를 요구한다. Primary spectrum \(\phi_j^{\rm cap}(\epsilon)\)를 단위 적분으로 정규화하고 cascade channel \(a\)의 평균 yield를 \(Y_{ja}\), 정규화 spectrum을 \(\phi_{ja}\)라 두면

\[
 S_\gamma(\epsilon)=\sum_j\mathcal R_j
 \left[\phi_j^{\rm cap}(\epsilon)
       +\sum_aY_{ja}\phi_{ja}(\epsilon)\right],\qquad
 \dot N_\gamma=\sum_j\mathcal R_j\left(1+\sum_aY_{ja}\right).
 \tag{18}
\]

Energy source는 \(\int\epsilon S_\gamma(\epsilon)d\epsilon\)다. 식(17)은 \(\sum_j\alpha_j\)만 정하므로 state weights, cascade branching과 electron-energy-weighted capture spectrum은 추가 입력이다. Effective recombination coefficient에는 선택한 case/재흡수 convention까지 필요하다. 원행의 PHOTON token과 total RR coefficient만으로 식(18)의 전체 photon 수·에너지 분포를 고정하지 않는다. 이는 새로운 no-go 주장이 아니라 inclusive coefficient를 state/spectral consumer에 연결할 때 필요한 입력을 식으로 구별한 것이다.

## 7. 현재 구현으로의 대응

| 위의 결과 | 재사용 구현 또는 새 명시 정보 | 현재 근거 상태 |
|---|---|---|
| (1)–(3) finite number/isotope/charge/baryon 항등식 | frozen stoichiometry, conservation, source 함수 | 기존 구현과 이 식의 직접 대응 |
| (4) abundance normalization | provider normalization + consumer reference density/clock | consumer-specific binding 필요 |
| (5)–(7) bound/free electron 및 weak lepton ledger | material charge/composition + explicit electron/neutrino sidecar | 직접 유도; 실제 weak state/branch binding 별도 |
| (8)–(13) mass/Q/reservoir 사상 | 원 mass type/state, electron binding, named energy owner | 변환식 derived; 실제 Q 미평가 |
| (14)–(15) uncertainty | 같은 mass identity의 covariance/marginals | 조건부 유도; covariance source 미결 |
| (16) 사건 flux | 원 coefficient units/domain/normalization 및 symmetry convention | 원행 복구 완료; actual flux 미평가 |
| (17)–(18) RR radiation | REC state/cascade/spectral source와 CR/HE energy owner | 입력 의무 명시; total coefficient만으로 activation하지 않음 |

과거 249-check는 고정 compiler의 synthetic finite ledger 범위를 유지한다. 이번 공급자 행을 읽고 동일한 정수 보존식에 연결한 근거는 그 범위에서 재사용하며, 실제 Q·rate·radiation의 승인에는 각 행의 위 물리 입력과 독립 검토를 결속한다.
