# WU088_HH PHYS57: 유리수 certificate로 PHYS56 hybrid 역연산자 상계의 두 OPEN 전제 해소

## 범위 / 선행 결과

- 기준: WU088_HH Draft PR #96, commit `baa7c5924ef9ceb733f98b9014e4e4c7dd00108a`, tree `f14e89420e805ec628e67acbe7a00606efe20f4c`.
- 원래 spectator Hamiltonian `h=-Delta/2-1/r-(1+1/s)exp(-2s)`, `s=|x-(7/10)zhat|`, `kappa=7/10`, 원자 단위, 원래 `eta=Fy`, `xi=Fy-phi` 불변.
- 원본 1386 complex128 `FROZEN_U_SUBSET.npz` SHA256: `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d` (원본의 독립 보존 ZIP을 해제해 실제 바이트 재확인).
- PHYS55는 실제 비중심 screened finite collar [20,27]의 `Lambda_D,TT` 하한 `c_D=9/1000`과 **중앙** Coulomb outgoing exterior `Z_C`의 hybrid bounded inverse 존재를 이미 보였다. PHYS56 R5는 무한 tail sign / 유한 예외 current 하한이 추가로 인증되어야만 다음 양적 Schur 상계가 성립한다고 분리했다.

  `||M_hyb^(-1)||_(X* -> X) <= (1+C_trace/c_D)^2 * max(c_D^(-1), j_*^(-1))`,
  `C_trace=4849/16800`, `X` norm² `sum_(ell>=21,m)(ell+1)|g_lm|²`.

**PHYS57 결과:** PHYS56의 두 미완료 *certificate*를 원래 수치상수에 한해 명시적으로 충족했다. 실제 screened exterior `Z_S`가 아니라 `M_hyb=Lambda_D,TT(screened finite collar)-Z_C(central Coulomb exterior)`의 **새 quantitative norm upper**다. 상계는 매우 커서 실제 scattering 오차 허용값으로 유용하지 않다.

## R5 정리 A: ell>=128 모든 정수, 중앙 Coulomb outgoing 실수부 엄밀히 음수

`B=27`, `rho=kappa*B=189/10`, `a=-eta_C=10/7`. 각 `ell>=128`에서 `H_l^+=G_l+iF_l`, `A_l²=|H_l^+|²`. Brune–Hale–Paris, *Monotonic properties of the shift and penetration factors*, [arXiv:1708.07554](https://arxiv.org/abs/1708.07554), §II.2 Eq.(16)–(21)의 Erdelyi/Nicholson amplitude 적분을 사용한다 (흡인 Coulomb eta<0에 대해 repulsive-only monotonic theorem을 재사용하지 않음).

```
A_l²(rho) = 2rho * integral_0^inf exp(-2rho z) Q_l(z) dz
          = 1 + integral_0^inf exp(-2rho z) Q'_l(z) dz,
Q_l(z)=exp(-2a atan z)*(1+z²)^l * F_l(t),
t=z²/(1+z²),
F_l(t)=sum_{n>=0} d_n t^n, d_0=1,
d_(n+1)/d_n=((n-l)²+a²)/(n+1)² >0.
```

`Q'_l/Q_l = 2(l z-a)/(1+z²) + (F'_l/F_l)*t'(z)`. `F'_l>=0` on z>=0, so `Q'_l>=0` for `z>=a/l`.

정확한 tail 진폭 부호는 `(A_l²)'_rho=-2 integral_0^inf z exp(-2rho z) Q'_l(z) dz`로부터 얻는다. 실수부는 `(kappa/2)*(A_l²)'/A_l²`.

**음의 부분 상계** `0<z<a/l`: 계수 재귀에서 `(j-l)²+a² <=(l+a)² (j+1)²`, 따라서 `d_n<=(l+a)^(2n)/(n!)²`와 `F_l(t) <= I_0(2(l+a)sqrt(t)) <= exp(2(l+a) z)`. 아울러 `(1+z²)^l <=exp(l z²)`와 eta<0 때문에 `Q_l(z) <=exp(2(l+a)z+l z²) <=exp(2a+3a²/l) <e³<27` (l>=128). 따라서

`- integral_0^(a/l) z exp(-2rho z) min(Q'_l(z),0) dz <= 27a³/l²`.

**양의 부분 하계** `1<=z<=2`: `F_l>=1`, `Q_l>=exp(-a*pi)*2^l`, `Q'_l/Q_l>=2(l-a)/5`; `z>=1`, `exp(-2rho z)>=exp(-4rho)`. `pi<22/7`, `4rho+a(22/7)<81`, `e<3`이므로

`integral_1^2 z exp(-2rho z) Q'_l(z) dz > [2(l-a)/5] *2^l/3^81`.

`l=128`에서 이 양의 하계/음의 상계 비율은 정확한 유리수 약 **8086.5594** (하계 ~38.8520, 상계 ~0.00480452). 좌변 하계는 정수 l에서 증가하고 음의 상계는 감소한다. 따라서 모든 정수 l>=128에 대해 `(A_l²)'<0`이고 `Re Z_C,l(27)<0`. **유한 l 표본을 증명으로 바꾸지 않았다.** 본 정리는 고정 `rho=189/10`, `eta_C=-10/7`의 정확한 source convention에 종속한다. 분광함수의 모든 r/eta 영역에 대한 monotonic claim이 아니다.

## R5 정리 B: 예외 채널 21<=ell<=127의 양의 current 엄밀 하한

Coulomb reduced radial ODE `u''+q_l u=0`, `q_l=k²+2/r-l(l+1)/r²`, `k=7/10`. `T=512`, `Lambda=127*128=16256`. 모든 21<=l<=127, r>=T에서

```
q_l(r) >= k²-Lambda/T² = 21913/51200 >1/4,
int_T^inf |q_l'(r)|dr <=2/T+Lambda/T²=135/2048<1/8.
```

`E(r)=|u_r'|²+q_l(r)|u|²`, `E'=q_l'|u|²`, unit Coulomb outgoing at infinity `E(infty)=2k²`. 따라서 Gronwall `E(T)<2k² exp[(1/8)/(1/4)]<4k²`. `Y=(u,u_r'/k)`로 쓰면 `||Y(T)||<4`.

`r in [B,T]`에서 2-norm logarithmic matrix measure

`mu_2 <=[Lambda/r²+2/r]/(2k)`.

`e>8/3`, `(8/3)^3=512/27=T/B`이므로 `log(T/B)<3`. 이에 따라

```
int_B^T mu_2 dr <= D
D=[Lambda*(1/B-1/T)+6]/(2k)=311215/756 ≈ 411.66005.
```

따라서 `|H_l^+(B)|<4 exp(D)`; Wronskian `j_l=k/|H_l^+(B)|²`. `2D<824`, `e<3`으로부터 모든 21<=l<=127에서

`j_l/(l+1) > j_* = (7/10)/(16*128*3^824)`.

이는 **mpmath 고차 출력의 허수부나 interval Coulomb 라이브러리에 의존하지 않는 exact rational 증명**이다. 다만 수치적으로 약 `10^-396.614...`라 극히 약한 안정도 상계이다.

## R5 정리 C: 이전 조건부 hybrid inverse bound를 source-scoped 양적 bound로 승격

PHYS56에서 이미 검토된 `U=W^-1/2 M_hyb W^-1/2`의 block decomposition `P:ell21..127`, `Q:ell>=128`을 활용한다. PHYS55의 collar lower/upper `c_D=9/1000`, `C_trace=4849/16800`은 원래 off-centre screen과 모든 m을 포함한다. PHYS57 A는 Q에서 `Re Z_C<=0`을, PHYS57 B는 P에서 normalized `j_*>0`을 증명했다. 그러므로 PHYS56 Schur estimate

```
||M_hyb^-1||_(X*->X)
 <= (1+C_trace/c_D)^2 * max(1/c_D,1/j_*).
```

를 **현재 k=7/10, B=27의 정확한 물리 상수에 대해 적용 가능**하게 했다. 이 수는 대략 `10^399.653...`이며 실제 과학적 허용오차에 쓸 만큼 sharp하지 않다. 완전한 실수·허수 flux와 Schur 부호를 보존한다. 상계는 무한 고차채널 hybrid에서만 증명된다.

## 적대적 검토 및 기존 연구와 연결

- **흡인 Coulomb**: Brune–Hale–Paris의 일반 monotonicity 결론은 repulsive eta>0에서만 유효하고 eta<0에 대부분 적용되지 않는다고 원 논문이 명시한다. 우리는 해당 논문의 **eta 부호 무관한 Nicholson 적분 등식 및 양의 hypergeometric 계수**를 재해석하여 큰 ell>=128 범위만 직접 따로 증명했다. eta<0 전역 monotonic을 인용한 것이 아니다.
- `q_l'(r)`는 부호가 바뀔 수 있으므로 `int |q_l'|`를 실제로 `2/T+Lambda/T²`로 상계했다. q>0 외부 영역에서만 energy norm을 사용하며 r27에서는 그대로 energy estimate를 연장하지 않는다. **r27..512는 별도 matrix lognorm bound**를 사용한다.
- 각 m에 같은 l 증명이 적용되므로 all m 그대로 성립한다. finite exceptional count 21..127은 유한 (but all m included)이고 lower bound는 l uniform.
- `PHYS56`의 full physical P-Q Feshbach 및 screened exterior LAP는 남아 있다. 본 결과는 `Z_S`, `sigma(E)`, `xi=Fy-phi`, `k_HH(T)`, `HH_R10`에 관한 물리 생산 정리가 아니다. `HH_R10=OFF` 유지.
- 최신 cross repos: REI PR162 (source-locked photon/chemistry audit), BASS_HE PR71 (source birth timing), bass_cr PR75 (common-q threshold source) read-only. 이들은 HH microscopic outgoing potential을 대신하지 않는다.

## R5 실행 및 보존

- 샌드박스 exact Fraction 코드 `src/wu088_hh/phys57_coulomb_cert.py` 및 `tests/test_phys57_coulomb_cert.py`, source guarded original NPZ SHA confirmed from earlier independently restored PHYS55 ZIP.
- 독립 Wolfram tool exact rational positivity and `2D=823.32..., ceil=824`, ratio `8086.55940114522`, implied log10 inverse ~399.653 returned `PASS=True`. Wolfram output warns `Global symbol T/B undefined` in formatting but computed all rational checks PASS; do not call native wolframscript.
- Actual `python -m pytest -q` targeted `15 passed`, producer returns exit0. No NCP execution, full-repo pytest NOT_RUN here. No native subagent API exposed: `native_subagent: NOT_RUN`.

## Positive next action

PHYS57 R5 result allows PHYS56 Schur bound numerical certification but at unusably huge magnitude. Next coding stage C5–C8 independently implement high-precision partial-wave comparisons, finite-dimensional P/Q Schur matrix identity and deterministic negative tests, then R6 adversarial check. Separately PHYS58 must construct actual **fully screened exterior** `Z_S` and a quantitatively effective perturbation estimate including P-Q boundary and volume coupling, plus original regular/driven source. No production admission before this.
