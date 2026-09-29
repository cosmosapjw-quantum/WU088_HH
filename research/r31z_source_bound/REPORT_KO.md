# R31Z: source-bound mixed interpolation no-go와 structure-preserving 3-node candidate

기준 parent는 `d573e7b40446b07b1a5544644cf3f977b89264a6`, tree `374a17cff99bed80cc7e356f2e03a1c9d1f1a077`이다. R31Y follow-up에서 Q 생성 원본, basis ordering, frozen phase, independent `j_dotO` 정의·단위, z=0/4 OD/JVP endpoint의 source/member와 array identity가 hash-verified archive에 연결되었다. 따라서 R31X의 mixed secant/derivative 불일치는 더 이상 “공통 frame이라면”이라는 미확정 조건에만 머물지 않고, **해당 archive가 정의하는 frozen representation 안에서는 source-bound incompatibility**로 판정할 수 있다. 이것은 complete HH dynamics의 물리적 적합성 또는 global transport authority의 승인이 아니다.

## 1. Authority가 실제로 닫은 것과 아직 닫지 못한 것

Producer intake가 복원한 source contract는 다음이다.

- `parity_sp.py`의 s=0 static inversion-sector map과 `cusp_ohd.py`의 ionic extension이 저장 Q의 생성 규칙을 정의한다.
- `aocc_sp.py`와 `r10_blocks.py`가 channel ordering, deterministic atomic-eigenvector sign, frozen `phase_E`, Q byte export를 정의한다.
- `mixed_derivative/CONTRACT.json`과 `run.py`는 `j_dotO`가 `D+D†` 대입이 아니라 actual frozen mixed overlap을 z로 미분한 뒤 `dz/dtau=v`와 exact channel phase derivative를 적용한 독립 derivative임을 정의한다.
- `mixed_h/od_run.py`와 `full_model/assemble_v3.py`는 z=0/4 OD와 JVP가 같은 declared ordering/phase bridge를 사용하고 full49 block insertion 뒤 Q projection이 일어남을 정의한다.
- R31W/X snapshot의 z0/z4 OD/JVP arrays는 이 원본 archive/seal arrays와 elementwise exact하다.

따라서 저장된 Q는 이제 단순한 sparse numerical pattern이 아니라 **producer source가 선언한 s=0 inversion-sector subspace map**으로 기술할 수 있다. 다만 이 선언이 complete HH physics에서 독립적으로 적합하다는 최종 review, 시간의존 `dotQ`, 전 구간 sector preservation은 여전히 미확정이다.

## 2. affine mixed O는 source-bound node 자료와 양립할 수 없다

시간 `tau`에서 T=`4/v=8.943508956135245 t_a`라 하자. 동일 frozen representation에서 mixed overlap block을 `O_m(tau)`라 쓰고

    S = (O_m(T)-O_m(0))/T

를 endpoint secant로 둔다. 정확한 affine 함수라면 모든 tau에서 `dotO_m=S`이어야 한다.

저장자료의 spectral 2-norm 비교는

- `||S-dotO(0)||2 = 0.5495713714162325 / t_a`,
- `||S-dotO(T/2)||2 = 0.2910484768338663 / t_a`,
- `||S-dotO(T)||2 = 0.33156843070467085 / t_a`.

또 direct z=2 mixed overlap은 endpoint chord와

    || O_m(T/2) - (O_m(0)+O_m(T))/2 ||2
      = 1.1608909908205545

만큼 다르다. 이제 endpoint/direct arrays가 같은 frozen ordering/phase pipeline에 source-bound되었으므로, **z=0,2,4의 실제 archived represented node data를 동시에 재현하는 affine mixed-overlap 모델은 존재하지 않는다.** 이 결론은 physical exact source function에 대한 continuum error bound는 아니며, archive representation의 모델 적합성 판정이다.

## 3. 모든 C2 source-compatible interpolant에 필요한 curvature 하한

`O(t)`가 twice differentiable이고 위 세 node 값과 endpoint derivatives를 정확히 재현한다고 하자. Banach-space integral remainder identity에서

    S-dotO(0) = (1/T) ∫_0^T (T-u) O¨(u) du,
    dotO(T)-S = (1/T) ∫_0^T u O¨(u) du.

따라서 spectral norm에 대해

    sup ||O¨||2 >= 2 ||S-dotO(0)||2 / T,
    sup ||O¨||2 >= 2 ||dotO(T)-S||2 / T.

Midpoint chord error에는 Peano kernel mass `1/8`이므로

    sup ||O¨||2 >= (8/T^2) ||O(T/2)-(O(0)+O(T))/2||2.

또 endpoint derivative 차이로 `sup||O¨||2 >= ||dotO(T)-dotO(0)||2/T`가 성립한다. 네 하한의 최대는

    sup_{0<=tau<=T} ||O¨_m(tau)||2
      >= 0.1228983778317182 / t_a^2.

속도가 일정하므로 `d/dtau=v d/dz`, 따라서

    sup ||d²O_m/dz²||2 >= 0.6143870602870756 / a0².

이는 **비선형성이 반드시 필요하다는 source-bound represented-data certificate**다. 부동소수점 input/source uncertainty의 interval enclosure는 포함하지 않으므로 `certified_interval_arithmetic=false`다.

## 4. endpoint cubic Hermite도 direct midpoint를 재현하지 못한다

z=0/4의 `O,dotO`만 정확히 맞추는 unique cubic Hermite interpolation을 만들면 direct z=2에서

- `O` error 2-norm = `0.7456046027649951`,
- `dotO` error 2-norm = `0.15168609198173066 / t_a`.

따라서 source-bound endpoint 값과 derivatives를 사용하는 단순 two-endpoint cubic도 stored midpoint를 통과하지 않는다. 이는 기존 affine보다 구조적으로 낫다는 일반론과 “이 HH 데이터에서 충분하다”는 주장을 구분해야 함을 보여준다.

## 5. 최소 3-node structure-preserving mixed-block candidate

새 heavy node를 만들지 않고 이미 존재하는 z=0,2,4 node의 `O_m,dotO_m,D_col,D_row`만 사용한다. `s=tau/T`에서 값과 time derivative를 세 node `s=0,1/2,1`에서 모두 맞추는 degree<=5 Hermite polynomial `O_5(s)`는 유일하다. Wolfram exact 계산에서 여섯 constraints가 모두 0으로 닫혔다.

Node의 anti-Hermitian connection part를

    K_j = (D_col,j - D_row,j†)/2

로 정의하고 세 node를 지나는 quadratic `K_2(s)`를 사용한다. 그러면

    D_col(s) = 1/2 dotO_5(s) + K_2(s),
    D_row(s)† = 1/2 dotO_5(s) - K_2(s)

로 정의할 수 있고

    dotO_5 - D_col - D_row† = 0

이 algebraic identity는 모든 s에서 자동 성립한다. Wolfram exact evaluator도 이 identity를 0으로 확인했다.

저장자료에서 node별 원래 mixed block 자체가 이미 metric compatible하며 residual 2-norm은 z0 `2.83e-17`, z2 `9.45e-17`, z4 `2.74e-17 /t_a` 수준이다. 따라서 이 3-node candidate의 node reproduction은

- max O node error = `0`,
- max dotO node error = `3.96e-17 /t_a`,
- max D_col node error = `8.95e-17 /t_a`,
- max D_row node error = `4.93e-17 /t_a`,
- 65-point metric-compatibility residual max = `1.62e-16 /t_a`.

이것은 **node-exact, structure-preserving represented interpolant 후보**일 뿐이다. z=1 또는 z=3 같은 fitting에 사용하지 않은 direct node와 비교하지 않았으므로 `validated_between_nodes=false`다. 원본 function의 정확한 형태, source error, transition error를 보증하지 않는다.

## 6. 문헌 및 Wolfram 상태

SciSpace 검색은 structure-preserving quantum integration의 맥락을 확인하는 데 사용했다. Ture–Jang의 Magnus propagator(DOI 10.1021/acs.jpca.3c07866)는 unitarity를 보존하는 time propagator, Lubich의 MCTDH integrator(DOI 10.1093/AMRX/ABV006)는 norm/energy-preserving splitting, Xie–Liu–Gu(DOI 10.1126/sciadv.adz3711)는 overlap/connection geometry와 local trivialization을 다룬다. 이 문헌들은 “구조 보존이 중요하다”는 방법론적 맥락이며, 이번 HH quintic candidate의 정확성을 대신 검증하지 않는다.

Wolfram에서는 unique quintic Hermite basis, six node/derivative constraints, quadratic K interpolation, compatibility identity, endpoint/midpoint remainder kernel mass를 exact 계산했다. 첫 evaluator call의 괄호/치환 문법 오류는 실패로 취급하고, 수정 후 실제 성공 결과만 `WOLFRAM_RESULT.json`에 기록했다.

## 7. 판정과 다음 gate

이번 node가 닫은 것:

1. archived z0/z2/z4 mixed overlap의 affine interpolation은 source-bound frozen representation에서 기각된다.
2. source-compatible C2 path에는 nonzero curvature가 필수이며 정량적 하한을 갖는다.
3. two-endpoint cubic Hermite는 direct midpoint를 통과하지 못한다.
4. 기존 세 node만 사용하는 quintic-O + quadratic-K 구조보존 후보는 node-exact하게 구성 가능하다.
5. Q는 source-declared static inversion-sector map임을 producer source까지 추적할 수 있다.

아직 닫히지 않은 것:

- quintic candidate의 between-node predictive accuracy,
- full neutral47 endpoint O/D/dotO와 time-dependent Q/dotQ를 포함한 full-cell bound,
- H interpolation/transition amplitude error,
- source-error/roundoff interval enclosure,
- inversion-sector construction의 독립 physical adequacy review,
- independent decision review와 production/H-skip admission.

다음 최소 경로는 **기존 archive에 fitting에 쓰지 않은 intermediate direct mixed node가 이미 있는지 한 번 확인**하는 것이다. 없다면 새 z=1 또는 z=3 node는 자동 실행하지 않고 `INTERMEDIATE_VALIDATION_DATA_BLOCKED`로 종료하여 별도 science-node 승인을 기다린다. 동시에 recovered producer archive 안의 neutral endpoint/dotQ 자료가 이미 존재하는지 read-only inventory를 한 번 수행할 수 있다. 동일 세 node를 다시 감사하거나 polynomial order만 계속 올리는 메타루프는 중단한다.
