# PHYS16 원 source cooling-cone 교차점검

## 판정과 확인 방법

**판정: `PASS_SCOPED_SOURCE_MAPPING`.** 현재 상속된 `nonphoto` export는 photo를 정확히 끈 FT03의 CI·RR·DR thermal map이다. 물리적 fraction 영역과 원 온도 영역에서 그 thermal map은 수소·헬륨 각각 cooling cone에 속한다. 따라서 PHYS16의
\[
\frac{F^{np}_w}{n e f}\le k_{w\mathrm{He}}\le0
\]
적용에 필요한 부호와 source 분리가 성립한다.

이번 메모는 endpoint 결과를 다시 계산하지 않고 원 Rust source의 함수 경계, 기호, 제어 경로, export 순서를 직접 읽어 교차확인했다. 줄 번호에 의존하지 않는 symbol mapping을 아래에 남긴다. 새 scientific 실행·fit 평가·root/history 실행·코드 수정은 0회다. 최종 독립 수치·이론 심사는 별도 검토자의 결과와 함께 root가 판정한다.

## 1. 함수와 export의 연결

| 원 source symbol | 확인된 동작 | PHYS16의 대상 |
|---|---|---|
| `HHeModel::controlled_fixture` | 양의 \(c,k_B,\epsilon_{eV}\), threshold와 초기 model field를 정의 | 실제 leaf와 threshold의 최초 정의 |
| `Ft03Model::controlled` | 위 fixture를 만들고 photon energies, alpha/beta field 및 sigma를 조정; threshold와 물리 상수는 유지 | controlled FT03 model |
| `coupled_primary::model(stage)` | `Ft03Model::controlled`를 호출하고 `n_h_cm3`, `n_he_cm3=fl(n_h_cm3*f_he)`만 stage 값으로 설정 | \(n\), 저장된 \(n_{He}\), \(f=n_{He}/n\) |
| `phys04_reduced_residual`의 `m.gas.sigma_cm2=[[0.0;3];3]` | FT03 내부 photo cross-section을 전부 exact zero로 지정 | photo-off 호출 |
| `ft03_interval_rhs` | gas \((x,y,z,w)\)와 세 양의 dummy photon 좌표를 받아 CI·RR·DR 및 photo를 조립 | 아래에서 감사를 수행한 닫힌 함수 body |
| `phys04_compose` | raw gas source jet을 owner gas jet으로 연쇄미분 | 값의 물리식은 유지 |
| `let nonphoto=f.clone()` | FT03의 앞 네 성분을 HH·외부 photo·팽창 추가 전에 보존 | `SOURCE_*_COMPONENTS.json/nonphoto` |
| 같은 함수의 `hh_rate_jet` 이후 수정 | \(+\lambda q\)와 \(-\chi_H\lambda q\) 추가 | \(B\)의 별도 HH 항 |
| 같은 함수의 `for (n,e) in incoming.iter().zip(energies)` | 33개 외부 photon group의 photo rates 및 heating 추가 | \(VP\)의 별도 광자 항 |
| 같은 함수의 마지막 thermal 수정 | \(-2H w\) 추가 | \(B\)의 별도 팽창 항 |
| `sourcebox::source_components` | export의 `rhs`, `nonphoto`, `photo_rates`를 서로 다른 JSON key에 기록 | 이번에 읽은 `nonphoto`의 정확한 위치 |

`ft03_interval_rhs`의 photo loop 안에 양의 photoheating 표현은 존재하지만, 위 호출에서 각 \(\sigma_{ak}=0\)이므로 해당 정확한 source 함수의 모든 photo 항은 0이다. 양의 dummy photon 좌표 1은 FT03 함수의 입력 domain을 만족시키는 역할을 한다. 이 판단은 signed interval tail을 삭제하는 처리가 아니라, 상속된 fixed-real source graph의 정확한 zero coefficient를 사용하는 것이다.

## 2. 변수·정규화·물리 영역

`ft03_interval_rhs`의 `y[0],y[1],y[2],y[3]`를 각각 \(x,y,z,w\)로 쓴다. \(x=x_{HII}\), \(y=x_{HeII}\), \(z=x_{HeIII}\), \(w\)의 단위는 eV/H다. `nh`, `nhe`, `fhe`, `ne`, `particles`, `t`는 다음과 대응한다.
\[
n=n_H>0,\quad n_{He}>0,\quad f=n_{He}/n>0,
\]
\[
e=x+f(y+2z),\quad n_e=n e,\quad
\Pi=1+f+e,\quad T=\frac{2\epsilon_{eV}w}{3k_B\Pi}.
\]
함수 진입은 모든 `bx[i].lo>0`, `bx[0].hi<1`, `bx[1].hi+bx[2].hi<1`을 요구한다. 따라서
\[
0<x<1,\quad y>0,\quad z>0,\quad y+z<1,\quad w>0
\]
이며 \(e,\Pi>0\)이다. 함수의 온도 guard는 \(30000\le T\le110000\ \mathrm K\)다.

물리 반응 population은 `lower`, `upper`에 정확히 다음과 같이 들어간다.

| index / absorber | `lower[a]` | `upper[a]` |
|---|---:|---:|
| 0 / HI | \(n(1-x)\) | \(nx\) |
| 1 / HeI | \(nf(1-y-z)\) | \(nfy\) |
| 2 / HeII | \(nfy\) | \(nfz\) |

각 항은 위 fraction 조건에서 비음수다. 기존 `C2_DOMAIN.json`의 원 \(X\)는 대략 \(x\in[0.90,0.93]\), \(y\in[0.29,0.31]\), \(z\in[0.59,0.61]\), \(w\in[13,14]\)이며, 그 exact endpoints는 같은 파일의 bits가 권위다. 저장된 `simplex_sum` 상한은 \(0.9200000000000003<1\)이고 `temperature`는 약 \([46996.7104457,51452.8842149]\ \mathrm K\)다. 현재 root와 온도 정렬 pullback의 더 작은 hull은 이미 이 \(X\) 내부로 확인되어 있다.

## 3. 정확한 상수와 세 반응군

이 절에서 \(\langle v\rangle\)는 **원 Rust f64 literal `v`가 나타내는 binary64 수를 정확한 실수로 읽은 값**을 뜻한다. 따라서 원 source의 고정 leaf를 decimal 실수로 다시 정의하지 않는다. 아래 표는 함수·배열 이름으로 대응되므로 source 줄 이동에 영향을 받지 않는다.

| symbol | 원 literal/bit 정의 |
|---|---|
| \(\Lambda_a\), `lambda` | \(\langle315614\rangle,\langle570670\rangle,\langle1263030\rangle\) K; 이 정수들은 exact |
| \(A_a\), `ci_a` | \(\langle21.11\rangle,\langle32.38\rangle,\langle19.95\rangle\) |
| \(p_a\), `ci_p` | \(\langle-1.089\rangle,\langle-1.146\rangle,\langle-1.089\rangle\) |
| \(c_a\), `ci_c` | \(\langle0.354\rangle,\langle0.416\rangle,\langle0.553\rangle\) |
| \(r_a\), `ci_r` | \(\langle0.874\rangle,\langle0.987\rangle,\langle0.735\rangle\) |
| \(d_a\), `ci_d` | \(\langle1.101\rangle,\langle1.056\rangle,\langle1.275\rangle\) |
| H/HeII RR constants | \(\langle0.522\rangle,\langle0.470\rangle,\langle1.269e{-13}\rangle,\langle1.503\rangle,\langle1.923\rangle\) |
| HeI RR constants | \(\langle3e{-14}\rangle,\langle0.654\rangle\) |
| \(A_{DR}\), `dr_a` | `f64::from_bits(0x3f5f8b1ba9b90acb)` |
| \(B_1\), `b1` | `f64::from_bits(0x411caf2e364afdee)` |
| \(B_2\), `b12` | `f64::from_bits(0x412135e886f9cb6f)` |
| DR multiplicities | exact 1, \(\langle0.3\rangle\) |

\(\chi_H,\chi_I,\chi_{II}\)는 `threshold_ev`를 통해 들어가며 positive다. 실제 threshold는 다음 stored leaf와 일치한다.

| Threshold | value 표시 | exact binary64 bits |
|---|---:|---|
| \(\chi_H\) | 13.598434599702 eV | `402b3266051507a6` |
| \(\chi_I\) | 24.587389011 eV | `4038965f20504658` |
| \(\chi_{II}\) | 54.41776 eV | `404b357928e0c9da` |

`NATIVE_CONSTANT_LEAVES.json`의 \(k_B\)는 `3ca3e5b21cc8f74f`, \(\epsilon_{eV}\)는 `3d7c2f8fe5409db9`다. 기존 `FT03_THRESHOLD_IDENTITY.json`의 모델 생성 경로와 일치함을 원 `Ft03Model::controlled` 및 `HHeModel::controlled_fixture`에서 다시 읽었다. `C2_DOMAIN.json/thresholds=[13.60,24.59,54.42]`는 sourcebox 작성문에 고정된 반올림 metadata이며 실제 reaction threshold를 정의하는 위치는 위 model field다. 현재 부호 증명은 양성만 사용하고, 에너지 계수의 수치 적용은 실제 captured bits를 사용한다.

### CI

\(\ell_a=\Lambda_a/T>0\)에서 `beta`는
\[
\beta_a(T)=
\frac{A_aT^{-3/2}e^{-\ell_a/2}\ell_a^{p_a}}
{[1+(\ell_a/c_a)^{r_a}]^{d_a}}>0.
\]
`ci=lower[a]*ne*beta/nh`는 H당 반응률이고 thermal 수정은 정확히 \(-\chi_a\,\mathrm{ci}\)다. 양의 threshold·coefficient·population이므로 이 기여는 비양수다.

### RR

HeI는
\[
\alpha_I(T)=\langle3e{-14}\rangle\ell_I^{\langle0.654\rangle}>0,
\quad s_I=-\langle0.654\rangle.
\]
H 및 HeII는 \(m_H=1,m_{II}=2\)에 대해
\[
u_a=\left(\frac{\ell_a}{\langle0.522\rangle}\right)^{\langle0.470\rangle},\qquad
\alpha_a=
\frac{m_a\langle1.269e{-13}\rangle\ell_a^{\langle1.503\rangle}}
{(1+u_a)^{\langle1.923\rangle}}>0,
\]
\[
s_a=-\langle1.503\rangle+
\langle1.923\rangle\langle0.470\rangle\frac{u_a}{1+u_a}.
\]
`kinetic`는 \(k_BT\alpha_a(3/2+s_a)\)이고 thermal 수정은
\[
-\frac{\mathrm{upper}[a]\,n_e}{n\epsilon_{eV}}
k_BT\alpha_a\left(\frac32+s_a\right).
\]
원 온도 범위 전체에서
\[
\frac{\Lambda_H}{\langle0.522\rangle\,110000}>1,
\qquad \Lambda_{II}>\Lambda_H,
\]
이므로 H와 HeII 모두 \(u_a>1\)이다. 이에 따라
\[
\frac32+s_a>
\frac32-\langle1.503\rangle+
\frac{\langle1.923\rangle\langle0.470\rangle}{2}>0.4489>0.
\]
HeI는 \(3/2-\langle0.654\rangle>0\)이므로 같은 부호가 성립한다. RR가 빼는 kinetic energy는 세 종 모두 양수다.

### DR

`for (factor,b) in [(1.0,b1),(0.3,b12)]`는
\[
d_r(T)=c_rA_{DR}T^{-3/2}e^{-B_r/T}>0
\]
를 사용하고 `dr=upper[1]*ne*d_r/nh`를 정의한다. thermal 수정은
\[
-\mathrm{dr}_r\frac{k_BB_r}{\epsilon_{eV}}\le0.
\]
`upper[1]=nfy`여서 이 기여는 헬륨 항에 정확히 속한다.

## 4. 전체 thermal body의 항 목록과 누락 검사

`ft03_interval_rhs`의 `w`는 `c(0.0)`으로 시작한다. 함수 끝에서 `w`를 반환하기까지 `w`를 수정하는 모든 경로는 다음 세 군이다.

| 수정군 | 해당 fixed source에서의 값 |
|---|---|
| `for a in 0..3`의 두 번의 subtraction | CI threshold loss + RR kinetic loss |
| 그 안의 `for k in 0..3`의 addition | 내부 photoheating; 호출 전에 지정된 \(\sigma_{ak}=0\)로 exact zero |
| 두 DR channel의 subtraction | DR thermal loss |

위 함수 body와 해당 호출/export 사이에는 Compton 교환, free-free/bremsstrahlung, collisional-excitation cooling, 외부 heating이나 추가 closure callback을 더하는 경로가 없다. 현재 controlled `nonphoto`의 닫힌 구성항이 CI·RR·DR임을 확인했다. HH, 원 33-group photoheating, 팽창은 `nonphoto=f.clone()` 뒤에 별도로 더해지므로 그 값이 cooling-cone의 \(F^{np}_w\)에 섞이지 않는다. RR/DR escaped radiation은 원 event/energy bookkeeping의 별도 항이고 thermal body에서는 위 kinetic/DR loss로 이미 반영된다.

따라서 같은 정확한 \(n,f,g\)에서
\[
F^{np}_w=n e\,[k_{wH}(x,T)+f k_{w\mathrm{He}}(y,z,T)],
\]
\[
k_{wH}=-\chi_H(1-x)\beta_H-x\kappa_H\le0,
\]
\[
\begin{aligned}
k_{w\mathrm{He}}={}&-\chi_I(1-y-z)\beta_I-\chi_{II}y\beta_{II}
-y\kappa_I-z\kappa_{II}\\
&-y\sum_{r=1}^2d_r\frac{k_BB_r}{\epsilon_{eV}}\le0,
\end{aligned}
\]
여기서 \(\kappa_a=k_BT\alpha_a(3/2+s_a)/\epsilon_{eV}>0\)다. \(n e f>0\)로 나누면
\[
\frac{F^{np}_w}{n e f}=\frac{k_{wH}}{f}+k_{w\mathrm{He}}
\le k_{w\mathrm{He}}\le0.
\]
이것이 PHYS16에서 사용한 source lemma의 완전한 source 대응이다.

## 5. 실제 적용점과 판정 범위

PHYS16은 \(T_2(g_*)=T_1(g_1)\)인 pullback \(g_*\)에서 보존된 Full nonphoto 값을 사용한다. \(x,y,z\)는 pullback에서 고정되고 \(w\)만 바뀌므로 원 population 부호가 유지된다. 양의 \(n_2,e_2(g_*),f_2\)와 \([F^{np}_{2,w}](g_*)\)를 이용한
\[
\left[\frac{F^{np}_{2,w}}{n_2e_2f_2}\right]^-\le
k_{w\mathrm{He}}(y_1,z_1,T_1)\le0
\]
는 필요한 동일 온도의 He cooling coefficient를 포함한다. \(\Delta f<0\)의 곱에 대해 thermal bridge correction은 비음수다. 기존 `run01`의 부호와 단위 대응이 이 전제와 일치한다.

본 판정은 현재 정확한 fixed-source definition과 명시한 fraction·온도 범위에 적용된다. Source에 새로운 에너지 교환항이 추가되면 그 항의 species·density factorization을 연결하는 지점부터 lemma를 확장한다.

## 읽은 원 source의 identity

PHYS15 안의 prefix를 `inputs/phys14/inputs/ncp07/`로 줄여 썼다. 추가 두 원본은 기존 NCP07 intake의 `candidate/src/`에서 읽었으며 PHYS15의 threshold identity 기록과 일치한다.

| 파일 | SHA256 |
|---|---|
| `candidate/src/ft03_interval.rs` | `886580a810b8ec29c8f0b6199c0e35d82fde1f46d984a5f8f1da304326a42a42` |
| `candidate/src/phys04_mixed.rs` | `0fa10fdea11cb24aa1a191a2ea81cf4c8442299fde7278a191553b42a26585d3` |
| `candidate/src/coupled_primary.rs` | `2c528f1e7dcf44622374f8421a192f75ce8cff8b1c311bbff508f9ed863d7dcc` |
| `src/sourcebox.rs` | `d771968e9c12c0cce5a9e3ec5fa7311d0040ac63d1f4f4a6f54f048972f674ae` |
| NCP07 `candidate/src/ft03_controlled.rs` | `61e11471482bb49d99e5d0eb79504d3f67538fbe6361653a0462d1abb0b672db` |
| NCP07 `candidate/src/hhe_events.rs` | `c100b08e034089c2d67b2102769ccdd51f1d29a2f388d6bb2dfe7984af93b290` |

읽기·hash 확인 외 새 수치 실행은 수행하지 않았다. PHYS16 application 코드와 기존 결과 파일은 변경하지 않았다.
