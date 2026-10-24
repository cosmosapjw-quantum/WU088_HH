# PHYS89 covariance provenance의 추가 원전 조사

## 결론

현재 MF1의 COMMARA-2.0/July2011 출처문구는 채택한다. 다만 **원 COMMARA 제품에서 현재153group MF33 및 새 nominal evaluation으로 이어지는 정확한 변환 계약은 닫히지 않았다**. 다른 provenance라는 사실만으로 잘못된 covariance라고 단정하지 않는다. 이번 작업은 원자료의 PSD 계산을 하지 않았다.

## 실제 조회와 채택 범위

Exa search1, SciSpace search1, Exa batch fetch1회로 primary URL2개를 읽었다. 추가 조회 한도는 소진됐고 더 검색하지 않았다. Wolfram0, numerical children0, 적분0, 기존 과학 재실행0이다. Raw tool responses는 이 디렉터리의3개 RAW JSON에 보존했다.

[AFCI/COMMARA-2.0 공식 보고서](https://www.osti.gov/servlets/purl/1013530)는 ENDF/B-VII.0 central values와 함께 쓰는33group 제품을 설명한다. NJOY의1/E flux 처리와[1e-5eV,19.6MeV] group 범위를 명시한다. 실제 fetch 결과는 보고서 abstract/metadata/references였으며 full PDF나 원bytes를 확보한 것은 아니다. 현재 raw MF33의153groups/154boundaries와 같은 배열이라고 주장할 수 없다. [DOI](https://doi.org/10.2172/1013530)

[Paris–Hale의2017 LANL 원 발표자료](https://indico.bnl.gov/event/3580/contributions/10531/attachments/9392/11489/Paris_Hale-csewg_171107_wNJOY.pdf)는 relativistic R-matrix, nuclear/electromagnetic channel, polarized/unpolarized observable과 parameter covariance에서 observable covariance로 가는 일차 전파를 설명한다. H1 capture의 uncertainty/correlation plot도 있다. 현재 파일 hash, exact mass deck, target electron-state 계약과 current153group PSD 판정은 확인되지 않았다. 일부 수식·그림의 추출이 훼손돼 수치 normalization 규칙은 채택하지 않았다.

[BNL2020 covariance-testing 자료](https://indico.bnl.gov/event/7233/contributions/43619/attachments/31606/49925/Cov-Testing-dbrown.pdf)와 [NNDC2010 QA 보고서](https://doi.org/10.2172/1013490)의 검색 발췌에는 eigenvalue 검사와 ENDF numerical precision에 대한 제한이 있다. 이는 일반 지침이다. 현재 H1 행렬의 PASS, 미래 negative-minor의 원인 또는 raw data의 임의 교정 허가는 아니다.

SciSpace는10개 논문 lead를 반환했지만 이 current ENDF covariance의 identity/PSD/mass/target-state를 직접 닫는 원문은 제공하지 않았다. 대체 EFT kernel, 다른 핵종 논문, 원전 미확인 index metadata는 current source의 근거로 승격하지 않았다.

## 다음에 실제로 필요한 입력

1. Current MF3/MF6 nominal과 일치하는 evaluator-identified covariance object 및 exact identity.
2. 원 parameter/group covariance에서 current MF33으로 옮긴 binning, energy map, relative/absolute normalization, nominal-version 관계.
3. 표시 행렬에 결함이 발견될 경우, 원 precision covariance 또는 source-approved correction과 변환 이력.
4. n,p,d,gamma mass deck 및 source LAB/invariant-s 정의, target/electron-state 가정과 correction의 적용 범위.
5. Covariance가 angular/energy/mass/state 중 어디까지 다루는지에 대한 계약.
6. 실제 thermal/fast/radiation consumer의 state/history/domain/owner ACK.

이 입력을 얻지 못한 상태는 INPUT_DEPENDENCY다. 물리 no-go나 전체 uncertainty 결과가 아니다. Physical node=PARTIAL, HH_R10=OFF, production NOT_ISSUED, global completion=null을 유지한다.
