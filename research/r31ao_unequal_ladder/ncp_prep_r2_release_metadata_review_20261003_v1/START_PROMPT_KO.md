# NCP prep R2: 원 archive metadata 보존과 실제 도구집합 closure

NEXT_ACTION=NCP_PREP_R2_RELEASE_METADATA_FIDELITY_AND_TOOLCHAIN_CLOSURE
PROJECT=cosmosapjw-quantum/WU088_HH
BRANCH=research/r31ao-unequal-order-ladder-20260930
OBSERVED_R1_HEAD=c50dd46a67c2da209b6788ccebdbd8bb01e1ea05

## 즉시 회수할 원자료

기존 verified local cache를 우선 사용하고, 없으면 기존 인증된 Drive/Dropbox 중 한 곳에서만 bytes를 받는다. 사용자 재업로드를 요구하지 않는다.

상세 prompt:
- name: WU088_HH_NCP_PREP_R2_RELEASE_METADATA_PROMPT_KO_20261003.md
- bytes: 10949
- SHA256: e3a9fc6652e9f3cf97d7521e61ad3dabffe6e5ed8ea234dad5c723a17f75984e
- Drive ID: 1ykkxIjC0un25mlvvSgVnDJ7iuyJwnGzz
- Dropbox ID: id:BSpOijBcT10AAAAAADxxaA

실행 가능한 후보/12개검사/원MPFRarchive/선택R1로그/검토문:
- name: WU088_HH_NCP_PREP_R2_RELEASE_METADATA_REVIEW_20261003_v1.zip
- bytes: 1945164
- SHA256: e44eff52486e04ae147933462e52b1c6479e8137aa85b376deb4a88653941396
- Drive ID: 1oASJTFFH4Oe7CnH1Ej2wYET3OPnGZjNF
- Dropbox ID: id:BSpOijBcT10AAAAAADxxZw
- payloads: 50, local SHA/CRC verified

독립 report:
- name: WU088_HH_NCP_PREP_R2_REVIEW_KO_20261003.md
- bytes: 7065
- SHA256: 8539d2fa29fdb68d73927229c03bd014865807d514d5c8706612c23603dfe5b1
- Drive ID: 1bZQvhwZKX244DkEVlHduroPocGXcQJ-z
- Dropbox ID: id:BSpOijBcT10AAAAAADxxaQ

이 Git 파일은 시작 인덱스다. 전체 helper/12개시험/원로그를 Git에 개별게시한 것은 아니며 위 ZIP이 재현 기준이다.

## 검토 결과

R1의 Texinfo7.1 clean-PATH 검증, 실제32GiB/CPU quota4의 cgroup 관측, GMP configure/build/check/install 성공을 유지한다. 단 R1 transient cgroup은 종료돼 새 실행에서 재관측해야 한다. UID0/capabilities0는 비rootUID 증명이 아니다.

MPFR fatal error는 automake-1.17 부재다. 상류 원인은 pinned safe_extract가 tar mtime을 보존하지 않는 것이다. 원 tar의 aclocal.m4는 Makefile.in보다1초 오래됐지만, R1 추출본에서는2,000,027ns 더 새로웠다. 해당두파일의content는원tar와같다. 로그에autoconf와automake-1.17호출이기록됐고configure는실제재생성되어원tar와다른bytes가됐다.

동일MPFRarchive를원extractor와mtime보존후보로분리추출하고실제의존성부분의격리된GNU make -rR -q만검사했다. 원경로는Makefile.in/configure둘다exit1,후보는둘다exit0이며filebytes는모두같다. 패키지configure/make/backend/HH는실행하지않았다.

후보release_extract.py는새tree에서만원tarmtime을복원한다. 임의touch로skip하는것이아니다. 원path/hash/size/중복/link거절을유지하고미지원mtime은출력전거절한다. 새12개고유시험PASS(5개관측RED→GREEN,7개후속회귀),실패0,skip0이다. isolated2x2dependencyquery를4개추가시험으로세지않는다. NCP전체backend가고쳐졌다는claim은false다.

FLINT고정source는bootstrap.sh의autoreconf를실제로필요로한다. 따라서metadata수정으로Autotools전체가불필요해지는것은아니다. 실제cleanPATH에서필수생성기도구와data경로를함께검증하고필요하면정품Automake1.17/호환Autoconf를workspace-local로제공한다. old1.16.5를1.17로이름만바꾸거나MAKEINFO=true/maintainer-rule삭제는금지한다.

## 다음실행계약

위상세prompt와REPORT를읽고원source/lock을바꾸지않은새명시적orchestration에추출후보를연결한다. 변경된orchestration/extractoridentity를숨기지않는다. R1실패tree,원PREPARED/registry/B22를보존한다.

cheapmetadata/toolchaingate가모두통과한뒤새prefix에서원GMP6.3.0/MPFR4.2.2/FLINT3.4.0,pins/flags/jobs2와R1budget으로최대1회비과학backendcontinuation을수행한다. 이후실제로성공한경우에만workercompile/link/ABI와dispatch없는BINDING_PROPOSAL을작성한다. 이번에원run/worker/consume를호출하지않으며science_dispatch=0,scope_consumed=false다.

종료는READY_FOR_EXACT_SCIENCE_AUTHORIZATION또는정확한원인을갖는PREPARATION_BLOCKED다. 관리자변경필요성을다시가정하지말고이미있는위임과workspace-local도구를쓴다. 과학실행승인은별도다.

accepted20/289,missing269unbounded,epsilon_C/R=null,B22OPEN,scientific/production=false를유지한다. DB변경과Bianchi/rei_bianchi/다른원자repo변경은없다.

같은branch에additive/nonforce게시하고기존Driveparent1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM와Dropbox ns:183516487//BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/에create-only백업한다. 양쪽현재업로드ACK+이름/크기는확인됐으며새outputRESTORE_VERIFIED=false다.
