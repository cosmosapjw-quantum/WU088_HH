# 실제 공급자 행과 finite event registry — R1 보고

## 1. 이번 단위의 결과와 승인 범위

고정 인계서의 실제 HEAD
`34dd7d1d018abff8a0a4ebd1d3f3579ac46d2fad`를 기준으로,
공급자 변형·원자료 기록 **102개**, 후보 사건 투영 **125개**,
compiler용 종·상태 identity **92개**를 저장했다.
과거 설정의 **21개 population / CI·PI·RR 39개 방향**을 별도 view로
보존하고, 39개 방향 모두에 최소 한 개의 실제 공급자 후보를 연결했다.

이 수치는 서로 다른 대상을 센다. 102개는 독립적인 실측 반응 102개를
뜻하지 않는다. 원소별 계수의 동위원소 후보 투영, 같은 물리 과정의 서로
다른 fit, 과거 cold kinematic record를 구별한 source inventory다.
125개는 source 연결이 있는 유한 number-operator 투영이다. 92개에는
aggregate view와 상태별 view가 함께 있으므로 이 모두를 동시에 진화시키는
모형이 아니다. 실제 source selector와 원자료 hash는
[providers.json](registry/providers.json)에 들어 있다.

현재 독립 판정은 `ACCEPT_SCOPED_SOURCE_ROWS_AND_INTEGER_PROJECTIONS`다.
새 empirical rate, 핵 Q, IVP, named consumer 승인은 각각 0이다.
PHYS91 B1, source atomic→bare 변환, mass covariance 및 원 nuclear-network
입력은 별도 의존성으로 남는다. 전역 물리 완료율은 `null`,
`HH_R10=OFF`, `production=NOT_ISSUED`, `L4_ready=false`를 유지한다.

## 2. 권위와 기존 계산 재사용

사용자가 지정한 [고정 인계서](../program_expansion_20261025/HANDOFF_KO.md)를
먼저 읽고, 최신 branch HEAD·AGENTS·병렬 PR·기존 두 백업의 실제 metadata를
확인했다. 원 owner는 PHYS91 PR148,
`2912a315aa39e7293000b7b2b8c7cc7a706fea9e`이며 확장 PR149의 HEAD는
`34dd7d1d018abff8a0a4ebd1d3f3579ac46d2fad`다.

중앙 과학 계약은
`rei_bianchi@641a725ada4be27473069c2c35005a94c2ab0248`의 DAG를
직접 회수했다. 원본은 1,543,000 bytes이며 SHA-256은
`2fd13e63bda782142b5a93703fe7050697c829844276ce298e7873751459ad7d`다.
`authority/CENTRAL_DAG_PINNED.json.gz`는 이 바이트를 그대로 복원한다.
관측된 중앙 HEAD `78f7ac5864d5817ceb79b48cb5e298cc30006510`까지의
변경은 게시·인계 결속이며 해당 과학 DAG 계약은 바뀌지 않았다.

재사용한 compiler는
`research/rei_chem_ledger_20261025/chem_ledger.py`이고 SHA-256은
`60a502895266b6feb96964abc4b24db61c2faed2344db0f7d12f16bb47ed62af`다.
기존 249 synthetic checks와 admission은 원 결과로 재사용했다. 기존
PHYS83의 finite CE/radiative 결과, PHYS81 cold 3행 및 PHYS91 인증도
재계산하지 않았다. PHYS91의
$0.5808771124940327\le t_{\rm PSD}\le1.0015608216979872$
는 기존 scoped 결과이며 새로운 source confidence 승인으로 바뀌지 않는다.

## 3. 실제로 회수한 공급자

| 계열 | 실제 회수·저장 내용 | 사용 범위 |
|---|---|---|
| Verner PI/RR | H/He/Li 전자수별 PI 6행과 RR 7변형 | He I fit a/b를 분리; isotope-blind 원자료 |
| Voronov CI | 원 406행 중 H/He/Li 6행, 원 설명·Fortran | 13개 동위원소/전하 후보 방향; 계산·활성화 없음 |
| 기존 finite CI | H1, He4, Li7 원자료 3개·총 127 knots | 기존 finite window와 과거 admission 범위를 보존 |
| H I CE·방사 | CCC 4전이, CHIANTI 4방사 record | 1s/2s/2p 및 J/branch identity 보존 |
| 핵/약반응 | ENDF MT102 153 knots·152 cells, n/T의 NUBASE·LiveChart 대안 4개 | source Q와 branch를 보존; 실제 핵 Q 결속 미승인 |
| 과거 cold 기록 | np→dγ, nd→tγ, pd→He3γ 3행 | 저장된 값·source identity만 재사용 |
| UMIST | 원 8,767행 중 H/He/e/photon/CR 닫힌 부분계 37행·38 fit 구간 | H−, H2, H2+, H3+, HeH+를 포함; native 환경 결속 필요 |
| LiH photoprocess | Leiden 원 1,562 samples, 91.2–351.1 nm | 6LiH/7LiH 2개는 후보 매핑; source isotope/state 미지정 |
| HD | LAMDA J 9준위, A 8행, 하향 충돌 18쌍×3온도 | para/ortho H2 충돌자를 구별; REC radiation owner 유지 |

위 행의 공급자 수는 35 atomic/nuclear source variants + cold 3 +
UMIST 37 + LiH 1 + HD 26 = 102다. 모든 native payload는 원문 행 또는
실제 원문 표를 주소 지정하는 `payload_ref`와 hash를 가진다. 원문
다운로드·Git blob 회수 영수증 및 정확한 바이트는 `sources/`에 있다.

### 원자 CI 공백의 처리

기존 설정은 n, H1, D, T, He3, He4, Li6, Li7의 21개 전하 population이다.
기존 39개 CI/PI/RR 방향 중 29개에는 기존 source 연결이 있었고 10개 CI
방향은 finite admission source가 없었다. 원저자
[Voronov 자료 페이지](https://www.pa.uky.edu/~verner/col.html)의
[cfit.dat](https://www.pa.uky.edu/~verner/dima/col//cfit.dat),
[cfit.txt](https://www.pa.uky.edu/~verner/dima/col//cfit.txt),
[cfit.f](https://www.pa.uky.edu/~verner/dima/col//cfit.f)를 직접 회수해
실제 6개 원소/전자수 fit을 13개 후보 방향에 연결했다.

이로써 source-candidate coverage는 39/39다. 과거 finite admission의
10개 공백은 원래 필드에 보존하고, 새 후보는 별도 필드에 저장했다.
원 fit의 하한 단위는 eV, 상한은 keV이며 변수는 $k_BT$에 해당하는
에너지다. 이를 K로 잘못 읽거나 rounded `dE`를 원자 반응 Q로 쓰지
않는다. 원 Fortran의 상수와 큰 $u$에서의 0 반환 규칙도 원문 특성으로
보존했다. D/T/He3/Li6에 대한 실측 isotope qualification은 부여하지
않았다.

### He I 두 fit과 total RR의 광자 수

초기 추출에서 $(Z,N)$만 key로 삼아 He I fit a가 fit b로 덮이는 문제를
독립 입력 검토에서 발견했다. 원자료는 별도 보존하고 correction packet에
두 fit을 분리했다.

- fit a: $3<T<10^6$ K, 원문 RMS 2.5%.
- fit b: $3<T<10^{10}$ K, 원문 RMS 4.7%.
- 기존 alias는 역사적 선택인 fit b에 연결한다.
- RMS는 fit residual이며 covariance 또는 confidence interval이 아니다.
- 같은 물리 owner에 두 fit을 동시에 활성화하는 선택은 거부한다.

[원 설명](https://www.pa.uky.edu/~verner/dima/rec/table.txt)의 total
Case A RR 계수만으로는 총 cascade 또는 escaping photon 개수가 정해지지
않는다. 따라서 13개 역사적 RR 방향의 `total_photon_count`는 `null`이며,
기존 단순 표기의 γ=1을 실제 escaping-photon 승인으로 옮기지 않았다.

## 4. 종·상태·가지와 보존 법칙

종의 구성은 각 핵 constituent의 $(Z,A,\mathrm{isomer})$와 정수
multiplicity, 전체 전하, 전자 상태·분자 내부 상태로 나타낸다.
입력 목록에서 nuclide identity를 읽으므로 역사적 8개 핵종을 확장 상한으로
하드코딩하지 않는다. 별도 회수한 NUBASE source catalogue는 5,843행으로,
ground 3,558행과 non-ground 2,285행이다. non-ground 전부를 isomer로
부르지 않으며, 원 자료의 추정치·준위·resonance·IAS 표지를 보존한다.
이 catalogue 자체가 활성 반응망은 아니다.

정수 사건 열은 $\nu_{ir}=b_{ir}-a_{ir}$로 정한다. 화학 반응에는
각 isotope/isomer constituent 보존과 전하 보존을 적용하고, 핵/약반응에는
baryon number와 전하 보존을 적용한다. 핵 변환은 isotope별 보존을
잘못 요구하지 않는다. 명시한 전자·중성미자에 대해서는 전자 lepton
number도 검사한다. 물질 종의 bound electron 수는
$L_i=\sum Z-q_i$, 자유 전자는 +1, 전자 반중성미자는 −1이다.

예를 들어 중성 T의 spectator bound electron을 유지한 β− 후보는
$\mathrm{T}^0\to{}^3\mathrm{He}^{+}+e^-+\bar\nu_e$로 적었다.
딸 핵종을 중성 He로 놓고 전자를 하나 더 더하는 잘못된 열은 거부된다.
딸의 shake-up/shake-off와 최종 전자 상태별 branch는 미해결이며,
이 number identity가 해당 확률이나 energy spectrum을 결정하지 않는다.

광자·중성미자·cosmic-ray field는 핵종처럼 위장하지 않고 별도 외부 ledger에
기록했다. 같은 γ를 count 2로 한 번 적거나 count 1로 두 번 적는 표현은
canonical signature가 같다. `branch`는 identity의 일부이며, source
variant가 달라도 같은 물리 owner의 중복 선택을 막는다. 역반응의 구조
signature는 제공하지만 역 rate는 상세균형으로 임의 생성하지 않는다.

## 5. Q·불확실성·소비자 결속

원 source의 Q, half-life, branch 또는 fit uncertainty는 native 값과
단위를 그대로 가진다. Q가 없는 자료에는 `null`을 둔다. UMIST
Arrhenius `gamma`는 activation parameter이며 Q가 아니다. 두 source의
차이나 두 fit의 산포도 승인된 confidence interval을 대신하지 않는다.

ENDF MT102의 native Q 2.224648 MeV와 저장된 bare cold Q
2.22456637 MeV는 별도 source record다. 이를 평균하거나 원문을 수정하지
않았다. 기존 nd와 pd cold 값 6.25723026 및 5.49342331 MeV도 재사용한
숫자이며 새 계산 결과가 아니다. CODATA2022 bare p/n/d/t/helion 5개
mass source는 보존했고 전체 반응망에 필요한 mass/covariance closure는
미해결이다. 153 cross-section knots/152 cells와 covariance의
153 groups/154 boundaries를 구분한다.

NUBASE와 오래된 ENSDF/LiveChart neutron half-life 609.8±0.6 s,
613.9±0.6 s를 다른 평가로 저장했다. 어느 하나를 자동으로 선택하거나
합쳐 precision을 높이지 않았다. LiveChart β Q도 원자/핵/endpoint
convention과 consumer binding을 완료하기 전에는 에너지 원장에 넣지 않는다.

이론 문서에서 neutral atomic mass $M_0$, charge $q$의 ion mass $M_q$,
positive electronic binding $B_q$에 대해

$$
M_q=M_0-qm_e+(B_0-B_q)/c^2
$$

를 유도했다. 닫힌 반응의 rest-mass Q는 $Q=-c^2\nu^TM$이며,
$\sum_i\nu_i Z_i=0$인 지정된 원자/핵 비교에서는
$Q_{\rm bare}=Q_{\rm atom}-\sum_i\nu_iB_{0,i}$다.
사용한 state, electron, recoil, radiation/neutrino owner까지 결속되어야
heat source를 정할 수 있다. mass covariance가 있을 때만
$\mathrm{Var}(Q)=c^4\nu^T C_M\nu$를 평가할 수 있다.
이번에는 이 유도만 사용했고 새로운 물리 Q 수치는 계산하지 않았다.

compiler에는 모든 실제 source energy를
`PROVIDER_SOURCE_ONLY_NOT_EVENT_ENERGY`로 넘겨
`UNQUALIFIED:ENERGY`가 유지되도록 했다. 정수 number source의
독립 event flux normalization과 native coefficient의 density/clock
binding을 구분했다. reference density가 반응으로 변할 때의 추가
항도 이론 문서에 명시했다.

## 6. 분자·음이온의 구체적 경계

UMIST 37행은 실제 원문 문자열·계수·온도 구간·정확도 표지를 가진다.
H1/He4 구성은 companion species file의 nominal mapping으로 표시하고
모든 isotope에 대한 실측 검증으로 해석하지 않는다.
반응 74의 10–100 K와 101–3000 K 구간 사이에는
$100<T<101$ K 공백이 있다. 보간으로 채우거나 unsupported 구간을
0 rate로 바꾸지 않았다. 동일 H가 두 번 등장하는 반응 계수와 같은
충돌자가 양변에 나타나는 identity도 보존했다.

UMIST의 CR/CRPH 계수에는 원 $\zeta_0=1.36\times10^{-17}\,s^{-1}$
및 H2 density, albedo, UV field convention이 필요하다. 원문 CRP를
소모되는 proton으로 바꾸지 않는다. PH coefficient는 native radiation
field/dust extinction 기준이며 임의의 cosmological spectrum 또는
self-shielding rate가 아니다. UMIST A/B/C/D 정확도 등급과 Leiden의
A/B/C 정확도 정의는 서로 다르므로 같은 uncertainty scale로 합치지 않았다.

LiH의 1,562개 실제 samples와 summary threshold 579 nm 사이의
범위 불일치는 보존했다. 표에 저장된 zero PI/PD columns도 모든 파장과
상태에서 물리적으로 0이라는 명제가 아니다. Li6H/Li7H의 별도 후보
projection은 source가 지정하지 않은 isotope/rovibrational state를
결정하지 않는다. HD는 J=0…8과 A 8행, para/ortho-H2 충돌 18쌍,
50/100/200 K의 실제 표를 가진다. HD 형성·파괴 chemistry 또는
전체 electronic/vibrational closure를 제공한다고 표시하지 않았다.

## 7. 검증, 실패 보존과 자원

최종 PRIMARY는 20/20 implementation check groups를 통과했다.
독립 reviewer는 원자료와 저장 결과를 직접 비교하고 정수 ledger를
별도로 재구성해 448/448 checks를 통과했다. 공급자 selector, original
Git blob 22개, native units/support, source alternatives, molecule
constituents, weak lepton balance, admission guard와 owner 충돌을 확인했다.
448개를 physical validation 수로 세지 않는다.

첫 PRIMARY의 20개 중 하나가 실패했다. checker가
`ISOTOPOLOGUE_CANDIDATE_ONLY`에 `ISOTOPE`라는 부분문자열이 있을
것이라고 잘못 가정한 구현 오류였다. 첫 결과·실패한 checker·exit=1을
보존하고 해당 predicate 한 줄만 수정했다. 새 attempt `primary02`는
20/20 PASS다. unchanged science의 재계산은 없었다.

입력 검토에서 발견한 He I a/b 덮어쓰기, total-RR photon count,
external-particle canonicalization, 배열을 잘못 주소 지정한 JSON pointer는
각각 원 실패·수정 packet·이전 build ZIP과 함께 남겼다.
[독립 판정](reviews/C9_FINAL.json)과 addendum에 실제 source/output hash가 있다.

각 bounded child는 CPU 30 s, wall 120 s, memory 512 MiB,
worker/thread 각 1을 적용했다. 실제 합계는
[실행 원장](EXECUTION_LEDGER.json)에 기록한다. 이 합계는 측정한 자식
프로세스만의 값이며 source download·preparation·전체 과거 비용을
0으로 간주하지 않는다. PHYS91 primary/reference/Wolfram remaining은
모두 0, 역사적 전체 CPU·금액·global remaining은 `null`다.

## 8. 남은 의존성과 다음 연구 노드

원 인계가 말하는 configured nuclear-network PNG는 실제 안정된
URL·filename·Drive/Dropbox object ID가 회수되지 않았다.
[locator 상태](sources/atomic_nuclear/NETWORK_LOCATOR_STATUS.json)에
확인한 참조와 필요한 최소 식별자를 기록했다. 이것이 없으므로 모든
configured 핵반응·daughter/isomer가 열거되었다고 주장하지 않는다.

다음 source intake는 (1) 해당 원 반응망 이미지의 실제 locator 결속,
(2) isotope/state가 명확한 HD 형성·파괴 및 LiH 형성/비광분해 source,
(3) 새로 선택한 원자 후보의 isotope threshold·branch·uncertainty,
(4) nuclear nominal/covariance와 actual atomic→bare/consumer 결속이다.
각 모형이 선택한 채널에 대해 독립적으로 진행하며, 모든 미래 채널의
완료를 유한 작업의 공통 선행조건으로 만들지 않는다.

이번 [DAG](DAG.json)는 source registry와 integer projection 자식을
scoped-complete로, 전체 target parent는
`PARTIAL_SOURCE_POPULATED`로 기록한다. 원 central contract와
기존 owner 결과는 고정 참조로 보존한다. 게시 commit, expected-SHA
non-force ref update, draft PR, source ZIP, Dropbox/Drive 완료 ACK는
별도 `delivery/` 영수증에 결속한다.

