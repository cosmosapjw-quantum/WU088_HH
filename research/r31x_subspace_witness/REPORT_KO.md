# R31X: reduced FAIL의 full49 witness lift와 mixed-block defect localization

기준은 R31W NCP replay commit `6cb5d023f80301ba3efad4f1af1d25c327600f15`, tree `0153f0a7bd900ff3d0e922fa7252b201ccbdec60`이다. R31W의 `AUTHORITY_INPUT_BLOCKED`는 full-cell 구간 증명에 관한 판정으로 유지한다. 이번 노드는 그 blocker를 우회해 interval/trajectory를 주장하는 것이 아니라, 이미 보존된 **한 시각 z=2 hybrid 49x49 represented matrices**에서 25D FAIL이 full49 FAIL로 얼마나 강하게 올라가는지를 조사한다. 새 native integral, H 계산, trajectory, M3 benchmark는 0이다.

## 1. 직접 유도: subspace FAIL은 ambient FAIL로 올라간다

O>0, R=R†이고 full-column-rank Q∈C^(n×k)라 하자. Reduced pencil은

    O_Q=Q†OQ > 0,   R_Q=Q†RQ.

Generalized Rayleigh quotient를 ρ(x)=x†Rx/(x†Ox)라 두면 모든 y≠0에 대해

    ρ_Q(y)= y†R_Q y / (y†O_Q y) = ρ(Qy).

즉 reduced problem은 ambient quotient를 range(Q)에 제한한 것이다. O-whitening 후 Hermitian Rayleigh-Ritz 문제로 옮기면 full eigenvalues λ1≤...≤λn과 reduced Ritz values θ1≤...≤θk에는

    λ_i ≤ θ_i ≤ λ_(i+n-k)

가 성립한다. 특히 λ_min(full)≤θ_min, θ_max≤λ_max(full), 따라서 eta_Q≤eta_full이다.

따라서 **reduced FAIL은 full FAIL을 증명한다.** θ≠0인 reduced eigenvector y는 x=Qy로 올리면 같은 Rayleigh quotient를 가진 ambient explicit witness다. 반대로 reduced PASS는 full PASS를 증명하지 못한다. O=I2, R=diag(1,-1), Q=(1,1)^T/sqrt2이면 reduced quotient는0인데 full eta=1이다.

Literature support는 Binding–Najman–Ye의 Hermitian pencil variational principle (DOI 10.1007/BF01228041), Knyazev–Argentati의 Rayleigh-Ritz/subspace framework (DOI 10.1137/08072574X), Argentati et al. (DOI 10.1137/070684628)에서 확인했다. 여기서 쓰는 FAIL-lift 식 자체는 quotient 제한으로 직접 유도했으며 range(Q)의 invariant-subspace 가정을 필요로 하지 않는다.

## 2. full-space metric-compatibility correction에도 하한이 올라간다

기존 R31V 정리에서 같은 O,dotO를 유지하면서 D→D+δD로 metric compatibility를 복원하려면 δD+δD†=R이고 whitened spectral norm에서 최소 수정량은 eta_full/2이다. 따라서

    min_full ||C^-† δD C^-1||_2 = eta_full/2 ≥ eta_Q/2.

이것은 physically correct repair의 승인이 아니라 represented equation에서 metric-compatible connection까지의 거리다.

## 3. 저장된 z=2 hybrid point: 25D extreme FAIL이 full49 extreme와 일치

입력은 R31W와 동일한 71,481-byte snapshot, SHA-256 `565a9ee6d831f5f9e3e69010270f5319aa3328432950efcfda81cfabf325c079`이다. 저장된 49x49 pencil 자체에 경량 generalized Hermitian eigensolve를 적용했다. 새 HH native node가 아니다.

- full49 eta = `0.6007169417167519 / t_a`
- reduced25 eta = `0.6007169417167524 / t_a`
- 차이 = `-4.440892098500626e-16 / t_a`
- full49 λ_min = `-0.4831184527967165 / t_a`
- full49 λ_max = `+0.6007169417167519 / t_a`
- reduced25 λ_min = `-0.4831184527967165 / t_a`
- reduced25 λ_max = `+0.6007169417167524 / t_a`

full extremal generalized eigenvector의 O-orthogonal projection outside range(Q) norm은 negative `5.16e-16`, positive `6.10e-16`이다. 이 stored point에서는 Q가 양쪽 worst generalized direction을 roundoff까지 포함한다.

하지만 **spectral equivalence는 아니다.** full49에서 |λ|>1e-12인 값은 -0.4831184527967165, -0.11540262422575817, +0.17743965987509827, +0.6007169417167519의 네 개이고, reduced25는 양 끝 두 개만 가진다. Approximate rank도 R_full=4, R_Q=2다.

Positive ambient witness의 rate는 `+0.6007169417167528/t_a`, relative generalized-eigen residual `6.73e-16`; negative witness는 `-0.48311845279671684/t_a`, residual `4.75e-16`이다. 따라서 full49 최소 whitened connection correction도 `0.30035847085837597/t_a`이고 reduced lower bound와 roundoff까지 일치한다.

## 4. defect는 neutral direct block이 아니라 mixed neutral–ionic block이 지배한다

Neutral-neutral residual 2-norm은 `1.03e-14/t_a`, mixed47x2 residual norm은 `0.3649304141812513/t_a`, ionic2x2 residual norm은 `0.018498256246365877/t_a`다.

Positive witness에서 neutral-ionic cross는 +0.6244098017137278, ionic-ionic은 -0.0236928599969749, total은 +0.6007169417167528이다. Negative witness에서는 cross -0.4640637914925836, ionic -0.01905466130413372, total -0.4831184527967169이다. 현 point defect의 extremal directions는 mixed neutral–ionic residual이 지배한다. 이는 pointwise algebraic attribution이지 causal-error budget은 아니다.

## 5. archived mixed block의 simple affine derivative compatibility

Mixed O endpoint secant slope S=(O4-O0)/Δt와 저장된 derivatives를 비교했다.

- ||S-dotO(z=2,direct)||2 = `0.2910484768338663/t_a`
- ||S-dotO(z=0,stored)||2 = `0.5495713714162325/t_a`
- ||S-dotO(z=4,stored)||2 = `0.33156843070467085/t_a`
- direct z=2 cross residual norm = `9.45e-17/t_a`
- hybrid cross residual norm = `0.3649304141812512/t_a`

Direct z2 기준 hybrid cross residual은 derivative mismatch + connection interpolation mismatch + direct residual로 닫히며 closure gap은 약 `5.9e-17/t_a`다. 두 주항의 2-norm은 각각 `0.2910484768`, `0.6386482736`이다. Extremal witness에서도 connection interpolation 항이 더 큰 signed contribution을 주고 derivative mismatch가 부분적으로 상쇄한다.

Exact affine O_cross라면 derivative는 구간에서 constant=S이므로, archive endpoint derivatives가 같은 coordinate/phase field라는 조건하에서는 simple affine cross-block model과 endpoint derivative data가 동시에 맞을 수 없다.

중요한 제한: R31W CELL_APPLICABILITY는 endpoint-to-endpoint canonical basis ordering/phase map을 아직 `ambiguous`로 판정했다. 따라서 이는 **archive representation 내부의 conditional incompatibility**이며 physical source-affineness 반증으로 승격하지 않는다.

## 6. 검증 상태

새 focused tests 13 PASS, failure/error/skip 0. 첫 개발 run에서 O-projection residual이 정확히 zero인 synthetic case를 norm helper가 거절해 2 RED failures가 있었고 allow-zero diagnostic norm으로 최소 수정했다. 기존 HH bug가 아니다. Snapshot SHA는 재검사했고 source bytes는 변경하지 않았다. SymPy exact fallback은 Rayleigh lift identity, reduced-PASS counterexample, exact interlacing example를 통과했다.

사용자가 요청한 Wolfram connector는 이번 루프에서 WolframContext, WolframLanguageEvaluator, WolframAlpha 모두 내부 tool error로 실패했다. 새 Wolfram 결과를 만들거나 이전 R31W 결과를 이번 증거로 재라벨링하지 않았다. exact fallback은 `VERIFY_EXACT_SYMPY.py`로 보존한다.

SciSpace에서는 Hermitian pencil variational principle 및 Rayleigh-Ritz/subspace 문헌을 실제 검색했다.

## 7. 결론과 다음 frontier

full-cell `AUTHORITY_INPUT_BLOCKED`는 그대로다. 그러나 현재 point FAIL은 불확정이 아니다. **현재 hash-locked hybrid z=2 represented matrix는 full49에서 metric-incompatible이며, 25D reduced witness만으로도 그 FAIL이 증명되고 실제 full49 stored-matrix eigensolve도 동일 extreme를 확인했다.**

다음 최소 연구는:
1. `direct_Q`가 어떤 physical/symmetry/channel 기준으로 구성됐는지 source authority를 찾아, 왜 extremal modes를 포함하는지 확인.
2. mixed47x2 endpoint의 canonical basis ordering/phase map 및 provider derivative authority를 찾아, affine derivative incompatibility를 physical statement로 승격 가능한지 판정.

authority가 없으면 `Q_AUTHORITY_BLOCKED` 또는 `MIXED_FRAME_AUTHORITY_BLOCKED`로 종료한다. Neutral complete endpoints 부재 때문에 full-cell interval/trajectory/H-skip gate는 여전히 닫혀 있다.
