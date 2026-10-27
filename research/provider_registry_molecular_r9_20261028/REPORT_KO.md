# WU088_HH R9 연구 보고서

**조건부 causal cell resolvent의 일반 증명과 실행 가능한 구현을 완성하고 독립 검증을 마쳤다. 과학 DAG는19/34, 이론 R1–R10 및 코딩 C1–C10 산출물은20/20이다.** 기존32개 노드는 바꾸지 않고 이론·구현2개를 추가 채택했다. 실제 물리 HD consumer, 중앙 DAG 또는 production 승인은 증가시키지 않았다.

새 방법은 같은 시간 셀의 R–E feedback을 양의2×2 역행렬로 풀어 초기 전체 궤도 오차 envelope 없이 순차 상계를 만든다. 저장된 native9 사례의 최종 감소는 R0.000073811913%, E0.005490601414%이며, 상계는 여전히 참조 표본의 약310.954/907.041배다. 구성의 독립성과 수치적 개선 폭을 분리한 결과다.

## 1. 채택 identity와 실제 완료 상태

| 항목 | 현재 근거 |
|---|---|
| 과학 채택 S09 | [f8b4ea63381fcdab91577c31005bc85e66789141](https://github.com/cosmosapjw-quantum/WU088_HH/commit/f8b4ea63381fcdab91577c31005bc85e66789141) |
| 과학 payload | 35files; SHA256 739f4225be52598eb99e90ddfbc6c749390335c90918add47b6ff3d080f6d1c3 |
| Core SHA256 | cc4e31a7dc72ceddb7ebba5f8f6ef64fb2e3325143a6abb9018a6a07c8129e1d |
| Proof SHA256 | b84da224515cf9ab7d9e39c3766332066c348f304bd2e8d63ddec940123c8ea3 |
| Primary |150/150PASS; failures0; exit0; CPU1.162604s |
| Independent reference |438/438PASS;34590component comparisons; failed0; exit0; CPU1.108081s |
| Independent C9 |PASS_SCOPED_FINAL_C9; open material findings0 |
| CAS |7algebra+4control residuals0; positivity1True/3unreduced; qualified corroboration |
| 실행 수 |primary1,reference1,newCAS1; remaining0/0/0 |
| 물리/중앙 |physical delta0; central delta0; HH_R10OFF; productionNOT_ISSUED; L4false |

두 Python child의 전체 OS CPU 합은2.270685s이며 import와 serialization을 포함한다. CAS의 실제 CPU와 전체 역사 CPU는 계측되지 않았으므로 null이다. Global remaining도 null이다. 저장·네트워크·metadata 시간을 과학 CPU로 합산하거나0으로 단정하지 않는다. [채택 원문](https://github.com/cosmosapjw-quantum/WU088_HH/blob/f8b4ea63381fcdab91577c31005bc85e66789141/research/provider_registry_molecular_r9_20261028/SCIENTIFIC_ADMISSION.json) · [최종 C9](https://github.com/cosmosapjw-quantum/WU088_HH/blob/f8b4ea63381fcdab91577c31005bc85e66789141/research/provider_registry_molecular_r9_20261028/reviews/C9_FINAL_REVIEW.json)

## 2. 전수 조사 범위와 종합

R8 종료 source b3ba2e4aff1f237a2835b2f3a1b07de81133e9f7을 baseline으로 삼았다. 중단 전20:31:57–20:32:25UTC census와 복구 후21:00:21–21:00:24UTC census는 접근 가능한51repo/2370branch heads/65pages를 모두 terminal까지 읽었다. 후자는 public35/1887/47pages, private16/483/18pages다. 비공개 상세는 공개하지 않고 집계만 보존했다.

21:44:41–21:44:43UTC에 public 원문을 복구하며35repo/1890heads/47terminalpages를 실제 읽었다. 앞선 public mapping과 비교해 추가3,삭제0,HEAD이동4,불변1883을 확인했다. Private16/483은21:00 관측을 재사용하므로51/2373을 동시점 전체 재조회로 표시하지 않는다. 현재 public raw, exact delta, 그리고 이를 역으로 적용한 이전1887개 branch/head mapping을 보존했다. 이전 mapping 복구는 구조적 identity이며 잃은 원문 직렬화의 byte identity를 주장하지 않는다.

| 조사 대상 | 실제 범위 | 해석 |
|---|---|---|
| 전체 접근 가능 Git 목록 |51repo,2370heads,65pages,51terminal | 모든 branch head 목록; 모든 branch 내용/tag/hidden ref/전체 history를 읽은 것은 아님 |
| 후속 공개 목록 |35repo,1890heads,47pages,35terminal | 새3branch와 관련 이동 HEAD의 실제 원문을 추가 종합 |
| 초기 관련 source |27immutable files,300355bytes,27Git blob matches;7repos의 최신PR35rows | 실제 읽은 내용으로 owner 권한과 입력 범위 판정 |
| Dropbox |dossiers3464rows/6pages terminal;CR205;WU599 | 범위별 목록 관측 |
| Drive |parent1000rows historical partial;CR187;WU631 | 상위 과거 목록의 완전성은 주장하지 않음 |
| 신규 백업 대응 |51pairs=HE18+CR22+WU11 | 두 provider 이름·크기 대응;51개 전체 원본 hash 검증이라는 뜻은 아님 |
| 실제 신규 원본 판독 |HE APERTURE07 25256B, KINEMATIC08 195656B | 원본 SHA 및 의미를 확인; 이전 plot failure 보존 |
| 사용자 첨부 |20files가R7의 size/SHA와 동일;10archives60882members;15PDF 기존 text 재사용 | 새 standalone36page/68721chars 판독 포함, OCR 미수행 |
| 다른 대화 전문 |연결 context unavailable, retrieved0 | 대화 전체 전수 판독을 주장하지 않음 |

Drive의 recent query0이 folder listing16과 충돌한 사실을 기록했고0을 부재 근거로 쓰지 않았다. 파일명에 h2가 들어간 두 archive member는 실제 분자H2가 아니라 우주론 H-prime2 식이었다. Source 조건을 이름만으로 옮기지 않았다.

### 최신 관련 owner 결과

BASS의 atomic-H endpoint, prescribed Bianchi/Thomson clock 결과는 실제 HD/para-H2 density clock가 아니다. 최신 KM2C는13unique tests PASS와 별도6geometry/8optical-depth/8direct/7Volterra 계산을 보고하지만 upper scoped6/15이며 독립 모델 검토는NOT_RUN이다. HE AZIMUTH09는22/22PASS,109CASzeros+2True,local9complete+1partial+3physicalopen/13이다. 기존 KINEMATIC08의 plot CPU7.040661>6FAIL은 새 성공과 구분해 남겼다.

REC weighted-enclosure02는28accepted/29evaluations와556referencePASS를 보고하지만 fresh R6/C9 미수행으로HOLD18/20, actual physical coverage0/313이다. 해당 owner backup의 원격 전체 byte readback은NOT_RUN이며 WU가 대신 검증했다고 하지 않는다. REI thermal endpoint는 옛R1 handoff1/20보다 최신 R3 source3/20을 우선했다. Matched bath/EOS/native25가 여전히 열려 있다. 중앙 scoped status는28/88와HEdelta0을 명시한다. Vigil의464개 기존 통과와 새로운 CI/정책 부록을 구분했고 전체 release 성공으로 승격하지 않았다.

새3branch와 관련 변경분에서 GL2022 reactive array, 이름이 정해진 WU HD consumer, 실제 para-H2 density/clock의 신규 회수는0이다. 이는 조사 범위의 관측이며 전역 부재나 물리 no-go가 아니다. 상세 immutable URLs, source bytes 및 원문은 authority/LATEST_SOURCE_MANIFEST.json과latest_sources/에 있다.

## 3. 문헌과 연구 의무 선택

요청된 Exa는 중단 전5검색/28requested slots,6fetch/10URL slots; SciSpace는3검색/30paper rows에 실제 사용했다. AIP GL2022(DOI10.1063/5.0128598) 색인 본문 eq5–7의 incoming thermal average와 product even/odd1/4,3/4 가중치를 읽었고, 반응1 state-to-state 숫자가 supplementary에 있다는 정보를 확인했다. DigitalCSIC10261/305186 locator를 찾았지만 native array bytes를 얻지 못했다. EMAA HD rovibration10.17178/emaa_hd_rovibration_805a7aa5는 excitation 자료이며 reactive destruction으로 대체하지 않는다.

Mitrophanov2005 §2eq2.5–2.7의 contraction convolution, Michel–Siegle2024 §3.2Theorem4의 CTMC initial-error/defect 적분, Yazdani–Hadizadeh2012 §3Lemma5의 piecewise enclosure/intersection을 기존 원리로 연결했다. Hilder–vanMeurs–Sharma2026은 비평형 coarse-graining의 최신 맥락이며 그 가정/상수를 이 작업으로 옮기지 않았다. 양의 역행렬과 Volterra comparison 자체의 일반적 신규성을 주장하지 않는다. 이번의 새 결과는 이 프로젝트의 비교식에 대한 signed-d causal cell closure와 source-bound exact 구현이다.

원전: [GL2022](https://doi.org/10.1063/5.0128598), [Mitrophanov2005](https://doi.org/10.7153/MIA-08-15), [Michel–Siegle2024](https://arxiv.org/html/2403.07618v2), [Hilder–vanMeurs–Sharma2026](https://arxiv.org/html/2602.17579v1). 접근 오류와 실제 판독 범위는 authority/LITERATURE.json에 구분했다. 환경 장애 뒤 일부 raw tool response는 접근되지 않지만 당시 실제 판독과 이후 root의 직접 원전 read 범위를 섞지 않았다.

R8의 두 global Picard passes 뒤에도 native9 상계가 저장 참조보다 약311/907배 컸다. 이번 질문은 같은 셀 결합을 직접 닫을 수 있는가였다. 선택한 raw/capped 해법과 추가 global pass, 방향별 새 certificate, 실제 physical consumer 결속 후보를 비교했고, 새 physical/source producer 없이 풀 수 있는 구체 수학 의무를 선택했다.

## 4. 조건부 일반 정리

비음수 연속 오차 R,E, 유효한 고정 계수 a,b,c,g_r,g_e≥0와 signed d, 균일 셀 I_n=[nδ,(n+1)δ]를 둔다. 동일 generator family/state order/clock/l1 residual의 uniform-all-starts 인증 커널 h는1=h0≥h1≥…≥0이고, 저장 e_bar≥exp(dδ), phi_bar≥integral_0^δexp(du)du이다. R0,E0는 초기 상계다.

과거 셀 상계 U_R,j,U_E,j에서 F_j=aU_R,j+bU_E,j+g_r, L_j=cU_R,j+g_e를 만든다. 실제 현재 셀 suprema r_n,q_n은

$$r_n\le A_n+\delta a r_n+\delta b q_n,\qquad q_n\le B_n+\bar\phi c r_n.$$

$$A_n=h_nR_0+\delta\sum_{j<n}h_{n-j-1}F_j+\delta g_r.$$

d≤0이면 B_n=e_bar^n E0+phi_bar sum_{j<n} e_bar^(n-j-1)L_j+phi_bar*g_e다. d>0이면 초기 지수는n+1, 과거 지수는n-j로 바뀐다. 이는 exponential 과거 적분의 셀 최대가 각각 왼쪽/오른쪽 끝에서 생기기 때문이다. 현재 fresh forcing에는h0=1을 사용한다.

$$D=1-\delta a-\delta b\bar\phi c>0$$

이면 q 부등식을 r에 대입해

$$R_n^*=\frac{A_n+\delta bB_n}{D},\qquad E_n^*=B_n+\bar\phi cR_n^*$$

를 얻는다. 양의 역행렬 D^{-1}[[1,δb],[phi_bar*c,1−δa]]가 같은 결론을 준다. 첫 셀에서는 과거 합이 비어 있고 각 완료 셀의 상계를 다음 셀에 넣는 귀납이 성립한다. 초기 전체 궤도의 오차 envelope는 raw 입력에 필요 없다. 계수의 구간 전체 유효성과 외부 kernel/factor 인증은 여전히 전제다.

같은 닫힌 셀의 인증 cap Cw가 있으면 U=min(U*,Cw)를 성분별로 취한다. Endpoint는 h[n+1]R0+δsum_{j≤n}h[n−j]F_j와 e_bar^(n+1)E0+phi_bar sum_{j≤n}e_bar^(n−j)L_j로 계산하고, 현재 closed-cell bound 및 같은 정확한 시각의 point cap과 교차한다. 참조 trajectory sample을 cap으로 쓰거나 point cap을 whole-cell cap으로 보간하지 않는다.

D≤0은 이 충분조건/API domain을 벗어난다는 의미다. 반응계 발산이나 물리 불가능성을 뜻하지 않는다. Signed d를 절댓값으로 바꾸지 않고, source의 native v=UNSPECIFIED와 MISSING_NOT_ZERO를 유지한다. 선택 사례는 무차원 비교 좌표이며 실제 물리 clock/density 변환은 아직 결속되지 않았다. HD에서 E=|eta|, 전체 coarse l1은4E다. [전체 증명](https://github.com/cosmosapjw-quantum/WU088_HH/blob/f8b4ea63381fcdab91577c31005bc85e66789141/research/provider_registry_molecular_r9_20261028/theory/PROOF_KO.md) · [정리/API 계약](https://github.com/cosmosapjw-quantum/WU088_HH/blob/f8b4ea63381fcdab91577c31005bc85e66789141/research/provider_registry_molecular_r9_20261028/theory/THEOREM_AND_API_KO.md)

## 5. 구현과 수치 검증

공개 함수는 src/causal_resolvent.py의 sweep(B,g,delta,initial,kernel,coarse_factors,*,binding,whole_caps=None,point_caps=None,bits=128)다. Exact Fraction 합·곱 뒤 지정 scalar만 dyadic128로 위로 반올림한다. D는 exact로 유지하고 min은 다시 반올림하지 않는다. 유한 domain은1..192cells,8192-bit exact scalars,abs(d*delta)≤16,ordered states1..16이다. Float/bool,잘못된 shape/grid/family/source 및 비양의D를 거부한다. Generic metadata 검사와 실제 인증 부등식의 원천 증명은 구분한다.

S05 실제 실행에서3개 Python AST와9개 동결 source의 SHA/bytes가 PASS였다. Primary는 immutable R8 primary SHA520110d1cae1677491aecd7216621c25f1098470c939ee027d5df3bde183686b에서 입력과cap을 직접 읽었다. Independent reference는 생산 함수/이전 producer를 import하지 않고 Decimal100 직접 convolution과 E-first Gaussian 소거를 썼다. R7 저장 trajectory SHAe403c7803c080fd4f26be71a93b782b02d874f80ef11c85a706bea71e2a743cd의193시각을 보조 대조했다.

정확한 무반응, 상수 forcing, nilpotent 해; D=7/8의 R=8/7,E=2/7; D=1/1000의R=1000; signed-d maxima; fresh forcing h0;8192-bit roundtrip 및 provenance 거부를 검증했다. 실행 전 PRE01은 deepcopy의 binding alias를 분리했고 실제 guard가PASS했다. PRE02는 freeze PASS/bytes/SHA/required paths 조건을 명확히 하고 실제 reference에서 확인했다. R9 runtime failure0이며 사후 tolerance 변경이나 repair run은0이다.

오차 예산은 epsilon=2^-128을 powers,A/B,R/E,F/L,endpoints의 실제 반올림 위치와1/D를 따라 전파한다. 관찰된 생산−독립 최대 차이는 약2.859409286e-37이고 전역 최대 전파 예산은5.642372884e-37이다. 실제 판정은 각 component의 자체 예산을 사용했다. 최소 차이−1e-99는 Decimal100의 별도 scale×1e-80 guard 안이다. 같은 저장phi_upper를 비교하므로 기존 R8의 fixed1e-30 phi-closeness 오류를 반복하지 않았다.

438reference checks/34590component comparisons는 서로 다른 물리 실험 수가 아니다. 고정 grid/128bits에 대한 source/rounding/conditioning/제한해 검증이며 mesh-refinement 차수나 hardware speedup을 주장하지 않는다. 저장 sample containment도 새 continuous ODE certificate가 아니다.

## 6. 실제 결과와 의미

| 사례 | R9 capped R | R9 capped E | R 감소율 | E 감소율 | bound / saved sample R,E |
|---|---:|---:|---:|---:|---:|
| 2-state 무반응 | 0.0610351563 | 0.00000000 | 0.00000000% | — | 1.09416237 / — |
| 2-state 비선형 | 0.0678043993 | 0.000516508447 | 0.000129790040% | 0.00493586739% | 1.19013497 / 2.66240154 |
| 2-state source 차이 | 0.0678051452 | 0.000685196005 | 0.000131424970% | 0.00377943075% | 1.19014807 / 5.72801368 |
| native9 조건부 | 0.0000364476161 | 6.19120080e-7 | 0.0000738119131% | 0.00549060141% | 310.953728 / 907.041143 |

무반응의E=0/0비율은 정의하지 않았다. 모든 소수는 표시 근삿값이며 정확한 유리수는 raw/PRIMARY_RESULTS.json과raw/RESULT_ANALYSIS.json에 남아 있다.

두 nonlinear2-state 사례는 각각 raw whole성분1개(cell63,R)와endpoint성분8개가R8보다 크다. Capped 결과는 HD whole1536성분 모두 no-worse(1150strict),endpoint1544성분 모두 no-worse(1136strict)다. 이 실제 차이는 raw의 일반적 우월성을 가정하지 않고 동일 구간의 유효한 cap을 교차해야 한다는 설계를 뒷받침한다.

Native9의 R=3.6447616117818194e-5,E=6.19120080246264e-7에 비해 저장 sample은1.1721234642357073e-7,6.825711107438792e-10이다. R9는 큰 보수성의 주원인을 제거하지 않았다. 주요 성과는 현재 셀 결합을 직접 닫는 구성과 검증된 API이고, 정확도 개선은 위의 작은 실측 범위다.

## 7. 독립 검토·CAS·기존 실패 보존

생산 core/primary 작성자와 독립 reference/검토자를 분리했다. 검토자는 reference를 작성했으므로 reference 작성자 자체에 대한 제3의 독립 검토라고 부르지 않는다. 한 번의 bounded pass 안에서 증명, immutable source, 실제 freeze/primary/reference/process와 결과 해석을 확인하고 PASS_SCOPED_FINAL_C9,openmaterial0으로 끝냈다.

Wolfram 새 호출은7algebra+4control residuals0을 반환했지만 positivity는1True/3unreduced였다. 이를 QUALIFIED_SYMBOLIC_CORROBORATION으로 기록했다. 1−δa=D+δbphi*c>0과R*,E*≥0은 직접 증명 및 독립 R6로 성립한다. 추가 CAS나 재검토를 요구하는 새 수학적 지적은 없었다.

기존 R8 primary237/237,원래 reference726/727PASS+1FAIL,별도 exact scalar repair24/24를 그대로 재사용했다. 원래 reference를727/727PASS로 바꾸지 않는다. 이전 CAS warning과 실패 원문도 유지한다. R8및더이전의 exhausted allowance를 재설정하거나 old science를 재실행하지 않았다.

## 8. 환경 복구와 게시·백업

Local exec-server handshake가 실패해 로컬 접근이 중단됐다. 기존 authorized GitHub Actions에서 contents:read,secret없음,run_attempt1,immutable source guard,create-only results,60CPU/90wall 제한을 적용했다. 새로운 계정이나 임의 실행 host를 만들지 않았다. 세 child의 tree전송과 한 blob 대체 경로는ACK없이 중단되어 unknown 상태로 남겼다. Core/reference원문은 직접 전달해root가게시했고,공개census는정상인root read-only 경로로복구했다. 과학계산을잃거나중복실행하지않았다.

초기 S01 Drive 업로드의 transientURL403은 만료를 진단한 후 새 artifact 참조로 즉시 업로드하여 닫았다. 원본 실패는 ledger에 남겼으며 공개파일에 임시 signedURL을 넣지 않았다.

각 checkpoint는 actual expected-parent SHA와force=false로 기존research/provider-registry-20261025에 게시했다. PR150은draft이며base는research/program-expansion-20261025를 유지한다. Mainmerge나other-owner writes는0이다.

이 S10 source를 작성하는 시점에는 S01–S09의9개 단계 ZIP과18개 provider 원본 검증이 완료됐다. S10 자체의 게시·archive·양 provider 원본 검증이 다음 동작이다. 최종 metadata source에서 그 실제 영수증을 반영한다.

| 단계 | 단계 종료 절차 | 과학 DAG | 실제 source commit | Drive ZIP 및 양 원본 확인 |
|---|---:|---:|---|---|
| S01 / R1·C1 | 2/20 | 17/34 | [cce2d6344401](https://github.com/cosmosapjw-quantum/WU088_HH/commit/cce2d63444016a526d96ec9c7020e0cd3b803eb3) | [22aecfa24dd2](https://drive.google.com/file/d/1N8dGh98YLZNFMH2wUTAOPzsxxqKLM1Rj/view) · 두 원본 일치 |
| S02 / R2·C2 | 4/20 | 17/34 | [e5fbe3ffcdb3](https://github.com/cosmosapjw-quantum/WU088_HH/commit/e5fbe3ffcdb321735dbf337f110a07a040378d17) | [ec26b5cd16bd](https://drive.google.com/file/d/11A3Xh5LG3Rlt_f2qhcy5WXdgJslLwv7F/view) · 두 원본 일치 |
| S03 / R3·C3 | 6/20 | 17/34 | [c8031c66f08c](https://github.com/cosmosapjw-quantum/WU088_HH/commit/c8031c66f08c17a38238f0d900209a3ef8306954) | [ab178162704e](https://drive.google.com/file/d/1uA8S5fyLnYlDWdEgjETTH2Jy2pUDSyMx/view) · 두 원본 일치 |
| S04 / R4·C4 | 8/20 | 17/34 | [b5cb7d3fc172](https://github.com/cosmosapjw-quantum/WU088_HH/commit/b5cb7d3fc17243070a36533ab3c4ef50077d6751) | [413ef312a6fb](https://drive.google.com/file/d/1b65HUd-KDoRarwvqF83zlHl4mDVVEBWu/view) · 두 원본 일치 |
| S05 / R5·C5 | 10/20 | 17/34 | [c9d8ff41d85d](https://github.com/cosmosapjw-quantum/WU088_HH/commit/c9d8ff41d85dd5e7d31dd78467d561b7a2ab221b) | [c4ca23d3c5b9](https://drive.google.com/file/d/1lzeyEwhyIZCllq7YmRQuJ4E_2kAdlLQQ/view) · 두 원본 일치 |
| S06 / R6·C6 | 12/20 | 17/34 | [ce5e4ca5d216](https://github.com/cosmosapjw-quantum/WU088_HH/commit/ce5e4ca5d216e092e6f01e9521add5662b514dd0) | [9622e199932e](https://drive.google.com/file/d/18_vQm-10n75p-5nYRnJrU5QiA0E4DagF/view) · 두 원본 일치 |
| S07 / R7·C7 | 14/20 | 17/34 | [1b026536ef2a](https://github.com/cosmosapjw-quantum/WU088_HH/commit/1b026536ef2af0ecbe31ba83335cca1f2b742d09) | [ed1698aebd4c](https://drive.google.com/file/d/1O6SAt-6GWabdJQedVGNGEGeVqPI2494n/view) · 두 원본 일치 |
| S08 / R8·C8 | 16/20 | 17/34 | [9617c78f4041](https://github.com/cosmosapjw-quantum/WU088_HH/commit/9617c78f4041f72d394d4625d8481e8a5745bddb) | [25b4e141d71f](https://drive.google.com/file/d/1S_CdFUSxkdk_z8RSQ6NQCFdgHwokKuUp/view) · 두 원본 일치 |
| S09 / R9·C9 | 18/20 | 19/34 | [f8b4ea63381f](https://github.com/cosmosapjw-quantum/WU088_HH/commit/f8b4ea63381fcdab91577c31005bc85e66789141) | [2492bf821959](https://drive.google.com/file/d/1IPTI-LQ3z3nvjd2azBB1JLrbVoll42Ew/view) · 두 원본 일치 |
| S10 / R10·C10 | 20/20 | 19/34 | 이 S10 source의 containing commit | S10 게시 후 실행·원본 검증 예정 |

Archive scope는R4–R9 연구 leaf+AGENTS+R9workflow다. 전체 repository/history 백업이라고 부르지 않는다. Actions가 각 tracked source의 실제Git blob을 대조하고 ZIPCRC를 확인했다. 이후 Drive와Dropbox의 원본을 각각GET하여 archive bytes와SHA256을 확인했다. Remote copies를 별도 unzip한 것과 byte-identical 결과를 구분한다. 단계 영수증의 원문은delivery/PUBLICATION_INDEX.json,개별Sxx.json에 있다. 파일명 날짜20261028은KST이고 raw execution timestamp는UTC다.

## 9. 다음 연구와 재개

우선적인 물리 입력은 실제 reactive state-to-state array의immutable 원본,사용할consumer/state/spin/branch/common-pool,실제density/time law,초기H/D/charge invariants,whole-domain box 및same-family all-starts certificate다. Excitation을destruction으로바꾸거나missing채널을0으로채우지않는다. REI의thermodynamic N/U,CR의parent/channel,HE의azimuth,REC의tube범위를source-qualified 사상없이대체하지않는다.

입력 변경이 없다면 실제 남은 native9의 큰 상계 차이를 propagation/forcing geometry로 나누어 설명하는 별도 계산 가능한 의무를 먼저 고정한다. 해당새단위의resource계약을정하고완료된R9를반복하지않는다. 별도후속루프는이번종료에서자동으로시작하지않는다.

재개자는 HANDOFF_KO.md, SCIENTIFIC_ADMISSION,35-file manifest, DAG, ledger, latest intake, PR150의최종전달영수증을읽는다. 현재branch가더진행되었으면새HEAD와이source를비교하고hard reset/force push하지않는다. 기존결과의검증은파일identity검사로시작한다. 새과학실행은실제변경의무에대한새계약으로진행한다.
