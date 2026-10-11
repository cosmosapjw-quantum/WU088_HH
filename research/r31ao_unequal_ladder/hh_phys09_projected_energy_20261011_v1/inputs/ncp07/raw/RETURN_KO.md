# PHYS07 NCP 반환

T01–T06 구현, 허용된 최초 full/first-half source 실행과 비생성자 독립 검토를 완료했다. Stored COMMON과 point-seed reference 입력을 구별하여 공개 PreBE·reduced residual의 같은 호출에서 C² domain, whole-X/Theta export, signed Hessian 및 geometry를 보존했다. First-half는 같은 COMMON에서 시작한다.

실제 합계는 PreBE 2, direct residual 4, FT03 4, HH jet 4, provider channel 396, 저장 export 조건부 uniform 산술 2이다. 두 target exit 0, 동일 binary SHA256 8dfd6eaf24c827cdd199fc7e07b4e44335d9876413503022c4352ccfc8549416. Source 실패·수정·재실행은 없었다. 별도 artifact checker의 JSON field 가정 실패와 수정은 ARTIFACT_VERIFICATION에 보존했다.

조건부 uniform q는 full 0.00011736830563768177, first-half 0.000058538714993538125이며 strict image margins 양수다. 각 stage 136 scalar leaves는 reference bit identity, 314 intervals는 reference 포함이다. 서로 다른 입력·계수의 semantic equivalence와 구별한다.

독립 APPROVE는 source producer·고정계수 real-source C²·조건부 산술 범위다. 방향미분 support는 node32 subnormal tail 때문에 OPEN이며 clipping하지 않았다. Closed-vs-AD overlap은 동등성·포함 증명이 아니다. Actual native root/U/V/W/I, finite gas-energy 부호, carry·paired defect·time/continuum remainder, physical model adequacy, full49·production은 OPEN이다. Reference를 actual-native field로 옮기지 않았다. Finite birth M=exact(fl(d*S_*)), B_d=M/exact(d)를 유지했다.

Compiler/flags/CPU/precision과 실제 자원은 evidence 참조. Target memory·swap·CPU·wall/output 제한 적용. Build output cap은 command streams 및 per-file 크기이며 compiler artifact 전체 크기를 보증하지 않는다. 이전 미계측 binary hash는 null이다. 기존 보호 파일 183개는 byte identity 유지.

Core의 미래 commit/archive identity는 sibling delivery START·receipt·index에 기록하여 self-reference를 피한다. Upload ACK·metadata와 실제 cloud restore는 구별한다. 다음 작업은 NEXT_HANDOFF_KO.md에 있으며 새 source budget 또는 native 권한이 없다.
