# WU 실제 공급자 행 복구 결과

기준은 WU088_HH의 고정 commit `34dd7d1d018abff8a0a4ebd1d3f3579ac46d2fad`다. GitHub의 원문 22개를 복구했고, 모두 조상 `2912a315aa39e7293000b7b2b8c7cc7a706fea9e`의 실제 Git blob과 일치한다. 입력 registry에 기록된 CCC/Verner/CHIANTI/ENDF 원본 해시도 일치한다. 새 scientific rate, quadrature, IVP, PHYS91 replay는 0회다.

`provider_rows.json`에는 실제 공급자 28행이 있다: 원 Verner PI/RR 계수 12행, H1/He4/Li7 finite CI 3행(87/27/13 원 단면적 행 포함), H I CE 4행, CHIANTI 방사 전이 4행, ENDF MT102 1행(153 원 표본), 중성자·삼중수소의 NUBASE/ENSDF 평가 대안 4행. `configured_targets.json`은 실제 기존 21 population을 그대로 보존하며 `historical39_direction_coverage`는 원 CI/PI/RR 39방향에 공급자 또는 명시적 missing/null을 연결한다. 다른 state-resolved 공급자 species는 이 population view와 별도 key로 연결해야 한다.

## 실제 입력에서 중요한 구별

1. **Li7 ionization defect**: superseded elemental ASD 값 5.391714996 eV 대신 isotope-qualified Bushaw2007의 `5.39172060034581005605495430037584732371025203704225285812028` eV를 현재 승인된 finite CI registry에서 복구했다. 단면적 축과 임계점은 그대로다. D/T/He3/Li6의 isotope-resolved CI transfer는 원 source에 승인되어 있지 않다.
2. **원 PI/RR model**: H/D/T, He3/He4, Li6/Li7은 동일한 elemental 계수를 쓰는 명시적 isotope-blind 모형이다. VF RR의 값은 전체 Case A capture 계수이며 특정 final electronic level이나 개별 cascade branch를 제공하지 않는다. 원 coefficient literals를 source row 그대로 보존했다.
3. **H I CE와 방사 branch**: CCC의 file name은 final.initial이다. 2S.1S와 2P.1S는 excitation이다. 원 native gap 10.2043500 eV와 CHIANTI 관측 fine-level 에너지를 바꿔 끼우지 않는다. 2s에는 two-photon A=8.229e+00 s^-1 외에 M1 A=2.496e-06 s^-1도 명시되어 있다. A는 absolute transition rate이며 normalized branching fraction이 아니다. wavelength=0의 two-photon sentinel을 0 energy나 autoionization으로 해석하지 않는다.
4. **MT102 질량/Q**: 원 ENDF QI=2.224648e+6 eV를 보존했다. 현재 CODATA bare-nuclear cold result는 2.22456637 MeV로 원 source Q와 다른 identity다. 기존 SOURCE_MASS_AND_FORMAT_AUDIT의 차이는 81.63 eV다. atomic-to-bare event mapping, 원 nominal/covariance/formatter의 source 승인과 full-support consumer는 미결이다. registry의 n+p→d+gamma는 보존량 확인용 nuclear schematic projection이고 실제 source mass/electron assignment는 아니므로 Q 활성화는 false다. 153 knots/152 cells와 153 covariance groups/154 boundaries를 구별했다.
5. **평가 weak source의 실제 차이**: IAEA의 NUBASE2020 원행은 중성자 반감기 609.8(0.6) s, LiveChart의 ENSDF2005 행은 613.9(0.6) s다. 서로 다른 평가를 별도 공급자로 보존하고 자동 활성화하지 않는다. 삼중수소는 두 source에 12.32 yr가 있으며 원 불확실성 표기를 유지했다.
6. **weak Q와 endpoint**: LiveChart ground-state 표의 qbm은 neutron 782.347 keV, uncertainty 0.0004 keV; tritium 18.59202 keV, uncertainty 0.00006 keV다. 이것은 AME atomic-mass convention이며 naked-nucleus kinetic Q나 beta endpoint로 자동 사용하지 않는다. neutral T의 beta daughter는 한 bound electron을 가진 He3+ state manifold를 거쳐야 하며 electronic shake-up/shake-off와 recoil/spectrum 조건은 미결이다. 전자와 electron-antineutrino의 lepton ledger는 명시했다.
7. **CSV column 함정**: LiveChart decay-rads CSV는 `unc_me`가 두 번 등장한다. dictionary parsing으로 한 uncertainty를 덮어쓰지 않고 column index/name/literal을 전부 보존했다. 별도 decay-rad q uncertainty literal `500`은 ground-state qbm uncertainty와 합치거나 치환하지 않고 unresolved로 남겼다.

## Nuclear catalogue

공식 IAEA AMDC mirror의 NUBASE2020 파일을 직접 복구했다. `nuclear_catalogue.jsonl`은 5,843개 실제 nuclide-state 행을 원 column별로 보존한다. Ground-state 3,558개와 non-ground 2,285개이며, 후자를 모두 isomer라고 부르지 않는다. isomer/level/resonance/IAS의 provider index와 문자 표기를 원형 그대로 보존했다. `#` systematic estimate, ordering ambiguity와 inversion 표시, mass-excess/excitation uncertainty, half-life와 decay/abundance literal도 유지한다. `IS=`는 isotope abundance이며 decay branch가 아니다.

전체 catalogue는 실제 configured population network와 구분한다. 기존 8핵종의 ground rows는 manifest에 따로 있다. Li6/Li7의 IAS 행이 catalogue에 존재해도 이를 기존 configured isomer로 만들지 않는다. 이 구조는 기존 8핵종을 영구 상한으로 고정하지 않으면서 확인되지 않은 목표를 발명하지 않는다.

## 남은 input dependency

고정 handoff 및 연결된 중앙 atomic contract/coverage 기록은 원 nuclear network PNG를 `NOT_RECOVERED_NOT_READ`로 명시하지만, 조사한 계약에는 정확한 파일명·URL·object ID가 없다. 이번 입력복구에서 그 네트워크의 전체 reaction/daughter/isomer 목록을 결정할 수 없다. `NETWORK_LOCATOR_STATUS.json`에 검색 범위와 최소 재개 입력을 기록했다. 이는 그 파일이나 추가 핵종의 전역 부재 주장에 해당하지 않는다.

새 registry가 발급할 수 있는 승인은 source-row identity와 유한 compiler 적용 범위다. 원 249-check synthetic admission, physical rate admission, nuclear-Q admission, consumer ACK는 서로 독립이다. 원 budget remaining=0 및 unknown global remaining=null을 유지한다.
