# HH-ENERGY06D: 실제 방향별 birth measure와 C1 선택 급수의 정리

연구 기준일: 2026-10-10 KST. 모든 수치는 `WU088_HH_ENERGY06C_NCP_RETURN_20261009_sha_a9917ff75377.zip`의 원 저장 binary64에서 유도한다. 단위는 photon/H, proper second이다. 이 논증은 새 native 과학 root, 실시간 paired accept 또는 물리적 모델 정확도에 대한 증명이 아니다.

## 1. 동일한 연속 source와 서로 다른 이산 measure

Owner의 고정 prescription은 `SOURCE = 5e-15 photons/(H s)`, birth energy `13.7 eV`, 단계 끝점별 `source_weights`이다. 시작 `t0=1.6e11 s`, 중간 `t1=1.60625e11 s`, 종료 `t2=1.6125e11 s`; 전체 `h=1.25e9 s`, 소단계 `h/2=6.25e8 s`. 저장된 double에서 `W_full=6.25e-6 photons/H = 2 W_half`가 정확히 성립한다. 가중치의 총합은 원 f64 구현에서 수치적으로 1 근방이지만 정확한 유리수로는 반드시 1은 아니다.

원 source 순서는 `transport/remap -> source birth -> photon groups -> implicit BE gas/photon -> native ledger`이다. 방향 index `d=0,...,127`의 원 binary64 가중치를 `w_d(t)`라 한다. **이번 분석에만** exact rational normalization `p_d(t)=w_d(t)/sum_j w_j(t)`를 적용하여 총 birth 질량이 엄밀히 동일한 두 **수학적** 방향 measure를 정의한다. 이것은 원 owner source를 변경하거나 원 runtime가 정확 정규화했다는 주장이 아니다.

`B_full,d=W p_d(t2)`, `B_half,d=(W/2)[p_d(t1)+p_d(t2)]`라 두면

```
Delta B_d = (W/2) [p_d(t1)-p_d(t2)]
sum_d Delta B_d = 0
TV_birth = (1/2) sum_d |Delta B_d|.
```

위 식은 오직 birth input의 공간 가중치 비교다. 서로 다른 birth timestamp, 광자 흡수, 선행 gas/root 변화 및 최종 paired defect를 제거하지 않는다. 원 f64 `(source_n * weight)` 결과를 각각 `Fraction.from_float`로 계산한 질량 차이는 따로 보고한다. 그 차이는 binary64 연산·정규화의 산술적 잔여이며 `TV_birth`와 혼합하면 안 된다.

방출 시각의 첫 중심 moment는 정규화된 이상 birth measure에 대해

```
Delta M1 = sum_d (t1-t2) (W/2) p_d(t1)
         = -(h/2)*(W/2) = -1953.125000000000093597... s photons/H
```

이고, 소스가 동일함에도 두 이산 시간 measure가 같지 않음을 설명한다. 이 단일 moment로 실제 BE defect를 정할 수 없다.

## 2. 각도 관측함수에 대한 정량 상계

전체 질량이 동일하고 `sum Delta B=0`일 때 임의의 실수 방향 kernel `K_d in [K_min,K_max]`에 대해

```
|sum K_d Delta B_d| <= (K_max-K_min)*TV_birth.
```

증명: 양의 질량 `A=sum max(Delta B,0)`와 음의 질량 `-A`가 정확히 같고 `TV_birth=A`이므로 K의 최대/최소로 양·음 항을 각각 감싸면 된다. `K`가 kernel의 진짜 전 구간 상계임이 필요하며, 이 bound를 실제 nonlinear source residual의 일괄 오차로 전환하지 않는다.

임의의 관측 가능한 CMB 사중극이라고 오해하지 않도록 한정된 진단 kernel `K_d=P_2(mu_d)=(3mu_d^2-1)/2`, `mu_d=-1+2*(floor(d/16)+1/2)/8`을 사용했다. 이는 원 source의 8×16 각도 index와 일치하는 dyadic μ-centre를 쓰는 **입력 격자 모멘트**이지 sky `a_2m`, 각도 적분 quadrature, CMB 관측량이 아니다. 각 항은 정확한 Fraction으로 합산했고 위 TV bound가 모든 member에서 성립했다.

실제 입력 결과(전체 birth W에 대한 무차원 정규화): FLRW member0/1의 TV/W≈3.220080452281948e-17, P2/W≈-1.33356867215717e-17; BI member2/3의 TV/W≈2.05745388785974e-08, P2/W≈+1.86075520226485e-13. FLRW 잔여는 source_weights의 binary64 rounding 수준으로만 읽으며 물리적 isotropy 위반이 아니다. BI 결과는 원 고정 H=[1.01e-14,0.99e-14,1e-14]에서 두 endpoint의 방향 가중치가 바뀐다는 이산 입력 진단이다.

## 3. 두 단계 생성을 포함한 coupled 이산근의 올바른 미분

각 단계의 미지 기체 `y_i`와 기존 photon stock `P_{i-1}`에 대해

```
N_i(theta,lambda) = T_i(theta) P_{i-1}(theta,lambda) + B_i(theta)
R_i(y_i;theta,lambda) = y_i - y_{i-1} - h_i F_i(y_i; N_i,theta,lambda) = 0.
```

여기서 `T_i`는 원 angular/spectral transport-remap의 선형 부분, `B_i`는 endpoint source weights와 owner birth energy로 등록된 **그 방법의** birth vector다. 이번 scope에서는 기하 H, birth rate, birth energy, source weights가 λ와 독립이므로 `dB_i/dlambda=0`, `dT_i/dlambda=0`이지만 이것이 `dN_i/dlambda=0`이라는 뜻은 아니다. 이전 BE에서 흡수된 photon stock이 λ에 의존한다.

```
M_i v_i = v_(i-1) + h_i [ F_(i,N) T_i P'_(i-1) + c_H q_HH,i ],
M_i = I - h_i F_(i,y),
v_i = d y_i/dlambda, P'_(i-1)=d P_(i-1)/dlambda.
```

이 식은 이전 photon stock과 gas의 `lambda` 미분을 포함하며, `F_y`에는 원 implicit photon elimination의 체인 미분이 포함된다. 구간 `theta,lambda` 전체에서 **진짜 root family**와 preconditioner identity, Krawczyk `K⊂intY`, `q<1`, guard/threshold branch closure를 얻기 전에는 수치점의 derivative를 인증으로 부르지 않는다. Full은 1단계, two-half는 수락된 half1→half2의 실제 직전 상태로 이어야 한다. Owner 규약에서 full의 HH 장부는 진단이고 accepted trajectory의 HH 사건·열 장부는 half1+half2만 사용한다.

다른 시각에서 태어난 광자를 같은 최종 bin에 합칠 때 원 birth-time의 redshift/absorber exposure를 그대로 보존해야 한다. 위 birth-only TV와 P2를 **수송·흡수 후 photon/temperature의 rigorous bound**로 전환하려면 실제 `T_i`, source Jacobian, root inclusion에 대한 별도 구간 미분과 오차소유권이 필요하다.

## 4. C1 FD2 선택 Kummer 1F1의 독립 조건부 꼬리 보조정리

실제 후보 `finite_m.hpp`는 고정 family `a=r-k/2`, `b=r+3/2`, `k in {1,3,5,7}`, `r in {0,1,2}`와 복소 argument `z`의 전 ball L1 상계 ≤64를 대상으로 0..255 항을 계산하고 T256에 기하급수 상계를 붙인다. 고정 `b>=3/2`이므로 `{}_1F_1(a;b;z)`는 z에 관한 entire 함수다. 다만 **결합된 실제 HH integrand 전체가 analytic이라는 결론은 아직 없다**.

일반항 `T_n=(a)_n/(b)_n * z^n/n!`에 대해 n≥256에서

```
|T_(n+1)/T_n| = |n+a|/(n+b) * |z|/(n+1)
             <= 64/257 = q_new < 6656/26471 = q_FD2.
```

증명: n≥256에서 n+a>0, n+b>n+a, 그리고 n+1≥257, |z|≤64다. 따라서 꼬리 ≤|T256|/(1-q_new)=`(257/193)|T256|`. 기존 후보의 `(26471/19815)|T256|`보다 작고 동일한 정의를 감싼다. **원 FD2 C++ 구현이나 기존 더 보수적인 상수는 변경하지 않았다**. 이 수학적 결과는 selected scalar 1F1의 tail에만 해당하며, 원 z-box inclusion, σ≠0, complex log/power branch, mapped physical/log boxes, 107항 ordered sign/rank, holomorphic quadrature, finite live worker binding을 닫지 않는다.

## 5. 출처/검증 제약

원 `ENERGY06C` ZIP SHA256 `a9917ff7537701168e6130bac1ed536cbb621539332ca7688acf39ac08578394`, CRC pass. 이 분석은 그 ZIP에서 원 bytes를 선택 복사한 paired_runtime.rs, hh_paired_extension.rs 및 native PREBE 12행을 소비한다. input identity와 원 scientific source SHA를 확인한다. 원 binary64 상품 12행의 exact-dyadic sum이 NCP 기존 BIRTH_LEDGER와 전부 일치한다. 별도 Decimal 160 digits는 기존 저장 float를 같은 실수로 해석한 값을 서로 다른 합산 방식으로 검산한다. 이 검사는 독립 peer review, 새 native solver 실행 또는 float의 물리적 오차 상계가 아니다.

C1 `24/289`, `265 missing unbounded`, `epsilon_C/R=null`, `B22=OPEN_UNDETERMINED`, ON06G total256, S0 OFF control, physical/production HOLD를 보존한다.
