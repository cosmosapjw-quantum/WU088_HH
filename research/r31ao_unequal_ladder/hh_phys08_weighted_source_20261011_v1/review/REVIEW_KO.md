# PHYS08 독립 비생성자 검토

## 판정: PROMOTE_SCOPED

**보존된 NCP07 source 자료에 대한 가중 냉각 정리와 정확 유리수 재산술을 해당 범위에서 채택한다.** Full과 같은 COMMON에서 시작한 first-half 각각의 전체 photo source `P_N`과 birth 미분 `P_M`가 냉각 방향이라는 새 결론은 원 source 식과 실행 증거에 부합한다. HH/photo source 경쟁 항의 음수 및 gas-energy reaction-vector cancellation도 같은 범위에서 채택한다.

Rust gate·standalone driver·출력 consumer·NCP wrapper는 다음 NCP 실행을 위한 **READY_NOT_RUN 후보**다. 이 판정은 Rust 실행, native nonlinear root, 실제 U/V/W/I, 유한 gas-energy interaction, carried second-half, paired defect, time/continuum remainder, full49 또는 production을 인증하지 않는다.

후보의 코드·테스트·이론 생성에 참여하지 않은 `/root/phys08_decision_review`가 검토했다. 이 하위작업에서 후보 코드를 수정하거나 import하지 않았고, 과학 재산술·source/provider callback·build·test·원격 mutation을 실행하지 않았다. 작성한 파일은 이 문서와 `review/DECISION.json` 두 개다.

## 고정된 검토 대상

검토 대상은 `review/FROZEN_INPUT_MANIFEST.json`의 128개 파일, 총 3,832,865 bytes다. Manifest SHA256은 다음과 같다.

```text
ae56dc54ea01a3757941aa919140bed8231e33cd7bd953550c478893f7048ab4
```

마지막 단계에서 한 번의 읽기 전용 identity pass를 수행했다. 128개 payload의 size/SHA256과 실제 파일 집합이 모두 일치했다. 선택된 NCP07 raw 81개 파일 역시 intake manifest의 size/SHA256 및 그 manifest에 보존된 authoritative Git blob SHA1과 일치했다. Reviewer가 원격 Git 객체를 새로 가져온 것은 아니다. 원격 intake 자체의 기록과 현재 보존 bytes를 구별했다.

원 NCP snapshot은 `4d5c18b8a6d348e2de42b5e12dc0fd4d753add7b`이고, 연구 부모는 `e9272a1ffe0bd012e4e34718b7b2576bfd26772e`다. Sourcebox producer, reduced source, HH Jet, transport, COMMON family, frozen domain, 원 독립 판정과 그 실행 기록을 읽었다. Repo AGENTS와 지정된 baseline 문서도 읽었으며, 그 문서의 과거 실행 예시는 수행하지 않았다.

5개의 중복 transport FETCH_PAYLOADS 중간물은 core에서 제외되었지만 필요한 raw 81개와 provenance는 모두 남았다. 이는 선택된 source intake의 전달 범위이며 전체 NCP archive의 복원을 새로 인증하는 주장이 아니다. 최종 top-level MANIFEST/checksum, 이 review의 두 출력과 이후 detached delivery 기록은 위 고정 manifest의 범위 밖이다.

## 수학과 source mapping

온도는 같은 source의 고정 계수에서

\[
p=1+\widehat f+x+\widehat f(y_1+2y_2),\qquad T=Cw/p
\]

로 정의된다. Quotient rule에 따라

\[
DT[v]=\frac{C}{p^2}\left[pv_w-w(v_x+\widehat f v_{y_1}+2\widehat f v_{y_2})\right]
\]

가 성립한다. 따라서 양의 \(C,p\) 아래 전체 balance 상계의 엄밀한 음수는 냉각의 충분조건이다. 개별 에너지 노드마다 같은 thermal inequality가 성립할 필요는 없다. 큰 고에너지 성분은 가열을 만들 수 있으므로 임의 스펙트럼에 대한 보편 냉각 명제는 아니다.

실제 `hh_rate_jet`와 `sourcebox::temperature`를 읽어 위 온도 식의 대응을 확인했다. 온도의 \(\widehat f\)는 저장 nHe와 nH scalar leaf의 정확한 실수 비다. Photo ion-fraction 변환에는 별도의 stage fHe leaf가 사용된다. 두 상수를 같다고 축약하지 않은 구현이 맞다. Scalar 계수의 곱을 새로운 binary64 scalar로 재반올림하여 fixed-real 식을 바꾸지도 않았다.

| 대상 | 보존된 source 슬롯 |
| --- | --- |
| 전체 photo \(P_N\) | `photo_rates[*][*].value` |
| \((P_N)_g\) | `photo_rates[*][*].gradient[k]`, \(k=0,\ldots,3\) |
| Birth 미분 \(P_M\) | `photo_rates[*][*].gradient[5]` |
| \((P_M)_g\) | `photo_rates[*][*].signed_hessian[k][5]` |

`aggregate`는 33개 노드와 세 absorber channel을 모두 읽는다. Helium 성분은 stage f로 정규화하고, thermal 성분은 source에서 실제 캡처한 heat leaf를 사용한다. 작은 양·음 값과 subnormal tail을 screening하거나 0으로 바꾸는 경로가 없다. N, 유한 birth amount M, M/dt와 \(P_M=\partial_bF_\gamma\)도 분리되어 있다.

COMMON은 future Jet을 상수로 초기화하고, transport/remap/geometry coefficient는 gas·lambda·b에 대해 고정되어 있다. 직접 birth는 b slot 5로 들어간다. 따라서 이 fixed-real family에서 incoming의 gas 미분이 0이라는 closed-form 전제가 source에 맞는다. 이 구조적 사실로 저장된 미분 interval의 작은 폭을 삭제하지 않았다. 서로 다른 stage, 중심점 자료와 whole-box 자료 또는 과거 reference root를 섞지 않은 것도 확인했다.

## Source 경쟁 및 에너지 범위

HH source \(H=q(1,0,0,-\chi_H)\), \(q=n_H(1-x)^2k(T)\)에 대해

\[
Dq[P]=q\left[-\frac{2P_x}{1-x}+\frac{\nu}{T}DT[P]\right],
\qquad \nu=\operatorname{exact}(\operatorname{fl}(1.2))+157800/T
\]

를 미분하면 native HH source의 captured coefficient와 일치한다. 현재 domain에서 \(q,1-x,\nu,T\)는 양수다. \(P_x>0\), \(DT[P]<0\)가 함께 성립하므로 \((H_gP)_x<0\)를 얻는다.

HI-only fixed sigma leaves와 gas-independent incoming Z 아래

\[
((P_Z)_gH)_x=-q\sum_j\frac{c n_H\sigma_jZ_j}{D_j^2}
\]

가 성립한다. Signed M에서는 각 노드가 양수라고 가정하지 않고 합계 포함값으로 부호를 판정한다. 코드의 별도 경로는 저장 q.gradient와 rate gradient/Hessian을 수축한다. 두 표현의 overlap은 정합성 진단으로만 기록하며 identity 증명으로 승격하지 않았다.

Gas energy의 \(\ell\)은 stage f와 같은 CHI leaf를 사용한다. \(\ell\cdot(1,0,0,-\chi_H)=0\)이므로 \(\ell H_gv=0\)은 정확한 반응 벡터 항등식이다. 독립 interval endpoint를 임의로 상쇄하여 0을 만든 것이 아니다. Photo projection은 heat+CHI를 유지하여 heat subtraction의 rounding correction을 보존한다.

이 source 항들의 부호는 유한 solution-map interaction의 부호가 아니다. Implicit Jacobian inverse, mixed response, parameter integration, carry와 remainder가 추가로 필요하므로 실제 U/V/W/I와 finite energy sign은 OPEN이다.

## 관측된 실행과 실제 결과

첫 `weighted_first`는 `157800/T`에서 reflected division 연산자가 빠져 exit 1로 종료했다. 0.21646843599592103 s의 실행 기록, 원 stderr와 코드 snapshot이 보존되어 있으며 snapshot hash가 첫 실행의 원 bound hash와 맞았다. 실패를 성공으로 재라벨하지 않았다.

정적 diff에서 확인한 수정은 기존 interval division으로 위임하는 `__rtruediv__`, 새 create-only output-run-id 및 invocation counter 명칭 정리다. 수학식, source 입력, box, 허용오차, 부호 조건이나 assertion을 완화하지 않았다. 계약상 허용된 한 번의 corrected run은 exit 0, 0.3678347829991253 s, Linux max RSS 19,324 KiB였다. 두 run 각각의 bound 19개 항목과 stdout/stderr hash가 보존 bytes와 일치한다. 현재 exact reference와 진단 코드의 hash는 corrected run이 실행한 hash와 같다.

다음은 `WEIGHTED_RESULTS.json`에서 읽은 outward binary64 **상계**이며 reviewer가 새 물리 계산을 수행한 값은 아니다.

| Stage·역할 | B 상계 | DT 상계 [K/s] |
| --- | ---: | ---: |
| Full \(P_N\) | -6.407154466296521e-13 | -1.0823745158896578e-9 |
| Full \(P_M\) | -1.0282460808385432e-16 | -1.7370384307378258e-13 |
| First-half \(P_N\) | -6.414618176522015e-13 | -1.0836353766640553e-9 |
| First-half \(P_M\) | -5.1473289690541e-17 | -8.69549459172802e-14 |

네 경우에서 B·DT·\((H_gP)_x\)·\((P_gH)_x\)·\(\ell(P_gH)\)는 엄밀한 음수이고 \(P_x,P_w\)는 양수다. 광반응이 thermal energy를 올리면서 입자 수의 증가를 통해 온도를 낮추는 결과가 가능하다. 원 node32 per-node witness의 OPEN은 그대로 남아 있고 새 aggregate 결과는 별도다.

294는 프로그램 assertion 수이며 독립 과학 실험이나 test case 수가 아니다. Golden fixture는 실제 source의 네 stage/role 조합과 일곱 의미 사례, 총 11개다. TSV의 case ID·role·16개 endpoint word가 각 oracle fixture와 정확히 일치함을 마지막 artifact check에서 확인했다. Creator claim JSON의 `semantic_fixture_cases=11`은 이 전체 golden collection을 지칭하는 필드이며 정확한 분류는 이 문서와 RESEARCH_STATE의 4+7을 따른다.

정확 유리수 구현은 유한 endpoint bits를 Fraction으로 읽어 사칙연산을 수행하고 표시용 binary64만 바깥으로 반올림한다. 이 산술과 source mapping의 정적 검토를 마쳤다. 다만 원 native Jet·초월함수 kernel 전체를 독립적으로 다시 증명하거나 실행한 것은 아니므로, 저장 source 포함성과 C² provenance는 계속 전제로 남는다.

## Rust와 NCP handoff 검토

Rust scalar gate의 사칙연산은 ordinary IEEE binary64와 gradual underflow 아래 한 칸 next-down/next-up으로 포함값을 만든다. 유한 입력·분모·overflow와 일부 FP 환경 위반을 명시적으로 거절한다. 환경 probe는 완전한 platform attestation은 아니다. B와 DT의 strict sign을 따로 보고하여 underflow로 0을 포함하는 DT에 엄밀한 부호를 만들어 주지 않는다.

Rust는 일반 scalar 함수로 signed fhat도 허용하고, exact reference는 물리적 fhat>=0을 요구한다. 현재 11개 fixture는 두 함수의 공통 domain 안에 있다. 양의 실제 abundance, 동일 T=Cw/p identity, role의 source provenance는 caller의 별도 의무이며 label만으로 보증되지 않는다.

Standalone driver와 output consumer는 11개 case의 누락·중복·추가, role, sign label, 유한 interval, 정확 rational oracle의 **전체 포함**과 요약 schema를 검사한다. 소비자는 전달받은 출력의 검증만 주장하고 특정 binary가 실제 실행되었다고 자칭하지 않는다. 의미 그룹 7, 전체 scalar gate 호출 26, 의도한 gate 오류 7은 후속 실제 출력에서 검사할 계획값이다. 현재 실행 실적으로 채우지 않았다.

NCP wrapper는 기존 compiler 식별, offline build 한 번, gate 한 번, consumer 한 번을 순차 수행하고 create-only 로그와 전후 input/binary identity를 기록한다. 새 source/solver를 호출하는 경로가 없다. Compiler 부재 또는 첫 실패 시 설치나 자동 retry를 하지 않는다. 실제 네 source fixture를 연결하는 sidecar도 archived aggregate의 scalar gate 구현 증거로 한정했다.

현재 Rust, wrapper와 출력 consumer는 **NOT_RUN**이다. Syntax evidence는 최종 Python 다섯 파일의 AST parse를 결박하지만 build나 실행 증거를 대신하지 않는다. NCP가 실제 기록을 생성하기 전에는 이 판정을 Rust 검증 완료로 읽으면 안 된다.

## 남는 의무와 전달 범위

이 후보에 대한 material correctness blocker와 필수 수정은 발견하지 못했다. 기존 사용자 승인 범위 안의 additive 연구 branch/PR 및 전달 작업은 이 scoped 판정으로 진행할 수 있다. Native runtime 설치, provider·full49·production 승격은 포함되지 않는다.

후속 NCP는 고정된 core와 계약을 먼저 확인한 뒤 저장 fixture의 최초 build/gate/consumer만 수행한다. Source producer, 성공한 exact reference와 historical scientific suite를 다시 실행하지 않는다. 미계측 inherited counter는 null로 보존한다.

원격 Git publication, Drive·Dropbox upload ACK/metadata 및 다운로드한 bytes의 restore 검증은 이 검토자가 수행하지 않았다. 해당 사실과 실제 객체 ID는 별도 delivery receipt가 결박해야 한다. 이 판정의 해시·수학 검토를 원격 복원 성공으로 표현하지 않는다.

