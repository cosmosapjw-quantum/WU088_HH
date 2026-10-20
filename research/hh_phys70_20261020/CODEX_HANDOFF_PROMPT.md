# NCP / Codex 실행 인계 — PHYS70 최적화 runner

```text
WU088_HH의 완성된 PHYS70 최적화 runner를 실제 호스트에서 이어서 실행하라.
Repository: https://github.com/cosmosapjw-quantum/WU088_HH
Branch: research/hh-phys70-structured-optimization-20261020
Actual parent: efd1520dfc0643220f729307583ff0bc04b059e9 (PR119).
최신 source commit, metadata HEAD, PR 및 백업 ZIP SHA는 외부
PHYS70_DELIVERY_20261020.json과 research/hh_phys70_20261020/publication/의
실제 ACK에서 읽어라. 예정된 commit을 실제 HEAD라고 쓰지 마라.

먼저 최신 GitHub/관련 백업/실제 호스트 process·job·result 디렉터리를 확인하라.
같은 request/source/seed/engine/binary의 완료본은 읽기 검증하고 재사용한다.
진행 중이면 그 작업을 관찰한다. 접근하지 못한 호스트 상태는 UNKNOWN이다.
기존 완료 PHYS64 NCP20, PHYS66 pilot/smoke, PHYS67 인증, PHYS68 L28,
PHYS69 j29..36/예전 native2, PHYS70 완료 성능 적분31개는 반복하지 마라.

먼저 PHYS70 REPORT_KO.md, theory/PROOF.md, EXECUTION_LEDGER.json,
NEXT_DAG.json, ncp_delivery/README_KO.md, publication/FINAL_DELIVERY.json을 읽어라.
Rust 블록 직접해법, ordered SIMD, 독립 Rayon batch와 실패/재사용 guard는 완성됐다.
NCP 역할은 컴파일·작은 환경 수정·실제 실행·근거 반환이다. solver 설계가 아니다.

고정 물리: atomic B27,k7/10,E49/200Hartree, shift0.7,
h=-Delta/2-1/r-(1+1/d)exp(-2d),d=|x-0.7zhat|.
H+=G+iF_C, Z=+u'u^-1, radial V=2(1+1/d)exp(-2d).
eta=Fy,xi=Fy-phi,eta_C=-10/7을 구분한다. HH_R10=OFF.
원본 NPZ SHA f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d.
VigilODE a21d573980f66fe02891bd216153443b5352f921,
wide1.7.1,rayon1.12.0,num-complex0.4.6,gauss-quad0.3.2의 Cargo.lock을 유지한다.
PHYS63 질적 all-angular LAP/Poisson/DtN과 PHYS69 all-angular D2는 완료 근거를 재사용한다.

원격에서 새 완료본이 없을 때의 구체적 다음 요청:
research/hh_phys70_20261020/ncp_delivery/REQUEST_L64.json
L64,m0,target21/20,T65,nodes128,rtol1e-10,atol1e-12,max_step0.25,block_simd.
이 요청은 현재 대화에서 PREFLIGHT_ONLY였다. 원격 NCP 제출은0이었다.
완료된 L28 pilot은 새로 실행하지 마라.

1. 이미 있는 L64 seed를 source/L/정규화와 함께 확인해 우선 사용한다.
   없을 때만 기존512-bit initializer의 --make-seed를 사용한다.
2. Rust1.94.1, cargo build --locked --release --jobs1로 현지 컴파일한다.
   제공된 측정 binary는 GLIBC2.39 요구가 있으므로 구형 host에서는 source를 빌드한다.
   현재 sandbox binary SHA는303efb12fb6c6169b97440a1224d30730e5194a6230c02d469a13a25b9270c13.
3. 서로 다른 preflight/실행 output 경로를 사용하고 timeout900s, memory4GiB부터 실행한다.
   기존 출력은 덮지 않는다. 실패 시 원본 로그와 부분 출력을 남기고 실제 원인만 수정한다.
4. RESULT, REQUEST, SEED_INPUT, source, EXECUTION, 각 command stdout/stderr/receipt,
   CHECKSUMS와 실제 compiler/flags/CPU/HEAD/binary SHA를 원문 그대로 반환한다.
5. native success, stored point error, 통합 오차 인증, 성능, Git 게시, 백업, DAG는 분리한다.
   L28 인증서로 L64 값을 인증하지 마라. 새 L64 검증본이 있으면 동일 대상을 대조한다.
6. additive branch/draft PR와 create-only 백업을 게시하고 실제 ACK를 기록한다. main은 merge하지 않는다.

source-driven xi, 원점/incoming adjoint, sigma(E), Maxwellian k_HH(T),
all-angular D3/higher remainder 및 남은 수치 인증은 각 OPEN 의무로 유지한다.
```

## 실행 명령

저장소 또는 준비된 NCP source capsule의 루트에서, 앞의 중복 실행 확인을
마친 뒤 사용한다. 아래 첫 명령은 seed·compiler를 호출하지 않는 사전 점검이다.

```bash
python3 scripts/phys70_ncp.py \
  --request research/hh_phys70_20261020/ncp_delivery/REQUEST_L64.json \
  --out runs/phys70_l64_preflight --make-seed
```

기존 seed를 사용하는 실제 요청:

```bash
python3 scripts/phys70_ncp.py \
  --request research/hh_phys70_20261020/ncp_delivery/REQUEST_L64.json \
  --seed /absolute/path/to/L64_SEED_INPUT.txt \
  --out runs/phys70_l64_block_simd \
  --run --timeout 900 --build-timeout 900 --memory-gib 4
```

seed가 없으면 위 `--seed ...`를 `--make-seed`로 교체한다. 생성기의 의존성은
`research/hh_phys68_20261019/ncp_delivery/requirements.txt`에 고정돼 있다.
이미 빌드한 적합한 binary를 쓰려면 `--binary /absolute/path/to/binary`를
추가한다. 완료본의 재사용은 동일 요청·binary·출력 경로에 `--resume`를
사용하며 새 적분과 파일 쓰기를 수행하지 않는다.

컴파일만 먼저 할 경우:

```bash
cargo build --locked --release --jobs 1 \
  --manifest-path native/phys70_optimized/Cargo.toml \
  --bin wu088-hh-phys70-optimized
```

`native/phys70_optimized`와 `native/phys69_vigilode`는 path dependency 관계이므로
둘을 함께 유지한다. 완료한 기존 시험의 동일 identity에서는 시험을 반복하지
않고, 환경·코드 수정으로 영향받은 의무만 표적으로 확인한다.
