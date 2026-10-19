# PHYS69 — 실제 all-angular D2 인증과 VigilODE Rust 적용

2026-10-19 UTC. 과학적 판정: **PROMOTE_SCOPED**.
Git 게시·백업의 실제 완료 여부는 `publication/`의 후속 영수증으로 확인한다.

## 1. 이번에 실제로 완성한 결과

원래 원자 좌표 B=27, k=7/10, E=49/200 Hartree, R0=7/10 및
화면 퍼텐셜을 유지한 outgoing DtN의 두 번째 Taylor/Born 계수에서,
외부 채널 (ell,p,m)=(21,20,0)에 대해 **모든 중간 angular degree와
모든 r>=27**를 포함하는 다음 인증을 얻었다.

\[
D_{2;21,20}^{m=0}=
(7.01774363281637372857673
+3.20016322230539545153550i)\times10^{-48}+\varepsilon,
\]

\[
\boxed{|\varepsilon|\le1.279825889920\times10^{-64}\ a_0^{-1}.}
\]

이는 원래 절대오차 목표 1e-62를 유지하면서 달성한 결과다. 위 반경은
표시한 유한 소수 중심의 반올림까지 포함한 위쪽 endpoint다. 정확한
dyadic/rational 중심·각 오차·표시 오차는
`all_angular/CERTIFICATE.json`에 있다. SHA256:
`965dc9e3d4a1b40fd7e379629f13480c5a7f30b382aa5b240fd7663b56ae9e29`.

여기서 D2=Z''(0)/2이며 Z_lambda-Z0=lambda D1+lambda^2 D2+...이다.
이는 실제 all-angular 경계 연산자의 계수다. 전체 lambda=1 비선형
응답, 원래 source-driven xi와 반응률의 완료 여부는 별도 연구 노드다.
PHYS63의 질적 all-angular LAP/Poisson/DtN은 ESTABLISHED_REUSED,
HH_R10은 OFF로 유지한다.

## 2. 연구 전에 회수한 새 결과와 실제 원격

원래 대화의 PR115는 현재 baseline보다 이전이다. 연구 시작 시 실제
WU088_HH 최신 PR118의 metadata HEAD는
`2a79d961388e4fc71cbc0938f012b08af7ecf14e`, tree는
`3255eff8a21ff4b97880e34312de44281988ea23`였다. 부모 science commit은
`489ef7dee76231fcaf3c890d8706a2614ff69fe9`다. 이번 로컬 branch는 이
실제 HEAD에서 만들었다. PHYS66 로컬 snapshot을 원격 descendant로
추정하지 않았다.

| 회수 범위 | 새로 확인한 사실 | 이번 사용 |
|---|---|---|
| WU, BASS_HE, bass_cr, rei_bianchi, REC의 branch 전체 pagination와 최근 갱신 PR 각15개 | branch 수127/83/161/247/126; 관련 새 실행·준비 commit 구분 | `intake/GITHUB_INTAKE.json` |
| Library 최신 목록33개와 WU 검색102개 | 새 WU longtail6/L64 완료 영수증 관찰 안 됨 | 목록 부재를 NCP host의 실행 부재로 해석하지 않음 |
| Drive WU root25개, 22하위폴더47개 항목 및 관련 백업/legacy 목록 | 이전 UNKNOWN이었던 PHYS68 업로드 실제 완료 | bytes를 내려받아 SHA/MD5/size 확인 |
| Dropbox root428개, dossier6페이지3238개 | 현재 WU canonical path 접근 실패 및 일부 검색 truncation | 관찰 범위와 미완전 범위를 그대로 보존 |
| 관련 REI/REC 새 영수증 | REI BR05 16/16, RUN16의 gas-only3 IVP, REC ownerU6 완료 | 실행 관리·오차 판별 방법만 참조 |
| HE29, CR C21G | 실행 준비와 NOT_RUN 구분 | WU 검증으로 전용하지 않음 |

Drive의 PHYS68 source/evidence ZIP은 실제 객체
`19zKus8f9Z8bIOMmkqd_T8P2d2heOZNMn`, 6,546,827 bytes,
SHA256 `9843e924955c9a522921d7b3a297e684ea2305fb7ea40be7bc6df55f7156b483`,
MD5 `72a828fda25653e1367ca439f41d21f5`가 모두 일치했다. 이전 UNKNOWN
영수증을 고쳐 쓰지 않고 이번 확인을 추가했다. 같은 파일을 다시 업로드하지 않는다.

전체 제공자 자료의 무제한 부재 증명은 하지 않았다. Drive의 broader root
1000개 cap, Dropbox의 legacy WU 검색 cap과 현재 경로 접근 제한은
`intake/BACKUP_INTAKE.json`에 명시했다. NCP host 상태는 별도 UNKNOWN이다.

요청된 PHYS66 최종 ZIP `993317b1...`, snapshot `2d08f8da...`는 여전히
**BLOCKED_ARTIFACT_ACCESS_EXACT_FINAL_VERSION**이다. PR117에서 회수·검증된
이전 `84c29de7...` 배포본과 혼동하지 않는다. 현재 PHYS67/68/69의 실제
원격 소스와 검증된 입력으로 이번 연구를 진행했으며 가짜 복원은 없다.

## 3. 새 이론: growing-mode Coulomb 경계와 angular 합

모든 정수 j>=20, 27<=r<=t에 대해

\[
|H_j^+(t)/H_j^+(r)|\le (800/189)(j+1)
\]

를 증명했다. a_j=(j-1)/k, R_j=(j+1)/k에서 정확한 nu 부호를 확인하고,
허용영역의 energy identity, 짧은 turning 구간의 logarithmic norm,
Wronskian Gram determinant1, forbidden 영역의 양의 backward transfer를
연결했다. 전이 지수는 모든 j에서 41/20 이하이고 exp(41/20)<8을
정확한 유리수 Taylor remainder로 확인했다. 표본 j의 계산으로 무한
angular 범위를 대신하지 않았다.

원래 S=V/2에 대해 PHYS67의 E10 analytic bound M=1/(4*10^19)를
재사용했다. degree N의 angular polynomial은 ell을 최대 N만 바꾸므로
N=j-ell-1을 택하면 comparison polynomial의 행렬 원소가 정확히 0이다.
따라서 모든 허용된 signed m에서

\[
|V^m_{\ell j}(r)|\le(4M/9)10^{\ell+1-j}e^{-2(r-27)}.
\]

두 q primitive의 정확한 Green 표현에서 각 중간 j의 절대 기여는
Gamma_ext C_j^2 v_lj v_pj/16 이하가 된다. 외부21/20에 대한
Gamma_ext=5929는 기존 PHYS68의 실제 인증서로 재사용한다. x=1/100에서
sum_{j>L}(j+1)^2 x^j를 닫힌 유리식으로 합하여

\[
\mathcal A_{21,20,L}=
\frac{5929}{16}\left(\frac{800}{189}\right)^2
\left(\frac{4M}{9}\right)^2 10^{43}S_L(1/100)
\]

를 얻었다. L35의 경계는1.134074004678017e-62, L36은
1.196186052654912e-64로, 기존 L28에 **j29..36만** 추가하면 목표에
도달한다는 계산 결정을 직접 지지한다. 모든 bound 결정은 Fraction이다.

PHYS63의 weighted LAP 공간에서 P_lambda=(I-lambda R0 V)^-1 P0를
lambda=0 근방에 구성하여 실제 DtN 계수와 이 angular 합을 식별했다.
Green kernel의 derivative jump=-1, boundary derivative=+f를 확인했다.
V는 bounded multiplier이며 compactness를 잘못 부여하지 않았다.
정식 증명과 독립 유도는 `theory/PROOF.md`, `INDEPENDENT_REVIEW.md`에 있다.

## 4. 새 검증 적분과 전체 오차 예산

PHYS68의 완료된 j0..28, 57쌍,76panel 결과를 SHA로 재사용했다. 새
코드는 Coulomb modes {20,21,29,...,36}과 실제 중간 j29..36만 구성한다.
external20/21이 중간 합에 잘못 들어가지 않는다.

새 요청은 T65, h1/4, rho1/2, majorant radius2, Taylor degree96,
512-bit operation/1536-bit coefficient이다. preflight 1.558283초,
첫2panel 2.490811초, resume2개 재사용+새74개 44.967343초였다.
두 실제 child가 exit0이고, **새76개 panel은 각각 한 번만** 계산했다.

새 band의 정확한 midpoint에 대한 결과는 대략

\[
B^T_{29:36}=(8.4094262982766578653
+1.8370926064984768950i)\times10^{-61} a_0^{-1},
\]

numerical absolute L1 error는3.164889152292244e-71 이하이다.
새 certificate SHA는
`e123f084bea390a25162826f306c115d683b7c9fd3157b15967c88814787d0c8`.
검증은 76payload 해시,1216경계 포함관계,760양의 zero-free gate 및
전체 increment의 정확한 합 포함관계를 확인했다. 저장값 검증에서
특수함수·radial 적분 재실행은0이었다.

| 오차 성분 | 크기의 위쪽 표시, a0^-1 | 합성 의미 |
|---|---:|---|
| 기존 L28 numerical | 8.228101e-67 | 기존 full-radial total을 다시 쓰지 않음 |
| 새 j29..36 numerical | 3.164890e-71 | Coulomb/각도계수/Taylor적분/Arb roundoff 포함 |
| 공통 L36 radial cutoff | 7.541139e-66 | PR115 Gamma64/T65 beta2를 전체 합에 한 번 |
| 모든 j>36, 전체 반경 angular | 1.196187e-64 | 새 이론의 정확 유리수 사용 |
| midpoint 합산 | 0 | 두 dyadic 중심을 Fraction으로 더함 |
| 최종 표시 반올림 | certificate의 exact 항목 | 실제 finite-decimal 중심과의 L1 차이 추가 |
| 최종 표시 중심의 전체 반경 | **1.279825889920e-64** | 원래1e-62 목표 PASS |

수치 integrator는 수정하지 않은 PHYS68의 Coulomb Taylor disk,
정확한 m0 angular moment 감소식, reciprocal zero-free gate, Cauchy
remainder 및 outward Arb 산술을 사용한다. native tolerance가 이
인증 오차의 대용으로 사용되지 않았다.

## 5. VigilODE 조사와 Rust에 실제 적용한 부분

VigilODE 실제 source pin은
`a21d573980f66fe02891bd216153443b5352f921`, benchmark PR71 HEAD는
`fa07baf27a37674848d963e30e010d54e4af3f33`이다. 과거 main을 최신
solver로 착각하지 않았다. 저장 CT2700행의 실제 측정 commit
`8a8bd409...`에서 source pin까지 Rust 수정이0임을 확인했다.
백업 CSV와 Git CSV의 SHA가 같았고, 새 VODE/Diffsol 비교 ZIP의
10payload도 검증했다. 기존 benchmark는 재실행하지 않았다.

CSV의2639 solver success와2329 `R_up<=1`은 다른 판정이었다.
이를 반영해 HH 클라이언트는 종점에 직접 착지하고, 두 반환 시각과
모든 상태 차원을 검사하며 실제 인증값과 비교한다. 서로 다른
호스트·오차의 속도 비율을 과학적 성능 순위로 쓰지 않았다.

새 standalone Rust crate는 VigilODE의 matrix-free RODAS5P U-form,
GMRES-into와 재사용 LS workspace, PI controller를 호출한다.
`num-complex=0.4.6`, `gauss-quad=0.3.2`를 실제 적용하고 Cargo.lock을
고정했다. flint-sys/rug/Diffsol/scirs2-special도 공식 자료에서 조사했지만
이미 검증된 Arb 경로를 근거 없이 교체하지 않았다. 자세한 채택 이유와
원전은 `vigilode/THEORY_AND_REUSE_KO.md`에 있다.

tau=65-r, q 배율2^80, D2 배율2^160을 정확히 사용한다. 해석적 JVP와
고정 상태의 explicit time partial을 구현했다. 원래 작은 D2가 scalar
atol 아래에서 사라지는 문제를 scale로 해결하지만, WRMS tolerance를
전체 구간 참오차 보증으로 해석하지 않는다.

Rust1.94.1로 실제 컴파일·실행했다. 첫 두 build는 공유 디스크 ENOSPC로
실패했고 그때 물리 적분/Rust test 실행은0이었다. 실패를 보존하고
재현 가능한 자체 cache/중복 공간을 정리해 기존 build를 이어 완료했다.

| 새 L28 요청 | accepted/rejected | 실제 적분 시간 | 저장점 상대 참오차 상한 |
|---|---:|---:|---:|
| rtol1e-10,scaled atol1e-12 | 883/0 | 4.312258초 | 4.755593436e-11 |
| rtol1e-12,scaled atol1e-14 | 2277/0 | 10.309392초 | 3.775319802e-13 |

두 저장점의 참오차는 기존 SHA-pinned PHYS68 certificate와 exact
Fraction/isqrt 후처리로 제한했다. tolerance100배 강화에서 약126배
오차 감소를 관찰했다. completed resume2건에서 원래 payload SHA가
동일하고 새 적분0이었다. L64 native 요청은 별도 NOT_RUN이다.

## 6. 테스트·독립 검토·수정의 실제 상태

새 고유 테스트는 **Python137개+Rust7개=144개 PASS**다.
같은 전체 suite를 마감용으로 다시 돌리지 않았다.

| 대상 | 실제 고유 PASS |
|---|---:|
| all-j/정확 angular 경계 | 36 |
| exact JSON parser 결함에 대한 추가 경계 검사 | 23 |
| 새 band 코어/child/resume 계약 | 36 |
| VigilODE wrapper | 25 |
| exact all-angular 합성 | 14 |
| 상속 numerical engine 연결 | 3 |
| Rust RHS/JVP/time partial/단위/각도 커널 | 7 |

두 Python 시험의 fixture 오류는 실패 기록을 남기고 각각 그 한 시험만
수정 검증했다. 구현의 exact parser가 bool/float를 int로 절삭하던
문제는 독립 검토에서 찾아 새23개 검사로 닫았다. 원래 고정 산출물
수치에는 영향이 없었다. 실제 arithmetic producer 이후에는 기존
REQUEST.binding을 SHA-pinned PHYS68 fingerprint에 연결하는 guard를
추가해 새3개 검사로 확인했다. 실제 producer source539891add...와
angular producer8e60a031...은 각 `producer_source/`에 원래 바이트로
보존했다. 완료된 과학 계산과 certificate를 다시 쓰지 않았다.

정식 수학, angular 코드, 새 band, exact 합성은 별도 검토자에게
원자료와 식을 제공해 검토했다. 판정과 구체적인 지적은 `theory/`의
각 REVIEW.json에 있다. 새 strong no-go를 주장하지 않았고,
구성적 all-j 경계와 실제 유용한 추가 band 계산을 산출했다.

## 7. 게시·백업·다음 실행점

게시 branch는 `research/hh-phys69-angular-tail-vigilode-20261019`,
실제 부모는 PR118 HEAD2a79d961...이다. science commit과 후속
metadata HEAD는 실제 생성 이후 `publication/`에 기록한다.
원래 PHYS65/66 proof, source NPZ와 PHYS68 구현은 보존했다.
AGENTS.md에는 현재 연구 우선순위만 앞에 추가하고 과거 지침을 유지한다.

Git에는 코드·증명·고정 certificate·실행 및 검토 영수증을 게시한다.
새78원본 panel 파일은 SHA256
`538e16bb74ff5305584fbe2d42491dda55fdffdde536f9276e038bc48da561f0`인
`PHYS69_BAND_PAYLOADS_20261019.zip`에 모두 보존한다. 2,021,962bytes,
CRC 및78member SHA를 확인했고 source/evidence 배포 ZIP에 넣는다.
완료본은 읽기 검증만 사용한다. band `--run --resume --max-new-panels 0`도
certificate 메타데이터를 다시 쓰므로 완료 디렉터리에 실행하지 않는다.

NCP에는 완성된 PHYS66 longtail6, PHYS68 validated L64,
PHYS69 VigilODE L64 실행기와 고정 요청을 전달한다. 먼저 host/백업의
실행 중·완료 영수증을 확인한다. 이 세 campaign은 이번 all-angular
D2 entry의 완료를 되돌리는 선행조건이 아니다. NCP에 solver 설계를
남기지 않았다. 복사 가능한 실행/반환 계약은 CODEX_HANDOFF_PROMPT.md에,
새 대화 시작점은 NEW_THREAD_HANDOFF.md에 있다.

다음 이론 단위는 **PHYS70: 고정 외부21/20,m0의 all-angular D3 또는
그 이상의 잔차를 닫는 구체적 가중 angular convolution 추정**이다.
이번 C_j가 j와 함께 증가한다는 사실을 보존하고 uniform Gamma_infinity를
가정하지 않는다. 필요한 두 중간 지수의 절대합/Green 추정을 먼저 유도하고,
기존 D1/D2 profile을 재사용할 부분을 분리한다. 원래 source-driven xi,
origin/incoming adjoint, sigma(E), Maxwellian k_HH(T)는 순서와 의존성을
NEXT_DAG.json에서 각각 유지한다.
