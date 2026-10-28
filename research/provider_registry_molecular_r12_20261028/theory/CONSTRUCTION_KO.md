# R12 구성 후보와 선택

원 아이디어는 R11의 all-starts full-A step kernel을 보존하면서 source/observation clock 제약을 제거하는 것이다. 두 정확한 표현을 병렬로 구성한다.

1. **양의 overlap 합**: 실제 source interval과 각 age strip의 교집합 길이를 계산한다. 모든 항이 비음수이며 primitive subtraction을 피한다. 생산 경로로 선택한다.
2. **Primitive 차이합**: J(x)=integral_0^max(x,0) h를 exact geometric sum으로 계산하고 source 양끝에서 차분한다. 같은 식을 다른 계산 경로로 확인하므로 독립 reference로 선택한다.
3. **Uniform clock으로 반올림 후 기존 index sum**: q=1/2,tau=1/3,g=1_[0,1/4],t=1/2의 정확값1/6에서 실제 age-strip split이 생긴다. 이번 단위는 그 clock 변경의 오차를 도입하지 않고 실제 translated knots를 사용한다.

원 forcing history는 source partition에 있고 observation은 출력 위치만 정한다. 닫힌 셀 cap이 추가되면 cap grid도 event union에 포함한다. 원 endpoint caps는 정확히 일치하는 point에서만 사용한다. 이 사상은 서로 다른 clock을 같은 인덱스로 다루는 구현 결함을 구체적인 interval inclusion으로 교정한다.

코드 DAG는 exact parser/source identity → event union/coverage → exact overlap F/R → signed positive scalar weights → raw/capped subcells → requested point/closed-cell aggregation이다. 계산은 단일 bounded Python pass이고 independent reference는 별도 파일·다른수식으로구성한다. BITS128/Taylor96은 그대로 유지하고, 추가 자원은 CONTRACT의 primary1/reference1/CAS1뿐이다. 의미 있는 새로운 endpoint 개선을 사전 수용 조건으로 강요하지 않는다.
