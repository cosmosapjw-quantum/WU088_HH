# HH-TH01: 대칭·문턱 민감도·rank-one HH 근 인증

판정: SYMMETRY_REGULARITY_AND_RANK_ONE_SOURCE_THEORY_DERIVED__ACTUAL_CERTIFICATES_OPEN.

사용자 요청에 따라 미해결 이론을 진행했다. 새 이력이나 production 코드를 만들지 않았다. 전체 유도·정리의 가정·quadratic-HH 반례·검산 script·원 로그·4개 선택 입력·claim ledger/DAG는 sealed ZIP에 있다. Git의 문서는 검색용 요약이며 ZIP 상세 THEORY/REPORT와 byte 동일하지 않다.

## 새 결론

H_i=H(1+epsilon,1-epsilon,1)에서 초기자료/birth/source/evolution이 정확한 x/y 교환에 대해 equivariant이고 해가 유일하면 scalar O(epsilon,lambda), HH shift D, 이중차이 A는 epsilon의 짝함수다. lambda는 단일 선택 HH율의 수학적 homotopy이며 LCS/KS 혼합이나 물리오차 분포가 아니다. O_lambda_epsilon_epsilon가 전체 parameter rectangle에서 bounded/continuous일 때만 |A|<=lambda*epsilon^2*M/2를 얻는다. 짝함수라는 이유만으로 이차 억제를 선언하지 않는다.

동일 두 photo beam의 cutoff가 관측시각에 합쳐지는 isothermal quadratic-HH reduction에서 A=(kappa*t0/2)*D(0,lambda)*abs(epsilon)+O(epsilon^2)를 정확히 유도했다. S0 history에서 이 cusp를 관측했다는 뜻은 아니다. Local binary64 방향+exact-decimal H/E의 새 epsilon-root 진단에서는 실제 S0 birth6.5e10/7e10의 fit crossing이 epsilon약.0049173/.0053812에서 종료시각8e11s를 넘는다. 전체0..0.01의 동일eventbranch를 가정할 근거가 없다. Numerical root이며 interval 인증은 아니다.

13.6eV fit cutoff는 실제 photo source jump지만, retained photons가 이미 비흡수인 13.598434599702eV binding 경계에는 두 번째 physical jump가 없다. 개별 event에서 z_epsilon^+=z_epsilon^- -DeltaF*tau_epsilon, tau_lambda=0이면 z_lambda는 연속이다. 그러나 mixed jump는 -D_zDeltaF*z_lambda*tau_epsilon로 남을 수 있다. 동시에 여러 guard를 지나면 개별 saltation을 arbitrary order로 곱해 하나의 C2 Hessian이라 하지 않는다.

네 gas 좌표(h,y1,y2,w_eV/H)의 HH q=nH(1-h)^2 k(Cw/Pi)에 대해 1/ne나1/(1-h) 없는 gradient/Hessian을 완결했다. J_HH=c grad(q)^T는rank<=1이며c=(1,0,0,-chi)다. Reduced BE에서 M_lambda=M0-dt*lambda*c*grad(q)^T이므로 determinant 분모d=1-dt*lambda*grad(q)^T*M0^-1*c가 중요하다. M0는 같은 ONcandidate에서의 baseline derivative다. HH-only 소산성이 있어도 결합 행렬이 singular인 정확한2x2반례를 얻었다. 새 physical box의 center residual/self-map/contraction을 함께 인증해야 한다.

이상적인4x8방향 규칙은S0 x/yparity를 보존하지만 M2=diag(11/32,11/32,5/16)으로 완전 등방이 아니다. S0 fourth moment137/512와 구면4/15의 상대차7/2048은 HH관측량 오차가 아니다. 원binary64방향을 수정하거나 대칭화하지 않았다. Actual native parity는 미검증이다.

## 실제 검산과 입력 구분

proof script1회에서61symbolic identities/8exact assertions/새shear-parameter root4개 확인,exit0,stderr0byte. 자동 정리증명이나 production tests가 아니다. Native/Rustcompile/BEroot/time-stepper/ODE/oldscience/fullF08-F09실행0. 제3자독립review없음. 실제globaltube/continuouserror/physicalerror/rootbox 인증은OPEN.

HH source-read7495a89aa843e90be6351f2bd285993682717260의새coarse/fineON05B를수신했다. 그413950057-bytefullZIP과첨부153023575-byteZIP은다르다. 원격결과를재실행하지않았고이번선택4개입력은첨부스냅샷manifest/hash와대조했다. REI756e1d4f833a1eec454e660b340d3424f3e5d768의별도angular-block이론/BIraw요청도수신했지만HHcohort의인증으로전용하지않았다.

## 전체 패키지

WU088_HH_TH01_SYMMETRY_HYBRID_ROOT_20261005_v1.zip
55295bytes,23entries/22payloads
SHA256 e85ad9e79658d9ea150c1583463828bb76184fc6263419b72c8526f0b6638ba6
Drive18NbePt3EypI5l3PCWmhUjGOEZT3jqoT1, parent1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM
Dropbox id:BSpOijBcT10AAAAAADzbgQ, 기존HH폴더. 양쪽완료ID/name/size확인,R1이며새outputremote fullrestore=false.

다음에는 THEORY§7-9의 HH J/H와 새 ON root box 조건을 실제 ON06에 결속한다. 오차이론은 event-sector/incomingerror/차이residual을 유지한다. 기존S0OFFcontrol/criteria/legacy24/289·265unbounded·epsilon_C/Rnull·B22OPEN·consumedscopes를 보존한다. 새 activation승인을 묻지 않는다. 같은branch append-only/nonforce,PR33/REIPR83.
