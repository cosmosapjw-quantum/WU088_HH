$physmath-research-loop $scispace $exa $wolfram
WU088_HH 연구를 이어가라.

REPO=cosmosapjw-quantum/WU088_HH
BRANCH=research/wu-hd-source-bound-r18-20261029
DRAFT_PR=155
FROZEN_PARENT_PR154=31d3270ef210ef6659915105358f8fdbf8dae5a0
R18_SCIENCE_COMMIT=4b85a94e136d4f3183cc010908af54f6ff1feca8
LEAF=research/wu_hd_source_bound_r18_20261029
DAG=34/49; ORIGINAL_DAG=33/48; INHERITED_NODE_OBJECTS=48_UNCHANGED
WORKFLOW_R18=20/20_SCOPED; PARENT_R17A_AND_R17B_CLOSURE_OVERLAYS=20/20
MODULE_GIT_BLOB=be2a845263b215b604f255ffe5deabe55be9dd7b
MODULE_SHA256=282ba390836979f051a3e80e502569df8238b2f28c734de9df2da1b88122eb60
SOURCE_PDF_SHA256=a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754
SOURCE_PDF_BYTES=273554

Read current HEAD and REPORT_KO.md, SCIENTIFIC_ADMISSION.json, DAG.json,
NEXT_INPUT_CONTRACT.json, reviews/r18_code/FINAL_C9_REVIEW.json and
delivery/PUBLICATION_INDEX.json first. Keep final metadata HEAD and science commit distinct.

원자료 blocker는 해소됐다. DIGITAL.CSIC 저자 기관 원본 PDF:
https://digital.csic.es/bitstream/10261/305186/2/h_hd_rate_supplementary_material.pdf
Table2/page6 HD(v0,j2)->H2(v0,j1) reactive SQM raw rate10cells:
T_K=15,55,105,255,505,1005,1505,2005,2505,3005
tokens=3.99(14),2.92(11),1.15(10),2.74(10),3.33(10),3.18(10),2.85(10),2.55(10),2.30(10),2.08(10)
a(x)=a*10^(-x)cm3/s; SI factor1e-6.
No interpolation or physical source-error enclosure supplied.
Raw rate에 외부 thermal spin3/4와 p2(T)를 중복 적용하지 마라.
Supplement initialj0..6/mainEq5j0..8 scope차이는 미해결; j7/8=MISSING_NOT_ZERO.
TIQM/EQM와 SQM, inelastic/EMAA/LAMDA와 reactive를 구별하라.

실행은 새 입력·변경이 필요한 범위만 확인하라.
현재 원본·코드 identity가 같으면 primary19/19, independent10/10, CAS15zeros,
distinct-authorC9 final53PASS와 source판독10cells를 재사용한다.
최초 constructor source표지 문제와 mutable-path hash/extractor race, 교정 코드·로그는 보존되어 있다.
공개 API는 검증한 PDF바이트를 stdin으로 추출한다.

정확한 재현이 필요한 clean checkout 명령:
  cd research/wu_hd_source_bound_r18_20261029
  # 원본을 private stageZIP의 ORIGINAL_SOURCES/에서 복구하거나 위기관URL로 취득한 뒤 SHA/크기 확인
  WU_R18_SOURCE_PDF=/absolute/GL2022_CSIC_supplement.pdf python3 tests/test_native_rates.py
  WU_R18_SOURCE_PDF=/absolute/GL2022_CSIC_supplement.pdf python3 tests/independent_reference.py
  python3 figures/render_source.py
필요조건 Python3.10+,Poppler pdftotext,pypdf,Matplotlib.
기존 출력·로그를 보존하는 별도 checkout/output에서 실행하라.

다음 실제 과제는 source-grid native row의 named 소비자 결속이다.
REC현재50/100/200K와 REI300K는 이 원자료grid와 교집합0, REI17state에는HD/H2없다.
기존 소비자에 sourceT/state를 추정해 넣지 말고 repo/path/function/commit,
HD02/H201/H+/D+ stateorder,density,clock,energy convention을 명시하라.
NEXT_INPUT_CONTRACT.json의 고정105K·한 방향4종·외부 등온 bath nominal 반응계가
다음 유한 구현/해석 검증 후보이며 R18에서는 수행하지 않았다.
진행할 경우 새 단위의 유한 예산·범위를 기록해 실제 유도와 구현을 수행하고,
부모의 소진된 suite를 되풀이하지 마라.
명목 source 기반 모델 검증과 source불확실성·wholeA/whole-domain을 포함하는
엄밀한 물리 오차 인증은 각각의 근거로 관리하라.
실제 REC/CR ownerACK 없이 owner소비자를 바꾸거나 HH_R10/production/L4를 켜지 마라.

Root가 독립 researchbranch/draft에 expectedSHA/forcefalse로 게시하고,
매 Ri/Ci 단계의 실제 commit·ZIP·Drive/Dropbox ACK·DAG완료/전체를 기록하라.
다른 repo는 읽기만 하며 mainmerge하지 마라.
현재 runtime은 새 실행 시점에 다시 확인하고 과거 TOOL_NOT_EXPOSED/실패를 상속하지 마라.

