# Bennett 500 K — 좁은 원자료 의미 확인

## 결론

**원 Table 3의 500 K 행과 출판된 fit 식은 현재 frozen packet의 literal·지수·단위와 일치한다.** 이번 확인에서 parser, 단위 scale 또는 통계 인자의 잘못을 뒷받침하는 증거는 발견하지 않았다. 원 fit과 첫 primary 출력은 변경하지 않는다.

저장된 table 기준 잔차 0.24810218511972792는 유지한다. 다만 원 rate-fit 문단은 상대오차의 분모를 명시하지 않는다. 따라서 이 수치만으로 논문의 20% 서술이 잘못됐거나 모순이라고 판정하지 않는다. 이 note는 원문 의미 확인이며, 별도의 고정밀 수치 구현 검사를 대신하지 않는다.

## 직접 읽은 근거와 literal

[Primary DOI](https://doi.org/10.1046/j.1365-8711.2003.06422.x)의 원 출판 PDF에서 보존된 page6 이미지, 즉 printed p.366의 Table3와 하단 fit 문단을 다시 읽었다. 이미지를 만든 원 PDF는 앞선 source 검토에서 확인했으며, 현재 원 PDF bytes는 미복구 상태다. 이번에 사용한 retained image의 SHA256은 daa6e8a313d48de1b85350c65103f0e5b6774b7c1a4027bd6db72e6b3a1db388이다.

| 확인 항목 | 인쇄 원문 및 packet에서 일치한 값 |
|---|---|
| Table3의 온도 | 500.0 K |
| 해당 rate mantissa | 4.79 |
| Table3의 공통 단위 | \(10^{-20}\ {\rm cm^3\,s^{-1}}\) |
| Fit의 상수항 | 3.22 |
| 첫 denominator 항의 계수·지수 | 0.0657, −2.45 |
| 둘째 denominator 항의 계수·지수 | 0.00631, +0.837 |
| 두 항의 무차원 온도 | \(T/(1000\ {\rm K})\) |
| Fit의 공통 단위 scale | \(10^{-20}\ {\rm cm^3\,s^{-1}}\) |

확인한 함수는

\[
k_{\rm fit}(T)=10^{-20}
\left[
3.22+\frac{1}{
0.0657\left(T/(1000\,{\rm K})\right)^{-2.45}
+0.00631\left(T/(1000\,{\rm K})\right)^{0.837}}
\right]\ {\rm cm^3\,s^{-1}}.
\]

원문은 Table3와 fit 모두 spontaneous association 및 quasi-bound radiative-decay 가중을 포함한 계수로 연결한다. 같은 페이지의 stimulated-emission 절·그림과 섞지 않았다. 이 한 점을 맞추려고 기존 electronic \(1/4\)나 별도 입사쌍 계수를 다시 적용할 근거도 없다.

이번에 재확인한 native row는 B03_T500.0 한 개다. Source packet SHA는 40e2fbd73d451c0c8116b4ca9bd4db4d2e43e4cdf8967988a2fea551f99ce35e로 유지되며, 기존 77개 셀 검토를 반복하지 않았다.

## 저장된 계산값과 오차 정의

registry/fit_diagnostics.json의 SHA256은 5f687fac3c21dc8a9747c45ac6558a4b9d7c107577d6d9eb9285bc13a9c7f599이다. 다음 값은 해당 첫 primary 출력에서 읽은 값으로, 이 source reviewer가 새로 계산한 값이 아니다.

| 저장 필드 | 값 |
|---|---|
| \(k_{\rm table}(500\,{\rm K})\) | \(4.79\times10^{-20}\ {\rm cm^3\,s^{-1}}\) |
| \(k_{\rm fit}(500\,{\rm K})\) | \(5.978409466723497\times10^{-20}\ {\rm cm^3\,s^{-1}}\) |
| \((k_{\rm fit}-k_{\rm table})/k_{\rm table}\) | 0.24810218511972792 |
| 이 점이 27-node 최대라는 관측 | 기존 primary summary의 기록을 재사용; 이 note에서는 재계산하지 않음 |

프로젝트가 사전에 정의한 진단은

\[
r_{\rm table}=\frac{k_{\rm fit}-k_{\rm table}}{k_{\rm table}}
\]

이다. 원문은 약 800 K보다 높은 온도에서 대략 5% 수준이라고 설명하고, 저온에 대해 다음과 같이 서술한다.

> the error can be up to 20 per cent

해당 rate-fit 문단에는 오차의 분모 또는 별도의 상대오차 공식이 없다. 이미 회수된 EXA_HD2024_BENNETT_FULLTEXT.txt의 Bennett section에서도 error·relative·fit 문맥을 좁혀 확인했지만, rate fit의 분모를 정의하는 구절을 찾지 못했다. 진동준위 표의 다른 percent-error 항목은 실험 비교의 별도 문맥이므로 rate-fit 정의로 옮길 수 없다.

같은 두 양수에서 다른 상대오차 정의

\[
r_{\rm fit}=\frac{k_{\rm fit}-k_{\rm table}}{k_{\rm fit}}
=\frac{r_{\rm table}}{1+r_{\rm table}}
\]

도 가능하다. 현재 저장된 양의 \(r_{\rm table}\)은 \(1/4\)보다 작으므로 이 식에서 \(r_{\rm fit}<1/5\)가 대수적으로 따른다. 이는 새로운 fit 평가 없이도 분모 선택이 20%와의 비교를 바꿀 수 있음을 보여 준다. **이 사실로 원 저자가 fit 분모를 사용했다고 확정하지는 않는다.** 원문의 의도한 분모는 미결정으로 남긴다.

따라서 table 기준 진단을 그대로 보고하면서 원문 정확도 설명을 별도로 보존한다. 원 fit을 수정하거나, 표를 보정하거나, 허용오차를 결과에 맞춰 늘리거나, 첫 출력을 덮어쓰지 않는다. 이 잔차를 물리적 uncertainty 또는 covariance로 해석하지 않는다.

## 접근·provenance와 검토 범위

이번 확인의 중심 근거는 보존된 primary PDF page image다. 기존 cached fulltext representation의 전체 SHA256은 d496439a29e7485c7eae2084174161a405c3be106a161bd1199f5e0f2cab3ff4이며, 그중 원 [ADS PDF URL](https://articles.adsabs.harvard.edu/pdf/2003MNRAS.341..361B) marker 이후의 Bennett section만 error 정의 검색에 사용했다. 이 representation은 원 pdftotext 파일과 동일한 bytes라고 주장하지 않는다. OCR의 기호 불명확성은 page image로 대조했다.

새로 전달받은 publisher alternate URL은 이번 web open에서 internal error로 접근되지 않았다. 따라서 그 요청을 새 원문 회수 성공으로 기록하지 않는다. 원문 전체나 page image는 이 공개 note에 재배포하지 않는다.

최신 AGENTS와 local HEAD 7898ef5affbfc654d4a3a8d8acd0d7a899a0d7e0, S05 preflight 및 S04의 실제 Dropbox/Drive upload ACK를 읽었다. Root가 첫 primary 결과를 보존하고 독립 checker가 고정밀 구현 검사를 담당한다. 이번 작업의 새로운 fit·residual 수치 평가, compiler·Wolfram 실행, source 변경 및 physical rate/Q 승인은 모두 0이다.
