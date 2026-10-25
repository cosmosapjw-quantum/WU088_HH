# PHYS90 source intake — H-1 capture covariance 계보와 다음 원자료 의무

## 1. 범위와 결론

이 조사는 완료된 PHYS89 `ENDF_MF33_PULLBACK_AND_TYPED_NUCLEAR_CONSUMER_INTERFACE`의 decode·eigh·exact checker·negative witness를 재실행하지 않았다. 부모 FINAL `480baabc73ebaaba735d285d969e79177f5545ed` 및 원 ENDF/B-VIII.1 파일 SHA256 `3024d8f0db604b074e33ed8b05027eb9f5a738614041ba44c83f048e0d0bc1af`를 재사용한다. 새 수치 과학 실행, Wolfram, ODE, benchmark, nuclear rate activation, fast stopping은 모두 0이다.

**새로 닫은 것은 일부 source 역사와 파일 구분이다. 현재 nominal에 결속된 원 precision covariance, current MT102에 승인된 correction, exact capture mass/target-state deck은 확보하지 못했다.** 따라서 선택 물리 노드 `NUCLEAR_BARE_KERNEL_SOURCE_AND_CONSUMER_CONTRACT`는 계속 `PARTIAL_INPUT_DEPENDENCIES`이다. raw 표시행렬에 대한 PHYS89 admission `DISALLOWED_DISPLAYED_MATRIX`와 원인 `NOT_ESTABLISHED`도 유지한다. 새 자료는 원 precision covariance가 불가능하다는 증거가 아니다.

## 2. 33-group → 153-group라는 단일 변환을 가정하지 않을 근거

[NNDC의 Hoblit CSEWG 2011 발표](https://www.nndc.bnl.gov/meetings/nuclear-data-week-2011/Thursday/CSEWG/hoblit-71.pdf)는 COMMARA의 대다수 MF33를 VII.1에 직접 도입했다고 설명하고 H-1을 목록에 넣는다. 이는 공개된 COMMARA 33-group 처리 제품과 native ENDF MF33 채택 경로를 구별할 이유다. 일반 QA에서 FUDGE를 이용한 negative-eigenvalue 제거도 언급하지만, 그 설명은 현재 H-1/MT102 correction 승인이나 이 파일의 원인 판정이 아니다. 원 PDF 830499 bytes와 SHA256 `7fc65960ed20d2835595efae5fe4715567e0e8a5edcdff500c9344676e574bb2`를 확보했다.

이번에는 [NNDC 원 VII.1 neutron ZIP](https://www.nndc.bnl.gov/endf-b7.1/zips/ENDF-B-VII.1-neutrons.zip)에서 `neutrons/n-001_H_001.endf` 한 member의 원bytes를 실제로 복원했다. 전체 ZIP을 내려받은 것은 아니다. tail 65536 bytes와 prefix 14001 bytes 두 range GET을 사용했고, 해당 member의 local-header CRC와 완전한 uncompressed bytes CRC가 일치한다. tail 중앙목차에도 같은 CRC가 기록되어 있다. 두 응답의 weak ETag/Last-Modified는 서로 다르므로 동일 전체 archive의 강한 identity를 주장하지 않는다. 두 range의 전체 길이는 모두 226499549 bytes로 보고되었다. 현재 다운로드되는 원 release member 자체는 2011-12-05 revision 532 / EVAL-OCT05 / 20111222 표기다.

| 공개 객체 | 원bytes / SHA256 | MT102 MF33 문서 header | 적용 한계 |
|---|---|---|---|
| VII.1 원 neutron H-1 member | 54513 / `5bc558ac458face9cea2a1afba7391529df7c136415f1cb5babfab2ced4c97ce` | 21 lines; LS=1, LB=5, NT=105, NE=14 → 13 groups | 현재 153-group의 원 precision source가 아님 |
| VII.1 scattering standard H-1 member | 26325 / `86fb43f98918caa200744343ba7814112e37f5f2f832eba88d809f623919982b` | MT102 MF33 없음 | scattering standard이므로 capture supplier로 대체 불가 |
| PHYS88/89 현재 VIII.1 H-1, 재사용 | 671232 / `3024d8f0db604b074e33ed8b05027eb9f5a738614041ba44c83f048e0d0bc1af` | 1993 lines; LS=1, LB=5, NT=11935, NE=154 → 153 groups | 기존 exact displayed witness와 source gate 유지 |

위 표는 byte identity 및 section header 읽기이다. 13-group 행렬을 새로 수치 decode하거나 현재 행렬과 재계산·PSD 비교하지 않았다. 과거 native MF33가 13 groups라는 점은 공개 33-group 제품과 current153group을 곧바로 같은 객체로 볼 수 없음을 구체화한다.

## 3. 공식 수정 이력이 추가한 연결점

[NNDC VII.1 errata](https://www.nndc.bnl.gov/endf-b7.1/errata.html)는 H-1에 예정된 high-fidelity covariance 대신 older file이 들어갔으며 SVN commit 610, 2013-04-12에 교체했다고 명시한다. 설명의 맥락은 neutron scattering/standards다. 어느 MT block이 어떻게 수정되었는지, 특히 current MT102에 대한 승인 precision 수정인지는 이 페이지가 닫지 않는다.

[NNDC VIII.1 공식 CHANGELOG 원문](https://www.nndc.bnl.gov/endf-releases/releases/B-VIII.1/neutrons/CHANGELOG.md)은 과거 VIII.0 개발 이력도 포함한다. 실제 GET 122162 bytes, SHA256 `4a28ba9249254fc02ab173105103f9d07eb60bf40846cf2112272bc62ddc05cf`를 보존했다. H-1에 관한 기록은 다음과 같다.

| 날짜 / release | 공식 기록의 범위 | 이번 채택 |
|---|---|---|
| 2016-04-08 / VIII.0beta0 | H-1 covariance를 Hale high-fidelity evaluation으로 교체, T. Kawano 표기 | H-1 전체 파일 provenance의 연결점 |
| 2017-02-28 / VIII.0beta4 | 새 standards cross section; documentation과 file33은 아직 미갱신 | nominal 교체와 covariance 갱신을 별개로 추적할 근거 |
| 2017-10-02 / VIII.0beta5 | H-1 covariances added | later covariance 공급 이력이 있다는 근거 |
| 2023-03-01 / VIII.1beta1 | H-1을 other small fixes 목록에 포함 | H-1 단위 변경 표시만 채택 |
| 2023-08-04 / VIII.1beta2 | H-1을 변경 파일 목록에 포함 | MT102-specific 변경 사유는 닫히지 않음 |
| 2024-08-30 / VIII.1 final | 모든 파일 header metadata 갱신; 열거된 17 content-change files에는 H-1 없음 | final 이전 history 추적 필요 |

이 기록은 현재 MF1의 COMMARA/July2011 문구만으로 current153group의 마지막 생성 과정을 확정할 수 없음을 보인다. **2016/2017의 어느 변경이 MT102 153-group를 만들었는지는 확인되지 않았다.** 따라서 “현재 MT102가 2017년에 생성되었다”거나 “현재 공분산이 nominal과 불일치한다”는 결론으로 승격하지 않는다.

## 4. 원 precision 또는 대체 공급으로 승격하지 않은 자료

- [NNDC GNDS 배포 설명](https://www.nndc.bnl.gov/endf-library/B-VIII.1/GNDS/)은 ENDF-6와 GNDS가 같은 underlying data를 담아야 한다고 설명한다. XML이라는 이유만으로 원 evaluator precision 회복본으로 보지 않는다. 1.3GB GNDS archive는 내려받지 않았다.
- [JAEA JENDL-5 H-1 공식 comment](https://wwwndc.jaea.go.jp/jendl/j5/Comment/n_001-H-001.txt)는 기존 영역의 자료가 ENDF/B-VIII.0에서 왔고, 20MeV 위에서는 JENDL-4.0/HE를 병합했다고 명시한다. 이 문서는 independent current153group correction이나 합법적인 tail-bound 확장 계약을 제공하지 않는다. 대체 library 사용은 별도 scientific identity, mass/state, tail/covariance/nominal binding이 필요한 새로운 작업이다.
- [Parsons 2023 low-Z covariance 연구](https://www.epj-conferences.org/articles/epjconf/pdf/2023/10/epjconf_nd2023_13002.pdf)는 VIII.0을 NJOY/ERRORR로 30-group 처리한 결과를 다룬다. H-1 등에서 큰 음의 고유값을 보지 않았다는 해당 처리·해상도 판정은 current native153group의 exact negative witness와 다른 주장이다. 원 precision data나 source-approved correction이 아니다.
- [Paris–Hale 2023](https://www.epj-conferences.org/articles/epjconf/pdf/2023/07/epjconf_cw2023_00020.pdf), DOI `10.1051/epjconf/202328100020`은 R-matrix parameter confidence/uncertainty scaling 방법과 5Li 적용을 설명한다. 이 논문의 confidence scaling을 current H-1 MT102에 임의로 적용하지 않는다.
- [Paris–Hale 2017 발표](https://indico.bnl.gov/event/3580/contributions/10531/attachments/9392/11489/Paris_Hale-csewg_171107_wNJOY.pdf)는 PHYS89가 이미 읽은 자료를 재확인한 것이다. H-1의 R-matrix/capture 도표가 있지만 이번에도 exact mass deck, target electron state, 원 parameter covariance numerical object는 확인하지 못했다.
- 원 VII.1 standards H-1 header AWR token은 `9.986234-1`, neutron H-1 파일은 `9.991673-1`이다. 서로 다른 공개 token을 관찰했을 뿐, 이를 이용해 capture의 evaluator mass/target-state 계약을 추정하여 닫지 않는다. 특히 standards member에 MT102가 없다.

## 5. 다음 원자료 요청을 실제로 좁힐 의무

1. **정확한 capture provenance:** COMMARA native source, 2013 SVN610, 2016 high-fidelity 교체, 2017 nominal/MF33 변경 중 실제 current MT102에 영향을 준 commit/file과 exact identities. 33→153이라는 변환 모양을 미리 지정하지 않는다.
2. **현재 nominal에 결속된 원 covariance:** EDA fit parameter set, parameter covariance 원 precision, nominal/evaluation 버전, confidence normalization, observable Jacobian, energy/group representation 및 relative/absolute covariance 규칙. 원 parameter matrix 대신 원 full-precision group matrix를 공급한다면 그 생성 이력도 필요하다.
3. **표시 precision 의무:** decimal serialization의 실제 rounding rule·precision·오차 범위, PSD/rank 처리, 승인 correction 여부와 수정 전후 identity. PHYS89의 conditional halfULP를 actual formatter guarantee로 승격할 수 없다.
4. **bare kernel 의무:** n/p/d/gamma exact mass deck, LAB/invariant-s 및 angular coordinate 정의, source target/electron state, atomic/bare correction 적용 범위, energy support와 tail mass/energy moments. 원 scattering standard만으로 capture 계약을 대신하지 않는다.
5. **consumer 의무:** thermal/fast/radiation의 실제 named owner·state/history/domain·ACK는 source 문헌으로 대체하지 않는다. PHYS89 typed interface와 미결 요청을 그대로 승계한다.

## 6. 원 precision 입력이 계속 없을 때의 생산적인 finite child

새 과학 contract를 동결한 뒤에만, 부모가 보존한 displayed F와 token-specific halfULP U에 대해 **명시적으로 가정한 rounding box**와 PSD cone의 양립 가능성을 연구할 수 있다. 이는 source 승인 보정 행렬을 생성하는 작업이 아니다.

조건 `C=C^T`, `|C_ij-F_ij|≤U_ij` 아래에서는 임의의 고정 유한 가중치 a,b에 대해

`|a^T(C-F)b| ≤ Σ_ij |a_i| U_ij |b_j|`.

따라서 PSD 후보 존재 여부를 따로 증명하면 유한 consumer functional의 conditional enclosure를 만들 수 있고, 어떤 witness w가 `w^T F w + |w|^T U |w| < 0`를 만족한다면 그 가정된 box 안에는 PSD 행렬이 없다는 명시적인 finite exclusion certificate가 된다. 이 단계는 실제 source CI, 실제 formatter 입증, current source의 물리적 수정, coupled thermal/xe history bound를 제공하지 않는다. 본 child는 이 검사를 실행하지 않았고, 가능·불가능 어느 쪽도 선결하지 않는다.

## 7. 관측 한계와 실행 기록

Exa search3 + batch fetch3, SciSpace search2를 실제 호출했다. Exa fetch URL11 중 text-content 획득8/실패3이며 top-level isError=false가 per-URL 성공을 뜻하지 않는다. Web3 calls도 official source 정밀 탐색에 사용했다. 세부 수와 실패 원문은 `SOURCE_CALL_LEDGER.json` 및 RAW JSON에 있다.

기본 sandbox의 urllib3 요청은 모두 네트워크 권한 거절로 끝났다. 이후 허용된 escalated read-only 요청9 중 원문 수신7(whole object5, range2), IAEA HTTP403 2를 관찰했다. 이것은 다운로드 실패를 원자료 부재로 판정한 것이 아니다. VII.1 source archive 전체 SHA/wholeGET를 수행했다고 주장하지 않는다. 파일들은 원래 repo를 수정하지 않고 새 intake 디렉터리에 보존했다.

이전 과학 허용량0, budget reset=false를 유지한다. 새 연구 retrieval 비용·금액과 전체 역사 미관측량은 null이다. 본 source child의 scientific executions/eigh/integrals/ODE/benchmark/rate activation/fast stopping은0이다. HH_R10=OFF, production admission=NOT_ISSUED, global physics completion=null이다.
