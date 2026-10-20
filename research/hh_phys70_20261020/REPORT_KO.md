# PHYS70 — HH 블록 구조를 이용한 최적화·SIMD·독립 작업 병렬화

## 결과와 채택 범위

원래 HH 유한 angular D2 방정식의 동결 Jacobian을 직접 푸는 코드를 완성했다.
동일한 입력·허용치·바이너리·호스트에서 원래 PHYS69 GMRES 경로와 비교한
L28 전체 적분의 **모델 준비와 solve 구간 중앙값은 98.7113배 및 91.1700배**
개선됐다. 두 그룹의 저장된 D2 값은 기존 PHYS68 인증서와 정확한 유리수로
비교해 각각의 오차 목표를 만족했다. `PROMOTE_SCOPED_OPTIMIZATION`으로
채택하며, 이 수치를 NCP나 다른 모델의 일반적인 가속률로 확대하지 않는다.

완성된 산출물은 `native/phys70_optimized`, `scripts/phys70_ncp.py`,
실제 측정·오차 영수증, 독립 검토, 두 가지 handoff다. 이전 solver와 과학
proof는 그대로 재사용한다. `AGENTS.md`에는 현재 사용자의 최적화 우선순위를
새 머리말로 추가했고 전체 이전 내용을 보존했다. 현재 실행은 샌드박스에서
이뤄졌으며 원격 NCP 제출은 0이다.

이 문서는 source snapshot의 과학·구현 결과를 기록한다. 실제 Git source
commit/최종 metadata HEAD와 외부 백업 ACK는
`publication/SCIENCE_REMOTE.json`, `publication/FINAL_DELIVERY.json`,
`publication/BACKUP_ACK.json`에서 별도로 확정한다. 해당 파일이 아직 없으면
게시 또는 백업 완료를 추정하지 않는다.

## 1. 새 연구 전 실제 복원·원격 대조

작업 공간의 중단 후 복원을 먼저 수행했다. 실제 clone의 부모는 PR119
`efd1520dfc0643220f729307583ff0bc04b059e9`, tree
`8356e2edc9f490cf15c9f884e197366b31ef726c`다. PR115를 새로 push한 것으로
취급하거나 PHYS66의 로컬 snapshot을 실제 descendant라고 바꾸지 않았다.

확인 범위는 WU 128개 branch의 두 페이지, 최근 PR 30개, Actions 전체 3개,
연관 VigilODE·REI·REC·BASS 결과, 접근 가능한 최근 Library 172항목,
Drive의 WU 부모 26항목 및 관련 Dropbox 검색과 알려진 폴더다. 이 범위에서
PR119 이후 새 WU 완료 실행은 발견되지 않았다. 실제 NCP 호스트는 관찰하지
못했으므로 `NCP_HOST_UNKNOWN`을 유지한다. 검색 범위 밖 실행의 부재까지
주장하지 않는다. 원본 관측과 한계는 `intake/`에 보존했다.

PHYS69 통합 source/evidence ZIP의 원본 SHA256
`12983336200c2a7f4cfd3d55e9c4481d06d6ce310adfbddcf336cc2a9b5d6a89`를
복원해 345개 payload의 SHA·크기 및 ZIP 경로/CRC를 확인했다. 과학 적분과
기존 test suite는 이 복원에서 실행하지 않았다. PHYS66 정확한 최종
`993317b1c78edf496ec5a82a261eceb5a54515a78e38d139a924722a5d28f891`
산출물은 여전히 `BLOCKED_ARTIFACT_ACCESS_EXACT_FINAL_VERSION`이다.
이전 84c29… 버전이나 PHYS69 복원본과 합치지 않는다.

VigilODE PR73은 LU 특화와 exact cache, PR74는 autonomous coupled JVP,
PR75는 residual-first coupled correction의 실제 새 Rust 결과를 제공했다.
각각 source·실행·accuracy 범위를 읽었다. 현재 HH baseline에는 LU와 조립
Jacobian이 0회이므로 PR73의 LU 가속을 그대로 적용할 대상은 없다.
PR74/75의 autonomous stage는 시간 의존 HH에 바로 치환할 수 없다.
해당 source에서 재사용한 것은 정확한 cache identity, 작업량 기록,
상태 일치 비교의 방법이며, 실제 적분은 확인된 기존 pin의 tableau와
controller를 이용해 HH 구조에 맞게 구현했다.

## 2. 고정된 물리와 이미 완료된 과학

원래 atomic 좌표에서

\[
h=-\frac12\Delta-\frac1r-
\left(1+\frac1d\right)e^{-2d},\qquad
d=|\mathbf x-0.7\hat z|,
\]

를 유지한다. `B=27`, `k=7/10`, `E=49/200 Hartree`, `H^+=G+iF_C`,
`Z=+u'u^{-1}`이고 radial equation에 들어가는 양의 coupling은
`V=2(1+1/d)exp(-2d)`다. `eta_C=-10/7`과 `eta=Fy`, `xi=Fy-phi`는
서로 다른 정의다. frozen1386 complex128 NPZ SHA는
`f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`다.

PHYS63의 질적 all-angular real-axis LAP/Poisson/DtN은
`ESTABLISHED_REUSED`다. PHYS69에서 확립된 all-angular/all-radial
`D2(21,20),m=0=Z''(0)/2`는

\[
(7.01774363281637372857673+
3.20016322230539545153550i)\,10^{-48}\;a_0^{-1},
\]

표시 중심에 대한 절대 오차 상한 `1.279825889920e-64 a0^-1`로 완료됐다.
인증서 SHA는
`965dc9e3d4a1b40fd7e379629f13480c5a7f30b382aa5b240fd7663b56ae9e29`다.
이 계수와 질적 존재 정리를 다시 계산하거나 OPEN으로 돌리지 않았다.

현재 성능 오차 비교에는 같은 finite-L28 대상의 PHYS68 인증서 SHA
`ddaae206009a276def281af5526851ceb717baf2e0de5f8472552a9db340de9a`
를 사용했다. L28 계산에 all-angular 중심만 대입하는 방식의 비교를 피하고
동일한 수학적 대상을 비교했다. 이 인증서의 구간과 공통 radial tail을
포함해 **실제로 저장된 binary64 D2 점의 참 오차**를 둘러싼다.

## 3. 가속의 수학적 원인

`tau=65-r`, `a=21`, `b=20`, `j=0..L`로 놓고 scaled 상태를
`f_j,g_j,A_j,B_j,z`라 쓰면 방정식의 구조는

\[
\begin{aligned}
f_j'&=-g_j,&g_j'&=Q_j f_j,\\
A_j'&=c_{aj}f_af_j,&B_j'&=c_{bj}f_bf_j,\\
z'&=\sum_j A_jB_j/f_j^2,&
Q_j&=k^2+2/r-j(j+1)/r^2.
\end{aligned}
\]

`A,B`의 scale은 `2^80`, `z`의 scale은 `2^160`이고 coupling과 terminal
입력은 이전 코드와 동일하다. 정확한 변수 정의와 비자율 time partial은
`theory/PROOF.md`에 전개했다.

각 Rodas 단계에서 동결된 전체 Jacobian J에 대해
`(I-sJ)x=b`, `s=h gamma`를 푼다. 먼저 각 angular channel의 oscillator를
풀고, 공유된 외부 channel a,b를 이용해 A,B를 구한 뒤 z를 구한다:

\[
\begin{aligned}
x_{f_j}&=\frac{b_{f_j}-s b_{g_j}}{1+s^2Q_j},&
x_{g_j}&=b_{g_j}+sQ_jx_{f_j},\\
x_{A_j}&=b_{A_j}+s c_{aj}(f_a x_{f_j}+f_jx_{f_a}),\\
x_{B_j}&=b_{B_j}+s c_{bj}(f_b x_{f_j}+f_jx_{f_b}),\\
x_z&=b_z+s\sum_j\left[
\frac{B_jx_{A_j}+A_jx_{B_j}}{f_j^2}
-\frac{2A_jB_jx_{f_j}}{f_j^3}\right].
\end{aligned}
\]

`j=a` 또는 `j=b`에서도 두 미분 항을 함께 유지한다. 복소 켤레와 추가
Taylor factorial을 넣지 않는다. `L<=64`, `r>=27`, `h<=0.5`와 실제
`gamma=0.21193756319429014<0.212`에서

\[
1+s^2Q_j\ge
\frac{17171964889}{18225000000}>0.94222029569.
\]

이는 oscillator 분모의 analytic 하한이다. `f_j`를 포함하는 전체 역행렬의
norm이나 binary64 반올림 오차 전체에 대한 인증으로 확대하지 않는다.
코드는 finite·nonzero guard와 전체 shifted residual 검사를 수행한다.

정확한 shifted solve와 잔차 검사는 O(L)이다. 기존 restarted GMRES도
restart p를 상수 40으로 고정하면 L에 대해 O(L) 저장량이지만, Arnoldi
basis·directions·직교화와 다수의 JVP를 필요로 한다. 이번 이득은 이
p 의존 작업과 큰 buffer를 제거한 데 있다. Angular callback의 O(Q L)
비용은 남는다. Q를 L과 함께 증가시키면 callback의 전체 복잡도는 O(L²)가
되므로 전체 solver를 무조건 O(L)이라고 부르지 않는다.

Wolfram의 3-channel 복소 전체 Jacobian 계산에서 공유된 외부 channel을
포함한 13개 residual이 모두 정확히 0이었다.
`BLOCK_INVERSE_WOLFRAM.wl`와 `WOLFRAM_RESULT.json`에 식과 실제 결과를
분리해 남겼다. 이 유한 symbolic 검증은 임의 L에 대한 위의 직접 대입
증명을 보조한다.

## 4. 외부 코드의 실제 도입

| 재사용 대상 | 실제 적용 | 고정 범위 |
|---|---|---|
| VigilODE `a21d573980f66fe02891bd216153443b5352f921` | Rodas5P raw-U tableau, PI controller, 원래 비교 solver | 기존 method와 비자율 항 유지 |
| `wide=1.7.1` | `f64x4`의 독립 j-lane 곱셈·덧셈 | node 누적 순서, scalar sqrt/exp, 곱셈 괄호 유지 |
| `rayon=1.12.0` | 별도 workspace를 가진 독립 요청의 thread pool | ordered indexed collect, worker1..8 |
| `num-complex=0.4.6` | 복소 상태·블록 대수 | 이전과 동일 |
| `gauss-quad=0.3.2` | 기존 angular node/weight 생성 | 이전과 동일 |

SciSpace와 Exa로 원전 및 공식 문서를 조사했다. Steinebach의 Rodas5P 논문
[Eq.1.2–1.3, §4](https://link.springer.com/article/10.1007/s10543-023-00967-x)
의 비자율 stage 및 work/precision 관점을 실제 코드와 대조했다. 공식
[wide API](https://docs.rs/wide/1.7.1/wide/struct.f64x4.html)와
[Rayon pool API](https://docs.rs/rayon/1.12.0/rayon/struct.ThreadPoolBuilder.html)
에서 적용한 연산·thread 계약을 확인했다. 다른 논문의 solver 순위나 다른
저장소의 timing을 현재 HH의 측정치로 사용하지 않았다.

SIMD는 angular quadrature의 서로 다른 j 항을 lane에 배치한다. 각 node에
대한 누적 순서를 그대로 유지하고 `reduce_add`, fused `mul_add`, vector
approximate exp는 이 동등성 경로에서 사용하지 않는다. 선택된 두 행의
basis product를 미리 계산하고 패딩한 4-lane 배열 및 재사용 buffer를 쓴다.
이 선택은 table 메모리를 늘리는 대신 callback의 곱셈·메모리 접근을 줄인다.

각 accepted base에서 정확히 같은 시간·상태 bits와 kernel 설정일 때만
동결 Jacobian을 재사용한다. h만 달라지는 retry에서는 base가 같으므로
재사용할 수 있다. Radial carry는 순차 계산하고, 서로 독립된 요청들을
Rayon으로 병렬 실행한다. 내부 부동소수점 reduction 순서를 thread 수에
맡기지 않는다.

## 5. 실제 전체 적분의 work–precision

다음은 **새 허용치 두 개 × 3 engines × 3 alternating samples = 18회**의
실제 적분이다. 기존 PHYS69의 완료된 rtol `1e-10`, `1e-12` 요청을 그대로
다시 실행하지 않았다. 모든 engine은 하나의 release 바이너리에 들어 있다.

| rtol / atol | accepted/rejected | 기존 GMRES | Block scalar | Block SIMD | GMRES/SIMD |
|---|---:|---:|---:|---:|---:|
| `3e-10 / 3e-12` | 703 / 0 | 3.041681740 s | 0.044981303 s | 0.030813919 s | 98.7113배 |
| `3e-12 / 3e-14` | 1819 / 0 | 8.136270035 s | 0.118403532 s | 0.089242810 s | 91.1700배 |

시간은 모델·workspace 준비, 적분 및 일부 counter 직렬화가 포함된 solve
구간의 중앙값이다. 프로세스 기동·입력 읽기·최종 JSON 출력을 포함한
Python process-wall 중앙값 비율은 각각 **48.0449배, 71.6688배**다.
poll/wait 오버헤드도 해당 wall 측정에 포함되므로 두 시간 정의를 섞지 않는다.

| 목표 | 기존 GMRES 참 상대 오차 상한 | Block scalar/SIMD 참 상대 오차 상한 |
|---|---:|---:|
| `3e-10` | `1.4727851774252374e-10` | `1.4728567155626935e-10` |
| `3e-12` | `1.2717040124565395e-12` | `1.2701532252981296e-12` |

독립 검토에서 18개 원본 파일의 54개 영수증 해시, 90개 정확한 유리수
오차 기록, 36개 binary64 성분의 Fraction을 재계산해 일치시켰다.
Scalar/SIMD의 6개 대응 상태 배열 2,808성분은 비트까지 같았다.
기존 GMRES와 block은 rounding 및 linear stopping이 달라 비트 동일로
주장하지 않지만 각각의 참 D2 오차 목표를 만족한다.

같은 단계 수에서 block scalar의 개선은 **67.6210배·68.7164배**이고,
SIMD 추가 개선은 **1.45977배·1.32676배**다. 느슨한 그룹의 JVP 호출은
기존 236,208회에서 전체 shifted residual 검사용 5,624회로 바뀌었다.
기존 직교화 inner product 9,223,360회와 Krylov 반복을 제거했다.
더 엄격한 그룹은 기존 JVP 611,143회와 직교화 23,863,640회에 대해
14,552회의 구조적 solve 및 full residual check를 수행했다.

실제 timing 변동은 보존했다. 느슨한 SIMD 세 sample은
`0.029824452, 0.030813919, 0.062358916 s`, 엄격한 scalar는
`0.201225098, 0.118176558, 0.118403532 s`다. 이상치를 삭제하지 않았고
세 표본으로 통계적 confidence interval이나 NCP 성능 하한을 제시하지 않는다.

## 6. microbenchmark, 메모리와 병렬성

저장된 PHYS69 종점 상태를 읽어 고정 callback과 한 단계 probe를 구성했다.
이는 새로운 실제 radial trajectory가 아니다. 7개 sample에서 SIMD RHS는
기존 RHS보다 중앙값 **1.91911배**, 준비된 JVP는 기존보다 **2.58524배**
빨랐다. RHS scalar/SIMD 결과는 producer assertion과 원래 callback을
사용한 별도 contract test에서 비트 동일을 확인했다.

12단계 probe를 5회 비교한 중앙값 비율은 **85.7371배**다. 공통 한 단계
종점의 relative infinity 차이는 `1.72428e-16`이다. 다만 마지막 embedded
stage의 raw relative 차이는 `1.0`으로 보존한다. 기존 GMRES의 absolute
linear stopping이 매우 작은 우변에 대해 0 해를 반환했고, 새 방법은
작지만 nonzero인 correction을 계산했다. 원래 state 오차 weight로 나눈
최대 stage 차이 `0.0001133706`은 사전 gate `0.005`보다 작다. 모든 stage의
비트 동일이나 작은 embedded error만을 근거로 한 전역 오차 인증은 아니다.

| 메모리 계측 범위 | retained vector capacity |
|---|---:|
| 기존 driver: cache/scratch/GMRES/least squares | 256,280 bytes |
| 새 driver와 frozen Jacobian | 30,632 bytes |
| 새 kernel table/rows, 별도 | 52,736 bytes |
| 새 driver+kernel의 계측 합계 | 83,368 bytes |

동일한 driver 범위의 감소는 **88.0474%**다. 기존 model/table은 driver
계측에 포함되지 않았고 RSS나 모든 allocation 횟수는 측정하지 않았다.
새 binary는 기존 비교 경로까지 포함해 5,543,600 bytes이며 전체 binary
크기 감소를 주장하지 않는다.

독립된 네 전체 적분을 1/2/4 worker에서 각각 한 batch씩 실제 실행했다.

| workers | batch 시간 | 1 worker 대비 | 상태·순서 |
|---:|---:|---:|---|
| 1 | 0.201385102 s | 1.00000배 | 기준 |
| 2 | 0.138033682 s | 1.45896배 | 비트 동일 |
| 4 | 0.099805345 s | 2.01778배 | 비트 동일 |

4개의 서로 다른 허용치가 만들어내는 작업량이 달라 가장 긴 작업의 시간이
남는 자연스러운 제한도 있다. 이 측정은 설정별 단일 batch다. 별도 8개
frozen RHS 작업을 5회 측정한 micro 중앙값은 4 worker에서 2.54072배였다.
독립 검토가 full trajectory의 대응 8쌍 3,744성분의 bit parity와 각 D2
오차 목표를 원본 결과에서 재확인했다.

## 7. 검증·수정·실제 실행의 구분

Rust의 13개 신규 release 시험은 모두 통과했다. 원래 RHS/JVP/time partial,
8개 raw-U stages, shared external derivative, 분모/finite guard,
정확한 cache key, represented clock의 strict cap와 종점 도달을 확인한다.
실행기 시험은 최초 19개가 통과했고 후속 guard 결함을 재현하는 3개 신규
시험을 추가했다. 해당 3개와 영향받은 기존 2개를 합한 최종 표적 5개도
통과했다. distinct 신규 시험은 35개이며, 최종 한 번의 35-test suite를
실행했다고 쓰지 않는다. Python fixture는 비물리 mock으로 구분했다.

독립 검토에서 구체적으로 발견한 두 Rust 결함을 닫았다. 실패한 freeze가
기존 Jacobian을 valid로 남기는 경우에는 진입 시 invalidate하도록 했고,
residual normalizer의 overflow가 양의 잔차를 0으로 보이게 하는 경우에는
분자·분모 finite 검사를 나누기 전에 수행했다. Wrapper도 nested request와
B/T/k/eta_C/m/target/clock/scales를 실제 결과에서 강제하도록 보완했다.
수정 전 실패와 최종 표적 PASS를 모두 보존했다.

완성된 NCP용 wrapper로 샌드박스 L28 pilot 1회를 실행했다. 1,132개 accepted
step, `tau=0..38` 완료, 참 D2 상대 오차 상한 `1.3856994587496746e-11`
로 목표 `3e-11`을 만족했다. RESULT SHA는
`0ef41785793d32d47fdb63a7d12828d9d5c2f6e06e3746c65ade85d8ac23be27`다.
완료 resume 후 10개 파일의 SHA·크기·mtime은 이전과 같고 새 적분 0,
파일 쓰기 0이었다. 원격 NCP 작업으로 세지 않는다.

이번 실제 완료 적분은 **18 + 12 + 1 = 31회**의 새 성능 실험이다.
기존 PHYS64 NCP20, PHYS66 pilot/smoke, PHYS67 인증, PHYS68 L28,
PHYS69 새 band 및 예전 native 두 실행의 재수행은 0이다.
독립 리뷰어도 적분·callback·stage를 재실행하지 않았다.

## 8. NCP 실행 준비와 남은 DAG

L64 request는 `L64, nodes128, T65, rtol1e-10, atol1e-12, max_step0.25`,
`block_simd`로 완성됐다. 실제 사전 점검은 `PREFLIGHT_ONLY`이며 child
process·Coulomb seed 생성·적분이 모두 0이다. 먼저 같은 요청·source·seed·
engine·binary의 완료 영수증 또는 실행 중인 작업을 확인해야 한다.
일치하는 완료본은 읽기 검증하고 진행 중이면 관찰한다.

실행기는 create-only output, 정확한 request 원문 hash, source/seed/binary와
두 crate·Python guards의 fingerprint, bounded POSIX process group, timeout,
주소 공간 제한, 전체 stdout/stderr/exit receipt를 제공한다. 부분 실패를
완료로 바꾸거나 같은 디렉터리에 자동 재실행하지 않는다. NCP가 해야 할
작업은 필요한 의존성 준비·컴파일·작은 환경 수정·실제 실행·결과 반환이다.

Rust 1.94.1을 실제 복원해 새 crate를 컴파일하고 실행했으므로 이번에는
Fortran fallback이 필요하지 않았다. 실제 측정 binary SHA는
`303efb12fb6c6169b97440a1224d30730e5194a6230c02d469a13a25b9270c13`다.
기본 x86-64 build는 SSE2를 사용하며 AVX/AVX2/FMA는 활성화되지 않았다.
ELF가 GLIBC2.39를 요구하므로 오래된 glibc의 NCP에서는 고정된 source와
Cargo.lock으로 현지 컴파일한다. 현지 build는 별도 binary identity와
성능 영수증을 갖는다.

| DAG 대상 | 상태 |
|---|---|
| PHYS63 질적 all-angular LAP/Poisson/DtN | ESTABLISHED_REUSED |
| PHYS69 all-angular/all-radial D2(21,20),m0 | COMPLETE_REUSED |
| PHYS70 analytic block inverse | COMPLETE_ANALYTIC |
| ordered SIMD / 정확도 대조 / 독립 병렬 jobs | COMPLETE_SCOPED |
| 완성된 runner와 sandbox pilot/resume | COMPLETE |
| PHYS70 optimized L64 | READY_NOT_RUN, host UNKNOWN |
| PHYS66 longtail6 / PHYS68 validated L64 / PHYS69 native L64 | 이전 상태 유지, 새 완료본 미관찰 |
| all-angular D3와 higher remainder | OPEN, 기존 successor 식별자 보존 |
| 남은 전체 response의 수치·roundoff 인증 | OPEN, PHYS67–69 완료 범위 보존 |
| 원래 source-driven xi, 원점/incoming adjoint | 각각 OPEN |
| sigma(E), Maxwellian k_HH(T) | 각각 OPEN |

각 R1–R10, C1–C10의 산출물과 유도·코드·검증·실행·게시·백업·DAG 상태는
`LOOP_RECORD.json`과 `EXECUTION_LEDGER.json`에 분리해 기록했다.
현재 최적화 기여는 구성적 결과이며 새로운 strong no-go를 주장하지 않는다.
전역 REI DAG와 `HH_R10=OFF`는 유지한다.

## 근거 안내

- `theory/PROOF.md`: 완전한 식·분모 하한·stage mapping·복잡도·NG 검토.
- `reuse/SOURCES.json`, `reuse/LITERATURE_AND_PACKAGES.md`: 원전·공식 package 근거와 실제 사용 범위.
- `verification/INDEPENDENT_REVIEW.json`: 독립 수학/구현 검토와 닫힌 두 결함.
- `verification/PERFORMANCE_REVIEW.json`: 18개 원본 실행의 독립 해시·유리수·시간 검토.
- `verification/ADDITIONAL_EXECUTION_REVIEW.json`: 병렬12개·pilot1개·resume·L64 preflight.
- `benchmark/`: 원본 요청·결과·실행 영수증·정확한 point-error 기록.
- `figures/PHYS70_PERFORMANCE.svg`: 저장된 실제 수치만 사용한 그림.
- `CODEX_HANDOFF_PROMPT.md`, `NEW_THREAD_HANDOFF.md`: NCP와 다음 대화의 재개 계약.
