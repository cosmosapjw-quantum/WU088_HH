# PHYS82 이후 재개 계약

Repository: https://github.com/cosmosapjw-quantum/WU088_HH
Draft PR138: https://github.com/cosmosapjw-quantum/WU088_HH/pull/138
Branch: research/hh-phys82-li-threshold-sensitivity-20261023
Parent PHYS81: b3ec271a96cb67e583bffa9b61533802838236f9
Scientific results commit (final source-byte restoration recorded separately): 6a5c5a48e0ef345ff438941d037c9452453b1fb3
Scientific identity: caae042b139373a10c516d759854ad117d807e9f7ace8c365529a1621419b73f
Unit: research/hh_phys82_li_threshold_sensitivity_20261023

최종 metadata HEAD 및 최종 ZIP SHA/Drive·Dropbox IDs/전체 복원검증의 확정값은 외부 PHYS82_FINAL_DELIVERY_20261023.json과PR138최종본문에서 읽는다. 이 Git문서는 자기HEAD를 자기내용에 넣지 않는다. 시작 전 actual branch refs를 읽고 비교한다.

## 완료하여 재사용할 것

Li7 threshold I=5.39172060034581eV부터6eV까지 네 CCC endpoint matched 모델L0/L1/W0/W1와 독립 recentered ZA1969 slope comparator를 구성했다. Source facts와physicaluncertainty구분, 양의 gamma moment·exactT derivative·reaction-selected energy·fixed-exposure difference를 구현했다. Existing CCC6–15eV13knots는그대로다.

새study1시도=1완료+0실패.72T,새baseline63,저장baseline9재사용,gap360,total360,exposure1080,새ODE0,benchmark0. 실제resume1회skip/scientificcallback0. 독립검증1924assertionsPASS_SCOPED. 첫verifierlabelNameError와그에따른accountingfailure2records는보존하고미완료controls만수정실행했다. 수치matrix재실행0. Wolfram4residual0. 그림3PNG3PDF.

Tmax25370.66308424773K에서gap은기존finite rate대비3.07055–3.39319% 증가(ZA3.45822%).255K에서는비율2.3374e10–3.7061e10이지만K~1e-115cm3/s. 이값은finiteconditionalmodel결과다. 고정노출량확률차이를coupledthermaltrajectory오차경계로쓰지않는다.

## 반드시 읽기

FINAL_REPORT_KO.md, CONTRACT.json, DAG_OVERLAY.json, EXECUTION_LEDGER.json, RESEARCH_LOOP_MAP_KO.md, source_data/LI_THRESHOLD_SOURCE_CONTRACT.json, theory/THRESHOLD_CONSTRUCTION_KO.md, verification/INDEPENDENT_REVIEW_KO.md, delivery/SCIENCE_PAYLOAD_MANIFEST.json, CODEX_HANDOFF_KO.md, POST_PUBLICATION_HANDOFF_KO.md, delivery/ 및외부finalJSON.

## 다음 선택 DAG

BOUND_BOUND_CE_AND_RADIATIVE_COOLING: primary excitation strength/state/branching와radiation-energy contract를물리단계에서먼저닫은뒤코딩한다. He/LiCX product-state/photon-energy도parallelOPEN. Li source는energy-response/deconvolution,isotope/targetstate와physicaluncertainty가OPEN이며조건부곡선반복계산으로대체하지않는다.

핵쪽: PHYS81 radiative-capture photon/recoil사건회계를thermal/fast particle-numberownership,normal-frameenergy,finite-T eventaveraging과먼저연결한다. 실제rates/stopping은그후다. RECOMBINATION_TO_Z20_INITIAL_CHARGE_CONTRACT,D_PI_RR_MATCHED_SOURCE_MOMENTS,LI_HARD_UV_INNER_SHELL_SPECTRAL_CONTRACT,FULL_GEOMETRY_SPECTRAL_BACKREACTION은OPEN이다.

## 최신외부결과를원래범위로재사용

HE37 d618344413193950ec3e4e499be526d1ed636d98: H1 stationary-heavy-target/isotropic-outgoing/infinitesimal electron Grad STF;gasSTF아님. C23A215defe6f631050255b73baec83e9418a8a2b66f(science7643af28…): P19HHez0–15.1,FS2010finite,beta conditionalcoverage. REIANGTHERM01 00303ab27c33a7afa0cec61679af78ef72e3f4aa: preparedinputs,새IVP0. 상세inventory에서identity를읽고현재refs로delta만확인한다. 접근불가능한privateconversation전수검사를주장하지않는다.

## 중복실행금지와보호계약

PHYS78/79/80/81/82 및 HH1231/REI729/HH74control63,C22D/E,REIlocalflows,REC124/125/126,HE34/35/36/37,ANGULAR01,C23A의완료identity를재실행하지않는다. runtime버전이다르다는이유만으로완료science를자동재실행하지않는다. 다른process를종료하지않고sharedlease와1worker/thread를지킨다.

non-tiltedLRSBianchiI;reactinggaspi0,collisionlessDMpi_m별도. 같은normalorthonormalframe의signedmatter/radiationtensor를합한뒤norm,Frobenius=sqrt2×half-contraction. sampled검증은continuumcertificate아님. same-trajectorycomponents는species-offcausalexperiment아님. HH_R10=OFF. Production admission NOT_ISSUED.

## 실행 및 코드 연결

Python3.12.14 / NumPy2.3.5 / SciPy1.17.0. source/threshold_gap.py의 named_models(), evaluate(T), combine_rates(), fixed_exposure()가 계산 API다. source/run_study.py는9개저장row를읽고새63온도에만byte-pinnedfinite_ci를호출한다. source/plot_study.py는저장결과만읽는다.

원래실행명령은아래와같다. 이미완료된checkout에서는새receipt이름으로science를요청하지말고저장receipt와identity를먼저읽는다. 같은identity의run_study는SKIPPED_IDENTICAL_COMPLETE를반환해야한다.

```bash
python source/leased_call.py --label THRESHOLD_STUDY_001 --receipt verification/LEASE_THRESHOLD_STUDY_001.json -- python source/run_study.py
```

위receipt는이미존재하므로보호wrapper가재호출을거부하는것이정상이다. 삭제/rename으로재실행을허용하지않는다. 새단원은별도directory와새physics/input계약을만든다. Git에는고유PHYS82directory만추가하며기존parentfiles와main을수정/merge하지않았다.

최종Git science51파일은delivery/SCIENCE_PAYLOAD_MANIFEST.json으로동결했다. finalmetadata와providerrestore상태를수정할때이51파일은변경하지않는다. 공유lease원본은PHYS78sourceSHA76ff57ba…이며oldscientificrunner를호출하지않고LeasePool만재사용했다.

## 최종 Git byte 복구

최종 원격 blob 대조에서 PHYS81_LITERAL.csv 하나의 CRLF가 초기 text export에서 LF로 바뀐 사실을 확인했다. 로컬 과학 입력과 S0/S1/S2 백업 payload는 원본 bytes를 유지했으므로 저장 과학 결과와 scientific identity는 변하지 않았다. 원격 source pin은 변환된 CSV의 실행을 거부한다. 원본 bytes를 base64 Git blob으로 복구하는 추가 descendant를 만들고 최종 원격 전체 파일을 대조했다. delivery/TRANSPORT_BYTE_REPAIR.json이 관측된 이전 blob과 정확한 원본 identity를 기록한다. 과학 결과 commit6a5c5a48만 checkout하지 말고 외부 final-delivery JSON이 가리키는 최종 HEAD를 사용한다. 새 과학 실행0이며 final archive가 이 복구를 포함한다.
