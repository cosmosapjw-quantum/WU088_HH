# PHYS73 — 실제 Coulomb Green 적용과 NCP 통합 최적화

## 결과

원래 HH의 outgoing Coulomb Dirichlet Green kernel을 그대로 적용하는
선형 시간 Rust sweep, 원래 screened source의 양의 analytic multipole,
중첩 radial grid의 Coulomb cache, 남은 NCP 작업을 묶은 실행기를 완성했다.
새 이론과 가벼운 실제 실행은 완료했다. 64코어/128 GiB NCP 전체 실행은
아직 제출하거나 수행하지 않았다. 실제 게시 SHA와 draft PR은
`publication/REMOTE_PUBLICATION.json`, 최종 전달·백업 상태는 외부
`PHYS73_DELIVERY_20261021.json`과 `PHYS73_FINAL_BACKUP_ACK_20261021.json`이
기록한다. 이 보고서의 실행 결과와 미래 host 결과를 섞지 않는다.

기준은 실제 PR124 HEAD `9d6d7491f26850918d6316ed466e3df35dace570`이다.
새 파일만 `research/hh_phys73_20261021/`에 추가했다. PHYS63 질적 존재,
PHYS69 D2, PHYS71 all-angular/all-radial D3 및 PHYS72 weighted inverse와
Born remainder는 완료 상태를 보존했다. 완료된 76개 패널과 152개 inherited
profile payload를 다시 적분한 횟수는 **0**이다. `HH_R10=OFF`이다.

## 1. 새 결과 대조

PHYS71 DELIVERY를 읽고, PHYS72 DELIVERY·최종 ACK·recovery ZIP의 실제 bytes를
대조했다. recovery는 132 members/131 manifest payload가 모두 일치했으며
SHA256은 `4dcce38c8ed820ffa6b7e1da05a426c0823a942d34d3494dc87a08808f104cd3`이다.
복원 capsule과 full Git clone을 구별하고, 실제 Git parent에서 새 branch를 만들었다.

2026-10-20 20:41–20:45 UTC의 fresh intake에서 GitHub branch 132개,
최근 HH PR, PR124, VigilODE PR77/78, Dropbox root와 HH 백업 폴더,
Drive root와 HH 관련 폴더, 최근 저장 자료를 확인했다. 접근한 범위에서
PHYS72 최종 전달 이후의 새 HH host return은 발견되지 않았다.
현재 다른 대화 조회는 unavailable, 직접 NCP host 접근은 미제공 상태였다.
따라서 관찰 범위 밖에도 실행이 없다는 결론은 내리지 않았다.
마지막으로 관찰한 실제 HH NCP 결과는 이미 채택한 PR123이다.

PHYS71의 frozen M 안 PENDING은 외부 DELIVERY로 닫혔고, 이후 PHYS72가
4차 이상 remainder를 닫았다. PHYS72의 과거 Drive upload는 ACK 없는
`UNKNOWN_INTERRUPTED_NO_UPLOAD_RECEIPT` 상태를 보존하고 자동 재시도하지 않았다.
세부 증거는 `intake/`에 있다.

## 2. 원래 source와 적용 범위

원래 원자 Hamiltonian과 변환변수는

\[
V=2(1+d^{-1})e^{-2d},\quad d=|r\mathbf n-(7/10)\hat z|,
\quad \eta=Fy,\quad \xi=Fy-\phi,\quad \phi=e^{-r}/\sqrt\pi
\]

를 유지한다. Coulomb parameter \(\eta_C=-10/7\)는 \(\eta\)와 다른 기호다.
\(B=27,k=7/10,E=49/200\)에서 원래 inhomogeneous 방정식을 변환하면

\[
(A_0-V)u=V\chi,\qquad u=r\xi,\quad \chi=r e^{-r}/\sqrt\pi.
\]

새 실행 대상은 \(u(27)=0\)인 outgoing exterior particular solution이다.
실제 matched solution의 trace \(g=u(27)\)는 별도 입력이다.
frozen NPZ는 \(r\le20\)의 inherited interior state이며 이 trace를 제공하지 않는다.
NPZ SHA256은
`f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`로 보존했다.
origin matching, incoming adjoint, cross section 및 thermal rate는 이번
zero-trace particular 계산으로 완료 처리하지 않는다.

PHYS72의 all-j weighted inverse와 screen multiplier bound를 재사용하면

\[
\|R_0^+\|_{X_+\to X_-}\le c=253/1000,\quad
q=c B^2(3\times10^{-23})=5.53311\times10^{-21}<1,
\]

이고 \(X_+=L^2(r^2dr\,d\Omega),X_-=L^2(r^{-2}dr\,d\Omega)\)이다.
따라서 \(\lambda=1\)의 source Born series가 수렴한다. Bernstein ellipse
\(\rho=8\)과 명시적 지수 적분으로 무한 angular source tail과 radial source
tail을 구했다. \(L=64,T=44,N=1\)에서 실제 exact Fraction 계산은 다음과 같다.

| 항목 | 엄밀한 상한 |
|---|---:|
| 원래 source \(\|V\chi\|_{X_+}\) | 3.398182960240250e-32 |
| zero-trace particular solution \(X_-\) norm | 8.597402889407831e-33 |
| 첫 source Born term 이후 나머지, \(X_-\) | 4.757037590141137e-53 |
| \(r>44\) source omission, \(X_+\) | 6.372559949693160e-54 |
| \(j>64\) source omission, \(X_+\) | 1.546747939001964e-87 |
| source omissions에 inverse를 적용한 오차, \(X_-\) | 1.612257667272370e-54 |
| analytic components 합계, \(X_-\) | **4.918263356868373e-53** |

마지막 수치는 exact continuum first Green action의 source omission·Born
remainder에 대한 상한이다. 실제 radial quadrature, Coulomb 함수 입력,
analytic Bessel 평가 및 native arithmetic의 오차를 합친 finite-grid certificate는
아직 아니다. 유한 행렬 residual을 continuous strong residual로 대체하지 않았다.
모든 \(j\)에서 자라는 boundary weight \(C_j\)를 finite-L Gamma64로 바꾸지 않았다.
충분조건 실패를 strong no-go로 해석한 결과도 없다.

## 3. 두 가지 실제 최적화

### Green 적용: mode별 O(Nr)

\(f_j=H_j^+(r)/H_j^+(B)\), \(a_j(B)=0,a'_j(B)=1\)로 쓰면
\(G_j(r,s)=a_j(\min(r,s))f_j(\max(r,s))\)이다. 유한 quadrature의
\(d_i=a_i f_i,t_i=f_i/f_{i-1},x_i=w_i g_i\)를 사용하여

\[
L_0=d_0x_0,\quad L_i=t_iL_{i-1}+d_i x_i,
\qquad T_{n-1}=0,\quad T_i=t_{i+1}(x_{i+1}+T_{i+1}),
\quad u_i=L_i+d_iT_i
\]

로 같은 complex-symmetric 행렬을 정확산술에서 동일하게 적용한다.
diagonal은 한 번만 포함하고 conjugation이나 추가 \(2,r^2\) 인자를 넣지 않는다.
Rust kernel은 mode 내부 연산 순서를 고정하고 independent task만 thread에
배분한다. dense 비교기는 같은 packet의 \(O(N_r^2)\) 계산이다.

### Angular source: 양의 Yukawa multipole

높은 \(j\)의 binary64 Gauss projection은 큰 양·음 항의 상쇄 때문에 신뢰할 수
없었다. 실제 \(j=64,r=27\)에서 Gauss128은 약 \(1.62434\times10^{-37}\),
180-digit 직접 적분은 약 \(9.26316\times10^{-109}\)를 주었다.
생산 source는 원래 \(V\)의 정확한 Yukawa addition theorem을 미분한 식으로 바꿨다.
\(a=7/10,\kappa=2,\bar k_j=(2/\pi)k_j^{\rm DLMF}\)이면

\[
\int_{-1}^1 V P_j\,d\mu
=4\kappa\left[(i_j-a i_{j+1})\bar k_j+r i_j\bar k_{j-1}\right],
\quad \bar k_{-1}=\bar k_0,
\]

이고 \(i_j-a i_{j+1}\ge(101/150)i_j>0\)이다. 보조 screening \(\kappa\)와
collision \(k\)를 구별했다. retained modes의 angular quadrature는 수행하지 않는다.
다섯 고정밀 기준점 대비 최대 상대 차이는 1.988e-14였다. 선택한 387개 점의
두 SciPy 공식 사이 최대 차이 2.247e-12는 별도의 diagnostic이다.
이 비교를 uniform floating-point certificate로 부르지 않는다.

## 4. 실제 샌드박스 검증과 속도

| 실제 검증 | 결과·범위 |
|---|---|
| Exact source budget | 12 tests PASS; exact CLI 1회 |
| Rust | 6 unit tests; 정상 CLI 5개와 예상 거부 11개 PASS |
| 직접 Coulomb oracle | 70 dps, 4 mode×17 node; 최대 상대 차이 2.244e-16 |
| Analytic angular source | 180 dps 직접 적분 4점, Bessel reference 5점; domain 거부 8개 |
| Nested cache | L1/N3→N5/dps40; cached/uncached packet 동일, 완료 resume 평가 0 |
| 최종 analytic→cache→Rust pipeline | dense/sweep 모두 independent finite action PASS |
| Validated L64 wrapper | exact error assembly·152-panel synthetic chain·resume·atomic writer 검증 |
| 실제 신규 interval panel | j37 한 패널, 1.1893초, process address-space cap 2 GiB |
| NCP 전체 배치 | 미실행, submissions 0 |

모든 원시 결과와 실패 이력은 `verification/`, `native/`에 보존했다.
실행 당시 source와 이후 label/atomic-write 수정의 source를 구별했다.
synthetic chain은 fixture이며 actual scientific panels로 세지 않았다.

실제 같은 packet을 사용한 4개 balanced block, 각 3회 반복의 paired-median:

| 비교 | 커널 시간 비율 |
|---|---:|
| dense 1 worker / sweep 1 worker | **56.8090** |
| dense 1 worker / sweep 8 workers | **184.7993** |
| sweep 1 worker / sweep 8 workers | **2.9110** |

입력은 low-mode 실제 source 4개를 16회 복제한 64 independent tasks,
129 radial nodes다. 실제 sandbox 제한은 CPU 8개/8 GiB이며, 공유 host의
경합이 있는 diagnostic 측정이다. kernel timing은 worker spawn/join을
포함하고 Coulomb preparation·입출력을 제외한다. sweep worker 변경 결과는
bit-identical이고 dense 대비 최대 상대 차이는 7.395e-16이었다.
이는 전체 HH 계산이나 NCP64의 속도비가 아니다. NCP batch가 실제 L64 packet으로
같은 형식의 측정을 새로 수행한다.

## 5. NCP 64코어/128 GiB 실행 구성

단일 entry point는 `implementation/ncp_batch.py`다. 기본은 read-only plan,
`--run`만 현재 host에서 실제 실행한다. runner는 SSH나 외부 게시를 하지 않는다.

| 단계 | 작업 | 64/128에서 자원 |
|---|---|---|
| A | PHYS72 scalar 3개·Fortran 재현, source exact budget, Rust build | 작은 작업 순차 |
| B | L64/T44, N257와 N513, dps60의 실제 Coulomb 준비 | 최대 64 process×1 GiB |
| B | Green sweep·radial refinement·paired benchmark | 최대 64 native worker |
| C | PHYS66 longtail L28/L64×T55/65/75 | 6 process×4 GiB |
| C | validated L64 신규 j37..64 | 28 process×2 GiB, longtail과 동시 |

OS/headroom 16 GiB를 남긴다. C 단계는 34 CPUs/80 GiB 상한이고,
독립성이 없는 panel chain을 잘게 쪼개거나 완료된 일을 채워 넣지 않는다.
BLAS/OpenMP 내부 thread는 1로 고정한다. 실제 affinity·cgroup CPU·memory가
요청보다 작으면 실행 자원은 하향 조정된다.

두 nested source grid는 per-channel hash-bound cache를 공유한다.
노드별 직접 Coulomb 평가 수는 65×(257+513)=50,050개에서 65×513=33,345개로
줄어든다. **33.38%는 평가 개수 절감률이며 측정된 wall-time 절감률이 아니다.**
cache의 dps·코드·mpmath·B/k/eta_C가 달라지면 재사용하지 않는다.

validated L64는 완료된 j0..28, j29..36의 실제 enclosure를 재사용하고
j37..64의 28개 chain만 새로 계산한다. 각 chain은 152 panels로 순차 의존성이 있다.
합산은 정확 유리수 midpoint/radius와 한 번의 full-L64 radial tail을 사용한다.
최종 D1 1e-45, D2 1e-62 목표는 실제 산출 enclosure로 판정한다.
새 28개 numerical budget을 만족한다는 조건에서 D2 합산 예산은
2.80836e-63이나, 이것을 미실행 full-L64 결과로 선언하지 않았다.

PHYS66 longtail은 원래 full-matrix ordered hierarchy 요청이다. PHYS70의
two-row D2 최적화로 같은 출력이 보장된다는 대응이 없으므로 solver·정밀도·게이트를
바꾸지 않고 6 independent cases를 병렬화했다. 최신 batch wrapper에서 실행하되
원래 per-case timeout 900초와 gate를 유지한다. 실패는 기록하고 다른 준비된 작업은
계속한다. 완료 case는 resume에서 다시 실행하지 않는다.

VigilODE의 reflecting-grid 모형은 HH의 outgoing 경계나 상수를 제공하지 않는다.
이번 sweep의 수학적 대응은 HH kernel 자체의 separability에서 유도했다.
PHYS70/VigilODE native L64의 이미 완료된 PR123 결과는 재실행 queue에서 제외했다.

## 6. 전달과 다음 과학 단계

원래 compiler/source/runtime/output hash, 개별 job 성공·실패, 실제 자원,
원시 로그를 immutable attempt에 기록한다. 성공 resume는 child 0회이다.
time limit은 runner가 만든 process group만 종료하며 unrelated process를 건드리지 않는다.
batch 종료 시 결과·source subset·SHA256 manifest의 ZIP을 만들고 전체 payload를
readback 검증한다. ZIP와 ACK는 `archives/`에 생긴다. capsule은 full Git clone이 아니다.

남은 실제 작업은 NCP에서 compiler와 의존성을 맞추고 제공된 명령을 실행하는 것이다.
새 solver 설계나 이론 유도를 NCP에 넘기지 않았다. 자세한 명령은
`ncp_delivery/README_KO.md`와 `CODEX_HANDOFF_PROMPT.md`에 있다.
다음 이론 의존성은 finite-grid reconstruction의 rigorous error/residual,
원래 matched trace와 origin/incoming adjoint다. 이와 기존 D3/Born 완료 상태는
`NEXT_DAG.json`에서 별도 노드로 관리한다.

### 근거

- 본 단위: `theory/FAST_GREEN_APPLICATION.md`, `ORIGINAL_SOURCE_AND_ERROR_BUDGET.md`,
  `ANALYTIC_SCREEN_SOURCE.md`; `verification/`의 실제 실행 receipt.
- Primary identities: https://dlmf.nist.gov/33.2,
  https://dlmf.nist.gov/10.60.E3, https://dlmf.nist.gov/10.51.
- 사용자가 선택한 SciSpace·Exa·Wolfram의 실제 사용·경고·실패도
  `theory/TOOL_EVIDENCE.json`와 추가 symbolic evidence에 기록했다.
