# R8 native9 φ 상계의 제한된 exact-rational 재판정

작성 단계 상태: **NOT_EXECUTED**. 이 문서는 단일 보완 검증기의 수학 계약이다. 실행 결과는 별도의 `raw/PHI_SCALAR_REPAIR_RESULTS.json`과 전체 프로세스 CPU 영수증으로 판정한다. 원래 `raw/REFERENCE_RESULTS.json`의 FAIL은 그대로 보존한다.

## 1. 관측된 실패와 적용 범위

고정 native9 사례 `saved_native_nine_state_K_conditional_feedback`에서 독립 Decimal80 검산의 φ 항목 하나가 실패했다. 원래 검산은 727개 항목·22,659개 성분 중 한 항목·한 성분의 차이 `2.91082879488003260494168072896889699597324659550784E-30`가 공통 근접성 허용치 `1e-30`를 넘었다고 기록했다. 나머지 항목의 기존 결과는 재사용한다.

이 보완은 해당 고정 스칼라 하나의 엄밀한 상계 여부와 저장된 지수 구간에 따른 실제 오차 예산만 판정한다. 이론식, 생산 코어, primary 결과, 원래 reference 결과·허용치·실행 기록을 변경하지 않는다. 새 ODE·지수함수 계산·생산 import·기존 runner 재실행은 없다. 원래 근접성 기준을 통과했다고 소급하여 기록하지 않는다.

## 2. 저장된 상계의 생성식과 오차 예산

이 사례에서 \(d=-1/20000000<0\), \(\delta>0\)이며 \(r=-d\), \(x=r\delta\)로 둔다. 저장된 exponential enclosure는 \([\ell,u]\)이고,

\[
u-\ell=\frac{51}{2^{128}}.
\]

생산 코어의 φ 값 \(P\)는

\[
P=\operatorname{up}_{128}\!\left(\frac{1-\ell}{r}\right),
\qquad
\phi=\int_0^\delta e^{-rs}\,ds.
\]

기존 지수 구간의 유효성을 사용하면

\[
0\le P-\phi\le
\frac{u-\ell}{r}+2^{-128}
=\frac{1020000001}{2^{128}}=:A.
\]

이는 작은 \(r\)로 나누면서 지수 구간 폭이 증폭되는 정확한 오차 예산이다. 고정 `1e-30` 근접성 기준은 이 항을 결속하지 않았다. 보완 검증기는 저장된 값의 생성식과 위 폭·예산의 exact rational 동일성도 확인한다.

## 3. 생산 구현과 독립적인 직접 적분 급수

\(0<x<1\)이면

\[
\phi=\delta\sum_{k=0}^{\infty}\frac{(-x)^k}{(k+1)!}.
\]

양의 항 \(t_k=\delta x^k/(k+1)!\)는

\[
\frac{t_{k+1}}{t_k}=\frac{x}{k+2}<1
\]

을 만족한다. 따라서 교대급수 정리로 고정된 두 부분합

\[
L=S_9=\delta\sum_{k=0}^{9}\frac{(-x)^k}{(k+1)!},
\qquad
U=S_8=\delta\sum_{k=0}^{8}\frac{(-x)^k}{(k+1)!}
\]

에 대해 \(L\le\phi\le U\)이며,

\[
U-L=\frac{\delta x^9}{10!}.
\]

보완 검증기는 저장된 exact rational \(d,\delta,P,\ell,u\)를 읽어 `Fraction`만으로 \(L,U\)를 계산한다. 생산 코드의 지수함수나 φ 함수를 호출하지 않고, Decimal80 지수함수도 재계산하지 않는다. 차수 8/9는 실행 전에 고정되어 있으며 결과를 보고 증가시키지 않는다.

## 4. 수용 조건

핵심 수용 조건은 다음 두 부등식이다.

\[
P\ge U,
\qquad
P-L\le A+(U-L).
\]

첫 식은 \(\phi\le U\le P\)를 직접 보장하므로 저장된 φ가 엄밀한 upper임을 생산 구현과 독립적으로 증명한다. 둘째 식은 실제 여유가 저장된 지수 구간·outward rounding의 분석적 예산과 양립함을 보인다. 추가로 \(P-U>10^{-30}\)를 요구한다. 이 조건이 실제 통과하면 참값과의 차이도 원래 `1e-30` 기준보다 크므로, 원래 근접성 실패가 예상되는 보수적 여유임을 확인한다.

출력은 이 단일 스칼라의 재판정이다. 새로운 물리 시나리오나 전체 reference의 새 실행으로 세지 않는다. 최종 심사자는 원래 `726/727 PASS, 1 FAIL 보존`과 별도 scalar 결과를 함께 인용한다. 전체 이론·코드 채택은 이 결과 외에 기존 일반 증명·primary·reference의 나머지 항목·독립 심사를 함께 요구한다.

## 5. 원본 결속과 실행 제한

원본 primary SHA256은 `520110d1cae1677491aecd7216621c25f1098470c939ee027d5df3bde183686b`, 원본 reference SHA256은 `da699b9a8b53389e3d222f34a5a421cd88ce17787bde69cc2e9bed5fb15409df`이다. 검증기는 이 바이트 식별자, 유일한 실패 이름·원래 카운트·원래 허용치, 고정 B/δ/상태 순서·동일 family·R6/R7 source pin, 저장된 φ와 지수 구간을 확인한다. 계산 후 원본 두 파일의 해시도 다시 확인한다.

성공 경로에는 **24개의 명명된 검사**가 있다. 이는 과학적으로 독립적인 24개 시나리오라는 뜻이 아니다. 계약은 `verification/PHI_SCALAR_REPAIR_CONTRACT.json`의 schema `WU_R8_PHI_SCALAR_REPAIR_CONTRACT_V1`를 요구하고 실제 계약 바이트의 SHA256을 출력한다. 실행 허가·script pin·전체 CPU 10초 제한은 root가 게시한 계약과 실행 wrapper가 관리한다.

보완 출력은 `raw/PHI_SCALAR_REPAIR_RESULTS.json`에 create-only로 기록하며 기존 출력이 있으면 실행을 거부한다. 원래 primary/reference budget은 그대로 소진 상태이고 이번 보완 allowance는 별도로 기록한다. 현재 문서 작성자는 script 실행·import·AST·과학 계산을 수행하지 않았다.
