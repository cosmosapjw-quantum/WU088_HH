# R4 R3/C3 독립 정적 설계 검토

판정은 **PASS_SCOPED_STATIC_DESIGN**이며 blocking finding은 없습니다. 이 판정은 설계·원식·거절 조건의 정적 일치에 한정됩니다. 여섯 새 열의 실제 출력, 29개 식 평가의 수치 오차, 최종 C9 판정은 아직 검사하지 않았습니다.

## 읽은 권위와 입력

로컬 HEAD는 **e9276ea2ba8af2d73197a6852931fcafbf39ddf5**입니다. 최신 R4 AGENTS prefix, 고정 CONTRACT, source packet **40e2fbd7…**, source review의 복구 영수증과 S02 전달 기록을 읽었습니다. S02의 실제 source ZIP은 427,248 bytes, SHA256 **91d94753261582fcf03d9f1ef6056c1cd3de180326fb0c608c07776d9adf816f**입니다. 양쪽 업로드 완료와 최종 전체 source byte readback을 구분합니다.

설계 파일은 **5ec65638…**, 모듈은 **c11bd724…**, CLAIM_ALIGNMENT는 **85d105f3…**에 고정했습니다. 전체 해시는 같은 이름의 JSON에 있습니다. 과거 source review는 독립 검토 완료 보고에서 복구된 영수증이며, 원래 review 파일의 정확한 bytes가 없다는 한계를 유지합니다. 이번 검토자가 raw 논문을 새로 전수 대조했다고 주장하지 않습니다.

Root가 알려 준 REC **09b2230c7735496ccf1516fb8d26e5f854fe203d**의 실제 commit metadata도 읽었습니다. 변경은 CODING_BASELINE, R10 전달 영수증, C1 stage의 세 파일입니다. 이 최신 commit에는 새로운 화학 형성 공급자나 소비자 구현이 없습니다. 전체 조상 diff를 새로 조사한 결과라고 확대하지 않습니다. S03 게시 직전의 선택 HEAD 갱신과 actual receipt는 root가 별도로 남깁니다.

## 정적 검토 결과

Bennett 경로는 원문의 다음 식을 구현합니다. T는 K, 계수의 단위는 cm³ s⁻¹입니다.

\[
k=10^{-20}\left[3.22+\left(0.0657(T/1000)^{-2.45}
+0.00631(T/1000)^{0.837}\right)^{-1}\right].
\]

GL2022는 \(\alpha\exp(-\gamma/T)\)이며 gamma의 단위 K와 음의 지수 부호가 맞습니다. 두 경로는 각각 27개와 2개의 고정 원문 온도만 허용하고, 반환을 **SOURCE_FORMULA_SAMPLE**로 한정합니다. Bovino의 인쇄된 b 단위 문제를 조용히 수정하거나 평가하지 않습니다.

**exact**는 bool과 binary float를 거절합니다. 비유한·잘못된 문자열, 비양수 온도, 등록되지 않은 온도, 추가 spin 인자, 불명 공급자 및 physical-rate 요청도 거절 경로가 있습니다. TIQM/SQM 동시 선택은 방법 대안의 중복을 막습니다. Bovino ortho/para 동시 선택 거절은 현재 spin-sum convention이 결속되지 않았기 때문이며, 서로 다른 두 최종 spin branch가 같은 물리 채널이라는 뜻은 아닙니다. Registry에는 여섯 비활성 공급자 variant를 모두 보존해야 합니다.

\(X=\sum_i x_i\), \(\sum_i\pi_i=1\)이면 \(r=x-\pi X\)의 합은 0입니다. 모듈의 exact rational 계산은 다음 식과 맞습니다.

\[
J=h\,d^Tx,\qquad J_\pi=h(d^T\pi)X,\qquad
J-J_\pi=h\,d^Tr.
\]

\(c=(d_{\max}+d_{\min})/2\)를 빼면 다음 경계를 얻습니다.

\[
|J-J_\pi|
=|h(d-c\mathbf 1)^Tr|
\le \frac{h(d_{\max}-d_{\min})}{2}\|r\|_1.
\]

차원·정규화·비음성 조건은 코드에서 거절 조건으로 구현되어 있습니다. \(h>0\)에서 모든 허용 \(x\ge0\)에 대한 고정 lift의 균일 scalar closure는 basis-vector 선택으로 \(d\)가 상수인 경우와 동치입니다. \(h=0\), \(x=\pi X\)의 예외와 실제 source의 \(d,\pi\) 미공급을 구분합니다.

서로 다른 입자 두 종류의 조건부 식 \(k\,n_A n_B/n_{\rm ref}\)도 cm 기반 계수·밀도에서 reference nucleus당 proper second의 event 수 차원을 갖습니다. 특정 실제 밀도·clock·consumer를 구성했다는 주장은 없습니다. 원문 fit residual, table rounding, 모델 대안, physical covariance 및 Q는 별도입니다. Fit의 activation parameter를 Q로 읽지 않습니다.

## C7 이후 독립 확인 계획

실제 builder와 출력 schema가 준비되면 다음 변경 부분만 확인합니다.

1. Packet·모듈·compiler/adapter pin과 실제 제한 child 영수증을 대조합니다. 과거 149열, 249검사와 PHYS91은 실행하지 않습니다.
2. 여섯 variant의 77개 원문 coefficient literal·scale·unit·locator 및 null state/Q/covariance를 대조합니다.
3. 여섯 새 열의 각 isotope·baryon·charge·electron-lepton 합을 저장된 species와 event로부터 독립적으로 계산합니다. 열적 물질 입자 변화는 RA −1, 나머지 0으로 따로 확인합니다.
4. 독립 Decimal80 식을 직접 작성합니다. Bennett의 비정수 거듭제곱은 decimal ln/exp로 계산하고 GL2022는 decimal exp를 씁니다. 27+2 노드에서 저장된 binary64 값을 정확하게 읽어 상대차 \(2\times10^{-14}\) 기준을 적용합니다. 생산 코드나 compiler를 참조 계산으로 import하지 않습니다.
5. 저장된 fit값과 exact 원표에서 signed residual을 따로 확인합니다. Source residual이 크면 그대로 보고하며 수용 기준이나 원행을 바꾸지 않습니다.
6. 최소 변경 입력으로 type·domain·spin·방법 중복·state-vector·physical 요청의 거절 경계를 확인합니다. 모듈 호출이 필요하면 system under test로만 사용하며 29개 정상 fit값을 재평가하지 않습니다.
7. 구성된 작은 유리수 예제에서 lift·비영 defect·half-spread 포화·\(h=0\)·constant-d closure를 독립 계산합니다. 이를 실제 상태 인구의 관측으로 표시하지 않습니다.
8. 출력과 후속 admission에서 활성화·physical rate·Q·state-consumer 결속을 승인하지 않는지 확인합니다.

각 child는 30 CPU s, 120 wall s, 512 MiB, 단일 worker/thread로 제한합니다. C7 이전의 수치 실행은 하지 않습니다. 첫 실패와 변경 근거를 보존하고, 구체적 결함이 확인된 부분만 새 attempt로 교정합니다.

## 실행과 판정의 한계

이번 검토는 text/data 읽기와 metadata hash 계산뿐입니다. **생산 코드 import 0, fit 평가 0, compiler 0, 수치 검사 0, 과거 과학 재실행 0, 원격 수정 0**입니다. Source rows, 정수 operator, native 식 구현의 단계별 수용과 실제 소비자 수용은 계속 구분합니다. 수치 결과가 아직 없으므로 최종 C9와 물리적 rate/Q/consumer는 승인하지 않았습니다.

이 설계 검토 이후 작성된 **build_molecular.py**와 실제 registry는 별도의 preexecution/출력 검토 대상입니다. 이 판정에 포함시키지 않았습니다.
