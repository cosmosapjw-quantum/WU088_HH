# PHYS03: 실제 source의 문턱 remap과 birth 연령

## 1. 원자료와 계산 대상

source owner commit은
569b04cd71e45756e0fd476aef6643bd9434f4fa다.
inputs/source_survey/SOURCE_LINE_BINDINGS.json은 원격 blob,
파일 SHA-256, 구간 byte hash와 source URL을 연결한다.

선택된 member 1의 half1은
\[
t_0=1.60\times10^{11}\ {\rm s},\quad
\delta=6.25\times10^8\ {\rm s},\quad
t_1=t_0+\delta,
\]
이고 full macro 길이는 \(h=2\delta=1.25\times10^9\) s다.
source 설정은 \(h_i=10^{-14}\ {\rm s}^{-1}\)인 FLRW 특수형이다.
binary64로 주어진 leaf를 정확한 실수로 해석했다.

이번 수치 대상은 fixed node 16에 놓인 단위 basis packet의 remap
operator column이다. 그 packet을 실제 저장 이력으로 꾸며 넣지 않았다.
기체 RHS, 광자 흡수, BE root 또는 물리 trajectory를 적분하지 않는다.

## 2. 실제 owner 순서와 PHYS02 초기점의 뜻

실제 source는 다음 순서를 사용한다.

1. 외부 배경 \(a_i(t)=\exp(h_it)\)에서 characteristic redshift.
2. transported photon을 고정 에너지 격자에 선형 hat으로 remap.
3. \(t_1\)에 \(S\delta\)의 13.7 eV birth를 추가.
4. 직전 gas와 endpoint photon·density를 함께 BE-stage 입력으로 구성.
5. fixed-node cross section과 길이 \(\delta\)로 coupled BE source map.

full step은 진단이고, two-half step의 순차 결과가 accepted 경로다.
PHYS02의 old_gas와 old_point_photons는 이 중 4번의 stage aggregate다.
gas는 \(t_0\), photon은 remap/birth 뒤의 \(t_1\) 자료에 해당한다.
이 aggregate를 새 frozen ODE의 초기값으로 선언한 PHYS02 정리는 유효하다.
이를 실제 macro 이전의 동일 시각 continuous snapshot이라고 해석하면
source chronology가 달라진다.

owner에는 배경 법칙이 존재한다. 현재 비어 있는 것은 그 배경 자체가
아니라 actual accepted root와 그 위의 \((\lambda,b)\) parameter family다.

## 3. cutoff 아래 characteristic이 fixed active node로 남는 비율

고정 node 15, 16을
\[
E_-=13.599804324962749\ {\rm eV},\qquad E_*=13.60\ {\rm eV}
\]
라고 쓰고 \(\Delta E=E_*-E_-\)라 하자. provider는
\(\sigma(E<E_*)=0\), \(\sigma(E_*)>0\)를 사용한다.
이 fit cutoff 13.60 eV와 binding energy
\(\chi_H=13.598434599702\) eV는 구분한다.

FLRW에서 \(r=\exp(-H\delta)\)이고, 검증된 cell 관계는
\[
E_-<E_*r^2<E_*r<E_*.
\tag{1}
\]
따라서 actual hat의 active node weight는
\[
w_\delta=\frac{E_*r-E_-}{\Delta E},\qquad
w_{2\delta}=\frac{E_*r^2-E_-}{\Delta E}.
\tag{2}
\]
두 half remap을 합성하면 첫 half에서 아래 node로 간 성분은 redshift로
위 node에 돌아올 수 없으므로 active weight는 \(w_\delta^2\)다.

Arb 256-bit real-expression enclosure의 대표값은 다음과 같다.
모든 정확한 dyadic endpoint와 바깥쪽 반올림 decimal은
results/CHRONOLOGY_256.json에 있다.

| 연산 | node 16에 남는 weight | packet당 effective \(\sigma_H\) [cm²] |
| --- | ---: | ---: |
| 한 half remap | 0.5656076750012450 | \(3.58951392848\times10^{-18}\) |
| 한 full remap | 0.1312180649460370 | \(8.32748727801\times10^{-19}\) |
| 두 half remap | 0.3199120420203140 | \(2.03025662747\times10^{-18}\) |

characteristic 자체의 에너지는 half 후
13.599915000265624... eV, full 후 13.599830001062495... eV다.
둘 다 provider cutoff 아래여서 직접 characteristic의 에너지로
그 provider를 평가하면 0이지만, fixed-grid opacity는 위와 같이 양수다.
이는 그 provider를 기준으로 한 remap의 opacity 누출이다.
정확한 실제 원자 단면적이나 actual gas 오차에 대한 판정은 아니다.

## 4. 보존되는 모멘트와 보존되지 않는 opacity

\(K=E_*/\Delta E\)라 하면 exact algebra는
\[
\boxed{
w_\delta^2-w_{2\delta}
  =K(K-1)(1-r)^2>0.}
\tag{3}
\]
현재 값에서
\[
w_\delta^2-w_{2\delta}
 =0.1886939770742769596662556089\ldots,
\]
\[
\Delta\sigma_{\rm eff}
 =1.1975078996699213364150918\ldots\times10^{-18}\ {\rm cm^2}.
\]
즉 \(T_\delta^2\ne T_{2\delta}\)인 remap의 구체적인 한 column이다.
이 차이는 source가 추가되지 않는 transport에서도 존재한다.

반면 각 interior hat column은
\[
(1-w)+w=1,\qquad
E_-(1-w)+E_*w=E_{\rm transported}
\]
를 만족한다. 두 half에도 선형성이 유지되어 전체 photon number와
redshift된 첫 energy moment는 한 full과 같다. 그러므로 photon 수와
에너지 보존 ledger만으로 cutoff를 가로지르는 opacity functional 또는
HH 혼합 이온화 반응이 보존된다고 결론낼 수 없다.

active node 아래 neighbor까지 내려가는 시간은
\[
t_{\rm left}=\frac{\log(E_*/E_-)}{H}
 =1.4387973892481477543\ldots\times10^9\ {\rm s}>h.
\]
따라서 이번 full과 두 half 계산은 모두 식 (1)의 지정 cell 안에 있다.
큰 상대 변화의 원인은 좁은 \(\Delta E\)와 discontinuous provider cutoff의
조합이다. 일반적인 전체 광자 분포의 상대 오차로 확대하지 않는다.

## 5. 같은 photon 수라도 source energy의 연령 모멘트가 다르다

흡수 없이 동일한 FLRW 배경을 통과하는 13.7 eV birth를 별도로 보자.
constant rate \(S\), 종료 \(h\), 총 광자 수 \(N=Sh\)일 때
\[
\begin{aligned}
{\cal E}_{\rm cont}&=SE_b\frac{1-e^{-Hh}}{H},\\
{\cal E}_{\rm end}&=ShE_b,\\
{\cal E}_{2{\rm end}}&=\frac{ShE_b}{2}(1+e^{-Hh/2}).
\end{aligned}
\tag{4}
\]
둘째는 모든 birth가 최종 endpoint에 있는 schedule,
셋째는 \(h/2,h\)에 절반씩 있는 schedule이다.
단순 적분과 유한 합으로 얻으며 trajectory solver를 쓰지 않았다.

실제 leaf \(S={\rm binary64}(5\times10^{-15})\),
\(E_b={\rm binary64}(13.7)\)를 쓰면
\[
{\cal E}_{\rm cont}<{\cal E}_{2{\rm end}}<{\cal E}_{\rm end}.
\]
continuous 대비 endpoint energy excess는 약 6.250013 ppm,
two-endpoint excess는 약 3.125003 ppm이다. 세 경우 photon 수는 같다.

이 계산은 source가 어디에 얼마나 오래 존재했는지를 number ledger가
담지 못한다는 별도의 예다. 실제 BE의 ionization/HH response 또는
그 finite remainder를 제공하지 않는다. 그 leading response의 chronology
차이는 smooth_theory/PHYS03_SMOOTH_THEORY_KO.md의 causal kernel과
\(C_m\)으로 설명한다.

## 6. 수치 검증과 해석 한계

src/analyze_chronology.py는 selected JSON의 SHA-256을 고정하고,
정확한 binary64 leaf를 Arb에 넣는다. 주요 cell 관계, active-weight
순서와 source energy 순서를 strict interval inequality로 확인했다.
positive factorization은 Sympy exact algebra로 별도로 확인했다.
독립 mpmath 110자리 계산 9개가 각각 Arb의 정확한 dyadic endpoint 안에
들어갔다. decimal endpoint는 42자리로 바깥쪽 반올림했다.

이 인증은 명시한 real-expression의 enclosure이며, Rust의 각 연산별
binary64 반올림을 따라가는 native certificate가 아니다.
한 column 진단에서 전체 selected photon 분포의 gas error나
\(I_x\)의 유한시간 부호를 추정하지 않았다.

다음 실제 family 계산에는 endpoint birth의 노출시간, 두 half의
이전 상태/감도 연결, fixed-grid cutoff를 포함한 remap을 그대로 보존해야 한다.
PHYS02의 frozen continuous 부호 정리는 이 연결을 대신할 수 없다.
