# EXFOR Target 6 독립 source intake 최종 검토

2026-10-27. 검토자 `/root/provider_rows`; source 작성자 `/root/molecule_sources`.

## 판정

**PASS_SCOPED_SOURCE_INTAKE — 9/9 검토군의 합성 판정.** 첫 실행에서 통과한 8개 군과 수정한 G6를 합성한다. 기존 36개 주 표 행을 재파싱하거나 전체 suite를 재실행한 결과가 아니다. 승인 범위는 공식 EXFOR 표의 원행·출처·관측량과 기존 target 6 방향의 source 정체성이다. 실제 rate, Q, 원자 전하·핵 상태, energy deposition 및 named consumer 승인으로 확장하지 않는다. [기계 판정](INTAKE_REVIEW_FINAL.json)

동결 입력은 `IAEA-NDS/exfor_master@939a14d7bba1ddce51975cb5e8711ce96b3b0871`이며 provider packet SHA256은 `d8b0b92f0374f73fa7f838db5ca07be45bd448696654b07c6db71c5847235ac2`, manifest SHA256은 `a1c5d4009d0bfacc4edcb248a6878eef6cdafa9690b4ea0d0826dd5356052d06`이다. 작성자의 parser를 import하지 않고 별도 고정폭 읽기로 실제 RAW와 대조했다. [공급자 packet](../sources/exfor/PROVIDER_ROWS.json), [manifest](../sources/exfor/MANIFEST.json)

## 원행에서 확인한 범위

| 실제 subentry | 확인한 표·범위 | native 단위 | 원래 오차 |
|---|---|---|---|
| M0011002 | 저자 제공 SIG 14행, EN 26–65 MeV | MICRO-B | ERR-S |
| M0475002 | Arends 1976 Table 1의 DA 12행, EN 213/258/330 MeV와 각 46/61/73/87° CM 각도 | NB/SR | ERR-S |
| M0475003 | 같은 실험 Table 2의 SIG 6행, EN 201–359 MeV | NB | ERR-S |
| M0826002 | Arkatov 1972 Table 1의 SIG 4행, EN-MIN/MAX 30–40, 40–50, 50–60, 60–75 MeV | MICRO-B | ERR-S 및 parent의 빔 세기 systematic 상한 ≤5% |

네 TABLE에는 **36행·124개 native 숫자 cell**이 있으며, SIG 24행과 DA 12행을 구분했다. 표기 문자열, 단위, 고정폭 cell, 원문 행, DATA/BIB/COMMON 및 parent locator를 확인했다. M0011003의 E2 보조 자료 7행·21개 숫자 cell은 이 집계에 포함하지 않았다. M0826003 및 M0034005/006의 CURVE 표지는 원문과 제외 기록에서 확인했다. 그래프 digitization은 0이다. [보조 자료](../sources/exfor/AUXILIARY_ROWS.json), [제외 기록](../sources/exfor/EXCLUDED_ROWS.json)

4개 TABLE은 통계적으로 독립적인 실험 4개라는 뜻이 아니다. M0475002/003은 동일 논문의 서로 다른 관측량·에너지 격자이며 공동 covariance가 제공되지 않았다. M0826의 두 출판 reference도 원문과 번역의 관계로 보존되어 있다. 값을 합치거나 평균·재정규화하지 않았다. 원 자료 출처는 [M0011](https://github.com/IAEA-NDS/exfor_master/blob/939a14d7bba1ddce51975cb5e8711ce96b3b0871/exforall/M00/M0011.x4), [M0475](https://github.com/IAEA-NDS/exfor_master/blob/939a14d7bba1ddce51975cb5e8711ce96b3b0871/exforall/M04/M0475.x4), [M0826](https://github.com/IAEA-NDS/exfor_master/blob/939a14d7bba1ddce51975cb5e8711ce96b3b0871/exforall/M08/M0826.x4)이다.

## 관측량·불확실성의 의미 검토

[IAEA LEXFOR Rev.2025/05](https://nds.iaea.org/nrdc/nrdc_doc/iaea-nds-0208-202505.pdf)의 C.1, C.8, D.13, M.12를 실제 공개 PDF 텍스트에서 읽었다. EN은 lab 관례이고 ANG-CM/DATA-CM만 CM을 지정한다. SIG는 이차 입자의 각도·에너지에 대해 적분된 단면적이다. 입사 에너지 적분 INT는 면적×에너지 단위이므로 M0826002의 area-unit SIG bin과 다르다. DA는 각도 미분 단면적이며 EP/POLAR=2는 electric quadrupole 성분이다. Source packet이 이 구분을 반영한다. Full manual PDF의 바이트·SHA를 검증하거나 packet에 포함했다고 주장하지 않는다. [정의 출처 기록](../sources/exfor/SEMANTICS_REFERENCE.json)

ERR-S의 원 숫자와 단위는 통계 오차로 보존되었다. M0826의 5%는 incident gamma beam intensity에 관한 상한이며, Gaussian 표준편차·전체 총오차·공동 covariance로 변환하지 않았다. 다른 계통오차를 0으로 채우거나 서로 다른 오차를 제곱합하지 않았다. Confidence probability와 covariance, 합성오차는 null이다. 이러한 미제공 필드는 source 수치의 삭제 사유가 아니라 후속 물리 연결의 입력 의무다.

에너지 표지는 native 측정 좌표이며 그 사이의 연속 보간법을 제공하지 않는다. M0826의 bin 내부 응답·가중치, 다른 자료의 에너지 해상도, 미분 자료의 각도 acceptance 및 전체 각도 적분 절차는 선택 entry만으로 확정되지 않는다. 따라서 26–359 MeV의 연속 coverage나 그 범위 밖의 0을 이번 표로 구성하지 않았다.

## 동일 D와 기존 event 열의 연결

이번 핵 채널의 수 사영은 기존 R2의 `TARGET19_PHOTONUCLEAR:06`을 재사용한다. `⁴He + γ → D + D`의 material 변화는 `ν_He4=−1`, `ν_D=+2`이다. Bare 좌표를 선택한 기존 열에서는 baryon 변화 `−4+2×2=0`, 전하 변화 `−2+2×1=0`, electron-lepton 변화 0이 성립한다. 이 관계를 새로 컴파일하지 않았다. 원실험의 핵종 label을 bare ionic state의 실측으로 동일시하지 않는다.

나중에 특정 공급자 SIG가 event cross section이고 실제 stationary-target photon spectrum이 결속되면, 그 조건 아래

\[
\Gamma=c\int n_\gamma(E)\sigma_{\rm event}(E)\,dE,
\qquad \mathcal R=n_{{}^4\mathrm{He}}\Gamma,
\qquad (\mathcal C_{{}^4\mathrm{He}},\mathcal C_D)=(-1,2)\mathcal R
\]

로 연결된다. 이번에는 어느 값도 대입하지 않았다. 입사 He-4와 photon은 서로 다르므로 최종 D 두 개를 이유로 초기 동일쌍 계수 1/2를 곱하지 않는다. 이미 실험에서 정의한 SIG에 임의의 final-state 보정을 추가하지 않는다. DA가 이 exclusive channel의 완전한 D 입자 수율이라는 조건에서는 그 전 입자 적분이 `2σ_event`이며, event로 정규화된 관측량에 이를 다시 적용하면 중복이다. 현재 entry의 full/half-sphere 및 particle/event 규약은 후속 결속 의무로 보존되어 있다. 이 때문에 12개 DA 행을 4π배하거나 임의 대칭으로 적분하지 않는다.

단위 대응은 `1 MICRO-B=10⁻³⁴ m²`, `1 NB=10⁻³⁷ m²`, `1 MeV=10⁶ eV`이다. NB/SR는 같은 면적 변환 뒤에도 sr⁻¹를 유지한다. 이 차원 관계만 명시하고 source 값은 원 단위로 보존했다. 에너지 장부에는 입사 photon 제거, 일관된 ionic/nuclear mass와 Q, 두 빠른 D의 운반·감속·열 침적 소유권이 추가로 필요하다. 이 표는 그 Q·분배를 공급하지 않으며 새 계산도 수행하지 않았다. 기존 REC의 원자 광이온화 좌표를 MeV photon consumer로 발명하지 않았다.

[TARGET6_OBSERVABLE_MAPPING_KO.md](../theory/TARGET6_OBSERVABLE_MAPPING_KO.md)도 정적으로 검토했다. 교정된 문서 SHA256은 `a938cb758499c8912bcd2e21e8cf6ea35010928ff9d967163d2494b5cf38085e`이며 판정은 PASS_SCOPED이다. 네 공급자와 독립 실험 수의 구분, 조건부 `∫dσ_D=2σ_event`를 명시하는 두 문구 보완을 반영했다. Source·registry·실행 출력은 이 보완으로 바뀌지 않았다. 최종 JSON의 `post_execution_static_theory_review`가 이 수동 검토를 별도로 기록한다.

## 최초 실패와 표적 교정

최초 `independent01`은 8/9군을 통과하고 G6에서 실패했다. 원 source의 auxiliary record를 checker가 주 공급자 class로 기대한 **검사기 구현 오류**였다. 최초 실패 JSON SHA256은 `eb430e6ddbb0a6688b690b6d553f30a5b0d6e91a9a4e58873988b2fb39f4c654`이며 raw와 최초 command argv를 보존했다. [최초 판정](INTAKE_REVIEW.json), [실패 해설](INTAKE_REVIEW.md), [첫 실행 영수증](../raw/independent01/RECEIPT.json)

후속 `independent_g6fix01`은 main 4개와 auxiliary 1개의 class 구분 및 최초에 진행하지 못한 auxiliary state/admission 조건을 검사했다. **표적 조건 11개와 재사용 identity guard 5개가 통과**했다. Main 4개의 이미 통과한 다른 state/admission 조건 24개와 원래 8개 통과군은 재사용했다. 새로운 전체 suite 성공이나 36행 재검증으로 기록하지 않는다. [표적 checker](check_g6_auxiliary.py), [표적 실행 영수증](../raw/independent_g6fix01/RECEIPT.json)

| 검토 범위 | 최종 근거 |
|---|---|
| G1–G5, G7–G9 | 최초 실행의 8개 pass_scoped 군 재사용 |
| G6 | 기존 main 조건과 수정한 class/미완료 auxiliary 조건의 표적 검증 합성 |
| Target6 이론 문서 | 독립 source 의미·차원·정규화 읽기, 추가 실행 없음 |
| Overlay 구현·release | 별도 `/root/authority_survey` 정적 검토의 범위 |

이번 source 검토는 source author와 별도의 원행 읽기 및 parser 방식으로 수행했다. 공급자의 불확실성·새 물리 rate·Q 정확도를 source 전사 검사 수로 주장하지 않는다. PHYS91 예산의 재설정·이체, 기존 249/R1/R2/PHYS91/REI science 재실행, compiler 호출, rate·Q·각도 적분은 모두 0이다.

## 후속 입력

Target 6에 직접 숫자 공급자가 없던 입력 의존성은 실제 TABLE 원행으로 해소할 수 있다. 다음 물리 계약에는 선택 실험의 energy response/bin weighting, angular acceptance와 동일 D 정규화, 상태·불확실성, 실제 MeV 광자 spectrum과 proper-time/reference-density convention, 하나의 process owner가 필요하다. Rate/Q/energy/state-branch-domain/consumer activation은 계속 false이다. 이는 해당 의존성을 구체화한 source 결속 판정이며 전체 확장 registry의 물리 완료 판정은 아니다.
