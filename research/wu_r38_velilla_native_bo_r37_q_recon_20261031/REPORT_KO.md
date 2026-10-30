# WU088_HH R38 원본 Velilla BO/Q 교차검증 보고

**진행 구분:** 이미 보존된 두 개의 R38 원본 과학 실험을 보존하고 결합하는 bounded reconciliation. 새로운 3체 scattering 연구를 시작한 것이 아니다.

**Parent PR:** WU #176, 보호할 HEAD `341b3363c68b35defc78987a55f8a2f6c8216866`. **Canonical DAG 34/49 unchanged (+0)**. R38 auxiliary source-scoped 1/1, R/C scoped 18/20, distinct-author R6/C9 NOT_RUN.

원본 자료:
- EPUB/EPAPS AIP 원본 `084307_1_supplements.zip` 20,445바이트 SHA `a781d3b6f7d3cdffc210f2e8abd436e7378eb3716af80eb96b102a542eaba304`, `h3plus.f` 109,636바이트 SHA `8dbf8b7e3852d02504ba92317f79593051d689f1357263ac0891a3a24084ed8c`.
- 기존 보존 R38 spectral ZIP 2026-10-31 SHA `94a70bae5d7e2639b9ca99cb4433567e52f90baa01d4c9ad1eab354eef545be4` (18,591,227 B).
- 기존 보존 R38 FD/chemistry ZIP 2026-10-30 SHA `0b259c1ff0e619b56cf712e6729c970b1531daba2c4278f2455526e09a5a61b0` (20,118,529 B).

## 실제 산출
- 190 original-source HD/H₂ 점근 채널의 spectral–FD 에너지 대조. \(\max|\delta\Delta E|/k_B=0.3287380717733\,\mathrm K\), 고진동/고회전 채널에서 주로 발생. 흡열·발열 분류 변경 0/190.
- 바닥상태 흡열 문턱: spectral 416.2319214315 K, FD 416.2319911104 K (차이 −0.00006968 K). 이는 모델 정확도 보증이 아니라 두 수치 구현 차이.
- R37 실제 화학반응 첫 이탈 확률 19,200 H₂ 생성물 분기 × spectral BO Q의 새로운 source-preserving 매핑 19,200행, 1,920 조건별 에너지 요약. 반응 확률·전이율은 바꾸지 않았음.
- 조건부 \(Q/k_B\) 계산 격자 범위: −1999.00114 K에서 +847.36770 K. FD의 동일한 조건부 Q와 차이: −0.00154510 K에서 +0.00220387 K.
- 대표 Tgas=105K, n(H+)=1000cm^-3, z_boundary=300, GL spin rule, 초기 J2: Pchem(first-exit)=0.19386816454744, 새 \(\langle Q\rangle_{\rm chem}/k_B=-229.87936644715\) K. 이 경우 P_endothermic_given_reaction=1.
- 초기 J=0,1,2에서는 해당 제한된 화학반응 분기 전체가 흡열; J=3,4에는 발열 가능한 H₂ 최종 상태가 존재. 이는 고정 source-grid와 초기 상태에 한정됨.

## 검증
- 원본 Fortran 별도 컴파일 `gfortran -std=legacy -O2 -fPIC -ffixed-line-length-none -shared -llapack -lblas`와 native PES 샘플. 비정삼각형 순열 에너지 차이 8.65e−13 Hartree (원본 좌표·순열 실수 계산 한계).
- 원본 보존 R38 spectral 16/16, FD 15/15 테스트를 이번 세션에서 각각 실행 PASS.
- R38 crosswalk 코딩 테스트 7/7 정상 및 `-O` 7/7 PASS, 별도 70자리 Decimal 검산은 19,200개 source row 전수 대응, 최대 Q roundtrip ~6.81e−36J 및 probability mass discrepancy ~1.21e−16.
- 새 데이터의 clean independent replay는 별도 로그와 file SHA-256으로 판정; 상기 결과는 모두 bounded numeric/implementation scope임.

## Blind referee 핵심 판정
(1) electronic De와 동위원소 BO Q 혼동 금지; (2) spectral/FD 절대 zero energy shift (+1 Hartree) 비교 금지, only differences; (3) source GL rate에 Maxwell tail 재곱 금지; (4) probability weights from R37 are precomputed conditional first-exit, not full fate; (5) PES source compiler warnings preserved, original bytes untouched; (6) full isotope scattering, author-source 50-cell reconciliation, independent distinct-author R6/C9 outstanding.

**HOLD:** `PES_NATIVE_FORTRAN=ACQUIRED`, `PES_BO_DIATOMIC_Q=DERIVED_NUMERICALLY_CHECKED`, `PES_NATIVE_SCATTERING_THRESHOLD=NULL`, `PHYSICAL_Q_FULL=NULL`, `OWNER_ACK=NOT_OBTAINED`, `L4=false`, `PRODUCTION=NOT_ISSUED`, `NO_MAIN_MERGE=true`, `NO_FOREIGN_REPO_MUTATION=true`, `AUTO_NEXT_NODE=false`.
