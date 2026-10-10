# PHYS06: 보관된 COMMON seed의 에너지 성분 진단

## 판정 범위

고정 입력 `inputs/ARCHIVED_COMMON_SEED_POINT_INPUT.json`의 저장된 binary64 수를 정확한 유리수로 올려 계산했다. 입력 SHA256은 `1f462e7fa7c1d4251c5004194c42b0e471fe5c42303962f1a40d5d5062f1923d`이며, 원 COMMON seed binary의 SHA256은 `678f967f0d50ad1fff47a73e2e63193429b708246cd84ca8ffc72191c31b522b`다. 소스는 NCP commit `4b9231a0eff113701e7178ad98624233f387dd15`에 고정되어 있다.

계산하는 N은 보관된 primary photon packet의 기존 stock이다. 방향별 합으로 교체하지 않았으며, 다음 endpoint의 remap·birth 뒤 preBE 입력이라고 해석하지 않는다. 밀도도 원 seed의 t0 값으로 고정했다. 두 d는 동일 점에서 비교한 수식의 매개변수이며, 시간 진화 결과나 승인된 dt가 아니다. 저장된 단면적은 원 provider를 Python binary64로 옮겨 산출한 값으로, 새 NCP Rust/libm 출력의 bitwise 확인은 아니다.

이 결과의 상한은 **고정된 광흡수 에너지 성분의 정확 유리수 진단**이다. 실제 혼합 gas response W, implicit root, parameter tube, finite interaction의 부호·remainder는 이 결과로 승인하지 않는다. 작성자는 이 진단의 생성자이며 최종 독립 판정자가 아니다.

## 계산식과 확인 방법

가스 좌표는 g=(x,y1,y2,w)이고, 기존 에너지 ledger와 맞는 matter 좌표는

\[
e=w+\chi_Hx+f_{\rm He}\chi_Iy_1+f_{\rm He}(\chi_I+\chi_{II})y_2
\]

이다. 고정된 각 그룹에서

\[
\kappa=c n_H[(1-x)\sigma_H+f_{\rm He}(1-y_1-y_2)\sigma_I+f_{\rm He}y_1\sigma_{II}],\qquad D=1+d\kappa,
\]

\[
\phi=\sum_j \frac{E_jN_j\kappa_j}{D_j},\qquad
\nabla\phi=\sum_j\frac{E_jN_j a_j}{D_j^2},\qquad
\nabla^2\phi=-2d\sum_j\frac{E_jN_j a_ja_j^T}{D_j^3},\qquad a_j=\nabla\kappa_j.
\]

닫힌 미분식을 확인하는 별도 계산은 x 방향의 분자·분모 다항식을 차수 2까지 나누는 일반 계수 recurrence를 쓴다. q0, q1, 2q2를 각각 φ, φx, φxx와 비교했다. 유한차분은 쓰지 않았다. 검증식은 같은 고정 물리 입력을 공유하므로, 원 native callback 자체에 대한 독립 구현 검증을 주장하지 않는다.

정확한 잔액

\[
d\phi=\sum_j E_jN_j-\sum_j\frac{E_jN_j}{D_j}
\]

과 Hessian의 rank 1 인수분해도 유리수로 확인했다. 결과 JSON에는 집계값의 정확한 분자·분모, 표시용 소수, 유리수 문자열 SHA256이 함께 있다.

## 수치 결과

고정된 matter energy는 **30.52960733831340474550377 eV/H**다.

| d (s, 비교 매개변수) | φ (eV/H/s) | ∂xφ (eV/H/s) | ∂xxφ (eV/H/s) | dφ (eV/H) |
|---|---:|---:|---:|---:|
| 625000000 | 8.536680343843970813573255e−13 | −9.817984430216069560041684e−12 | −2.285864947853798737909267e−13 | 5.335425214902481758483284e−4 |
| 1250000000 | 8.528057001271731044073367e−13 | −9.798159140595121775510760e−12 | −4.557889319463253811169635e−13 | 1.066007125158966380509171e−3 |

33개 에너지는 10–20 eV이므로 저장된 HeI·HeII 단면적은 모두 0이다. HI 단면적이 양수인 그룹은 16–32의 17개이며, 그중 저장 N도 양수인 16–24의 9개가 곡률에 기여한다. 두 비교 모두 Hessian은 음의 준정부호이며 rank는 정확히 1이다. xx 성분은 엄격히 음수이고, 다른 모든 Hessian 성분 및 y1·y2·w gradient는 정확히 0이다. 일반적인 세 종 정리는 이 점 결과와 별도로 구분해야 한다.

## 실제 소스 leaf와의 두 가지 경계

### 밀도 정규화

소스는 모델 nHe를 binary64(nH·stage.fHe)로 저장한 뒤, FT03 interval 부분에서 두 저장 밀도의 비를 사용한다. 따라서 정확한 실수로 해석하면 f̃He=exact(nHe)/exact(nH)는 stage.fHe와 다를 수 있다. 원 t0 값에서

\[
\delta f=f_{\rm stage}-\tilde f=\frac{518739254785749}{132286298964070155145850814201856}
\simeq3.921337726189180454150429\times10^{-18}.
\]

이에 따라 nonphoto 에너지 행에는 δf[χI F0_y1+(χI+χII)F0_y2] 보정이 필요하다. 여기서는 모델을 재정규화하지 않았다. `SOURCE_DENSITY_LEAF_CORRECTION.json`에 원 t0와 제안 endpoint 밀도의 정확 유리수 기록 및 소스 위치가 있다.

### 광흡수 excess-energy 뺄셈

[phys04_mixed.rs의 고정 원문](https://raw.githubusercontent.com/cosmosapjw-quantum/WU088_HH/4b9231a0eff113701e7178ad98624233f387dd15/research/r31ao_unequal_ladder/ncp_phys04_local_20261011_v2/candidate/src/phys04_mixed.rs) line 44는 E−χ를 먼저 binary64로 빼서 interval 상수로 넣는다. 따라서 일반 소스 그래프에는 εa=exact(χa)+exact(fl(E−χa))−exact(E)가 생길 수 있다.

이번 33×3 채널에서는 19개 inactive helium 채널에 ε≠0이 있지만, σ>0인 HI 17채널에는 ε=0이다. **99개 N·σ·ε가 모두 정확히 0**이므로 이번 점의 Eκ 에너지 행에는 이 뺄셈 오차 보정이 없다. 별도 일반 반례로 E=100 eV의 HI에서는 ε=−1/281474976710656 eV이고, 같은 E에서 HeI·HeII의 ε는 0이다. 따라서 이번 점의 Eκ 항등식과 곡률 판정을 전체 에너지 범위의 실제 구현으로 확장하려면 보정식 또는 별도 exact-subtraction 조건이 필요하다. 100 eV 값은 leaf 반례일 뿐, 새 spectrum이나 모델 실행이 아니다.

## 실행 증거

`archived_energy_run01`은 한 번 실행했다. exit 0, wrapper 벽시계 0.115214 s, script 벽시계 0.021308 s, 최대 RSS 11,648 KiB였다. 30 s / 256 MiB 한도를 지켰고 재실행은 없었다. 그룹별 정확 등식 198개, 집계 등식 6개, 두 d의 정확 에너지 잔액과 rank 인수분해가 모두 일치했다.

소스 subtraction leaf는 별도 read01에서 99개를 확인했고, 그 저장 결과를 재사용한 addendum에서 N·σ 가중 99개와 일반 100 eV leaf 3개를 계산했다. addendum은 exit 0, 0.046095 s, 최대 RSS 11,008 KiB였다. 원 에너지 진단은 다시 실행하지 않았다.

모든 단계에서 native endpoint, BE point solver, root producer, IVP, 기존 과학 suite, native FT03/LCS callback, 원 native decoder, native Rust provider 실행 수는 각각 **0**이다. 새로운 native 권한은 없으며 budget=0이다.

주요 산출물은 `archived_energy_point_results.json`, `archived_energy_run01.json` 및 첫 stdout/stderr, `archived_energy_photo_leaf_check.json`, `archived_energy_photo_leaf_addendum.json` 및 별도 코드·run01 ledger·stdout/stderr다.
