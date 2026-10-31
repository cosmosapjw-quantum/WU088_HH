# R43 | EMAA HD52 비LTE 순복사 냉각, source-conditional 복원

## 문제·원전

보존된 EMAA 원본 HD RADEX(`HD.Rovibration.805a7aa5.radex`, SHA256 b0db1613425e403889c3a74f6cd9e142c562a552f1ebf05e61cbf509cd429c94)은 52개 rovibrational level, 368 Einstein-A line, H–HD 1326 collision pairs ×15 published temperatures, H⁺–HD 171 pairs ×25 published temperatures를 제공한다. H⁺ 계수는 19준위 내부에만 존재한다. H와 H⁺ 원래 온도 교집합은 5 K 하나다.

원전 DOI: https://doi.org/10.17178/emaa_hd_rovibration_805a7aa5 (EMAA 2023); H 충돌: Desrousseaux, Coppola, Lique, MNRAS 513 900 (2022), https://doi.org/10.1093/mnras/stac911; H⁺ 충돌: González-Lezana et al. JCP 157 214302 (2022), https://doi.org/10.1063/5.0128598.

비교 코드: https://github.com/grackle-project/grackle, main commit 01261db0cefc69d8d5558e76a671b0c1f6e48271, `src/clib/rate_functions.c` blob dfbab661e7c45981eed750baebff140849917152. `HDlow_rate`은 Wrathmall, Gusdorf & Flower (2007), `HDlte_rate`은 Coppola, Lodi & Tennyson (2011) 기반. 표에 들어가는 Grackle 수치는 원 공개 코드의 다항식이며 EMAA 충돌률의 대체 소스가 아니다.

## 정의와 수치식

에너지 ε_i [cm⁻¹], E_i=100 hc ε_i [J], g_i=2J_i+1. 다운워드 충돌률 n_X k_{u→l}(Tgas) [s⁻¹]은 EMAA를 사용한다. 업워드는 동일한 기체 열저장소의 microreversibility로 k_{l→u}=k_{u→l}(g_u/g_l) exp[-(E_u−E_l)/(kB Tgas)]. 광자 점유수 n̄=(exp[(E_u−E_l)/(kB Trad)]−1)⁻¹. 외부 복사 OFF는 n̄=0이지만 자발방출 A_ul은 유지.

R^{sp}_{lu}=A_ul; R^{stim}_{lu}=A_ul n̄; R^{abs}_{ul}=A_ul (g_u/g_l) n̄. K는 열방향 column generator로 ∑_i K_ij=0이다. 비LTE 고정상태는 Kp=0, ∑p_i=1, p_i≥0. 원전 52준위 경계 내에서 충돌과 복사가 서로 다른 Tgas, Trad를 가질 수 있으므로 Tgas≠Trad에서는 일반적으로 Gibbs 분포가 아니다.

순복사 냉각 per HD:

Λ = ∑_{u>l} (E_u−E_l) [A_ul(1+n̄_ul)p_u − A_ul (g_u/g_l) n̄_ul p_l] [J s⁻¹ HD⁻¹].

Λ>0이면 분자→복사 에너지 전달(가스 냉각), Λ<0이면 복사→분자(가스 가열). 고정상태 에너지 항등식: Λ = Eᵀ(C_H+C_H+)p. 비음수 H 및 H⁺ 밀도 단위 [cm⁻³], rate coefficient [cm³/s], E [J], flux [J/s]. 우주론적 스케일 팩터 진화, optical depth, HD abundance, 화학적 Q나 관측 스펙트럼은 계산하지 않는다.

## 이회차 격자·검산

온도 15개 정확한 원전 H 노드. H-only: nH={1,1000,10000,1e6} cm⁻³, Trad-boundary z={OFF,0,30,100,300} (300 조건). Joint H+H⁺: 오직 Tgas=5 K, nH는 동일 4종, nH+={1000,1e6}, boundary={OFF,30,300} (24 조건). 총 324개. 52×324=16848 점유율, 368×324=119232 각 광자전이, Grackle 고밀도(LTE) 및 저밀도 fit 비교 15행.

어떤 H⁺ 상위준위 충돌률도 채워 넣지 않는다. 원전 바깥 온도에서 보간한 수치를 source-original로 취급하지 않는다.

## 기록상 차이와 제한

과거 PR #182 텍스트 체크포인트는 324 조건 중 냉각 236 / 가열 88이라고 적었다. 현재 **명시적으로 보존한 위 격자**의 sign tally는 224 / 100이다. 70/100 K 실수치와 Grackle 저밀도 비율은 역사적 게시값에 일치한다. 원본 R43 소스 master를 현재 세션에서 확보하지 못하여 이전 격자와 차이의 원인을 확정하지 못한다. 과거 상태를 조용히 수정하거나 두 ZIP이 byte-identical이라고 주장하지 않는다. 이에 따라 이 복원본은 새 provenance SHA의 scoped dataset이다.

R6/C9 별도 저자 검증 NOT_RUN, WU canonical 34/49 unchanged, HH_R10 OFF, L4 false, production HOLD, no main merge.
