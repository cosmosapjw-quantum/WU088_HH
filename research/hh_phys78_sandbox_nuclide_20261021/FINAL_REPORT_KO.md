# PHYS78: 샌드박스에서 완료한 LRS Bianchi I 동위원소 pilot

## 1. 결과와 적용 범위

2026-10-21 UTC에 이 샌드박스에서 **31개 parameter point의 z=20→2 적분과 10종 그림(PNG/PDF)을 완료했다.** 별도의 한 점에서 quadrature와 ODE 허용오차를 함께 강화한 정련도 완료했다. 실행에 Rust, NCP 접속, 외부 반응률 다운로드는 필요하지 않았다. 사용한 Python 패키지는 `requirements.txt`에 고정했다.

완료 범위는 **등방 반응성 H/D/T/He/Li 기체 + 비등방 collisionless 비바리온 물질·자유 복사 + 보존적으로 결합한 gray PI/RR**라는 유한 탐색 모형이다. 이는 PR132의 실제 미완료 DAG `FULL_NATIVE_COLD_EOR`에 속하는 실행 가능한 자식 단계다. 그 상위 의무 전체를 닫지는 않았다. 사용자 그림의 19개 핵·원자 반응 전체가 활성화된 핵반응망, 분자/음이온, CI/CX, Compton/Thomson, 주파수·각도 분해 반응성 수송은 남아 있다. 특히 **현재 비영 물질 비등방 응력은 collisionless DM에서 나오며, 반응성 바리온 기체는 등방 closure로 π_gas=0이다.**

지정한 원시 동위원소의 모든 비음 전하 상태를 보존한다. Li III/IV 슬롯도 있으나 이번 18/30/60 eV 광원에서는 생성되지 않는다. 존재하는 슬롯과 실제로 활성화된 반응을 구별한다. 이 파일과 `DAG_OVERLAY.json`의 OPEN 표기가 최종 과학적 범위다.

`HH_R10=OFF`; production admission은 `NOT_ISSUED`. PR128 기준 구현을 대체하거나 기존 1231/729/63 이력을 다시 계산하지 않았다. 결과는 실제 remote descendant의 additive Draft PR133에만 게시하며 merge하지 않는다.

## 2. 선행 조사와 identity 조정

접근 가능한 6개 repository에서 1,060 refs, 최근 PR metadata 180건, 고정된 source file 26개, 알려진 backup ID 10개를 조사했다. source file 26개는 Git blob identity와 대조했다. PHYS75의 요청된 final delivery·post-publication handoff·DAG 및 PHYS77의 DAG/handoff도 실제 원격 bytes를 확인했다. 이 범위는 `evidence/INVENTORY_*`의 원본·identity 기록과 `inventory/`의 최종 확인으로 감사할 수 있다. 비공개 다른 ChatGPT 대화 전체를 읽는 기능은 사용할 수 없어, 모든 대화를 전수 확인했다고 주장하지 않는다. 이름 검색의 누락 가능성이 있어 기존 backup의 정확한 ID도 조회했다.

| 기준/기여 | 확인된 identity | 사용 방식 |
|---|---|---|
| HH PR128 | `92f5ab9dba531ebe05909dcb77d3740d2c68c580` | 과학 기준 유지 |
| HH PR129 | `b76fd4b5d0dfe4850ebde66a8a10f78402d36c00` | signed attribution 보충 범위 유지 |
| HH PR132 | `d43cf2df2c4864ae05049f44301c5b389b80a49c` | 실제 descendant 부모 |
| REI PR199 D9 | `cce008b3fc32c298185b30550b2cd909d74fcd87` | 175×153 saved-history 결과 반영; ODE 재실행 없음 |
| REI PR217 ACCEL03 | `de73c5d6c7bd3498571e9226298040d8259e1acf` | moment response 재사용·대조 |
| BASS PR179 | `d14652646c1da77b6513e7f97725ff5dd5c1db4e` | ACCEL03 원본 계보 |
| REI PR210 atomic | `e4c8133288614638792888367ca10b2ded3138ff` | 저자 PI/RR 계수와 source-domain 재사용 |
| REI PR211 HHeD | `c9deb933761a8d2593d1176aee028cd423bdbc05` | 이온/동위원소 기여 조사 |
| HE31 / BASS_HE84 | `88e415c45d8607c85cd3ab36aabeaed4378820ce` | z20→4 donor; z2 완료로 승격하지 않음 |
| CR95 실제 branch | `8dc5031b3323d4be42a7444843294200aa8887f2` | stale PR snapshot과 구별; 고유 129 결과 |
| REC118 | `99f5f4fb57358a0347286f8299977125a2724774` | tiny sensitivity 2건과 미실행 full 3건 구별 |

게시 직전의 추가 HEAD 확인은 `inventory/FINAL_HEAD_REFRESH.json`으로 분리한다. 그 후 타 스레드의 변경 가능성은 다음 작업 시작 때 다시 확인해야 한다. 기존 PHYS75 Dropbox 보충 ZIP의 BLOCKED 기록을 이번 PHYS78의 성공으로 덮어쓰지 않는다.

업로드된 `원시 광핵반응 및 재이온화 네트워크(2).png`도 실제로 읽었다. 파일 SHA256은 `472ba6be633d2b5fc05fc1e0e88f965ff3c0311b0697e3c35c05bbca1629e6f9`이다. 최초 메시지의 missing-file 오류가 이 세션의 최종 접근 상태는 아니다. 그림의 19개 반응을 source registry와 대조했으나, 그림 자체를 반응률 데이터로 간주하지 않았다.

## 3. 최적화: 바꾼 계산과 보존한 계산

`source/kinetic.py`는 양의 canonical packet quadrature의 q², μ², 가중치를 한 번 준비하고 불변 객체로 사용한다. 동일 상태의 에너지 제곱근을 공유하여 밀도, 평행·수직 압력, signed stress와 response를 함께 계산한다. 다수 출력 시점은 제한된 크기의 batch로 처리한다. 각 worker는 독립 parameter point를 담당하고 BLAS/OpenMP 내부 thread는 1개로 제한한다. 이 구성은 반복 준비·반복 transcendental 계산·중첩 thread를 제거하기 위한 구조적 수정이다. **속도 배수나 benchmark 결과는 측정하지 않았다.**

기존 canonical FV 두 owner 및 ACCEL03 response를 9개 상태에서 직접 비교했다. 최대 절대 차이는 `2.220446049250313e-16`, derivative 상대 차이는 `2.3243077290757727e-10`이다. 이 비교는 유한 owner의 점별 동등성 증거이며 continuum quadrature 정확도를 증명하지 않는다. 원본 owner는 `vendor/`에 출처와 함께 보존했다.

미량 Li6까지 포함한 state의 크기 차이가 BDF Newton 예측을 불안정하게 만들었다. 따라서 양의 대각 행렬 D로 정확한 좌표 변환

\[
y=Dz,\quad z'=D^{-1}f(x,Dz),\quad \mathrm{atol}_z=D^{-1}\mathrm{atol}_y
\]

을 적용했다. 이때 각 성분의 `error/(atol+rtol*|state|)`는 동일하다. 반응식·물리 RHS·오차 척도를 변경하거나 허용된 최종 상태를 clipping한 것이 아니다. 첫 실패의 absent neutron `-5.89e-39/H`에 대해서는 명시적 absent-inventory stage tolerance `1e-28/H`를 두었고, 실패 기록과 snapshot을 보존했다. 첫 실패 source snapshot은 사후 reverse patch로 복원했음을 별도 receipt에 표시했다.

현재 SciPy BDF에서 domain-invalid Newton trial의 NaN은 조건부로 재시도를 유발할 수 있으나 invalid predictor/Jacobian이면 LU 단계에서 명시적으로 실패할 수 있다. 무조건 복구된다는 보장은 하지 않는다. 완료된 31 pilot에서는 negative stage 및 rejected-domain stage가 모두 0이었다. 실제 실패가 생길 때에만 해당 기록을 근거로 수정한다.

## 4. 동일 normal orthonormal frame과 norm

\[
a_\perp=a e^{-b},\quad a_\parallel=a e^{2b},\quad
x=\ln(a/a_0),\quad a_0=1/21,
\]

\[
\sigma_{\hat i\hat j}=\operatorname{diag}(-s,-s,2s),\qquad
\pi^A_{\hat i\hat j}=\operatorname{diag}(-p_A,-p_A,2p_A).
\]

물질과 복사를 각각 같은 normal tetrad에서 계산하고 `p_m`, `p_r`의 부호를 저장한다. 산출물의 기본 norm은 full Frobenius다.

\[
\Sigma_F=\sqrt6\frac{|s|}{H},\qquad
\Pi_{A,F}=\sqrt6\frac{\kappa_E|p_A|}{H^2},\qquad
\Pi_{\mathrm{tot},F}=\sqrt6\frac{\kappa_E|p_m+p_r|}{H^2}.
\]

SI 에너지밀도·압력과 proper time 초를 사용하는 구현에서 `κ_E=8πG/c²`다. Einstein 방정식의 `κ=8πG/c⁴`를 쓰는 표기로는 `κ_E=c²κ`이며, c=1에서는 구별이 사라진다. half-contraction `sqrt(T_ab T^ab/2)`의 해당 계수는 √3이므로 **Frobenius = √2 × half-contraction**이다. total은 tensor를 더한 뒤 norm을 취한다. `Π_m+Π_r`는 일반적으로 total과 다르다.

평균 팽창과 전단 방정식은

\[
3H^2=\kappa_E\rho_E+\Lambda c^2+3s^2,\qquad
\dot s+3Hs=\kappa_E(p_m+p_r),\qquad b'=s/H
\]

를 사용한다. 유한 packet의 에너지 연속식에는 `−6(s/H)(p_m+p_r)`가 포함된다. 별도 reviewer의 3개 내부 상태 directional check에서 total continuity와 Friedmann–Raychaudhuri 관계는 각각 최대 `3.94e-16`, `4.15e-16`의 상대 defect를 보였다. 이는 방정식 구현의 점별 검증이다.

같은 trajectory의 signed stress·tensor cancellation 그림은 조건부 성분 분석이다. 이전 `S=S0/I+Jm+Jr` 분해를 포함해 species-off 인과 실험으로 해석하지 않는다.

## 5. 실제 원자·동위원소 모형

| 핵종 | 전하 상태 | 초기 abundance/H | 이번 실행 |
|---|---|---:|---|
| H1 | I, II | 1 | PI/RR 활성 |
| D2 | I, II | 2.460e-5 | PI/RR 활성 |
| T3 | I, II | 0 | 0 유지; fraction 미정의 |
| He3 | I, II, III | 1.074e-5 | PI/RR 활성 |
| He4 | I, II, III | 약 0.08205168 | Yp=0.24709 및 trace 질량과 일치하도록 계산 |
| Li6 | I, II, III, IV | 1.20e-14 | I↔II; III/IV는 정확히 0 |
| Li7 | I, II, III, IV | 5.627e-10 | I↔II; III/IV는 정확히 0 |
| n | 중성 | 0 | 0 유지 |

합계 21개 nuclear/ionic state와 charge neutrality로 유도한 electron이다. 모형의 원소별 atomic fit은 isotope에 공통이고 각 isotope population은 별도로 적분한다. isotope shift·정밀 원자 질량은 이번 범위가 아니다. 초기 abundance는 PRIMAT 표의 중앙값을 사용한 탐색 초기조건이며 lithium abundance 관측 적합을 주장하지 않는다. 과거 붕괴 생성물이 반영된 abundance를 사용하므로 T/n의 유한 초기 population을 새로 주입하지 않았다.

실제 rate RHS는 **13 PI + 13 RR**다. 보조 stoichiometric registry의 22 species/43 channels는 정수 baryon number·charge 결함이 0인 구조 검사이며, 43개의 검증된 활성 rate를 구현했다는 뜻이 아니다. 사용자 그림의 핵반응·약붕괴는 별도의 rate/source 의무다.

PI는 Verner 등의 저자 table, RR는 Verner–Ferland 저자 table을 사용했다. 다음 bytes를 source identity에 포함했다.

| 자료 | SHA256 |
|---|---|
| `photo.dat` | `a53e73b0af4cc6b801aef67b84bd964e3ed8c9c4992f214e4a69dc7e4443f389` |
| `rec_table1.dat` | `2382f6896fe58ee1da58c9bd563fd7d02c0d94410dbd4150767eed26a54f5091` |

저자 PI 페이지와 partial/inner-shell 자료: <https://www.pa.uky.edu/~verner/photo.html>. RR 계수 및 3–10^9 K 적용 범위: <https://www.pa.uky.edu/~verner/rec.html>. PRIMAT 초기 abundance: <https://arxiv.org/html/1801.08023v3>. 실제 실행 SciPy BDF: <https://docs.scipy.org/doc/scipy-1.17.0/reference/generated/scipy.integrate.solve_ivp.html>. Exa·SciSpace 발견 metadata와 실제 Wolfram 확인은 `theory/EXTERNAL_DISCOVERY_METADATA.json`, `theory/WOLFRAM_*.json`에 보존했다.

## 6. 열·광자·source reservoir의 결합

33개 IVP state는 `b,q,Y[21],u,Nγ[3],Uγ[3],R_escape,Q_source,H0*t`다. 반응성 기체의 electron·thermal·binding energy가 H에 되먹임하고, gray 광자는 흡수·적색편이를 겪는다. source를 에너지 없는 외부 주입으로 처리하지 않고 양의 pressureless reservoir Q에서 차감한다. UV와 escaped RR 복사는 등방이므로 별도의 비등방 응력을 만들지 않는다.

reference H당 에너지 eV를 사용하여

\[
N_j'=\mathcal S_j-\mathcal A_j/H,\quad
U_j'=-U_j+E_{0j}\mathcal S_j-\bar E_j\mathcal A_j/H,
\]

\[
u'=-2u+(Q_{\rm PI}-Q_{\rm RR})/H,\quad
R'=-R+Q_{\rm escaped}/H,\quad Q'=-\sum_j E_{0j}\mathcal S_j
\]

를 결합했다. B를 ionization binding energy라 할 때 D=`u+B+sum(U)+R+Q`는

\[
D'=-2u-\sum_j U_j-R
\]

을 만족한다. source absorption과 recombination의 내부 교환은 상쇄된다. RR fit에서 유도한 유효 Maxwellian capture cooling은

\[
E_{\rm cap}=k_BT\left(\frac32+\frac{d\ln\alpha}{d\ln T}\right)
=\frac{k_BT}{2}\left[
\frac{1-b_{\rm VF}}{1+\sqrt{T/T_0}}+
\frac{1+b_{\rm VF}}{1+\sqrt{T/T_1}}\right]
\]

이며 양의 안정된 형태로 구현했다. 이는 이번 모형의 유도된 closure다. 독립적으로 검증된 모든 thermal-rate owner를 가져왔다고 주장하지 않는다.

초기 gas 300 K는 미리 가열된 탐색 시나리오다. source는 H당 ln(a)당 `8*uv_scale*logistic((8-z)/1.5)*[0.7,0.25,0.05]`, 고정 주입 에너지는 18/30/60 eV다. 관측으로 복원한 EOR 광원이 아니다. 마지막 에너지까지 Li I outer-shell fit의 64.39 eV 상한 안에 있지만 Li II/III의 75.64/122.5 eV 문턱을 넘지 않으므로 Li III/IV가 생성되지 않는다. hard UV를 넣으려면 Li I inner-shell·branching과 일관된 에너지 회계를 먼저 추가해야 한다.

gas는 이번에 25,371 K까지 도달했다. **CI/CX 생략이 이 온도에서 무시 가능하다고 검증하지 않았다.** 이것이 다음 physics→coding 의무를 선택하는 핵심 근거다. 핵광반응의 source 기여가 유한 60 eV cutoff 때문에 0인 것과 CMB의 Planck tail이 수학적으로 정확히 0이라는 주장은 서로 다르다. 후자는 주장하지 않는다.

## 7. 실행한 parameter sweep와 실제 결과

기본 27점은 signed `ΣF,0∈{-0.1,0,+0.1}`, `A_m,A_r∈{-0.8,0,+0.8}`, `uv_scale=1`이다. A는 양의 packet의 초기 quadrupolar angular anisotropy를 조절한다. isotropic packet의 `ΣF,0=±0.01` 두 점과 완전 등방 UV scale 0.5/2 두 점을 추가해 총 31점이다. 각 점에 161 epoch, 합계 4,991 epoch를 저장했다.

| 관측량 | 실제 저장값의 범위/최댓값 |
|---|---:|
| 초기 ΣF | 0–0.1 |
| z=2 ΣF 최대 | 0.005578856056502901 |
| Πm,F 최대 | 0.0005468865088172861 |
| Πr,F 최대 | 0.0023885550415890665 |
| Πtotal,F 최대 | 0.0029354415504063524 |
| T | 255.4376789706–25370.6630842477 K |
| xe | 0.0002–1.164109743658757 |

등방 입력의 약 10^-18–10^-17 성분은 유한 산술 residual로 별도 그림에 표시한다. 그 값을 물리적 최소 anisotropy로 설명하지 않는다. 주 로그 그림에서는 관측된 control 최대값 이하의 소수 sample을 생략하고, 각 panel에 기준과 개수를 명시했다. 값을 양의 floor로 대체하거나 데이터 자체를 수정하지 않았다. 그 cutoff는 검증된 오차 상한이 아니다. sweep 그림은 실제 점의 slice이며 보간된 연속 parameter surface가 아니다.

반대 부호인 P024에서는 초기 `|p_m+p_r|/(|p_m|+|p_r|)=0.6273906`이며 이후 약 0.965295까지 변한다. signed 성분과 tensor cancellation은 `02c_signed_tensor_cancellation`에 별도로 보였다. 14개 case에서 radiation sign 또는 norm 순서를 일부러 잘못 적용하면 탐지되었고, sum-of-norms 오류는 최대 약 `1.0938e-3`이었다.

| 그림 | 내용 |
|---|---|
| 01 | 실제 sweep 좌표·z2 전단 색상 |
| 02 / 02b / 02c | Σ, 분리된 Π, 등방 residual, signed cancellation |
| 03a / 03b / 03c | H/D/T/n, He3/He4, Li6/Li7 전하 이력 |
| 04a / 04b / 04c | 온도/electron, gray photon, 보존 진단 |

그림 10종은 작성 agent가 실제로 열어 검사했고, root도 핵심 01/02/02c/03c를 직접 확인했다. 03 계열의 대표 P013은 같은 UV=1 완전 등방 입력이며 각 isotope는 자신의 abundance로 정규화한다. n/T가 0이면 분율은 미정의라고 표시한다.

## 8. 검증 범위와 계산 ledger

가벼운 고유 검증은 atomic 14 + coupled 8 + kinetic 6 + runner fake 7 = **35개 PASS**다. 이전 5/6개 subset은 합산하지 않는다. 추가로 9점 owner 대조, 3점 독립 연속식/방향미분 검사, saved-result algebra, plot-format fixture, 1회 C9 review를 구별해 기록했다. reviewer는 code author와 다르지만 앞선 theory contract에 참여했으므로 완전 외부 모형 검증이라고 부르지 않는다. P0/P1 finding은 없고 BDF recovery 보장의 한계 P2는 문서화했다.

완료된 pilot의 isotope 보존 상대 결함 최대는 `1.7350768007071328e-14`, sampled instantaneous exchange identity는 `2.514452716784673e-16`이다. tensor-sum 계산 차이는 0, √2 관계 차이는 최대 `2.7755575615628914e-17`이다. algebraic cancellation과 선형 invariant 보존을 ODE global error 또는 continuum certificate로 바꾸어 해석하지 않는다.

P024 한 점의 기본 12×12×Gauss3 massive quadrature/32 radiation angle을 24×24×Gauss3/64 angle로 강화하고 rtol을 2e-7→2e-8로 바꾸었다. 사전 계약 `inputs/REFINEMENT_CONTRACT.json`의 모든 조건을 통과했다.

| 정련 비교 | 최대 변화 척도 |
|---|---:|
| ΣF | 1.3206581e-8 |
| Πm,F | 1.5680133e-6 |
| Πr,F | 7.6327661e-10 |
| Πtotal,F | 4.6562507e-7 |
| H relative | 4.1724291e-10 |
| T relative | 2.5065136e-7 |
| xe absolute | 9.8235206e-9 |
| isotope charge fraction absolute | 8.0682408e-8 |

처음 네 척도는 각 series 최대 절댓값을 분모로 하는 상대 척도다. near-zero pointwise relative error가 아니다. 이것은 한 점의 결합된 수치 민감도 검사이며 quadrature와 적분 오차를 따로 분해한 budget이나 continuum 증명은 아니다.

**실제 ODE attempt는 총 34회: 초기 실패 2 + 완료 pilot 31 + 고유 정련 1.** pilot 첫 baseline은 성공한 control에서 identity·bytes 대조 후 입양하여 재실행하지 않았다. 남은 새 pilot 30개가 모두 완료되었다. scientific campaign 실행 run ID는 `e153004b9ec94ee3ac0abb8ba049cda7`, 정련은 `70886fa8b3374cd7bfc71093183f3b3e`다. 완료 이력 재실행 0, NCP 0, benchmark 0이다. `--resume` 실제 점검에서는 31개 모두 skip, 새 ODE 0, case 파일 93개 bytes 불변이었다.

## 9. 자원 공유와 실행 방법

이번 sandbox 실제 한도는 cgroup 8 CPU/8 GiB였고, 사용자가 제시한 NCP 64 CPU/128 GiB를 이 환경의 용량으로 오인하지 않았다. 기본 3개 one-thread worker, reserve 1 CPU/1.5 GiB를 사용했다. NCP profile의 상한은 64 CPU/128 GiB, reserve memory 16 GiB다. `--max-workers`는 요청 상한이고 실제 cgroup·affinity·idle headroom·memory·동료 lease에 따라 할당량이 줄어든다. `/tmp/rei-bianchi-cooperative-leases`의 HH74-compatible 협력 lease를 사용한다. 다른 process를 종료하지 않는다. 다른 작업이 존재한다는 이유만으로 전체 작업을 취소하지 않는다.

unit 디렉터리에서 다음을 실행한다. 저장 결과가 포함되어 있어 resume는 완료 계산을 다시 돌리지 않는다.

```bash
python source/run_pilot.py --output results/pilot --site local --max-workers 3 --preflight
python source/run_pilot.py --output results/pilot --site local --max-workers 3 --resume
python analysis/check_saved_results.py
python source/plot_pilot.py --input results/pilot --output figures
```

이미 완료된 이 unit을 NCP에서 재생할 필요는 없다. 다음에 실제로 새 source/input identity를 갖는 과제가 생기면 `--site ncp --max-workers 64`가 상한 요청 방법이다. 그때도 실제 가용량 안에서만 dispatch된다. 새 ODE를 만들기 위해 기존 완료 claims나 실패 기록을 삭제해서는 안 된다. `analysis/`와 plotting은 과학 source manifest에서 제외한 후처리다.

## 10. 게시·백업·다음 DAG

S0 inventory/optimization은 commit `9a9f5c16ddf3c9fe98bfbcae6ee1f0cf1ae5ea15`, 19/19 blob readback PASS다. S1 theory/code/baseline은 `81f414482803bafce969059bffce8d462f71dd57`, 88/88 blob readback PASS다. S0 두 provider upload는 확인되었고 S1 두 provider는 전체 remote ZIP을 다시 내려받아 SHA256·ZIP CRC·payload 88개 SHA256까지 확인했다. S2는 이 보고서, 결과, 정련, 실제 그림을 담는다. 그 후 S3는 게시·백업 receipt만 마무리한다. 최종 HEAD와 최종 archive SHA는 self-reference를 피하려고 외부 `PHYS78_FINAL_DELIVERY_20261021.json`에 기록한다.

다음 선택 의무는 **`COLLISIONAL_ATOMIC_AND_THERMAL_CLOSURE`**다. 25,371 K까지 도달한 실제 이력 때문에 H/He/Li의 domain-valid CI/CX와 해당 thermal·escaped-energy 항을 동일 회계 안에 넣는 것이 우선이다. rate table의 출처·domain과 detailed balance/energy convention을 먼저 닫고, 그 다음 구현한다. Li III/IV를 유의미하게 활성화하려면 별도 `LI_HARD_UV_INNER_SHELL_CONTRACT`에서 75.64/122.5 eV 이상 광원, Li I inner-shell/branching, spectral closure를 먼저 해결해야 한다. 그림을 채우기 위한 임의 floor·초기 population 주입으로 대신하지 않는다.

다음도 OPEN이다: 전체 19 핵반응의 active rate owner, 분자/음이온·비평형 수송, 반응성 바리온의 anisotropic closure, PHYS77 full-history enclosure, angular/momentum continuum certificate, HH physically matched rate와 non-LRS. 이번 결과는 이 의무들의 완료 증거가 아니다. `CODEX_HANDOFF_KO.md`와 `NEXT_THREAD_HANDOFF_KO.md`는 이 경계를 유지하여 후속 작업을 이어가도록 작성했다.
