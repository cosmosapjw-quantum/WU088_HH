# R14 구성 선택과 실행 DAG

## 선택을 판별한 작은 구성

\(P(x)=\int_0^x(s-1/4)^2ds=x^3/3-x^2/4+x/16\)는 비음수·비감소이지만 B3 coefficients는\((0,1/48,-1/24,7/48)\)이다. 따라서 R13의 monotone quadratic lemma를 cubic으로 자동 옮기는 후보는 이 중간 추론에서 실패한다. 이것은 그 특정 lemma의 반례이며 연구 전체의 no-go가 아니다.

원래 source의 두 quadratic vertices를 exact union하면 각 effective source의 coefficients가 비음수다. 각 overlap의 선형 길이와 exact Simpson bracket을 곱하면 positive B3가 직접 나온다. 이 방식은 scalar polynomial의 단순 monotonicity에 기대지 않고 source provenance와 integral 자체에 연결된다.

| 후보 | 판별과 선택 |
|---|---|
| 원래 B2 coefficients 모두 비음수인 cone만 받기 | 구현은 간단하지만 valid negative middle 입력을 제외한다. 정확한 vertex split의 최대3배 finite 비용으로 full nonnegative quadratic cone을 받기로 했다. |
| Cubic critical roots를 algebraic E time knots로 삽입 | 새 algebraic time arithmetic이 필요하다. Whole-R용 rational boxes만 사용하고 E rational base clock을 유지했다. |
| Whole interval의 균일 subdivision tree | 일반화 가능하나 quadratic derivative의 최대2roots 구조를 활용하지 못한다. Rational derivative vertex와96 bisections를 선택했다. |
| Signed monomial production E | 수학적으로 동등하나 cancellation을 포함한다. Production은 positive B3 beta/reversal, reference는 독립 monomial phi4로 분리했다. |

## 각 구조가 실제 쓰이는 위치

Original source vertex는 positive coefficient 확보와 finite Neffective bound에 쓰인다. Translated grid는 overlap max/min branch를 고정한다. Stored cubic은 endpoint/F/left limit/critical/rootbox/whole outputs의 유일한 convolution 데이터다. Derivative vertex는 root uniqueness를, de Casteljau는 positive restriction과 sup gap의 chain factor를 제공한다. Beta weights는 signed scalar E enclosure를 제공하며 global memory는 원래 t0에 유지된다.

## 실행 DAG와 자원 계약

Theory 및 literature 저자와 production/primary 저자, standalone reference 저자 및 independent reviewer를 분리했다. Reference 저자는 새 production source를 읽지 않고 API와 고정 inputs로 작성했다. 독립 reviewer는 proof/core/reference를 작성하지 않았다. Root가 source/input/명령을 동결하고 실제primary1회, savedprimary를읽는reference1회,새CAS1회만실행한다.

Primary/reference 각각 CPU90초, wall120초, AS1GiB. CAS tool constraint30초와내부TimeConstrained25초. 실제childprocess CPU는imports와serialization을포함하여측정한다. 완료한R13/이전과학·심사·ODE는재실행하지않는다. 모든old allowance증가0이고globalremaining/fullhistoricalCPU는null이다.

Original source≤16, observations≤32, effective≤48, fullblocks≤8,base≤512. Full combination precharge≤221184<250000이고rootbisections≤98304이다. Code의직접workhelper경계검사와실제로도달한fixturework를구별한다. Bit guards 및 문자열문법/유한6000digits는별도한계다. Runtime값을미리PASS로예측하지않는다.

Science가끝난뒤savedoutput만으로2개그림의PNG/SVG를생성하고실제확인한다. 그림process는별도CPU10/wall30/AS1GiB이며solver호출0이다. Endpointconnector는display이며whole-cellcertificate는별도구간표시다.

## 완료 기준

실제31valid/46guard 결과와독립reference의모든비교·coverage·sourceidentity,32개CASidentity의실제출력및모든메시지를기록한다. 과학채택은새R6/C9닫힘과실행근거가있을때만한다. Published/backupACK는각stage후실제provider응답으로표시한다. 이문서는아직실행결과가아니다.
