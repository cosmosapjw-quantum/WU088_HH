# PHYS09 비생성 독립 검토

## 결정: PROMOTE_SCOPED

검토자는 `/root/phys09_decision_review`다. 이 검토자는 PHYS09의 정리·과학 코드·의미 사례·Rust 구현·handoff 작성에 참여하지 않았다. 생성자들이 고정한 candidate를 읽고 독립적으로 판단했다. **원 NCP07 fixed-coefficient real-source의 C² 및 source-inclusion 전제 아래, 두 first-stage 계열의 균일 implicit 응답과 유한 기체 에너지 상호작용의 엄격한 음수를 scoped 결과로 채택한다.** 실제 native issuer의 root/U/V/W/I, Rust 첫 빌드·실행 또는 continuum 결과는 이 결정으로 채택하지 않는다.

검토 기준은 `FROZEN_INPUT_MANIFEST.json`의 142개 payload, 총 6,565,074 bytes다. 해당 manifest SHA256는 `688eb86aeb9434e6f4cc49a5206d3db0432bd67cb80c5b3c41cee27dec3b12a1`이다. 모든 payload의 SHA256·크기가 일치하고, manifest 자신을 제외한 누락·추가 파일은 없었다. 검토자는 이 고정 입력을 변경하지 않았으며 최종 두 review 문서만 작성했다.

## 1. 원 소스와 같은 계열의 범위

최신 과학 source의 결박은 NCP07 delivery `4d5c18b8a6d348e2de42b5e12dc0fd4d753add7b`, source core `dfa574ce2c302ff2dce38d0e487903d57f1db977`이다. PHYS08 연구 delivery는 `3490c77ea548fa810443b06546ba847856a7eaea`다. 현재 검토자는 원격 branch를 다시 조회하거나 원 bytes를 재다운로드하지 않았으며, intake의 실제 조회 기록과 보존된 bytes를 검토했다.

`inputs/ncp07/SOURCE_INTAKE_MANIFEST.json`의 선택된 원본 81개는 SHA256·크기 및 당시 authoritative Git tree에서 기록된 blob SHA-1과 모두 일치했다. 그중 원 NCP package manifest에 속하는 69개도 원 SHA256·크기와 일치했다. `LOCAL_REUSE_MANIFEST.json`의 93개 재사용 파일도 일치한다. 이것은 선택한 자료의 identity 확인이며, 과거 전체 native archive의 재다운로드 restore를 수행했다는 뜻이 아니다.

`raw/src/sourcebox.rs::source_stage`는 같은 PreBE 객체와 전체 b 범위, 전체 lambda 범위를 사용하여 X와 고정 gas centre를 각각 평가한다. 따라서 `SOURCE_CENTRE`는 theta midpoint 한 점의 잔차가 아니다. `COMMON_INPUT_SCOPE`와 원 이론은 old gas 및 transport/source coefficient tuple을 parameter rectangle 전체에서 고정함을 명시한다. Full과 first_half는 각각 같은 COMMON에서 출발하는 첫 stage다. Carried second_half의 미분을 이 계산에 넣었다고 해석할 수 없다.

C²의 대상은 captured leaves를 정확한 실수에 올린 source 식이다. Native rounded program의 clipping·guard·반올림 전체가 C²라는 주장은 없다. 원 interval kernel, AD, geometry 및 provider가 그 source의 값과 미분을 포함한다는 전제는 상속된다. PHYS09의 exact arithmetic이 이 원 kernel 전체를 새로 형식 증명한 것은 아니다.

## 2. 에너지 source 항등식의 직접 점검

`raw/candidate/src/phys04_mixed.rs::phys04_reduced_residual`에서 nonphoto는 HH·photo·팽창 항을 더하기 전에 clone된다. HH는 정확히 q(1,0,0,−chi_H)이고, 같은 chi_H literal이 원 source와 `raw/src/energy.rs`에 사용된다. Stage f를 사용하는 photo fraction 식과 같은 f를 사용하는 ell을 결합하면 HI, HeI, HeII 채널의 에너지 계수는 각각 heat+chi_a가 된다.

따라서 다음 source 행은 유효하다.

\[
\mathcal E=\ell F
=\ell F^{np}+\sum_{j,a}(\mathrm{heat}_{ja}+\chi_a)r_{ja}-2H_{mean}w.
\]

동일 HH 반응벡터에서 ell H, ell H_g, ell H_gg가 정확히 0이라는 항등식을 적용한 것이다. 원 q interval의 양·음 끝점을 선택하거나 작은 항을 수치적으로 제거한 절차가 아니다. HH의 상태 피드백은 전체 G의 미분 및 U,V,W 안에 계속 들어 있다.

Stage f와 exact(nHe_stored)/exact(nH)의 차이는 유지된다. Nonphoto를 ell로 직접 투영하므로 normalization 차이는 이미 포함되고, Jnorm을 별도 추가하여 이중으로 계산하지 않는다. Captured heat와 threshold의 정확한 합을 원 node energy로 바꾸지 않는다. 저장된 33×3 rate와 nonphoto의 전체 signed gradient/Hessian을 사용하며, lambda 관련 numerical tails와 He·node32의 극소 signed 기여도 유지한다.

## 3. 근 존재, 선형 역작용과 전체 혼합 미분

검토한 Banach 논증은 두 상자의 역할을 구분한다. Y는 exact centre±radius로 정의되는 닫힌 완비 상자이고 원 native X 안에 있다. K=I−CA의 가중 norm 상계 gamma가 1보다 작고, 모든 margin r−|CGc|−|K|r이 양수이므로 g−CG(g,theta)는 Y의 strict interior로 간다. 같은 derivative bound가 convex X 전체에 적용되므로 X 안의 근도 유일하다. 고정 C의 determinant가 0이 아니며, C² source chart와 가역 Jacobian은 이 유일한 근들을 같은 C² parameter 계열로 연결한다.

이 논증에 사용한 centre residual은 같은 coefficient family와 theta 전체를 포함한다. 서로 다른 parameter 또는 서로 다른 interval endpoint에서 뽑은 계수를 한 root family처럼 섞지 않는다. 경계 미분은 source 식의 작은 열린 수학적 연장으로 정의되며, native runtime의 허용 범위를 바꾼 호출을 요구하지 않는다.

코드의 역작용은 sum(k=0..3) K^k Cs에 radius_i × gamma^4 ||Cs||_r/(1−gamma)의 양·음 tail을 더한다. 이 식은 네 항 이후의 기하급수 꼬리를 모두 포함한다. K와 rhs가 서로 의존하더라도 각 실제 값의 interval 포함이므로 유효하며, 이 의존성 손실은 포함 폭에 반영된다.

Gas slot 0–3, lambda slot 4, birth slot 5의 대응이 원 source와 일치한다. W의 forcing은 원 G_lambda,b, G_g,lambda V, G_g,b U, G_gg[U,V]의 네 종류를 모두 포함한다. 저장 Hessian을 대칭화하거나 원 signed tail을 교체하지 않는다. 이후 energy 식은 다음 다섯 항을 모두 포함한다.

\[
W_e=d\{\mathcal E_gW+\mathcal E_{gg}[U,V]
+\mathcal E_{g\lambda}V+\mathcal E_{gb}U+\mathcal E_{\lambda b}\}.
\]

이는 같은 implicit energy 행을 두 번 미분한 정확한 chain rule이다. 온도에도 T_gW와 T_gg[U,V]가 모두 들어 있다. 별도 leading/remainder 분해는 U=dH+(I−A)U에서 나오며, M을 source rate로 바꾸거나 d→0 Taylor 근사를 사용하지 않는다. Direct energy와 먼저 투영한 energy의 overlap 검사는 진단으로만 쓰이고 source 항등식의 증명으로 제시되지 않는다.

## 4. 결과와 유한 상호작용의 판정

아래 값은 결과 JSON의 exact rational 구간을 바깥쪽으로 표시한 binary64 끝점이다.

| 항목 | Full | First_half |
| --- | --- | --- |
| gamma의 바깥쪽 상계 | 1.173683056367391e−4 | 5.853871499248869e−5 |
| det C의 양의 하한 | 0.9989733765062391 | 0.9994855624197574 |
| x self-map margin 하한 | 0.013221275908576044 | 0.01317995208132721 |
| w self-map margin 하한 | 0.43475378690754274 | 0.43455361464301717 |
| W_x | [−1.4640154020811193e−16, −4.625587031747189e−17] | [−1.8337498099688988e−17, −5.798310291160896e−18] |
| Direct ell[W], eV/H | [−1.5677099720350667e−15, 7.471154418415632e−16] | [−1.9635516724141098e−16, 9.339628114251213e−17] |
| 먼저 투영한 W_e 및 같은 계열의 I_e, eV/H | **[−6.192852956727484e−16, −2.012354998700877e−16]** | **[−7.75969827499494e−17, −2.5357316013204017e−17]** |

나머지 두 self-map margin도 양수다. W_w와 전체 observable Hessian을 포함한 W_T는 양수이며, helium 혼합 성분들은 0을 포함한다. Direct ell[W]의 0 포함은 원 결과로 남는다. 원 상자를 줄이거나 원 배열을 수정하여 energy 부호를 강제한 흔적은 없다.

같은 C² family에서는 I_e=e(1,1)−e(1,0)−e(0,1)+e(0,0)가 W_e의 단위 사각형 적분과 같다. Uniform interval과 사각형 넓이 1을 사용하므로 위 W_e 포함은 I_e도 포함한다. 네 native corner를 실행하지 않고도 이 수학적 결론은 성립한다. 단, 미계산 corner 값이나 실제 native issuer가 발행한 I를 관측했다고 주장할 수는 없다.

음의 I_e는 동일한 stage 이후 baseline에 대한 HH/birth의 가산 예측보다 결합 기체 에너지가 낮다는 뜻이다. 절대 에너지 감소, 순수 온도 상승, 전체 photon+gas+escape conservation 또는 장시간·continuum 부호와 같지 않다. 두 duration의 결과만으로 convergence order를 주장하지 않는다.

## 5. 보존 실행과 읽기 전용 점검

과학 계산의 실제 첫 실행은 `evidence/projected_first/EXECUTION.json`에 결박된다. Exit 0, elapsed 0.8762889720092062 s, Linux 최대 RSS 26,184 KiB이며 stderr는 0 bytes다. 45 s/384 MiB/파일별 16 MiB 제한이 기록되어 있다. 실행 전후 21개 bound 파일이 일치하고, 계약·interface·진단·interval primitive·wrapper의 5개 snapshot도 해당 실행 source와 일치한다. 새 과학 실패 또는 수정 재실행은 없다.

48개 assertion은 8개 의미 사례와 두 stage의 구조·도메인·산술 검사를 포함한 assertion 수다. 이를 48개 독립 물리 시험으로 읽지 않는다. 저장된 첫 결과의 모든 check가 PASS이며, 원 interval 표현 검사는 stage마다 7,096개다. 의미 사례에는 정확한 cancellation, 필수 Neumann tail, 부호/zero-touching, subnormal, 해석적 finite interaction과 잘못된 contraction/radius의 거절이 있다.

검토자는 원 프로그램이나 새 Rust checker를 실행하지 않았다. 별도 읽기 전용 표준 라이브러리 점검으로 다음을 확인했다.

- 결과와 oracle의 stage 목록·수치가 동일하고 stdout의 핵심 수치도 같다.
- 두 JSON에 저장된 709개 exact interval 표현에서 rational 순서, outward display, bit/display 대응 및 sign이 일치한다. 이 수는 직렬화된 표현의 수로 중복을 포함할 수 있다.
- TSV의 12,594행은 원 source Jet·leaf와 모든 endpoint word가 일치하고 누락·중복·추가 행이 없다. 원 mapped input의 negative-zero endpoint는 없으며 signed subnormal words는 그대로 남았다.
- 과학 실행에 사용한 21개 파일, 원 5개 snapshot 및 최종 고정 payload에 변형이 없다.

이들은 source 식이나 derived interval을 다시 계산한 과학 replay가 아니다. 새로운 초월함수 평가, source callback, compiler, gate, root/endpoint/IVP, 과거 suite 및 원격 mutation은 검토자 경로에 없다.

## 6. Rust와 NCP handoff의 정적 범위

최종 Rust는 dependency-free saved-data consumer다. 매 elementary operation의 outward binary64 포함, NaN/Inf·overflow·zero-containing divisor 거절, 전체 key 소비, 고정 C의 nonsingularity, strict contraction과 self-map margin을 확인한다. Gamma는 [0,upper], margin은 beta와 |K|r의 안전한 상계를 이용한 interval로 출력하므로 상계를 exact scalar라고 오인하지 않는다. Arithmetic environment probes는 관측된 부적절한 실행 모드를 거절하는 guard이며 모든 플랫폼의 IEEE-754 실행을 형식 증명한 것은 아니다.

Rust 의미 검사는 손으로 유도한 7개 합성 그룹이다. 정상 합성 evaluate 1회, 거절 합성 5회와 보존된 stage 2회는 구분되어 있다. Exact checker가 비교하는 50개 scalar interval은 stage당 scalar 4개, 네 길이-4 vector의 16개 성분, energy term 5개로 구성된다. Checker는 각 Rust 구간이 oracle의 exact rational 구간 전체를 포함하는지, 부호 label이 실제 끝점과 일치하는지, 보고된 다섯 항의 합을 projected-energy interval이 포함하는지 확인한다. 0 포함으로 넓어진 결과에서 엄격한 음수를 새로 만들지 않는다.

검토 중 nHe=0을 허용하던 generic Rust 조건과 Python의 nHe>0 조건 차이를 발견하여 생성자에게 알렸다. 생성자가 freeze 전에 nHe>0으로 통일했다. 두 실제 입력은 원래 양수였으므로 과학 수치 수정이나 재실행은 없었다. 최종 Rust SHA256는 `1c2c33f396a0e67a87c49859f331c74ccfc5e820475cc7206aba9bc13766ce9a`다. 현재 고정본에 남은 blocking finding은 없다.

NCP wrapper는 기존 compiler identity, offline build, gate, exact consumer를 각각 한 번으로 제한한다. Create-only 외부 run directory와 전후 source/input/compiler-entrypoint/binary identity, 실제 command와 raw logs, timeout process-group 종료 및 Linux wait4 자원 기록을 남기는 구조다. PHYS08 wrapper를 자동 호출하지 않고, 도구 설치나 native source route도 없다. 실제 compiler·빌드·gate·checker·wrapper는 연구 호스트에서 실행되지 않았다. 정적 코드 확인과 Python AST PASS를 Rust 실행 성공으로 바꾸지 않는다.

`prepare_predecessor.py`는 포함된 PHYS08 archive SHA, 133개 member, manifest 및 payload를 확인하고 새 경로에 bytes를 추출하는 helper다. 이 helper도 현재 실행되지 않았으며 과학 gate와 별개다. PHYS08의 같은 입력에 대한 실제 완료가 NCP에 있으면 evidence를 재사용하고, 미관측 최초 실행만 원 제한으로 수행하는 분기가 handoff에 있다. PHYS08 blocker가 독립적인 PHYS09 saved-input gate를 불필요하게 막지 않는다.

## 7. 채택하는 것과 그대로 남는 의무

`CLAIMS_PROJECTED_ENERGY.json`의 P09-01부터 P09-04까지를 위 전제와 범위에서 채택한다. Creator의 pending-review 문자열은 생성 시점 제안의 snapshot이고, 최종 채택은 이 비생성 결정과 `DECISION.json`이 정한다.

| 의무 | 이 결정 이후 상태 |
| --- | --- |
| 동일 HH leaf의 source energy cancellation | DERIVED, scoped 채택 |
| 원 source 전제 위의 uniform root, U/V/W, 에너지 5항 및 finite FTC | DERIVED + 실제 exact-rational 첫 실행으로 검증, scoped 채택 |
| 두 first-stage fixed-source 계열의 I_e<0 | 조건부 수학적 결과로 채택 |
| PHYS08 NCP 반환 | 2026-10-11 06:30:12 UTC의 명시한 조회 범위에서 미관측; 이후 완료는 NCP에서 관측·재사용 |
| PHYS09 Rust/compiler/gate/consumer | READY_NOT_RUN, 실제 NCP 첫 결과 대기 |
| Actual native root/U/V/W/I | null 유지, native authority false |
| 원 PHYS07 analytic-reference energy OPEN 및 NCP07 node32 per-node witness OPEN | 원 판정 그대로 보존 |
| Carried second_half, paired defect, time/continuum remainder, full49, production | OPEN |

검토자는 후속 Git publication이나 양쪽 backup 업로드 완료를 아직 관측하지 않았다. Core handoff의 완전성과 additive delivery 계획을 검토했으며 실제 commit/archive/object ID 및 ACK·metadata 완료는 root가 생성할 detached START/receipt/index를 따른다. ACK·metadata 확인과 실제 다운로드 restore를 구분해야 한다. 이 검토를 다시 검토하는 재귀 audit나 통과한 과학 계산의 반복은 요구하지 않는다.
