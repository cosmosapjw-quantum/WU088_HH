# R2 전달 메타데이터 독립 검토

**판정: `PASS_SCOPED_DELIVERY_METADATA`. 남은 차단 사항은 없습니다.** 검토 시점은 source 게시·이중 백업 완료 이후, delivery metadata child 게시 이전입니다.

Source commit `71019bb469c92d1ea665155ed98c472b362d6706`, tree `d91c82fece682b12d34a01db8ae12b4dc55f4c66`, 부모 `18a6804d7cbe4879701e83631f7e908bbb84cef1`이 실제 Git 메타데이터 및 게시 영수증과 일치합니다. PR150은 draft이며 expected-SHA non-force 갱신이 기록되어 있습니다. main merge나 owner branch 변경은 없습니다.

Source ZIP은 7,084,911 bytes, Git 파일 380개와 manifest를 합한 381개 멤버입니다. SHA256은 `43845ea085797a6d628b722d58197a64a0af6f0a34a708f3dc981a5274faa906`입니다. Dropbox `id:BSpOijBcT10AAAAAAEAfFg`와 Drive `1C4NE14swNXTL4GXb-ol8HE8cm57sHaIe`의 완료 ACK 및 실제 HTTP 200 다운로드 영수증이 같은 크기·SHA를 기록합니다. Dropbox content hash도 일치합니다. 이번 검토는 다운로드나 패키지 검사를 반복하지 않았습니다.

검토 중 두 가지 표현을 수정했습니다. `173`은 전체 tree의 파일 수가 아니라 부모에서 추가·변경한 entry 수이며, operational history와 publication receipt가 이를 명시합니다. 보고서 9절과 인계서의 이전 pending 문구는 source snapshot 작성 당시의 관측으로 표시하고 현재 완료 절·영수증을 가리킵니다. 전달 JSON의 영수증 경로 기준도 같은 delivery 디렉터리로 명확히 했습니다.

후속 metadata commit은 이 파일을 담는 실제 containing Git commit으로 해석하며, 백업된 source commit과 구별합니다. source ZIP이 생성 이후의 자체 백업 영수증까지 포함한다고 주장하지 않습니다. 다음 게시의 expected parent는 `71019bb469c92d1ea665155ed98c472b362d6706`, force는 false입니다. 이 검토는 아직 수행하지 않은 최종 metadata ref 갱신을 완료했다고 주장하지 않습니다.

Git diff는 전달·인계 메타데이터 8개 파일에 한정됩니다. 과학 core, AGENTS, 고정 handoff에는 변경이 없습니다. 19개 ID, 28개 방향 중 27개의 공급자 참조, target 6 정방향의 수치 입력 공백, 새 source variant 26개와 새 column 24개를 유지합니다. rate/Q/consumer 미승인, 부모 DAG의 partial 상태, 중앙 ACK 미가정, 기존 예산도 유지합니다. R10/C10의 완료는 이번 scoped source 전달에 대한 기록입니다.

최신 `PRE_METADATA_PUBLICATION.json`은 source HEAD, AGENTS, base·owner·central HEAD 및 병렬 작업을 확인한 근거입니다. 사용자에게서 받은 자동 게시·백업 권한을 그대로 적용해 metadata child를 게시할 수 있습니다. 이번 검토에서는 정적 읽기와 Git 메타데이터 확인만 수행했고 계산·검사 재실행·packager·다운로드·외부 쓰기는 모두 0입니다. 실제 검토 파일의 SHA256 목록은 동명 JSON에 기록했습니다.
