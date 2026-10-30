# WU088_HH R33 | PR #172 다음 스레드 Handoff

2026-10-30 KST. 본 문서는 R33의 원본 과학 산출물과 별도 종료 검증을 연결한다. GitHub의 현재 HEAD는 언제나 PR #172에서 다시 읽어라. 이 문서 작성 직전의 확인된 과학 HEAD는 `a441fa12d84d599620c3ffb251e462b137543631`이다.

## 실행 계약

```text
$physmath-research-loop $scispace $exa $wolfram
PROJECT=cosmosapjw-quantum/WU088_HH
CURRENT_PR=172
CURRENT_BRANCH=research/wu-hd5-cmb-chemistry-r33-20261030
CURRENT_HEAD=READ_LIVE_PR_HEAD_FIRST
SCIENTIFIC_HEAD_BEFORE_HANDOFF=a441fa12d84d599620c3ffb251e462b137543631
PARENT_PR=171
IMMUTABLE_PARENT_HEAD=320b3a7252b0bb9fe8b3cbdb40f816545a33bed1
CURRENT_UNIT=WU_HD_CMB5_CHEMISTRY_COMPETITION_R33
NEXT_UNIT=WU_HD_EMAA_171x25_PRIMARY_RADEX_CROSSWALK
AUTO_NEXT_NODE=false

CANONICAL_DAG=34/49_UNCHANGED
R33_AUXILIARY_PHYSICS=1/1_SCOPED
SCOPED_STAGES=18/20
R6_DISTINCT_AUTHOR=NOT_RUN
C9_DISTINCT_AUTHOR=NOT_RUN
NATIVE_SUBAGENT=NOT_EXPOSED

FULL_SOURCE_ZIP=WU_R33_SOURCE_ORIGINAL_20261030.zip
SOURCE_BYTES=6324203
SOURCE_SHA256=8036d1d4cae599a1dc113612e67146fa8b822224b074f827ae2c0d9684e7a362
LIBRARY_PATH=/WU088_HH/R33_HD5_CMB_CHEMISTRY_20261030/
SOURCE_MANIFEST=79/79_PASS
SOURCE_ZIP_CRC=PASS
REMOTE_FULL_BACKUP=25/25_SHA256_CRC_PASS

PES_NATIVE_THRESHOLD=NULL
PHYSICAL_Q=NULL
EMAA_171x25_ASCII=NOT_ACQUIRED
CDMS2011_V2_FIT_COVARIANCE=NOT_ACQUIRED
OWNER_ACK=NOT_OBTAINED
HH_R10=OFF
FULL_A=NULL
L4=false
PRODUCTION=NOT_ISSUED
NO_MAIN_MERGE=true
NO_FOREIGN_REPO_MUTATION=true
```

## 실제 물리와 검산

R29/R30 원본: GL2022 computed SQM에서 (v=0,J=0..4) reactive 350 cells + inelastic downward 70 cells, REC161의 전사된 Einstein A, REC164 Sung fitted line centers. 고정된 `Tgas`, `n(H+)`, 외부 Planck `T_CMB=2.7255(1+z)` 아래 5준위 HD의 first-chemistry absorption Markov 모형을 구성한다. `OFF`는 외부 복사장이 없는 제한 모형으로 물리적 적색편이 -1이 아니다.

관측량: 1,470 조건부 물리 사례, 5,880개의 4개 HD 회전선별 spontaneous/stimulated/absorption 기록, 14,700개 H2(v'=0,J'=0..9) 생성물 분기, 735개 동일 양성자 밀도 정책 비교, 210개 복사 균형 탐색에서 163개 제한 구간 0..300 내부 부호 교차. 105 K, 초기 J2, spin effective, n(H+)=3954.4181821071797 cm^-3에서 z_balance=38.19417624108174, T_CMB=106.82372734506828 K. 외부 복사장 OFF 기준 순복사 에너지 +2.5806029252187536e-21 J/초기 HD, z100 -1.0246306136451205e-20 J/초기 HD. 물리적 cosmic transfer, net volumetric gas heating, full-H/D chemistry나 Q 확보 결과가 아니다.

검증: 원본 SOURCE ZIP SHA256 8036..., 전체 manifest 79/79, ZIP CRC, 포함된 R32 원본 SHA256 01482... 동일. 새 깨끗한 추출 경로에서 Python unittest 17/17 normal, 17/17 `-O`, compileall, 7/7 계산 결과물 SHA256 재생성 일치. 동일 작성자의 별도 mpmath85 계산 420 cases / 2,100 metrics, max scaled delta 1.2439228792274382e-12. Git 원본 핵심 13개 blob SHA 확인. Library 원본 SOURCE 1개+단계 ZIP 20개+phase ZIP 4개, 재다운로드 25/25 SHA256/CRC 검증. 서로 다른 작성자의 R6/C9는 수행되지 않았다.

## 재현 명령 및 알려진 실행환경 차이

```bash
unzip -q WU_R33_SOURCE_ORIGINAL_20261030.zip -d R33_CLEAN
cd R33_CLEAN
PYTHONPATH=. python -m src.cmb5 --out results
PYTHONPATH=. python -m unittest discover -s tests -p test_r33.py -q
PYTHONPATH=. python -O -m unittest discover -s tests -p test_r33.py -q
PYTHONPATH=. python tests/independent_mp85.py
python -m compileall -q src tests
```

불변 SOURCE ZIP 안의 역사적 README는 독립 검산 명령에 `PYTHONPATH=.`를 누락했으며, 깨끗한 환경에서 `ImportError`가 실제 발생했다. 위의 수정 명령과 Git PR #172의 README는 정상 실행된다. 이는 실행환경/호출 문제이며 물리 계산 오류가 아니다. 원본 ZIP은 수정하지 않는다.

## 다음 실행과 stop condition

(1) 공식 EMAA HD–H+ 171 transition×25 temperature RADEX ASCII를 원본 바이트·SHA로 확보하고 quantum-state, partner ID 7, 온도 격자, 단위 및 GL2022와의 수치 사상을 검사한다. GL2022 출처 표시만으로 수치 동치나 독립 검증을 주장하지 않는다.
(2) Velilla2008 native EPAPS Fortran과 same-PES sigma(E), isotope energy zero, 원본 CDMS2011 v2 fit covariance 및 실제 REC/CR chemistry owner ACK는 별도 미충족.
(3) 서로 다른 작성자의 R6/C9 없이는 canonical DAG 승격, full-A, L4, production/merge 불가. 다음 노드는 자동 시작하지 않는다.
