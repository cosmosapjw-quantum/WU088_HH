# HH-ON05B: 고정 birth와 HI 문턱 분할

판정: FIXED_BIRTH_EVENT_REMESH_MATCHED_CONTRAST_MEASURED__LIVE_F08_AND_CONTINUUM_OPEN. HH 연구 ACTIVE. 이번 bounded phase B는 끝났으며 canonical S0/F08의 HH OFF와 기존 인증은 보존했다.

## 실제 구현·검증

원 0..8e11s S0-derived moving-cohort 모형의 두 기하와 OFF/LCS를 사용했다. 각 해상도의 원 accepted-half birth 160/320개, 32방향의 시간·에너지·방향·가중치를 동결했다. 두 기하에서 13.6eV fit cutoff와13.598434599702eV binding crossing의 합집합을 삽입했다. 내부 event에서 새 birth는0이다. 동일 binary64시각만 병합하며 fuzzy merging은 없다. rounded mp80 analytic event시각과 실제 native transport의 차이는 남고 uniform event-time certificate가 아니다.

coarse289/fine572 accepted-source 구간을 네 경로가 공유한다. 각 macro의 네 후보가 모두 통과해야 함께 commit한다. 비수락 auxiliary full map은 원래 estimator용이며 accepted remesh와 동일 source quadrature가 아니다. full-vs-remeshed local proxy를 연속오차상계로 해석하지 않는다.

실제 native paired process3회 중 첫 coarse는 올바르게 거절됐고, reserve를 사용한 coarse/fine2회가 완료됐다. 완료8구성에서960macro/3444acceptedsource/960auxiliaryfull,4404map 호출. 실패 시도의 전체map호출수는 완전계측하지 않았다. 신규18tests,독립최종70854assertions/64고유BEendpoint,1722matched환경pair와1728pre-event기체bitwise대조를 확인했다. 최대BE차2.220446049250313e-16,사건율 상대차6.390463073893204e-15. 최대전구간energy1.576276008354639e-14,event3.3635717572025478e-15,ONdirectbound합2.778379889212489e-14로기존1e-12아래다. local최대5.347236108821374e-5<2e-4.

## 실패와 수치 수정

첫 실행은 t7.3e11s에서 time-only budget보다 stagnated state의energy결손상계가커서 거절됐다. 네경로 해당macro미commit. 사전명시된 finite-list reserve를켜서 b_j=.75epsilon*dt_j/T+1_affected*epsilon/(2Naffected)를 사용했다. epsilon1e-12,T1e13이며현8%prefix의총배정은최대.56epsilon이다. 전체기준이나normtolerance1e-15는완화하지않았지만 예산분포는변경됐다. projection/refill/clipping은없다.

독립checker의fine최종짧은구간4개는원(old+delta)-old-dtF식의상쇄로progressfailure였다. 같은실수방정식을delta-dtF로바꾸고normalizedphysicalresidual<1e-15를추가했다.32선정진단에서새실패0,최대physicalresidual6.52284e-17. native재실행없이미완료fine검사만닫았다. 원checkers/실패/logs를보존했다. 괄호누락compilefailure와root진단45초환경timeout도별도다. 18개전체가red-first이거나독립심사자검토를받았다는주장은없다.

## 결과와 해석

D=LCS-OFF,A=D_BI-D_FLRW. 최종D_x는coarseFLRW8.062587142365629e-8/BI8.062611212000803e-8, fineFLRW8.070270851590067e-8/BI8.070295087758694e-8. 약.0952%의두격자변화다.

원A_x=3.789135671894428e-11/5.843103778602199e-13에서event후2.4069635173873394e-13/2.4236168627567167e-13으로가까워졌다. 최종격자변화.68713%,공통birth시각최대차9.769962616701378e-15(t7.35e11s). exactEOS의A_T=-2.0403358461240524e-8/-2.0660074886420666e-8K,최종격자변화1.2426%,공통시각최대차4.865711517141385e-10K다.

고정birth에서event-related remeshing이큰민감도에강하게영향을미친유한증거다. sourcepartition과budget도바뀌었으므로모든차이를cutoff시각하나에귀속시키지않는다. coarse/fine사이birth측도는서로다르다. A는네binary64상태의매우작은차이며nativeevent-edge에너지차최대4.42313e-13eV의globalcontrast기여도미확인이다. 물리신호/참해.69%정확도/각도연속체/일반root인증은아니다.

## 재현 및 저장 상태

전체원시ZIP: WU088_HH_ON05B_FIXED_BIRTH_EVENT_20261005_v1.zip,413950057bytes,219entries/218payloads,SHA256117245432848a513d3bc05a73813de148cda42d01149935de23afee2ef3602a7. 대화산출물로존재하고localCRC/manifest확인. 원격upload는nativeadapter UNREGISTERED_FILE_REFERENCE 및Drive Library file_too_large로실패했다. 전체원시이중백업완료가아니다.

별도복구core: WU088_HH_ON05B_RECOVERY_CORE_20261005_v1.zip,634441bytes,209entries,SHA256212348d676edc4faf05eed198b72fc452b8300cf442eb3e6fb442ff3caffaafa. 원source/input/test/results/failure207개파일을유지하고12개native.jsonl.gz만제외했다. RECOVERY_CORE_MANIFEST는제외파일의size/hash와전체ZIPidentity를명시한다. core의원MANIFEST는fullarchive용임을주의한다. Drive1xUjOM7jMT3kbQkgtp0IxoVydLViTywWP/Dropbox id:BSpOijBcT10AAAAAADzICw에core만이중저장완료. Drivecore는Dropbox전송을위한실제회수와SHA확인,Dropbox는R1ID/name/path/size확인이다. raw전체restore나raw전체remotebackup과구분한다.

전체유도·실행명령은REPORT/THEORY/REPRODUCE,실제실패는NUMERICAL_BUDGET_AMENDMENT/REFERENCE_CHECKER_REPAIR/evidence에있다. Git폴더는검색·인계용이며standalonecrate가아니다. event_grid.py와9개tests는검증ZIP과byte동일하다. 다른요약문을전체보고서와byte동일하다고하지않는다.

다음HH-ON06은실제F08의point/thermal/dedicatedHHcounter와interval/Jet2/primary_stage_root,immutablebudget,model/checkpointidentity를동시에묶는작은pilot이다. 기존사용자승인을계승한다. oldatomic/KS/각도/새continuousODE/fullF08F09/NCP/HHprimitive재실행0. legacy24/289·265unbounded·epsilonnull·B22OPEN·consumedscopes보존.

REIsealed76be0902이후a2bc41f8의FLRW08-MACRO문서8개증분을읽었다. fixed-grid첫macro의half오차계승은별도모형이고HH에인증전용/재실행하지않았다. 상세LATE_REI_ACK. canonicalTASKS/S0/F08source변경없음. 같은HHbranchappend-only/non-force,PR33/REI반환PR83.
