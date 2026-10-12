# WU088_HH PHYS14: 공동 carry의 두 번째 half와 광자 기억

## 결과

같은 COMMON에서 시작한 `first_half`의 결과를 실제 다음 half로 전달했다. 전역 미래 파라미터 λ, b∈[0,1]는 두 half에 공통으로 적용된다. 이번 새 계산은 원 소스와 일치하는 실수 함수의 등방 기하학적 부분 계열을 대상으로 한다. 새 암시적 단계 한 개에서 기체·광자·guard의 값과 U, V, W를 전달하고, 온도와 전자 관측량의 포함을 구했다. 정확한 결과는 `results/advance01/ADVANCE_RESULTS.json`, 실행 기록은 `evidence/advance01/`, 독립 채택 범위는 `review/DECISION.json`에 있다.

| 관측량 | HH λ:0→1 | Birth b:0→1 | 유한 λ–b interaction |
|---|---|---|---|
| 전자/H | [1.343169300092e-10,2.595287368628e-10] | [8.548580514394e-9,9.901746622979e-9] | [-6.233916429722e-17,-3.439765714258e-17] |
| 열에너지 eV/H | [-3.530954084890e-9,-1.828317230050e-9] | [8.733265021478e-10,1.014234750421e-9] | [3.083461172737e-16,5.145063958952e-16] |
| 온도 K | [-1.893684639279e-5,-9.751531029264e-6] | [-2.278717930823e-4,-1.931735858256e-4] | [1.966322264584e-12,3.448057221983e-12] |

표의 유한 차이는 동일한 파라미터 사각형에서 균일하게 포함한 U, V, W에 미적분학의 기본정리(FTC)를 적용해 얻었다. HH와 birth의 응답은 각각 다른 파라미터를 고정한 경우에 성립하며, interaction은 같은 사각형의 유한 혼합 차이다. 각 구간은 고정된 source/carry family에 대한 검증된 포함을 나타낸다.

## 새 물리·수학

원 등방 기하학에서 G_r(t)=exp(-Ht)||q_r||이므로 모든 ray의 redshift ratio는 같은 rho=exp(-Hh)다. Source weight는 ||q_r||^-3를 정상화하므로 합이 1이다. 실제 공통 rho와 정상화된 weight가 원 128개 ray의 구간에 포함된다는 것을 독립 검토에서 확인했다. 원 독립 계수 box와 그 안의 기하학적 관계를 만족하는 부분 계열을 구별한다.

원 hat remap과 ray에 공통인 absorption denominator를 사용하면, full-ray stage를 계산한 뒤 합산하는 것과 먼저 합산한 상태의 stage를 계산하는 것이 교환된다. 기체 4개, photon group 33개, guard 합 2개로 이루어진 총 39개 상태가 정확히 닫히며, 네 carry 성분을 포함하면 156개 slot이다. 이는 같은 등방 source-aligned 함수에 대한 대수적 축약이다.

두 번째 half의 종료 시각 t2=1.6125e11 s는 기존 Full의 종료 시각과 같다. 따라서 nH/nHe 및 원자 상수의 leaf가 같은 기존 Full의 nonphoto/q 값, gas gradient와 Hessian을 재사용했다. 새 h=6.25e8 s와 실제로 전달된 광자는 새 denominator D=1+h*a*(1-x)와 gas 잔차에 넣었다. 전체 33개 node 중 HI photo는 16..32만 활성화되어 있고, He photo는 모두 0이다. 따라서 photo gas Jacobian은 x 한 열만 비영인 rank-one 구조다.

원 X에서 strict self-map과 κ≤0.0005392100481791을 얻었다. Source centre의 Taylor 포함과 근 사상 포함을 네 번 교차한 뒤에는 κ≤0.0005045844357588을 얻었다. 새 root image는 대략 x∈[0.9132202086,0.9168624395], y1∈[0.2999648443,0.3000354168], y2∈[0.5999927007,0.6000072419], w∈[13.4343397863,13.5652408859]다. 새 근과 도함수는 상속한 첫 단계의 C² family를 실제 다음 단계로 이어간다.

## 광자 기억의 온도 방향

첫 half의 HH 이온화는 중성 H의 opacity를 줄여 잔존 광자를 늘린다. 이를 수송하면 다음 stage에 양의 photon-memory forcing이 전달된다. 같은 A^-1를 적용하여 U2를 이전 기체의 기여, 현재 단계의 직접 HH 기여, 이전 광자 기억의 기여로 분해했다.

| 온도 첫 미분의 기여 | 검증된 포함 |
|---|---|
| 전달된 기체 | [-11.418410006,-3.729392608] μK |
| 두 번째 half의 직접 HH | [-7.518434740,-6.022137910] μK |
| 전달된 광자 기억 | [-1.649099652,-0.492443409] pK |

광자 기억의 열에너지 미분은 [1.788044232338e-18,5.689540210192e-18] eV/H로 양수이며, 전자 수 미분도 양수다. 그러나 T=C_T*w/(1+fhat+e)에 두 효과를 함께 넣으면 온도 미분은 음수다. 이 부호는 실제 33개 node의 작은 signed tail까지 포함한 암시적 선형 계산에서 얻었다. 고에너지 node의 작은 tail도 원 signed interval로 유지했다. λ와 b 각각의 온도 응답이 음수이고 혼합 온도 응답은 양수이므로, birth가 늘어날 때 HH의 추가 냉각이 약해지는 유한 interaction도 포함했다.

## 원 격자의 spectral 분할

Δj=Ej−Ej−1, αj=(1−rho)Ej/Δj라 하면 원 branch에서 다음 식이 성립한다.

\[
[R(\rho)^2-R(\rho^2)]e_j=\alpha_j\alpha_{j-1}\left[\frac{\Delta_{j-1}}{\Delta_j}e_j-\left(1+\frac{\Delta_{j-1}}{\Delta_j}\right)e_{j-1}+e_{j-2}\right].
\]

Photon number와 energy moment는 정확히 0이다. j=1의 lower guard까지 함께 계산했고, j=2..32의 실제 branch도 확인했다. j=16에서는 계수가 대략 (+0.1886939771,−0.3773879542,+0.1886939771)이며, 최대 column L1는 [0.7547759083005,0.7547759083006]이다. 최소 node 간격에 비해 한 half의 redshift가 작지 않아 발생하는 원 격자의 효과다.

동일한 COMMON 스펙트럼에 차이 연산자를 먼저 적용해 얻은 HI-active photon 수 차이는 [-8.680771077461e-9,-8.680422250484e-9] photons/H다. 이는 birth와 absorption을 제외한 transport operator 진단이다. 보존 moment가 0이라는 사실과 각 활성 spectral group의 재분배는 양립한다. 완전한 Full 대 two-half의 gas endpoint 차이는 다음에 동일 계열을 결박한 계산으로 이어간다.

## 증거와 다음 연구

Fraction에서 256 bit 유효숫자의 외향 dyadic 반올림을 사용하고, 지수는 제한하지 않았다. 원 입력 45개와 NCP07 binary payload의 크기·SHA를 결박했다. 새 과학 실행은 첫 시도에 통과했으며, wall time은 0.667 s, CPU 시간은 0.639 s, 최대 RSS는 41016 KiB였다. 별도의 analytic implicit quadratic oracle과 directed-rounding oracle을 실행했고, 기존에 성공한 과학 suite는 재실행하지 않았다. 후보 생성에 참여하지 않은 reviewer가 source와 geometry를 검토하고, 별도의 고정밀 산술로 실제 수치를 확인했다.

다음 루프에서는 같은 COMMON과 geometry coefficient를 사용하는 Full 및 실제 two-half의 endpoint defect를 상관관계를 보존한 잔차 차이식으로 포함한다. 이번 remap 항등식, 원 Full source, 새 two-half carry를 재사용하여 spectral 재분배, 중간 absorption, source 시각과 birth chronology의 기여를 구분한다. 원 전역 DAG와 이전 9개 HH node를 보존하고, 이 provider의 후속 작업만 추가한다. 구체적인 다음 계획과 복구 명령은 `HANDOFF_KO.md`에 있다.

전체 유도, 단위와 전제, 수치표 및 원문 출처는 `report/WU088_HH_PHYS14_20261012.pdf`와 같은 이름의 LaTeX 원문에 수록했다.
