# 2026-10-27 WU 재개 권위·병렬 작업 관측

관측 시각: 2026-10-27 02:48:20 UTC. 원격 읽기만 수행했고 과학 실행·저장소 mutation은 0이다.

## 현재 권위

WU PR150은 open/draft이며 HEAD는 `87933da5654bb2e4d93f7de4341df5e0fa0f8716`으로 그대로다. source `71019bb469c92d1ea665155ed98c472b362d6706` 및 source ZIP SHA256 `43845ea085797a6d628b722d58197a64a0af6f0a34a708f3dc981a5274faa906`의 게시·양쪽 actual-byte backup은 이미 완료되어 있다. PR150 이후 새 WU PR은 최신15개 updated 목록에서 관측되지 않았다. AGENTS의 최우선 지침은 기존 R2 target19 supplier registry이며 물리 rate/Q/consumer 승인을 추가하지 않는다. root는 현재87933da의 clean 로컬 복구 및 같은 백업 ID·크기를 별도로 확인했다.

중앙 권위 branch `research/orchestration-sandbox-20261022`는 여전히 `a5db4bac9dafadae29685bbea3cec7f43ab990b2`이다. 따라서 기존에 검토한 그 commit의14WU 노드 근거는 재사용한다. 최신 REI 작업 branch PR236의 HEAD `ee94bef85b56d879dc38f184856a5c613575e9e1`는 별도이다. 직접 읽은 GLOBAL_DAG_STATUS는 작업32/88, 중앙27/88, central_merged=false를 구분한다. 작업 branch의9개 WU_ 독립 계약 blob은 중앙과 정확히 같다. 전체 작업 DAG의 모든 노드를 새로 검토했다고 주장하지 않는다.

## 재사용할 실제 후속 결과

| 결과 | 고정 정체성 | 기존 수용 범위와 남은 경계 |
|---|---|---|
| REI PR234 |95eb74e673553c3bf4c16f73077d2955dac455ee|HE7/REC21 source-keyed 종 사영,71확장 미승인; 작업27→29/88. 동일 사영 재작성 불필요.|
| REI PR235 |3ab52a286a443622492403d89cd2bf80e58fb722|normalized beta·moving exchange15그룹, 이전25검사 재사용. stopping/L4는 미완료.|
| REI PR236 |ee94bef85b56d879dc38f184856a5c613575e9e1|native PW19와25좌표 pre-assimilation source/JVP. 최신 child는28기존PASS+68새검사, 추가노드완료0; REC-COUPLED partial.|
| REC PR138 |4a8e541030ee2cbd02e26ba671083b705d309d49|Oct25 HD/H5 owner 반환 이후 새 HEAD 없음.|
| HE PR102 |ac6042a6b0610b09d0576538767ee0299389a5eb|Oct25 typed source intake와conditional finite-mass exchange 반환 이후 새 HEAD 없음.|
| CR PR106 |b11b2e9255f2b10fb5582376412e045bd1e9151c|finite scalar source/event interface, exactC23B/C23E 소비. 새 microphysics 승인 아님.|

PR236의 고정 입력 경로는 `research/rei_expanded_event_consumer/coupled_source_20261027/ADMISSION.json`, `HANDOFF_KO.md`, `GLOBAL_DAG_STATUS.json`, `implementation/coupled_photo_source.py`다. 실제 열적 assimilation/stopping, native RR/DR·Compton thermal-electron 밀도 결합, 물리 history·오차·응력은 열린 의무다. `lumina_resume_20261026/HANDOFF_KO.md`의 native HeII 입력은 z2.479이고50keV 밖 rate는unknown/null이다. 현재 읽은 자료는 H2 photodisintegration에 필요한 MeV 광자 consumer를 제공하지 않는다.

## 선택한 다음 WU 단위

Root가 새로 회수한 공식 IAEA EXFOR의 원래 target6 직접 수치 packet을 R3 입력으로 선택했다. 공급자 독립 검토 통과 후에만 새 source-binding overlay로27/28→28/28 참조 상태를 바꾼다. 기존 R2 열 전체와 과거27/28 원본 snapshot은 보존한다. 실제rate/Q/heat/consumer/L4 승인은 늘리지 않는다. 이 선택은 이미 완료된 REI 종 사영·PW19 source와 겹치지 않는 WU source 의무이다. 새 packet의 수치·source mapping은 별도의 독립 검토 대상이며 이 권위 관측만으로 승인하지 않는다.

원격 source URL, PR별 HEAD·업데이트 시각, AGENTS·DAG·계약 Git blob SHA는 동명 JSON에 기록했다. 큰 DAG의 connector 본문이 빈 문자열로 반환된 경우 이를 내용 회수 성공으로 해석하지 않았다. 중앙은 같은 commit의 기존 전체 자료를 재사용했고, 최신 작업 branch는 직접 읽은 계약·admission·status에만 결론을 한정했다.

