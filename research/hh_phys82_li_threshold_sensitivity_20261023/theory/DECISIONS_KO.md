# PHYS82 이론 선택과 검증 계약

## 선택한 구성

실제 부모 PHYS81은 Li7 threshold-to-6-eV source/uncertainty를 다음 원자물리 작업으로 지정했다. 공개 primary source를 조사해 Zapesochnyi–Aleksakhin1969의 resolved linear slope를 확보하고, Wannier의 엄밀한 문턱 극한과 구별했다. 이번 독립 단원은 이 source-gap의 양의 조건부 함수족, 정확한 Maxwell 적분, 고정 노출량 민감도를 닫는다. 실제 물리 단면적 전체의 신뢰구간을 닫는 단원으로 바꾸지 않는다.

네 matched 모델은 CCC sigma(6eV)를 보존한다. 실험 slope comparator ZA1969는 I를 부모 Li7 chemical defect로 재중심화한 모델로 명시한다. 실험 beam spread와 energy-axis 오차는 physical I의 오차가 아니다. ZA를 endpoint에 재정규화하면 독립 기울기 비교의 의미가 없어지므로 그렇게 하지 않는다. IAEA/Bell, ADAS, Younger 등의 대안은 근거와 source coverage가 달라 미활성화 상태로 보존한다. 원문 PDF/ADAS 원자료는 private evidence backup, 작은 유도 계약은 공개 PR에 남긴다.

## 계산을 단순화한 물리 구조

stationary-target electron Maxwell kernel의 E factor와 q=1 단면적의 1/E가 상쇄된다. q=0도 양의 finite moments 세 개만 있으면 rate, 반응 가중 평균 에너지 및 exact T derivative가 동시에 나온다. 런타임의 매 적분마다 adaptive quadrature를 부르지 않는다. 이 구조적 절감에 별도의 wall-time speedup 수치를 붙이지 않는다. 양의 small-z 급수와 logaddexp를 사용하며 오차 판정은 독립 quadrature와 PL identity로 한다.

thermal pool 사건 회계는 -mu+(mu-I)=-I이다. mu는 선택된 incoming 전자의 평균 에너지로 rate derivative와 source bias를 설명한다. Outgoing 입자들이 동일 열 저장소에 들어온다는 가정과 finite rate의 stationary-target convention을 혼동하지 않는다.

## 유한한 과학 설계

255–50000 K의 65점 geometric grid와 부모의 9개 저장 Li 온도를 합친다. 중복 endpoint를 제거한 72개 T다. 기존 9개 baseline은 그대로 복사하고 63개 새 T만 보존된 finite operator로 계산한다. 5개 새 gap model은 360행이다. 외부에서 지정한 Lambda=1e9,1e11,1e13 cm^-3 s 각각에서 총1080개 확률 진단을 만든다. ODE0, benchmark0, 기존 완료 identity 재실행0을 목표로 고정한다.

노출량은 실험 설계 변수이며 실제 Bianchi 궤적의 전자 밀도 적분으로부터 얻었다고 해석하지 않는다. DeltaP=exp(-Lambda Ktab)[1-exp(-Lambda Kg)]는 같은 prescribed T/ne에서 정확하다. coupled T/xe의 경계는 도출하지 않았다. 저온 rate 비율이 커져도 두 rate가 지수적으로 작아져 유한 노출량의 절대 DeltaP는 0으로 간다.

## 열린 문제와 no-go 심사

물리적 저온 coverage가 열려 있는 이유는 실험 response/deconvolution, isotope/target-state specificity 및 pointwise covariance가 확보되지 않았기 때문이다. 기존 증거만으로 confidence band를 선언하지 않는다. 이 증거 부족을 물리적 불가능성 정리로 주장하지 않으며 strong no-go 판정은 발행하지 않는다.

원문 0.1eV final beam spread와 0.1–0.2eV energy-axis uncertainty가 gap 폭 약0.608eV에 비해 작지 않다는 사실은 이후 forward-convolved 비교 설계를 요구한다. 그 모델의 energy response를 원문 없이 임의 Gaussian으로 고정하지 않는다. Finite gap 모델 민감도 결과를 우선 제공하고 He/Li CX·CE cooling·nuclear thermal-fast ownership의 별도 의무는 DAG에 남긴다.

## 검증 게이트

CONTRACT.json에 코드/과학 실행 전에 고정한 허용치: gamma-free independent integral 및 PL identity 상대1e-10, derivative scaled relative1e-7. T=255,777,3200,11000,25370.66308424773,50000K를 사용한다. 근처 derivative0에는 scale-aware 판정을 한다. Source 정확도는 이 수치 일치와 별개의 열린 항목이다. Wolfram 네 residual0은 symbolic identity 점검이며 floating-point 구현 인증서가 아니다.
