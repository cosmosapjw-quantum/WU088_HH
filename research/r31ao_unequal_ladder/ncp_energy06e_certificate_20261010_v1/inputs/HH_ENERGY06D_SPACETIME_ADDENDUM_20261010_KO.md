# HH-ENERGY06D 봉인 후 추가 수학 결과: 시간·방향 전체 birth measure

2026-10-10 KST. 원 `HH-ENERGY06D` ZIP의 내용은 변경하지 않았다. 본 보조정리는 **추가 산출물**이며 원 native source/미완료 과학 gate를 변경하지 않는다. 동봉된 별도 `HH_ENERGY06D_SPACETIME_ADDENDUM_20261010.py`는 원 ZIP을 안전하게 추출한 폴더의 저장된 `inputs/OWNER_PREBE_FINAL_BINARY.jsonl`을 읽어 exact Fraction으로 재현한다. 첫 작성의 괄호 SyntaxError 및 분석 변수 `p2`를 격자 P2 kernel로 덮어쓰는 이름 충돌을 발견하고 수정했다. 실패 기록은 별도 작업 로그에 남겼다.

## 새 핵심 구분

정규화된 방향 분포를 p1(d),p2(d), W=6.25e-6 photons/H, H=W/2, 서로 다른 t1<t2라고 하자.

```
mu_full = W delta_{t2} p2(d)
mu_half = H delta_{t1} p1(d) + H delta_{t2} p2(d)
Delta_mu = H delta_{t1} p1(d) - H delta_{t2} p2(d).
```

정규화된 원 저장 방향 weights를 분석 전용으로 사용했다. 시간과 방향을 모두 보존한 **전체 양의 birth measure**의 total variation distance는

```
TV(mu_half,mu_full) = (1/2)[H sum_d p1(d) + H sum_d p2(d)]
                     = H = W/2.
TV(mu_half,mu_full)/W = 1/2 exactly.
```

반면 `d` 방향으로 시간 변수를 소거한 **angular marginal** 사이의 거리는

```
TV_angle = H/2 sum_d |p1(d)-p2(d)|,
TV_angle/W = 3.22008e-17 (FLRW), 2.05745e-8 (Bianchi-I).
```

즉 *작은 angular-marginal distance를 전체 birth measure가 비슷하다는 주장으로 사용하면 안 된다*. 두 시각은 서로 다른 원자적 지지점을 가지므로 시간-방향 전체 TV/W=1/2이다. 이것은 두 numerical schemes가 같은 연속 source law의 정당한 근사일 수 없다는 주장이 아니다. Discrete quadrature 차이를 보여줄 뿐이며 numerical convergence는 별도다.

## 선형 kernel의 정확한 timing-angular decomposition

K(t,d)를 이미 source-independent이고 실제로 정의된 선형 response kernel로 한정하면

```
Delta_O = H sum_d [p1(d)K(t1,d) - p2(d)K(t2,d)]
        = H sum_d p1(d)[K(t1,d)-K(t2,d)]
        + H sum_d [p1(d)-p2(d)]K(t2,d)
        = timing + angular.
```

따라서

```
|Delta_O| <= H sup_d |K(t1,d)-K(t2,d)|
            +(max_d K(t2,d)-min_d K(t2,d))*TV_angle.
```

상수 K=1은 Delta_O=0, 중심 시간 K=t-t2는 Delta_O=-(t2-t1)H, 격자 P2(mu)는 Delta_O=original angular P2 moment이다. 저장된 4 member×3 kernels = 12개 exact Fraction identity + bound가 모두 PASS다.

실제 **nonlinear** photon absorption/HH gas feedback는 지정된 source-independent linear K로 자동 표현되지 않는다. Local tangent/adjoint kernel을 진짜 근 영역에서 인증해야 위 경계를 적용할 수 있다. 이전 coupled nonlinear root, paired scientific acceptance, continuous time error, C1 full-box proof는 여전히 OPEN이다.
