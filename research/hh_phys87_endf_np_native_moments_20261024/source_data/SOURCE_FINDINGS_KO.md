# PHYS87 원전 조사: ENDF H1 capture와 finite-T 사건 moment

## 판정 범위

공식 NNDC의 **ENDF/B-VIII.1 H1 평가 원문**에서 단면적, 비등방 photon 각분포, recoil branch 및 capture covariance를 실제로 확보했다. 첫 완결 단위는 root가 선택한 `SOURCE_NATIVE_ENDF_NP_FINITE_T_MOMENTS`이다. 원본 평가의 질량·Q 규약을 명시적으로 고정한 finite-domain supplier를 만들 수 있다. 프로젝트의 bare-nuclear network 채택, 소스 밖 tail, 실제 physical uncertainty 및 stopping은 독립 OPEN gate다.

이 조사자는 원전 검색·다운로드·기계적 전사와 유도를 수행했다. Wolfram, 반응률 적분, 사건 수치 계산, 과거 science 재실행, Git/provider 변경은 0이다. root의 실행 계약과 독립 검토가 뒤따른다.

## 실제 확보한 원문과 identity

공식 discovery 경로는 NNDC ENDF API landing → ReDoc → advertised OpenAPI schema → H1/version10 dataset 검색 → dataset12940/datafiles이다. 모든 조회는 공개 read-only였다.

| 원문 | 실제 bytes | SHA256 | 처리 |
|---|---:|---|---|
| `n-001_H_001.endf` |671232|`3024d8f0db604b074e33ed8b05027eb9f5a738614041ba44c83f048e0d0bc1af`|canonical input candidate|
| `n-001_H_001.gnds.xml` |176209|`9c6e1469abc7b40de06538a1990ef2a916dcf2e7a7cf43d0982e68801ec8b69f`|checksum discrepancy retained; excluded from canonical input|
| `ENDF-102-2023.pdf` |2221300|`6da0d63d42d477eb8e832249e032112a3b4a226a9c4acffe1d7ffb4abb41e06b`|official format/kinematics manual|
| `SOURCE_TABLE.json` |48887|`b14ad9b4a2379166ec2b2c04b2a77efb4c819498924682072d74a6b4e31c5014`|153 source rows, decimal strings and exact original field spellings|

ENDF 실제 SHA1 `8fc3df2c793d45d54b4b2efe47792c5da2bec16c`은 API advertised checksum과 일치한다. GNDS advertised SHA1 `106b5e08b0594b5ced05afab231b23ba23fd3eed`와 실제 `b8133b702226fc95f19fe6bd2e4b66e749b65854`는 다르다. 이유는 미확정이며 ENDF의 일치를 무효화하지 않는다. GNDS는 canonical 또는 독립 수치 검증 입력으로 사용하지 않는다.

공식 파일 URL:

- https://www.nndc.bnl.gov/endf-data/ENDF/ENDF-B-VIII.1/n-001_H_001.endf
- https://www.nndc.bnl.gov/endf-api/datasets/12940/datafiles
- https://www.nndc.bnl.gov/endfdocs/ENDF-102-2023.pdf

`NNDC_H1_DATASET.json`, `NNDC_H1_DATAFILES.json`, `NNDC_DOWNLOAD_RECEIPT.json`이 조회 원문/수신 영수증이다. `H1_MF1_MT451.endf`, `H1_MF3_MT102.endf`, `H1_MF6_MT102.endf`, `H1_MF33_MT102.endf`는 canonical 파일의 해당 records를 줄바꿈까지 보존한 부분집합이다. 부분집합 SHA/크기는 `SOURCE_MASS_AND_FORMAT_AUDIT.json`에 있다.

## 평가의 출처와 사용할 범위

MF1은 LANL G. M. Hale, EVAL-JUL16, DIST-AUG24, REV1-NOV23이라고 명시한다. n-p capture와 inverse photodisintegration을 R-matrix 분석에 함께 포함했고, integrated/differential 자료 및 일부 polarization 정보를 사용했다고 설명한다. 이를 새 실험이나 이 프로젝트의 재평가로 세지 않는다.

API의 target은 ground H1 nucleus, incident neutron, laboratory incident energy `1e-5–2e7 eV`다. 그러나 **target metadata label만으로 AWR을 bare proton mass라고 읽을 수 없다.** 아래 ENDF 명시 규약이 우선한다.

원문 narrative의 thermal capture `332.0 mb`와 MF3 literal knot `En=0.0253 eV, sigma=0.3325842 barn`를 함께 보존한다. 계산은 원 MF3 표를 따른다. narrative 값 또는 EFT 논문의 `334.2 mb`로 새 정규화를 하지 않는다. 두 수치 차이를 실험 confidence interval로 쓰지 않는다.

### MF3/MT102

- 153개의 동일 source-native 에너지 절점.
- 1번부터 33번 절점(상단 `1e4 eV`)까지 INT5 log-log.
- 33번부터 153번까지 INT2 linear-linear.
- `QM=QI=2224648 eV`, `AWR=0.9991673`.
- 단면적 단위 barn; `1 barn=1e-24 cm^2`.
- 특정 energy query가 source 밖이면 domain error. 적분은 명시된 window의 부분 기여를 계산하며, window 밖 물리 단면적이 0이라고 주장하지 않는다.

### MF6/MT102

- HEAD `JP=0`, `LCT=2`, `NK=2`.
- photon `ZAP=0`, `LIP=0`, `LAW=2`, yield 1.
- photon AWP field `2223300 eV`는 질량이 아니라 primary photon energy field다.
- 153 En 절점, `LANG=0`, `NL=2`, 암묵적 `a0=1`, En 방향 INT2 linear-linear.
- recoil `ZAP=1002`, `LIP=0`, `LAW=4`, yield 1, `AWP=1.996256`.
- MF14 또는 MF15에 별도 photon law가 있는 모델이 아니다.

Photon polar cosine μ는 COM에서 incoming neutron 방향과 outgoing photon 방향 사이 cosine이다. 축대칭 unpolarized law의 azimuth는 균일하다. Manual §6.2.4 Eq.(6.8)의 정규화는

\[
 f(\mu|E_n)=\frac12[1+3a_1(E_n)\mu+5a_2(E_n)P_2(\mu)],\qquad
 \frac{d\sigma}{d\Omega_*}=\frac{\sigma(E_n)}{2\pi}f(\mu|E_n).
\]

`f=1/2`로 대체하지 않는다. 예를 들어 첫 절점의 `a1=-3.770475e-8`, `a2=-8.74260e-13`도 원자료에 실제 존재한다. 마지막 절점은 `a1=-4.224523e-3`, `a2=-1.873716e-1`이다. 원문 153개의 MF3/MF6 energy 필드 문자열은 모두 동일했다. 이 전사 검사는 공급자의 물리 오차 또는 continuum 수치 적분 검증이 아니다.

정규화와 moment는 Legendre 직교성에서 `〈μ〉=a1`, `〈μ²〉=(1+2a2)/3`다. Quadratic density의 양성성은 각 source knot에서 끝점 및 내부 정지점을 검사할 수 있다. En 선형보간은 두 endpoint angular density의 convex combination이므로, knot의 정확 양성성 증명을 전체 source energy 사이로 전파할 수 있다. 이는 수치 샘플링만으로 대체하지 말아야 할 간단한 구조적 gate다.

## 질량·Q·photon energy 계약

Manual §0.5.1.1(printed p.24)은 AWR target을 **atomic mass**, light-product AWP를 **nuclear mass** 규약으로 구별한다. §3.3.2(printed p.105)는 QM/QI를 atomic masses로 정의한다. §6.3.2(printed pp.152–153)는 primary photon LAW2와 대응 LAW4 recoil을 짝지으며 relativistic Appendix E를 적용한다. §6.2(printed pp.134–135)는 LCT/LAW fields, §6.2.4(printed pp.142–144)는 normalized angular law와 coefficients를 정의한다.

Appendix E.4 Eq.(E.21), printed p.381은 residual rest energy를

\[
 \epsilon_R=\epsilon_t+\epsilon_i-\epsilon_e-Q_I
\]

로 구성한다. 따라서 photon일 때 `epsilon_e=0`이고, native target AWR과 light daughter AWP를 독립적으로 곱하여 Q를 재계산하는 경로는 source의 two-body kinematics 처리가 아니다. Appendix E.4.1(printed p.383)과 E.3.2 Eqs.(E.19)–(E.20)는 photon recoil과 Lorentz boost를 명시한다.

프로젝트 PHYS85의 rounded CODATA2022 bare masses에서 `Q_np=2224566.37 eV`다. Source QI와의 차이는 `81.63 eV`이며, 이를 0으로 반올림하거나 새 원자 source CI로 처리하지 않는다. 전사 파일은 raw AWR/AWP/QI/photon field를 모두 유지한다.

Root가 선택한 새 계산 계약은 **explicit source-native test system**이다. `epsilon_n`만 이전 CODATA neutron energy를 명시적으로 사용하고, `epsilon_H=AWR*epsilon_n`, `epsilon_D_eff=epsilon_n+epsilon_H-QI`로 정한다. 이것은 실제 source mass 원전이 CODATA2022라고 주장하는 것이 아니며, bare p/d network mass를 덮어쓰지도 않는다. Bare-network remap은 OPEN이다.

이 계약에서는 `M0=epsilon_n+epsilon_H`, `W=M0+K`, `En=K(2M0+K)/(2epsilon_H)`이고

\[
 e_*=\frac{(W-\epsilon_D)(W+\epsilon_D)}{2W},\quad
 k_{D*}=\frac{(W-\epsilon_D)^2}{2W},\quad E_{D*}=\epsilon_D+k_{D*}.
\]

QI와 이 식이 energy owner의 수치 권위다. Header photon field `2223300 eV`를 독립적인 두 번째 에너지 law로 넣어 과잉 결정하지 않는다. 해당 field와 kinematic energy의 대조는 source metadata 진단으로 보고해야 한다.

## 새 source와 PHYS85/86을 연결하는 유도

### 방향이 고정된 조건부 사건

Incoming COM axis와 normal-frame COM boost axis 사이 cosine을 c, photon과 boost axis 사이 cosine을 ν라 두자. Azimuth 평균으로

\[
\langle\nu\rangle=a_1c,\qquad
\langle\nu^2\rangle=\frac{1-a_2+3a_2c^2}{3}.
\]

따라서 fixed W,γ,β에서

\[
\langle E_\gamma\rangle=\gamma e_*[1+\beta a_1c],\quad
\langle K_D\rangle=\gamma(E_{D*}-\beta e_*a_1c)-\epsilon_D.
\]

이는 source의 비등방성을 실제 conditional event에 보존한다. Parent PHYS85 exact event closure와 다른 식을 발명할 필요가 없다.

### 공통 T driftless Jüttner의 각도 소거

PHYS86 rate measure는 `sigma * Moller flux * f_n d3p_n * f_H d3p_H`다. Flux의 `1/(E_n E_H)`와 두 momentum measure를 모으면 invariant two-particle measure를 얻는다. W와 total COM boost를 고정한 two-body initial phase space에서 incoming COM 방향은 균일하고, 공통-T Boltzmann weight는 `exp(-gamma W/theta)`만 보므로 그 방향에 의존하지 않는다. Incoming 방향을 적분하면 모든 l≥1 Legendre 성분이 0이 되어 absolute outgoing photon 방향이 COM에서 균일해진다.

이것은 microscopic kernel을 등방으로 가정한 결과가 아니다. Common T, zero drift, classical unpolarized populations 및 source kernel의 적절한 invariant energy dependence를 사용한 rotational averaging이다. 다른 T/drift/polarized/directional population으로 이 결론을 옮기면 안 된다.

### Fixed W에서 boost 평균

`z=W/theta`, `theta=k_B T`에서 boost conditional density는

\[
 dP(\gamma|W)\propto\sqrt{\gamma^2-1}\,e^{-z\gamma}d\gamma,\quad\gamma\ge1,
 \qquad I(z)=K_1(z)/z.
\]

`-I'/I=K2/K1`과 `I''/I=1+3K2/(zK1)`이므로

\[
g_1=\langle\gamma\rangle_W=K_2/K_1=K_0/K_1+2/z,
\quad g_2=\langle\gamma^2\rangle_W=1+3K_2/(zK_1).
\]

에너지 moments는

\[
\langle K_{in}\rangle_W=K+W(g_1-1),\quad
\langle E_\gamma\rangle_W=e_*g_1,\quad
\langle K_D\rangle_W=k_{D*}+E_{D*}(g_1-1),
\]

\[
\langle E_\gamma^2\rangle_W=e_*^2[(4/3)g_2-1/3]
=e_*^2[1+4K_2/(zK_1)].
\]

따라서 `Kin+QI=Egamma+KD`가 같은 event-weight 아래 유지된다. All-fast birth h=0일 때 PHYS85 particle/energy incidence를 그대로 적용한다. h=1 또는 threshold retention은 stopping에서 도출되지 않은 별도 caloric/selection model이므로 자동 채택하지 않는다.

### Finite source-window coefficient

`lambda(s)=[s-(epsilon_n+epsilon_H)^2][s-(epsilon_n-epsilon_H)^2]`라 쓰면 source-window coefficient는

\[
\kappa_I(T)=\frac{c}{4\epsilon_n^2\epsilon_H^2\theta K_2(\epsilon_n/\theta)K_2(\epsilon_H/\theta)}
\int_{W_{min}}^{W_{max}}\sigma(E_n(W))\lambda(W^2)K_1(W/\theta)\,dW.
\]

여기서 c는 cm/s, sigma는 cm²로 통일한다. 위 같은 양의 W weight로 g1/g2 기반 energy moments를 평균한다. Stable input variable K를 쓰면 `lambda=K(K+2M0)(K²+2M0K+4epsilon_n epsilon_H)`다. Exponential mass suppression은 scaled Bessel 또는 검증된 high-z 경로에서 상쇄한다. T255K 등에서 큰 z의 underflow/cancellation을 수용 기준에 넣어야 한다.

이 식은 새 표를 PHYS86의 표준 statistical identity에 결속한 것이다. 표준 thermal-average formula나 Bessel identity 자체를 새 일반 정리로 주장하지 않는다. Parent reference의 완료 identity를 재실행할 이유가 없다.

## 남는 scientific gates

1. Bare-network remap: atomic/source-native target 및 effective residual을 실제 bare p/d masses와 연결하는 명시 source/model decision.
2. Full-domain: below1e-5eV/above20MeV source tail. 현재 kappa_I는 finite-source-window 부분 계수다.
3. Physical uncertainty: MF33/MT102 covariance는 확보했지만 아직 전사·PSD·interpolation·rate covariance 전파를 수행하지 않았다. MF34 angular covariance는 이 raw evaluation에 없다. 이 원문의 MT1 uncertainty 표를 capture uncertainty에 전용하지 않는다.
4. Thermal/fast stopping 및 named consumer admission: 새 rate/moment 숫자가 만들어져도 production/network activation과 별개다.

## SciSpace와 대안 원전

SciSpace를 한 번 사용해 Rupak의 `Precision Calculation of n+p→d+gamma Cross Section for Big-Bang Nucleosynthesis`, arXiv:nucl-th/9911018v2 / Nucl. Phys. A678(2000)405를 찾고 arXiv primary fulltext를 읽었다. 이 논문은 약1MeV까지의 low-energy EFT total cross section과 M1/E1 기여 및 이론오차 추정을 제공한다. 현재 ENDF supplier의 uncertainty로 그 오차를 옮기지 않는다. SciSpace repository 항목의 2022 ingestion date는 논문 출판연도가 아니며 원전은1999preprint/2000publication이다.

JENDL-5 공식 소개와 논문은 H1에 ENDF/B-VIII.0 데이터를 채택했다고 설명한다. JAEA H1 raw iframe은 Imperva human check를 반환하여 그 사이트의 추가 취득을 중단했다. 별도 공식 NNDC ENDF/B-VIII.1 파일로 진행했으며 JENDL 원문을 내려받았다고 주장하지 않는다.

Primary literature URLs:

- https://arxiv.org/html/nucl-th/9911018v2
- https://wwwndc.jaea.go.jp/ftpnd/jendl/jendl-5-n.html
- https://www.nndc.bnl.gov/endf-library/

## 조사 실행 기록과 재사용

`transcribe_source.py`는 numerical kernel이 아니라 exact source-field transcription이다. 첫 inline 전사 command는 dict closing-brace 누락으로 SyntaxError를 냈고 과학 실행 전 실패했다. 수정된 파일을 한 번 실행해153rows를 전사했다. 초기 sandbox network GET은 `Operation not permitted`를 반환했고, 이후 승인된 read-only public-download escalation으로 NNDC 자료를 수신했다. 매뉴얼 전체 텍스트 범위 읽기 한 번은 로컬 text의 끝을 넘어 IndexError가 났고 원 PDF에서 AppendixE 해당 페이지만 별도 추출했다. 실패는 source/evidence 수신·기계적 inspection 계층에 남기며 과학 실패·rate execution으로 세지 않는다.

Root가 최종 source identity, 계약, 계산 허용량, validation 및 independent review를 정한다. 본 결과는 physical rate 또는 production admission 발급이 아니다.
