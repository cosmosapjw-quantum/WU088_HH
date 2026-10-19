# PHYS68 NCP 전달: 선택적 finite-L64 확장

## 준비한 작업

`scripts/phys68_ncp.py`는 완성된 `scripts/phys68_profiles.py`를 호출한다.
기본 실행은 preflight-only이며 실제 L64 radial campaign은 `--run`이
명시될 때 시작한다. 본 전달의 상태는 **PREPARED_NOT_SUBMITTED**다.
이 단계에서 실제 NCP 접속·host 전달·radial campaign은 수행하지 않았다.

L28의 진행·완료 결과는 기존 PHYS68 profile 증거에서 재사용한다.
이 wrapper의 고정 요청에는 L28 선택지가 없다. NCP가 설계할 solver나
새 수치기법은 없으며, 필요한 업무는 환경 호환 확인과 실제 실행이다.

| 항목 | 고정 요청 |
|---|---|
| 표적 | D2(21,20), m=0, finite L=64 |
| 내부 angular sum | j=0..64 전부, 65개 |
| 필요한 D1 pairs | 129개 |
| 반경 | B=27, T=65 |
| panel half-width | h=1/8, 총 152개 panel |
| zero-free disk | rho=1/4 |
| analytic majorant disk | R=2 |
| Taylor 차수 | 96 |
| arithmetic / angular coefficient precision | 768 / 2048 bit |
| 모든 요청 D1(B)의 절대오차 목표 | 1e-45 a0^-1 |
| full-radial D2의 절대오차 목표 | 1e-62 a0^-1 |

요청 본문은 `REQUEST_L64.json`에 있다. 원래 source SHA256은
`f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`다.
해석적 D2 반경 cutoff bound는 약 7.541139e-66 a0^-1이고 고정 D2
목표보다 작다. 전체 numerical budget 충족 여부는 실제 반환된
`CERTIFICATE.json`의 오차 상한으로 판정한다.

이 finite-L64 확장은 finite-L28 이후의 수치 범위 확장이다. L>64의
excluded-angular response, 원래 source-driven xi, origin/incoming
adjoint, sigma(E), Maxwellian k_HH(T)의 완료를 뜻하지 않는다.
HH_R10은 OFF다.

## 호환 환경과 명령

이번 preflight 환경은 Python 3.12.14, python-flint 0.8.0 / FLINT 3.3.1이다.
패키지는 `requirements.txt`에 정확히 고정했다. 실제 Python patch version,
python-flint/FLINT version과 engine 파일 SHA256은 실행 fingerprint에 들어간다.
이전 결과를 resume하려면 그 입력·engine·runtime binding이 일치해야 한다.

저장소 root에서 환경을 준비한다.

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r research/hh_phys68_20261019/ncp_delivery/requirements.txt
```

먼저 NCP의 기존 성공 영수증과 실행 중인 process를 확인하고 일치하는
완료 결과를 재사용한다. 다음 명령 자체는 신규 radial panel을 계산하지 않는다.

```bash
.venv/bin/python scripts/phys68_ncp.py \
  --request research/hh_phys68_20261019/ncp_delivery/REQUEST_L64.json \
  --out-root runs/phys68_ncp
```

실제 NCP 실행 명령은 다음과 같다.

```bash
.venv/bin/python scripts/phys68_ncp.py \
  --request research/hh_phys68_20261019/ncp_delivery/REQUEST_L64.json \
  --out-root runs/phys68_ncp \
  --run --ncp-limits --wall-seconds 3600 --memory-gib 4
```

동일 명령을 다시 호출하면 일치하는 기존 `REQUEST.json`을 검사하고
`phys68_profiles.py --resume`을 사용한다. 완료된 panel은 내부 hash·chain
검사 후 재사용한다. wrapper는 동일 fingerprint의 동시 호출을 file lock으로
막는다. 별도의 runner나 외부 process 전체를 이 lock만으로 조사한 것으로
간주하지 않는다.

## 실행·실패 처리

출력 경로는 `runs/phys68_ncp/phys68_l64_<full SHA256 fingerprint>`다.
fingerprint는 정규화한 request, source SHA, engine source SHA와 runtime
identity를 함께 결합한다. request 자체의 canonical SHA와 사용한 JSON
파일 bytes SHA도 별도로 기록한다.

빈 output은 새 실행에 사용할 수 있다. 이미 존재하는 output의 REQUEST
binding이 다르거나, 빈 폴더가 아닌데 REQUEST가 없으면 child를 시작하기
전에 거부한다. 같은 scientific request가 다른 engine/runtime 아래의
형제 폴더에 있으면 자동 중복 실행을 거부하고 먼저 대조하도록 한다.

preflight receipt와 launch logs는 solver output 바깥의 `receipts/`에,
완전한 요청 파일은 `requests/`에 기록한다. 따라서 solver의 빈 output
검사를 preflight 기록이 방해하지 않는다.

한 solver process를 사용하고 child의 BLAS/OMP thread 수는 1로 고정한다.
`--ncp-limits`는 Linux child에 address-space RLIMIT_AS 4 GiB와 nice10을
적용한다. wall timeout이 지나면 자신이 만든 process group만 종료하고,
기존 output을 보존한다. 실제 저장 panel 수를 기록하며 checkpoint의
존재를 가정하지 않는다. timeout 뒤 새 INVOCATIONS 행이 없으면 이전
성공 기록을 이번 실행 결과로 채택하지 않는다. resource limit의 실제
target-host 적용 결과는 NCP 실행 receipt에서 확인한다.

## 실제 preflight와 검증

선택한 요청으로 preflight를 실제 한 번 수행했고 exit0, 약 3.923 s였다.
center=217/8, rho=1/4에서 normalized outgoing Coulomb 함수의 검증된
zero-free lower endpoint는 다음과 같이 양수였다.

| ell | lower endpoint의 읽기용 값 |
|---|---:|
| 0 | 0.7936551545496114 |
| 20 | 0.9266218192709977 |
| 21 | 0.9217943086171174 |
| 64 | 0.1859770365786238 |

정확한 dyadic endpoints는 `PREFLIGHT_STDOUT.json`과 `preflight_only/receipts/`
파일에 있다. (21,64), (20,64)의 degree96 angular Taylor 계수도 각각
97개가 finite임을 실제 확인했다. 전체 152개 panel이나 모든 반경에서
목표를 달성했다는 판정은 이 preflight로 내리지 않는다.

wrapper의 최종 focused tests는 `TEST_EXECUTION.json`에 기록했다.
실제 engine을 `max_new_panels=0`으로 호출해 REQUEST/resume 계약을
확인했고, 작고 독립적인 Python child로 single-thread environment와
wall timeout을 확인했다. NCP resource limit을 적용한 과학 실행은 없다.

첫 preflight 뒤의 변경은 실행 전용 file lock과 timeout/invocation
분류 보강이다. 실제 preflight에 사용한 원 wrapper bytes를
`PREFLIGHT_EXECUTED_WRAPPER.py.txt`로 보존했다. request·binding·destination·
mathematical_preflight 함수의 AST와 scientific engine identity가 그대로이므로
이미 통과한 네 Coulomb·두 angular probe는 재실행하지 않았다.

기존 PHYS66 six-case longtail runner는 별도 준비물이다. 그 ZIP SHA256
`34a59dfe3158c454811ed6e6f47c82357e502ef8cdef9ee5f14640b37f73a835`와
미제출 상태를 보존하며, PHYS68 wrapper가 이를 실행하거나 대체하지 않는다.
