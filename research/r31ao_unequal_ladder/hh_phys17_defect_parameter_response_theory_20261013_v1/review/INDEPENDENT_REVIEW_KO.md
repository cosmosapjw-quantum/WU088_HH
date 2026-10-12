# PHYS17 독립 심사 — PROMOTE_SCOPED

**판정:** 원 fixed-coefficient source-aligned \(C^2\) family, 하나의 고정 admissible \(\alpha\), 동일 COMMON 및 전역 \((\lambda,b)\in[0,1]^2\)에서 PHYS17의 1차 parameter-response 구성과 실행 결과를 채택한다. 원 source·closure·정규화의 변경은 없으며, 채택을 막는 과학적 오류는 발견되지 않았다.

검토자: /root/hh_phys17_literature_review. 검토 완료일: 2026-10-13 KST. 기계 판독 판정과 정확한 code/result/proof 식별은 INDEPENDENT_REVIEW.json에 고정했다.

## 1. 실제로 확보한 응답

아래 값은 main run02의 256-bit 외향 exact interval을 십진 외향 표기로 옮긴 것이다. \(\lambda,b\)는 무차원 parameter이므로 단위는 K/parameter다.

| 응답 | 검증된 포함 | 부호 |
|---|---:|---|
| \(\partial_\lambda\Delta T\) | \([-1.009599125635\times10^{-8},-8.137506081166\times10^{-9}]\) K | 엄밀히 음수 |
| \(\partial_b\Delta T\) | \([6.776348385589\times10^{-5},7.185335549648\times10^{-5}]\) K | 엄밀히 양수 |

이 값은 실제 root family의 \(g_{1,\theta},g_{2,\theta},g_{F,\theta}\)와 opacity feedback을 포함한다. \(\alpha\)를 고정한 채 두 parameter를 같은 전역 변수로 미분한다. 온도 차이 \(\Delta T=T_2-T_F\)의 정의 및 원 유한 분모 \(\Pi_F\)를 보존했다.

직접 forcing과 state/opacity feedback을 같은 \(J_F\), 같은 \(\Pi_F\), 같은 goal row로 전달한 별도 forcing01도 채택한다.

| parameter | 직접 forcing | state/opacity feedback |
|---|---:|---:|
| \(\lambda\) | \([-8.547862783773,-6.959235163714]\times10^{-9}\) K | \([-1.548117483502,-1.178280571010]\times10^{-9}\) K |
| \(b\) | \([6.784453758953,7.193378236380]\times10^{-5}\) K | \([-8.403008830470,-7.759040903738]\times10^{-8}\) K |

\(\lambda\)의 두 구성은 모두 음수다. \(b\)의 직접 forcing은 양수이고 feedback은 음수다. 각 포함의 합과 main run의 총 응답은 양립한다. \(\lambda\)에서는 그 교차가 \([-1.009598026728\times10^{-8},-8.137515734724\times10^{-9}]\) K로 약간 좁아진다. \(b\)에서는 원 main 구간이 유지된다.

## 2. 유도·원 source·구간 산술의 연결

독립 검토는 다음 순서로 과학적 근거를 연결했다.

1. 원 implicit 식에서 P1/P2를 직접 유도해 \(C^2\) 충분성과 두 feedback 항을 빼는 부호를 확인했다.
2. 원 Rust source의 nonphoto·HH·photon·팽창 분리, captured \(\chi_H\), \(f=n_{\rm He,stored}/n_H\)를 확인했다.
3. 원 nonphoto Jet의 \(U=(F_w+\chi_HF_x)/(ne)\)와 고정 온도 방향을 사용한 He 소거 및 \(D\xi[v]\) 항을 검토했다.
4. 같은 stage increment derivative를 gas movement와 photon opacity difference에 공유하는지, density pullback의 작은 계수를 유지하는지 확인했다.
5. 원 residual Hessian과 mixed derivative slot 96개를 직접 대조하고 같은 \(C,B,q,S\)를 확인했다.
6. 후보의 Gaussian elimination과 다른 exact determinant/Cramer 계산으로 응답 포함을 독립 재구성했다.
7. 같은 유한 온도 분모·goal row와 geometry 항을 확인하고 P4 구간, forcing 분해, Neumann 오차를 대조했다.

상세 수식과 원 source 식별은 SOURCE_AND_DERIVATION_REVIEW_KO.md에 있다. main 입력 13개와 PHYS16 다음 연구 계약의 입력 binding 14개가 원 SHA256과 일치한다.

## 3. 독립 산술의 실제 실행

최종 검토 프로그램은 independent_arithmetic_review_v2.py다. 후보 프로그램 및 PHYS14 helper를 import하지 않는다. 모든 중간 연산은 Fraction endpoint 구간이고, 4차 determinant의 24항 Leibniz 식과 Cramer 법칙을 쓴다. 원 physical source 호출, 새 root solve, history replay는 모두 0회다.

| 실행 | 결과 | 검토 묶음 | 내부 계산 시간 | 최고 RSS |
|---|---|---:|---:|---:|
| arithmetic01 | 검토기 가정 수정 필요 | 26/29 통과 | 0.2221 s | 27,560 KiB |
| arithmetic02 | PASS | 29/29 통과 | 0.2219 s | 27,580 KiB |

첫 실행의 세 실패는 inherited carry와 \(L_H,a\)에 대해 원 장분모 Fraction과 256-bit 외향 복사본의 정확 동등성을 요구한 검토기 가정에서 발생했다. 후보가 보존해야 하는 것은 원 구간의 포함과 보수적인 상계다. 원소별 확대가 바깥 방향이고 상대 endpoint 확대가 \(2^{-254}\) 이하임을 확인하도록 교정했다. 원 후보 수치나 과학 식은 바꾸지 않았다.

첫 실행의 source, PRE_RUN, RUN, stdout/stderr, FAIL 결과와 수정 실행의 대응 파일을 모두 보존했다. 최종 PASS만 남기기 위해 이전 증거를 지우지 않았다.

29개 최종 묶음에는 490개 photon manual/dual 교차, 8개 RHS 합 교차, 동일 inverse의 sector 전달, P4, 네 개 Neumann Kelvin 상계, 다섯 corollary exact interval 및 원 Wolfram/xAct 출력 검사가 포함된다. 이 숫자는 실제 검사 묶음 수이며, 전체 원 물리계를 29회 새로 실행했다는 의미는 아니다.

## 4. 유한 Neumann 오차

\(m=2\)에서 \(\varepsilon_F=q^3a_\theta\), \(\varepsilon_y=[q^3+L_Ha(1+q+q^2)]a_\theta\)를 검토했다. Jacobian 차이의 Hessian 적분에는 계수 1이 들어가며 \(1/2\)를 넣지 않는다.

| parameter | \(J_F\) 기준 온도 도함수 다항식 오차 상계 | \(J_y\) 기준 상계 |
|---|---:|---:|
| \(\lambda\) | \(4.066246749000\times10^{-20}\) K | \(8.959060026852\times10^{-18}\) K |
| \(b\) | \(7.526159651071\times10^{-16}\) K | \(1.658219981417\times10^{-13}\) K |

이 값은 실제 \(d_\theta\)를 유한 Neumann 다항식으로 대체할 때의 오차 상계다. 기존 구간의 폭 자체를 이 오차와 동일시하지 않는다. 전체 P4 geometry 항은 보존한다.

원 \(a\)의 상계를 256-bit로 바깥 복사한 확대는 약 \(4.94068\times10^{-83}\), 그 사본보다 \(\max_i|d_i|/S_i\)가 더 큰 양은 약 \(2.08036\times10^{-84}\)다. 후자의 정확 외향 구간은 neumann02의 outward_copy_expansion 필드에 있다. 최종 \(a\)는 두 상계를 모두 덮는다.

## 5. Wolfram과 xAct

실제 Wolfram Language evaluator에서 official xAct 1.3.0 archive의 SHA256 확인 후 xTensor 1.3.0 및 xPerm 1.2.4를 사용한 실행을 검토했다. xPerm의 Wolfram Language group backend를 사용했고 external canonicalizer는 사용하지 않았다.

**6개 tensor 항등식과 9개 scalar 묶음의 15개 원소가 모두 exact 0**이었다. tensor dummy-index, P2 cancellation, Hessian 대칭, 공통 adjoint, He projector와 derivative, P4, 일반 비가환 2-slot photon 항등식의 값·미분, \(m=2\) Neumann 항등식을 확인한다. 실제 raw 출력은 Completed이고 message list는 비어 있다.

이 공식 계산의 범위는 선언된 수학식의 대수다. 물리 source binding, 원 35-slot 포함, 원 \(C^2\) family와 \(q<1\)은 이 심사의 별도 source·산술 근거로 확인했다.

## 6. 문헌 대조와 범위

SciSpace 검색 1회에서 10개 문헌을 반환받았고, Exa 검색 4회에서 중복을 포함하여 총 20개 후보를 요청했다. Exa fetch 4회와 원 scan 읽기를 수행했다. 네 개 핵심 원전은 Neumaier 1989, Rump 1990, Goldsztejn 2008, Margossian–Betancourt 2022이며, PHYS16의 Rump 2010 및 Rannacher 2003 대조는 재사용했다.

문헌 조건을 현재 \(C^2\) implicit family와 맞췄다. 독립 tolerance family에 대한 inner-hull 정리를 현재 correlated common-parameter family의 날카로움 주장에 가져오지 않는다. Margossian–Betancourt의 일반적인 “if and only if” 설명은 필요한 충분조건 방향으로 한정하여 인용한다. 원문 위치·DOI·URL 및 이 교정의 이유는 literature/LITERATURE_REVIEW_KO.md에 있다.

원고 §9.1의 모서리 극값, 유한 parameter 변화, 국소 등결함 곡선과 continuation 조건, 네 모서리 혼합 contrast 상계도 채택한다. 마지막 상계
\[
|\mathcal I|\le1.958485175177039\times10^{-9}\ {\rm K}
\]
는 이번 \(\lambda\) 도함수 폭과 기본정리의 결과다. mixed derivative의 부호와 더 정밀한 interaction 포함은 후속 연구 항목이다. 이론 §6.2의 추가 photon-ledger derivative는 유도되어 있으나 모든 추가 endpoint photon 관측량을 이번 실행에서 수치 평가한 것은 아니다.

## 7. 채택된 파일의 식별

| 파일 | SHA256 |
|---|---|
| theory/PARAMETER_RESPONSE_THEOREM_KO.md | f0b6891420784239ef4e87793dde4ca425e52a9b320b0d1f4ce7a07f8c546b9b |
| run02 PARAMETER_RESPONSE_RESULTS.json | fd4fc0fe6bcf035496270bb92f0c56c44ca43d16694cb40296087569a305e7c0 |
| forcing01 FORCING_FEEDBACK_RESULTS.json | 1eef9f7011f5897777075796393f6f911b34f7b13c0ac8345c9966e71b257a90 |
| neumann02 DERIVATIVE_NEUMANN_RESULTS.json | c22604e4c78d96072e536ccf71b7d22c1079bb5776eac0c8134acf223a5b8be6 |
| Wolfram parameter_response_checks.wl | b33af2650c0a3e229166f5b2a0ec7c1a86beb8c47cb19df563c9d3cbc2acbb72 |
| WOLFRAM_XACT_EXECUTION.json | 7c8b1df7efae7d60dc943da44dceddeda85dbfbe36afca9635bf840926bc63f9 |
| independent_arithmetic_review_v2.py | c0e79879cabdd30a1e7c13f84cd4f2b24aecb44e3b78d52c718d5cad5294348f |
| arithmetic02 INDEPENDENT_ARITHMETIC_RESULTS.json | dfed22bcda2e45a4ccd7861b7454ea7535751fb75d1d1e32be2f61d72a66f6c2 |

실행 source·PRE_RUN·RUN을 포함한 28개 binding은 INDEPENDENT_REVIEW.json에 있다. 원 raw candidate의 CANDIDATE_COMPUTED 상태는 보존하고, 이 독립 판정에서 해당 범위의 채택을 기록한다. 새 strong no-go, 원 물리 source 밖의 일반화, 다른 DAG branch의 완료 주장은 추가하지 않는다.
