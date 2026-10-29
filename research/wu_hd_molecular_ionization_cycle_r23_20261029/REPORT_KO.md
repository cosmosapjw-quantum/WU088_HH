# WU088_HH R23 | 분자 이온화 순환으로 상태별 Q 독립 검산 (2026-10-29)

**판정:** `PASS_SCOPED_MOLECULAR_IONIZATION_CYCLE / HOLD_GL2022_PES_NATIVE_Q_AND_OWNER`. R21 PR159 동결, R22 PR160/161 비병합, 별도 WU Draft 브랜치만 변경. 중앙 과학 DAG **34/49 unchanged**, 신규 R23 scoped R/C **18/20**(distinct-author R6/C9 NOT_RUN), HH_R10 OFF, production NOT_ISSUED, L4 false.

## 핵심 수학

R23은 원자 IP 및 D0 경로와 독립된 **분자/분자이온 단계별 이온화 에너지** 네 개로 이온반응 흡열량을 계산하는 새 구성적 경로다:

`DeltaE_21=I(HD)+I(HD+)-I(H2)-I(H2+)+epsilon_H2(0,1)-epsilon_HD(0,2)`.

이 식은 자유전자 에너지 영점이 같은 ionization 단계의 합과 차에서 **정확히** 유도된다. 참조 출처: Hölsch 2023 HD, Doran 2026 H2, Korobov 2017 HD+/H2+, Cozijn 2022 HD rotational, H2 rotational Salumbides 2011 (Jennings1984 원 출처). 2026 논문은 **accepted 2026-08-31**, 정식 발간 완료로 바꾸지 않는다. SI상수 h,c,e 고정.

**새 계산:** ΔE=**168.973314814208608276... cm⁻¹** (= 약 20.95002099384046 meV 흡열). 따라서 Q=-20.95002099384046 meV/event, J/event=-3.356563411814064e-21. R22 PR161의 외부 분광 D0/IP 순환 ΔE=168.9733160842086...cm⁻¹와 차이는 **−1.27×10⁻⁶ cm⁻¹**, 등가 **−38.073642166 kHz**. 입력 출처가 일부 같은 2017 이온 계산을 공유하므로 완전히 통계적으로 독립적인 검증은 아니다. 약 0.000177867cm⁻¹의 quoted-marginal L1은 **error bar가 아니다**.

**GL2022에 대한 지위:** JCP 157 214302 DOI 10.1063/5.0128598은 Velilla2008 ionic H3+ PES를 사용하지만, SQM 내 정확한 동위원소 이온화 보정·상태 문턱 원자료가 아직 없음. 따라서 **물리 Q, bath heat, 역반응, detailed balance 전부 NULL**; no mere rate-to-Q inversion. 2019 Lepers의 3.4 meV는 **다른 제품 j′=0**, BO/코드 및 coarse 숫자, 2021 erratum은 thermal spin aggregation이며 목표 j′=1 문턱을 직접 고정하지 않는다. 2021 Zhou neutral H+HD PES도 GL2022 ionic H+ + HD와 동일하지 않다.

## 실제 코드/검산

- 소스 입력 여섯 값·원전 DOI·quantum state/order·GL2022 PDF SHA·R21/R22 원본 ZIP SHA 엄격 검사, 원본 실제 SHA/CRC, 2019 SI 정확한 h,c,e 이용.
- R21 SOURCE ZIP 432135 bytes SHA256 `5ace176fdba1b1ed01cedbd11e381b98ee242475ef1a401d89dcfcf0b7a3d220`, source PDF 273554 bytes SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754` 현재 재검증.
- R22 PR161 SOURCE ZIP 95734 bytes SHA256 `5d92267615c91e9c34c9c496956bdf58473ee41f1db6e58ccbbbfbf4fd95477c` 현재 재검증.
- 기존 R21 원본 복원 unittest 18/18, 기존 R22 PR161 복원 22/22, 신규 R23 Python 29/29 및 `-O` 29/29, SymPy exact symbolic, mpmath100/independent Fraction, Wolfram exact identity true. 국소 테스트이며 GL2022 PES physics validation 아님.
- 실제 원본 바탕 두 synthetic 그림 생성·시각 검수. 이온화 input perturbation은 D0의 같은 출처 재계산과 함께 움직여야 한 정확한 항등식; 이를 atomic ionization *physical gauge*라고 부르지 않는다.

## 최신 저장소 범위/소유권

WU PR160 `9db6f91...`(cross-paper)와 PR161 R22 spectroscopy는 병렬 근거. REC PR156 `8806a4f...` LAMDA HD rotational nonreactive; CR PR123 `9f520c5...` He exact SSP multi-budget; REI PR265 `9b0b97aa...` H/He photo-only lumping; BASS PR251 `cd7e7efd...` Bianchi-I pressure enclosure; BASS_HE PR109 `11b3cfdb...` D-pair nuclear angle. REC/CR 전체 런타임 call graph 및 owner ACK는 확정되지 않았으며 기존 최신 PR들 자체가 본 목표 4-state reactive donor를 제공하지 않는다는 *선택경로 판정*만 채택. 다른 repo에 쓰지 않음.

## 남은 승인 조건

GL2022 본문/PES 원본 1) isotope-asymptote energy source/zero and mass convention 2) exact HD(0,2)→H2(0,1) threshold 3) proper ionization offset (or explicit omitted convention) 4) original scattering threshold and rate consistency 5) uncertainty provenance 필요. 역반응과 상세평형, 실제 bath/energy deposition, full-A, REC/CR named owner ACK, distinct-author R6/C9 별개. 중앙 34/49는 변경하지 않는다.
