# WU R8: 인증된 지연 커널과 두 번의 양의 Volterra 상계 개선

작성일2026-10-27 UTC. 상태: 저자 기여; 독립 심사와 실제 실행/채택은 reviews, raw, SCIENTIFIC_ADMISSION이 결정한다.

## 0. 변경 의무 및 물리 범위

R7 native9의 세 번째 블록 끝점 상계는 저장된 reference보다 residual R에서 약599배, scalar coarse E에서 약1749배 크다. 기존 인증의 오류를 뜻하지 않는다. 동일 입력과 명목 생성자 및 이미 저장된 reference를 유지하면서 과거 forcing이 겪은 혼합을 상계에 반영하는 구체적 의무다.

R6의 네 인증과 R7의 네 조건부 사례를 재사용한다. 세 macro block을192cell로 나누고 정확히 두 번 상방 적분한다. 새 K/Gibbs/rate 인증과 ODE 적분은0이다. 실제 HD 소비자, GL2022 reactive state array, para/ortho pool, 밀도와 물리 clock 결속은 INPUT_PENDING이다. 합성 reaction과 native excitation generator를 구분한다.

## 1. 원자료 및 같은 family 결속

모든 재사용 파일은 WU088_HH@c1badb7de44131715a4998d76515506da5573707에 고정한다.

|자료|경로 suffix|SHA256 또는 Git blob|
|---|---|---|
|R6증명|provider_registry_molecular_r6_20261027/theory/INTERVAL_BLOCK_PROOF_KO.md|blob354b07428b24c47ef3468dabab3795eee30d0439|
|R6원시|provider_registry_molecular_r6_20261027/raw/PRIMARY_RESULTS.json|1a3b55f7c14a64a10a651de2df7b7f7d2df24d0b9e809b729f32d73377c90e84|
|R7증명|provider_registry_molecular_r7_20261027/theory/NONLINEAR_FEEDBACK_PROOF_KO.md|0390132d823cb227a8eeb7f0e8d29157acba5d50a26983d0385e72626a1ea8f3|
|R7원시|provider_registry_molecular_r7_20261027/raw/PRIMARY_RESULTS.json|6eaf3c0eed7968cf4023180e15373a180bb5b1bab2e56cd4a8547387ed337a15|
|R7reference|provider_registry_molecular_r7_20261027/raw/REFERENCE_RESULTS.json|e403c7803c080fd4f26be71a93b782b02d874f80ef11c85a706bea71e2a743cd|
|R7exp정의|provider_registry_molecular_r7_20261027/src/nonlinear_feedback.py|002a66a30961b21e566a940462468c9ea8e1bc868d98549d3ea79d164c239957|

경로 앞에는 research/를 붙인다. Native source SHA256는0c99fe168235d6d6dac3063093bbbe8b4a2ea15cca53c7e2987763c801fdaefb다. 선택T=100K, collider_id2는para-H2이며 native v는UNSPECIFIED로 유지한다.

R6는 off-diagonal interval 안에 있고 대각을 정확한 음의 column sum으로 정의한 Markov generator family다. 대각을 독립적인 box변수로 취급하지 않는다. 같은 residual 공간 Z=ker(1^T)에서 모든 시작 시각s에 대해
\[
 \|\Phi(s+H_j,s)z\|_1\le \rho_j\|z\|_1,\quad z\in Z,             \tag{R8.1}
\]
이며 모든 부분 창이 비팽창이다. 실제 R6 graph.blocks의 네 native 인증은 같은lambda와P_lower를 저장한다. R6증명§2의 ordered-product 하한은 시작시각에 독립적이다. 따라서 같은family/all-starts 조건이 성립한다. R7 native9 K는 저장Kbox의exactmidpoint이며 그membership은 원시결과에 인증돼 있다. 이번runner도 sourceidentity와membership을 확인하되 원래 인증을 다시 계산하지 않는다.

R7 reaction/reset feedback은 a,b,g에 포함되어 있다. h는 nominalK 전파에 적용하며 full reactive operator로 무단 전이하거나 destruction을 중복 차감하지 않는다.

R6 H_j=mu_j/lambda, mu_j={8,32,128,256}. H=H_256, delta=H/64=4/lambda, T=3H=192delta이므로
\[
 m_j=H_j/\delta=\{2,8,32,64\}.                                \tag{R8.2}
\]
이는 exact rational cross-product로 확인한다. 소수 grid snapping은 없다. 설명용H는약{0.94904331,3.79617324,15.18469296,30.36938593}, rho의저장ceiling은{0.999357494399183,0.923996059566344,0.165295730962774,0.008346121460630}이다. 계산에는원래exactrational을쓴다.

Native sourceclock tau=n_coll*(1e-11 cm^3/s)*t이며 R7fixture는 동일 선언 무차원K/H/rho좌표를 사용한다. 실제n_coll 없이는H를물리초로해석할수없다. 두상태사례는H=1/4,rho=5/8,step64의동일all-starts분석인증을재사용한다.

## 2. 두 성분 비교식

R=||r||_1,E=|eta|로 두며 R7동일초기불변량조건에서전체coarse l1=4E다.
\[
 \|F_r(t)\|_1\le aR+bE+g_r,\qquad
 D^+E\le cR+dE+g_e,                                         \tag{R8.3}
\]
a,b,c,g_r,g_e>=0,d는실수다. R7각사례의3blocks는같은B=[[a,b],[c,d]],g를쓴다. 따라서전체3H에같은계수경계가유효하다. 미래block별다른계수에는현재고정계수증명을그대로쓰지않는다.

Duhamel 및scalar integrating factor로
\[
 R(t)\le h(t)R_0+\int_0^t h(t-s)[aR(s)+bE(s)+g_r]ds,           \tag{R8.4}
\]
\[
 E(t)\le e^{dt}E_0+\int_0^t e^{d(t-s)}[cR(s)+g_e]ds.           \tag{R8.5}
\]
물리좌표일때B는inverse time,g는density/time,delta/phi는time이고모든항은density다. 현재무차원fixture규약을보존한다.

## 3. 인증된 지연 ladder

h_0=1로 두고
\[
 h_n=\min\{h_{n-1},\min_{j:m_j\le n}\rho_jh_{n-m_j}\}.         \tag{R8.6}
\]
n에귀납한다. nδ구간을(n-1)δ+δ로분해하면비팽창성과기존h_(n-1)가상계를준다. (n-m_j)δ+m_jδ로분해하면propagatorcomposition과유도norm의submultiplicativity가rho_jh_(n-m_j)를준다. 모든시작시각에같은인증이유효하므로각분해가가능하고상계들의min도상계다. 실제구현의각곱을위로dyadic반올림해도유효하다. 따라서0<=h_n<=h_(n-1)<=1이다.

임의u의kernel을
\[
 h(u)=h_{\lfloor u/\delta\rfloor},\quad h(T)=h_{192}           \tag{R8.7}
\]
로두면남는부분구간비팽창성으로valid upper다. 이계단함수는실제전파의불연속을뜻하지않는다. 단일aligned-endpoint인증만으로이all-starts ladder를구성하면안된다. prefactor1의순간exponentialgap을추론하지않는다.

## 4. 연속 양의 연산자와 구현의 구분

(R8.4–5)의우변을F라하고ordinaryMetzlercomparison
V(t)=exp(Bt)w0+int_0^t exp(Bs)g ds를생각한다. h<=1이면F(V)<=V다. F는양의kernel로순서를보존하고actual<=F(actual)이므로exactfunctioniteration W^(p+1)=F(W^p),W^0=V에서
\[
 actual\le W^{p+1}\le W^p\le V.                              \tag{R8.8}
\]
그러나실제초기배열은저장whole-blockupper를복제한piecewiseconstant상계이며V를새로평가한것이아니다. 이배열에서F(U)<=U가자동으로성립한다고가정하지않는다. Cell상방적분과반올림이후의감소성은
\[
 U^{p+1}=\min(U^p,\widehat F(U^p))                           \tag{R8.9}
\]
로보장한다. 두항각각이whole-cellupper임을아래에서증명한다.

## 5. Closed cells와 초기배열

t_n=nδ,I_n=[t_n,t_(n+1)],n=0..191이다. R7blockk의
blocks[k].certificate.whole_block_upper=C_k를사용하여
\[
 U_n^0=C_{\lfloor n/64\rfloor}.                              \tag{R8.10}
\]
원래exactFraction을64cell에복제한다. R7인증으로I_n전체에actual<=U_n^0다. 인접closedcell의공유끝점은양쪽상계가모두유효하고적분의단일점은측도0이다. 초기R0,E0는전체t=0의initial_error이며macro경계에서reset하지않는다.

## 6. 한 pass의 residual cell 및 endpoint

이전pass의고정배열U에서
\[
 F_j=aU_{R,j}+bU_{E,j}+g_r,\quad L_j=cU_{R,j}+g_e.             \tag{R8.11}
\]
t∈I_n,j<n,s∈I_j이면t-s>=(n-j-1)δ이므로h(t-s)<=h_(n-j-1). 현재cell은길이<=δ이고kernel<=h0=1이다. 따라서
\[
 \widehat R_n^W=h_nR0+
 \delta\sum_{j<n}h_{n-j-1}F_j+\delta F_n.                     \tag{R8.12}
\]
오른쪽끝점t_(n+1)에서j<=n의최소lag는(n-j)δ이므로
\[
 \widehat R_{n+1}^P=h_{n+1}R0+
 \delta\sum_{j\le n}h_{n-j}F_j.                              \tag{R8.13}
\]
whole초기h_n/point초기h_(n+1),wholepast n-j-1/pointpast n-j의차이를보존한다. n=0과거합은0이며음수index가없다. 현재forcing에전체blockrho를곱하지않는다.

## 7. d의 부호와 coarse 적분

\[
 e=e^{d\delta},\quad
 \phi=\int_0^\delta e^{du}du=
 \begin{cases}(e^{d\delta}-1)/d&d\ne0\\\delta&d=0.\end{cases}  \tag{R8.14}
\]
항상phi>0이다. 과거cell의정확한가중은phi*exp(d(t-t_(j+1)))이다. d<=0이면이항과초기항의sup가cell왼쪽에서발생하여
\[
 \widehat E_n^W=e^nE0+
 \phi\sum_{j<n}e^{n-j-1}L_j+\phi L_n.                        \tag{R8.15}
\]
d>0이면오른쪽에서발생하여
\[
 \widehat E_n^W=e^{n+1}E0+
 \phi\sum_{j<n}e^{n-j}L_j+\phi L_n.                          \tag{R8.16}
\]
현재cell의phi(d,t-t_n)는미분exp(d(t-t_n))>0이므로모든d에서phi(d,δ)보다작다. 그래서두식의마지막항은동일하다. 모든d의오른쪽끝점은
\[
 \widehat E_{n+1}^P=e^{n+1}E0+
 \phi\sum_{j\le n}e^{n-j}L_j.                                \tag{R8.17}
\]
d=0에서두branch가이어지고B역행렬은필요없다. native9의d=-1/20000000,c=1/1250000,g_e=0를그대로쓴다.

## 8. 두 번의 안전한 감소

p=1,2마다이전배열U^(p-1)만읽고F,L,whole/point를계산한다. 같은pass내새cell값을뒤섞지않는다.
\[
 U_n^p=\min\{U_n^{p-1},(\widehat R_n^W,\widehat E_n^W)\}.       \tag{R8.18}
\]
귀납으로Uprev가전체cell을덮으면F,L이forcing을덮고(R8.12,15,16)이새wholeupper다. 두validupper의min도valid이므로
\[
 actual(t)\le U_n^2\le U_n^1\le U_n^0,\quad t\in I_n.         \tag{R8.19}
\]
strictcontraction/solver수렴/smallδ조건없이정확히2pass에서멈춘다. strict개선의크기는실제결과가필요하다. 각pass의endpoint도같은Uprev로(R8.13,17)을계산하며whole배열과별도보존한다.

## 9. 기존 exact point caps

실제저장R7query의절대시각은blocks[k].t0+query.t,upper는query.bound다. 더강한macroendpoint는blocks[k].certificate.w_next_upper이고시각t0+H다. queries[-1].bound는ordinaryV(H)이므로이둘을혼동하지않는다.

time/δ가exactinteger인실제저장시각에서만
\[
 P_{\rm final}(t_k)=\min(P_{\rm new}(t_k),C_{\rm old}(t_k)).   \tag{R8.20}
\]
중복시각의여러validcaps도성분별min을쓴다. 최종min뒤에는다시dyadic반올림하지않아원래exactcap보다커지지않는문자그대로의no-worse를보존한다. Wholecellmin도원래exactbaseline을보존한다.

Pointcap은wholecellbound가아니다. core는point결과에만적용하고전체cell에이식하지않는다. referenceR_E는upper인증이아니므로cap으로쓰지않는다. 저장되지않은시각의cap을보간하지않는다. no-worse의대상은wholecell에서U0,point에서실제저장common-clockcertificates이며계산하지않은oldpointbound에는주장하지않는다.

## 10. 상방 산술

up_p(x)=ceil(2^p x)/2^p,p128,x>=0를사용한다. 양의곱/합각단계에서위로반올림한다. source/initial/baseline/cap은exactFraction이며최종min을다시반올림하지않는다.

R7검증exp_neg_enclosure를새dδ에한해재사용한다. d<0이고ell<=exp(dδ)<=u면eupper=min(1,up(u)),phiupper=up((1-ell)/(-d)). d>0이면exp(-dδ)의양의lower ell로eupper=up(1/ell),phiupper=up((eupper-1)/d). d0에서는e1,phiδ의정확한수학값을사용하며실제phi중간저장은up(δ)이어도상방이다. eupper의양의상방거듭제곱으로e^(dmδ)를덮는다. Cancellation이있는binary64 exp-1을사용하지않는다.

core의유한도메인은max192cells,8certificates,2passes,128bits,정수크기8192bits,|dδ|<=16이다. 실제reference근접검사의고정입력은더좁은|dδ|<=1/4에있다. 유효한exp상계와매우작은relativegap주장을구분한다.

## 11. late forcing 및 경계

Kz=-gamma*z,||z||=1,마지막epsilon동안forcing=(J/epsilon)z,초기잔차0이면
R(H)=J*(1-exp(-gamma*epsilon))/(gamma*epsilon).
잘못된전체block수축상계rho*J=exp(-gammaH)*J는epsilon→0에서실제값이J로가므로실패한다. 올바른freshforcingupper는J이며현재cellh0=1이이를유지한다. 이번고정검사는gamma1,H1,epsilon1/4,J1이다.

rho1이면h1이고혼합개선을강요하지않는다. 초기h0=1,n0빈합,d0,singular/nilpotentB,positive/negative d를명시적으로검사한다. Clock/stateorder/norm/family가다르거나all-starts조건이없으면재사용을거부한다. 정확한K-onlyrho를미계상fullreactiveoperator에적용하지않는다.

## 12. 검증 역할

엄밀성은기존인증의유효한재사용,일반증명,exact/directed산술에기초한다. Decimal80참조는productioncore를import하지않고같은cell식을독립합산한다. 저장된193binary64trajectory와의비교는samplecorroboration이며새continuousODEcertificate가아니다. 그tolerance는cap이나증명의전제가아니다.

Primary/ref각1회,각CPU60s,과학CAS1회30s이며기존R6/R7/PHYS91예산은0으로유지한다. 과학과별개인원본ZIP해시I/O예산은delivery/TRANSPORT_IO_ALLOWANCE.json에사전명시한다. 실제OSCPU는외부wrapper가imports/serialization포함측정하고첫실패도보존한다.

## 13. 문헌과 기여 한계

A.Yu.Mitrophanov(2005), “Ergodicity coefficient and perturbation bounds for continuous-time Markov chains”, Mathematical Inequalities&Applications8,159–168, DOI10.7153/MIA-08-15.
https://files.ele-math.com/articles/mia-08-15.pdf

출판사원문§2,식2.5–2.7을실제로읽었다. 시간별ergodicitycoefficient를forcingconvolution에사용하고floor-blockbound를얻는원리는기존문헌에있다. 기본원리를새정리로주장하지않는다. WU기여는저장R6의네exactcertificate를같은family로조합하고R7비선형두성분feedback및negativecoarsedamping을유지하며whole/point를구분하는고정2passoutward구현이다. 그조건부방법의채택이분자물리입력누락을해소하지않는다.
