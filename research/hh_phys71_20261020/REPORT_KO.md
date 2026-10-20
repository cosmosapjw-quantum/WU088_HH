# PHYS71 — 원래 HH 외부 DtN의 all-angular 3차 계수 인증

## 1. 실제 결과와 범위

원래 atomic Hamiltonian에서 외부 DtN의 한 성분
`D3(21,20), m=0 = Z'''(0)/6`을 계산했다. 유한 계산은 L=36,
T=65의 76개 패널이며, 모든 제외 angular mode와 r>65의 효과는
각각 증명된 상한으로 합성했다. 원래 all-angular, all-radial 계수에 대해

\[
\begin{aligned}
z={}&(2.14300135468641834333042543662\\
&+1.71865149630238869433259719024\,i)\,10^{-71}\ a_0^{-1},\\
|D_{3,\infty}(21,20)-z|&\le 7.121295358370\,10^{-79}\ a_0^{-1}.
\end{aligned}
\]

출력 중심의 반올림 오차까지 포함한 값이다. 고정 목표 `1e-78`을 통과했다.
세부 중심과 exact rational budget은 [DISPLAY_RESULT.json](DISPLAY_RESULT.json),
실제 최종 인증서는 [ALL_ANGULAR_CERTIFICATE.json](d3/run_l36_t65_stable_errors/ALL_ANGULAR_CERTIFICATE.json)에 기록한다. 최초 producer의 CERTIFICATE.json은 수치 결과 증거로 보존하며, 그 안의 radial 요약 소수는 독립 감사에서 inward rounding으로 판정됐다. 수정된 최종 인증서의 실제 SHA는 DISPLAY_RESULT와 최종 DELIVERY에서 읽는다.

이 결과의 범위는 이 3차 Taylor 계수 한 성분이다. 전체 λ=1 응답,
4차 이상 Born 나머지, 원래 source-driven xi, 원점/incoming adjoint,
sigma(E), Maxwellian k_HH(T)는 각각 남은 의무다. PHYS63의 실제
all-angular LAP/Poisson/DtN 질적 존재와 PHYS69의 all-angular D2는
완료 근거를 그대로 재사용한다. HH_R10=OFF다.

## 2. 먼저 확인한 원격·백업 상태

연구 시작 전에 실제 PR120 HEAD
`31745376ca751e7c925b3b1453ef292436cd30e8`과 원격 129개 branch,
최근 PR·commit·Actions·comments 및 관련 저장소의 새 기록을 조사했다.
PR120의 source commit은 `e73048e1399263eac3d40ffd3e700807bbc7c72e`다.
사용자 최초 인계의 PR115는 이 시점의 최신 원격이 아니었다.
최신 PHYS70 ledger와 DAG가 로컬/원격에서 같은 바이트임을 확인했다.

접근 가능한 Library·Dropbox·Drive 범위에서는 새 HH longtail/L64/D3
완료 영수증을 발견하지 못했다. 이는 조사한 범위의 결과다. 다른 대화는
PersonalContext가 unavailable을 반환해 `BLOCKED_CONTEXT_ACCESS`이며,
실제 NCP host는 조회하지 못해 UNKNOWN이다. Dropbox의 일부 검색에는
상한/필터 제약이 있었다. 전체 세계에 새 결과가 없다는 주장은 하지 않는다.

VigilODE PR76, BASS_HE PR78, REI PR198/199, REC PR110 및 새 VigilODE
연구 파일은 별도로 분류했다. generic solver·toy 또는 다른 물리계의
실행을 HH 완료 영수증으로 승격하지 않았다. 이미 PHYS70에서 사용한
pinned VigilODE/Rust block solver·ordered SIMD·독립 작업 병렬화는
그대로 유지했다. 이번 단위는 그 벤치마크를 반복하지 않았다.

정확한 범위와 읽기 근거는 [Git intake](intake/GITHUB_INTAKE.json)와
[backup intake](intake/BACKUP_INTAKE.json)에 있다. 원래 PHYS66 최종
SHA `993317b1...` ZIP의 정확한 버전은 여전히
`BLOCKED_ARTIFACT_ACCESS_EXACT_FINAL_VERSION`이다. 이번 계산은 실제
회수·해시 검증한 PHYS68/69 profile archive를 사용했으며 해당 ZIP을
가짜로 복원했다고 주장하지 않는다. 앞선 PHYS70 Drive 업로드의
ACK 미확인 상태도 UNKNOWN_UNRESOLVED로 유지하고 재시도하지 않았다.

## 3. 바꾸지 않은 물리와 먼저 고정한 요청

| 항목 | 고정값 |
|---|---|
| 좌표와 단위 | 원래 atomic coordinates, a0/Hartree |
| 외부 경계 | B=27 |
| k, E | 7/10, 49/200 Hartree |
| shift | 7/10 zhat |
| Hamiltonian | h=-Delta/2-1/r-(1+1/d)exp(-2d), d=abs(x-0.7zhat) |
| radial perturbation | V=2(1+1/d)exp(-2d) |
| outgoing / DtN | H+=G+iF_C, Z=+u'u^-1 |
| 다른 eta | eta=Fy, xi=Fy-phi, eta_C=-10/7 |
| 새 유한 요청 | L36, T65, m0, external21/20, h=1/4, rho=1/2 |
| Taylor / arithmetic | N80, 384 bits, angular constants1024 bits |
| 새 절대 목표 | 1e-78 a0^-1, 첫 pilot 이전 고정 |

원래 frozen complex128 NPZ SHA256은
`f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`다.
NPZ 바이트, PR114/115의 최신 proof 바이트를 그대로 검증했다.
오래된 PHYS65 proof로 원격 proof를 덮지 않았다. AGENTS.md는 현재의
연구 순서만 앞에 추가했으며 기존 전체 suffix의 바이트를 보존했다.
기존 D2 목표 `1e-62`도 바꾸지 않았다.

## 4. 실제 유도: 두 source row로 D3 구성

기존 q-profile의 전체 enclosure를 사용해

\[
q_{aj}(r)=\int_r^\infty f_a(s)f_j(s)V_{aj}(s)\,ds,\qquad
P'_{a,j}=q_{aj}/f_j^2,\quad P_{a,j}(27)=0,
\]
\[
U_{a,j}=f_jP_{a,j},\qquad
D_{3,ab}=\sum_{j,k}\int_{27}^\infty U_{a,j}V_{jk}U_{b,k}\,dr
\]

를 얻었다. 복소 conjugation이 없는 bilinear 식이다. `D3=Z'''(0)/6`에
factorial이 이미 포함되어 추가 6을 곱하지 않는다. 직접 미분하면
`-U''-Q_j U=f_a V_aj`이므로 부호와 원래 경계조건을 점검할 수 있다.

상속한 76+76개 profile payload에는 총 73개의 서로 다른 q pair가
각 패널마다 있다. a=20,21만 필요하며, q20,21을 공유하더라도 분모
f20²/f21²가 다르므로 새 forward primitive는 74개다. 이전 전체
Taylor array가 저장돼 있다고 가정하지 않는다. 저장된 q-center ball과
majorant를 보존하고 analytic derivative coefficients를 재구성한다.
이 재구성은 새 downstream 평가로 집계했으며 이전 q/D2 적분 호출은 0이다.

무한 angular tail은

\[
C_j=77\ (j\le28),\qquad C_j=\frac{800}{189}(j+1)\ (j\ge29),
\]
\[
v_d=\min(3\cdot10^{-23},\;10^{-d}/(9\cdot10^{18}))
\]

의 세 결합을 보존하는 double convolution으로 상계한다. 가운데
`v_|j-k|`를 균일한 큰 값으로 버리지 않는다. radial factor는
`(1/16) integral_0^infinity exp(-2x)(1-exp(-2x))² dx = 1/96`이다.
결과적으로 L 바깥 두 방향의 tail을 합하되 겹친 영역을 양으로 두 번
세어도 안전한 상한을 얻는다. 멀리 떨어진 index의 합은 degree5
polynomial times geometric series로 정확히 합산한다. 무한 합을
어떤 임의의 큰 index에서 끊은 수치 검사는 아니다.

| L | all-radial 제외 angular D3 상한, a0^-1 |
|---:|---:|
| 28 | 3.45716107716002415432785e-64 |
| 35 | 4.45815477016082342197050e-77 |
| 36 | 5.63697247035361181066503e-79 |
| 40 | 1.21471050862947663398945e-86 |
| 64 | 1.81089325144712534358499e-133 |

L36은 이미 확보한 두 row를 재사용하면서 새 목표를 만족시킬 수 있는
선택이다. L35의 상한만으로는 목표를 통과하지 못한다. 상세 증명과
정확한 유리수는 [ANGULAR_D3.md](theory/ANGULAR_D3.md) 및
[RESULTS.json](angles/RESULTS.json)에 있다.

## 5. 구현과 실제 오차 전파 개선

새 구현은 기존 Arb/FLINT의 enclosed Coulomb 함수, exact rational
angular moments, Taylor/Cauchy integration을 재사용한다. 각 새 disk에서
f_j의 zero-free lower bound가 양수여야 진행한다. 함수 평가·반올림·상속
오차·radial Taylor tail을 함께 포함한다. 부동소수 tolerance를 인증
오차로 대신하지 않는다.

m0 각도 부분은 37개 mode의 두 Legendre 다항식을 곱하고 0..72차
moment 73개와 수축한다. 가운데 V의 1369개 행렬 원소를 각각 만드는
대신 73개 moment function을 사용한다. 입력 q derivative 재구성에
쓰는 73개 source-pair 계산은 별도다. 이 수는 구조적 작업량 비교이며
새 end-to-end 속도 배율을 측정했다고 주장하지 않는다.

첫 실제 pilot은 종료코드0과 checkpoint를 남겼지만, 수치 반경이
`1.4690349306218242e-72`로 고정 목표에 실패했다. 나머지75개를 즉시
실행하지 않고 이 pilot과 당시 소스 바이트를 보존했다. 각도 monomial
변환이 입력 구간의 의존관계를 잃으면서 오차를 크게 확대하는 문제가
실제 자료에서 드러났다.

개선된 방법은 각 response Taylor 계수를 정확한 dyadic 중심 p와
그 계수 오차로 나눈다. 변환에는 p만 사용하고, 오차는 원래 정규직교
기저에서 weighted coefficient norm으로 제한한다. h=1/4, rho=1/2에서

\[
A_a=\sum_{j,n}|p_{a,j,n}|_1h^n,\qquad
E_a=\sum_{j,n}{\rm rad}_1(U_{a,j,n})h^n,
\]
\[
E_{\rm coef}\le\frac{M_V}{1-h/\rho}
(E_aA_b+A_aE_b+E_aE_b).
\]

이 식은 실제 함수값의 작은 차이만 주장하는 것이 아니라 degreeN으로
project한 계수의 차이를 직접 제한한다. 비음수 weighted convolution에서
고차 조건을 풀면 상한만 증가한다. 따라서 기존 **실제 integrand의
Cauchy tail**에 이 계수 상한을 한 번 추가하면 된다. midpoint 변환 자체의
roundoff와 V moment 오차는 계속 Arb ball에 남는다. 원래 carry 오차를
삭제하거나 중심값을 참값으로 취급하지 않았다.

수정 pilot의 중심 dyadic, 74개 carry, inherited hashes, Cauchy remainder는
첫 pilot과 정확히 같았다. 반경은 `5.554828422675563e-86`으로 약
`2.6446090119094e13`배 줄었다. N80/384비트/목표를 그대로 유지한 상태다.
이는 **인증 구간 폭의 개선**이며 wall-time 속도 배율이 아니다.
[오차 증명](theory/ANGULAR_ERROR_STABILITY.md)과
[독립 pilot 판정](verification/STABLE_PILOT_INDEPENDENT_GATE.json)에 근거가 있다.

## 6. 실제 계산과 최종 오차 예산

| 실행 | 실제 새 패널 | 재사용 | 종료·판정 |
|---|---:|---:|---|
| 초기 pilot | 1 | 0 | exit0, checkpoint 보존, 수치 목표 미달 |
| 수정 pilot | 1 | 0 | exit0, 독립 gate PASS |
| 같은 수정 campaign의 나머지 | 75 | 1 | exit0, 76/76 수치 완료·radial 소수 교정 필요 |
| exact analytic 후처리 | 0 | 76 | radial 상한을 위로 교정·최종 독립 검토 별도 |
| 완료 후 resume | 0 | 76 | 수치 callback0, worker0, 관찰한 파일 변경0 |

따라서 새 패널 계산 호출은 총77회이며, 승인된 완성 결과는76개다.
기존 완료 scientific campaign의 재실행은0이다. 수정 campaign의 두
실행 wall time 합은 약217.979초, 첫 미달 pilot까지 합하면 약227.558초다.
단일 worker와 thread 환경1, address-space limit4GiB를 적용했다.
4GiB는 측정 peak RSS가 아니라 제한값이다. 실제 NCP 제출은0이다.

| 오차 종류 | 위로 반올림한 상한, a0^-1 | 근거 |
|---|---:|---|
| finite L36,T65 수치·상속·함수 평가·roundoff | 5.73125795490702815268701e-86 | 76개 ball 적분의 합 |
| r>65 radial cutoff | 1.48432231489e-79 | PR115 beta3, finite L<=64에 적용 |
| L36 바깥 모든 angular mode | 5.63697247035361181066503e-79 | 새 exact infinite convolution |
| 중심 dyadic 기준 합 | 7.12129535836940730136784e-79 | 위 세 항의 정확한 합 |
| 표시한 decimal 중심 기준 최종 상한 | **7.121295358370e-79** | exact printing displacement 추가 |

독립 감사는 양의 exp(76) 급수와 그 tail로 beta3를 직접 감싸서, 요약1.484322e-79가 실제1.484322314885...e-79보다 작음을 찾았다. PR115 원문의 위쪽 끝점1.48432231489e-79를 채택하고 모든 numerical panel을 그대로 재사용했다. 이전 REQUEST/fingerprint/CERTIFICATE, 당시 campaign 소스와 첫 실패 audit는 보존한다. 현재 campaign의 상수도 수정했으며, 새 최종 인증서는 원래 producer를 가장하지 않고 별도 analytic provenance를 가진다.

기본 Arb display 문자열의 자릿수는 최종 인용 중심으로 쓰지 않는다.
표시 중심은 dyadic에서 별도 생성했고 그 반올림 오차까지 정확히 합쳤다.
radial/각도 tail은 이 계수의 나머지이며 λ=1 전체 Born 나머지가 아니다.

## 7. 검증과 재사용 가능한 코드

새로 통과한 서로 다른 테스트는54개다: angular10, 상속 reader13,
finite core8, 초기 campaign13, 실행 경계 표적6, 새 centered angular4.
여러 표적 실행의 합이며 전체54개를 하나의 최종 suite로 다시 실행하지
않았다. 초기 실패·fixture 오류·개선 후 PASS를 모두 남겼다.
새 centered 테스트는 complex corner16개, exact Fraction polynomial 및
적분 oracle, projection 반례, zero-error와 잘못된 입력을 검사한다.

radial 상수 교정 전 원래 producer로 수행한 완료 resume의 관찰 범위는 src, scripts, PHYS71 d3다. 해당288개 파일의
SHA256/size/mode/mtime가 모두 같고, 새 수치 callback0, 새 worker0,
새 invocation receipt0을 확인했다. 확인용 바깥 CLI 프로세스1개와
검증 영수증 쓰기는 실제 수치 작업과 구분한다.

독립 표준 Python verifier는 saved panel과 carry, source/proof/request
fingerprint, exact rational 오차 합, 두 무한 tail, 표시 중심 오차를
다시 계산한다. 이것은 저장된 증거의 검증이며 Coulomb 함수나 적분을
다시 실행하지 않는다. 현재 campaign은 교정 때문에 원래 producer와 fingerprint가 다르다. 원래 수치 CLI를 강제로 재개하지 않고 finalizer/portable verifier를 사용한다. 현재 verifier runtime과 결과를 만든 producer
runtime을 구분하므로 NCP에서 producer의 Python patch version이
없어도 해당 증거의 읽기 검증을 할 수 있다.

| 경로 | 역할 |
|---|---|
| src/wu088_hh/phys71_angular_d3.py | 정확한 infinite angular sum과 tail |
| src/wu088_hh/phys71_inherit.py | 기존152 payload의 strict 읽기·해시·carry 검증 |
| src/wu088_hh/phys71_d3.py | forward primitive, 73 moments, 안정화된 enclosed 적분 |
| src/wu088_hh/phys71_campaign.py | immutable panels, certificate, 정확한 resume |
| scripts/phys71_ncp.py | bounded child, 자원·timeout·thread 제한 |
| src/wu088_hh/phys71_finalize.py 및 scripts/phys71_finalize.py | 저장된 수치 결과의 별도 exact analytic 교정·완료본 재사용 |
| verification/verify_saved_d3.py | portable stdlib scientific evidence 검증 |

소스·실행 identity에 실제 사용한 모듈과 원래 proof SHA를 포함했다.
잘못된 full box/중복 scope/count를 재해시해도 거부한다. lock 뒤에 생긴
campaign에 대한 재개 조건도 다시 검사한다. timeout 때 직접 child가
먼저 종료돼도 남은 소유 process group을 정리한다. 완료 resume에서는
bytecode·lock·결과 파일을 새로 만들지 않는다.

## 8. 외부 문헌·코드의 실제 재사용

NIST DLMF33.2는 Coulomb convention, Johansson의 Arb 논문과 rigorous
integration 논문은 enclosed arithmetic/analytic remainder의 배경,
FLINT 공식 문서는 API와 적분 원리를 확인하는 데 사용했다. 실제 실행은
python-flint0.8.0 / FLINT3.3.1 / Python3.12.14다. 최신 문서의 다른 버전을
실행 버전으로 오인하지 않는다. SciSpace/Exa 결과의 사용 범위는
[SOURCE_INDEX.json](theory/SOURCE_INDEX.json)에 분리했다.

Wolfram은 실제 미분식·scalar 모델·radial integral·angular 변수변환을
확인했다. 첫 angular 입력의 rR token 오류와 수정한 두 번째 호출을
모두 보존했다. 최종0/1/6 출력만 따로 만든 성공 영수증이 아니다.
논문의 일반 정리가 이번 HH 수치 결과를 대신 증명했다고 주장하지
않으며, 문헌상 최초라는 주장이나 strong no-go 주장도 하지 않는다.

## 9. 게시·백업·다음 연구

과학 결과와 배포 상태는 별도다. 이 source snapshot이 만들어지는 시점의
정확한 게시·백업 상태는 NEXT_DAG와 publication 영수증을 확인한다.
실제 source commit과 후속 metadata commit, 두 capsule의 SHA256,
provider ACK, 깨끗한 복원 검증은 최종 외부 PHYS71_DELIVERY 파일에 묶는다.
예정된 commit이나 업로드 요청을 완료된 게시·백업으로 기록하지 않는다.

교정된 D3의 독립 최종 검토가 통과했으므로 새 D3 node만 COMPLETE로 올렸다.
기존 `PHYS70_ALL_ANGULAR_D3_AND_HIGHER_REMAINDER` 식별자는 보존하고
`PARTIAL_D3_COMPLETE_HIGHER_REMAINDER_OPEN`으로 기록한다. 고차 remainder는
아직 OPEN이다. 무한 j에서 다항식으로 커지는 C_j를 Gamma64로 치환해서
all-order contraction이라고 주장할 수 없다. 다음의 고정 의무는 실제
outgoing Coulomb Green kernel의 angular/radial 가중 operator bound로
4차 이상을 합산하는 것이다. 실패한 충분조건과 물리적 불가능성도 구분한다.

NCP에는 완성된 runner와 입력·의존성·실제 완료 증거를 전달한다. 이 D3를
새로 실행시키지 않는다. NCP가 사용 가능하고 동일 완료본이 없다면 기존
PHYS70 L64 요청은 별도 scientific obligation으로 실행할 수 있다.
그 역할은 컴파일·작은 환경 수정·실제 실행이며 새 solver 설계가 아니다.

## 최종 독립 검토

[C9_INDEPENDENT_FINAL_REVIEW.json](verification/C9_INDEPENDENT_FINAL_REVIEW.json)은 `PASS_CORRECTED_SINGLE_ALL_ANGULAR_ALL_RADIAL_D3_COEFFICIENT`를 기록한다. 첫 audit의 inward rounding 발견과 교정 후 첫 full audit PASS를 구분한다. 최종 full audit는 관찰한90개 파일을 변경하지 않았으며, 이어서 corrected finalizer를 정확히 한 번 재사용한 검사도282개 관찰 파일의 변경0, 새 물리 패널0, 쓰기0으로 통과했다. 표시 중심의 exact L1 반올림 오차는 약3.67524692068853e-101이며 최종 상한에 포함돼 있다.
