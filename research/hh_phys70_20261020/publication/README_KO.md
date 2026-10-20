# PHYS70 게시·배포 영수증

과학 소스 commit은 `e73048e1399263eac3d40ffd3e700807bbc7c72e`(S)이고,
실제 부모는 PR119 `efd1520dfc0643220f729307583ff0bc04b059e9`다.
S의 원격 tree와 로컬 검증 tree가 일치한 사실은 `SCIENCE_REMOTE.json`에 있다.

이 디렉터리를 추가한 별도 metadata commit(M)은 S의 직접 자식이다.
M은 코드·proof·실행 payload를 변경하지 않고 게시·백업 영수증 및
NEXT_DAG/LOOP_RECORD의 transport 상태만 확정한다. 자신의 commit SHA를
자기 payload에 넣는 순환 참조를 만들지 않는다. 실제 M과 원격 readback은
외부 `PHYS70_DELIVERY_20261020.json`, `PHYS70_METADATA_REMOTE_20261020.json`에 기록한다.

두 고정 ZIP은 S의 source/evidence를 담고 있으며, 나중의 M을 담는다고
주장하지 않는다. M의 파일·증분 patch·Git bundle은 별도 metadata addendum에
전달한다. 과거 전체 archive는 source/evidence ZIP에 보존했고 NCP 축소판은
실행과 무관한 보관 ZIP 4개 및 구 PHYS69 standalone binary만 제외했다.
양쪽 source crate, source fingerprint, 원본 입력과 완료 pilot은 유지했다.

각 capsule의 CRC·SHA256·크기·mode·member closure는 검증됐다. NCP 축소본의
깨끗한 복원에서 완료 pilot의 읽기 전용 resume를 확인했고 전체 564개 파일의
내용·크기·mode·mtime가 같았다. 이 전달 검증은 새 native 적분 0회다.

`BACKUP_ACK.json`은 실제 provider ACK와 제공된 크기·해시 대조를 기록한다.
로컬 ZIP 검증, 업로드 ACK, 원격에서의 전체 재다운로드는 서로 다른 사실이며
원격 전체 재다운로드 검증을 수행했다고 주장하지 않는다. 서명 URL과 전송
token은 공개 영수증에 넣지 않는다. HH_R10=OFF다.
