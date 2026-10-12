# WU088_HH PHYS15 이론 연구 결과

**판정: PROMOTE_SCOPED.** PHYS14의 실제 두-half와 기존 Full 사이의 차이를 동일 COMMON의 잔차에서 직접 구성하고, 원 Full 검증을 재사용하여 유한 endpoint·온도 차이에 전달하는 정리를 완성했다. 독립 검토에서 아홉 개 주장을 채택했고, 필수 교정은 모두 닫혔다.

## 핵심 결과

기체 차이를 d=g2−gF, Full 잔차를 r=HF(g2), 실제 두-half의 integrated photon absorption을 P1+P2라 두면

\[
r=h[\mathcal B_1(g_1)-\mathcal B_2(g_2)]+V(P_1+P_2-\widehat P_F),
\quad\overline{\mathcal A}d=r.
\]

같은 COMMON과 같은 λ,b를 먼저 묶었으므로 초기 기체가 이 항등식에서 정확히 소거된다. 광자 결함은 opacity 변화, 흡수·수송 순서, 흡수 node의 시점, 기존 광자의 흡수 분할, 원 수송의 분할, 먼저 생성된 광자의 redshift, birth의 흡수 시점이라는 일곱 항으로 분리된다.

원 Full의 저장 C,B,q,S를 함께 사용하면

\[
\|S^{-1}d\|_\infty\le
\frac{\|S^{-1}Cr\|_\infty}{1-q},
\quad q=\operatorname{exact}_{64}(0.00011736830563768177),
\quad\frac1{1-q}<1.000118.
\]

이 상한은 전처리된 잔차 Cr의 원 반경 척도 노름에 적용된다. 같은 endpoint의 electron normalization에서

\[
\Delta T=\frac{C_Td_w-T_2d_e}{\Pi_2-d_e},
\quad d_e=d_x+\widehat f_2(d_{y_1}+2d_{y_2}).
\]

같은 평균 inverse와 endpoint covector를 적용하면 source·photon 각 항의 온도 기여가 전체 ΔT를 정확히 분할한다.

## 새로 얻은 물리적 구조

원 active HI cross section이 energy node에 따라 감소하므로 중간 흡수·수송 순서 항 L[R,A]Q1은 물리 영역에서 성분별 비음수다. 기존 광자와 birth의 같은-opacity chronology 항은 C1[τR²Z0−bJ]가 되어 birth node의 잔존 광자 stock과 새 생성량의 대소로 판별된다.

먼저 생성된 광자의 추가 redshift 항에서는 원 leaf 조건과 b>0, x2<1, α24>0에서 이온화 absorption이 증가하고 열 침적은 감소한다. 이 직접 forcing의 온도 사영도 음수이며, endpoint 기여는 같은 implicit inverse를 통과시켜 정의한다.

원 FT03 source를 밀도와 electron factor로 인수 분해하고 온도 정렬 사상 Ψg=(x,y1,y2,wΠ2/Π1)을 만들었다. 첫 stage와 endpoint의 미소 fhat 차이는 명시적인 He thermal correction으로 남는다. 두 stage의 차이는 작은 밀도 비, 정규화 차이 및 원 source 도함수로 구성된다.

Guard를 포함한 photon number·energy 수지에서

\[
\mathbf1^Tp=-\Delta\mathcal N,\qquad
E\cdot p=(1-\rho)(E\cdot P_1-bME_{24})-\Delta\mathcal U
\]

를 얻었다. 원 active heat identity εj=Ej−χH를 확인하여 χHx+w의 잔차에 연결했다. 이 사영에서 HH의 직접 화학·열 source는 소거되고, 실제 상태와 광자 이력에 전달된 HH 효과는 유지된다.

## 근거와 실제 수행

적용 계열은 PHYS14가 결박한 source-aligned geometric isotropic, 같은 고정 α와 λ,b∈[0,1]², 원 33개 node와 두 guards, 기존 C² source/root 전제다. Full과 실제 둘째 half의 source endpoint는 같고, captured 총 birth MF=2M도 정확히 같다.

| 수행 | 실제 결과 |
|---|---|
| 광자 exact Fraction 및 네-slot 관계 | 39개 관계, 3148개 scalar equality 통과 |
| 원 leaf의 새 sector 부호 조건 | exact 유리수 비교 통과 |
| 비선형 기체 구성 예제 | 14개 관계, 16개 scalar equality/관련 비교 통과 |
| Wolfram 유리식 정리 | 네 식의 차가 모두 0 |
| 별도 검토자의 유도·원 source·독립 산술 | 26개 검토 항목 통과, 아홉 이론 주장 채택 |
| 새 physical source·root·history 실행 | 0회 |

수학 표기 한 건을 교정했다. Photon secant의 대각행렬×스칼라 표기를 retained node별 성분식으로 바꾸고 guard를 따로 명시했다. 독립 검토자는 수정본의 계수·부호·차원을 확인했다. 원 과학 결과와 입력은 보존했다.

## 다음 연구 단위

`HH_CORRELATED_ENDPOINT_ENCLOSURE`는 이번의 실제 후속 과제다. 검토된 식과 기존 joint input·source derivative·fixed C를 사용해 r,d,ΔT/e/w/ne와 photon endpoint, sector별 기여의 검증 구간을 평가한다. 구현 계약은 `contracts/ENDPOINT_ENCLOSURE_CONTRACT.json`, 재개 지점은 `HANDOFF_KO.md`, 원 계획과의 연결은 `NEXT_DAG.json`에 있다.

전체 증명은 `theory/CORRELATED_ENDPOINT_THEORY_KO.md`, 완전한 photon 증명과 source 반응 정의는 같은 폴더의 보조 원고, 독립 판정은 `review/DECISION.json` 및 `review/REVIEW_KO.md`에 있다. LaTeX/PDF 보고서는 `report/`에 제공한다.
