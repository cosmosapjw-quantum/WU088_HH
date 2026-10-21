# PHYS78 atomic PI+RR 구현 — C5–C7

## 전달 결과

`phys78_impl/source/atomic_network.py`는 입력→number/energy RHS까지 실행 가능한 NumPy 모듈이다. Root 소유 geometry·driver 파일은 수정하지 않았다. 테스트는 `phys78_impl/tests/test_atomic_network.py`, 원본자료는 `phys78_impl/vendor/atomic/photo.dat`, `rec_table1.dat`에 있다. 두 author table의 SHA256이 원본 REI210 manifest와 일치하고 prepare 시 embedded 여섯 elemental coefficient row를 원문과 대조한다.

현재 source SHA256: `2e8b5f892961ebf60fb21fe90895c961fde423689634684305c58ba34830bab6`.

## 사용 인터페이스

```python
import atomic_network as atomic
net = atomic.prepare_network((18., 30., 60.))
y = atomic.neutral_abundances()  # 21 nuclear/ionic states, per reference H1
out = net.rhs(T_K=300., nH_cm3=0.002,
              species_abundance_per_H=y,
              photon_number_cm3=[0., 0., 0.])
```

상태 순서는 `H1_I,H1_II,D_I,D_II,T_I,T_II,He3_I,He3_II,He3_III,He4_I,He4_II,He4_III,Li6_I,Li6_II,Li6_III,Li6_IV,Li7_I,Li7_II,Li7_III,Li7_IV,n`이다. `SPECIES_INDEX`로 조회하는 것이 안전하다. `electron_abundance_per_H=CHARGE@y`, `electron_density_cm3=nH*electron_abundance_per_H`이며 electron을 별도 적분하지 않는다.

`out.dsdt`는 abundance/H/s. 다음 에너지들은 eV/H/s다.

- `photo_absorbed_eV_per_H_s`: 광자에서 흡수된 전체 에너지.
- `photo_heat_eV_per_H_s`: photo excess kinetic heating.
- `rr_kinetic_cooling_eV_per_H_s`: RR가 제거한 electron kinetic energy.
- `heat_eV_per_H_s`: photo heat − RR kinetic cooling.
- `rr_escape_eV_per_H_s`: RR binding+kinetic escape energy.
- `binding_derivative_eV_per_H_s`: `binding_eV@dsdt`.

`photo_absorbed - heat - binding_derivative - rr_escape`를 energy residual로 저장한다. `photon_absorption_per_H_s` 및 `photon_absorption_cm3_s`를 모두 제공하므로 root는 photon state의 정규화에 맞는 것을 한 번만 사용한다. `nucleus_count_per_H`, `nucleon_count_per_H`, `binding_eV_per_H`, `d_electron_per_H_dt`도 반환한다. H 또는 ln(a) 시간 변환은 이 모듈에 없다.

광자의 실제 gray mean energy가 변하면 `net.rhs(..., photon_energy_eV=E)` 또는 `net.with_photon_energies(E)`가 cross sections를 갱신한다. 원본자료와 transition layout은 재구성하지 않는다. 모든 mean energy는 양수이고 LiI fit Emax64.39eV 이하여야 한다.

## 최적화와 유효성

한번 준비한13 transitions, stoichiometry, elemental coefficient mapping, photon kernel, Jacobian sparsity를 작은 연속 NumPy arrays로 재사용한다. H/D/T, He3/4, Li6/7의 원자 계수 공유는 명시한 isotope-blind approximation이다. isotope별 abundance와 flux는 각각 남는다. Numpy arrays는 immutable bytes를 바탕으로 하므로 caller가 writeable flag를 다시 켤 수 없다.

VF96 RR의 kinetic capture는

\[
\epsilon_{\mathrm{cap}}={k_BT\over2}\left[
{1-b\over1+\sqrt{T/T_0}}+{1+b\over1+\sqrt{T/T_1}}\right]
\]

를 사용한다. 이는 `kT(3/2+dlnalpha/dlnT)`와 같고 큰T에서 뺄셈 cancellation을 피한다. Source-fit domain3–1e9K를 강제한다.

기본 RHS는 negative state/photon population을 거절하며 clipping이 없다. Stiff solver의 intermediate stage에는 `allow_solver_extension=True`가 가능하다. 기본허용폭은 isotope total의1e-10이고, caller가 `solver_extension_scale_per_H`로 고정규모를 명시할 수 있다. 이 경로는 원래 signed state로 flux를 평가하며 작은 음수를0으로 치환하지 않는다. 지표에 solver-extension 여부와 음수 좌표 수를 남긴다. Photon과 derived electron density는 여전히 nonnegative여야 한다. Accepted physical histories 검사는 별도다.

기본 abundance는 지정받은 PRIMAT median D/H2.460e-5, He3/H1.074e-5, Li6/H1.20e-14, Li7/H5.627e-10, He4 mass fraction0.24709를 사용한다. He4/H는 다른 trace nuclei의 A-weighted mass를 포함해 변환했다. T=n0. 이 초기 charge distribution은 neutral이며 matched recombination history를 주장하지 않는다.

## 실제 검증

명령:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python -m unittest discover -s phys78_impl/tests -p test_atomic_network.py -v
```

최종14 unique tests가PASS(exit0), unittest 시간0.170s였다. 처음11개PASS 이후 요구된 source binding·dynamic photon energy·explicit solver extension 세 검사를 추가했다. 따라서 unique test 수는14이며25가 아니다.

원문 SHA+계수대조, independent Decimal PI/RR anchors, 단위변환, RR capture analytic derivative, isotope/nucleon/charge conservation, 모든 coordinate boundary의 quasipositivity, number+thermal+binding+photon energy balance, dark-neutral/pure-RR limits, fit Emax/Tdomain, negative state 거절, immutable arrays, electron-feedback Jacobian sparsity를 점검했다. 실제14개 test 이름/출력은 `ATOMIC_TEST_STDOUT.txt`, exact command/source identities는 `ATOMIC_IMPLEMENTATION_CHECK.json`에 있다.

## 현재 과학적 경계와 다음 작업

이 모듈은13PI+13RR channel이다. Nuclear reaction, beta decay, charge exchange, CI, molecules, DR, secondary electron 처리는 명시적으로 제외했다. 특히 n/T0 default 보존은 beta-decay 구현 증거가 아니다. Isotropic baryons의 anisotropic stress는0이라는 fluid closure이며 별도 DM/radiation anisotropic tensor가 root 결합계에서 계산된다. 전체19목표반응 구현 또는 full primordial reionization/production admission을 발급하지 않는다.

이 하위 업무의 new ODE/NCP/benchmark는각각0회다. C7 검증은 point algebra/source/energy closure에 제한된다. 다음은 root의 geometry+photon+gas IVP 연결, 소수 실제 exploratory pilot, accepted-state/energy/tolerance 확인, plot readback이다. HH_R10=OFF를 유지한다.

`skill_context_used`: physmath-research-loop1.3.0 SKILL.md 및 POLICY_INTEGRATION/CODING_LOOP/SUBAGENT_MODE를 실제 열람했다. 부모가 배정한 C5–C7 atomic module 범위 안에서 구현·시험을 수행하고 원본 scientific execution과 독립 상태로 기록했다.
