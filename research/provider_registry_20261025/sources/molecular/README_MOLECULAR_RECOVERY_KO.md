# WU088_HH 분자 공급자 원행 복구 — 2026-10-25

## 실제 산출물과 범위

`umist_light_provider_rows.json`은 공식 UMIST Rate22 final 원파일의 8767행에서 명시적인 H/He/D/Li/e/photon/CR label 집합으로 닫힌 37개 반응행, 38개 온도 fit 구간을 추출한다. 실제 남은 종은 H−, H, H+, H2, H2+, H3+, He, He+, HeH+, e−와 source photon/CR driver다. 각 항목의 원행, 행번호, 원행 SHA256, 순서와 중복을 보존한 반응물/생성물, 원 십진계수, 구간, 측정·계산·추정·문헌 출처 코드, 오차 코드, 원 논문 참조를 보존했다. 새로운 rate 평가는 수행하지 않았다.

`lih_photoprocess_provider.json`은 Leiden의 LiH 광해리 channel과 1562개 원표 sample을 보존한다. 해당 source의 isotope와 전자/진동/회전 상태는 지정되어 있지 않다. actual 표의 파장 범위는 91.2–351.1nm이고 같은 공급자의 요약표 threshold는579nm다. 두 정보를 유지하고 표를 확장하지 않는다. 긴 파장 threshold 부근의 우세 생성물 Li+H라는 설명은 전 에너지 범위의 완전 분기비를 제공하지 않는다. 원파일의 photoionisation=0 literal은 보존하되 LiH photoionisation의 전 범위 부재를 주장하지 않는다.

`hd_provider_rows.json`은 고정 중앙 authority의 LAMDA HD bytes를 그대로 재사용해 9개 J-labelled level, 8개 radiative line, 18개 downward collider pair, 각3개 온도 node(50,100,200K)의 원행을 추출한다. p-/o-H2 두 collider는 분리된다. 이는 REC 소유 spectral/collider 입력의 registry용 extraction이며, 기존 scalar reference 계산이나 REC 물리 adapter를 재구현하지 않았다. v-label은 원파일에 없고 기존 webpage의 v=1 불일치가 해결되지 않았으므로 null이다.

## 직접 확인한 공급자 계약

Rate22 구조와 rate 법칙은 [Millar et al.2024](https://doi.org/10.1051/0004-6361/202346908) §2.1–2.2 및 공식 `UDfA2024.pdf`에서 확인했다. Binary k의 단위는 cm³s⁻¹, CP/CR/PH의 단위는 s⁻¹다. γ는 reaction Q가 아니다. CR rate의 source 기준 ζ0는1.36×10⁻¹⁷s⁻¹이고, γ는 H2 density convention 및 1/(1−ω)와 연결된다. ω=0.5는 논문의 사례로서 이번 consumer에 자동 채택하지 않았다. PH 계수는 source ISRF와 dust extinction A_V를 따른다. source가 self-shielding을 포함하지 않는다는 사실도 보존했다.

UMIST accuracy 정의는 원 공급자 웹행 네 개에서 직접 확인했다: [#74](https://umistdatabase.uk/react/74) A<25%, [#998](https://umistdatabase.uk/react/998) B<50%, [#8267](https://umistdatabase.uk/react/8267) C factor2, [#6353](https://umistdatabase.uk/react/6353) D order-of-magnitude. 이것은 Leiden A/B/C와 다른 체계다. 원 카테고리와 출처를 유지하며 covariance 또는 통계분포를 생성하지 않았다.

## registry assembler가 보존할 사항

- Rate22 #74의 두 fit은10–100K와101–3000K다. 100–101K 열린 gap을 임의 보간으로 닫지 않는다.
- CRP/CRPHOT는 prescribed environment driver다. 실제 소비되는 proton 또는 pseudo-electron으로 넣어 baryon/charge ledger를 맞추지 않는다.
- source에 반복 기재된 H product와 unchanged H2 collider를 multiplicity로 보존한다.
- Rate22 species 파일에서 H는 nominal mass1, He는4다. 이는 isotope-shift/isomer/state-resolved rate를 제공하지 않는다. H→1H, He→4He mapping은 selected-model binding으로 명시할 수 있지만 source-native isotope qualification과 분리한다.
- `.specs`의 `Conserved` 및 `Parents` 아래 값은 초기 abundance다. H2의1.00E+00를 mass로 읽거나 cosmological abundance로 채택하지 않는다.
- H3+ DR #1577/#1578은 별도 product channel이다. 실제 계수는 보존하되 완전 branch set, normalized probability 또는 inverse detailed balance를 추가하지 않는다.
- 실제 Q는 세 공급자 모두 chemistry용으로 채택하지 않았다. 에너지 ownership·원자/분자 state·mass convention·consumer가 별도로 결속될 때만 실제 energy admission을 검토한다.
- 모든 extracted row의 `rate_admission`은 false다. approved finite compiler는 원 isotope/charge/stoichiometry 구조에만 재사용한다.

## 남은 coverage와 접근 상태

Rate22 선택행에는 HD, D/T-bearing chemistry 또는 LiH 화학반응이 없다. LiH 광해리와 HD spectral/collision source를 별도 provider로 채워 source gap의 정확한 범위를 보였다. He3/T molecular substitution, molecular isotope rate shift, nuclear isomer와 weak/nuclear reaction은 이 분자 source가 제공하지 않는다.

기존 문서에 직접 연결된 KIDA network URL은 현재 web와 실제 curl에서 모두404였다. Exa/검색의 캐시는 deuterated network와2021 spin-rate correction 경고를 보여 주지만 archive 원행을 복구하지 못했으므로 empirical row로 import하지 않았다. 이 접근 실패는 해당 현재 URL에 한정한다. JPL directory의 LiH/LiD isotope tags는 확인했지만 이번 입력에서는 추가 spectral provider를 채택하지 않았다.

기본 sandbox curl의 실패와 별개로 승인된 require_escalated curl로 UMIST와 Leiden 공식 byte 복구가 실제 성공했다. 복구·파싱 산출물은 `SOURCE_MANIFEST.json`과 extraction scripts로 추적한다. No heavy solver, PHYS91 rerun, rate evaluation, radiation integral, thermal interpolation, isotope scaling, Q computation or empirical admission was performed.
