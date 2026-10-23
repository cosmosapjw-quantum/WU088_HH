# PHYS83 R2–R3: H I 충돌 여기와 복사 사건 source 계약

## 판정

실제로 내려받은 CCC 저자 database의 `2S.1S`, `2P.1S` 두 excitation table을 선택한다. 각 452개 행이며, 역전이 raw table도 각각 451개 행을 보존했다. 파일명은 **final.initial**이다. `2S.1S`는 1s→2s이며, `1S.2S`가 역전이다. README와 각 table header가 이 해석을 독립적으로 지지한다. 원 자료의 영역은 (E_{\uparrow}=10.20435\)–(968.6058\) eV, 단면적 단위는 (a_0^2\)이다. 원 자료·추출·비교의 기계 판독 계약은 `HI_CE_SOURCE_CONTRACT.json`이다.

Source 연구의 선택은 R2/R3이며, 새 Maxwell 온도 grid, 과학 profile, ODE, benchmark 또는 기존 완료 identity는 실행하지 않았다. 소스의 행 파싱과 reciprocal print-precision consistency만 수행했다. Parent의 다음 구현은 새로운 단면적 입력에 대한 계산으로 별도 기록해야 한다.

## 원전·데이터와 대안

1. **선택: CCC author H I LS data.** https://atom.curtin.edu.au/ccc-db/index.html 은 H I의 complete (n_i\le9\) dataset을 August2026로 표시하고 Bray–Stelbovics1992, DOI10.1103/PhysRevA.46.6995로 연결한다. 실제 archive HTTP Last-Modified는2026-10-12이고,2026-10-23 snapshot은 `57730e72656639e92c47c1b8457db0edac5a69ae93db6c357471a93759af1fc9`이다. 표시된 data month, archive 수정 시간과 수집 시간은 다른 metadata다. 현재 원본 데이터와1992논문 당시 table을 동일 bytes라고 주장하지 않는다. 원논문 공식 abstract를 읽었고 full text authorization wall은 우회하지 않았다.
2. **대안: CHIANTI H I effective collision strengths.** Official page https://db.chiantidatabase.org/h/h_1.html 및 NASA SolarSoft의 `.scups`는 Anderson2000, revised2002를 명시한다. 값은 Burgess–Tully scaled **Maxwell 평균 effective collision strength**로, 국소 단면적이 아니다. 2002 corrigendum은 기존2000 table을 대체한다고 명시한다. 이 대안은 source-native T 영역/변환/보간을 별도 구현해야 하므로 이번 CE 단면적 입력으로 활성화하지 않는다. 다만 동일 공식 dataset의 radiative A와 level metadata는 아래와 같이 채택 가능하다.
3. **보류: Benda–Houfek2018 ECS data.** DOI10.1016/j.adt.2017.02.003의 저자 제공 원문은 (n=4\) 문턱 이하 resonance-resolved T matrices와 detailed-balance consistency를 다룬다. 실제 raw T-matrix dataset을 이번 module에 반입하지 않았고 더 정확한 결과를 이미 얻었다고 주장하지 않는다.

Exa와 SciSpace를 각각 실제1회 호출해 위 경로와 원전 후보를 찾았다. Connector raw receipts는 `EXA_HI_RAW.json`, `SCISPACE_HI_RAW.json`이며 source 사실은 공식 원문·데이터로 좁혔다. SciSpace의 검색 요약 자체를 수치 input으로 삼지 않았다.

## 에너지 좌표와 통계 가중치

두 excitation table에는 (E=10.2043500\) eV, σ=0인 문턱 행이 **원래 들어 있다**. 다음 행은10.2043885eV이며, 두 역전이 table의 첫 에너지는0.0000385eV다. 451개 대응 행 모두에서 (E_{\uparrow}-E_{\downarrow}=10.20435\) eV가 binary64 readout 차이9.1e-14eV 이하로 일치했다. 이 마지막 숫자는 parsing arithmetic의 차이이며 물리적 문턱 오차가 아니다.

Source의 LS 상태에는 (g_{1s}=2\), (g_{2s}=2\), (g_{2p}=6\)을 사용한다. Fine-structure metadata에서도2p의 (J=1/2\)와 (3/2\) 가중치2+4가 이를 지지한다. Source reciprocity

\[
g_{1s}E_{\uparrow}\sigma_{\uparrow}
=g_u E_{\downarrow}\sigma_{\downarrow}
\]

를 raw 대응 행에서 검사하면 최대 상대 잔차는2s4.62361378e-4,2p6.39319499e-4이다. 출력 단면적은 대체로4유효숫자다. 각 printed E와σ가 마지막 자리까지 nearest rounding됐다고 가정하고 half-last-digit decimal interval을 만들면 **각451행 모두** 양쪽 flux interval이 겹친다. 이것은 printed precision과의 일관성 확인이며 source error bar나 물리적 신뢰구간을 만드는 절차가 아니다. `CCC_PRINT_PRECISION_CONSISTENCY.json`에 가정과 판정을 기록했다.

Literal gap은 (10.20435=0.75\times13.6058\) eV다. 이를 native Hartree27.2116eV 사용과 일관된 값으로 **추론**할 수 있지만, 원 자료의 에너지축을 현대 CODATA Hartree27.211386…eV 또는 isotope-specific NIST fine-level gap으로 몰래 바꾸지 않는다. 현재 자료만으로 isotope-resolved finite-mass scattering을 확보했다고 주장하지 않는다.

면적 변환은 NIST2022 CODATA의 (a_0=5.29177210544\times10^{-11}\) m를 써서 σcm²=σa0²(100a0)²로 정한다. 이는 부모 C22D/PHYS81의 `A0_M`과 같다. NIST standard uncertainty는8.2e-21m이며 계산 고정 입력과 측정 불확실성을 구별한다. 공식 constant source는 https://physics.nist.gov/cgi-bin/cuu/Value?bohrrada0%7Csearch_for=bohr+radius 이다.

## 부모가 선택한 새로운 보간 계약

Parent가 제안한 kernel은 ε=E−Δ에서

\[
W(\epsilon)=(\epsilon+\Delta)\sigma_\uparrow(\epsilon+\Delta)
\]

의 양의 piecewise-linear 보간이다. 역전이는 동일 support 위에서 σdown=(g1/gup)W/ε로 구성한다. 그러면 하나의 양의 Maxwell moment로 양쪽 rate를 얻고 유한 연산자에 대해 exact detailed balance를 보존할 수 있다. 이 보간은 **σ 자체의 PL 보간과 다르다**. 공급된 역전이 table을 별도로 PL 보간하면 그 별도 선택에 따른 상세평형 오차가 생기므로 production 모델로 자동 결합하지 않는다. 원 역전이 table은 source reciprocity witness로 보존한다.

원 reverse sample은ε≥3.85e-5eV에 존재한다. 새 reciprocal model의 첫 cell이ε=0까지 이어지는 것은 원 excitation의 문턱 행과 명시한 W-PL 선택에 따른 구성이다. 원 reverse sample에0행이 있었다고 기술하지 않는다. 상단968.6058eV 밖의 실제 단면적은 이 자료로 닫히지 않는다. 유한 연산자에서 제외하는 것과 물리적으로0이라고 주장하는 것은 다르다.

## 복사 rate와 사건 에너지

공식 CHIANTI H I page는 ion metadata VERSION11.0.1이며 전체 database 다운로드 page의11.0.2와 구별한다. 원본 `.elvlc`, `.wgfa`, `.scups`를 모두 byte identity로 보존했다.

- 2p1/2→1s와2p3/2→1s는 각각 (A=6.260\times10^8\) s⁻¹이다. 따라서 두 상태를 같은 LS upper state로 묶을 때 이 A는 그대로 쓸 수 있다.
- 2s→1s two-photon rate는 (8.229\) s⁻¹이다. 이 event는 총2개의 photon을 만들며 두 에너지의 합이 선택한 atomic gap이다. A 하나로 photon별 spectrum은 결정되지 않는다.
- `.wgfa`는 작은2s M1 branch (A=2.496\times10^{-6}\) s⁻¹도 별도로 준다. 이를 제외하면 선택한 채널 목록에서 제외했다고 적고, two-photon이 유일하게 가능한 decay라고 말하지 않는다.
- zero-wavelength2s 행에 붙은 `[autoionizing rate]`는 일반 출력 label이다. 이 H I bound2s→ground 항을 autoionization으로 활성화하지 않는다. 공식 database의 Parpia–Johnson1982 귀속과 원논문 abstract의2E1/M1 구분을 함께 사용한다. λ=0은 총 photon energy0이 아니다.
- `.scups` 주석의 Parpia–Johnson1972는 PhysRevA26,1142와 맞지 않는다. 공식 `.wgfa`·page·DOI record는1982를 지시한다. 원본은 수정하지 않고 문헌 정규화 기록에서만 바로잡았다.

NIST fine-level metadata의2s energy는82258.956cm⁻¹,2p1/2는82258.921cm⁻¹,2p3/2는82259.287cm⁻¹다. 이 값들은 CCC native gap과 다르다. 이번 approximate LS module을 구성할 때는 **collisional loss, stored atomic energy와 total emitted energy에 동일한 CCC Δ**를 사용하도록 권고한다. 이는 fine-structure/isotope precision line transport의 완성이 아니라 명시적으로 닫힌 native energy 회계다.

## 열린 의무와 범위

CCC README는 degenerate LS에서2s↔2p와 같은 Δl=±1 전이의 integrated cross section이 formally infinite임을 명시한다. 따라서 이 mixing을 빠뜨린 ground-star module의 high-density quenching/saturation은 **조건부 subset 결과**다. 실제 plasma에서 혼합이 무시 가능하다는 결론은 이 자료에서 나오지 않는다. Finite splitting, cutoff, electron/proton mixing의 source 계약이 후속 의무다. 이 관찰은 일반적인 물리 no-go 주장이 아니다.

추가 excited-state ionization, 상위 준위와 cascade, radiation absorption/stimulated terms, Lyman-alpha 재처리, two-photon spectrum과 cosmological transfer는 이번 source 반입으로 닫히지 않는다. 현재 모형의 mathematically exact conservation과 물리 채널의 completeness를 구분한다.

## 보존·재사용

CCC archive는 저자 공식 공개 다운로드지만 index/README에서 명시적 redistribution 또는 SPDX license는 발견하지 못했다. MIT나CC-BY라고 이름 붙이지 않는다. CHIANTI의 official referencing page는 database의 첫 논문·사용 version·원 계산 논문 acknowledgement를 요구하고 다른 database에 반입할 때 version을 표시하도록 안내한다: https://www.chiantidatabase.org/referencing.html .

필요한 최소 수치 입력과 원 출처·hash를 함께 보존하고, 원 논문 전체 PDF를 공개 repository에 복제하지 않는다. 전체 조사 receipt와 다운로드 source archive는 요청한 private checkpoint에 보존할 수 있다. 이 문서는 source가 부여하지 않은 코드 license를 만들어내지 않는다.

## 산출물

- `HI_CE_SOURCE_CONTRACT.json`: machine-readable source, domain, units, state, radiative/event and reuse contract.
- `CCC_2S.1S`, `CCC_2P.1S`, `CCC_1S.2S`, `CCC_1S.2P`, `CCC_README`: 채택하는 원문 numerical input.
- `CCC_PARSE_AND_SOURCE_RECIPROCITY.json`, `CCC_PRINT_PRECISION_CONSISTENCY.json`: 직접 source consistency 계산.
- `h_1.elvlc`, `h_1.wgfa`, `h_1.scups`: 공식 CHIANTI 원문.
- `CCC_ARCHIVE_MANIFEST.json`, `CCC_SELECTED_MEMBERS.json`, `PRIMARY_FETCH_RECEIPT_*.json`: typed byte provenance.
- Exa/SciSpace/Web/NIST raw receipts: 접근 범위와 실제 획득 근거.

Maxwell rate evaluation0, science profile0, ODE0, benchmark0, 완료 identity 재실행0. 다음 parent 작업은 이 source 계약과 원리 유도를 고정한 뒤 새로운 finite W-PL CE 연산자를 구현·검증하는 것이다.
