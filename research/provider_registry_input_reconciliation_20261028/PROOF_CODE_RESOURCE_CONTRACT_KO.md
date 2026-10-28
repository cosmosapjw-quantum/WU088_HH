# R11 후속 비정렬 분할: 현재 요청과 이미 존재하는 R12 계약의 대조

## 판정과 이번 작업의 범위

현재 사용자가 지정한 후속은 **proposal-only, 새 실행 allowance 0**이다. R11 FINAL `c0b97999b928acb04a805bf3e5283af73aff9831`의 결과와 과거 실패를 유지한다. 읽기 시점에 발견한 R12 head `eb431411f6f0c4c9065edb0a5a11ce2c4bccf2fe`에는 이 후속의 증명·API·구현이 이미 존재한다. 그러므로 같은 비정렬 convolution을 새로 구현하거나 완료된 과학 검사를 재실행할 이유를 이 대조에서 찾지 못했다.

이 문서는 현재 요청에 필요한 유한 proof/code/resource 계약을 원래 수식에서 독립적으로 정리하고, 이미 존재하는 R12의 정확한 위치에 대응시킨다. R12의 기존 C9를 대신하거나 재수행하는 검토가 아니며, 새 과학 채택·DAG node·실행권을 만들지 않는다. R12의 실행 결과 및 역사적 승인 근거는 root의 별도 provenance 확인 대상이다. 현재 읽은 소스만으로 그 기록을 현재 사용자의 새 승인으로 전환하지 않는다.

## 실제로 읽은 근거

이 문서가 대조한 R12 과학 S09는 `eb431411f6f0c4c9065edb0a5a11ce2c4bccf2fe`이다. 이후 같은 branch의 FINAL `7f841fe643d0ab8cb6c90d1068f459fe6321aba9`에서 종료 metadata가 20/20으로 진행한 사실은 [보고서](REPORT_KO.md)에 별도로 기록했다. 이 문서의 수학·코드 대응 source는 S09에 고정되어 있다.

기준 파일은 R11 FINAL의 `followup/NEXT_INPUT_CONTRACT.json`, `REPORT_KO.md`와 R12 S09의 `CONTRACT.json`이다. 실제 읽기 identity와 immutable URL은 `evidence/SOURCE_READ_IDENTITIES.json`에 있다. R12 소스는 모두 아래 immutable commit에서 GitHub connector로 읽었다.

| 소스 | Git blob SHA | 이 대조에서 사용하는 범위 |
|---|---|---|
| `theory/PROOF_KO.md` | `942201b6da196a4ffff4a9f48c133b9ad7228117` | 연속시간 비교식, 전체 knot, signed scalar 적분, 닫힌 셀 cap 귀납 |
| `theory/THEOREM_AND_API_KO.md` | `a753000804baea52d552371c67961bc3f49497bf` | public API, 입력 영역, 실제 source binding, output 의미 |
| `src/nonaligned_convolution.py` | `ca387589387290899ca02e47c34d6376494849e9` | 해당 수식과 입력 제한이 이미 구현된 위치의 정적 확인 |

원격 경로의 공통 prefix는 `research/provider_registry_molecular_r12_20261028/`이다. 각 원문은 `https://github.com/cosmosapjw-quantum/WU088_HH/blob/eb431411f6f0c4c9065edb0a5a11ce2c4bccf2fe/`에 위 prefix와 상대 경로를 연결하여 읽을 수 있다. R12 source에 적힌 실행 성공은 여기서 재실행·재판정하지 않았다.

## 1. Proof 계약: 연속 비교함수와 유한 합

고정 `K/pi/destruction`, `H=pi*d^T-diag(d)`, `A=K+wH`, 전체 허용 `w` box 및 모든 시작시각의 full-A certificate를 전제로 한다. `q`는 같은 zero-mass l1 부분공간의 full block `tau>0`에 대한 상계이고 `0<=q<=1`이다. 더 짧은 remainder는 같은 family에서 l1 nonexpansive여야 한다. R11의 certificate identity와 validity interval을 그대로 결속하며 nominal K의 rho를 full A로 직접 옮기지 않는다.

정확한 clock 구간 `[t0,T]`와 source partition `t0=a0<...<aJ=T`에서 `g_r,j>=0`인 상수 forcing을 둔다. Observation partition은 동일 구간을 덮되 source와 독립이다. 그러면 기존 Duhamel 비교식은

\[
R(t)\le {\cal R}(t)=h(t-t_0)R_0+F(t),\qquad
h(u)=q^{\lfloor u/\tau\rfloor},\quad h(0)=1,
\]
\[
F(t)=\int_{t_0}^t h(t-s)g_r(s)\,ds
=\sum_{j=0}^{J-1}g_{r,j}\sum_{k=0}^{B}q^k\ell_{jk}(t),
\quad B=\left\lfloor{T-t_0\over\tau}\right\rfloor,
\]
\[
\ell_{jk}(t)=\left[\min(a_{j+1},t-k\tau)-\max(a_j,t-(k+1)\tau)\right]_+.
\]

마지막 식은 실제 source interval과 age strip의 교집합 길이다. 적분에서는 개별 끝점의 포함 여부가 영향을 주지 않는다. `q=0`에서는 `q^0=1`을 명시해 fresh forcing을 보존한다. `t0`가 0이 아니어도 kernel age는 항상 `t-s`와 `t-t0`로 계산되므로 위 식은 그대로다. Source 위치를 관찰 index로 바꾸는 근사나 clock 반올림은 이 계약에 없다.

독립 algebraic 표현은 `J(x)=integral_0^max(x,0) h(u)du`를 써서

\[
J(x)=\tau\sum_{k=0}^{n-1}q^k+q^n(x_+-n\tau),\quad
n=\lfloor x_+/\tau\rfloor,\qquad
F(t)=\sum_j g_{r,j}[J(t-a_j)-J(t-a_{j+1})].
\]

`J`는 모든 `n*tau`에서 연속이고, `q=1`이면 `x_+`, `q=0`이면 `min(x_+,tau)`다. 이 두 표현의 등가는 독립 산술 검증의 명료한 기준이지만, 현재 turn에는 실행하지 않는다. R12 proof §§3–4와 production `_overlap_forcing`가 이미 이 의무를 다룬다.

## 2. 정확한 breakpoint와 closed-cell 계약

각 overlap의 slope 변화는 `a_j+k*tau`에만 생긴다. 초기항은 `t0+k*tau`에서 downward jump할 수 있다. 따라서 유한 event set은 observation knots, source knots, 모든 유효한 translated source knots, 초기 block knots와 실제 inherited cap knots의 합집합이다. Exact rational equality로 중복을 제거하고 정렬한다.

연속 event 사이 `[b_l,b_(l+1)]`에서 `F`는 affine이고 초기항의 계수는 일정하다. `Delta=b_(l+1)-b_l`와

\[
L_l=h(b_l-t_0)R_0+F(b_l),\qquad
V_l=h(b_l-t_0)R_0+F(b_{l+1})
\]

를 두면 열린 구간에서는 `(1-u/Delta)L_l+(u/Delta)V_l`이다. `V_l`는 오른쪽 끝점에 **왼쪽에서 접근한 극한**이다. Closed-cell upper에는 `L_l`, `V_l`, 실제 오른쪽 point 비교값을 모두 포함한다. R11 endpoint 연결선을 이 인증으로 대체하지 않는다.

R12 proof §§4–5 및 `_refined_grid`, `nonaligned_sweep`의 `lexact/vexact/rs`가 이 연결을 이미 구현한다. `refined_times`와 source-cell inclusion map이 출력에 보존된다.

## 3. Scalar E 및 memory 계약

`E=abs(eta)`, coarse l1=`4E`, sweep 전체에서 고정 `c>=0`와 signed `d_c`를 유지한다. `g_e`도 같은 source partition에서 whole fine/coarse domain의 상수 상계다. Refined cell마다

\[
W_0=\int_0^\Delta e^{d_c(\Delta-u)}(1-u/\Delta)\,du,\qquad
W_1=\int_0^\Delta e^{d_c(\Delta-u)}u/\Delta\,du
\]

는 부호와 무관하게 양수이고, affine raw comparison의 endpoint는

\[
{\cal E}_{l+1}=e^{d_c\Delta}{\cal E}_l
 +c(W_0L_l+W_1V_l)+(W_0+W_1)g_{e,j(l)}.
\]

Whole-cell R upper `Rbar`로 만든 상수 scalar majorant `Y`는 `Y'(u)=exp(d_c*u)(d_c*Y(0)+c*Rbar+g_e)`이므로 한 cell 안에서 단조다. 따라서 whole-E upper는 `max(Y(0),Y(Delta))`로 얻는다. 이것은 affine raw endpoint와 구별된다.

Local E cap 귀납은 유효한 초기 E upper를 다음 cell로 전달할 수 있다. 그러나 `R`의 `h(t-t0)R0` 및 `F(t)`는 원래 전역 source history에서 계속 계산해야 한다. R12 proof §§6–7, production의 `forcing` 선계산과 capped E 귀납, `R_memory_reset=False`가 이미 이 의무를 반영한다.

## 4. Cap 결속과 observation aggregation 계약

Old cap의 source bytes/SHA/JSON pointer, case, family, state ordering, normalization, 초기값, 계수와 clock이 현재 비교 대상과 같아야 한다. Whole cap은 exact interval inclusion으로 전달한다. Point cap은 정확히 같은 rational point에만 전달하며, 그 사이의 새 point에는 그 point를 포함하는 whole-cell cap만 사용할 수 있다. Saved sample은 cap이 아니다.

모든 old cap knots를 refinement에 포함하면 각 subcell이 한 old closed cell 안에 들어간다. 서로 다른 유효 upper들의 min은 같은 대상·같은 범위에서만 취한다. Observation closed cell은 빈틈없이 덮는 refined closed-cell upper들의 max로 집계한다. Shared endpoint는 양쪽 closed cell의 cap을 모두 사용할 수 있다. Raw ideal은 observation partition 변경에 대해 같은 함수를 나타내지만, capped E 숫자는 local whole-R majorant가 바뀌어 달라질 수 있으므로 refinement invariance를 요구하지 않는다.

R12 proof §§7–8, `_prepare_caps`, `_point_old_cells`, `_aggregate` 및 `caps` 출력이 이미 이 의무를 다룬다. 중요한 실제 구현 범위는 **cap 공급자가 고정된 R11 PRIMARY_RESULTS bytes와 네 case로 제한**된다는 점이다. 새로운 physical consumer의 일반 cap을 받아들이는 인터페이스가 이미 공급되었다고 읽지 않는다.

## 5. 유한 code/resource 계약과 현재 실행 상태

R12 소스에 이미 적힌 유한 영역은 state 1..13, source/observation/old-cap cells 각각 1..192, refined cells<=2048, full blocks<=8, exact input numerator/denominator<=1024bits, `abs(d_c)*(T-t0)<=16`이다. Production은 overlap 평가 전에

\[
M=(\#\text{refined knots})\,(\#\text{source cells})\,(B+1)\le200000
\]

를 실제 guard로 검사한다. 모든 개별 최대치를 동시에 만족하는 입력이 자동으로 허용된다는 뜻은 아니며, 결합 work guard도 만족해야 한다. Float/bool clock, 중복·역순·영길이 cell, 음수 forcing, 잘못된 source/clock/case와 초과 작업량의 거절 경로가 이미 있다. Dyadic128/Taylor96, 독립 Decimal160과 실행 전 고정 `1e-80` guard는 기존 계약 identity로 보존한다.

| 항목 | 이번 turn 계약 |
|---|---|
| 새 primary/reference/CAS allowance | 0 / 0 / 0 |
| 이 대조가 실행한 scientific Python/CAS/ODE | 0 / 0 / 0 |
| 기존 R11/R10/R9/R8/R7/R6/PHYS91 allowance 증가 | 0 |
| 새 구현·재실행 요구 | 없음; 실제 읽은 R12 source 재사용 대상으로 연결 |
| Global remaining/full historical CPU | null 유지 |
| 본문 상태 | proposal-only 계약 대조; 실행·채택 증거를 새로 만들지 않음 |

R12 CONTRACT에 기록된 과거 1/1/1 실행 슬롯은 그 source의 역사적 단위 계약이다. 현재 요청의 0/0/0을 늘리는 값으로 사용하지 않는다. 실제 완료 여부는 immutable ledger/raw results/admission을 root가 읽어 확인한다. 이 문서의 정적 관찰을 `C9 PASS`나 scientific `20/20`으로 세지 않는다.

## 6. 재실행 대신 남겨야 할 구체적 의무

1. **이미 존재하는 결과의 정체성 연결:** root가 R12 immutable manifest/admission/ledger/delivery를 확인하고 이번 R11 재개 요청과의 차이를 기록한다. 비정렬 proof·code를 새 R13으로 복제하지 않는다.
2. **실제 physical 입력 결속:** 새로운 HD reactive array가 들어오면 original bytes/version/DOI/units/uncertainty/missingness와 native state ordering을 먼저 고정한다. Native v가 공급되지 않았으면 UNSPECIFIED로 유지하고 TIQM/SQM을 구별한다.
3. **Named consumer 계약:** consumer/state/density/정확한 clock, 전체 w family, zero-mass residual 및 whole fine/coarse forcing의 실제 공급자를 연결한다. 문헌상 데이터 존재 진술이나 conditional consumer는 이 결속을 대신하지 않는다.
4. **새 source의 cap 경로:** 새 physical 입력에서 cap 전송이 필요하면 실제 그 source의 exact point/closed-cell certificate를 공급하는 별도 adapter 계약이 필요하다. 현재 고정 R11 bytes 검증을 임의 metadata/배열로 완화하지 않는다. 이 작업은 입력이 도착했을 때 범위를 확정하며 현재 추가 실행권은 없다.

이 대조에서 별도의 미해결 비정렬 수학 lemma 또는 구현 결함을 확립하지 않았다. 따라서 일반적인 경고나 재감사를 새 연구 성과로 만들지 않는다. 새 no-go 후보는 없으며 NG1–NG7 채택 대상도 없다. 실제 HD/consumer 입력은 현재 확인 범위의 INPUT_PENDING을 유지하고, 전역 자료 부재는 주장하지 않는다. HH_R10=OFF, production=NOT_ISSUED, L4=false, central/physical delta=0이다.
