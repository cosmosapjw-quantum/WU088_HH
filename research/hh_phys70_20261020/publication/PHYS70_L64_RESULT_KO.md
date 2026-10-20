# PHYS70 최적화 L64 — 실행 결과

## 상태

PHYS71의 all-angular/all-radial D3 완료 결과를 그대로 재사용했다. D3 캠페인을 다시 실행하지 않았다. checkout에 상속 PHYS68 profile archive가 빠져 있어 첫 portable verifier 시도는 read-only 상태로 불완전 종료됐다. PR121에서 고정한 PHYS71 Dropbox source capsule(30,636,014 B, SHA `1a17cd48...`)을 `/tmp`에 독립 다운로드해 SHA를 확인하고, 저장된 76개 D3 panel을 새 계산·파일 쓰기 없이 verifier PASS로 검증했다. 먼저 호스트·로컬 run 경로·Dropbox/Drive에서 동일 PHYS70 L64 완료 실행을 찾지 못했고, 현재 승인 NCP `s1a0e5abed09`에서 고정 요청을 1회 실행했다.

`runs/phys70_l64_block_simd/`에 raw request, 동결 NPZ, 512-bit seed 입력/balls, build·seed·native stdout/stderr 및 종료/벽시간 영수증, 결과와 `CHECKSUMS.json`을 보존했다. 실행 종료 코드들은 모두 0이며 native 적분은 1회다. read-only `--resume`는 `REUSED_COMPLETED`, 새 적분 0, 파일 쓰기 0을 반환했다. payload 22개의 SHA-256을 재검산했고, `RESULT.json`과 native stdout이 byte-identical임을 확인했다. `tests/test_phys70_ncp.py -v`의 22개 계약/runner 테스트도 통과했다.

## 고정 요청과 실행 환경

요청은 L64, 128 angular nodes, `rtol=1e-10`, `atol=1e-12`, initial/max step `0.01/0.25`, 최대 50,000 attempts, `block_simd`이며 request SHA-256은 `4894196e50b9da91b31465b5723c8ba7c770b0a8ecbc8eeeb5f94053b68b2d03`이다. frozen input SHA는 `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`, 생성 seed SHA는 `38216fd59acbc66146f4abc27fddb3a076a745b81aac8164b0772ebae96d7f65`이다. 고정 VigilODE source `a21d573980f66fe02891bd216153443b5352f921`, Rust/Cargo 1.94.1, locked build를 사용했다. toolchain 및 `requirements.txt` venv는 `/tmp`에 격리해 원래 환경을 변경하지 않았다.

빌드와 native child 각각 900초, 주소 공간 4 GiB, `nice +10`, build job 1개, solver/BLAS/OpenMP/Rayon 1 thread였다. preflight/seed/build/native exit code는 각각 0이다. seed 생성은 2.222초, locked build 328.065초, native integration 0.217초였다. peak RSS는 계측하지 않아 4 GiB는 측정치가 아니라 설정된 상한이다. 동시간대 unrelated nice-0 build 하나가 관측됐지만 이 실행은 제한값과 우선순위를 유지했다.

## 유한 L64 결과

native 결과 중심은 `D2 = (7.017743632402883 + 3.200163222655957 i) × 10^-48 a0^-1`이다. 825 accepted / 0 rejected steps, 6,600 structured shifted solves와 6,600 JVP 호출을 기록했다. 관측된 최대 shifted backward residual은 `1.9051004806626438e-16`, 최소 shifted denominator는 `0.9995149855101603`, `|F(B)-1|` 최대는 `5.4352251588341005e-9`이다.

이는 PHYS70 runner의 상태 `COMPLETED_BINARY64_REFERENCE_NOT_CERTIFICATE`에 해당하는 유한 L64 binary64 진단이다. 이를 새 all-angular 계수, 전 ODE·Coulomb·quadrature·roundoff 상계 또는 전체 응답 인증으로 해석하지 않는다. wrapper는 identity, endpoint layout/finiteness, 고정 관계식을 검사했으며 total error 인증은 `false`다. 기존 PHYS69 all-angular D2 certificate와 PHYS71 D3 certificate는 별도 범위로 계속 재사용한다.

PHYS70의 결합 DAG 노드는 `PARTIAL_D3_COMPLETE_HIGHER_REMAINDER_OPEN` 그대로다. 4차 이상 Born 나머지/전체 비선형 응답, original source-driven `xi`, regular origin/incoming adjoint, `sigma(E)`, Maxwellian `k_HH(T)`는 계속 OPEN이다. `HH_R10=OFF`를 유지한다. 다음 단계는 이 addendum·실행 capsule·Git bundle의 additive 게시와 각각의 백업 복원 검증뿐이다.
