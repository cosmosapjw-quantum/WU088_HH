# R4/C4 유한 구성·자원·판별 계약

## 작업 순서와 실행 권한

Root는 source/expected-SHA/force=false 게시와 provider 저장을 맡는다. 별도 작성자가 production/primary를 구현하고, 이론 작성자는 production을 import하지 않는 J0/J1+monomialphi reference를 작성한다. 다른 검토자가 새로운 R13 증명과 코드의 R6/C9를 맡는다. 현재 skill1.0.0을 사용하며 기존R11/R12 심사는 다시 하지 않는다.

새 primary1회/reference1회는 각각 OS CPU60초·wall90초·address-space1GiB 이내다. run_bounded.py는 frozen fileSHA, exclusive attempt, RLIMIT_CPU/RLIMIT_AS, walltimeout, 실제 stdout/stderr/returncode와RUSAGE_CHILDREN을 기록한다. ScientificCPU는 import/serialization을 포함한 child OSprocess전체다. 이전단위allowance증가0, globalremaining/fullhistoricalCPU=null. ODE/nativegenerator/exponentialsource재실행0.

새CAS1회는 frozen check_affine_moments.wl의25개기호식만평가한다. Wolfram tooltimeConstraint30초와내부TimeConstrained25초를쓴다. 실제제출바이트와반환message를보존한다. Symboliczeros와warning/timeout/unreduced를분리하고원인을확인하지않고단정하지않는다.

## 유한 크기와 선행 작업량

Contract의모든크기조건을동시에적용한다. Basecell수N,sourcecell수Ns,fullblock수B라하면cachedF평가는base끝점N+1개+midpointN개+vertex최대N개이므로최대3N+1개다. Overlapterm상한은(3N+1)*Ns*(B+1)<=200000으로처음overlap계산전에확인한다. 각basecell에는vertex가최대1개이므로최종cell수<=2N이고4096상한을지킨다. 실제Fcall/term수를결과에기록한다. Derivedrationalbitsguard는시간상한과별도로적용한다.

## 실제 판별 질문

| 구성 | 실행 전 수기 기준 | 해소할 위험 |
|---|---|---|
| q=1,gr=s,c=1,d=0,T=1 | R(1)=1/2,E(1)=1/6 | affine forcing과degree2전파 |
| 같은cell상수sup gr=1 | R(1)=1,E(1)=1/2 | ideal함수의forcingmonotonicity |
| q=0,tau=1,삼각gr,T=2 | R(1)=R(2)=1/2,R(3/2)=3/4,E(2)=5/6 | 내부vertex/wholecell |
| q=0,R0=1,gr=1,T=1 | pointR(1)=1,leftlimit2,sup2 | unattainedsupremum과actualendpoint |
| q=1/2,tau=1,gr=1,t=5/4 | F=9/8 | globalmemory보존 |
| signed/nearzero d_c | 독립Decimal160phi,smallargument직접series | cancellation과signreverse |
| source/observation분할변경 | sameidealF/R/E | 정확한refinement과rounding구별 |
| source/clock/certificate/resource오류 | 명시적reject | 잘못된premise/무제한실행방지 |

전문헌의다항forcing지수적분을재사용하고WUstepkernel과vertexrefinement를직접구성한다. 새로운strongno-go는없으며자료접근실패로배제정리를채택하지않는다.
