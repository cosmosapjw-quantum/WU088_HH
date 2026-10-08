# HH-F1R: 로그온도 source jet와 엄밀한 상태 구간 Taylor 상계

상태는 SOURCE_JET_AND_TAYLOR_BOUND_VERIFIED__WAITING_ON_REI_DOMAIN이다. 새26개 검사(기록된RED/GREEN6+후속회귀20)를 통과했다. 이것은 HH-F1 전체 physical admission이나 HH-F2 소비자 port가 아니다. 기존 F1의 두 named fit과 hh_external.py bytes를 그대로 사용한다. 정확한 재현 명령은 이 디렉터리에서 다음과 같다.

```sh
python3 -B -m unittest discover -s tests -v
python3 -B src/hh_source_jet.py --provider LCS91 --T 10000 --n 2 --chi 3e-18 --dy 0.01 --dn 0.02 --out /tmp/hh_f1r_NEW.json
```

CLI는 표준라이브러리만 사용한다. 검사는 requirements-tests.txt의 mpmath/sympy가 필요하다. 예시는 manufactured 입력이며 물리 domain과 chi를 채택하는 명령이 아니다. 같은 출력 경로를 덮어쓰지 않는다. 이미 완료되고 source가 같은 과거 F1/FD2/NCP suite는 반복하지 않는다.

## 새 결과와 증명 요약

y=ln(T/Tref),x=B/T에서 D_y x=-x이고 k=A*T_K^p*exp(-B_K/T_K)이다. K_j=D_y^j k=kP_j로 두면 P_(j+1)=(p+x)P_j-xP_j'이므로 P1=p+x, P2=p²+(2p-1)x+x², P3=p³+(3p²-3p+1)x+(3p-3)x²+x³이다. 두 p>1에서 계수가 비음성이며, k와 x의 구간 다항식으로 각K_j를 외포한다. 이 사실이 K_j의 전역 T단조성을 뜻하지는 않는다.

R=n²k의 미분은 R_n=2nk,R_y=n²K1,R_nn=2k,R_ny=2nK1,R_yy=n²K2,R_nnn=0,R_nny=2K1,R_nyy=2nK2,R_yyy=n²K3이다. n으로 나누지 않아 n=0에서도 정의된다.

한 smooth branch 안의 n(s)=n0+s*dn,T(s)=T0*exp(s*dy),0<=s<=1에서 g(s)=R(n(s),T(s))라 하자. n0>=0,n0+dn>=0과 nmax>=sup n(s),Kjmax>=sup |K_j|이면

g^(3)=6dn²dyK1+6n*dn*dy²K2+n²dy³K3.

g(1)-P2=(1/2) integral_0^1 (1-s)²g^(3)(s)ds이므로

|g(1)-P2| <= |dn|²|dy|K1max+nmax|dn||dy|²K2max+nmax²|dy|³K3max/6.

P2는 기준점의 gradient/Hessian으로 계산한다. 코드가 P2를 outward interval로 계산하고 위 remainder를 추가하므로 계수반올림도 별도로 포함한다. 직접 endpoint의 image를 제공하되 둘을 교집합으로 줄여 결과를 숨기지 않는다. 이것은 state-segment source근사이고 time update/ODE local error/전체REIresidual의 인증이 아니다. dn에는밀도단위,dy에는차원이없고 remainder단위는m^-3s^-1이다.

LCS3000K에 닿거나 관통하면 global smooth jet=null이며 source Taylor는 거절한다. Branch별 one-sided 자료는 남긴다. KS에 cutoff를추가하지않는다. floor내부 또는dy=0이면절단나머지0이지만평가반올림구간은남는다. 모든종source와열/결합에너지는 같은event변수와오차를공유하고보존계수부터수축한다. 소비자의chi는fixedparameter이며불확실/상태의존이면추가항이필요하다.

18개 상태구간을130-working-digit독립계산과대조했다. 최대관측오차/상계=.9924614091949121이고이는 유한사례관측이다. 일반상계의근거는위증명이다. mpmath의workingdigits,fit수치외포,empirical물리오차,독립과학심사를구분한다.

## Cloud-first 전체 원자료

- name: WU088_HH_FAST_F1R_DELIVERY_20261004_v1.zip
- bytes: 130243
- SHA256: 1ffc7930d18fb9fec7d515b9e3d3058b2f4b3cc1081880b4a0720745f994ea65
- Drive ID: 1qWkkWEe7Siq3aWmZE4xSwnFDxieF2aRd
- Dropbox ID: id:BSpOijBcT10AAAAAADx6DQ
- Drive parent: 1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM
- Dropbox parent: /BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/

이미 검증된 cache가 없을 때만 한 provider에서 bytes를 회수한다. 사용자 재업로드를 요구하지 않는다. 전체58개 payload,CRC,원source19개를검증했다. Git에는reference와전체26개검사가있고,전체증명/계약/측정자료/원실패로그는ZIP에있다. OUTPUT RESTORE_VERIFIED=false다. 최종 게시/보고서/receipt백업은 detached receipt가권위다.

## 다음 단계

최신 rei_bianchi successor의 REI-F07 domain/observable/constant/단일owner/actualcoordinate를 먼저 읽어라. 관측commit18708555beae91f577181f54eb68f962656836b1의 FT01은 합성 T-independent ODE연구이며 canonical tasks를닫지않았다. 그4800~36000K범위를물리domain으로가져오지않는다. 지정된science_scenario/model_lock은그commit에서404였다. 없는15개consumerfield를임의로채우지않는다.

현재jets는 REIFT02/FT04의선행provider자료로쓰되, actual residualchainrule과Rustcompilerparity는consumer가구현한다. HHrepo에는원자rate자료만두고Bianchi/thermalODE/history를복제하지않는다. REI-F09가유일pairedhistory실행자이며HH-F3는그결과를읽는다. 기존24/289,265unbounded,epsilon_C/Rnull,B22OPEN과소비scope를유지하고legacy적분으로되돌아가지않는다. 동일branchadditive/nonforce게시와기존Drive/Dropboxcreate-only백업을유지한다.
