# WU088_HH PHYS68 — NCP 실행/반환 handoff

ROLE=BOUNDED_NCP_EXECUTION_AND_RETURN
REPO=https://github.com/cosmosapjw-quantum/WU088_HH
BRANCH=research/hh-phys68-validated-born-profiles-20261019
BASE_PR117=1a149efeba61a9ffd7ea882bdd86f7ea36c0b78c
HH_R10=OFF

## 먼저 읽고 실제 상태를 구분한다

`research/hh_phys68_20261019/REPORT_KO.md`, `NEXT_DAG.json`,
`theory/PROOF.md`, `theory/FINAL_EXECUTION_REVIEW.json`,
`profiles/run_l28_t65_completed/CERTIFICATE.json`,
`ncp_delivery/README_KO.md`, 최신 `publication/` 영수증을 읽는다.
science commit, 이후 metadata HEAD, ZIP payload, cloud ACK는 서로 구분한다.
해당 branch는 실제 PR117 위의 추가 연구다. 이전 PHYS66 local snapshot을
Git descendant로 추정하지 않는다. 원래 최신 PR114/115 proof를 덮지 않는다.

완료 재사용: PHYS64 NCP20건, PHYS66 pilot/smoke, PHYS67 D1 및 Coulomb20점,
PHYS68 L28 D2의76패널(첫2개 보존+74개 신규), Rust2432/4864step.
이미 성공한 이 계산과 historical test suite를 반복하지 않는다.
PHYS68 원본78개 panel payload는 SHA256
`b930a1dff10f656c853d81f7ddc8048e9eb7b188431958cd8c4ca702ca87d1e3`인
`PROFILE_PANEL_PAYLOADS_20261019.zip`에 있다. Git에는 코드·증명·최종
certificate·실행 및 독립검토 영수증을 게시하고, 원본 payload ZIP은
source/evidence 배포 ZIP에 포함한다. panel이 필요하면 이 archive를
검증해 `research/hh_phys68_20261019/profiles/`에 복원한다.

## NCP에서 새 실행 전에 확인할 것

NCP의 실제 process/job 목록과 `runs/phys66_longtail`, `runs/phys68_ncp`
및 새 백업의 REQUEST/CERTIFICATE/INVOCATIONS/manifest를 확인한다.
동일 request·source·engine·runtime의 성공 결과가 있으면 검증해 재사용한다.
실행 중이면 같은 job을 관찰한다. provider의 특정 검색에서 결과가 없었다는
것만으로 NCP host에 실행이 없다고 판단하지 않는다. 이 ChatGPT 세션의
NCP 제출 및 NCP radial 실행은0이며, actual host state는 확인하지 못했다.

## 완성된 PHYS68 L64 확장

추가 solver 설계 없이 있는 runner를 사용한다. fixed request는 m0,
D2(21,20), 모든 j=0..64, B27,T65,N96,h1/8,rho1/4,R2,
768/2048bits, D1(B)goal1e-45,D2fullgoal1e-62다.
기존 L28 결과가 이 L64 요청을 완료한 것은 아니다.

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r research/hh_phys68_20261019/ncp_delivery/requirements.txt

.venv/bin/python scripts/phys68_ncp.py \
  --request research/hh_phys68_20261019/ncp_delivery/REQUEST_L64.json \
  --out-root runs/phys68_ncp \
  --run --ncp-limits --wall-seconds 3600 --memory-gib 4
```

`--run` 없는 동일 명령은 preflight-only다. 현재 환경에서 이미 수행한
preflight는 성공했지만 새 NCP runtime의 binding은 실제 버전으로 기록한다.
wrapper가 기존 REQUEST를 검사하고 일치하는 panel을 `--resume`으로
재사용한다. 입력/engine/runtime mismatch나 불명확한 output은 자동
새 계산으로 우회하지 않는다. 임의 tolerance/목표 완화, source SHA guard
제거, force-resume 또는 수학적 구현 변경은 하지 않는다.
컴파일/패키지/경로 등 작은 호환 수정은 diff와 새 engine fingerprint를
보존하고 영향 범위만 검증한다. timeout이면 저장된 진행을 보존한다.

## 기존 PHYS66 longtail6

새 host 성공 결과가 없고 실행 중이지 않을 때만 완성된 기존 runner를
사용한다. PHYS68 L64 인증 campaign과 다른 f64 longtail campaign이다.
기존 전달 ZIP SHA256:
`34a59dfe3158c454811ed6e6f47c82357e502ef8cdef9ee5f14640b37f73a835`.

```bash
.venv/bin/python scripts/phys66_ncp.py \
  --profile longtail --out runs/phys66_longtail \
  --workers 1 --memory-gib 4 --timeout 900 --resume
```

## 반환해야 할 실제 결과

실제 checkout HEAD/tree, source/engine/runtime/request hashes, hostname과
실제 시작·종료·exit code, 새로 계산/재사용한 panel 또는 case 수,
CERTIFICATE와 INVOCATIONS/표준출력/표준오류/manifest를 반환한다.
오차 목표 통과 여부를 수치 적분/roundoff, radial cutoff, excluded angular로
나누어 판정한다. ZIP+SHA256SUMS를 만들고 기존 파일을 덮지 않는 새 이름으로
Git 게시와 Google Drive/Dropbox 백업을 수행한다. 실제 ACK·object ID·size·
revision/checksum 또는 unresolved 상태를 각각 기록한다.

PHYS63 all-angular qualitative LAP/Poisson/DtN은 ESTABLISHED다.
finite-L 바깥 higher-order angular bound, 원래 xi=Fy-phi,
regular origin/incoming adjoint, sigma(E), Maxwellian k_HH(T)는 OPEN이다.
atomic B27,k7/10,E49/200,eta_C=-10/7,H+=G+iF,Z=+u'u^-1,
V=2(1+1/d)exp(-2d), 원래 frozen NPZ SHA
`f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`
및 HH_R10=OFF를 유지한다.
