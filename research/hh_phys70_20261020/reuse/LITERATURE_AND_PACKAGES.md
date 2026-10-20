# PHYS70 — 원전·Rust 패키지의 최적화 적용 계약

2026-10-20 UTC. 이 문서는 실제로 읽은 PHYS69 소스와 공식 원전에서
도출한 적용 선택이다. 여기서 과학 적분·벤치마크를 실행하지 않았다.
구현 채택·시험·측정·게시 결과는 PHYS70의 별도 실행 영수증을 따른다.
원래 PHYS69 인증서와 완료 실행은 그대로 재사용한다.

## 1. 사용할 핵심 결과

가장 큰 알고리즘 후보는 HH의 정확한 희소 블록 구조를 이용한
Rosenbrock shifted solve이다. SIMD는 angular 행의 독립 채널 계산에,
Rayon은 서로 독립인 요청의 병렬 실행에 적용할 수 있다. 세 변경은
서로 다른 비용을 줄이므로 각각의 대조군과 측정값을 남긴다.

| 후보 | 실제 소스에서 확인한 근거 | 적용 조건 | 완료 판정에 필요한 값 |
|---|---|---|---|
| HH 블록 소거 | `rhs`, `jvp`의 Coulomb oscillator → 두 Born row → D2 순서 | 같은 단계 기준 상태·Jacobian, 모든 shift 분모 비영 | 원래 JVP로 계산한 선형 잔차와 전체 상태 비교 |
| 반복 계수·workspace 재사용 | 같은 r의 angular rows, 각 채널의 Q와 기준 상태 계수가 여러 JVP에 쓰임 | 반경 bits 및 상태 epoch의 정확한 identity | miss/hit·준비 횟수, allocation/peak memory, stale-state 검사 |
| `wide::f64x4` | angular node 하나에서 j 채널은 독립 | q-node 합산 순서와 곱셈 괄호 보존 | scalar/SIMD 결과와 실제 kernel 시간 |
| `rayon` | 서로 다른 request의 상태와 출력은 독립 | 결과 배열의 요청 순서 보존, 각 적분 내부 합산 순서 보존 | thread 1/2/4 결과 identity와 batch 시간 |

이 판정은 `native/phys69_vigilode/src/lib.rs`의 실제 내용을 읽은 결과다.
소스 identity는 [PR119 HEAD의 파일](https://github.com/cosmosapjw-quantum/WU088_HH/blob/efd1520dfc0643220f729307583ff0bc04b059e9/native/phys69_vigilode/src/lib.rs)에
고정한다. 기존 코드는 하나의 반경에 대한 angular cache가 이미 있으므로
"기존에는 cache가 없었다"고 서술하지 않는다.

## 2. 원전의 ROW 식과 HH의 대응

[Steinebach (2023), DOI 10.1007/s10543-023-00967-x](https://link.springer.com/article/10.1007/s10543-023-00967-x)의
식 (1.2)–(1.3)은 비자율 ROW 단계가 같은 step 기준의
`M − h γ J`를 사용하며 explicit time partial도 포함함을 명시한다.
HH의 mass matrix는 identity이고 시계는 `tau=65-r`다. 따라서 원래
VigilODE tableau, 단계 RHS, time partial, embedded error와 PI 제어를
보존한 채 이 선형계의 풀이만 특화할 수 있다. 해당 논문은 이 일반
적용 근거다. 다음 HH 블록 공식은 현재 코드의 식을 직접 소거한 것이다.

`n=L+1`, `a=21`, `b=20`라 놓고 현재 scale을 포함한 상태를
`(f_j,g_j,A_j,B_j,z)`로 쓴다. 그러면

\[
f'_j=-g_j,\qquad g'_j=Q_j f_j,\qquad
A'_j=C_{aj} f_a f_j,\qquad B'_j=C_{bj} f_b f_j,
\]

\[
z'=\sum_j A_jB_j/f_j^2,\qquad
Q_j=k^2+2/r-j(j+1)/r^2,
\]

여기서 `C_aj=2^80 V_aj(r)`, `C_bj=2^80 V_bj(r)`다.
`z=2^160 D2`이므로 마지막 식에는 별도 scale이나 켤레가 없다.
정확한 수학에서 `s=h γ`로 놓은 `(I-sJ)x=b`의 순차 소거는

\[
\Delta_j=1+s^2Q_j,\qquad
x_{f_j}=(b_{f_j}-s b_{g_j})/\Delta_j,\qquad
x_{g_j}=b_{g_j}+sQ_jx_{f_j},
\]

\[
x_{A_j}=b_{A_j}+sC_{aj}(f_a x_{f_j}+f_jx_{f_a}),\qquad
x_{B_j}=b_{B_j}+sC_{bj}(f_b x_{f_j}+f_jx_{f_b}),
\]

\[
x_z=b_z+s\sum_j\left[
\frac{x_{A_j}B_j+A_jx_{B_j}}{f_j^2}
-\frac{2A_jB_jx_{f_j}}{f_j^3}\right].
\]

모든 `f_j`와 `Delta_j`가 비영일 때 이 소거의 작업량과 저장량은
`O(n)`이다. 이는 전체 선형계의 정확한 구조를 쓴 것이며 Jacobian의
항을 버린 근사가 아니다. 구현에서는 upstream U-form이 사용하는
shift/RHS scale을 실제 API에 맞춰야 한다. 원래 JVP를 이용한
`b-(I-sJ)x` 잔차를 별도로 평가하면 이 대응을 직접 검증할 수 있다.

부호가 다른 `Q_j`도 허용하므로 분모 검사를 생략할 수 없다.
큰 step에서 `Delta_j`가 0에 접근할 수 있으며, 이 경우 기존 step 실패
및 감소 계약으로 전달해야 한다. 또한 정확한 산술의 동등성이 binary64
출력의 bit identity를 자동 보장하지는 않는다. 변경된 선형 풀이의
잔차·전체 상태·기존 인증값에 대한 D2 오차를 각각 확인한다.

## 3. SIMD: 채널 병렬성과 감소 순서를 분리한다

공식 release manifest를 직접 읽어 `wide=1.7.1`을 확인했다.
Rust 최소 버전은 1.89, edition은 2024이며 라이선스는
`Zlib OR Apache-2.0 OR MIT`다. 공급된 Rust 1.94.1로 빌드할 수 있는
버전 범위다. [실제 published Cargo.toml](https://docs.rs/crate/wide/1.7.1/source/Cargo.toml)을
기준으로 고정하고 Cargo.lock의 registry checksum을 보존한다.
동일 version 문자열을 가진 mutable main의 dependency 내용은 이미
published manifest와 다르므로 main을 release source로 대체하지 않는다.

[`f64x4` API](https://docs.rs/wide/1.7.1/wide/struct.f64x4.html)의
`new`, `splat`, `to_array`와 lane별 `+`, `*`를 쓰면 `j=4k..4k+3`의
네 채널을 함께 계산할 수 있다. 각 lane은 동일한 angular node 순서를
따르고, tail 채널은 scalar로 처리한다. 기존의
`(p_a * p_j) * v`라는 괄호도 유지한다. `p_a*p_j`를 사전 계산한다면
그 exact binary64 곱만 재사용하고 weight의 곱셈 위치를 바꾸지 않는다.

현재 목적에서 `reduce_add`로 node나 채널 합을 묶지 않는다. 이 API의
문서는 감소 순서를 고정하지 않는다. `mul_add`도 하드웨어 FMA 지원에
따라 rounding 동작이 달라진다고 명시한다. 기존 scalar `exp`와 `sqrt`를
wide의 초월함수 근사로 일괄 교체하는 것은 별도 정확도 변경이므로
같은 연산 순서를 유지하는 이번 첫 적용에 포함하지 않는다.

[`wide`의 target 설명](https://docs.rs/crate/wide/1.7.1)에 따르면 SIMD
선택은 compile time에 이뤄진다. 배포 기본값은 호환 가능한 CPU target으로
두고 `-C target-cpu=native`는 NCP의 실제 CPU에서 별도로 컴파일할 때만
사용하는 선택이다. 한 host용 native binary를 다른 host에서도 안전하다고
가정하지 않는다. `std::simd`는 [현재 공식 Rust 문서](https://doc.rust-lang.org/std/simd/index.html)에서도
nightly 실험 API이므로 이 목적의 stable toolchain에는 `wide`가 직접적인
재사용 후보다.

SIMD 또는 precomputation이 peak memory까지 줄이는지는 측정해야 한다.
예를 들어 두 row의 모든 basis 곱을 저장하면 계산은 줄지만 저장할 계수는
증가할 수 있다. allocation 횟수 감소, 실제 바이트 감소, peak RSS 감소를
동일한 주장으로 합치지 않는다.

## 4. 병렬화: 독립 요청만 병렬로 실행한다

공식 [Rayon 1.12.0 published manifest](https://docs.rs/crate/rayon/1.12.0/source/Cargo.toml)와
[release tag의 원본 manifest](https://github.com/rayon-rs/rayon/blob/v1.12.0/Cargo.toml)를
확인했다. Rust 최소 버전은 1.80, edition은 2021, 라이선스는
`MIT OR Apache-2.0`다. main은 같은 version 문자열로 이미 MSRV/edition이
바뀌어 있으므로 release와 구분한다.

[`ThreadPoolBuilder::num_threads`](https://docs.rs/rayon/1.12.0/rayon/struct.ThreadPoolBuilder.html)에
양의 thread 수를 명시하고, 하나의 pool을 만든 뒤 `install` 안에서
독립 요청 배열의 `par_iter().map(...).collect::<Vec<_>>()`를 실행하는
계약이 적합하다. [`IndexedParallelIterator`](https://docs.rs/rayon/1.12.0/rayon/iter/trait.IndexedParallelIterator.html)의
정해진 index 순서로 결과를 모으고, 반복적인 collection이 필요한 경우
`collect_into_vec`로 기존 버퍼를 재사용할 수 있다.

요청의 출력 순서와 계산 내부의 부동소수점 감소 순서는 서로 다른 문제다.
독립 요청마다 own state/workspace/cache를 두고, 각 적분 안의 scalar
감소 순서를 보존한다. 다른 job이 같은 completed output에 기록하거나
공유 mutable cache의 state epoch를 바꾸지 않도록 해야 한다.
Rayon의 data-race freedom만으로 이 과학적 identity 계약이 증명되지는 않는다.

반경 panel 간에는 carry 의존성이 있으므로 완성된 검증 적분의 panel
순서를 그대로 병렬 map으로 바꿀 수 없다. inner `n=29` 또는 `65` loop를
매 callback마다 thread pool에 넘기는 방법은 overhead를 실제 측정한 뒤
선택해야 한다. 독립 campaign의 batch 병렬성이 먼저 판별할 경로다.

## 5. 같은 정확도에서 비교할 측정 계약

Steinebach 논문의 section 4는 tolerance마다 실제 걸린 시간과 달성한
오차를 함께 비교하며, 내부 step 지점의 오차와 dense output의 오차를
구분한다. [공식 SciML ROBER benchmark](https://docs.sciml.ai/SciMLBenchmarksOutput/stable/StiffODE/ROBER/)도
공통 reference, error metric, tolerance sweep, thread 설정을 실행 코드에
남긴다. 이 방법을 HH에 적용하되 그 문헌의 숫자나 solver 순위를 HH의
속도 근거로 가져오지 않는다.

이번 HH 비교는 고정된 동일 request·seed·원래 source SHA, 같은 compiler
및 CPU target, 같은 output schedule에서 수행한다. 필요 측정은 다음과 같다.

1. 변하지 않은 baseline callback과 새 kernel의 동일 입력 비용:
   준비·재사용을 구분하고 결과 차이·JVP/RHS count를 기록한다.
2. 새 구현의 전체 요청 비용: compile/setup/적분/output 시간을 나누고,
   accepted/rejected steps 및 완전 종점 도달을 기록한다.
3. 정확도: 전체 scaled 상태 차이와 D2의 기존 인증값에 대한 오차를
   함께 기록한다. local WRMS tolerance를 전체 구간 인증으로 바꾸지 않는다.
4. 병렬 실행: thread 1/2/4에서 동일 요청 배열을 사용하고 결과 identity,
   총 batch wall time과 peak memory를 보고한다. 한 요청의 latency 감소와
   여러 요청의 throughput 증가를 구분한다.

변경된 경로의 성능을 판별하는 짧은 측정은 새 optimization evidence다.
완료된 PHYS64/66/67/68/69 과학 캠페인의 재검증을 명목으로 같은 적분을
반복하지 않는다. profile에서 hot path가 아닌 후보는 코드 복잡성만
늘리지 말고 그 판별 결과를 보존한다.

## 6. 조사와 적용 상태

Exa 검색은 두 각도에서 각 5개, 총 10개 결과를 검토했다.
SciSpace의 자연어 질문 한 번에서 논문 10개가 반환됐고, 현재
비자율 ROW 계약에 필요한 Steinebach 원문을 직접 열어 적용했다.
공식 Rust release manifest와 API는 별도 직접 조회했다.
원전 identity·조회 실패의 해소·채택하지 않은 문헌은 `SOURCES.json`에 있다.

| 상태 축 | 이 문서 작성 시 실제 상태 |
|---|---|
| 유도·재사용 | 정확 HH 블록식과 SIMD/병렬 적용 조건 도출 |
| 코드 | root 구현에 전달한 후보; 이 문서가 구현 완료를 주장하지 않음 |
| 검증·계산 | 이 조사 작업의 과학 적분 0, 벤치마크 0 |
| 게시·백업 | root의 실제 후속 ACK를 사용 |
| DAG | PHYS70 최적화 의존성을 지원; PHYS63/D2 인증·HH_R10 상태 변경 없음 |
