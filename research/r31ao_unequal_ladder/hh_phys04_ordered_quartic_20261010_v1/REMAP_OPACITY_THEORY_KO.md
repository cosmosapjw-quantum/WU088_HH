# PHYS04: fixed-grid remap, opacity와 열 가중 혼합 quartic

## 1. 계산 대상과 source identity

Owner commit 569b04cd71e45756e0fd476aef6643bd9434f4fa의 fixed-grid
redshift -> endpoint birth -> coupled BE 순서를 보존한다.
inputs/SELECTED_SOURCE.json의 SHA-256은
26a340065a9a99d02903bf0cc008baaf6ade00d2e845beb9d2b0b7d801316494다.
파일의 binary64 leaf를 정확한 실수로 해석한다. Native 연산별 반올림은
재현하지 않았다.

첫 수치 실험은 이 파일의 25개 positive photon group을 입력으로 하는
순수 remap operator 진단이다. 이 spectrum은 PHYS03에서 확인한 half1
preBE 조립값이다. 실제 macro 이전의 raw initial state나 gas trajectory로
간주하지 않는다. 두 번째 실험은 같은 gas 상태와 source grid를 사용하되
old photons를 0으로 둔 별도의 local-coefficient 특수화다.
두 실험의 초기 photon 상태를 혼동하지 않는다.

## 2. 한쪽 active remap

한 FLRW proper-time increment h>0에서 r(h)=exp(-Hh)이다.
node j의 이동 에너지가 바로 아래 node와 자신 사이에 있으면

\[
E_{j-1}<E_jr(h)<E_j,\qquad
\alpha_j=\frac{HE_j}{E_j-E_{j-1}},
\]

\[
L e_j=\alpha_j(e_{j-1}-e_j),\qquad
s(h)=\frac{1-e^{-Hh}}{H},\quad s(h)|_{H=0}=h
\]

로 쓸 수 있다. 가장 아래 active node에서 inactive로 나가는 부분은
active block 밖의 outflow로 기록한다. 따라서

\[
\boxed{R_A(h)=I+s(h)L_A}
\tag{1}
\]

가 그 cell 안에서 정확하다. 이는 일반적으로 exp(hL_A)가 아니다.

이 결과의 active block은 HI provider cutoff 13.60 eV 이상의 node다.
현재 입력의 0..15번 node는 HI/HeI/HeII 단면적이 모두 0이고, redshift가
이들을 active sector로 돌려보내지 않는다. 이 조건에서 gas와 결합하는
opacity/heating observable을 active quotient에서 정확히 계산할 수 있다.
He nonphoto/thermal 상태를 버리는 뜻은 아니다.

전체 원 photon+guard 배열에는 식 (1)을 그대로 쓰지 않는다.
Owner는 E<10eV인 packet을 lower guard로 전부 내보낸다. 따라서
최저 node E=10eV에 처음 놓인 packet은 임의의 h>0에서 즉시 guard로
이동하고, 그 원 배열에서는 R(0+)가 I가 아니다. Guard의 photon 수와
에너지는 별도 장부로 운반한다. 수치 witness는 이 실제 guard 규칙을
포함한 전체 25-group hat map을 사용한다.

## 3. Full/two-half의 정확한 operator 결함

h=2d라고 하자. s(2d)=2s(d)-H s(d)^2이므로

\[
\boxed{
R_A(d)^2-R_A(2d)=s(d)^2(L_A^2+HL_A).
}
\tag{2}
\]

이 식은 cell 조건 안에서 정확하다. 시간의 한쪽 전개는

\[
s(h/2)^2=\frac{h^2}{4}-\frac{Hh^3}{8}
+\frac{7H^2h^4}{192}+O(H^3h^5).
\tag{3}
\]

Q=L_A^2+HL_A라 놓으면 임의의 fixed-node weight w와 photon vector p에 대해

\[
\boxed{
\Delta{\cal O}_w
=w^\mathsf T(R_A(h/2)^2-R_A(h))p
=s(h/2)^2 w^\mathsf TQp.
}
\tag{4}
\]

각 column의 값이 양수라고 다른 column 또는 양의 spectrum 합까지
양수인 것은 아니다. 실제 Q는 비대각 성분에 서로 다른 부호를 갖는다.
Transport와 fixed-node absorption의 비가환 항도
\([{\rm diag}(\sigma),L_A]_{ij}=(\sigma_i-\sigma_j)(L_A)_{ij}\)
로 드러난다. 에너지 경사가 커지거나 provider cutoff가 있는 곳에서는
photon number만으로 이 항을 제어할 수 없다.

## 4. 선택 spectrum의 새 엄밀 수치

H=binary64(1e-14) s^-1, h=binary64(1.25e9) s이고,
active node 16..24의 full-step cell 부등식을 정확한 구간으로 확인했다.
단면적과 photon stock도 inputs/SELECTED_SOURCE.json의 leaf다.

Opacity functional을
\({\cal O}_\sigma=\sum_j\sigma_{{\rm HI},j}p_j\),
excess-energy weighted functional을
\({\cal O}_{E}=\sum_j\sigma_{{\rm HI},j}(E_j-\chi_H)p_j\)라 정의한다.
단위는 각각 cm² photons/H, eV cm² photons/H다.

| Observable | Full remap | Two-half remap | Two-half minus full |
|---|---:|---:|---:|
| HI opacity | 2.4108813685103331e-19 | 2.4108808093629068e-19 | -5.5914742628126907e-26 |
| HI excess-energy weight | 1.9191991429028059e-20 | 1.9191990889708504e-20 | -5.3931955506219376e-28 |

Full로 나눈 상대 변화는 각각 -0.23192656162371124 ppm,
-0.028101281571357316 ppm이다. 이 표는 midpoint 요약이고
정확한 유리수 끝점과 48자리 외향 decimal은
results/REMAP_OPACITY_EXACT_V1.json에 있다.

왜 PHYS03의 단위 문턱 column 결과와 부호가 다른가?
선택 spectrum으로 가중하면 node16의 양의 기여는
+1.1492751245328895e-24이고 node17의 음의 기여는
-1.2052810061249352e-24이다. 나머지 node18..24의 작은 양의 기여를 더해도
합은 음수다. 단위 column의 +0.18869 weight defect를 spectrum 전체에
적용하는 추론은 성립하지 않는다.

식 (3)의 quartic polynomial을 식 (4)에 넣었을 때, 이 지정 h에서
정확한 remap defect에 대한 상대 remainder는

\[
-6.1035406325009134\ldots\times10^{-17}
\]

이다. 이는 pure remap operator의 특별한 scalar factor에 대한 bound다.
Mixed gas response의 고차 remainder나 실제 gas trajectory의 오차 bound가 아니다.

각 interior hat column의
\(\sum w_j=1,\ \sum E_jw_j=E_{\rm transported}\)와 guard 에너지 운반에 의해
photon 수 및 redshift된 첫 에너지 모멘트는 보존된다.
Independent Decimal150 direct-hat 계산에서도 full/two-half의 네 모멘트
residual이 사전에 정한 1e-135보다 작았다. 이 decimal 검사는 algebraic
conservation proof와 구분한다.

## 5. Thermal-weighted source-remap mixed quartic

quartic/PHYS04_ORDERED_QUARTIC_KO.md 식 (11)–(13)을 사용한다.
이 절의 추가 가정은 P0=0, U0=V0=W0=0, frozen external coefficients,
constant birth, 지정 source 외 transported photon 내부 생성 없음이다.
실제 nonzero-photon spectrum의 전체 gas 결함으로 읽지 않는다.

\[
q=n_H(1-x)^2 k(T),\quad
\Pi=1+f_{\rm He}+x+f_{\rm He}(y_1+2y_2),
\quad T=\frac{2E_{\rm eV}w}{3k_B\Pi},
\]

\[
\nu=\frac{d\ln k}{d\ln T}=1.2+\frac{157800\ {\rm K}}T,\qquad
\Xi_j=\frac{1-x}{\Pi}\nu
\left[1-\frac{\Pi(E_j-\chi_H)}{w}\right].
\]

HH q에는 1/2가 없다. A_j=c n_H sigma_j라 두면
two-half mixed quartic 중 L에 의존하는 gas x항은

\[
\boxed{
\Delta_L[h^4]\partial_\lambda\partial_b x_{\rm two}
=-\frac q{16}\sum_j A_j(4+\Xi_j)(LB)_j.
}
\tag{5}
\]

이 식의 B에는 S_*가 들어간다. B를 단위 packet으로 놓은 coefficient를
보고할 때는 마지막에 S_*를 곱해야 한다. H/He particle-number feedback은
Pi를 통해 남아 있고, E_j-chi_H가 thermal weighting을 바꾼다.

13.7eV의 first birth가 다음 half에서 node24->23으로 redshift되면
\[
LB=S_*\alpha_{24}(e_{23}-e_{24}).
\]
현재 leaf에서
\[
\sigma_{23}(4+\Xi_{23})-\sigma_{24}(4+\Xi_{24})>0.
\]
따라서 식 (5)는 음수다. 첫 birth가 더 낮은 에너지 node로 이동하면
이 설정에서 HI opacity가 커지고, 광자당 excess heat는 작아져
음의 HH 혼합 반응을 강화하는 항이 된다.

C2=13/8+Xi_24/2와 두-half의 inherited leading cubic
\(-\lambda S_* b\,c n_H\sigma_{24}q C_2 h^3\)로 나눈,
고립된 remap quartic 항의 비는

\[
\frac{h\alpha_{24}
 [\sigma_{23}(4+\Xi_{23})-\sigma_{24}(4+\Xi_{24})]}
 {16\sigma_{24}C_2}
=5.3049511108096286866\ldots\ {\rm ppm}
\tag{6}
\]
이다. 분자와 cubic이 둘 다 음수이므로 비는 양수다.
이 수치는 실제 total quartic, full/two-half finite error, 또는
전체 HH 반응의 relative error가 아니다. Density drift, nonphoto/thermal
evolution, old photon/old sensitivity 항은 일반 quartic 식으로 처리해야 한다.

## 6. 검산과 한계

src/remap_opacity.py는 Fraction 산술로 모든 binary64 leaf를 정확히
가져오고, 0<=x<=1의 exp(-x) 교대급수에서 짝수 16차 partial sum을
상계, 다음 홀수 17차 partial sum을 하계로 사용한다.
Small Hh에서 감산 소실은 없다. Exact rational factorization과 signed
column 합으로 interval dependency의 불필요한 팽창도 피한다.

Independent witness는 Decimal.exp 150자리와 원 에너지 hat의 직접
full/two-half 적용으로 얻었다. L, L² 또는 식 (2)의 결함식을 재사용하지 않는다.
여섯 개 observable witness가 exact endpoint 안에 있다.
H=0 및 zero-vector 극한, cell 조건, inactive의 H/He sigma=0도 확인했다.
근거 상태는 derived + rigorously bounded real-expression +
implementation-verified다. Native rounding, BE trajectory 및 actual finite
mixed sign은 미평가다.
