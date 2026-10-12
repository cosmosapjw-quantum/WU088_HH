# PHYS14 필수 작은 의미 검산

2026-10-12 12:49:42 UTC 실행. 후보 이론 작성자가 남아 있던 두 종류의 의미 검산을 수행했다. 최종 독립 판정과 별도의 검증 증거다. 원 PHYS14 `main`, 실제 history 계산 및 과거 과학 suite는 호출하지 않았다. 새 물리 case 수는 0이다.

## 1. Directed dyadic rounding

`phys14_advance.py::dyadic`의 256 significant binary bits 반올림을, binade를 입력 구성에서 알고 있는 별도 유리수 oracle과 비교했다. Oracle은 양의 magnitude에 Euclidean quotient/remainder를 적용한 뒤 음수의 하향·상향을 교환한다. 후보의 `bit_length` exponent 추정 로직을 복제하지 않는다.

- 9종 normalized mantissa, 17개 binade exponent, 양·음 두 부호의 306개 입력을 확인했다.
- 지수는 −16384에서 +16384까지이며 −1075·−1074 등 binary64 subnormal 경계도 포함한다.
- 반올림 끝점의 정확한 oracle 일치, 원 유리수 포함, 부호 보존, 이미 반올림한 끝점의 멱등성을 확인했다.
- 별도로 `2^(-100000)` 규모의 양·음·영 교차 interval을 확인했다. 이 지수에서 signed tail도 보존된다.
- 영을 포함한 divisor 네 형태의 거절, ±4096 지수차를 가진 interval의 곱·몫 포함을 확인했다.

## 2. Closed-form implicit gas/photon oracle

한 gas unknown과 한 photon group에 대해

\[
x=r(\lambda,b)+\gamma\lambda(1-\beta x)
+N(\lambda,b)\frac{1-x}{4-x},\qquad
N^+=\frac{3N}{4-x}
\]

를 썼다. \(\gamma=1/20\), \(\beta=0,1\) 두 변형이며, 평가점은 \((\lambda,b)=(1/3,2/5)\)다. 이전 gas와 photon의 두 일차 미분 및 mixed derivative가 모두 비영인 bilinear 함수를 입력으로 선택했다. 두 변형 모두 평가점의 작은 근이 \(x=1/2\)가 되도록 기존 gas 값을 고정했다.

\(B=1+\gamma\beta\lambda\), \(c=r+\gamma\lambda\), \(L=4B+c+N\), \(C=4c+N\)라 하면

\[
x=\frac{L-\sqrt{L^2-4BC}}{2B}
\]

가 국소 analytic branch다. 이 closed form을 \(\varepsilon^2=\eta^2=0\)인 유리수 다항식 대수에서 계산했다. 양의 rational-square 상수항에 대해 binomial expansion으로 square root를 계산하므로 유한차분·수치 미분을 사용하지 않는다. 그 결과 원 implicit residual의 네 다항식 계수가 정확히 0이고, 같은 근의 \(U,V,W\)와 photon quotient의 혼합계수를 정확한 유리수로 얻는다.

이 독립 closed-form 결과를 PHYS14 체인룰과 비교했다. 이전 gas의 mixed carry, gas Hessian, 두 방향 gas/photon 교차항, incoming photon mixed carry가 모두 비영이며 각 항 하나를 누락하면 oracle의 정확한 답과 달라진다. Photon mixed quotient도 다섯 항을 각각 누락하는 오류를 구분한다.

실제 후보의 `Source.evaluate`, `contraction`, `neumann`, `outgoing_carry`는 synthetic 한-unknown fixture에서 호출했다. 후보의 기본 Neumann degree 8과 원 256-bit dyadic 연산을 사용한 포함이 closed-form \(U,V,W\), outgoing photon 및 absorption의 네 성분을 모두 포함한다. 후보 평가 함수의 lambda box는 원 구현대로 `[0,1]`을 유지하므로 해당 포함과 국소 평가점의 exact oracle equality를 구분한다.

## 3. 실제 실행 기록

`PROSPECTIVE_CONTRACT.json`을 실행 전에 기록했고, `FIRST_CLAIM`의 create-only 표시 뒤 한 번 실행했다. 예산은 wall/CPU 30초, address space 256 MiB다.

- 종료: exit 0, `PASS`.
- 전체 process wall: 0.164559초.
- CPU: user 0.106012초 + system 0.008388초.
- 최대 RSS: 14,464 KiB.
- 내부 oracle 계산: 0.073315초.
- 원 후보 코드 SHA256: `d20d9797278b8da71d38a3db229325dc7792d3991863f07bcdb7f72f2ba5567a`.
- Oracle 코드 SHA256: `b28b5e69c2108fd970b861a06e649cdcc947081332ccc77312e2d3e3078a2ff7`.
- 결과 SHA256: `738a9eaffe4672f2fbc0b3cc0ac27d43693168c988deb0599ec6095132ab0c40`.

원 후보 파일은 실행 전후 byte-identical이다. 결과는 `ORACLE_RESULTS.json`, process 기록은 `EXECUTION.json`, 원 stdout/stderr는 각각 `stdout.txt`, `stderr.txt`에 있다. 두 검산 종류와 두 quadratic 변형을 과학 history 실행 수에 더하지 않는다.
