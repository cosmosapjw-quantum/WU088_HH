# WU088_HH R22 연구보고서: HD 반응 상태에너지 소스 정합성과 미발급 Q

**시점:** 2026-10-29 KST. 부모 R21 PR159 HEAD `fd351d0ff97ef0d7a9cf710bdecad922af7e885e`, 형제 R20 PR158 HEAD `1a5c6f47350da2b74e0b7e3071c4db3502810500`. 중앙 WU DAG **34/49 (변경 0)**, R22 R/C **18/20** (R06,C09 비저자 심사 미실행), `HH_R10=OFF`, `production=NOT_ISSUED`, `L4=false`.

## 실제 새 이론 결과

서로 다른 원전의 물리적 역할을 분리했다. 2019년 Lepers/Guillon/Honvault의 39.5 meV는 이온 교환 **기본 상태 (0,0)→(0,0)** 흡열량이며, 35.8 meV 영점진동 차이와 3.7 meV 이온화 전위 차이로 구성된다. 반면 2021년 Zhou 등의 Table 2는 **중성 H+HD** 충돌에서 계산한 HD/H₂ 분자 준위 에너지 표다. GL2022의 105 K SQM 한 방향 **이온 H⁺+HD(0,2)→D⁺+H₂(0,1)** 반응률은 별도 원본 PDF에서 검증된 값이지만, 이 표들 사이에 소스 동일성은 인정되지 않았다.

같은 PES·에너지 기준이 충족된 경우의 일반 항등식은 \(\Delta_{21}=\Delta_{00}-\Delta E_{HD,0\to2}+\Delta E_{H2,0\to1}\). 2021년 원문 인쇄 소수점으로 직접 계산하면 회전 에너지 증가량이 각각 **33.1139561 meV, 14.6911424 meV**다. 이때 세 **별개 조건부 표현**은 다음과 같다.

| 표현 | 조건부 흡열 threshold (meV) | 사건 Q (meV) | 상태 |
|---|---:|---:|---|
| 2021 neutral level 차이, IP 제외 | 17.4288329 | -17.4288329 | neutral-PES diagnostic |
| 2019 ionic ground 39.5 + 2021 rotational corrections | 21.0771863 | -21.0771863 | cross-paper diagnostic |
| 2021 neutral level 차이 + 2019 IP 3.7 | 21.1288329 | -21.1288329 | cross-paper diagnostic |

두 latter 표현의 차이 **0.0516466 meV**는 \((E_{H2,00}^{2021}-E_{HD,00}^{2021})+\delta_{IP}^{2019}-\Delta_{00}^{2019}\)에서 유도된다. 인쇄 수치의 결합 차이를 보존하는 진단이지 실제 Q의 오차막대나 인증 구간이 아니다. 정확한 물리적 Q를 도출하려면 GL2022의 Velilla ionic PES와 일치하는 적절한 HD(0,2)·H₂(0,1) 진동회전 에너지 및 ionization asymptote, 그 출처·불확실성이 필요하다. 이를 확보하지 못했으므로 **physical Q=null**을 유지한다.

R21 조건부 정확한 comoving 반응 extent는 기존 소스에서 재생한 **660441.4261460102 events/(reference m³)**이며 외부 bath 기준항은 **−6.2129205×10⁻¹⁵ J/(reference m³)**이다. 따라서 각 조건부 Q를 투입한 `Q×extent`는 −1.8442211842, −2.2302694449, −2.2357343980 ×10⁻¹⁵ J/(reference m³)의 세 진단수다. **실제 열방출 예측이 아니다.** 열욕조·역반응·수밀도 이력은 R21의 외부 지정을 넘어 물리적으로 풀지 않았다.

## 실제 새 코딩 검증

- 현 세션 Python 3.13.5, g++ 14.2.0 runtime 실행 확인. native subagent 생성 도구 없음, `R6/C9 distinct-author NOT_RUN`.
- R22 코드: `src/cross_paper_energy.py`는 전제된 2021/2019 인쇄 source-literal `Decimal`, 원전 DOI/상태/온도/반응률 SHA를 검사하고, 기존 R18→R21 실제 원본 소스 경로를 호출하여 세 조건부 진단을 생성한다. 직접적인 물리 Q 발급 경로는 없다.
- 초기 `test_wrong_channel_is_rejected`에서 `HD(v0,j2)` 메타데이터를 `HD(v0,j0)`로 변조해도 통과하는 **실제 검출된 identity 검사 결함**을 수정했다. 초기 25/26 FAIL, 수정 후 `unittest 26/26 PASS`, `python -O` 26/26 PASS.
- C++20 exact integer static assertions **5/5 PASS** (actual g++ 14.2.0 compile/run); `tests/exact_integer_cpp.cpp`, `results/CPP20_EXACT_INTEGER.log`.
- Wolfram symbolic **9/9** exact True, 독립 알고리즘 mpmath80 **160/160** PASS, 최대 extent 절대 오차 **5.061769788523247×10⁻¹¹ events/(reference m³)**, 상대 오차 4.58×10⁻¹⁶. 이는 같은 저자의 다른 계산법 검산이지 비저자 심사가 아니다.
- 2개 독립 그림 생성·실제 확인. 초기 에너지 계수 그림의 dashed bath baseline이 legend에 가려지는 표현 결함을 수정하여 물리 주장의 과장을 방지했다. 그 차트의 세 막대는 error bars 또는 credible intervals가 아니다.
- GL2022 원본 PDF 자체 SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`를 실제 현 세션 파일에서 확인했고, 2021 Table 2는 HTML 원문 인쇄 전사에 근거하되 **원본 2021 article raw byte identity는 검증되지 않았다**.

## Cross-repo 읽기 전용 현황

WU PR157(52f9ff3213ac...) source-grid 노출 해, PR158(1a5c6f47350d...) REC/CR 소비자 후보 소거, PR159 parent R21에 각각 대응한다. REC PR156(8806a4f...), CR PR122(f152e28...), REI PR264(7067a0e...), BASS PR247(bd94bf2...), BASS_HE PR108(e1587a...)의 최신 공개 코드·PR 설명을 비교했다. 이들 중 검사된 REC LAMDA HD 진단은 **비반응성 회전 전이**, CR은 **He event mincost flow**, REI는 **H/He/T electron/source** 채널이며 GL2022 이온 교환 4상태 actual owner ACK가 아니다. 읽지 않은 모든 비공개 저장소 또는 generated/native call graph에 대한 absence theorem은 아니다. 다른 저장소는 수정하지 않았다.

## Closeout

**`PASS_SCOPED_EXACT_ENERGY_PROJECTION / HOLD_PHYSICAL_GL2022_Q`**. 검증된 물리 반응률과 출처가 다른 수준에너지들을 혼합하여 물리적 에너지 source로 승격시키는 경로를 봉쇄하고, 가능한 교차 모델 비교를 수학적으로 재현했다. 다음 우선 입력은 GL2022 ionic PES와 같은 energy-zero·mass/BO·isotope-IP convention을 명시한 **상태별 threshold** 원본이다. 다음 독립 업무는 REC/CR owner ACK 및 전체 reachable chemistry consumer. Reverse, thermal bath closure, source-rate uncertainty, full-A 및 L4는 계속 미완료다.

## 원전

- González-Lezana, Hily-Blant, Faure (2022), *J. Chem. Phys.* 157 214302: https://doi.org/10.1063/5.0128598
- Lepers, Guillon, Honvault (2019), *MNRAS* 488 4732: https://doi.org/10.1093/mnras/stz1797
- Zhou et al. (2021), *MNRAS* 507 6012, Table 2 (neutral scattering): https://doi.org/10.1093/mnras/stab2381
