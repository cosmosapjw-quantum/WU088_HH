# WU088_HH PHYS67 — 원래 first-Born 항의 수치 인증

## 이번에 확보한 결과

원래 Hamiltonian의 \(D_{1,21\,20}(27),m=0\)를 각도 적분의 정확한 유한식과
복소 구간 반경 적분으로 계산했다. 저장한 정확한 dyadic 중심을 기준으로
수치 오차는 \(2.328\times10^{-41}\,a_0^{-1}\) 미만이다. \(T=65\) 바깥의
반경 tail은 기존 PR115 정리로 \(4.973\times10^{-53}\,a_0^{-1}\) 미만이다.
반경 무한대까지의 원래 단일 first-Born 항에 이 두 성분을 합칠 수 있다.

\[
D_{1,21\,20}(27)\simeq
(2.7660422459784296+0.4500676730172737i)10^{-24}\ a_0^{-1}.
\]

이 소수는 읽기용 근삿값이다. 인증의 중심·반경은
`first_born/FIRST_BORN_CERTIFICATE.json`의 정확한 이진 유리수다.
전체 nonlinear DtN 값이나 원래 source-driven xi를 이 수로 대체하지 않는다.

동시에 다음 두 성분을 완성했다.

| 새 결과 | 확보 범위와 근거 |
|---|---|
| 각도 구적 | 모든 r>=27, finite L<=64, 모든 signed m에서 exact Gauss–Legendre rule의 연산자 오차 정리. L64,Q128이면 epsilon=2/(9*10^146), exp[-2(r-27)] 가중치. |
| Coulomb | ell=0,20,21,28,64와 r=27,55,65,75의 20점에서 512-bit H+, d_r H+, Z와 H(r)/H(27) 포함 구간. 기존 binary64 Z의 최대 절대오차 <8.387e-17 a0^-1. |

실제 현재 환경은 Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, mpmath 1.3.0,
SymPy 1.14.0, pytest 8.4.2, python-flint 0.8.0 / FLINT 3.3.1이다.

## 먼저 수행한 백업·GitHub 대조

최신 PR은 PR116이었다. 실제 HEAD는
`1a1e5b6df5e5f88de851bc4686949089e2444291`이고 부모는 사용자가 고정한
PR115 `445d82db9c42b4f2f81e4ac1b107dec3b69b3c24`다. PR116은
`ARTIFACT_ACCESS_STATUS.json` 하나를 추가한 과거 접근 차단 기록이며,
C5–C8 코드나 새 실행이 아니다. PR114/115의 과학 결과는 그대로 유효하다.

Google Drive와 Dropbox의 최신 PHYS66 백업은 37,727-byte R5 ZIP이었다.
두 제공자 및 관찰한 GitHub tree/branch에서 새 longtail 영수증을 찾지 못했다.
이 사실과 NCP host의 실제 접근·실행 상태를 구별한다. 원격 접근 시도와
최종 전달 상태는 `recovery/`, `ncp_delivery/`, `publication/`의 실제 영수증을 따른다.

대화 파일 저장소에서 요청한 네 이름의 파일은 회수했지만 내용은 이전 버전이었다.

| 구분 | 사용자 지정 최종 버전 | 실제 회수한 이전 버전 |
|---|---|---|
| ZIP SHA256 | 993317b1c78edf496ec5a82a261eceb5a54515a78e38d139a924722a5d28f891 | 84c29de77c77a0d5699859599f3eed2d43479bd7621ca691e97449e3cb02a1c3 |
| local snapshot | 2d08f8da64d647938ff548fdf5fa550c58d947dc | 3794ac6b6e1db86f0f2ac57558402de13694535c |
| add-only paths | 45 | 84 |
| 현재 접근 | BLOCKED_ARTIFACT_ACCESS_EXACT_FINAL_VERSION | 실제 bytes 회수, 91개 payload manifest 검증 |

정확한 최종 ZIP의 bytes를 확보했다고 주장하지 않는다. 사용할 수 있는 이전
버전은 그 자체의 manifest와 실제 코드를 검증하여 독립적으로 식별했다.
그 84개 추가 경로를 실제 PR116 checkout에 `git apply --check` 후 적용했고,
새 branch는 실제 Git ancestry를 갖는다. 회수된 이전 local snapshot을 PR115의
후손으로 소급해 주장하지 않는다.

PR115의 여섯 경로, 최신 PR114 proof와 Coulomb bound 코드, 원본 NPZ 등
아홉 보호 파일의 Git blob이 모두 원격 원본과 같다. 오래된 local PHYS65 proof를
원격 proof에 덮어쓰지 않았다. `local_verification/PROOF.md`, C5–C8 보고서와
handoff는 원래 위치의 과거 기록으로 유지한다. 현재 판정은 PHYS67 문서가 맡는다.

## 실제 유도

각도 변수 mu와 원래 shift R=7/10에 대해 d=r+t로 치환하면

\[
\mu=-t/R+(R^2-t^2)/(2Rr),\qquad -R\le t\le R.
\]

정규화 m=0 basis의 Legendre 곱은 유한 다항식이므로 원래 V=2S의 행렬 원소가
exp(-2r)에 r의 유한 Laurent 다항식을 곱한 정확한 식으로 바뀐다. 모든 계수는
정확 유리수와 exp(±2R)로 계산한다. 이 식을 1024-bit 구간으로 준비하고,
outgoing Coulomb H+=G+iF를 256-bit 복소 구간으로 적분한다. 적분 callback은
Re(r)>R인 analytic domain을 전체 test ball에서 검사한다.

D1에는 중간 angular index 합이 없다. 따라서 두 external mode를 포함하는
모든 finite projection에서 같은 원소이며 unrestricted first forcing의 그
원소와도 같다. D2부터의 중간 채널 및 제외 angular response에는 이 결론을
확장하지 않는다. 상세 유도와 단위·부호·분기 검토는 `first_born/PROOF.md`에 있다.

별도 angular 정리는 PHYS58의 E10 타원 위 majorant를
M exp[-2(r-27)]로 강화했다. 정규화 associated Legendre 곱은 odd m에서도
차수 <=2L 다항식이므로 Q>=L+1인 exact Gauss sampling은 isometry다.
차수 N=2Q-1-2L의 Chebyshev projection을 삽입하면 채널 수에 비례하는
계수 없이 epsilon=(8M/9)10^-N을 얻는다. 이 정리는 실제 f64 nodes/basis의
평가 오차를 포함하지 않는다.

Coulomb 검증은 ell-shift recurrence, Wronskian, ODE series와 Tricomi U
정의식의 직접 미분을 비교했다. 특히 ell64,r27에서
Im Z≈1.3348657e-51 a0^-1의 양의 하한을 분리했다. 공유하는 FLINT 기반과
별도 mpmath 소프트웨어를 구분하여 산식 일치를 과장하지 않는다.

## 실제 실행·검증과 완료 실행 재사용

| 항목 | 이번 실행 및 재사용 상태 |
|---|---|
| 회수 C5–C8 통합 회귀 | 현재 host에서 57/57 PASS |
| 새 angular 테스트 | 25/25 PASS |
| 새 Coulomb 테스트 | 24/24 PASS |
| 새 first-Born 테스트 | 22/22 PASS |
| 새 angular 수치 판별 | 90자리 독립 직접 적분 대 Gauss의 6건 비교, analytic bound 안 |
| 새 Coulomb 실제 계산 | 20점, 약 5.37초 |
| 새 D1 적분 | 유효하지만 목표 미달 1회 보존, 오차 배분 수정 후 1회 성공; 성공 3269 evaluations, 약 7.68초 |
| 독립 exact 산식 검토 | 별도 Legendre 3항/moment recurrence로 고차 (21,20)를 포함한 5건 exact match |
| NCP runner 준비 | 깨끗한 추출본에서 preflight-only PASS; solver 실행 0 |
| PHYS64 20건 | 기존 149 payload/20 성공/18 extended 검증을 재사용; 재실행 0 |
| 기존 PHYS66 pilot/smoke | 저장된 결과 사용; 재실행 0 |

새 테스트는 총 71개이고 회수 통합 회귀 57개와 합쳐 실제 focused PASS는 128개다.
과거 175개 회귀를 이번에 다시 수행한 것으로 세지 않는다. 정확한 요청·코드·출력
해시, 실행시간과 실패 기록은 각 결과 디렉터리에 있다.

완료된 pilot의 complex128 원소를 exact binary64 유리수로 읽어 새 포함 구간과
비교했다. 저장된 그 D1 값의 실제 절대오차는 1.514e-36보다 크고
1.516e-36 a0^-1보다 작다. 이것은 그 한 결과의 총 오차에 대한 인증이며,
이전 pipeline의 각 오차원인을 분해한 추정이 아니다.

L64,Q128에서 기존 f64 sampling Gram의 측정 defect는 m0에서 약 9.088e-12다.
이 진단값은 엄격한 오차 상한이 아니다. 매우 작은 exact-Gauss truncation을
f64 행렬의 전체 오차로 쓰는 해석은 이 사실만으로도 정당화되지 않는다.

## NCP에 전달할 완성된 작업

`WU088_HH_PHYS66_LONGTAIL_RUNNER_20261019.zip`의 SHA256은
`34a59dfe3158c454811ed6e6f47c82357e502ef8cdef9ee5f14640b37f73a835`다.
기존 실행 코드, 원본 NPZ, 최신 bound proof, dependencies, exact manifest와
요청 여섯 개를 포함한다. L28/64 × T55/65/75, m0, join39, orders3,
nodes128, rtol2e-11, max_step0.25로 고정한다. 보수적 전달 명령은
worker1, BLAS1, worker VM4GiB, case timeout900s, resume다.

이 profile은 완료된 PHYS64 20건이나 기존 smoke를 호출하지 않는다. 유효한
새 longtail 성공 영수증이 생기면 source/code/runtime/request fingerprint와
payload hash를 확인하여 재사용한다. NCP에 solver 설계를 넘기는 작업은 없다.
원격 전달·실행 여부는 소스 준비 완료와 분리해 실제 영수증으로만 갱신한다.

## 남은 과학과 실제 단계별 상태

`NEXT_DAG.json`은 해석적 유도, 코드, 검증, 과학 실행, 원격 실행, Git 게시와
백업을 분리한다. 현재 단일 D1 인증을 다음 계산의 기준값으로 재사용한다.
다음 좁은 구현 의무는 m0 finite-L 블록의 validated D1 radial profiles와
모든 내부 j를 포함한 D2(21,20)의 수치 포함이다. 기존 비인증 D2/D3 수치를
자동으로 인증으로 승격하지 않는다.

finite-L 바깥 angular response, 원래 source-driven xi=Fy-phi, 원점의 regular
해와 incoming adjoint의 결합, sigma(E), Maxwellian k_HH(T)는 열린 과학 의무다.
PHYS63의 all-angular 질적 존재는 확보 상태로 유지한다. 해당 열린 노드들을
일반적인 불가능 정리로 바꾸지 않으며 새로운 strong no-go를 주장하지 않는다.
HH_R10=OFF다. 게시·백업 성공 여부와 정확한 commit/tree/제공자 식별자는
`publication/`의 후속 영수증이 권위다.
