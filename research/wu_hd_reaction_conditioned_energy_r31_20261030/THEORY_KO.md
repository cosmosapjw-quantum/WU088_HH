# WU R31 | 제한된 H⁺–HD 화학반응 전 회전 에너지 수지: 구성적 유도

**2026-10-30 KST.** 다음 결론은 원본 2022 SQM 충돌·반응률과 2022 Sung 실험 적합 선 중심을 결합한 **고정 열저장고의 제한적 HD tracer** 안에서 유도한 것이다. 전체 우주 냉각, chemical Q, 역반응, radiative transfer는 대상이 아니다. 원본 상위 근거는 WU R30 `72d189752d81febe48292e7532d0e96beac51f7f`, 불변 SOURCE ZIP SHA256 `d1aa63fedb6527d6aab59df447f1f2b4aa557fab98789b962464a2b86bb5bf16`이다.

## 1. 물리적 입력과 차원

HD 상태 공간은 진동 v=0, 회전 J=0,1,2,3,4이다. GL2022 (*J. Chem. Phys.* 157, 214302, 2022; DOI 10.1063/5.0128598)의 7개 source-printed 정확 온도 노드 T = (55,105,255,505,1005,2005,3005) K에서 350개의 H⁺+HD→D⁺+H₂(v′=0,J′=0..9) 반응률과 70개 하향 H⁺–HD 충돌률을 이용한다. 각 열반응률은 cm³/s, 외부 지정 양성자 밀도 n은 cm⁻³이며 사건률은 s⁻¹이다. 중복 J=5 표와 근거가 의심되는 T=15,1505,2505K를 일절 보간·교정하지 않는다.

Sung et al. (*JQSRT* 295,108412, 2023 표기, 온라인 2022; DOI 10.1016/j.jqsrt.2022.108412)에서 REC #164가 입력한 네 fitted 회전선 중심 (89.22792,177.84141,265.24055,350.85401) cm⁻¹을 사용한다. 여기서 \(\epsilon_0=0\), \(\epsilon_j = h c (100\,{\rm m}^{-1}/{\rm cm}^{-1})\sum_{r=1}^{j}\tilde\nu_r\) [J]이다. \(h,c,k_B\)는 SI 상수다. Einstein A (s⁻¹)는 REC161/LAMDA 원문 표시값을 재사용한다. 네 fitted 선 중심은 296 K 실험값의 전사로서, 전 온도 T에서 기체 압력 이동이 없다는 **조건부 모델 선택**이며 다온도 실측 관측 스펙트럼이 아니다.

## 2. 상세평형 및 생성자

GL2022 원본 하향 \(k_{j\to i}^{\downarrow}(T)\) (j>i)에 대해 상향률은 원본 인쇄값이 아닌 열평형 관계로 **유도**한다:

\[
 k_{i\to j}^{\uparrow}(T)=k_{j\to i}^{\downarrow}(T)
 \frac{2j+1}{2i+1}\exp[-(\epsilon_j-\epsilon_i)/(k_B T)].
\]

흡수되기 전 HD의 확률 열벡터 \(x(t)\)는 \(\dot x=Gx\), 초기조건 \(x(0)=e_s\), 반응 도달 뒤 HD 상태가 사라지는 absorbing 경계로 정의한다. \(G_{ij}\) (i≠j)는 비반응 충돌 사건률에 인접 자발복사 전이를 추가한다. 대각선은 모든 전이률 및 제한된 반응 이탈률 \(r_j=n\sum_{k=0}^{9} w_k q_{jk}(T)\)의 음의 합이다. \(w_k\)는 `raw_SQM`의 1 또는 Eq.6–7의 홀 3/4·짝 1/4이다. 모든 선택 상태에서 \(r_j>0\)이므로 \(-G\)는 이 범위에서 invertible transient M-matrix이다. 점유시간은
\[m=\int_0^\infty e^{Gt}e_sdt=(-G)^{-1}e_s\quad [\mathrm s].\]

## 3. 화학반응 *직전* 회전 에너지의 세 갈래

충돌에 의해 **양성자 운동 에너지 열저장고가 얻는** 부호 있는 에너지 기대값은
\[
 B=\sum_{j>i}(\epsilon_j-\epsilon_i)n\left[k_{j\to i}^{\downarrow}m_j-k_{i\to j}^{\uparrow}m_i\right]\quad [\mathrm J/initial\ HD].
\]

자발복사의 에너지 기대값과 반응이 발생한 **직전 HD** 회전 에너지는
\[
 R=\sum_{j=1}^{4}(\epsilon_j-\epsilon_{j-1}) A_jm_j,
 \qquad F=\sum_{j=0}^{4}\epsilon_jr_jm_j.
\]

**정리 (제한적 HD 회전 에너지 보존):** \(\epsilon_s=B+R+F\).

*증명.* \(E=(\epsilon_0,\ldots,\epsilon_4)^\top\)라 두면 \((-G)m=e_s\)를 좌측에서 \(E^\top\)로 수축해 \(\epsilon_s=-E^\top Gm\)을 얻는다. 임의 충돌 화살표 j→i는 \(-E^\top Gm\)에 \((\epsilon_j-\epsilon_i)n k_{j\to i}^{\downarrow}m_j\)를, 역방향은 음의 \((\epsilon_j-\epsilon_i)n k_{i\to j}^{\uparrow}m_i\)를 기여한다. 자발복사 j→j-1은 \((\epsilon_j-\epsilon_{j-1})A_jm_j\), 최종 HD 흡수 반응 j는 \(\epsilon_jr_jm_j\)를 기여하므로 세 항으로 정확히 분해된다. \(x(t)\to 0\)는 \(r_j>0\)에서 성립한다. QED.

이 보존은 **반응 후 H₂ 회전 에너지, D⁺+H₂ 생성물의 운동 에너지, 반응 Q**까지 보존했다고 말하지 않는다. 그 미측정 분배는 \(F\) 바깥이다. 음의 \(B\)는 열저장고가 HD를 여기시키는 방향으로 에너지를 공급함을 뜻하며, 물리적 가열률(시간당 W/m³)로 오인하면 안 된다. \(\epsilon_s\)가 0인 J=0에 대해서는 \(B=-(R+F)\le0\)가 엄밀한 특수 경우다.

## 4. 물리적으로 공정한 spin 정책 비교

기존 `n/ncrit`에 동일한 수치를 넣으면 두 정책에서 **물리적 양성자 밀도 자체가 다르다**. 신규 R31은 각 source T마다 동일한 \(n_{\rm Hp}=n_{crit}^{spin}(T,J=2)\)를 고정한 채 `raw_SQM`과 `Eq6-7_spin_effective`를 각각 풀어 7 T × 5 초기 J = 35개의 짝 비교를 추가했다. 따라서 두 정책의 차이는 density confounding 없이 source-defined spin weighting의 모델 민감도를 나타낸다. 이것은 불확실성의 신뢰구간이 아니다.

## 5. 계산 범위와 불변식

기본 7 T × 2 정책 × 3 `n/ncrit` × 5 초기 J = 210개 사례에 대해 10개의 독립 충돌쌍 = 2,100개 기대 충돌 열전달, 5개의 반응 종단 J = 1,050개 종단에너지, 4개의 radiative J→J-1 = 840개 line photon energy를 생성한다. 모든 값은 초기 HD 분자 1개당 통합 기대 에너지 [J]다. 신규 35 matched-density pairs는 주 모델과 같은 원본 상태률을 사용하지만 추가된 물리적 밀도 비교 실험이다.

검사: \(\sum_j r_jm_j=1\); \(\max|\epsilon_s-(B+R+F)|=2.02373107437565\times 10^{-34}\) J (210 사례), 75자리 mpmath 독립 소스 재조립 및 역행렬 210 사례 × 3 신에너지 =630 비교, 최대 scaled discrepancy \(9.9581495611029228\times 10^{-13}\), 절댓값 \(3.03224101172864869\times10^{-33}\) J. Wolfram 2-state 두 초기조건의 상징적 보존식 `{True,True}`. 이는 **같은 작성자의 독립 구현·CAS 검사**이며 distinct-author R6/C9가 아니다.

## 6. 관련 원전과 새로운 물리적 의미의 한계

- González-Lezana, Hily-Blant & Faure (2022), *JCP* 157 214302, DOI https://doi.org/10.1063/5.0128598 : 원본 통계 양자 산란 rate 표와 저밀도 방사 냉각함수. **R31은 이 논문이 이미 수행한 전체 cooling function을 새로 발명했다고 주장하지 않는다.** 새 계산량은 제한된 화학적 흡수 *전*의 signed collisional energy와 종단 HD 회전 에너지의 결합 분해다.
- Sung et al., *JQSRT* 295 108412, DOI https://doi.org/10.1016/j.jqsrt.2022.108412 : R30을 통해 계승한 네 measured fitted line centres. 원본 PDF raw와 full covariance 미확보.
- EMAA official DOI https://doi.org/10.17178/emaa_hd_rovibration_805a7aa5 : 52 HD 수준, H+에 171 transitions × 25 T 메타데이터는 검증되었으나 원본 numeric ASCII **미확보**. 따라서 GL2022 printed 70 source pairs와 동등한 숫자라고 인정하지 않는다.
- Velilla et al. (2008), DOI https://doi.org/10.1063/1.2973629 : PES 원논문의 EPAPS Fortran 출처 확인, Fortran/원시 \(\sigma(E)\), isotope-specific energy zero 미확보. 물리적 Q 미승인.

아직 고정 bath에 대한 실제 농도 방정식, reverse reactions, H₂ product vibrational completeness, 상호작용 상대별 입자 보존 및 \(L_4\) 검증은 확보하지 않았다. 정본 DAG는 34/49, R31 보조범위 1/1 별도, 실제 production off.