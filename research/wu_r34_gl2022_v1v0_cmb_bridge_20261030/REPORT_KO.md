# WU088_HH R34 | 다음 이론·코딩 루프 연구보고서

**판정:** `SOURCE_LOCKED_TWO_STAGE_PHYSICS_SCOPED_COMPLETE`, `EMAA_PRIMARY_ASCII_BLOCKED_INPUT_MISSING`, `CANONICAL_DAG=34/49_UNCHANGED`.

선행 WU PR #172 HEAD `5def43ef162fcf7bff43f6c90a31a5a3a48959b6`, 부모 PR #171 HEAD `320b3a7252b0bb9fe8b3cbdb40f816545a33bed1`는 변경하지 않았다. 사용자 요청에 따라 다른 Repo의 REC/REI/BASS/CR 연구 현황은 읽기 전용으로 조사하였으며 각 물리 원본의 source owner를 넘는 이식은 하지 않았다.

## 문헌과 원자료 현황

- González-Lezana, Hily-Blant & Faure, JCP 157 214302 (2022), DOI 10.1063/5.0128598: 원본 GL2022 SQM v1 소광과 v0 반응율의 물리 계산 입력으로 사용.
- EMAA 공식 데이터 DOI https://doi.org/10.17178/emaa_hd_rovibration_805a7aa5 : H+ 171 transitions/25 temperatures, 5–3005 K, RADEX original selector-based export. 공식 문서 https://emaa.osug.fr/documentation , https://emaa.osug.fr/file_format 에서 H+ partner ID 7, cm−1 및 cm³/s 명시. **원본 numeric ASCII 미확보**. 공식 DOI 메타데이터를 수치동등성 증거로 쓰지 않음.
- R32 historical CDMS2011 v2 displayed transcription과 R33 Sung 296K line-center fitted transcription의 energy representation이 다르다는 점을 실제 에너지 장부에서 분리함.

## 실제 신규 계산 (보조 물리)

6개의 원본 공통 기체온도, R32 진동-소광 정책 2개, v1 초기 J 7개, R33 정책 2개, 프로톤 밀도 3개, 외부 복사 경계 7개: **3528** source-derived restricted two-stage cases. H2 생성물 분기 **35280**행, 4개 회전선별 photon exchange **14112**행, z∈[0,300] endpoint-sign root 후보 **504**, 실제 bracketed root **324**.

표본 `Tgas=105 K`, `DB_UPWARD_V1`, `v1 J0`, `Eq6-7_spin_effective`, `n/ncrit=1`: v1 첫 소광이 R33 영역 `v0 J≤4`로 들어오는 확률 0.3587827519512391; z100 제한 복사 에너지 교환 -2.8614878750948852e-21 J/초기 v1 HD; radiation-neutrality root z≈46.717810. 원본 두 에너지 표현의 seam 최대 2.0195212731651592e-27 J를 보존. 이는 화학반응 Q 또는 가스 전체 heating이 아님.

새 출력의 내부 검산: 일반 Python unittest 10/10, `-O` unittest 10/10, compileall PASS. Full grid p-sum defect ≤1.893e-14, first-rad probability partition defect ≤9.55e-15, energy seam을 포함한 장부 residual ≤8.426e-35 J, root residual ≤1.201e-31 J. root sign 변화 부재 구간은 NO_ROOT로 단정하지 않고 UNBRACKETED로 표시. Wolfram symbolic telescoping identity 0 was observed in the same run; **서로 다른 작성자 R6/C9는 NOT_RUN**.

## 정확한 claim 및 stop condition

R32→R33 물리 계산은 **source-derived conditioned**이며 전면적 동일 반응계의 완결된 19준위 kinetics로 볼 수 없다. 원본 R32의 v1 복사·반응 경로는 소스 미확보, R32 고J quench branches는 의도적으로 바깥 영역, R33 외부 복사장은 prescribed blackbody이고 실제 재결합/광학두께/시간 진화가 없다. EMAA의 공식 proton RADEX 파일과 비교한 수치 행수 **0**. 미확보 원자료를 0으로 치환하지 않는다.

- 중앙 WU DAG: **34/49 unchanged, +0 canonical**.
- 신규 R34 보조 유도/계산: **1/1 scoped**, canonical promotion 대상 아님.
- 새 R/C 단계 상태: **18/20 scoped**; R6 및 C9는 distinct-author 보류.
- `PES_NATIVE_THRESHOLD=NULL`, `PHYSICAL_Q=NULL`, `OWNER_ACK=NOT_OBTAINED`, `HH_R10=OFF`, `FULL_A=NULL`, `L4=false`, `PRODUCTION=NOT_ISSUED`.
- `NO_MAIN_MERGE=true`, `NO_FOREIGN_REPO_MUTATION=true`, `AUTO_NEXT_NODE=false`.

다음 단위는 여전히 `WU_HD_EMAA_171x25_PRIMARY_RADEX_CROSSWALK`. 공식 H+ collision RADEX ASCII bytes 확보, 실제 해시·상태 양자수 매핑·동일 T·반대 전이 방향을 독립 검사한 뒤에만 비교/승격 논의. 새로운 고J rate 또는 19-state complete rate network는 이번 연구에서 주장하지 않음.