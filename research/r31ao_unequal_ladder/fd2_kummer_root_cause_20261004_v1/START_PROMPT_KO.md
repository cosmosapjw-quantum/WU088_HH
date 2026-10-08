# FD2: 최초 nonfinite 원인 해소와 검증된 scalar 후보

상태: INITIAL_NONFINITE_CAUSE_RESOLVED__BOUNDED_1F1_CANDIDATE_VERIFIED__CELL_CONVERGENCE_PENDING.

원 FD1 관측의 두 번째 signed107 항은 k=1이다. 실제 source-bound scalar 추적으로 첫 실패를 moment(k=1,r=0)의 M(a,b,z) 호출에 국한했다. a=r-k/2,b=r+3/2,z=-s/(2sigma)이며, 두 query의 전체 z 사각형은 0을 포함한다. 고정 FLINT3.4.0 자동 선택은 점근 표현을 택하며 k=1일 때 그 표현의 z^(a-b)=z^-2는 이 box에서 유한 외포를 줄 수 없다. M 자체는 b>=3/2에서 entire이다. 원 scalar 자동/점근 경로는 nonfinite, 직접1F1 경로는 finite였다. cached/reference의 전체 field를 재실행하지 않았고 적분은 0회다. cache 버그, 수학적 발산, 모든 queue 실패의 단일원인으로 일반화하지 않는다.

## 증명된 후보

T_0=1,
T_(n+1)=T_n*z*(2n+2r-k)/[(2n+2r+3)(n+1)].

0<=k<=8,0<=r<=2,|z|<=64,n>=256이면 |T_(n+1)|<=q|T_n|, q=6656/26471<1.
따라서 M과 n=0..255 부분합의 차이는 (26471/19815)|T_256| 이하이다. Acb128 outward partial sum과 Mag tail bound를 사용한다. finite whole-box L1 bound<=64와 zero-containing odd-k에서만 이 경로를 선택하고, 나머지는 원 acb_hypgeom_m 호출을 유지한다. midpoint, box 축소, 정밀도 저하, tolerance 완화가 없다. finite enclosure가 좁은 enclosure를 뜻하지는 않는다.

현재 33개 고유 검사 통과: 실제 scalar 회귀6, 경계/항등식/직접급수 대조15, 원 radial moment6, evidence6. 최초6개 및 경계2개에서 실패 후 통과를 기록했다. 나머지는 후속 회귀이다. 독립 과학 심사는 미수행이다. DB는 원91개 테이블 보존+6개=97개이며 integrity/FK/로컬SQL복원 검증을 마쳤다. 전체 근거와 원 실행로그는 아래 ZIP이 기준이다. Git의 test_regression.cpp만 실행하면 6개 검사이며 전체33개가 아니다.

## Cloud-first 입력

사용자에게 파일 재업로드를 요구하지 않는다. 검증된 cache를 먼저 쓰고, 없으면 접근 가능한 Drive/Dropbox 한곳에서만 다음 ZIP을 회수한다.

- name: WU088_HH_FD2_ROOT_CAUSE_DELIVERY_20261004_v1.zip
- bytes: 19979957
- SHA256: 21289a6cc78b1c172815c97b4053eb9990a26d048b0410ac1dee6b22bbcb66a1
- Drive ID: 1OiAs1b0G-ot7PJ-bdCwYmevN5xZGTmx2
- Dropbox ID: id:BSpOijBcT10AAAAAADx4pA
- Drive parent: 1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM
- Dropbox directory: /BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/

254개 payload와 CRC를 검증했다. 양 provider의 완료 ACK/name/size를 확인했지만 새 출력의 remote RESTORE_VERIFIED는 false다. 전체 proof, source lineage, candidate tree, 원 입력,33개 검사,DB/SQL은 ZIP에 있다.

## 다음 NCP 작업

NEXT_ACTION=NCP_FD2_CANDIDATE_BUILD_AND_EXACT_FULL_FIELD_PROPOSAL

1. 최신 remote successor를 읽고 원 FD1/6셀의 소비 registry를 보존한다. 과거 SHA로 reset하지 않는다.
2. ZIP SHA/size와 verify_delivery.py를 확인한 뒤 HANDOFF_KO.md,THEORY_KO.md,RESULT.json을 읽는다.
3. 기존 검증된 R2 FLINT/GMP/MPFR prefix를 재사용한다. backend를 재빌드하지 않는다.
4. run_tests.py --prefix <verified-prefix> --output <new-output>로 해당 host에서33개 scalar/read-only 검사를 한 번 확인한다. 기존18/40개 suite를 관례적으로 반복하지 않는다.
5. candidate tree의 두 줄 변경(include와 M 호출)을 새 sidecar에 명시적으로 결속한다. 원 numeric source/SOURCE_LOCK/worker/FD1 binary를 덮어쓰지 않는다. 새 source/build/linkage와 fresh cgroup 관측을 기록한다.
6. 새 FD2_CANDIDATE_PROPOSAL을 작성한다. 후보 query는 Q272_cached,Q272_reference,Q000_cached,Q000_reference 각1회,최대4 field callback,적분0,worker1,128bit,원 box/margin/order/field/계수순서다. query10초/1024MiB,unit60초,기존32GiB 및 CPU4분량의 정책을 유지한다.
7. 이번 인계는 준비까지만 허용한다. 실제 후보 full field는 별도 exact authorization 이후이며, 원 FD1 scope를 재사용하지 않는다. READY_FOR_EXACT_FD2_CANDIDATE_AUTHORIZATION 또는 정확한 blocker를 반환한다.

후속 승인 실행에서 finite output과107항 완료를 검증하되 width를 그대로 보존한다. 새 candidate cached/reference끼리 enclosure 정합성을 비교한다. 원 nonfinite FD1과 overlap 검사를 강제하지 않는다. 추가 helper 실패는 fresh 원인으로 보고하고 자동 추가 query/box/precision/queue 변경을 하지 않는다. 두 셀 적분은 그 다음 별도 scope다.

24/289,missing265 unbounded,epsilon_C/R=null,B22 OPEN_UNDETERMINED,scientific/production=false는 보존한다. Bianchi/rei_bianchi 및 다른 원자 repo는 변경하지 않는다. 같은 branch additive/nonforce 게시와 기존 Drive/Dropbox create-only 백업을 수행하고 ACK와 실제 restore를 구분한다.

원 source comparator: FLINT commit2b0788802abf62ec29d8e4a8f917993606e517e0/src/acb_hypgeom/m.c. 정의: NIST DLMF13.2.2. 새 꼬리상계는 위 명시된 전제에서 직접 유도한 결과다.
