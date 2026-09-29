# R31AB — z=1 최소 mixed node 승인 여부 결정

기준 parent는 R31AA follow-up remote HEAD `0566c65655128f0fffb3794860af23b2c3d1fe66`, tree `f2638642d85410185beca0a881e0db853adb826a`이다. R31AA NCP follow-up은 focused 5/5 PASS, local replay, z=3 post-hoc 비교, fixed-Q contract review, z=1 preregistration lock을 모두 닫았다. 새 과학 node는 아직 실행하지 않았다.

## 1. R31AA에서 확정된 상태

R31AA local 후보는 z=3에서 R31Z global보다 post-hoc으로 개선되었다.

- E_K: 0.31135192786034865 -> 0.26200533457534436 /t_a
- E_Dmax: 0.3192667733603847 -> 0.26929852552753863 /t_a
- E_O: 0.13213912310643441 -> 0.09901629838600878
- E_dotO: 0.07262393465956431 -> 0.07000108037492338 /t_a

그러나 local 후보는 이 z=3 실패를 본 뒤 설계되었으므로 z=3은 독립 검증이 아니다. 이 개선은 후보 선택의 동기와 post-hoc 진단으로만 사용한다.

Fixed-Q review는 `FIXED_Q_MODEL_DEFINITION_ESTABLISHED`이다. 현재 represented model은 동일 frozen Q를 모든 z에서 사용하므로 `dotQ=0 BY_MODEL_DEFINITION`이다. 이는 missing dynamic-Q bug가 아니라 모델 정의다. 다만 complete-HH에서 이 fixed sector가 물리적으로 invariant하다는 독립 증명은 여전히 없다.

## 2. z=1은 실제로 높은 정보량을 갖는가

사전등록된 z=1은 fit node z=0,2,4 사이의 왼쪽 cell 내부점이다. 새 source를 계산하기 전에, 이미 고정된 두 모델의 z=1 예측만 비교했다.

R31Z global vs R31AA local의 spectral-norm separation:

- ||Delta O_model||2 = 0.12604400117383283
- ||Delta dotO_model||2 = 0.009480380748858165 /t_a
- ||Delta K_model||2 = 0.2165779475378074 /t_a
- ||Delta D_col_model||2 = 0.2139491935471555 /t_a
- ||Delta D_row_model||2 = 0.21927766897126583 /t_a
- Dmax separation = 0.21927766897126583 /t_a

어떤 unknown direct truth X에 대해서도 triangle inequality로

    ||G-L|| <= ||G-X|| + ||L-X||

이므로 적어도 한 모델은

    E_K >= 0.1082889737689037 /t_a,
    E_Dmax >= 0.10963883448563291 /t_a

중 해당 quantity의 half-gap 이상으로 틀려야 한다. prereg tolerance 1e-10과 비교하면 primary model separation은 약 2.2e9 배 크다. 따라서 z=1 node는 두 frozen 후보를 가르는 데 수치적으로 충분히 강한 discrimination을 갖는다. 이는 어느 모델이 이길지 예측하는 것은 아니다.

Wolfram은 이 half-gap 수치와 triangle-inequality logic을 독립 계산했다.

## 3. 문헌 방법론과 validation policy

SciSpace 문헌 탐색은 다음 원칙을 지지하는 방법론적 배경으로 사용했다.

- Hermite interpolation의 fit-node exactness는 별도의 error/convergence control 없이 out-of-sample 정확도를 보증하지 않는다 (Luo & Levesley, DOI 10.1006/JATH.1997.3218).
- adaptive/interpolatory model reduction에서는 error estimator와 새 interpolation/validation point를 분리하여 선택하는 것이 핵심이다 (Chellappa et al., DOI 10.1007/978-3-030-72983-7_5; related arXiv 2003.02569).
- quantum invariant-subspace reduction은 sector invariance를 algebraically certify해야 하며 단순 projected-model agreement와 동일하지 않다 (Kumar & Sarovar, DOI 10.1088/1751-8113/48/1/015301).
- exact symmetry projector와 approximate projector는 구분되어야 한다 (Yen, Lang & Izmaylov, DOI 10.1063/1.5110682).

이 문헌은 WU088 HH 후보의 정확성을 직접 입증하지 않는다.

## 4. 결정

과학적 비용-정보 관점에서 **최소 z=1 mixed OD + independent JVP node를 다음 science action으로 승인하는 것이 타당하다**고 판정한다.

근거:

1. z=3은 이미 post-hoc으로 소비되어 새 독립 검증으로 재사용할 수 없다.
2. parent CP4 inventory에는 동등한 existing z=1 mixed direct node가 없다.
3. z=1에서 두 frozen 모델의 primary predictions가 크게 갈라져 있어 한 번의 node가 높은 판별력을 갖는다.
4. 필요한 계산은 mixed O,D와 independent dotO뿐이며 H, neutral47, ionic2, full49, trajectory는 필요 없다.
5. 모델, metrics, tolerance, decision rule은 실행 전에 이미 hash-locked되어 있다.

단, 현재 사용자 메시지는 "research loop와 handoff" 요청이며 기존 prereg의 `execution_authorized=false`를 명시적으로 뒤집는 문장은 아니다. 따라서 이 checkpoint에서는 **RECOMMEND_AUTHORIZE**만 기록하고 실제 science-node 실행 권한은 false로 유지한다. 사용자 또는 실행 스레드의 명시적 승인 뒤에만 z=1 계산을 시작한다.

## 5. 승인 후 실행 contract

승인되면 B192, z=1 a0, tau=2.2358772390338113 t_a에서 다음 네 output만 생성한다.

- mixed O 47x2
- mixed D_col 47x2
- mixed D_row 2x47
- independent mixed dotO 47x2

금지 output: H, neutral47, ionic2, full49, trajectory.

두 frozen 모델을 source direct node와 비교하여 primary metrics `E_K`, `E_Dmax`를 prereg rule대로 판정한다. z=1 결과를 보기 전 모델 또는 decision rule 변경은 금지한다.

- `PARETO_SUPPORTED_AT_Z1`: local이 두 primary metric에서 global보다 나쁘지 않고 하나 이상 >tol 개선.
- `GLOBAL_SUPPORTED_AT_Z1`: 반대 방향 dominance.
- `TRADEOFF_UNRESOLVED`: 그 외.

secondary metrics E_O, E_dotO, E_Dcol, E_Drow와 metric identity residual도 반드시 기록한다. 임의의 cross-unit scalar score는 만들지 않는다.

결과가 어느 방향이든 한 점으로 interval-wide/trajectory/transition accuracy를 승인하지 않는다. z=1 결과 해석 뒤 자동으로 또 다른 node를 생성하지 않는다.

## 6. full-cell와 Q gate

Q dynamic contract는 현재 represented model에서 blocker가 아니다. Q는 frozen model definition이며 dotQ=0 by definition이다. 남은 full-cell blocker는 주로

- z=4 neutral47 actual array 부재,
- z0-z4 neutral/H source bridge의 완결성,
- fixed inversion sector흘 complete-HH physical invariance 독립 검토,
- BR01/BR02,
- independent review

이다. z=1 mixed validation과 full-cell gate를 혼동하지 않는다.

## 7. stop condition

이 node의 stop condition은 decision + execution-ready contract 고정이다. 새 z=1 science computation은 이 checkpoint에서 수행하지 않는다. 다음 명시적 결정은 `AUTHORIZE_Z1_MINIMAL_MIXED_NODE` 여부다.
