# WU088_HH PHYS53: 고차 Coulomb outgoing 로그미분의 안정 계산과 전류 퇴화

Date: 2026-10-16 KST. Parent PR #91, commit `794ba603597e1e85dd9accc487dfe8dfe8246a43`.

## 1. 고정 원본과 범위

원래 H(1s)+H(1s) spectator one-electron Hamiltonian은 원자단위계에서
\(h=-\Delta/2-1/r-(1+s^{-1})e^{-2s}\), \(s=|\mathbf x-0.7\hat z|\), \(k=0.7\)이다. 원래 field \(\eta=Fy\), \(\xi=Fy-\phi\), 1386개 complex128 frozen 입력의 알려진 SHA256은 `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`이다. 이번에 개발한 코드는 SHA guard를 포함하지만, 도구 쿼터 소진 후 격리 Python 컨테이너에는 실제 원본 NPZ를 장착하지 못해 **이 실행에서 원본 바이트 동등성을 다시 검사하지는 못했다**. 정확한 원본은 GitHub 부모 ref `794ba603...`의 `research/hh_phys34_20261015/inputs/FROZEN_U_SUBSET.npz`에 존재함을 커넥터로 확인했다.

이번 구현은 **중심 Coulomb 기준계** \(-1/r\), \(\ell\)별 scalar outgoing \(H^+=G+iF\)에 국한된다. 비중심 screened \(-S(s)\), \(\ell\)-coupled outgoing 역행렬, 원본 physical \(\xi\), \(\sigma(E)\), \(k_{HH}(T)\)는 아직 계산하지 않았다.

## 2. 핵심 수학 결과 (DLMF-supported, derived)

\(\eta_C=-1/k=-10/7\), \(\rho=kr\), \(Z_\ell^+=k(H_\ell^+)'/H_\ell^+\)이며 Wronskian으로
\[
 j_\ell=\operatorname{Im}Z_\ell^+=\frac{k}{F_\ell(\eta_C,\rho)^2+G_\ell(\eta_C,\rho)^2}>0.
\]
DLMF §33.5(iv)의 \(\ell\to\infty\), fixed \(\rho>0,\eta_C\) 점근식은
\[
G_\ell\sim e^{\pi\eta_C/2}\frac{(2\ell-1)!!}{\rho^\ell},\quad
F_\ell/G_\ell\to0.
\]
따라서
\[
 j_\ell\sim k e^{-\pi\eta_C}\frac{\rho^{2\ell}}{((2\ell-1)!!)^2},\qquad
 \frac{j_{\ell+1}}{j_\ell}\sim\frac{\rho^2}{(2\ell+1)^2}\to0.
\]
중심 Coulomb 채널의 고정 반경에서 전류에 관한 엄격히 양의 \(\ell\)-uniform 하한이 존재하지 않는다는 점이 직접 따라온다. 이는 PHYS52 finite-dimensional current-only inverse estimate의 무한채널 확장이 막히는 **그 방법 자체의 장애**이며, 전체 screened outgoing inverse의 no-go 증명이 아니다. 고차 DtN real principal part 및 weighted boundary spaces를 다루는 별도 정리가 필요하다.

## 3. 새로운 계산 형태 (DLMF33.8.2)

\(a=\ell+1+i\eta_C\), \(b=-\ell+i\eta_C\), \(c=i(1-\eta_C/\rho)\)에 대해
\[
\frac{(H_\ell^+)'}{H_\ell^+}=c+\frac{i}{\rho}
 \cfrac{ab}{2(\rho-\eta_C+i)+\cfrac{(a+1)(b+1)}{2(\rho-\eta_C+2i)+\cdots}}.
\]
`outgoing_cf`는 연분수를 유한 깊이에서 뒤에서 앞으로 계산한다. 그 깊이 비교는 **수치 수렴 지표**이지 연분수 truncation의 interval remainder certificate는 아니다. 작은 \(j_\ell\)를 IEEE754 복소수 \(Z\)의 허수부로 읽으면 \(10^{-16}\) 정도의 roundoff plateau 또는 부호 오류가 나타난다. 따라서 \(\log_{10}j_\ell=\log_{10}k-2\log_{10}|H_\ell^+|\)를 arbitrary precision 별도 lane에서 직접 평가한다.

## 4. 실제 Python·Wolfram 검산과 실패

격리 실행: Python 3.13, `mpmath 1.3.0`, `pytest 9.0.2`. `PYTHONPATH=.../src pytest -q ...`는 **17 passed, 1.88s**. Source fixture가 존재하지 않는 이 실행에서는 numerical Coulomb/CF/large-ell tests만 시험되었으며 원본 SHA guard 함수 자체의 적용은 production 환경에서 남아 있다. 실제 `/mnt/data/...` 생성 코드는 이 응답에 산출물로 보존한다.

첫 시도는 import PYTHONPATH 오류로 collection ERROR, 수정 후 test 16/17 PASS, \(\ell=128\) flux를 \(10^{-308}\) 미만으로 예단한 테스트 가정이 반례 \(\log_{10}j_{128}\simeq-177.8633\)으로 거짓임을 확인해 \(\ell\ge128\)에 대해 \(<-120\), \(\ell\ge256\)에 대해 \(<-308\)로 **관측 사실에 맞게 테스트 기대값을 교정**했다. 수치 알고리즘이나 물리적 tolerance를 변경하지 않았다. 최종 17 PASS. Wolfram Language evaluator 별도 호출에서 \(\ell=21,29,64,128\)의 outgoing Re Z와 \(\log_{10}j\)를 고정밀 독립 재현하고 점근 current ratio \(\rho^2/(2\ell+1)^2\to0\)의 정확식 확인.

격리 Python 27개 grid point \(r=27,30,43\), \(\ell=21,28,29,40,64,100,128,192,256\)를 68-digit mpmath 기준으로 평가한 결과는 `results/ISOLATED_COULOMB_27_CASES.json`에 있다. 예: \(r=27,\ell=64\), \(\operatorname{Re}Z=-2.24730477022\), \(\log_{10}j=-50.8745624\); \(\ell=128\), \(\operatorname{Re}Z=-4.68066103626\), \(\log_{10}j=-177.8633017\); \(\ell=256\), \(\operatorname{Re}Z=-9.45163759917\), \(\log_{10}j=-510.1446394\). f64 imaginary part at \(\ell=192\) was even negative due roundoff and must never be passed to a positivity proof.

Native Rust 1.99 compatible standalone finite-depth CF + multithread implementation and tests are in `native/phys53_coulomb_cf.rs`. 이 파일은 **source-authored, NOT_COMPILED, NOT_EXECUTED**이다. 연결된 사용자 로컬 Desktop Commander가 월간 쿼터로 중단되었으므로 NCP에 제출하거나 NCP Rust benchmark를 측정하지 못했다. 사용자 제공 SSH 키 `/home/cosmosapjw/.ssh/ncp_key`, 포트 22로 **쿼터 소진 전에** 실제 NCP 접속하여 64 CPU, 125 GiB, Rust 1.99.0/Cargo 1.99.0을 확인한 것은 별도 실제 런타임 증거다.

## 5. 다른 저장소와 문헌

최신 읽은 sibling: `rei_bianchi` PR150 `fd684a90...` (FLRW solver/caching), PR151 `13ebaff2...` (NCP molecular research), PR152 `bbbd18b5...` (Verner angular thresholds/Rust), `BASS_HE` PR66 `ccd9125e...`, `bass_cr` PR72 `e91ffe36...`. 이들 산출물은 반응률 또는 광자 적분의 provenance 분리 방법을 공유하지만, WU088_HH의 실제 고에너지 scattering amplitude, incoming adjoint 또는 \(k_{HH}(T)\)를 제공하지 않는다. 다른 repo는 변경하지 않았다.

Primary reference: NIST DLMF [§33.5(iv)](https://dlmf.nist.gov/33.5.iv) (large-\(\ell\) asymptotics), [§33.8](https://dlmf.nist.gov/33.8) (outgoing continued fraction), [§33.23](https://dlmf.nist.gov/33.23) (stable numerical directions and cancellation warning). 이 전류 퇴화는 문헌 기반 유도이고, screened infinite-dimensional no-go 주장은 하지 않는다.

## 6. 다음 실행 기준

NCP가 다시 도구로 접근되면 `~/.cargo/env`를 적용해 `rustc --test native/phys53_coulomb_cf.rs`와 `rustc -O ...`를 실제 실행하고, 원래 frozen NPZ SHA 검사를 먼저 시행한다. 32 worker 이하(다른 NCP 작업과 공존), 3 radii × \(\ell=21..512\)에서 Rust–mpmath finite-depth 일치 및 CPU/memory scaling을 별도 검사한다. 이것은 미실행 명세이며 실제 NCP 성능 주장이 아니다. 그 뒤 infinite-\(\ell\) screened exterior operator의 real-part pseudodifferential coercivity, actual source-driven \(g_{20}\), origin and incoming adjoint가 남는다. REI `HH_R10=OFF` 유지.