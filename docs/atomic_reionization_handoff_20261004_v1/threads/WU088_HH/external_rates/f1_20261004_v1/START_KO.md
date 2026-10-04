# HH-F1 producer reference: fastest lane

판정: HH_F1_PRODUCER_REFERENCE_VERIFIED__WAITING_ON_REI_DOMAIN. 전체 HH-F1은 partial이다. 원 PROGRAM의REI_DOMAIN_FREEZE는REI-F07이다. 핵심코드와23개새검사(5개RED/GREEN+18후속회귀)는이디렉터리의src/tests에서실행한다. tests에는mpmath1.3.0이필요하고CLI는표준라이브러리만쓴다.

```sh
python3 -B -m unittest discover -s tests -v
python3 -B src/hh_external.py --provider LCS91 --lower 2999 --upper 3001 --out /tmp/hh_f1_unique.json
```

부모 external_rates/의두JSON은sealedZIP의동명JSON과내용이같으며Git에서는compact직렬화다. source_file/license/ref의상대경로는전체ZIP root 기준이다. 실제consumer Rust adapter로간주하지않는다. 모든numericresponse admission=false, field presence는source승인이아니다.

Grackle3.4.1 k57원함수의18회가벼운C호출과14온도직접식대조(max0ULP),80자리정확decimal모형구간,22개표시데이터와6개모형비를제공했다. 전체Grackle table/solver/history는실행하지않았다. 3000K floor1e-20과오른쪽극한2.557625796333375e-36cm^3/s의비는3.909876110233189e15이다. 경계포함구간은조각별로반환하고global smooth derivative를거절한다.

정확한십진식k=A exp(p lnT-B/T)의도함수는k'=k(p/T+B/T^2), k''=k[p(p-1)/T^2+2B(p-1)/T^3+B^2/T^4]이다. directed Decimal연산과명세상correctly-rounded exp/ln의인접표현값으로외포를구성한다. empirical rate오차와compiled libm enclosure는포함하지않는다. LCS/KS 비는T>3000에서(A_L/A_K)T^-0.3이고10000K에서162.8277018,100000K에서81.6071654다. 그spread는물리적오차상계가아니다.

기존KS92_corrected_Glover15는호환alias로보존했지만canonical식은Glover2015 Eq14의Kunc&Soon1991 corrected-threshold식이다. 원paper비교는PDF parsed text이며screenshot은cache miss; paperbyteshash는미확보다. 원Grackle3.4.1 C/Fortran/macro/license를ZIP에고정했다. R=k*nHI^2,추가1/2없음,nu=(-1,+1,0,+1),열/결합energy는같은R에-chi/+chi를곱한다. chi와T/n/z/SED/budget/domain/owner는소비자가결정해야한다.15개미확정field를null로유지했다.

전체package: WU088_HH_FAST_F1_DELIVERY_20261004_v1.zip
bytes=108353
SHA256=cf4d5ce5e217f397e8e1a23f33943c5e0aa751eb21f967b9c32bc73d28d4657f
Drive ID=1G8Mz3fP54cNYZQg3heaIvHVo4JTosz_f
Drive parent=1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM
Dropbox directory=/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/

Codex는기존cache또는위Drive/Dropbox중한곳에서직접회수하고SHA/size/verify_delivery.py로검증한다.사용자재업로드를요구하지않는다.48payload에source9개,일반증명,23검사원로그,원C추출/비교재현기,공통schema에맞는RESULT.json이있다.새원격ACK는별도deliveryreceipt를참조한다.

다음최소작업은rei소유REI-F07의등록된domain/observable budget회수다.현재확인한rei HEAD4af2912ce73fdb1240db74d420a0a48fe686af0b의지정model-lock/scenario경로는404다.없는입력을toyfixture로대체하지않는다.그receipt가오면HH-F1을결속하고HH-F2를실제consumer path에연결한다.HH-F3는REI-F09단일paired결과만해석한다. 여기서Bianchi/history/새Rustsolver는작성하지않는다.

Legacy FD2후보유한/107완료/overlap RETURN을읽었으며재실행하지않았다.24/289,미상계265,epsilon null,B22 OPEN,consumed원scope와scienceDB를보존했다.새HHfield/적분/NCP/history0회,기존suite재실행0회다. 같은현재branch의additive작업이며mainmerge/새branch/다른repo수정은없다. 차후감도가요구할때만legacy를제한재개한다.
