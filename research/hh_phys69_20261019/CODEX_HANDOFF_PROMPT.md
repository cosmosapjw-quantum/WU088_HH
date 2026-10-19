# WU088_HH PHYS69 — NCP 실행·반환 계약

ROLE=BOUNDED_NCP_EXECUTION_AND_RETURN
REPO=https://github.com/cosmosapjw-quantum/WU088_HH
BRANCH=research/hh-phys69-angular-tail-vigilode-20261019
ACTUAL_PARENT_PR118=2a79d961388e4fc71cbc0938f012b08af7ecf14e
HH_R10=OFF

먼저 최신 원격 PR/HEAD와 `publication/FINAL_DELIVERY.json`, REPORT_KO.md,
NEXT_DAG.json, theory/PROOF.md, all_angular/CERTIFICATE.json을 읽는다.
science commit, 후속 metadata HEAD, 실행 certificate, cloud ACK를 구분한다.
이 branch는 실제 PR118 descendant다. 과거 PHYS66 snapshot2d08f8da를
원격 descendant로 추정하지 않는다. PHYS66 최종993317b1 ZIP은 여전히
BLOCKED_ARTIFACT_ACCESS_EXACT_FINAL_VERSION이며 회수된 이전84c29de7과 다르다.

## 이미 완료된 결과를 재사용한다

PHYS64 NCP20, PHYS66 pilot/smoke, PHYS67 certificates, PHYS68 L28의
76panel 및 기존 Rust2432/4864step, PHYS69 j29..36의76panel과
새 VigilODE L28 두 실행은 완료됐다. 반복하지 않는다.

PHYS69는 원래 (ell,p,m)=(21,20,0)의 실제 all-angular/all-radial
DtN lambda^2 계수 D2=Z''(0)/2를 원래1e-62 목표로 인증했다.
표시 중심은 (7.01774363281637372857673+3.20016322230539545153550i)e-48,
표시 반올림 포함 절대오차<=1.279825889920e-64 a0^-1이다.
전체 lambda1 응답·원래 xi·반응률은 이 결과의 scope에 추가하지 않는다.

원본 새 band78JSON은 source/evidence 배포 ZIP 안의
`PHYS69_BAND_PAYLOADS_20261019.zip`에 있다.
SHA256=538e16bb74ff5305584fbe2d42491dda55fdffdde536f9276e038bc48da561f0.
다음은 완료본 복원·읽기 검증이며 새 적분을 실행하지 않는다.

```bash
python3 scripts/phys69_restore_evidence.py \
  --archive /absolute/path/to/PHYS69_BAND_PAYLOADS_20261019.zip
python3 research/hh_phys69_20261019/band/verify_saved_band.py
```

다시 조합값을 확인해야 할 구체적인 필요가 있을 때만 새 출력 이름으로
exact assembler를 사용한다. 기존 certificate를 덮어쓰지 않는다.

```bash
python3 scripts/phys69_all_angular.py \
  --band research/hh_phys69_20261019/band/run_j29_36_t65 \
  --output runs/phys69_readback/ALL_ANGULAR_CHECK.json
```

완료 band 디렉터리에는 `--run --resume`를 사용하지 않는다.
max-new-panels0도 메타데이터를 다시 써 고정 SHA를 바꾼다.

## 새로운 NCP 실행에 앞서

실제 process/job 목록, run 디렉터리, 최신 관련 GitHub/백업의
REQUEST/CERTIFICATE/EXECUTION/manifest를 확인한다. 같은
source/request/engine/runtime의 완료본은 검증해 재사용하고, 진행 중이면
그 job을 관찰한다. 검색에 결과가 없었다는 사실만으로 host 부재를
추정하지 않는다. 이번 ChatGPT 세션의 NCP 제출은0, host 상태는 UNKNOWN이다.

서로 다른 세 ready campaign 중 현재 필요한 것만 순서대로 실행한다.
solver 설계는 이미 구현되어 있다. tolerance 완화, 물리·source 변경,
force-resume나 모델 대체를 하지 않는다. 작은 compile/path/package 수정은
diff와 새 engine identity를 보존하고 영향받은 부분만 확인한다.

### A. 기존 PHYS66 longtail6 — 아직 반환 영수증 없음

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r research/hh_phys68_20261019/ncp_delivery/requirements.txt
.venv/bin/python scripts/phys66_ncp.py \
  --profile longtail --out runs/phys66_longtail \
  --workers 1 --memory-gib 4 --timeout 900 --resume
```

L28/64 × T55/65/75의 여섯 새 campaign이다. PHYS64 NCP20이나 완료
PHYS66 pilot를 다시 실행하는 명령이 아니다.

### B. 기존 PHYS68 validated L64 — 별도 NOT_RUN

```bash
.venv/bin/python scripts/phys68_ncp.py \
  --request research/hh_phys68_20261019/ncp_delivery/REQUEST_L64.json \
  --out-root runs/phys68_ncp \
  --run --ncp-limits --wall-seconds 3600 --memory-gib 4
```

고정값은 m0,external21/20,j0..64,T65,N96,h1/8,rho1/4,R2,
768/2048bits,D1goal1e-45,D2goal1e-62다. 기존 일치 panel은 wrapper가
검증·재사용한다. PHYS69의 완료 D2 entry를 되돌리는 선행조건이 아니라
선택 가능한 더 큰 finite-block 실행이다.

### C. 새 VigilODE L64 — 별도 NOT_RUN

Rust1.94.1 이상 및 locked dependency를 사용한다. upstream pin은
a21d573980f66fe02891bd216153443b5352f921이다.

```bash
cargo build --locked --release --jobs 1 \
  --manifest-path native/phys69_vigilode/Cargo.toml
.venv/bin/python scripts/phys69_vigilode.py \
  --request research/hh_phys69_20261019/vigilode/REQUEST_L64.json \
  --make-seed --out runs/phys69_vigilode_l64 --run --timeout 900
```

이미 일치하는 L64 seed가 있으면 `--make-seed` 대신
`--seed /absolute/path/to/L64_SEED_INPUT.txt`로 재사용한다. 새 seed 생성은
기존 Coulomb initializer만 호출하고 Born 적분을 재실행하지 않는다.
L64 값은 L28 reference certificate와 다른 angular 합이므로 L28값으로
인증하지 않는다. 대응 L64 인증결과와 비교하는 별도 의무로 남긴다.
완료 L28 두 run은 다시 실행하지 않는다.

## 반환·게시·백업

실제 checkout HEAD/tree, input/source/request/engine/runtime hashes,
실제 hostname·시각·exit code, 계산/재사용 수, CERTIFICATE 및
INVOCATIONS/EXECUTION/stdout/stderr/manifest를 반환한다. solver success,
목표 오차 PASS, radial/angular/roundoff 성분을 별도로 판정한다.
원본 결과 ZIP과 SHA256SUMS를 만든다. 허용된 additive branch/draft PR와
create-only Drive/Dropbox 백업에 게시하고 실제 object ID/size/checksum/
revision/상태를 기록한다. 실패·부분 결과도 보존하고 완료로 바꾸지 않는다.

원래 atomic B27,k7/10,E49/200,R0=.7,H+=G+iF,Z=+u'u^-1,
V=2(1+1/d)e^-2d를 유지한다. eta=Fy,xi=Fy-phi,eta_C=-10/7은 다르다.
원본 NPZ SHA=f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d.
PHYS63 질적 existence는 ESTABLISHED_REUSED다. HH_R10=OFF.
