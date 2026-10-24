# Wolfram 미단순화 항의 양의 branch 증명

두 번째 실제 Wolfram 출력은13개 잔차 group 중12개, scalar18개를 정확히0으로 반환했다. COM inverse 식은 radical expression으로 남았고 all_zero는False였다. 이를19개 모두0이라는 출력으로 바꾸지 않는다. 최초 JSON exporter 실패는 이 비숫자 식과 조건부 predicate를 JSON으로 내보내려던 단계에서 발생했다.

양수 입력 a,b,h,E_S에서 M_S=a+h>0, M_b=a+b>0이고 K=sqrt(M_S²+2hE_S)−M_S>0이다. E_b=K(2M_b+K)/(2b)를 대입하면 M_b²+2bE_b=(M_b+K)²이다. M_b+K>0이므로 principal square root는 정확히 M_b+K다. 따라서 recovered K_b=K이며 K(2M_S+K)=2hE_S로부터 recovered E_S=E_S다. 빼기 cancellation을 피하는 구현식2hE_S/(sqrt(M_S²+2hE_S)+M_S)는 같은 양의 K다.

Wolfram의 monotone predicate h+sqrt((a+b)²+2bE_b)>b는 같은 양수 조건에서 sqrt((a+b)²+2bE_b)>a+b>b이므로 성립한다. 미분식 dE_S/dE_b=bW_S/(hW_b)>0도 분자·분모가 모두양수다.

이는 원 모델/도메인을 바꾸지 않는 수작업 항등식 증명이며 추가 evaluator를 쓰지 않는다. 본 미단순화 항을 numerical failure 또는 physical uncertainty로 해석하지 않는다. 정확한 nominal 분해는 Q차81.63eV=binding shift0.003700036867eV+convention residual차81.626299963133eV다.
