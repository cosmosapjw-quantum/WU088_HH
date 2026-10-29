# WU088_HH R26 | 다음 대화 재개 계약

2026-10-30 KST. 원본 GL2022의 700셀 상태별 SQM 충돌 반응률과 두 HD 회전상태를 공유하는 H+ 유한 화학 예의 *제한된 실제 출처 기반* 검증을 완료한 인계서. 이 문서는 원본 출처의 물리적 열 방출 Q를 발급하지 않는다.

## 1. 정확한 기준점과 소유권

```
$physmath-research-loop $scispace $exa $wolfram
PROJECT=cosmosapjw-quantum/WU088_HH
PR_PARENT=164
PR_PARENT_HEAD=24302ab37ecc3b1220fb90a705ed375fe431b54e
R26_BRANCH=research/wu-hd-700cell-spin-chemistry-r26-20261030
R26_PR=READ_DRAFT_PR_AT_LIVE_GITHUB
R22_SIBLING_PR=160
R22_SIBLING_HEAD=9db6f91debf54af1cc129538cfd6f6a716a78a56
SIBLING_MERGE=false
CANONICAL_DAG=34/49_UNCHANGED
R26_SCOPED_SCIENCE_DATA=1/1
R23_HISTORICAL_WORKFLOW=18/20
R6_DISTINCT_AUTHOR=NOT_RUN
C9_DISTINCT_AUTHOR=NOT_RUN
NATIVE_SUBAGENT=NOT_EXPOSED
GL2022_PES_NATIVE_THRESHOLD=NULL
PHYSICAL_Q=NULL
PHYSICAL_BATH=NULL
REVERSE_RATE=NULL
SOURCE_RATE_UNCERTAINTY=NULL
OWNER_ACK=NOT_OBTAINED
HH_R10=OFF
L4=false
FULL_A=NULL
PRODUCTION=NOT_ISSUED
```

먼저 실제 GitHub Draft PR HEAD와 backup 원본 SHA-256을 검증하고 해당 HEAD에 고정해 읽어라. Parent, sibling, main 또는 REC/CR 등 외부 소유자 코드를 병합/수정하지 마라.

## 2. 새로 확인한 원본 물리 데이터

GL2022: González-Lezana/Hily-Blant/Faure, JCP 157,214302 (2022), DOI `10.1063/5.0128598`. 원본 supplementary PDF 273554 bytes SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`.
Tables 1–10에 10개 온도 T=[15,55,105,255,505,1005,1505,2005,2505,3005] K, H+ + HD(v0,J0..6) -> D+ + H2(v'0,J'0..9), 700 SQM 계산 rate 인쇄 셀. 양수 678, `0.00(00)` 등 물리적 0이라고 인증할 수 없는 인쇄 영 22. 양의 값 21개 의심 flag, 특히 Table1/Table2 원본 J5 완전복제 20과 Table8 J3 J'7 2505K `6.72(16)` 1. 원본 인쇄 문자열을 임의 보정하지 마라. 원문 독립 텍스트 엔진 700/700 동치. R25 J2 subset 100/100 원본 byte-token 동치.
본문 Eq(5)의 HD J0..8 전체 열평균은 부록 J0..6 만으로 정확히 복원되지 않는다. Eq(6–7) H2 핵스핀 짝 1/4, 홀 3/4 가중 effective rate를 raw SQM과 독립 옵션으로 보존한다. 실제 rate uncertainty source-qualified가 아니다.

## 3. 새 물리 이론/제한 계산

고정 부피, 외부 온도 구간에서 `p=n_H+`, `y_j=n_HD,J=j`, `z_l=n_H2,J'=l`, `D=n_D+`라 두면 `dy_j/dt=-p K_j y_j`, `dp/dt=-p sum_j K_j y_j`, `dz_l/dt=p sum_j q_jl y_j`, `dD/dt=p sum_j K_j y_j`. `K_j=sum_l q_jl`. H/D nuclear number, charge, particle count conserved. Collision-clock `u=∫p dt` yields exact `y_j=y_j0 exp(-K_j u)` per fixed T segment, scalar quadrature for t, and all species positive. Two temperature vector fields `F_A,F_B` have Lie bracket under `DF_A F_B-DF_B F_A` convention `p*y2*y4*(K_A2*K_B4-K_A4*K_B2)*(0,1,-1)`, Wolfram/SymPy checks. This is not a claim about cosmological history or native PES Q.

Original positive J2 and J4 rate cells only, initial densities p=1.3e6, y2=6e5, y4=4e5 m^-3, 105K and 255K each 5e9 s:
- raw SQM total extent 105→255 K = 933144.0064547455 m^-3, reverse order = 936568.2358469048, difference = -3424.2293921593.
- Eq(6-7) spin-weighted policy total extent 105→255 K = 831246.2991579813 m^-3, reverse order = 836068.6688582008, difference = -4822.3697002195.
These two policies are not statistical uncertainty bands; they are distinct explicit rate choices. No stimulated spin factors beyond Eq(6–7) or unqualified reverse rates.

## 4. Reproduction commands

Extract the immutable `WU_R26_SOURCE_ORIGINAL_20261030.zip`. Under the extracted R26 root:

```
PYTHONPATH=. python -m unittest discover -s tests -p test_r26.py -q
PYTHONPATH=. python -O -m unittest discover -s tests -p test_r26.py -q
python -m compileall -q src tests
python tests/independent_fitz_source.py
python tests/independent_sympy_commutator.py
PYTHONPATH=. python src/native_atlas.py --help
python figures/plot_results.py
```

Check tests 38/38 normal and 38/38 -O, PyMuPDF 700/700 versus `pdftotext -layout` original extraction, source hardcoded hash, valid original state/temperature guard, four coupling ODE cases (SciPy DOP853 versus scalar collision-clock), H/D/charge/particle conservation and source anomalies. Previous first failed P02 precision-context test remains for failure provenance, not a current failure. All figures are source/synthetic diagnostic, not actual thermal histories.

## 5. Next scientific rather than computational objective

First obtain original Velilla et al. 2008 H3+ 1^1A' PES Fortran EPAPS file, exact H+ + HD(0,2) vs D+ + H2(0,1) rovibrational asymptotes, isotope nuclear masses, BO/non-BO ionization correction, energy-zero mapping, native energy-resolved cross sections. Public `H3p-singlet-pot.f` by Aguado et al 2000 is **not** the Velilla2008 source. Reintegrate actual SQM σ(E) versus published k(T) with proper E_total vs entrance-kinetic definition and positive support bound. For the Eq5 thermal rate also obtain source-qualified missing HD J7,J8 channels and their state energies, not guessed extrapolation. Obtain named actual REC/CR four-molecular-species reaction consumer ACK after full read-only dynamic/native call-graph tracing. REC #160 HD spectroscopy rotational source, CR #126 helium allocation and CR historical `HD_CX` atomic charge exchange are **not** molecular exchange owners. Source-qualified Q, reverse, bath, full-A, L4 and production remain held.

Do not replay old full numerical campaigns, promise background computations, or count source-data auxiliary completion as canonical DAG increase. Return original SHA, code commit HEAD, physics status and smallest next proof/measurement source input.
