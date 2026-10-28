# R11 재사용 경계와 비정렬 clock 제약

이 메모는 채택된 R11 계약·API·소스를 읽어 다음 계약에 넘기는 요약이다. 새 proof나 R12 구현·실행·채택을 뜻하지 않는다. 기준 source는 R11 scientific S09 `e1db71bade6ff94959a74d8f297ad2568c247056`이며 50-file payload 동일성은 `R11_LOCAL_AVAILABILITY.json`에서 확인했다.

## 재사용 가능한 채택 결과

고정 열보존 Metzler K, 고정 simplex pi, 고정 비음수 destruction d에 대해 H=pi*d^T-diag(d), A=K+wH를 구성한다. 같은 whole w box에 속하는 모든 가측 w와 모든 시작시각의 블록에 대해 원래 K certificate를 결속한 뒤

    q_add = min(1, q_K + tau*M_w*||H||_1)
    b_H = max_j d_j*(1-pi_j) = ||H||_1/2
    q_minor = 1-exp(-b_H*M_w*tau)*(1-q_K)

를 사용한다. 선택 q는 위 두 상계의 outward rational upper다. 수학적 q_minor<1과 구현된 rational q<1 판정은 구별된다. Native K의 nominal rho를 full A에 그대로 적용하지 않는다.

모든 시작시각의 full-A 인증이 주어지면 age kernel h(u)=q^floor(u/tau), h(0)=1과 whole-domain zero-mass forcing의 인과적 convolution이 채택 근거다. R=||r||_1, E=abs(eta), coarse l1=4E, 고정 c>=0와 signed d_c, whole-fine/coarse forcing 전제를 보존한다. 이 일반 age 설명이 임의의 시계 분할을 현재 코드가 이미 처리한다는 뜻은 아니다.

## 현재 코드가 실제로 수용하는 범위

| 항목 | R11의 실제 API·guard 범위 |
|---|---|
| Clock | origin t0=0, exact uniform delta>0, t_n=n*delta |
| Block alignment | tau/delta가 정확한 정수 1..192 |
| Cells | 정수 1..192 |
| States | 고유 ordered IDs 1..13 |
| Scalars | exact int/Fraction/rational text; float·bool 거부, 입력 numerator/denominator 최대 8192 bits |
| Arithmetic | dyadic128, Taylor96 고정; scalar scaled exponential argument 절댓값<=16 |
| Coupling | c>=0와 signed d_c가 sweep 전체에서 고정 |
| Forcing | g_r,g_e는 비음수 scalar 또는 length=cells 배열, 같은 uniform cell에서 상수 |
| Initial | 비음수 [R0,E0]; singleton zero-mass 공간이면 R0=g_r=0 |
| Low-level q API | `convolution_sweep`는 입력 q의 full-propagator 인증을 전제로 한 산술 함수 |
| Generator wrapper | `sweep`는 실제 K/tau/rho/source binding을 검사해 full-A q를 구성 |
| Lower | 선택 rational-q ideal comparison의 lower만; 물리 오차 lower가 아님 |

`sweep()`는 `tau/delta`의 denominator가 1이 아니면 즉시 거부한다. `convolution_sweep()`도 integer `block_steps`를 받아 출력 tau를 `block_steps*delta`로 정한다. 두 API 모두 arbitrary observation nodes나 별도 source partition을 인자로 받지 않는다. 전체 스칼라한계는 자유로운 임의 precision 옵션으로 해석하지 않는다.

현재 저장 four-case 적용은 192셀, tau/delta=64다. 기존 실제 primary 214/214, independent reference 900/900, 19,195 component comparisons와 전체 두 Python OS CPU 1.477435초를 재사용한다. 이를 확인하기 위한 solver/import/ODE/CAS 실행은 이번 조사에서 하지 않았다.

## 비정렬 clock에서 그대로 전용할 수 없는 부분

R11 endpoint convolution은 같은 grid에서

    F_n = delta * sum_(j<n) h_(n-1-j) g_r,j
    R_n = h_n R0 + F_n

을 사용한다. 이것은 kernel jump와 source/observation cell이 위의 정수 정렬을 만족하는 계약에 속한다. 비균일 구간 길이, 비정수 tau/delta 또는 서로 다른 source/observation partition에 이 인덱스식을 그대로 적용할 채택 근거는 없다. Block_steps를 반올림하거나 float로 넘기는 변환도 현재 계약에 속하지 않는다.

현재 cell 내부 R은 왼쪽값 L_n과 오른쪽 끝점에 왼쪽에서 접근한 V_n 사이의 affine 비교식이다. Whole upper는 그 left limit와 실제 오른쪽 endpoint를 포함한다. E는 이 affine R을 양의 Bernstein moments로 적분하며 signed d_c를 보존한다. 비정렬 셀 내부에서 번역된 kernel jump가 발생하면 현재 한 셀 한 affine 식·한 쌍의 moments를 그대로 사용하는 근거가 부족하다. 새 계약에서 breakpoint·양쪽 극한과 적분 구간을 먼저 명시해야 한다.

`NEXT_INPUT_CONTRACT.json`이 제안한 후속 의무는 정확한 source/observation partition과 실제 번역 jump `t_j+k*tau`에서 셀을 분할하는 것이다. Fresh source는 age0, h0=1로 들어가고, 원래 R forcing memory는 cap 교차 때문에 reset하지 않아야 한다. 이 내용은 R11의 **PROPOSAL_ONLY_NOT_EXECUTED_OR_ADOPTED** 후속이며, 구체적인 유한 breakpoint·정수·산술·실행 계약은 아직 배정되지 않았다.

## Cap과 physical binding

현재 `_cap`은 pinned R10 primary SHA `1713df54bc3653003614f3deba93212735a345e8d7220f053ab9af2d84677fb1` 및 `/hd_cases/[0-3]/capped/endpoints_upper` 또는 `/hd_cases/[0-3]/capped/whole_cells_upper` pointer를 요구한다. 동일한 source family·상태 순서·clock·delta·셀 수를 확인하며, point와 whole은 별개다. 현재 코드가 일반적인 새 cap source나 임의 nonuniform cap partition을 이미 지원한다고 해석할 수 없다.

Point 사이를 보간해 whole-cell certificate로 쓰거나 저장 reference sample을 cap으로 삼지 않는다. 비정렬 새 clock에서 기존 cap을 재사용하려면 정확한 원래 닫힌 셀과 새 대상의 관계 및 source binding을 새 계약에 명시해야 한다. Cap metadata 검사 자체로 whole-domain 물리 전제가 증명되지는 않는다.

실제 reactive array 또는 named physical consumer가 공급되면 immutable array bytes/SHA·state ordering·units·uncertainty/missingness·반응/비반응 구별·initial invariants·density·exact clock/unit conversion·whole fine/coarse forcing을 먼저 결속한다. 그 입력이 기존 fixed K/pi/destruction family를 바꾸는 경우 기존 full-A 인증의 동일성을 자동으로 유지한다고 볼 수 없다.

Native9의 채택 범위는 native K + synthetic conditional reaction fixture다. 현재 actual HD reactive array/physical consumer/density/clock은 INPUT_PENDING이며, native v=UNSPECIFIED·MISSING_NOT_ZERO·TIQM/SQM 구별과 HH_R10=OFF·production=NOT_ISSUED·L4=false·central/physical delta0을 보존한다.

근거 파일: R11 `CONTRACT.json`, `theory/PROOF_KO.md`, `theory/THEOREM_AND_API_KO.md`, `src/full_generator_blocks.py`, `verification/PRIMARY_INPUT.json`, `SCIENTIFIC_ADMISSION.json`, `EXECUTION_LEDGER.json`, `followup/NEXT_INPUT_CONTRACT.json`. 기존 과학 코드와 계약은 수정하지 않았다.
