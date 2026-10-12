# WU088_HH PHYS14: 공동 carry의 두 번째 half와 광자 기억

## 결과

같은 COMMON에서 시작한 first_half를 실제 다음 half로 전달했다. 전역 미래 λ,b∈[0,1]는 두 half에 공통이다. 이번 새 계산은 원 source-aligned 실수 함수의 등방 geometric subfamily에 대해 새 implicit stage 한 개, gas/photon/guard의 값·U·V·W, 온도·전자 readout을 포함한다. 정확한 결과는 `results/advance01/ADVANCE_RESULTS.json`, 실행은 `evidence/advance01/`, 독립 채택 범위는 `review/DECISION.json`에 있다.

| 관측량 | HH λ:0→1 | Birth b:0→1 | Finite λ–b interaction |
|---|---|---|---|
| 전자/H | [1.343169300092e-10,2.595287368628e-10] | [8.548580514394e-9,9.901746622979e-9] | [-6.233916429722e-17,-3.439765714258e-17] |
| 열에너지 eV/H | [-3.530954084890e-9,-1.828317230050e-9] | [8.733265021478e-10,1.014234750421e-9] | [3.083461172737e-16,5.145063958952e-16] |
| 온도 K | [-1.893684639279e-5,-9.751531029264e-6] | [-2.278717930823e-4,-1.931735858256e-4] | [1.966322264584e-12,3.448057221983e-12] |

동일 parameter rectangle의 uniform U/V/W에 FTC를 적용한 유한 차이다. 열은 각 고정된 다른 parameter에 대해 성립한다. 통계적 confidence interval이 아니라 고정 source/carry family의 검증된 포함이다.

## 새 물리·수학

원 등방 기하학에서 G_r(t)=exp(-Ht)||q_r||이므로 redshift ratio는 모든 ray에 같은 rho=exp(-Hh)다. source weight는 ||q_r||^-3를 정상화하므로 합이1이다. 실제 common rho와 normalized weights가 원128ray구간에 포함됨을 독립 검토했다. 원 independent coefficient box를 그보다 구체적인 geometric subfamily와 구별한다.

원 hat remap과 ray 공통 absorption denominator를 사용하면 full-ray stage를 aggregate하는 것과 먼저 aggregate한 stage를 계산하는 것이 교환된다. 기체4, 33개 photon group, guard합2의 39개상태가 정확히 닫히며 네 carry 성분은156slots다. 이는 같은 등방 source-aligned 함수에 대한 대수적 축약이다.

두 번째 half 종료시각 t2=1.6125e11s는 기존 Full의 종료시각과 같다. 그러므로 nH/nHe 및 원자 leaves가 같은 기존 Full의 nonphoto/q 값·gas gradient·Hessian을 재사용했다. 새 h=6.25e8s와 실제 전달 photons는 새 denominator D=1+h*a*(1-x)와 gas 잔차에 넣었다. 모든33node중HI photo는16..32만활성이고He photo는모두0이다. 따라서photo gas Jacobian은x한열만비영인rank-one구조다.

원 X에서 strict self-map과 κ≤0.0005392100481791을 얻었다. 네 번의 source-centre Taylor/image 교차 후 κ≤0.0005045844357588이며 새 root image는 대략 x∈[0.9132202086,0.9168624395], y1∈[0.2999648443,0.3000354168], y2∈[0.5999927007,0.6000072419], w∈[13.4343397863,13.5652408859]다. 새 근과도함수는상속한첫단계C²family를실제로이어간다.

## 광자 기억의 온도 방향

첫 half의 HH 이온화는 중성 H opacity를 줄여 잔존 photons를 늘린다. 이를 수송하면 다음 stage의 양의 photon-memory forcing이 된다. 같은 A^-1를 적용해 U2를 전달gas, 현재직접HH, 전달photonmemory로분해했다.

| 온도 첫 미분의 기여 | 검증된 포함 |
|---|---|
| 전달 gas | [-11.418410006,-3.729392608] μK |
| 두 번째 half 직접 HH | [-7.518434740,-6.022137910] μK |
| 전달 photon memory | [-1.649099652,-0.492443409] pK |

Memory의 열에너지 미분은 [1.788044232338e-18,5.689540210192e-18]eV/H로 양수이고 전자미분도양수다. 그러나 T=C_T*w/(1+fhat+e)에두효과를함께넣으면온도미분은음수다. 이 부호는 실제33node의 작은signedtails까지포함한implicit선형계산에서얻었다. 특정높은node의tail을zero-support로읽지않았다. λ와b각각의온도응답이음수이며mixed온도응답이양수이므로, birth가늘어날때HH의추가냉각이약해지는finiteinteraction도포함했다.

## 원 격자의 spectral 분할

Δj=Ej−Ej−1, αj=(1−rho)Ej/Δj라 하면 원branch에서

\[
[R(\rho)^2-R(\rho^2)]e_j=\alpha_j\alpha_{j-1}\left[\frac{\Delta_{j-1}}{\Delta_j}e_j-\left(1+\frac{\Delta_{j-1}}{\Delta_j}\right)e_{j-1}+e_{j-2}\right].
\]

Photonnumber와energymoment는정확히0이다. j=1의lowerguard까지같이계산했고, j=2..32의실제branch도확인했다. j=16에서는계수가대략(+0.1886939771,−0.3773879542,+0.1886939771)이며최대columnL1는[0.7547759083005,0.7547759083006]이다. 최소node간격에비해한halfredshift가작지않아발생하는원격자효과다.

차이연산자를동일COMMON스펙트럼에먼저적용한HI-active photon수차이는[-8.680771077461e-9,-8.680422250484e-9]photons/H다. 이는birth/absorption을제외한transportoperator진단이다. 보존moment가0이라는사실과각활성spectralgroup의재분배는양립한다. 완전한Full대two-half의gasendpoint차이는다음결박된계산으로이어간다.

## 증거와 다음 연구

Fraction에서256bit유효숫자의외향dyadic반올림을사용하고지수는제한하지않았다. 원입력45개및NCP07binarypayload의size/SHA를결박했다. 새과학실행은첫회통과했으며wall0.667s,CPU0.639s,RSS41016KiB였다. 별도analyticimplicitquadraticoracle와directed-roundingoracle를실행했고기존성공과학suite는재실행하지않았다. 후보생성과구분된reviewer가source/geometry 및고정밀별도산술로실제수치를검토했다.

다음루프는같은COMMON·geometrycoefficients의Full과실제two-half endpointdefect를상관된잔차차이식으로포함한다. 이번remap항등식,원Fullsource,새two-halfcarry를재사용하여spectral재분배와중간absorption/source-time/birthchronology의기여를구분한다. 원전역DAG와이전9HHnodes는보존하고이provider후속작업만추가한다. 구체적다음계획과복구명령은`HANDOFF_KO.md`에있다.

전체유도·단위·전제·수치표·원문출처는`report/WU088_HH_PHYS14_20261012.pdf`와동일이름의LaTeX원문에수록했다.
