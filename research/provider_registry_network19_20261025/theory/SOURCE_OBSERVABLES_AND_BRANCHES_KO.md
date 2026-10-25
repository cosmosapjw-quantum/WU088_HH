# 원자료의 관측량·방향·가지와 finite event 사상

## 결과와 적용 범위

원 PNG의 19개 ID를 유지하면서, 공급자가 제시한 관측량과 event compiler가 검증하는 정수 열을 각각 추적한다. 실제 원자료가 있는 방향에서도 열의 전하·바리온·전자 렙톤수 보존이 반응률, 에너지 침적 또는 핵 Q를 승인하지 않는다. R1의 질량 관례·Q·공분산 유도는 `../../provider_registry_20261025/theory/REGISTRY_ENERGY_AND_LEPTONS_KO.md`를 변경 없이 재사용한다.

## 1. 대상 ID와 물리 방향

원 계약의 가역 화살표는 두 방향의 자료 의무를 만든다. 서로 겹치는 (7,13), (8,12), (11,19)는 모두 원래 ID를 유지하고, 같은 물리 방향을 공유한다는 별칭만 기록한다. 예를 들어 ID8의 역방향과 ID12의 정방향은 같은 `p+n→D+γ` 계열이다. 동일한 활성 물리 방향에 여러 대안 공급자를 중복으로 더하지 않는다. 원문에 단방향으로 주어진 ID12·13·19의 추가 역방향 자료는 별도 evidence이며 원래 대상 수를 늘리지 않는다.

이 계수법으로 원 19개 항목은 28개 명시 방향을 갖는다. 뒤에 만들어진 18-family 조건부 모형은 그 핵·약반응 부분을 13개 계열로 모으고 5개 closure를 더한 별도 집합이다. 전자 반응 ID1–3은 이 18개 집합으로 대체되지 않는다. 출처: `../sources/recovered_network/TARGET_NETWORK_19_c9deb93.json`, `REI18_NUCLEAR_NETWORK_CONTRACT_9620e1f.json` 및 원 PNG.

## 2. 동일한 숫자 형식으로 섞으면 안 되는 공급자 관측량

| 원자료 | native 관측량 | 보존할 조건 | 이 단계의 계산 |
|---|---|---|---|
| NACRE-II 표 | $N_A\langle\sigma v\rangle(T_9)$ | 표의 온도, 단위, adopted/low/high, 가지 | 숫자 문자열 전사만 |
| JENDL·NIST 표 | 특정 속도/에너지의 단면적 | channel cross section과 total absorption 구별 | 실제 표의 숫자와 단위만 |
| S(0) 논문 | 지정 모형/전이의 저에너지 S-factor | E1 등 전이, 외삽과 모형 오차 | 상수 전사만 |
| ENDF MF3 | 입사 광자 에너지의 단면적 | MAT/MF/MT, native interpolation와 지지 구간 | native knot 전사만 |
| ENDF MF6 | 반응당 생성물 수율 및 분포 | ZAP/LIP/LAW, 수율의 자체 에너지 격자 | native yield 전사만 |
| 광자 빔 실험 표 | 빔 분포로 평균한 가지별 단면적 | 빔 에너지 분포, 통계·계통 불확실성 | 원 평균값 전사만 |

NACRE-II의 $T_9=T/(10^9\,\mathrm K)$와 기존 조건부 계산의 100 K/10000 K는 다른 정의역이다. native 표 아래의 온도에 대해 새 값을 만들지 않았다. low/high는 평가자가 제시한 대안/모형 범위이며, 별도 통계 정의 없이 신뢰구간이나 상관 공분산으로 재해석하지 않는다. 출처: [NACRE-II 원문](https://arxiv.org/abs/1310.7099), `../sources/primary/PROVIDER_ROWS.json`의 각 table/section/line locator.

비축퇴·독립 입자·명시된 열분포 가정 아래 이체 반응의 체적 event flux는

$$\mathcal R_f=\frac{n_a n_b}{1+\delta_{ab}}\langle\sigma v\rangle_f.$$

따라서 같은 D+D 방향에서 소모 벡터의 $\nu_D=-2$와 event flux의 동일 입자 계수는 서로 다른 항목이다. native $N_A\langle\sigma v\rangle$ 표를 그대로 초당 event flux로 읽지 않는다. 위 식은 구현 연결식이며, 이 단계에서 밀도·온도·시간을 대입하거나 새로운 반응률을 계산하지 않았다.

## 3. ENDF의 생성물 수율과 배타적 가지

native file의 particle production representation은

$$\sigma_{\mathrm{prod},j}(E)=\sigma_{\mathrm{MT5}}(E)Y_j(E)$$

형태를 갖는다. 두 인자는 서로 다른 native 에너지 격자와 interpolation 정보를 가질 수 있다. 이 registry는 인자별 원표를 보존하고, 공통 격자 재구성이나 곱셈을 실행하지 않는다. $Y_j$는 생성물 multiplicity이므로 자동으로 서로 합이 1인 가지 확률이 아니다.

회수한 H2 파일은 MF3/MT50으로 `D(γ,n)p`를 직접 지정한다. source의 QI/QM 필드는 원 문자열 `-2.224600+6` eV로 남기고, 별도 bare/atomic mass ledger 또는 침적 에너지로 승인하지 않는다. He3 파일의 MF1 설명은 deuteron production을 `He3(γ,p)D`에 연결한다. 따라서 MF3/MT5와 deuteron MF6 yield는 **인수 형태의 가지 후보**로 보존된다. Li7 파일은 총 photoabsorption과 inclusive particle/residual production을 제공한다. 이 자료만으로 모든 triton 또는 alpha 생성 사건이 배타적 `Li7(γ,t)He4`임을 부여하지 않는다.

출처: [공식 NNDC ENDF/B-VIII.1 photonuclear 자료](https://www.nndc.bnl.gov/endf-releases/?sublibrary=gammas), `../sources/photon_native/raw/`의 MAT128·225·328 원파일, `PROVIDER_ROWS.json`의 줄별 locator. 실제 archive member만 부분 스트림으로 회수했으므로 전체 141 MB 아카이브의 checksum을 검증했다고 주장하지 않는다.

## 4. 빔 평균 단면적과 소비자 광반응률

실험 $j$가 광자 빔과 detector efficiency/acceptance를 포함한 정규화된 response 가중치 $w_j(E)$를 사용한다면 평균 관측량은

$$\bar\sigma_{j,f}=\int w_j(E)\sigma_f(E)\,dE,\qquad\int w_j(E)\,dE=1.$$

이는 일반적인 연결식이다. Shima의 표는 원문의 Eq.2에서 detector efficiency와 광자 빔을 함께 가중하고, Eq.3의 에너지는 단면적까지 포함해 가중한다. Murata의 표는 acceptance를 적용한 검출량에 더하여 fitted angular distribution의 $4\pi$ 보정을 사용하는 total-channel 관측량이다. 따라서 두 논문의 mean energy와 평균 단면적을 동일한 단순 beam-weight convention이라고 부르지 않는다. 정확한 정의와 대응 식 번호는 별도 He4 source packet에 보존한다.

정지 표적과 명시된 광자 number-density spectrum $n_\gamma(E)$를 사용하는 소비자의 event hazard는

$$\Gamma_f=c\int n_\gamma(E)\sigma_f(E)\,dE.$$

두 식은 서로 다른 선형 범함수이다. 평균값만 받아 임의의 소비자 spectrum에 바로 대입하려면 스펙트럼 대응 또는 별도 shape 모형이 필요하다. 이를 설명하는 두-bin 구성 예에서 실험 가중치를 $(1/2,1/2)$, 평균을 $m>0$라고 두면 단면적 $(m,m)$와 $(m+\delta,m-\delta)$는 $|\delta|<m$에서 같은 실험 평균을 준다. 소비자 가중치가 $(1,0)$이면 값이 $\delta$만큼 다르다. 이 예는 관측량 구별을 위한 명시적 toy 구성이며 실제 공급자 행이나 새 과학 no-go 결과가 아니다.

서로 다른 실험이 낸 값은 대안 공급자로 보존하고, 통계 오차와 대칭/비대칭 계통 오차를 섞어 하나의 Gaussian 오차로 만들지 않는다. 원 표가 보고한 no-candidate 관찰 역시 관측·노출·신뢰수준이 별도로 주어지지 않으면 물리적 단면적 0 또는 수치 upper limit으로 승격하지 않는다.

## 5. 전자·상태·에너지의 분리

all-bare 반응 열은 핵종 $(Z,A,m)$와 $q=Z$를 명시한다. 반면 중성 T의 β− 붕괴를 기록하려면 spectator electron을 포함하는 딸 원자/이온 상태가 별도로 필요하다. 예를 들어 한 bound electron을 유지하는 중성 T 후보는 $T^0\to{}^3He^+ + e^-+\bar\nu_e$로 전하를 보존한다. 원도면의 중성 label 배치는 이 명시적 전하 관계를 대체하지 않는다. 실제 shake-up/off, 딸의 전자 들뜸, 광자 cascade, 전자/반중성미자 스펙트럼 및 에너지 분배는 해당 source의 독립 의무이다.

unchanged core compiler는 supplied integer column의 $B^T\nu=0$, $q^T\nu=0$를 검사하고, 그 주위의 R1 adapter가 별도 외부 입자를 포함한 $L_e^T\nu=0$를 검사한다. 이 관계에는 단면적의 정확도, 표의 적용 온도, 가지 확률 또는 핵질량 공분산이 들어 있지 않다. 따라서 source-only projection은 `UNQUALIFIED:ENERGY`, 모든 새 activation과 physical rate/Q admission은 false를 유지한다.

## 검증 연결

native source extraction은 숫자 필드/줄 위치/해시만 확인한다. R2 builder는 새 24개 정수 projection에만 unchanged compiler를 호출하고, R1의 125개와 기존 249-check 결과를 재실행하지 않는다. 독립 검토는 원자료의 관측량, 가지별 연결, 실제 오차 정의와 이 선언된 claim scope를 대조한다. 최종 판정과 실행 비용은 `../SCIENTIFIC_ADMISSION.json`, `../EXECUTION_LEDGER.json`, `../reviews/`에 연결한다.
