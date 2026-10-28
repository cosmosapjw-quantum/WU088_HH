# Target 6 원문 정규화 조사 — 2026-10-27

## 판정과 범위

이번 조사는 완료된 R3의 네 TABLE 공급자, 36개 native 행을 그대로 재사용하면서 실제 원 논문에서 측정량과 사건률 사이의 정의를 더 회수할 수 있는지 확인했다. **새 빔 response, 각도 적분 관례, 동일 D의 particle/event 정규화 또는 covariance를 회수하지 못했다.** 접근 실패는 자료의 부재나 물리적 불가능성을 뜻하지 않는다. 이 단계에서 target 6의 실제 사건률을 계산하거나 기존 physical-admission 상태를 변경할 근거는 추가되지 않았다.

SciSpace 논문 검색 두 회와 Exa 검색·원문 경로 조회를 실제로 수행했다. SciSpace는 정확한 세 원 논문을 반환하지 않았고 주변 논문을 반환했다. Exa와 INSPIRE 공식 서지 API는 아래의 정확한 출판물 식별자를 확인했다. 검색 서비스의 자동 요약이나 주변 논문의 결과를 원 실험의 정규화로 채택하지 않았다. 상세 조회 식별자는 `TOOL_AND_ACCESS_RECEIPT.json`에 보존한다.

원 R3, source packet, registry 및 compiler를 수정하지 않았다. 기존 36행 재추출, 수치 적분, inverse conversion, rate/Q 평가, compiler 249-check 및 R1/R2/R3 재실행은 모두 수행하지 않았다. 검색·자료 준비의 실제 CPU/금전 비용은 측정하지 않았으며 0으로 보고하지 않는다.

## 정확히 확인한 출판물과 접근 결과

| 연결된 공급자 | 확인한 원자료 식별자 | 이번에 읽은 범위 | 아직 회수하지 못한 내용 |
|---|---|---|---|
| M0475002 / M0475003 | J. Arends 등, *Experimental investigation of the 4He(γ,d)d reaction*, Physics Letters B **62(4), 411–412 (1976)**, [DOI 10.1016/0370-2693(76)90671-7](https://doi.org/10.1016/0370-2693(76)90671-7), [INSPIRE 114329](https://inspirehep.net/literature/114329) | 출판사 서지·접근 안내, INSPIRE의 출판사 제공 초록·서지, 기존 EXFOR 원 BIB 서술 | 원문 pp. 411–412의 response/acceptance, Table 2의 각도 적분·외삽법, 전체/반구 적분, 동일 D 중복계수, DA와 SIG의 covariance |
| M0826002 | Yu. M. Arkatov 등, *Photodisintegration of 4He into two deuterons*, **Yad. Fiz. 16, 12–16 (1972)**, 영문판 **Sov. J. Nucl. Phys. 16, 6 (1973)**, [INSPIRE 75991](https://inspirehep.net/literature/75991) | INSPIRE 원어판 서지와 기존 EXFOR 원 BIB/COMMON/표 heading | Table 1의 incident-bin 평균 가중치, reconstruction response, angular acceptance 및 적분법, 동일 D convention, 통계 오차 정의·상관행렬 |
| M0011002 | Yu. M. Arkatov 등, *He-4 electrical quadrupole resonance studies by means of reaction He-4(gamma,d)H-2*, **Ukr. Fiz. Zh. 23, 918 (1978)** | 기존 EXFOR 원 BIB 및 저자 제공 TABLE의 출처 표기 | 원 논문 및 author-supplied data의 에너지 response, 총단면적 추출법, covariance, 원문과 저자 표의 차이 여부 |

M0475의 출판사 [abstract 경로](https://www.sciencedirect.com/science/article/abs/pii/0370269376906717)는 PDF 구매/기관 접근 안내와 서지를 반환했다. [article 경로](https://www.sciencedirect.com/science/article/pii/0370269376906717)의 Exa 결과도 서지·참조뿐이었다. ADS의 해당 bibliographic-code PDF 경로는 HTTP 403을 반환했다. 이 결과로 원문 전체를 읽었다고 주장하지 않는다.

Ukrainian Journal of Physics의 [현재 공식 페이지](https://ujp.bitp.kiev.ua/index.php/ujp/en/index)는 옛 archive 경로를 제공하지만, 이번 조회에서 `archive.ujp.bitp.kiev.ua/index.php`는 502, `archive.ujp.bitp.kyiv.ua/index.php`는 crawler 오류를 반환했다. 1978년의 개별 논문 PDF locator는 확보하지 못했다. 다른 논문의 후대 인용만으로 response 정의를 대체하지 않았다.

## 연결된 방법 보고서의 새 locator

[INSPIRE 847959](https://inspirehep.net/literature/847959), **KFTI-76-36 (1976), 23쪽**, Yu. M. Arkatov, P. I. Vatset, V. I. Voloshchuk, V. A. Zolenko, I. M. Prokhorets:

*Metod obrabotki i poluchenie fizicheskikh rezultatov po fotorasshchepleniyu He-4*.

[공식 metadata API](https://inspirehep.net/api/literature/847959)에는 Fermilab의 microfiche 소장 안내가 있고, 다운로드 가능한 원문 첨부는 이 응답에 없었다. 이 보고서가 정확히 M0011/M0826 데이터 처리와 같은 입력·버전을 설명하는지 아직 확인하지 않았다. 보고서 제목만으로 이번 실험의 response를 확정하지 않는다. 별도 사람에게 연락하거나 자료 요청을 보내지 않았다.

## 직접 재독한 기존 공급자 서술이 지지하는 범위

모든 EXFOR 참조는 [IAEA-NDS/exfor_master@939a14d7bba1ddce51975cb5e8711ce96b3b0871](https://github.com/IAEA-NDS/exfor_master/tree/939a14d7bba1ddce51975cb5e8711ce96b3b0871)에 고정되어 있다.

- [M0475.x4](https://github.com/IAEA-NDS/exfor_master/blob/939a14d7bba1ddce51975cb5e8711ce96b3b0871/exforall/M04/M0475.x4), BIB lines 11–26: photon energy는 reaction-particle kinematics로 정하며, 두 D를 두 TOF spectrometer에서 coincidence로 검출한다. 각 팔에서 질량·에너지·각도를 정하여 배경을 제거한다. 이는 coincidence 식별의 근거이고, 공개 DA의 full-sphere particle-yield convention이나 반구 event convention을 정하는 문장은 아니다. M0475002 Table 1과 M0475003 Table 2는 같은 실험의 다른 관측량이며 서로 독립된 실험이 아니다.
- [M0826.x4](https://github.com/IAEA-NDS/exfor_master/blob/939a14d7bba1ddce51975cb5e8711ce96b3b0871/exforall/M08/M0826.x4), BIB lines 8–18: 원어판과 영문판, two-particle kinematics, 자기장 속 He4 diffusion chamber, ERR-S와 beam-intensity uncertainty ≤5%가 명시되어 있다. ≤5%를 Gaussian 표준편차나 임의의 diagonal covariance로 바꾸지 않는다. EN-MIN/MAX와 MICRO-B는 incident energy interval에 속한 SIG 관측량이며, 이를 에너지 적분값이나 flat-bin 평균으로 확정하지 않는다.
- [M0011.x4](https://github.com/IAEA-NDS/exfor_master/blob/939a14d7bba1ddce51975cb5e8711ce96b3b0871/exforall/M00/M0011.x4), BIB lines 8–14 및 M0011002 STATUS: linac/track detector, statistical errors only, 저자 제공 TABLE이라는 사실까지 확인된다. 저자의 EXFOR 승인 표기는 새 물리 admission이 아니다. E2 auxiliary 7행은 total SIG와 분리된 기존 상태를 유지한다.

## 다음 실제 입수 계약

원문의 access 또는 연결된 author response가 생기면 한 실험만 먼저 선택한다. 다음 항목을 각각 원문 페이지·식·표와 연결해야 한다.

1. 각 데이터 행의 incident energy response와 incident-bin weighting. 평균 에너지 한 값 또는 bin 끝점만으로 response를 만들지 않는다.
2. DA의 검출 입자 정의, coincidence event 수와의 관계, 각도 acceptance, CM/lab 변수 및 Jacobian, full/half sphere convention.
3. SIG를 얻은 angular model 및 외삽/적분 연산, 그리고 동일 실험 DA와 SIG 사이의 공통 자료·오차.
4. ERR-S의 confidence/표준편차 정의, beam normalization nuisance의 범위·분포·상관. 부재는 null로 유지한다.
5. 원문을 읽을 권한과 원문 전체를 공개 재배포할 권한을 구분한다. EXFOR의 CC BY 4.0는 논문 PDF의 재배포 허가를 자동으로 부여하지 않는다.

## 후속 이론의 최소 연결만 보존

관측량을 사건으로 바꾸는 연산은 stoichiometric column과 분리한다. 기존 사건 열은 He4 −1, D +2이며 그대로 재사용한다. 만약 실제 측정 response가 주어져 비음수 유한 event-cell vector `x`에 대해 `y = A x`가 구성되고, 특정 consumer functional `qᵀx`에 대해 `q = Aᵀa`가 검증되면 `qᵀx = aᵀy`가 바로 따른다. 이 조건부 선형 항등식은 inverse cross-section fit 없이 이미 측정된 관측량에서 원하는 functional을 구성하는 방법이다. 원 response와 단위·정규화가 미확정인 현재 자료에 구체적 `A`, `q`, `a`를 대입하지 않는다.

동일 두 D에 대한 2는 event column의 생성 입자 수와, full-sphere single-particle angular yield의 적분에서 생기는 multiplicity라는 서로 다른 위치에 나타난다. 따라서 coincidence detection 사실만으로 공개 DA 또는 SIG에 1/2를 붙이지 않는다. 이 조사는 새 불가능성 정리나 새 no-go 결과를 주장하지 않으며, 대체 theorem/code를 구현하지 않았다. Root가 선택한 새 분자 반응 단위를 우선하고 target 6은 위 정확한 원문 입수 조건에서 재개한다.

## 재사용 기준과 보관

- 조사 시 로컬 WU HEAD: `bfdeed676617c8b75ed81ac5e79e800fa69f83db`.
- R3 provider packet SHA-256: `d8b0b92f0374f73fa7f838db5ca07be45bd448696654b07c6db71c5847235ac2`.
- R3 source commit: `80c0d758a5d5b3c030b20c874b8e1852fcb46f82`.
- `delivery/CLOUD_READBACK.json`에서 Dropbox/Drive 두 파일의 실제 다운로드 byte/hash 일치를 읽어 확인했다. 새 백업을 만들거나 완료 계산을 재실행하지 않았다.
- 이 scout의 변경 파일은 `next_loop_20261027/target6/`에만 있다. 원문 PDF 또는 긴 저작권 서술의 공개 복사본은 생성하지 않았다.
