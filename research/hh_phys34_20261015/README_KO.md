# PHYS34 C5: 실제 WU088_HH 구현, 정확한 radial whole-cell 상계

2026-10-15 KST. Parent WU088_HH PR72 `8391eb4e3d5d90b893e92ef0c446eafd6b32d47a`. **이번 산출물은 실제 패키지 소스** `src/wu088_hh/phys33_residual.py`, CLI `scripts/phys33_whole_cell.py`, 회귀 테스트 `tests/test_phys33_residual.py`, 원본 frozen subset, 두 수치분할 결과다. 별도 Codex 소유 `rei_bianchi`는 수정하지 않았다.

## 정확한 대상

동일 frozen-direct 원자모형 `h_lambda=-Delta/2-1/r-lambda S(|r-R zhat|)`, `S(s)=(1+1/s)exp(-2s)`, `lambda=1,R=kappa=.7`, 길이는 `a0`, 에너지는 `Ea=2I0` (source I0=13.605693122990eV, receiver chiH=13.598434599702eV), 기본 signature (-,+,+,+), 원자 공간 Euclidean, `c,hbar,kB`는 1로 두지 않는다. 이미 완료한 실제 full-screened exterior, Q>=21/29 및 이산화 기저는 변경하지 않는다.

### 코드가 실제로 엄밀히 계산하는 것

동결한 `FROZEN_U_SUBSET.npz`는 21부분파 x6 radial panel x11 저장 nodal complex128 `u`, 실제 dyadic radial abscissa `r` 66개를 포함한다. 매 panel에서 저장한 이진 유리수 `(r_i,u_l(r_i))` 전체를 정확히 통과하는 **새 유일한 degree10 Lagrange 다항식**을 유리수로 만든다. 부모의 부동소수점 `chebfit` 평가와 거의 같더라도 polynomial byte identity를 주장하지 않는다.

`psi(r,Omega)=sum_l u_l(r)Y_l0(Omega)/r`에 대해

```
D_l u_l = u_l'' + (kappa^2+2/r-l(l+1)/r^2) u_l,
N_l(r) = r^2 u_l'' + (kappa^2 r^2+2r-l(l+1))u_l,
G_l(r) = r u_l' -u_l.
```

임의 양의 radial subcell `[a,b]`마다 저장된 정확한 polynomial numerator로부터

```
||D psi||_cell² <= a^-4 sum_l integral_a^b |N_l(r)|² dr
||grad psi||_cell² <= a^-2 sum_l integral_a^b (|G_l(r)|² + l(l+1)|u_l(r)|²)dr
||psi||_cell² = sum_l integral_a^b |u_l(r)|² dr.
```

모든 적분은 다항식 계수의 정확한 유리수 적분이며, `r=0`의 singularity를 애매하게 통과시키지 않는다. 분할은 uniform 또는 geometric이고, geometric의 실제 binary64 breakpoints도 최종 JSON에 **정확한 유리수 문자열**로 저장한다. 따라서 사후 NumPy 버전이 달라도 인증한 radial partition을 재현할 수 있다.

이전 PHYS32의 정확한 bounded cusp 변환 `F=exp(lambda exp(-s))`에서 `h_tilde=-Delta/2-1/r+lambda exp(-s) shat.grad+U`이고 `|U|<=2, |lambda exp(-s)|<=1, F^-1<=1` (0<=lambda<=1), 정규화한 원자 `||phi||=1`를 사용한다. 그러므로 원래 **transformed PDE의 패널 내부 L2 잔차 전체 각도**에는 다음 삼각부등식 상계가 적용된다:

```
||bulk_residual|| <= ||D psi|| + 2lambda||grad psi||+4||psi||+(1+kappa²).
```

유한 경계값·경계 source·distributional interface jump·`r<1e-4`·continuous low-Schur inverse·outgoing dual은 **이 upper에 포함되지 않는다**. Stored source와 복소 이산행렬의 full error certificate가 아니라, 정확히 위에서 정의한 new interpolating field의 *broken bulk bound*다.

### 원본·실행

* Source ZIP `WU088_HH_PHYS33H_20261014_RESEARCH_BUNDLE.zip` SHA256 `e792f06520ca64feec9c737541658b9b1f3042c16744a86ecd7544283a486872`.
* Extracted `FROZEN_U_SUBSET.npz`, 21029 bytes SHA256 `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`.
* Run `PYTHONPATH=src python3 scripts/phys33_whole_cell.py --input research/hh_phys34_20261015/inputs/FROZEN_U_SUBSET.npz --partition geometric --subcells 32 --output /tmp/phys34_new_cert.json` (output create-only).
* Local tested Python3, NumPy2.4.2 (repository pyproject specifies NumPy2.3.5; exact dyadic source logic independent, reproducible geom partition is frozen per output).
* `pytest -q tests` tests package; no prior heavy atomic/rate/P01/REI scientific reruns.

### Result interpretation

The improved radii are **rigorous upper bounds for a broken bulk norm** under binary64 file input exact and rational arithmetic. They can be much looser than the independently computed sampled residual `~.00166518546`; this is **not** a numerical-error convergence certificate or certified near-threshold thermal ionisation rate. Shrinking upper bounds under finer partitions improves estimate conservatism, not necessarily physical accuracy. Interface derivative-jump squares use endpoint polynomial exactly and are stated separately.

## Latest REI and next

Read actual live rei_bianchi source/STATE and current CR65/66/BASS_HE57 during this coding session. The original signed AX08 and owner process/allocations belong to Codex; don't duplicate or change them. The optional HH near50kK source is OFF in cold IGM baseline. New threshold cohort representation in bass_cr is a separate candidate; no uncontrolled import or modification of consumer code.

**Next coding node C6/C8**: freeze same-input partition/sample identity at a stricter Python dependency version, improve `r^-p` subcell weighting via exact adaptive integration and source cancellation, certify the full distributional interface/outer boundary and continuous low inf-sup using PHYS33E/F inherited theorems. `continuous_low_inverse/global_amplitude/two_centre_thermal_rate=null`. Native subagents NOT_RUN (no callable). No merges, main update or release activation.
