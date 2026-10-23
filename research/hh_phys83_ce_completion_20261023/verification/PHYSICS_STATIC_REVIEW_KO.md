# 독립 정적 physics→code 검토

이 검토는 `CONTRACT.json`, 상속한 `PARENT_DERIVATION_KO.md`, 실제 `matched_ce.py`와 `frozen_star.py`, 새 `NUCLEAR_THERMAL_FAST_OWNERSHIP_KO.md`와 `nuclear_ownership.py`를 읽은 결과다. 수치 reference 또는 과학 grid를 실행한 증거가 아니며, 이후 runtime 검증은 별도 create-only receipts로 판정한다.

## 1. 원래 CE 문제와 연결

상속한 이론과 구현은 같은 source-native gap `10.20435 eV`, term degeneracy `g=(2,2,6)`, source incident energy/area 단위 및 shifted finite support를 사용한다. 구현은 forward source로부터 `W=(epsilon+Delta)*sigma_up`를 만들고 W를 선형 연결한다. Reverse source의 sigma를 독립 선형 연결하지 않는다. 따라서 같은 `M0`에서 up/down을 구성하여 얻는 detailed balance는 선택한 유한 operator의 정확한 대수 성질이며, raw reverse source의 반올림 오차나 물리적 tail의 confidence interval을 뜻하지 않는다.

Maxwell prefactor의 `100`은 velocity의 m/s→cm/s 변환이다. 원자 단면적의 a0²→cm² 변환은 별도이며, 두 변환을 중복하거나 생략하지 않았다. `M1/M0`는 excess energy 평균이다. Excitation incoming 평균에만 Delta를 더하므로 두 exact log-derivative 식의 threshold 항도 일치한다. 사건당 thermal exchange는 incoming mean 전체가 아니라 transition gap이다.

3-state generator에서 ground→upper는 `a_i=ne*q_up`, upper→ground는 `d_i=ne*q_down+A_i`다. 구현의 두 upper 식은 이를 ground-start로 줄인 정확해와 일치한다. 누적 gross upward/downward/radiative counts는 각 상태의 occupation integral을 곱하는 사건 회계다. 그 값은 확률이 아니므로 1보다 커질 수 있다.

`thermal_change_eV=-heat_withdrawal_eV`로 상속 문서의 Qth 명칭 충돌을 해결했다. Primary thermal packet을 atomic storage와 radiation의 합으로 계산하면서도 raw gross-event 차이와 residual을 따로 보존한다. 따라서 constructed closure와 독립 numerical check를 구분할 수 있다. 독립 verifier는 raw event thermal 값도 mp80 occupation reference와 비교한다.

## 2. 복사 owner와 의미

2s branch의 `A_2gamma=8.229/s`와 `A_M1=2.496e-6/s`가 별도 count로 남는다. 2p의 `A_E1=626000000/s`도 별도다. Two-photon event의 photon number는 2, total energy는 Delta다. 각 photon의 spectrum이나 반쪽 에너지 monochromatic line은 구현하지 않는다.

Native radiative owner를 함께 활성화하는 입력은 거부한다. Immediate escape는 현재 선택한 optically thin closure이며 일반적인 radiation transport의 결론이 아니다. 고정 T/ne의 energy ledger를 coupled thermal/charge trajectory의 bound로 해석할 수 없다. Coronal 오차 식은 이 유한 star의 stationary radiation과 비교한 값이다. Higher levels, LS 2s↔2p mixing, opacity 등을 포함한 실제 high-density H I의 오차 한계가 아니다.

형식적인 A=0 collision-only limit와 arbitrary initial state는 이 API에서 노출하지 않는다. 따라서 그런 입력을 numerical coverage에 포함했다고 주장하지 않는다. Root coincidence는 독립 helper 검증으로 제한하고, source rate와 owner 계약을 깨는 artificial RatePair로 물리 모형을 확장하지 않는다.

## 3. 정적 결함과 수정 범위

초기 `FrozenHIStar`는 RatePair의 저장 log 값으로 detailed balance를 확인하면서 실제 q와 log의 일치 및 log 유한성을 확인하지 않았다. Frozen dataclass의 새 객체를 `replace`로 구성하면 실제 q를 바꾸고 기존 log를 보존할 수 있었으며 NaN log도 비교를 통과할 위험이 있었다.

이 문제는 실제 수치 실행 전에 parent에게 보고했다. 초기 source와 finding은 `prevalidation_frozen_star_v1.py`, `PREVALIDATION_GUARD_FINDING.json`에 보존했다. 현재 코드의 공통 T domain, finite log, q/log coherence, underflow flag 및 finite-source scope 검사 추가를 정적으로 확인했다. Negative-input runtime 검증은 별도 verifier가 맡는다. 이 수정은 source나 physical model, 허용 오차, science grid를 바꾸지 않는다.

## 4. 핵 열/fast 소유권의 연결과 구현 경계

새 이론의 normal-frame event 항등식은 `Egamma+Kc-Kin-Q=0`이다. Incoming COM kinetic energy와 normal-frame total incoming kinetic debit을 구분했고, boost와 finite-T event averaging의 조건을 명시했다. 선택된 fast-first capture에서 thermal nuclei 2개를 제거하고 fast daughter 1개를 만든다. Rest, thermal kinetic, fast kinetic, photon의 signed energy는 각각 `-Q, -Kin, +Kc, +Egamma`다.

Continuous stopping은 에너지만 이동한다. Assimilation은 실제 남은 kinetic energy와 particle number를 동시에 한 번 옮긴다. Prompt-thermal은 별도의 명시적 선택이며, 두 ownership 경로를 동시에 적용할 수 없다. 같은 normalized positive event weights를 모든 에너지 성분에 적용하는 함수는 zero total weight일 때 conditional mean을 `None`으로 남긴다.

`u=(3/2)nthermal*kB*T`에서 number source와 expansion을 함께 미분한 temperature source의 부호와 단위가 이론 식과 일치한다. `kB*T*(3+alpha)`는 equal-T, zero-drift NR Maxwellian에서 COM energy와 reaction-selected relative energy를 더한 조건부 결과이며, T-independent sigma 및 미분·적분 교환 조건을 별도 요구한다.

실제 adapter는 **공급된 scalar normal-frame energy record와 상대 weight를 소비하는 detached ledger**다. COM→normal four-vector 구성, mass shell, physical finite-T weight, isotope stoichiometry, 실제 nuclear rate, stopping law, fast tensor/transport를 구현한 것으로 표시해서는 안 된다. 이 항목들은 후속 provider의 OPEN 의무다. 기존 PHYS81의 완료 kinematics를 재실행하지 않았다.

## 5. 현재 판정

원래 유한 문제의 식→코드 연결과 source/owner 범위는 정적 검토상 일치한다. 위 guard 결함은 실행 전 수정됐으며 runtime falsification 대상으로 남겼다. 그 밖의 정적 physics 결함은 확인하지 못했다. 이 판정은 수치 pass나 production admission을 대신하지 않는다.

Non-tilted LRS Bianchi I, reacting gas pi=0, 별도 collisionless DM pi_m 및 fast tensor의 소유권을 유지한다. 총 tensor diagnostic은 같은 normal frame의 signed 성분을 합한 뒤 norm을 취해야 하며 Frobenius와 half-contraction의 sqrt(2) 관계도 유지한다. 이 단원의 scalar ledger 검증은 그 전역 tensor pipeline의 새 검증이 아니다.

HH_R10=OFF. Production admission NOT_ISSUED.
