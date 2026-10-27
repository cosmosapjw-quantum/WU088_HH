# R4 구성 후보와 판별 예제

## 선택한 질문
저장된 R8의 동일 family/state/clock 커널과 계수만으로, 초기 전체 궤도 envelope 없이 현재 셀의 R–E 결합을 닫을 수 있는가? 각 셀의 실제 supremum에 대한 두 부등식을 양의 역행렬로 푸는 구성을 선택했다.

## 세 계산 후보
1. Raw causal solve: D=1−δa−δbφc>0이면 R*=(A+δbB)/D, E*=B+φcR*. 완료된 셀의 상계만 다음 셀의 forcing에 전달한다. 선행 전체 envelope는 필요 없다.
2. Certified intersection: 같은 닫힌 셀의 R8 whole cap과 raw 결과의 성분별 min을 다음 셀에 전달한다. 끝점은 raw endpoint, 현재 whole bound, 동일 시각의 R8 point cap을 교차한다. 기존 인증보다 커지지 않는다는 보장이 있다.
3. 추가 global Picard passes: 기존 전체 envelope를 출발점으로 재차 적분한다. 별도 반복 예산과 종료 규칙을 필요로 하므로 이번에는 실행하지 않는다. raw와 capped의 차이는 각각 실제 출력에 남긴다.

## 대표적인 결합 예제의 직접 계산
δ=φ=1, a=0, b=1/2, c=1/4, A=1, B=0이면 D=7/8이다.
따라서 R*=8/7, E*=2/7이며 R*−E*/2=1, E*−R*/4=0을 정확히 만족한다.
이 유도는 대수 확인이고 실행된 Python 검증은 아니다. 동일 예제를 S06 primary와 독립 reference의 정확한 control로 사용한다.

## 판별력이 있는 경계
- a=999/1000, b=c=0, δ=1, A=1이면 D=1/1000, R*=1000이다. 분모를 위로 반올림하는 오류를 분리한다.
- forcing만 있을 때 현재 셀은 h0=1을 사용한다. 전체 block contraction을 현재 forcing에 곱하면 새 forcing을 과소평가한다.
- d<0과 d>0은 과거 셀 coarse 적분의 최대가 서로 다른 끝점에서 생긴다. 두 분기를 구현한다.
- D≤0은 이 충분조건의 domain rejection이다. 물리 발산 판정으로 해석하지 않는다.
- 저장 trajectory sample은 비교용 관찰이다. whole 또는 point certificate cap으로 사용하지 않는다.

## 실제 출력의 판정
raw와 capped의 R8 대비 우열 및 실제 개선 비율을 따로 보고한다. raw의 보편적 우월성은 전제가 아니다. 식의 유효성과 이번 사례의 유용성을 별도로 판정한다.
