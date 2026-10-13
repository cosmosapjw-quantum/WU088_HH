# PHYS25: S65 원식 복원과 생략 vertex의 문턱 효과

PHYS24 백업/게시 완료 후 수행한 다음 이론 루프. 범위: Sheldon1965 NASA TN D-3134의 고전 궤적/sudden/product-state/plane-wave 모형. 교정된 물리적 H–H 단면적 오차범위를 채택한 것으로 기록하지 않는다.

## 새 결과

원 S65 식(2)–(18)을 실제 PDF 페이지로 복원했다. e=E_CM/I_Ry=2에서 singlet/triplet/비편극 단면적은 각각 3.1997029963,1.27774981255,1.75823810849 a0²로 원 Fig3의 규모를 재현한다.

같은 tagged-electron 직접 모형에서 생략한 I2−I5를 p=0에서 정확히 적분했다. C0(R)=exp(−R)(7/18−11/(27R))+exp(−2R)(1/9+11/(27R)). 원 vertex S=(1+1/R)exp(−2R)를 S−C0로 바꾼 선도 문턱 계수는 비편극에서 6.16620545974917→4.08770211160421, 비율 0.662920192699918이다. 이 33.70798% 변화는 같은 모형의 생략 근사 효과이며 유한 에너지 전 구간의 보정배수로 쓰지 않았다.

원 S65 식의 I_Ry..2I_Ry 부분 Maxwell 적분은 T=49999.63846..50000.36154K 전체에서 [1.1658244,1.1731356]e−11 cm³/s에 포함된다. 50000K 점값은1.1694741862013453e−11이며, 부모의 LCS 전체 rate 값의52.56283411배다. Tagged single-electron 모형에서 sigma_event=2sigma_tag인 대칭적인 배타적 가지 adapter를 명시하여 k=<sigma_tag v>를 사용한다.

구간밖 sigma를0으로 놓은 *별도 근문턱-전용 진단*의 warm P01 유한 효과: ΔT∈[−3.078070,−2.922760]e−9K, Δe∈[3.986960,4.367310]e−14/H, Δtau∈[2.359815,2.584956]e−21. 실제 전체 rate의 tail은 미결 입력으로 남아 있다.

## 증거

- Wolfram15.0.1 + 실제 xTensor1.3.0: tensor2, scalar15 잔차가0.
- 별도 Python 직접 적분/미분/유리수 비교71개 PASS. 같은 assistant의 다른 경로이며 외부심사 없음.
- 512 양의 에너지 bin, spin별128구간 도함수 양성, 명시 E1급수 tail.
- 복원 계수는 유한 E1/지수 moment 폐쇄식으로 별도 interval 검증.
- 새로운 ODE/native receiver/ab-initio 산란/HPC 실행은0회. 역사적 원자모형의 기호·수치 적분은 실제 실행.

보고서: report/REPORT_KO.pdf, LaTeX: report/REPORT_KO.tex. 실제 결과와 exact rational endpoints: results/. 재현 계약: REPRODUCE.md. 다음 실행: HANDOFF_KO.md.
