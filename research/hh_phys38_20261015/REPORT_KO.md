# WU088_HH PHYS38: C7B 유한 폭 cusp-strip + 전체 radial interface H⁻¹ 인증

날짜 2026-10-15 KST. 과학적 부모 **PHYS37 draft PR #76**, commit `e83f4bda79fecda26bb3854e94c0cdc786173835`. 선택된 노드 `C7B_RADIAL_STRIP_LIFT_AND_COUPLED_WHOLE_CELL` 중 **양의 부피 radial strip과 다섯 interface의 분포적 잔차**를 직접 유도하고, 현재 사용자의 Ubuntu에서 코드 구현·실행했다. Codex 호출 **없음**. 현장 native subagent tool이 노출되지 않아 `NOT_RUN`이며 multiprocessing과 구별한다. **전체 3D strong 잔차의 개선, 연속 low-Schur inverse, 물리적 cross section/rate는 아직 완료되지 않았다.**

## 1. 변경하지 않은 물리·경계

고정 1s spectator의 두 중심 직접 퍼텐셜, 공간에 대한 Euclidean gradient:
[
h_lambda=-\tfrac12\Delta-1/r-\lambda S(s),\quad S(s)=(1+1/s)e^{-2s},\quad
s=|\mathbf r-R\hat z|,\quad \lambda=1,\quad R=\kappa=7/10.
]
물리적 길이의 단위는 `a0`(Bohr radius), Hamiltonian 에너지 단위는 `Ea=2I0`이며 source `I0=13.605693122990eV`와 수신 열장부 `chiH=13.598434599702eV`는 다르다. c/hbar/kB를 1로 추가 가정하지 않는다. GR 배경 signature(-+++), 전자 공간 Euclidean. Original transition `S(R)-S(s)`, Coulomb continuum phase, event-tag/network 계수, 기존 THERMAL/P01 및 REI의 HH OFF를 변경하지 않았다. 상태는 PHYS34의 **정확한 이진 유리수 nodal 보간장**이다. `F=e^{\lambda e^{-s}}`, `eta=phi+lambda xi=F y`의 frozen-direct 동일 모델을 유지한다.

PHYS37에서는 `r=R`에서 두 one-sided frozen polynomial의 정확한 **각도** 잔차 인증을 마쳤다. 저장된 기준 자료 `SHELL_BOTH_N96_18.json`의 바이트 SHA256:
`a942df8c66f5d8c3817b3e41dc11329420d2cfef9800e827c27c5381a42f1be7`
와 원본 nodal `FROZEN_U_SUBSET.npz` SHA256:
`f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`
를 입력검사로 고정했다. 좌우 `L²(S²)` 상계는 각각 `0.001697685390802356`, `0.009340991924804115`이다.

## 2. 양의 부피에서 증명한 radial-strip theorem

`\delta>0`에 대해 (R-\delta<r<R+\delta). 고정 angular 방향의 spectator 분리벡터를
`z(r,mu)=r e_r-R e_z`로 놓으면 `|z(r)-z(R)|=|r-R|=t`, `|s(r)-s(R)|<=t`. 단위벡터 `n=z/|z|`는 cusp에서 일반적으로 Lipschitz가 아니다. 대신
[
|n(r)-n(R)|\le\min(2,2t/s(R)).
]
구면 (r=R)에서 `s(R)=2Rx`, `x=sin(theta/2)`, angular normalized measure `2x dx`를 사용하면, (0<t<2R)에서
[
\frac1{4\pi}\int_{S^2}|n(r)-n(R)|^2 d\Omega
\le\frac{t^2}{R^2}\left[1+2\log\frac{2R}{t}\right]=M(t)^2.
]
`log_ratio_bounds`는 정확한 Fraction atanh 양의 급수 및 남은항을 이용하며, 이 상계는 (x=0) cusp를 가정으로 제거하지 않는다.

Cusp conjugation 퍼텐셜 (U=E q-E/2-3E^2/2), (E=e^{-s}), (q=(1-E)/s=\int_0^1 e^{-su}du)에 대해 `|U|<=E<=1`, `|q'|<=1/2)에서 `|U'(s)|<=5`, `|E'|<=1`. `e^{-E}` 또한 s-Lipschitz 1이다. 따라서 frozen field에 대해 (G=\sqrt{4\pi}\,\mathcal R)의 각도 평균 제곱근 노름을
[
Q(r)=\|\mathcal R(r)\|_{L^2(S^2)}
\le Q(R_\pm)+K_\pm t+2\,M_{\nabla,\pm}M(t)
]
로 제한한다. 여기서 모든 (K,M_{\nabla})는 실제 nodal Lagrange polynomial의 (u,u',u'',u''') 계수를 **정확한 유리수 Taylor 다항식으로** 변환하여 `|r-R|<=delta`에서 majorize했다. `sqrt(2l+1)` 및 계수 모드의 상계는 정수 제곱근의 외향 경계이며 실제 구면조화 정규화에 맞다. 대략:
[
K=M_{D'}+2(M_\nabla+M_{\nabla'})+2(5M_B+M_{B'})+4(1+\kappa^2).
]
`delta`의 끝점은 분모 (r\ge R-\delta>0)의 명시 상계로 처리했다.

단순히 `Q(R)+delta K+2Mgrad M(delta)`를 유한 strip의 최대값으로 사용할 수도 있지만, **새 개선**은 radial 적분 안에 (t)를 유지하는 것이다.
[
\int_0^\delta t^2\left[1+2\log\frac{2R}{t}\right]dt
=\delta^3\left(\tfrac59+\tfrac23\log\frac{2R}{\delta}\right).
]
`L²_t` Minkowski를 적용하면 one-sided radial norm 상계는
[
\sqrt{\int_0^\delta Q(R\pm t)^2 dt}
\le Q(R_\pm)\sqrt\delta
+K_\pm\sqrt{\delta^3/3}
+{2M_{\nabla,\pm}\over R}
\sqrt{\delta^3(5/9+(2/3)\log(2R/\delta))}.
]
모든 제곱근은 Fraction 정수 제곱근으로 위쪽 반올림하고, 원 angular reference·로그 구간·원본 input identity를 유지한다.

**참고:** 실제 이산 인터페이스 반경 (r_b=float64(0.7))는 수학적 (7/10)보다 (\sim 4.44e-17) 작다. 좌 패널은 ([R-\delta,r_b]), 우 패널은 ([r_b,R+\delta])에서 유효하며 두 구간은 수학적 R을 기준으로 정확히 나누어지지 않는다. `mismatch=|r_b-R|` 만큼의 길이에 (Q_{\max}^2) 보수적 추가항을 적용해 false adjacency를 막았다. 이로써 positive-volume 내 껍질의 **broken strong transformed PDE bulk** bound를 얻는다.

실제 노출한 비교 (모두 `a0` 반폭; angular+radial corrected (L²(d^3x))):
| delta/a0 | 기존 uniform-sup bound | 새 radial-integrated bound |
|---:|---:|---:|
| 1/100 | 0.159644570395 | **0.092921847102** |
| 1/1000 | 0.004961053603 | **0.002951003776** |
| 1/10000 | 0.000212286605 | **0.000148787714** |

이들은 **3차원 양의 부피 서브도메인**에 대한 인증이다. 폭이 줄어들면 norm도 줄어드는 것은 측도 효과를 포함하므로 전체물리 정확도가 개선됐다는 의미가 아니다. PHYS36의 `r0=1e-4..20` strong broken-bulk bound `2.603747132326`을 국소 strip 값으로 대체하지 않는다.

## 3. 다섯 interface 전체의 정확한 H⁻¹ 부등식

실제 공유된 IEEE binary64 radial panel endpoint (b_j)를 기준으로, 21개 복소 partial waves 전부의 nodal Lagrange polynomial을 정확히 평가했다. (j=1..5)에서 **물리적 field 값의 jump가 정확히 0**이므로 `delta_prime` singularity는 없다. 첫 radial derivative의 angular `L²(S²)` jump 상계는 경계 순서대로:
`1.026e-13,9.0e-15,2.9e-15,6.0e-16,3.0e-16`.
강한 PDE residual의 좌우 2차 미분 trace jump `~.0104771`은 분포적 delta 계수가 아니다.

시험함수 (v\in H^1\)에 대해 실제 인터페이스 왼쪽의 radial 작은 collar ([b-w,b])에서
[
\|v(b)\|^2_{L²(S²)}
\le(2/w)\int_{b-w}^b\|v(r)\|^2_{L²(S²)}dr+
2w\int_{b-w}^b\|\partial_r v(r)\|^2_{L²(S²)}dr.
]
중량 (r²drd\Omega)과 (r\ge b-w)를 사용하면
[
\|v(b)\|_{S²}
\le C_{tr}\|v\|_{H¹},\quad
C_{tr}=\sqrt{2\max(w,w^{-1})}/(b-w).
]
분포적 `Delta psi`의 interface functional은 (b²\langle [\partial_r\psi]_b,v(b)\rangle_{S²})이므로
[
\| (\Delta\psi)_{interfaces} \|_{H^{-1}}
\le \sum_{j=1}^5 b_j² C_{tr,j}\|[\partial_r\psi]_{b_j}\|_{L²(S²)}
\le\boxed{1.793\times10^{-13}}.
]
물리적 Hamiltonian 운동항 `-Delta/2`의 대응 상계는 `8.97e-14`. 모두 a0/Ea 무차원 normalized angular spherical harmonics, `H¹` norm `(\int_{r0}^{20}(|v|²+|\nabla v|²)r²drdOmega)^{1/2}`로 정의된다.

PHYS36 C7A의 독립 원 strong bulk `L²` upper `2.603747132326`는 동일한 연속 transformed operator (D=\Delta+\kappa²+2/r) 표현, 동일 원본 SHA를 사용한다. `L²\hookrightarrow H^{-1}` norm embedding 1과 위 다섯 delta의 삼각부등식을 결합하면 **절단 annulus \(r0<r<20\)**에서
[
\boxed{\|\mathcal R\|_{(H_0^1(annulus))^*}
\le 2.603747132326180}.
]
이는 상한이 비록 넓어도 **모든 내부 radial distributional interface를 포함한 3D truncated-domain H⁻¹ 상계**라는 점에서 새로운 결과다. 하지만 원점 r<r0, 물리적 outgoing boundary, 외부 source, low-Schur inverse 및 dual amplitude는 포함하지 않는다.

## 4. 최적화, 실제 코드, 과학 진단

새 실행 코드 `src/wu088_hh/phys33_cusp_strip.py`, `src/wu088_hh/phys33_strip_preview.py`, `src/wu088_hh/phys33_interfaces.py`, `src/wu088_hh/phys33_truncated_hminus1.py`, `scripts/phys33_cusp_strip.py` 및 신규 tests 2종 이상을 WU088_HH 브랜치에서 직접 수정·실행했다. Codex 미사용.

`phys33_strip_preview.py`는 실제 arbitrary r용 spectator 거리 `s\in[|r-R|,r+R]`와
`mu=(r²+R²-s²)/(2rR)`, `dmu=-s/(rR)ds`를 사용해 **독립 NumPy/SciPy vectorized Gauss** 통계량을 출력한다. 이것은 **noncertifying**이며 scientific admission을 결정하지 않는다. `delta=1/1000`에서 48 radial ×128 spectator-s Gauss는 `2.0484930877e-4` 주변; 엄밀 strip upper `2.951003776e-3` 안에 들어간다. `delta=1/10000`에서는 `6.626e-5` 근처이다. 수치 진단은 고정 좌표 cusp의 이해에 유용하지만 거기서 오차 upper를 추측하지 않는다.

`phys33_cusp_strip.py` batch CLI는 `--workers {1,2,3,4}`의 **safe forkserver**로 독립 폭 세 개를 병렬 실행하고 항상 입력 index 순으로 감소한다. `--deltas 1/100 1/1000 1/10000`로 각도 접합의 exact parent SHA를 확인하고 decimal upper를 JSON에 기록한다. 단일 실행 약1.68s vs 3-worker 약0.62..0.83s로 약2x 이상의 속도향상을 관찰했고 병렬/직렬 과학 필드는 **동일**했다. NumPy 진단은 짧은 수십 ms이며 명시적으로 not certified. 전체 과학입력 1386 complex frozen dyadic values 그대로.

## 5. 실제 검산·다른 저장소의 현재 기여

사용자 원격 Ubuntu Wolfram Engine15+xAct/xTensor1.3.0을 실제 호출해 다음을 얻었다: 정확한 단위벡터 각도로그 적분, radial 로그 moment, `U'(s)` 대수, `e^{-e^{-s}}` derivative 모두 literal zero, manufactured scalar trace margin (773/300>0), Euclidean Green product tensor literal zero. 새 targeted tests 및 전 저장소 회귀시험 실제 결과는 `results/`에 저장한다. native subagent는 도구 미노출로 `NOT_RUN`, Python worker와 구분한다. 외부 독립 과학 검토도 `NOT_RUN`.

SciSpace/Exa에서 Coulomb coalescence analytic structure (arXiv:0806.1004)와 spherical-harmonic two-centre integrals (doi:10.1063/5.0124647)를 탐색했고, 이번에 채택한 숫자들은 논문에서 끌어온 보정이 아니라 이 패키지의 원 연산자·입력에서 직접 유도했다. 최신 bass_cr PR69은 helium q-grid threshold bias의 positive source quadrature를 다루며, WU088_HH continuum에 수치를 옮기지 않았다. 최신 BASS_HE PR61은 fifth warm P01 cell의 별도 광자/가스 opacity, rei_bianchi PR117은 cold reionization. REI의 AX07 ZERO는 완료, AX08 signed 진행 중, AX11/12 대기. Live REI 작업을 수정하거나 solver를 시작하지 않았고, stellar spectrum 50000K를 cold-gas T와 혼동하지 않는다.

## 6. 정확히 남은 작업

본 C7B substep은 **positive-width cusp radial strip + full five-panel H⁻¹ interface certificate** 범위를 완료했지만, **원래 전체 3차원 PDE strong residual의 coupling cross term 인증은 계속 열려 있다.** 다음 node `C7B_GLOBAL_RADIAL_S_SPECTATOR_INTERVAL_AND_HMINUS1_DUAL`에서 strip 외 다섯 panel을 원 `s\)-좌표 angular interval quadrature로 연결하고, origin patch 및 screened outgoing DtN defect와 continuous low-Schur inverse/adjoint를 정량화한다. 현재 전체 two-centre thermal HH rate and scattering intensity remain NULL. No merge or production promotion.
