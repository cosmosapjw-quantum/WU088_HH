# HH-ON04: 실제 S0 입력 선택과 첫 HI 문턱 통과

판정: S0_JSON_HH_RESEARCH_DISPATCH_AND_FIRST_THRESHOLD_PREFIX_PASS__LIVE_F08_AND_CONTRAST_ACCURACY_OPEN.

HH 연구는 ACTIVE다. 원 canonical S0 JSON bytes를 실제로 읽는 fail-closed 연구 dispatcher를 구현하고 OFF/LCS/KS를 명시적으로 native에 전달했다. 두 기하의 0..8e11s(원1e13s의8%)에서 fit13.6eV와 binding13.598434599702eV를 각각 통과했다. canonical F08 fixed-energy interval producer는 변경/실행하지 않았으며 원 HH OFF는 그대로다. 이번은 ON03계승 moving-cohort 경로다.

## 결과

coarse dt1e10s의 OFF/LCS/KS×FLRW/BI6개, fine dt5e9s의 LCS×두기하2개: 실제native8process,800acceptedmacro/1600sourcechildren/2400BEconstituent, 모두exit0. 새Python8tests는8assertionRED후GREEN, 새native6tests는post-implementationcoverage다. 최종14개통과. 원source/criteria는유지했다.

독립history검사31532개,선정66개BEroot를oldstate에서출발해대조했다. 최대root차2.6342843850093956e-16,같은endpoint사건율최대상대차5.553253008519273e-15. 최대누적exactenergy잔차1.6270001862878988e-14,최대전자+photon결손2.6684559273689764e-15,ONbound합1.768764663276979e-14로원1e-12아래다. maximumlocal1.0193003808967038e-4<2e-4. 단면적은sharedstageinput이며sourcefit/연속오차/parameterbox의인증이아니다.

E<13.6과binding..13.6 gap에서sigma/HIphotoevents0,photoncount가source동안보존됨을확인했다. 아래문턱광자의number/energy를retained로두고이중loss/export는없다. exact13.6은active이고photoheat/event=13.6-chi>0이다. FLRW첫fitcrossing약7.326040092073e11s,binding약7.441149680016e11s. highprecisionroot는기하진단이고actualsource는fixedgridmidpoint로평가했으므로event-alignedtimeaccuracy를주장하지않는다.

## 남은 시간 정확도

LCS fine-minus-coarse xHII는FLRW -4.796872719481371e-6, BI +4.584931887796628e-5. coarse LCS-OFF는각각8.058612666062004e-8,8.062401801733898e-8. fineOFF를계산하지않았으므로앞의차이를HHcontrast오차의상계로쓰지않는다. 공통bias가상쇄될수있다. 현재자료로HH효과의relativeaccuracy/physicalsignificance는미확인이다. 다음HH-ON05는matchedOFF/ON의공통event-aware시간격자와contrast정밀화다.

live F08을ON으로바꾸려면pointsource뿐아니라 intervalRHS/Jet2/primary_stage_root,HH전용events,immutablebudget,model/checkpointidentity를함께결속해야한다. 옛OFFcertificate에ONpoint만붙이지않는다. 본useractivation은계승하며승인대기로되돌아가지않는다.

## 실패 보존과 증거

첫finechecker는45초container timeout; assertion/native실패가아니다. exactdyadic합산을동일정수산술로최적화하고12동등성검사를한후두fine검사통과. 원로그보존. 미계측photo_calls_off0placeholder는삭제했으며 no-callback관측으로쓰지않는다. 문턱진단재현에서ideal80digittrig와원binary64component→mpnormalize의혼동을strictidentity실패로보존했다. 원representation을명시하여1e-70동일기준의최종차이0확인; native/physics/criteria변경없음.

newcontinuousODE/각도정밀화/oldHHsuite/primitive/NCP/fullF08F09/독립reviewer실행0. F08전체HH-OFF15history반환은수신했지만재실행하지않았다. legacy24/289·265unbounded·epsilonnull·B22OPEN·consumedscopes보존. physical/production/root/flowadmission=false.

## 전체 재현과 백업

Git에는이요약,결과,실행기,선택/후속/lateACK와backupmetadata를둔다. research/s0_dispatch.py는ZIP과blob792265341a6f1de3ee9e5dda6108d78c9bd39fbe로동일하다. Git폴더자체는standalonecrate가아니다. 전체nativecode/원source13개/14tests/독립checker/모든acceptedrawgziplogs/실패/입력/유도/REPRODUCE_KO는ZIP에있다. 요약문은상세보고서와byte동일하지않다.

WU088_HH_ON04_S0_DISPATCH_THRESHOLD_20261005_v1.zip,77044486bytes,171entries/170payloads,SHA256807139b037e1d0e625d8bcdeb0fbb0fb84ebd227d7d9efec9ac133c245c3bf2d. Drive18xIlyWJQz1idL1r1HH_CwjBqVVy7CCR0,Dropbox id:BSpOijBcT10AAAAAADzFpA. 원Driveparent1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM/기존HHDropbox폴더에create-only. 양provider완료/ID/name/size확인,R1이며새outputfullrestore=false.

HHparent89f4d9e5,REIinpute63ca073. seal후REI8629a630의FLRW08문서8개추가만읽었다. pointnative/source/S0변경없고그외부실험은재실행하지않았다. exactlate범위는LATE_REI_ACK.json이다. 같은HHbranchappend-only/non-force,PR33와REI반환PR83.
