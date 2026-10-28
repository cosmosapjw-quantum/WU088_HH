# 다음 분자 source intake와 원 nuclear PNG 위치

검토일: 2026-10-25. 대상은 현재 `research/provider_registry_20261025/registry/coverage.json`의 `molecular_chemistry_missing` 세 항목이다. 읽은 파일의 SHA256은 `67e6757038de2783d7b08f4bc840314a7bb2d04a8839c3a821a6be18be4f27f5`이며, 102 provider variants / 125 structural projections를 기록한다. 아래 검토는 이 registry나 동결 source packet을 변경하지 않는다.

## 1. 현재 결손 판정

세 결손 항목은 복구한 원자료와 일치한다. 이미 확보한 HD 자료는 상태전이·비반응성 충돌 자료이고, LiH 자료는 광과정 자료다. 따라서 각각을 HD 화학 형성·파괴와 LiH 형성·비광파괴의 공급자 행으로 셀 수 없다.

| 결손 항목 | 기존 payload가 실제 제공하는 것 | 다음 intake에 필요한 것 |
|---|---|---|
| `source isotope-specific HD formation/destruction` | LAMDA `hd.dat`: HD의 J-labelled 준위 9개, 복사선 8개, p-H2/o-H2 충돌 자료. UMIST의 선택된 37 반응에는 HD/D/T 행이 없음 | HD를 실제 반응물 또는 생성물로 갖는 원행, source의 isotope·spin·전자/진동/회전 상태 정의, 온도 지지구간·단위·불확실성 |
| `LiH formation and non-photo destruction` | Leiden LiH 광흡수/광해리/광이온화 표와 threshold 설명. JPL index에는 LiH/LiD isotope spectral tags만 있음 | LiH 형성 및 비광파괴를 직접 제공하는 일차 반응 source의 locator와 원행. 현재 읽은 연결집합에서는 해당 locator가 식별되지 않음 |
| `D/T negative ions and other requested isotope transfers when configured` | UMIST H− 원행. D−/T− 및 요청 isotope transfer를 직접 식별한 원행은 없음 | 실제 configured 목록과 해당 isotope-specific source. H− 계수의 질량 치환만으로 채우지 않음 |

LAMDA HD 입력의 SHA256은 `0c99fe168235d6d6dac3063093bbbe8b4a2ea15cca53c7e2987763c801fdaefb`다. HD의 핵 조성은 1H+2H로 식별되지만 raw 표의 v 표기와 웹 설명 사이의 상태 결속은 해결되지 않았으며, 원파일에는 coefficient covariance가 없다. 이는 화학 자료의 결손과 별개로 남는다. [HD 원표](https://home.strw.leidenuniv.nl/~moldata/datafiles/hd.dat)

## 2. HD: 이미 연결된 일차 후보와 아직 없는 원행

가장 구체적인 후속 후보는 [KIDA networks](https://kida.astrochem-tools.org/networks)에 기록된 `deuspin.kida.uva.2016.zip`이다. 연결된 논문은 Majumdar et al. **2017**, MNRAS **466**, 4470, [DOI 10.1093/mnras/stw3360](https://doi.org/10.1093/mnras/stw3360), [2016년 preprint](https://arxiv.org/abs/1612.07845)이다. 파일명의 2016과 논문의 출판연도 2017을 구별한다. [UMIST 원 논문](https://umistdatabase.uk/files/UDfA2024.pdf)의 deuterium 논의와 참고문헌도 이 2017년 모델을 직접 가리킨다.

현재 확보 수준은 **논문 identity·파일명·공급자 설명**이다. 기존 시도에서 위 KIDA endpoint는 HTTP 404였고, archive의 실제 download URL·bytes·hash·HD 반응행은 확보하지 못했다. 따라서 이 후보가 현재 registry의 특정 HD formation/destruction 행을 이미 채운다고 판정하지 않는다. `kida.uva.2024.zip`의 존재 또한 deuteration coverage의 증거가 아니다.

기존 Tielens 원문 IV.D, p.1039는 H3+와 HD의 동위원소 교환 및 H2/H3+ isotopologue의 spin 구분을 설명하며, Hugo, Asvany & Schlemmer (2009), J. Chem. Phys. **130**, 164302를 인용한다. KIDA의 이미 읽은 2021년 안내는 이 계열의 구 표에 대한 오류를 지적하고 Sipilä et al. (2017), A&A **607**, A26 및 Hily-Blant et al. (2018), MNRAS **477**, 4454를 가리킨다. 이들은 **수정 여부를 확인할 문헌 식별자**이며, 이번 payload에 correction 원행이 들어 있다는 뜻은 아니다.

다음 작은 intake는 이 archive의 안정된 object/download locator를 회수한 뒤 HD를 포함한 원행만 선택하는 것이다. spin family와 추가 생성물은 실제 선택 행이 요구하는 범위에서 닫고, nominal rate·uncertainty flag·통계분포·상관정보·validity를 원문대로 분리한다. 누락된 정확도나 covariance는 null로 유지한다. 논문 예시 반응식을 configured production network로 대체하지 않는다.

## 3. LiH: 광해리와 형성 사이에 남은 source 결속

이미 연결·복구한 정확한 공급자는 [Leiden LiH page](https://home.strw.leidenuniv.nl/~ewine/photo/display_lih_e2e65bc31792929cfaa15cecf7f23965.html), [LiH.txt](https://home.strw.leidenuniv.nl/~ewine/photo/data/photo_data/cross_sections/LiH/LiH.txt), [cross_section_properties.csv](https://home.strw.leidenuniv.nl/~ewine/photo/data/photo_data/cross_section_properties.csv)이다. `LiH.txt`의 SHA256은 `2463084effc5ad46f7553f9a94789d68d01af18b7591aa1c6370fa6057d5641f`다. 원 header는 Kirby & Dalgarno (1978)를 광해리 참고문헌으로 지정한다.

이 표의 1562점은 91.2–351.1 nm를 덮는다. 요약표의 광해리 threshold 579 nm와 차이를 보존하며, 표 밖 구간을 채우지 않는다. isotope와 전자/진동/회전 상태가 지정되지 않아 6LiH/7LiH 또는 특정 initial state의 실험적 qualification으로 승격할 수 없다. 요약표의 정확도 등급은 복사장 범주에 따른 A/B/C이며 점별 covariance가 아니다. threshold 부근의 우세 생성물 Li+H 설명도 전 구간의 완전 branch probability는 아니다.

광해리의 역과정으로 radiative association을 구성하려면 같은 양자 채널·통계중량·연속상태 정규화·상태 분포가 결속되어야 한다. 현재의 집계 표만으로 그 조건을 확인하지 못했으므로 형성 계수를 만들지 않았다. [JPL catalog index](https://spec.jpl.nasa.gov/ftp/pub/catalog/catdir.html)의 7001/8001/8002/9001 entries는 각각 6LiH/7LiH/6LiD/7LiD의 분광 후보이며 형성반응 공급자가 아니다.

**현재 연결된 자료 안에서 확인된 LiH formation의 직접 일차 provider locator는 없다.** 다음 작업에는 Li isotope와 reactant/product state를 명시한 formation·non-photo destruction 원 논문 또는 원표의 정확한 DOI/URL/file object가 필요하다. 이 문서는 기억에 의한 반응망이나 bibliographic guess를 새 후보로 추가하지 않는다.

## 4. 원 nuclear-network PNG의 구체적인 미확인 입력

[고정 WU 인계서](https://github.com/cosmosapjw-quantum/WU088_HH/blob/34dd7d1d018abff8a0a4ebd1d3f3579ac46d2fad/research/program_expansion_20261025/HANDOFF_KO.md), 고정 중앙 commit `641a725ada4be27473069c2c35005a94c2ab0248`의 [atomic authority audit](https://github.com/cosmosapjw-quantum/rei_bianchi/blob/641a725ada4be27473069c2c35005a94c2ab0248/research/orchestration_expansion_20261025/authority/atomic/AUTHORITY_AUDIT_KO.md), 연결된 `WU_ALL_TARGET_SPECIES_REACTION_REGISTRY` 계약 및 현재 `NETWORK_LOCATOR_STATUS.json`을 대조했다. 읽은 연결 기록에는 **원 그림의 stable file ID, 직접 URL, 정확한 파일명/경로 또는 object locator가 없다.** 기존 상태 `NOT_RECOVERED_NOT_READ` / `INPUT_DEPENDENCY_UNRESOLVED`를 유지한다.

최소 재개 입력은 원 PNG의 실제 Drive/Dropbox file ID, 고정 commit의 repo path, 또는 원출처에 결속된 configured reaction list 중 하나다. 현재 인계서가 지정한 PHYS91 백업 ZIP의 ID는 원 nuclear PNG 자체의 위치 증거가 아니며, 읽지 않은 archive member에 존재한다고 추정하지 않는다. 이는 조사한 연결집합의 결손이며 전 저장소·전 계정에 그림이 없다는 판정은 아니다. 추가 daughter/isomer는 unknown이며 0개로 세지 않는다.

이번 검토는 기존 원문·원표와 receipt를 재사용했다. 새 dataset download, 실제 rate/Q 평가, 완료 계산 재실행, registry 변경은 없다. 현재 세 분자 결손 항목을 보존하며 전체 configured coverage의 완료를 주장하지 않는다.
