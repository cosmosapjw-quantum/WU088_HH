# HH-ENERGY06B: 동일 연속 방출 법칙과 다른 이산 birth measure의 구분

작성일: 2026-10-09 KST. 연구 범위: source-bound 논리·정확한 스칼라 BE 항등식·고정된 NCP 반환 대조. **실제 HH/He/Bianchi paired_trial의 재계산 또는 시간연속 참오차 인증이 아님.**

## 1. 실제 원 source에서 고정되는 의미

- `PINNED_paired_runtime.rs` SHA-256 `8322d79609cc535b046b6000dd27bfdfd8859ddbffb5c3adac90ba396d6d2718`.
- `PINNED_hh_paired_extension.rs` SHA-256 `f47958a8e185ab02cd7d6c00cb7760be583eb769147ca4ed04ef7b1404e87830`.
- `SOURCE=5e-15 photons/(H s)`의 binary64 상수, 매 endpoint의 `source_n=dt*SOURCE`.
- `source_weights(c,h,t1)`이 호출되는 **각 endpoint의 시각**에 광자가 생성되어 angular/directional bin에 분배되고, 새 photons를 사용한 `primary_stage_root`에 들어간다. 따라서 birth timestamp는 **수치식의 source-insertion label**이고, 물리적 delta 방출 직후 흡수가 전혀 없다는 뜻은 아니다.
- Full `endpoint(...,dt)`, first-half `endpoint(...,dt/2)`, second-half `endpoint(...,&half,dt/2)`이며 수락 state는 two-half. HH에서는 full HH 사건수는 진단이고 accepted HH ledger는 half1+half2. Full/half 각각 기존 local/width/ledger 수락 gate가 적용된다.
- 이 source의 적분, 광자 characteristic, energy remap, He/H nonphoto rates, HH stiff source의 정확성을 이번 스칼라 수학으로 인증하지 않는다.

선택 proper-time 구간은 `t0=1.6e11 s`, `t1=1.60625e11 s`, `t2=1.6125e11 s`, `h=1.25e9 s`다. 소스가 저장한 binary64 출생량의 정확 dyadic 유리수는 `W=7378697629483821/1180591620717411303424 photons/H`이고 각 half가 정확 `W/2`다. 관측된 birth measure는

\[ \mu_F=W\delta_{t_2},\qquad \mu_{HH}=\frac W2\delta_{t_1}+\frac W2\delta_{t_2}. \]

따라서 총량은 같고 measure는 다르며 첫 시각 moment 차이는

\[ M_1(\mu_{HH})-M_1(\mu_F)=-\frac{Wh}{4}=-\frac{72057594037927939453125}{36893488147419103232}\ \mathrm{s\;photons/H}. \]

이것은 저장된 binary64 값을 **정확한 유리수로 해석한 결과**다. 과학적 무한정밀의 `5\times10^{-15}`와 binary64 곱을 동일시하지 않는다. 아래 스칼라 모형에서는 `S_eff=W/h`를 사용하되, 이는 **저장 weight를 표현하기 위한 대수적 파라미터**이지 물리 source의 새 설정이 아니다.

## 2. 닫힌 보조 정리: 상수 흡수율·상수 방출률·하나의 광자 stock

스칼라 ODE `dP/dt = S - kappa P` (`kappa>=0`, `S>=0`, `P0>=0`)를 생각한다. 단계 길이 `h>0`, `x=kappa*h`, `W=S*h`라고 둔다. Native endpoint-source의 순서처럼 `source W`를 더한 다음 backward Euler를 적용하면

\[
F_h(P)=\frac{P+W}{1+x},\quad
H_h(P)=\frac{P+W/2}{(1+x/2)^2}+\frac{W/2}{1+x/2}.
\]

정확한 유리수 항등식:

\[
\boxed{H_h(P)-F_h(P)=\frac{x(W-xP)}{4(1+x)(1+x/2)^2}.}
\]

증명: `a=1/(1+x/2)`, `b=1/(1+x)`일 때 `H=a^2P+(W/2)(a+a^2)`와 `F=b(P+W)`이고, `a^2-b=-x^2/[4(1+x)(1+x/2)^2]`, `(a+a^2)/2-b=x/[4(1+x)(1+x/2)^2]`를 대입한다.

`x>0`에서 부호는 오직 `W-xP`로 결정된다. 특히 `P=W/x`는 평형이고 양쪽 이산 연산이 **서로 다른 birth 시각에도 정확히 같은 P**를 반환한다. 반대로 `W=0,P>0,x>0`이면 birth measure가 서로 동일한 0이어도 `H-F<0`다. 따라서 measure의 일치 여부만으로 paired defect의 존재·부호·크기를 판정하는 규칙은 일반적으로 틀리다.

상수 ODE에 대한 실제 연속해는

\[P(t_2)=e^{-x}P_0+\frac{W}{x}(1-e^{-x})\quad(x>0),\]

이고 `x=0`에서는 `P_0+W`다. 이 연속해와의 차이는 **이 스칼라 모형**에 한정된다. 실제 coupled FT03+HH의 time/error bound가 아니다.

### 작은 단계의 leading term

`W=Sh`, `x=kappa h`를 같은 source rate와 opacity로 제한하고 `h→0`이면

\[ H-F=\frac{\kappa h^2}{4}(S-\kappa P_0)+O(h^3). \]

즉 이 paired defect에는 birth-source 이산화뿐 아니라 *homogeneous propagation의 BE 분할 오차*도 함께 들어 있다. NCP의 `-Wh/4` 시간 moment만으로는 이 계수를 얻을 수 없다. 실제 energy-dependent cross section, cutoff jump, Bianchi 방향 가중치에서는 이 스칼라 전개를 가져다가 보편 bound로 사용하면 안 된다.

## 3. 공통 매개변수 미분의 정확한 이산 연결

`P(λ), W(λ), x(λ)`가 미분가능할 때, 한 BE 단계

\[Y=(P+W)/(1+x)\]

를 미분하면

\[(1+x)Y_λ=P_λ+W_λ-x_λY.\]

두 half에서도 반드시 **첫 단계의 `Y_λ`를 두 번째 half의 incoming `P_λ`로 전달**한다. 이 항을 0으로 놓으면 다른 선형계가 된다. 코드에는 순차 implicit tangent와 닫힌 `a^2P+(W/2)(a+a²)`에 대한 별도 수식 미분을 구현했다. 5개 synthetic 매개변수에서 두 방식의 정확 유리수 항등식 및 mpmath 120자리 계산을 대조했다.

이것은 ENERGY05의 실제 네 기체 성분·25 packet 및 ENERGY04 재배치의 tangent proof를 대체하지 않는다. Coupled second-source에서는 원래 전달항 `v_1`, remap photon `N_λ`, direct HH `q_HH c_H`가 동시에 남아야 하며, 실제 birth `W_λ`와 angle weight parameter dependence가 있을 경우 그 항들도 빠뜨리지 않아야 한다.

## 4. 다음 owner 인계의 정확한 규약

**공통인 것:** physical source function/policy `S(t,E,angle;θ)`, 같은 초기 state·geometry·input parameter `θ`·HH multiplier `λ`, process/stochiometric accounting, observer definition.

**공통일 필요가 없는 것:** full/half 각각의 원 시간 quadrature **node** 및 binary64 `source_n` 투입 시각과 이산 photon birth measure. 두 이산 scheme은 동일 continuous model에 대한 각자의 approximations다.

**허용되지 않는 것:** ENERGY05 no-birth Chain을 실제 owner의 birth-included run으로 강제변환, 서로 다른 초기 상태·source law를 paired defect로 비교, full의 event/heat/photons를 accepted half event에 더해 중복 계수, dimension/clock/energy/angle correspondence 미검증, sigma cutoff crossing에 임의 smoothness 적용, Native point-difference를 엄밀한 root difference interval로 승격.

다음 단계의 opt-in `BirthLaw`와 `StepScheme`을 둘로 분리하고, 기존 caller의 원 source insertion/angle weights/primary BE law를 보존한 상태에서 `full`과 `half+half`의 서로 다른 source-time rule을 포함하는 수치 family 비교를 수행한다. 이 닫힌 **정책 규약**은 실제 coupled owner 근·한 단계 보존·refinement 수렴·continuous error·production에는 신규 인가가 아니다.

## 5. 272/0과 NCP 원자 인증의 별도 조건

NCP 최신 return은 24/289 accepted, 265 unbounded, epsilon_C/R null, B22 OPEN이고 소비된 FD1/FD2/6-cell scope를 되살리지 않았다. FD2 finite 107 field callback은 **새 full-box 적분 인증이 아니다.** 272/0 successor는 full-box rank/sign/holomorphic 조건, distinct binary+source hash, 실제 유한 cgroup, 정확한 새 authorization record를 요구한다. 이번 loop에서 HH callback·적분·root·scientific dispatch는 0회이며 이 gate를 닫았다고 주장하지 않는다.

## 6. 검증 한계

코드는 보조 scalar BE와 저장 birth 양의 출처에 대한 read-only exact Fraction 계산만 수행한다. `mpmath` 120자리 계산은 같은 식·상수의 다른 수치 구현이지 독립 물리 검토·형식증명·연속시간 HH 진실값이 아니다. 새로운 원자 fit·source/callback/production 코드를 수정하지 않는다.
