# R2 게시 메타데이터 독립 검토

**판정: `PASS_SCOPED_RELEASE_METADATA`. 남아 있는 게시 차단 사항은 없습니다.** 이 판정은 고정된 R2 자료·정수 투영 결과의 게시 범위와 인계·DAG·출처 경로를 대상으로 합니다. 새 반응률, 핵 Q, 소비자 결합 또는 전체 연구의 물리적 완료를 승인하지 않습니다.

## 확인한 범위

원래 사용자 target은 19개 ID와 28개 명시 방향입니다. 27개 방향에는 일차 공급자 참조가 있으며, target 6의 정방향 `4He(gamma,d)d`에는 직접 수치 행이 아직 없습니다. R2의 새 공급자 variant 26개와 새 정수 column 24개는 이미 승인된 C9의 범위와 일치합니다. R1의 species 9개와 event 참조 24개를 재사용하며 R1 event 재컴파일 수는 0입니다. R1의 102개 source variant, 125개 projection, 92개 material/electronic identity는 그대로 보존됩니다.

공급자 참조 수에는 배타적 채널, factorized 자료, inclusive 자료, 빔 및 검출 응답으로 평균된 측정, 출처의 모델 결과가 포함됩니다. 따라서 27개의 참조를 27개의 물리적 rate 승인으로 읽을 수 없도록 보고서·admission·DAG가 구분합니다. target 6의 자료 접근 실패도 측정값 부재나 물리적 불가능성 증명으로 확대하지 않습니다.

기존 primary 13/13 PASS와 independent의 원래 통과한 9개 그룹 및 수정된 public metadata 그룹을 재사용합니다. 독립 검토의 두 checker 실패는 보존되었으며, 최종 10/10은 합성된 범위별 수용 기록입니다. 전체 그룹을 새로 실행했다고 기술하지 않습니다.

## 발견 사항과 수정 확인

`R2_RELEASE_01`은 게시 전 수정이 필요했던 출처 경로 문제였습니다. R2로 복사한 DAG의 R1 상대 경로가 R2 내부로 해석되어, R1의 125-column 근거가 R2의 24-column 파일을 가리킬 수 있었습니다. 기존 R1의 evidence, budget, publication, local snapshot 및 다음 작업 경로를 `../provider_registry_20261025/`로 명시한 수정을 수용합니다. 기록된 22개 경로 필드가 현재 값과 일치하고, 해당 로컬 파일과 디렉터리가 존재합니다. 원래 중앙 저장소의 `source_file` 필드는 그대로 유지하면서 중앙 저장소 내부 경로라는 해석을 명시했습니다. 새 R2의 근거 경로는 바꾸지 않았습니다.

추가로 확인한 네 가지 표기 문제도 닫았습니다. 보고서의 pT E1 값은 원래 표기 `0.95(5)` eV b로 수정되었고, historical compiler는 올바른 sibling 경로를 사용합니다. WORKFLOW의 두 번째 이론 문서는 `theory/`를 명시하며, R1 인계서·보고서의 continuation prefix는 현재 R2의 `SCIENTIFIC_ADMISSION.json`을 명시적으로 가리킵니다. 숫자 자료와 이론·구현에는 변경이 없습니다. 각 수정의 전후 값과 SHA는 `RELEASE_METADATA_CORRECTION.json`에 보존되어 있습니다.

## 변경 범위와 승인 경계

root AGENTS는 게시된 R1의 전체 바이트를 정확한 suffix로 보존하고 R2 작업 지침만 앞에 추가합니다. 사용자 지정 고정 handoff는 commit `34dd7d1d018abff8a0a4ebd1d3f3579ac46d2fad`의 바이트와 같습니다. R2 builder, 계약, 두 이론 문서, 11개 registry JSON, C9 및 primary checker의 SHA도 수용 당시와 일치합니다. 기존 R1 파일의 변경은 DAG, delivery/workflow 및 continuation 메타데이터에 한정됩니다.

DAG의 전체 target 부모는 partial입니다. source identity 및 새 정수 column 자식의 scoped completion과 27/28 source binding 자식의 partial 상태가 충돌하지 않습니다. 관측한 최신 중앙 HEAD는 `a5db4bac9dafadae29685bbea3cec7f43ab990b2`이며 88개 노드 중 기존 WU 14개가 의미상 유지되었다는 근거를 기록합니다. 중앙 ACK 또는 타 소유자 계약 변경을 가정하지 않습니다.

실제 rate/Q/consumer 승인은 false이며 HH_R10은 OFF, production은 NOT_ISSUED, L4는 false, 전체 물리적 completion은 null입니다. 이전 합성 249-check를 물리적 승인으로 확대하지 않습니다. target 6 수치 자료, He4 response/consumer 대응, He3 factorized grid의 소비자 결합, Li7의 배타적 가지, HD·LiH의 남은 반응, isotope/state/domain, mass/Q convention 및 covariance, MT102_B1 등의 열린 의존성도 남겨 둡니다.

## 게시와 백업 상태

R1 source commit `18a6804d7cbe4879701e83631f7e908bbb84cef1`의 3,073,149-byte ZIP 및 Dropbox·Drive 실제 다운로드 일치 기록은 완료된 선행 근거입니다. R1 ZIP SHA256은 `c1ced1cdeb7382064e64d11abd38d52466802a699edf99bd78aa355c0ce17863`입니다. package-time의 pending 표기는 역사적 관측으로 보존하고 final ACK가 이를 대체함을 명확히 했습니다.

R2 게시·새 이중 백업은 이 검토 시점에 pending입니다. R10/C10도 source-scoped 완료와 delivery pending을 구분하므로 아직 없는 R2 receipt를 완료 근거로 주장하지 않습니다. 사용자의 명시적 게시·백업·자동 실행 승인은 유지됩니다. 다음 작업은 현재 source parent를 expected SHA로 사용한 non-force 게시, 실제 게시 tree의 source ZIP 생성, 두 저장소의 다운로드 바이트 확인, 별도 metadata child 기록입니다.

`delivery/package_source.py`는 정적으로 읽었습니다. 정확한 commit/tree의 허용 경로만 읽고, 기존 산출물을 덮어쓰지 않으며, 패키지 바이트/CRC 확인과 별도 ACK 기록을 구분합니다. 공개 source packet에서 제외한 비-CC 전문 자료를 추가하는 동작이나 과학 계산 호출은 없습니다. 이번 검토는 packager를 실행하지 않았습니다.

기존 PHYS91 primary/reference/Wolfram 잔여 0과 전역 CPU·금액 잔액 null을 유지합니다. 이전에 기록한 새 light child 8개의 CPU 0.737753초와 wall 0.861847초는 해당 child들의 측정 합계이며, 미측정 자료 검색·준비·검토 비용을 0으로 만들거나 전역 합계로 주장하지 않습니다.

## 검토 방식과 파일 고정

이번 단계에서 수행한 작업은 문서·코드 정적 읽기, 기존 diff 및 receipt 확인, SHA256·바이트 동일성·수정 경로의 존재 확인입니다. 계산, compiler/build 실행, numerical test replay 및 외부 게시 작업은 0입니다. 검토한 메타데이터의 실제 SHA256 목록은 같은 이름의 JSON 파일 `reviewed_metadata_sha256`에 있습니다. 이번 검토가 쓴 파일은 이 Markdown과 동명 JSON 두 개뿐입니다.
