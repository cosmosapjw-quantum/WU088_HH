# PHYS11 수치 결과의 물리적 해석

PHYS11은 PHYS10의 총 잔존 광자 에너지를 **33개 spectral group의 값·λ 미분·b 미분·혼합 미분**으로 풀어 보존했다. 동시에 흡수·HH 반응·열팽창 work와 source-derived escaping loss를 연결하여, 기체와 광자의 혼합 에너지 수지가 어떤 항으로 닫히는지 확인했다. 아래 결과는 같은 고정 소스 계수와 조건부 C² root family의 **numerically checked / implementation-verified** 포함이며, native root 또는 실제 carried second_half의 결과가 아니다.

## 1. 양의 총 광자 혼합량은 spectral하게 균일하지 않다

두 단계 모두 33개 group 가운데 **node 24 하나만 엄격한 양수**, node 16–23의 8개는 엄격한 음수이고, 나머지 24개 구간은 0을 포함했다. node index는 0부터 센다.

| Group | 에너지 | 잔존 photon mixed response |
|---|---:|---|
| 16–23 | 13.6–13.6875 eV | 8개 모두 엄격한 음수 |
| 24 — 직접 birth node | 13.7 eV | 엄격한 양수 |
| 0–15, 25–32 | 나머지 고정 node | 현재 포함은 0을 포함 |

Birth node 24의 mixed photon 수 포함은 Full에서
`[1.4814519834720054e−17, 4.522130822032077e−17] photons/H`, first_half에서
`[1.858781396830302e−18, 5.665152986139012e−18] photons/H`다. 비교하면 바로 아래 node 23의 Full 포함은
`[−3.9589591192267693e−20, −1.2438246332710034e−20] photons/H`다.

따라서 PHYS10의 양의 총 photon mixed energy가 모든 기존 photon group의 양의 혼합 효과를 뜻하지는 않는다. 직접 birth가 들어가는 13.7 eV group의 양의 기여와 기존 저에너지 stock의 음의 기여가 함께 존재한다. Quotient 미분에는 birth numerator와 opacity 변화의 교차항이 들어가므로, photon stock만 전달하고 두 일차 미분을 버리면 이 구조를 잃는다. 같은 단위 parameter 사각형과 같은 C² family에서는 uniform mixed derivative의 부호가 각 group의 finite interaction 부호로도 이어진다. 0을 포함한 24개 결과를 실제 0으로 판정하지 않았다.

## 2. escaping loss와 thermal work를 포함한 에너지 수지

이번에 추가한 escaping loss는 원 nonphoto source에서

\[
\Gamma_*=-\widehat\ell F^{np},\qquad
\widehat f=\operatorname{exact}(n_{\rm He,stored})/\operatorname{exact}(n_H)
\]

로 정의한 관측량이다. 원 controlled threshold가 CHI와 일치함을 소스에서 확인했으므로, 이는 해당 exact-real FT03 source의 RR·DR escaping losses다. 실제 native escape derivative export는 여전히 없다.

PHYS10에 ΔEesc,*=dΓ*와 ΔWth=2dHmean w를 더하면

\[
e^++e_\gamma^++\Delta E_{esc,*}+\Delta W_{th}
-e^- -E_\gamma^{in}=d(J_{norm}+\Psi)
\]

가 된다. 초기 gas가 θ-independent이고 incoming photons가 b-affine인 현재 두 첫 단계에서는, 네 출력 에너지의 **finite interaction 합**에도 다음 uniform mixed 포함이 적용된다.

| 항목 | Full | 같은 COMMON의 first_half |
|---|---:|---:|
| 증대 mixed 잔여, eV/H | `[−5.788230243389953e−40, 6.862357933552255e−39]` | `[−6.9733119029796365e−40, 8.2693439649913e−39]` |
| source-derived escape mixed, eV/H | `[−2.7907756952147026e−19, 2.787417411584523e−19]` | `[−1.7472999977840642e−20, 1.7451970205780317e−20]` |
| thermal-work mixed, eV/H | `[1.0578055231115218e−20, 3.440303431567093e−20]` | `[6.625765892416593e−22, 2.1530516342080285e−21]` |

이 작은 잔여는 **에너지 수지에 물리적으로 해당하는 항을 추가하고 공통 소스 항을 식에서 먼저 상쇄한 결과**다. PHYS10과 동일한 관측량의 수치 정확도가 수십 자리 향상됐다는 뜻이 아니다. 또한 전역 물리 에너지 보존을 10⁻³⁹ 수준으로 확인한 값이나 실제 적분기 오차도 아니다.

현재 표시된 잔여는 Jnorm 쪽에서 지배되고, captured heat defect Ψ의 mixed 기여는 binary64 외향 표시에서 ±최소 subnormal이다. 정확한 유리수 tail은 결과 파일에 보존돼 있다. f−fhat는 Full에서 약 3.80578×10⁻¹⁹, first_half에서 약 7.32583×10⁻¹⁸로 후자가 더 크다. 이 때문에 first_half의 증대 잔여 포함이 Full보다 조금 넓을 수 있다. 두 결과로 시간 수렴 차수를 추정할 수 없다. 증대 잔여는 모두 0을 포함하며 정확한 0과 실제 부호는 미정이다.

별도로, source-derived escape의 값 포함 자체는 interval dependence로 음수 끝점까지 넓어져 있다. 원 소스에서 유도한 물리 값의 비음수성과 모순되지 않는다. 이 넓은 값 포함이나 0을 포함한 escape mixed 구간을 음의 실제 escaping energy의 증거로 해석하지 않는다.

## 3. 반응 ledger와 다음 단계의 의미

흡수 photon 수의 mixed 포함은 두 단계 모두 엄격히 음수다. Full에서는 `[−4.518742300414275e−17, −1.4706227826893267e−17] photons/H`다. HH event mixed 역시 Full `[−1.0130997487450332e−16, −3.1480245244711963e−17] events/H`로 엄격히 음수이며, 같은 χH를 곱한 threshold thermal contribution의 mixed 부호는 양수다. 이는 절대 이벤트 수가 음수라는 뜻이 아니라, 두 미래 매개변수의 결합 효과가 단독 효과의 가산 예측보다 작다는 뜻이다. source_n과 source_u의 원 함수는 b-affine이고, 저장된 mixed signed tails는 그대로 남겼다.

이제 동일 source-family의 group·반응·에너지 carry를 다음 단계의 수학적 입력으로 사용할 수 있다. 실제 다음 단계에는 θ-dependent 이전 gas와 incoming photons의 일차·혼합 미분을 모두 전달해야 한다. 현재 group 결과만으로 실제 angular/guard 배열을 복원하거나 source와 native distribute의 coefficient graph를 동일시하지 않는다. 과거 HH ON과 primal compensation도 미래 derivative ledger와 별도로 보존한다.

성공한 수정 실행 `carry_v2`는 **4.029582590초, 최대 RSS 29,900 KiB**, exit 0으로 끝났고 **168 assertions / 8 semantic cases**를 기록했다. 첫 시도의 실패는 `old_gas`가 bare interval이 아니라 full Jet인 입력 schema 처리 오류였으며, 원 로그와 후보 snapshot을 보존한 뒤 parser만 수정했다. 입력·정밀도·허용오차는 바꾸지 않았다. 새 source callback·inverse solve·native root·과거 과학 실행 재수행은 모두 0회다. 따라서 이 단계의 NCP heavy queue는 비워 두는 것이 실제 비용에 맞는다.

근거: `results/carry_v2/SUMMARY.json`, `results/carry_v2/CARRY_RESULTS.json`, `evidence/carry_v2/EXECUTION.json`, `evidence/FIRST_FAILURE_AND_CORRECTION.json`. 이 해석 문서의 작성자는 저장된 결과를 읽었으며 과학 코드 수정이나 새 실행을 수행하지 않았다.
