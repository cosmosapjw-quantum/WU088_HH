# WU088_HH: 외부 계수 경로의 채팅 선행연구

2026-10-04. 상태: DERIVED_AND_BOUNDED_REFERENCE_CHECKED; 소비자 적용·물리 감도·구간 인증은 아직 아니다. 출판 경로는 `docs/atomic_reionization_handoff_20261004_v1/threads/WU088_HH/`이다. 이 문서의 모델 결정은 새 fastest lane에 관한 것이고 기존 원자 인증을 수정하지 않는다.

## 1. 실제 회수한 최신 상태

named branch `research/r31ao-unequal-order-ladder-20260930`, commit `4502a46c0111307d139aa0f0b9b2cd721e559a9d`, tree `4fabdc4a00b44efb8fbfdb34a4c0875d5f0e25c4`를 원격 조회했다. FD2 네 full-field callback과 네 저장 구간 비교가 끝났다. 이전 SSOT의 full-field 0회는 이 최신 관측에 의해 갱신된다. 후보는 finite/consistent이나 폭이 크고 모든 component가 0을 포함한다. 새 적분 0회, accepted 24/289, missing 265 unbounded, epsilon_C/R=null, B22 OPEN_UNDETERMINED, scientific/production admission=false다. 소모된 FD2 scope를 다시 실행하지 않는다.

C0는 49-row channel crosswalk와 22검사를 완료했지만 application domain/observable budget와 exact receiver implementation authority는 미해결이다. C1는 represented gap arithmetic과 24검사를 완료했지만 continuous target은 UNRESOLVED_INPUTS다. 이 원자료들의 20/289는 당시 역사값이며 최신 24/289와 혼합하지 않는다. 기존 PR #33이 현재 branch를 소유한다. 이 패키지로 새 science PR이나 merge가 이루어졌다는 뜻은 아니다.

## 2. 반응 의미와 closure

종 순서 (HI,HII,Hminus,e_free)에 대한 event stoichiometry는 다음과 같다.

| process_id | ν | 자유전자 | baseline 역할 |
|---|---|---:|---|
| HH_COLLISIONAL_IONIZATION | (-1,+1,0,+1) | +1 | 희박 Maxwell H/He chemistry 후보 |
| HH_ION_PAIR | (-2,+1,+1,0) | 0 | Hminus 없는 state에서는 비활성; 제거 closure가 필요 |
| HPLUS_H_RESONANT_CX | (0,0,0,0) | 0 | 동일 단일 유체의 aggregate chemistry 0; drift energy·momentum은 별도 |
| HH_ELASTIC | (0,0,0,0) | 0 | 수송·열평형 closure 검증용; 이온화율 아님 |
| HH_SPIN_EXCHANGE | (0,0,0,0) | 0 | 21 cm hyperfine populations용; bulk free-electron source 아님 |

핵수 row (1,1,1,0), 전하 row (0,1,-1,-1)와 모든 ν의 내적은 0이다. frozen positive-energy L2 pseudostate population이나 ionic trial population을 flux-normalized ionization으로 바꾸는 사상은 없다. singlet/fixed-plane 계산도 unpolarized total cross section으로 자동 변환하지 않는다.

비상대론적, 공통 bulk velocity, 등방 Maxwell 분포에서 E=μv_rel²/2, θ=k_B T_rel, T_rel=μ(T_a/m_a+T_b/m_b)라 놓으면

\[
k=\sqrt{8/(\pi\mu)}\theta^{-3/2}\int_{E_0}^{\infty}E\sigma(E)e^{-E/\theta}\,dE.
\]

이는 각 분포를 정규화한 상대속도 평균에서 얻는다. [σ]=cm², [k]=cm³/s다. 입자 event cross section으로 새 k를 정의하면 동일 pair의 unordered factor를 정의해야 하지만 **Grackle k57 network 자체의 source는 R=k57*n_HI²**다. 여기에 1/2를 다시 넣지 않는다. k58은 중성 He가 collider인 다른 process이며 R=k58*n_HI*n_HeI다. 코드의 He mass-density /4를 number-density에 다시 적용하지 않는다.

## 3. 공개식과 정확한 조각별 미분

Grackle 3.4.1 `rate_functions.c`의 units=1인 k57은 T>3000K에서
\[
k_L=1.2\times10^{-17}T^{1.2}e^{-157800/T}\quad[\mathrm{cm^3/s}]
\]
이고, T<=3000K에서는 macro `tiny=1e-20`이다. `grackle_macros.h`도 실제 읽었다. **이는 smooth cutoff가 아니라 불연속 인공 floor**다. 3000K 오른쪽의 식은 약 1e-36 수준이다. 일반 units 호출은 high branch만 /units를 하므로 units=1로 CGS를 받은 후 SI 변환하는 wrapper가 해석상 단순하다. Grackle의 tabulated/interpolated solver path와 direct function API를 동일하다고 가정하지 않는다.

Glover(2015)가 threshold를 고친 Kunc–Soon 대안은
\[
k_K=4.65\times10^{-21}T^{3/2}e^{-157800/T}\quad[\mathrm{cm^3/s}].
\]

두 식을 k=A T^p exp(-B/T)로 쓰면
\[
k'=k(p/T+B/T^2),\quad
k''=k\{(p/T+B/T^2)^2-p/T^2-2B/T^3\}.
\]

floor의 열린 내부에서는 k'=k''=0이며 3000K에서 도함수는 존재하지 않는다. interval이 경계를 포함하면 분기별 value enclosure를 합쳐야 하며 smooth Taylor bound를 그대로 쓰면 안 된다. floor를 0이나 smooth extension으로 바꾸려면 별도 provider version과 감도 비교를 만들고 원 Grackle parity를 주장하지 않는다. corrected KS에는 임의의 3000K cutoff를 붙이지 않는다.

고에너지 실험에서 threshold로 외삽한 문헌 계수들 사이의 차이는 물리 모델 감도다. 두 식의 최소/최대가 실제 rate를 엄밀히 포함한다는 증거는 없다. T-domain은 rei가 실제 쓸 domain과 출처의 지원/외삽 상태를 별도로 기록해 확정해야 한다. 여기 사용한 4000,1e4,1e5K는 도함수 검산점이며 physical domain admission이 아니다.

## 4. 열·결합에너지·온도 계약

HI+HI→HI+HII+e에서 R=k*n_HI²라 놓으면 S_HI=-R, S_HII=S_e=R, S_npart=R다. ground HI의 결합에너지 기준을 0으로 잡고 이온화 상태를 χ_H 높게 정의하면
\[
\dot u_{bind}|_{HH}=+\chi_H R,\qquad \dot u_{th}|_{HH}=-\chi_H R.
\]

복사 없는 isolated event에서 두 항의 합은 0이다. 표준 fit의 collisional-ionization cooling이 이미 χ_H R를 소유하면 별도 threshold term을 더하지 않는다. source+heat owner를 하나로 묶거나 중복 소유를 거절한다. χ_H는 consumer의 같은 constants registry를 사용한다. η-factor나 photo excess energy를 이 충돌에 잘못 적용하지 않는다.

u_th=3 n_part k_B T/2인 단일온도 단원자 모형에서는
\[
\dot T|_{chem}=\frac{2S_{u,th}}{3k_B n_{part}}-\frac{T}{n_{part}}S_{npart}.
\]

이 식은 국소 chemistry 부분만이다. 팽창·Compton·재결합·광가열 등은 각 owner의 식을 별도로 더한다. 온도 ODE에서 새 자유전자 때문에 생기는 n_part 변화를 빠뜨리지 않는다. 분자/상태별/다온도 모형에는 이 단원자식이 그대로 적용되지 않는다.

## 5. paired sensitivity와 종료 조건

고정한 source/IC/geometry convention에 대해 ΔO_j=O_Bianchi(k_j)-O_FLRW(k_j)를 각 동일 provider j로 계산한다. 같은 uncertainty parameter/temperature-rate curve를 두 geometry에 공유한다. 독립 무작위 계수로 양쪽을 perturb해 불필요한 차이 오차를 만들지 않는다. 각 branch/domain을 방문한 로그, |ΔO_j-ΔO_base|, 각각의 absolute-history variation, numerical enclosure를 별도 출력한다. atomic model spread와 적분 numerical error를 하나의 rigorous interval이라고 부르지 않는다.

종료는 모든 atomic uncertainty가 tiny Bianchi signal보다 작다는 보편 조건이 아니다. 선택 claim(부호/크기/검출성/정성 변화)이 등록된 model family에서 안정적이며 consumer가 정한 accuracy budget과 비교 가능한 경우 `CLOSED_FOR_SELECTED_REIONIZATION_CONSUMER_EXTERNAL_PROVIDER`다. 불안정하면 해당 observable의 claim을 낮추거나 영향을 지배하는 process/domain만 legacy lane에서 재개한다.

## 6. 이 채팅에서 실제 완료한 범위

`portable_reference.py`는 표준라이브러리만 쓰는 분석식·source reference다. `verify_prework.py`를 실제 실행해 보존 row, free-electron count, no-extra-half, cutoff, invalid domain refusal, 일차·이차 도함수 finite differences, 에너지/온도 구성, zero density의 34 finite checks가 통과했다. 결과는 PREWORK_CHECKS.json이다. 원자적분·우주론 history·Grackle native build 0회다. 따라서 이 구현은 portable reference이며 production/physical validation이 아니다.

원전: Grackle tag https://github.com/grackle-project/grackle/tree/grackle-3.4.1 ; Glover https://arxiv.org/abs/1504.00514 ; 상세 provenance와 SHA는 SOURCE_REGISTRY.json 및 legacy_sources/MANIFEST.json.
