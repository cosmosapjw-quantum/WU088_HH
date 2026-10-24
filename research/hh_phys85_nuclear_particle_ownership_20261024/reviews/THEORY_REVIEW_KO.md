# PHYS85 이론·계약 독립 검토

## 판정

**최종 PASS_SCOPED / GO_IMPLEMENT.** 아래 세 가지 작은 domain/표기 명확화를 controller가 revision2에 반영했고, 변경된 두 파일을 읽어 확인했다. Prescribed exact reference 구현으로 바로 진행할 수 있다. 새로운 물리 공급자나 부가 검증 계층을 선행 조건으로 추가하지 않는다. 구현·실제 Wolfram raw 결과의 검토는 이 문서의 판정 범위에 포함되지 않는다.

읽은 대상은 actual parent HEAD `d5c2c8dbbbd77bc81526dda6e74df534fba3c4e5`, 현재 branch `research/hh-phys85-nuclear-ownership-20261024`의 새 `CONTRACT.json` revision1과 `theory/FINITE_T_OWNERSHIP_KO.md`다. 검토자는 구현 작성에 참여하지 않았다. 도구로 수행한 계산은 없고, 문서 읽기 및 아래 대수 검토만 수행했다. 원 PHYS81/83 완료 kernel·test, local numerical child, lease 취득, cache 변경, 원격 변경은 모두0이다.

## 직접 검토한 유도

1. **정확한 사건 boost.** `e_star+Ec_star=W`, `gamma²(1−beta²)=1`에서 photon과 daughter의 boost cross terms가 상쇄되어 `Egamma+Kc=gamma W−mc=Kin+Q`다. 따라서 COM kinetic `K`를 normal-frame kinetic debit `Kin=gamma W−M`으로 혼동하지 않는다. Daughter의 longitudinal momentum과 transverse momentum square로 구성하는 별도 mass-shell oracle도 같은 boost 부호와 일치한다. 부모 cold-COM 수치의 재실행은 필요하지 않다.

2. **입자 소유권.** 두 thermal reactant의 소모와 binary daughter owner `h`가 `dNth=h−2`, `dNfast=1−h`를 준다. 합은 nuclear count−1이며, 세 채널의 baryon/charge incidence는 모든 thermal+fast nuclei를 포함할 때 보존된다. `dNe=0`은 이 fully stripped capture에 타당하다. Thermal-only nuclear charge로 electron count를 재계산하지 않는 구분이 필요하며 문서에 이미 있다.

3. **여섯 energy columns.** `h Kc−Kin + (1−h)Kc −Q +Egamma=0`이다. 하나의 photon energy destination만 합에 넣는 계약은 emitted diagnostic의 중복과 Q의 이중 heat 추가를 막는다. Thermal-birth는 주어진 순간 caloric closure이고 actual stopping이라는 주장이 아니다. Scalar 장부가 angular tensor 또는 cosmological consumer를 완성하지 않는 경계도 적절하다.

4. **Joint moments.** 같은 event weights로 column 전체를 평균하면 보존식이 유지된다. `mean(h Kc)`를 `mean(h)mean(Kc)`로 바꾸는 것은 covariance를 버리는 다른 모델이다. 각 사건마다 유일한 owner를 준 뒤 평균하는 구현 방향이 옳다.

5. **비상대론적 Maxwellian 선택.** 공통-T 독립 isotropic Maxwellian에서 `V`와 `g`의 Gaussian 분리가 성립한다. Cross section이 relative kinetic energy에만 의존하면 reaction selection 후에도 COM mean은 `3 theta/2`다. 개별 reactant kinetic mean의 mass fractions와 합 `3 theta/2+I2/I1`이 정확하다. 이 결과는 상대론적 event kernel의 exact finite-T average가 아니며 두 범위를 분리한 계약을 지지한다.

6. **Rate slope와 온도 부호.** 고정 적분영역과 T-independent cross section에서 `d I1/d theta=I2/theta²`이므로 `d log(kappa)/d log(T)=−3/2+I2/(theta I1)`이다. All-fast daughter에서는 thermal energy debit과 thermal count−2를 함께 미분하면 `Tdot=−(2/3)(R T/Nth)d log(kappa)/d log(T)`다. `sigma proportional K^s`, `s>−2`의 formal integral은 mean relative K=`(s+2)theta`; 따라서 constant sigma는 `−R T/(3Nth)`, inverse-speed sigma는0이다. 식의 부호가 맞고 실제 nuclear rate를 새로 제공하지 않는다.

## 동결 전에 반영할 작은 명확화

| ID | 현재 표현 | 필요한 최소 변경 | 이유 |
|---|---|---|---|
| T1 | valid events에서 모든 kinetic outputs가 positive | photon `>0`, incoming/daughter kinetic `>=0`; listed nondegenerate fixtures의 strict positivity는 별도 | 허용 domain에는 `K=r=0`으로 `Kin=0`인 사건과 딸핵을 rest로 만드는 boost가 포함된다. 유효 경계를 false-FAIL시키지 않는다. |
| T2 | finite integrals/normalized event mean/log slope | `T>0`, `Nthermal>0`, `sigma>=0`, `0<I1<∞`, finite I2 및 적분 미분 조건 명시; R=0이면 source0이며 normalized mean/log를 평가하지 않음 | 분모와 log의 정의역을 명시한다. 물리 모형 변경이 아니다. |
| T3 | rest energy와 light speed가 같은 `c` 표기 | final rest energy를 `epsilon_c` 또는 `mc_energy`로 고쳐 mass-shell 우변을 명확히 표시 | 현재 유도 뜻은 옳지만 차원 오독 위험을 없앤다. |

이 명확화는 reviewer가 production files에 직접 반영하지 않았다. Controller가 revision2에 반영했고 reviewer가 변경 부분을 read-only로 확인했다. 세 항목 모두 RESOLVED이며 새 review tree나 별도 numerical run은 요구하지 않는다.

최종 검토 대상 SHA256:

- `CONTRACT.json`: `44f30a1013294689414961a8e456277a41348090a759f0d795a4af77a9ea6dec`
- `theory/FINITE_T_OWNERSHIP_KO.md`: `2e04242ce09ed7d5c0313b5569a0a1cab36f3b544a0d6daa231a006938467e65`

## 실행 전환과 정지 조건

명확화 반영 후 lower-tier agent가 동결 계약대로 exact reference를 작성하고, 제한된 한 번의 Wolfram application 및 원래 계획한 직접 momentum/energy/incidence/guard 검증을 수행할 수 있다. 실제 raw 결과에 구체적 실패가 있으면 그 실패만 한 번 표적 교정한다. 구현 correctness나 application PASS를 이 이론 검토만으로 선언하지 않는다.

PHYS84의 local shared lease gate는 그대로 유지한다. Wolfram의 bounded exact calculation은 별도 tool execution으로 기록하고 local leased numerical application으로 세지 않는다. Remote hardware/thread scheduler가 관측되지 않았다는 기록과 no Parallel code 정책을 유지한다. 실제 physical nuclear finite-T supplier, fast stopping, consumer admission은 OPEN이며 HH_R10=OFF, production admission NOT_ISSUED다.
