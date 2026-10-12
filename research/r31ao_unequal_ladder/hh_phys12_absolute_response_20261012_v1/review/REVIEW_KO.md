# WU088_HH PHYS12 독립 판정

## 판정과 채택 범위

**PROMOTE_SCOPED.** 각 보존된 첫 단계의 같은 고정 계수 묶음에서 미래 LCS HH를 OFF에서 ON으로 바꿀 때의 유한 수소 이온화 분율·열에너지 응답, 기존 혼합 응답과의 비교, b_amp=1의 절대 HH 응답을 분모로 한 비율을 조건부로 채택한다. 이 판정은 원 source-inclusion과 열린 C² 계열 전제를 상속하며, 원 소스·native solver·시간 이력의 정확성을 새로 인증하지 않는다.

최초 검토에서 blocking finding이나 후보 수정 요구는 없었다. 판정 대상은 `review/REVIEW_INPUTS.json`의 31개 고정 파일이며 그 manifest SHA-256은 `09613443ea1c624dea21616865828a4d1ab6dfdb1d97ce42c6815549e1ab3023`다. 31개 모두 명시된 크기와 SHA-256에 일치했다. 이후 추가된 delivery 파일은 이 과학 판정에 포함하지 않는다.

판정자는 `/root/remote_state`다. 후보 생성 전에 수행한 역할은 원격 branch/PR 및 보존된 source identity 조사와 기록뿐이었다. 기존 계획의 내용과 원본 경로를 전달했으나 PHYS12 이론·코드·fixture·검증 설계를 만들지 않았다. 고정 후보를 받은 뒤 후보 코드를 수정하거나 실행하지 않고 별도 판독기를 작성했다. `theory/INDEPENDENT_SOURCE_PREMISES_READBACK_KO.md`는 creator-side 보조자료이며 이 독립 판정을 대신하지 않는다.

연구·코딩 Astra v4.0.0의 실제 진입 지침과 모델 라우팅 문서를 읽었다. research harness의 state 파일은 미작성 패키지 템플릿이므로 실제 연구 상태로 해석하지 않았다. 현재 작업의 권한과 범위는 실제 사용자 요청, frozen scientific contract, PR45/PHYS11 고정 상태에 근거한다. 호스트 라벨은 GPT-6 Astra Pro지만 별도의 backend attestation은 제공되지 않았다. 미지원 Pro 별칭을 임의로 정규화하거나 모델 전환을 주장하지 않고 기존 Astra v4 절차를 이어 적용했다.

## 1. 같은 계수에서의 유한 응답

각 stage의 한 고정 admissible α에 대해 보존된 root family를 g(λ,b;α)라 하자. PHYS09 정리 §§2,5–6 및 기존 DECISION의 `same_family_conditions`는 다음 조건을 명시한다.

- COMMON, old gas/photon/guard, transport 및 scalar coefficients는 Θ=[0,1]² 전체에서 같은 α다.
- SOURCE_BOX는 전체 X×Θ, SOURCE_CENTRE는 같은 계수에서 고정 중심×Θ를 포함한다.
- 열린 실수 source chart와 strict Banach 여유, 고정 C 및 Neumann 나머지가 root/미분 포함의 전제다.
- full과 first_half는 각자의 duration/PreBE 계수를 가진 별개의 첫 단계다.

이때 같은 b=b_*와 α에서

\[
D_{\lambda_0\to\lambda_1}O(b_*;\alpha)
=\int_{\lambda_0}^{\lambda_1}\partial_\lambda O(\lambda,b_*;\alpha)\,d\lambda.
\]

전체 Θ의 포함 U_O∈[u⁻,u⁺]는 이 경로를 포함하므로, λ₁−λ₀≥0에서 유한 차이는 (λ₁−λ₀)[u⁻,u⁺] 안에 있다. PHYS12의 길이는 정확히 1이다. 따라서 기존 U의 정확 끝점을 그대로 쓰는 것은 정당한 finite-response 포함이다. λ=0에서의 선형근사나 네 corner를 실제 계산했다는 주장으로 해석하지 않는다.

기존 root/Jacobian/source 산술을 새로 실행할 필요는 없으며 이번 판정에서도 실행하지 않았다. 다만 기존 source 포함 전제가 틀렸거나 α를 endpoint마다 바꾸면 이 결론은 유지되지 않는다. 후보의 changed-alpha 예제는 이 제한을 정확히 드러낸다.

H=q(1,0,0,−χ_H), q=n_H(1−x_HII)² k_LCS(T)의 단위·정규화와 선택된 closure는 유지된다. q는 H핵당 proper s⁻¹, w는 thermal eV/H, λ와 b는 무차원이다. 소스 자체의 q>0만으로 결합계의 U_x 부호를 추측하지 않고 실제 uniform-U 포함에 의존한 점도 적절하다.

## 2. 절대·혼합·상대 보정의 정확한 구분

채택하는 1차 결과의 외향 십진 표시는 다음과 같다. 정확한 유리수 끝점은 결과 JSON에 있다.

| 별개의 첫 stage | D_HH x_HII(1) | D_HH w(1), eV/H |
|---|---:|---:|
| full, 1.25×10⁹ s | [1.02776508×10⁻¹⁰, 3.12855435×10⁻¹⁰] | [−4.25821437×10⁻⁹, −1.39867706×10⁻⁹] |
| first_half, 6.25×10⁸ s | [5.14217934×10⁻¹¹, 1.56503922×10⁻¹⁰] | [−2.12917863×10⁻⁹, −6.99525692×10⁻¹⁰] |

두 stage 모두 D_x>0이고 D_w<0이다. 이는 같은 OFF 대조군에 비해 HH ON의 이온화 분율은 높고 열에너지는 낮다는 결과다. 순간 dx/dt나 stage 전후 w의 총 변화가 아니다.

기존 finite interaction의 gas 배열은 저장된 W 배열과 정확히 같았다. 같은 α에서

\[
I_O=D_{\rm HH}O(1)-D_{\rm HH}O(0)
\]

이므로 uniform U_x>0, U_w<0와 W_x<0, W_w>0는

\[
0<D_x(1)<D_x(0),\qquad D_w(0)<D_w(1)<0
\]

를 준다. 기존 음의 I_x가 HH 자체의 음의 이온화 기여를 뜻하지 않는다는 설명은 맞다. b=0에도 보존된 광자가 남으므로 이를 전체 photoionization OFF와 동일시하지 않는 제한도 필요하며 후보에 명시돼 있다.

비율은 정확히

\[
r_x=-I_x/D_x(1),\qquad r_w=I_w/[-D_w(1)]
\]

이다. 분모가 엄밀히 양수이고 구간의 반대쪽 끝점을 조합하므로, 상관관계를 별도로 이용하지 않아도 포함은 보수적으로 유효하다. 실제 결과의 네 비율 구간을 별도 Fraction 식으로 확인했다.

| stage | r_x | r_w |
|---|---:|---:|
| full | [1.47850621×10⁻⁷, 1.42446502×10⁻⁶] | [9.93661129×10⁻⁸, 9.83873554×10⁻⁷] |
| first_half | [3.70489775×10⁻⁸, 3.56609463×10⁻⁷] | [2.48951058×10⁻⁸, 2.46229885×10⁻⁷] |

이는 b=1의 HH 효과를 분모로 한 보정이다. b=0 기준 억제분율은 r/(1+r)이며 이 표와 다르다. 전체 이온화·가열에 대한 HH 비중이나 우주론적 생략 기준도 아니다. 후보는 이 해석 차이를 보존한다.

## 3. 실제 독립 검산과 실행 증거

검토자는 후보의 `analyze_absolute_hh.py`를 import하거나 재실행하지 않았다. 독립 판독기 `review/independent_endpoint_check.py`는 파일을 읽고 Python Fraction 및 Decimal로 다음만 검사했다.

| 검증 대상 | 실제 확인 |
|---|---|
| Frozen candidate | 31/31개 파일의 크기·SHA-256 일치 |
| 보존된 과학 실행의 입력·코드 | 15/15개 before=after=current; candidate/contract snapshot 일치 |
| 원 source identity | SHA-256 및 Git blob SHA가 독립적으로 관측한 parent remote tree와 일치 |
| 상속 구간 | gamma·det C·margins·U·W의 총 28개 구간: exact 순서·binary64 외향 표시·bits 확인 |
| 절대 결과 | 4개 정확 구간이 해당 저장 U와 정확히 동일 |
| 재사용 혼합 결과 | 4개 정확 구간이 W 및 원 finite-unit-square gas 배열과 동일 |
| 비율 | 4개 정확 구간이 독립 Fraction 계산과 동일 |
| 결과 표시 | 총 24개 끝점의 십진 표현이 정확 끝점을 바깥에서 포함 |
| 표·로그 | CSV 8행, SUMMARY, raw stdout의 수치·부호·단위·stage 일치 |

독립 판독기는 첫 실행에서 exit 0이었다. child 전체 경과시간은 0.048622801 s, 내부 판독시간은 0.016234881 s, CPU는 0.015984339 s, 최대 RSS는 15,696 KiB였다. 결과와 raw stdout/stderr 및 실행 정보는 `INDEPENDENT_ENDPOINT_CHECK.json`, `INDEPENDENT_CHECK_EXECUTION.json`, `independent_check.stdout.json`, `independent_check.stderr.txt`에 보존했다. 이 수들은 자료·산술 판독 건수이며 독립 물리 실험 수가 아니다.

원 `absolute_v1` 실행 기록은 exit 0, wall 0.064731937 s, CPU 0.054618 s, RSS 15,104 KiB다. 189개의 기록된 assertion이 모두 true이고 stdout의 행은 최종 SUMMARY와 같다. reviewer는 이미 종료된 그 child를 직접 관찰한 것이 아니라 실제 저장된 실행 기록·원 로그·결박 파일·결과를 교차 확인했다.

전체 과학 suite, source producer, 원 U/V/W/inverse 또는 native solver를 다시 실행하지 않았다. 새 후보 코드가 표준 라이브러리의 입력 판독·유리수 산술 경로만 사용한다는 것도 정적으로 읽었다. 그림 코드를 읽고 PNG를 직접 확인했으며 absolute/mixed 부호, 축의 다른 10의 지수, 재사용 표기, 별개 첫 stage 및 조건부 포함 설명이 결과와 맞는다.

## 4. 유지하는 조건과 종료

이번 승격은 다음을 포함하지 않는다.

- 원 interval kernel·provider의 source-inclusion을 새로 증명했다는 주장.
- 실제 native root/U/V/W/I의 생성 또는 authority 승격.
- carried second_half, full-versus-two-half 오차, 시간·연속체 remainder.
- 임의의 Bianchi 이방성 또는 전체 재이온화 history로의 일반화.
- global conservation, full49, production.
- microscopic singlet H⁺/H⁻ 채널의 물리 rate나 LCS와의 동등성.
- HH가 우주론적으로 무시 가능하다는 판정.

단계의 입력에는 Hubble triplet [10⁻¹⁴,10⁻¹⁴,10⁻¹⁴] s⁻¹가 고정돼 있다. 기존 포함 폭은 계수 domain·종속성 손실·원 inverse remainder를 함께 담으며 순수 수치오차 또는 신뢰구간으로 분해되지 않는다. 소비 관측량의 absolute threshold는 미지정이다.

최종 과학 completion bar는 이 조건 아래 충족됐다. 같은 bounded 질문의 추가 구간 정밀화나 과학 재실행을 요구하지 않는다. `heavy_queue=[]`, `launch=false`를 유지한다.

원격 push/PR/backup은 이 판정에서 검증하지 않았다. freeze 시점에 root는 해당 게시·백업을 아직 수행하지 않았다고 알렸다. 이후 provider ACK·object identity·restore 검증은 별도 delivery 증거로 판단해야 하며, 이 문서를 게시 또는 백업 성공 영수증으로 사용해서는 안 된다.
