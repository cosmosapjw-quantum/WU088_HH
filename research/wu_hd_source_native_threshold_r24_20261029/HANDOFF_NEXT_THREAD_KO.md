# WU088_HH R24 → 다음 연구 스레드 (사전 출판 계약)

```text
$physmath-research-loop $scispace $exa $wolfram
PROJECT=cosmosapjw-quantum/WU088_HH
CURRENT_UNIT=WU_HD_SOURCE_NATIVE_MAXWELL_SUPPORT_R24
PARENT_R23_DRAFT_PR=162
PARENT_R23_HEAD=2f214319ca8600475b1d4e85d1ca21a0249136a8
R22_PR160_READONLY_HEAD=9db6f91debf54af1cc129538cfd6f6a716a78a56
R21_ORIGINAL_PDF_SHA256=a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754
R24_DRAFT_PR=CHECK_POST_PUBLICATION_RECEIPT
R24_FINAL_HEAD=CHECK_LIVE_PR_AND_FINAL_COMMENT
CANONICAL_WU_DAG=34/49_UNCHANGED
SCOPED_WORKFLOW=18/20
R6_DISTINCT_AUTHOR=NOT_RUN
C9_DISTINCT_AUTHOR=NOT_RUN
PHYSICAL_Q=NULL
BATH_HEAT=NULL
SOURCE_UNCERTAINTY=NULL
REVERSE_RATE=NULL
OWNER_ACK=NULL
HH_R10=OFF
PRODUCTION=NOT_ISSUED
L4=false
```

## 읽기 순서

`research/wu_hd_source_native_threshold_r24_20261029/{THEORY_KO.md,REPORT_KO.md,DAG_DELTA.json,CROSS_REPO_PINNED.json,README_REPLAY.md,sources/,src/,tests/,results/,figures/,stages/,delivery/}`. 이전 R21/R23 원본 ZIP SHA와 GL2022 보충 PDF SHA, Git blob, GL2022 Table 2 열 개 온도 노드를 재확인한다. R22 형제 PR160을 병합하지 않는다. 원본 source archive에는 동시대 출력과 20개 단계 기록이 있으나 Git/Dropbox/Drive publication ACK는 별도 후행 receipt에 둔다.

## 주요 새 결과

같은 입사 HD(v0,J2), 단일 온도 비의존 양의 단면적 σ(E), **입사 충돌 상대 에너지 E≥0**, 문턱 Δ>0, Maxwell thermal convolution을 가정할 때 F(β)=k(T)β^(-3/2)/C는 Eσ(E)의 양의 Laplace transform이다. 따라서 15/55K Table 2 반응률로부터 **Δ ≤ 15.18630382175889727368776395345 meV** (인쇄 mantissa ±0.005만 반영한 최선 상한 **15.19157320477320978 meV**)라는 정확한 필요조건을 유도했다. Cross-model BO2019 j2→j0(3.4meV)+외부 H₂ 회전(14.6905meV) 진단 18.0905meV와 외부 R23 spectroscopy 20.9500meV 후보는 이 model class에서 각각 Laplace 저온 비 제약을 5.12445518배, 25.60830893배 초과한다. 이는 **원본 산란 구현의 원인/오류 인증이 아니며 PES-native 문턱을 구한 것이 아니다**.

이전 단순 p0 Arrhenius secant는 -12.3855~26.0662 meV로 서로 달라 하나의 p0 활성화 장벽으로 해석할 수 없다. Velilla2008 37,170 cm^-1은 H3+ PES 최저점 대비 전자 해리 geometry이며 isotope molecular state Q가 아니다. Lepers2019의 3.4 meV는 BO/TIQM j2→j0 (다른 제품 상태), 39.5meV는 ground→ground, GL2022 2022 Table2는 j2→j1. 서로 혼동하지 않는다.

## 실행·검증·보존

Python 신규 42/42 normal, 42/42 `-O`, C++20 독립 long-double, mpmath100, Wolfram 수치 일치. 원본 R18 parser+R21 PDF 파일 SHA 및 ten native printed nodes 직접 재현. 세 synthetic diagnostic plots 렌더링·시각검수. Native separate-author R6/C9 NOT_RUN. 별도 repo 수정·main merge 금지, stage Git commit/Library original ZIP/Dropbox content hash와 Google Drive 실제 ACK는 후행 receipt대로 보고한다. 다른 소유자의 비반응성 REC HD/LAMDA, CR He, REI H/He/Li, BASS geometry, HE deuteron은 바로 target 4-species owner에 연결하지 않는다.

## 다음 정확한 물리 노드

`WU_HD_GL2022_NATIVE_CHANNEL_ENERGY_AND_QUADRATURE_R25`: GL2022 원본 SQM 계산의 충돌 E 정의, channel HD(0,2)와 H2(0,1)의 same-PES E_in/E_out, Velilla 2008 raw potential/mass/isotope IP, **원본 k15/k55 cross-section raw energy quadrature** 획득·복원. 실제 소스 영점과 15/55 K rate를 재계산하여 conditional positivity conflict의 원인을 source interpretation / numerical quadrature / physical correction / other로 구분한다. 외부 분광값을 PES-native threshold로 자동 승격하지 않는다. 병렬 REC/CR owner 실제 4-species source RHS/clock/density call graph와 **명시적 owner ACK**를 확인하기 전 foreign mutation 금지. Reverse, rate uncertainty, real bath, full-A, production, L4는 별도 미완료.
