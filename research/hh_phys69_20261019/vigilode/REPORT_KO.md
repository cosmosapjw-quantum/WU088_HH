# PHYS69 VigilODE 적용·실행 보고

## 결과

원래 HH 외부 second Born 계수에 VigilODE의 adaptive RODAS5P matrix-free
구현을 실제 적용했다. 새 L28 적분 **2건**을 완료했고, 기존 PHYS68 Arb 인증서를
그대로 읽어 두 저장값의 참오차를 정확한 유리수 연산으로 제한했다. 기존 PHYS68
Arb/RK4, PHYS64 NCP20, PHYS66 완료 실행 및 VigilODE benchmark의 재실행은 **0건**이다.
HH_R10은 **OFF**다.

이 보고의 scope는 `B=27,T=65,k=7/10,m=0,(ell,ellprime)=(21,20),j=0..28`의
원래 external Born coefficient다. source-driven xi의 완료로 읽지 않는다.

| 항목 | 기본 요청 | 강화 요청 |
|---|---:|---:|
| 요청 파일 | REQUEST_L28.json | REQUEST_L28_TIGHT.json |
| rtol / scaled atol | 1e−10 / 1e−12 | 1e−12 / 1e−14 |
| angular nodes | 96 | 96 |
| 실제 accepted / rejected | 883 / 0 | 2277 / 0 |
| 실제 적분 시간 | 4.312257911 s | 10.309391728 s |
| 실제 analytic JVP vectors | 296688 | 765072 |
| 조립 Jacobian / 직접 분해 | 0 / 0 | 0 / 0 |
| max abs(F_j(B)−1) | 1.7202652031e−11 | 2.4472941955e−13 |
| 저장값 참 절대오차 상한, 위로 반올림 | 3.667970762e−58 a0^-1 | 2.911889512e−60 a0^-1 |
| 저장값 참 상대오차 상한, 위로 반올림 | 4.755593436e−11 | 3.775319802e−13 |

두 native 저장값은 각각

\[
\widehat D_{2,10}=(7.017743632541892+3.200163222549467i)\,10^{-48},
\]
\[
\widehat D_{2,12}=(7.017743632813095+3.200163222306804i)\,10^{-48}
\]

이다. 위의 십진 표기는 표시용이며, 원래 binary64 값의 정확한 유리수는 각
`CERTIFICATE_COMPARISON.json`에 들어 있다. rtol/atol을 100배 작게 했을 때
이 두 저장값의 실제 오차는 약 126배 감소했다. 이것은 같은 sandbox의 두 제한된
실행 결과이며 다른 solver와의 속도 순위나 전체 tolerance 범위의 수렴 정리를
주장하지 않는다.

실제 결과는 다음 디렉터리에 고정했다.

- 기본: `run_l28_rtol1e10_recovery2/`
- 강화: `run_l28_rtol1e12/`

각 디렉터리는 요청, 재사용 seed, 실행 명령/종료 상태/소요시간, native stdout,
정규화한 RESULT, 원래 인증서와의 대조, 엔진 소스·바이너리·결과 해시를 보존한다.

## 기존 결과를 먼저 확인한 범위

VigilODE의 원격 [PR71](https://github.com/cosmosapjw-quantum/vigilode/pull/71)
HEAD `fa07baf27a37674848d963e30e010d54e4af3f33` 및 관련 source/benchmark commit을
대조했다. 구현에 사용하는 commit은
`a21d573980f66fe02891bd216153443b5352f921`이고, 기존 CT 측정의 실제 commit은
`8a8bd409b1d96c7b7421f496d229e119fd3d284e`다. 두 commit 사이의 Rust 변경은 0이다.
이 사실을 근거로 측정 identity를 a21d573으로 바꾸지 않았다.

새 백업 CT CSV 2700행은 원격 PR71 파일과 바이트 단위로 같았다.
새 `VigilODE_VODE_Diffsol_Comparison_20261019.zip`의 manifest payload 10개도
모두 검증했고, 저장된 VODE 20행과 비교 노트를 읽었다. 포함된 실행 스크립트를
재실행하지 않았다. 입력 tolerance와 실제 달성 오차가 다를 수 있다는 CT 결과를
반영해, 새 HH client는 종점으로 직접 착지하고 독립된 기존 Arb certificate로
저장값을 대조한다. 원자료 pin과 SHA는 `SOURCE_PIN_AND_REUSE.json`에 있다.

## 실제 구현과 채택한 패키지

새 native crate는 다음을 구현한다.

- 원래 복소수 Coulomb 상태 F,F′와 두 q 행, D2를 실수 상태로 표현한다.
- tau=65−r를 사용해 증가 방향으로 적분한다.
- q에는 정확한 2^80, D2에는 정확한 2^160을 곱한다.
- 원식의 V=2(1+1/d) exp(−2d), bilinear 곱, 해석적 JVP와 고정 상태의
  시간 편미분을 사용한다.
- VigilODE의 PI 제어, strict max-step, GMRES-into, 재사용 LS workspace를
  실제 호출한다. 출력에 interpolation을 쓰지 않는다.
- seed/source/요청의 identity, endpoint의 개수·차원·유한성, 실제 work counter,
  complete/partial 구분, timeout과 실패 영수증을 처리한다.

VigilODE는 git commit으로, num-complex **0.4.6**과 gauss-quad **0.3.2**는
정확한 crate 버전으로 채택했다. gauss-quad의 공식 Gauss–Legendre 구현은
기존 RK4 경로의 node 생성과 다른 실제 angular 구현을 제공한다. 패키지 검색,
라이선스, flint-sys/rug/Diffsol/scirs2의 적용 가능성과 선택 이유, 모든 미분식은
`THEORY_AND_REUSE_KO.md`에 있다. Cargo.lock은 transitive dependency도 고정한다.

## 검증과 실패 기록

새 Python 검증은 **25개의 고유 테스트 PASS**, 새 Rust kernel 검증은
**7/7 PASS**다. Python 첫 실행은 24 PASS와 test fixture 오류 1 FAIL이었다.
해당 fixture가 Fraction에 문자열 둘을 넘긴 오류를 정수 변환으로 고친 뒤
그 테스트 하나를 재검증하여 PASS를 확인했다. 첫 실패와 표적 재검증 로그를
둘 다 `validation/`에 보존한다.

Rust 검증은 Gaussian moments/기저 정규직교성, 해석적 JVP와 중심 유한차분의
대조, 해석적 시간 편미분 대조, 정확한 스케일 관계, 시간 방향과 D2의 켤레 없는
곱, 잘못된 state/denominator 거부, angular cache의 키와 불변성을 실제 확인했다.

최초 두 Cargo build 시도는 공유 sandbox의 ENOSPC로 컴파일 단계에서 실패했다.
이때 Rust test case 및 물리 적분은 시작되지 않았다. 실패 로그는
`run_l28_rtol1e10/`, `run_l28_rtol1e10_recovery1/`에 있다. 원래 연구 결과를
삭제하지 않고 이번 작업의 재생 가능한 checkout을 정리한 뒤, 동일한 source와
기존 컴파일 cache를 사용해 `--offline`으로 빌드를 완료했다. 성공한 Rust test
command의 wall time은 208.208초, 그 뒤 CLI build는 2.724초였다.

완료한 두 결과에 실제 `--resume`을 적용했다. **2건 재사용, 새 적분 0건**이고,
각 run 디렉터리 payload SHA는 전후 동일했다. `validation/RESUME_READBACK.json`
은 이 검증을 기록한다. 기존 실행을 반복하는 대신 저장된 결과를 재사용한다.

검증된 바이너리는 5,637,232 bytes이며 SHA256은
`1ccc69012f39b7e303359a177f80f5bf7038fb371b6d8a0acd3659c5e2c7c481`이다.
독립된 보존 경로에 복사하여 hash와 실행 가능성을 확인했다. 과거 science 및
소스, 이번 두 실제 결과는 보존하고 재생 가능한 target cache만 정리했다.
정확한 경로와 시각은 `validation/BINARY_PRESERVATION.json` 및
`validation/CARGO_TARGET_CLEANUP.json`에 있다.

## 인증 범위와 후속 실행

Arb certificate의 원래 SHA256은
`ddaae206009a276def281af5526851ceb717baf2e0de5f8472552a9db340de9a`다.
그 dyadic midpoint/radius와 기존 radial-tail 정리를 그대로 읽었다. 새 후처리는
native float를 정확한 Fraction으로 바꾸고 정수 isqrt로 거리의 양쪽 한계를
구한다. 따라서 **이 두 저장된 값에 대한 참오차 상한**은 기존 인증서로부터
따르지만, VigilODE의 일반적인 전역 오차 또는 f64 angular/Coulomb/roundoff
전체에 대한 독립된 일괄 인증서는 아니다.

두 L28 실행은 완료되었으므로 NCP에서 반복하지 않는다. 새 L64 요청은
**NOT_RUN**이며 다른 j 합이므로 L28 인증서로 인증하지 않는다. L64에서는
원래 512-bit Coulomb initializer에서 만든 대응 seed를 받아 이미 작성된
runner를 실행할 수 있다. 먼저 원격/백업의 같은 fingerprint 실행이 있는지
확인한다. 완성된 NCP 명령과 offline 조건은 `native/phys69_vigilode/README.md`에 있다.
NCP에 solver 설계는 전가하지 않는다.

| 분리한 상태 | 이 모듈의 상태 |
|---|---|
| 실제 유도 | 원식·시간 변환·스케일·해석적 JVP/시간 편미분 완료 |
| 코드 | 기록된 engine SHA로 고정, 기존 PHYS68 코드 변경 0 |
| 실제 검증 | 새 고유 테스트 32개 PASS, 새 L28 물리 적분 2건 완료 |
| 결과 재사용 | 두 새 완료 결과 resume 성공, 새 적분 0 |
| 게시 | 통합 DELIVERY와 실제 remote readback에서 별도 추적 |
| 백업 | 통합 DELIVERY와 실제 backup receipt에서 별도 추적 |
| DAG | native adapter 완료, optional L64 NOT_RUN |

PHYS63의 all-angular 질적 존재는 ESTABLISHED다. all-angular Born bound,
원래 source-driven xi, 원점/incoming adjoint 및 sigma(E)/Maxwellian k_HH(T)의
상태는 통합 PHYS69 연구의 각각의 증명·실행 결과를 따른다. HH_R10은 OFF다.
