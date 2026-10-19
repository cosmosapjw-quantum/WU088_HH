# PHYS66 NCP longtail runner 전달 준비

**상태: PREPARED_NOT_SUBMITTED.** 기존 runner의 source와 필수 dependency
manifest를 deterministic ZIP으로 묶었고, 깨끗한 추출본에서
`--preflight-only`를 실제 실행해 exit0을 확인했다. 새 solver·pilot·campaign은
실행하지 않았다. NCP의 실제 host preflight와 longtail 실행은 아직 NOT_RUN이다.

## 전달 파일

- 이름: `WU088_HH_PHYS66_LONGTAIL_RUNNER_20261019.zip`
- 크기: 95,615 bytes
- SHA256: `34a59dfe3158c454811ed6e6f47c82357e502ef8cdef9ee5f14640b37f73a835`
- ZIP20 members, manifest18 payloads
- sorted member order, fixed timestamp/perms, ZIP_STORED 사용
- 같은 입력에서 다시 만든 archive와 전체 bytes 일치 확인

완성된 파일은 task staging의 `delivery_phys67/`에 있다. root가 최종 결과와
함께 게시·백업한다. 그 상태는 해당 provider·git 응답에서 별도로 기록한다.

capsule은 CODE8개, package init, 원본 frozen NPZ, 최신 PHYS65/66 proof,
정확 package versions,6개 request, 실행 shell command, 검증 script와 SHA
manifest를 포함한다. 기존 PHYS66 파일은 수정하지 않았다. 원본 NPZ 해시는
`f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`와 일치했다.

준비 당시 repository HEAD는 `1a1e5b6df5e5f88de851bc4686949089e2444291`이다.
이 HEAD는 복원된 runner overlay의 게시 commit을 뜻하지 않는다. 실행할
파일들의 authority는 capsule manifest의 개별 SHA256으로 고정했다.

## 실제 확인 범위

`PREFLIGHT_ONLY_EXECUTION.json`과 원 stdout/stderr에 다음을 보존했다.

- 깨끗한 추출본의 payload18개 hash/size 확인
- 원래 source guard와 PHYS65 upstream blob guard 통과
- Python3.12.14, NumPy2.3.5, SciPy1.17.0, mpmath1.3.0 실제 import 성공
- 기존 runner의 코드 compile/preflight 완료, exit0
- scientific worker request0개, campaign receipt0개, solver 실행0회

이 preflight는 약0.45초 걸렸으며 NCP host라고 주장하지 않는다. package
wheel과 Python interpreter는 source capsule에 포함하지 않았다. NCP는
기존 적합한 환경을 사용하거나 `requirements-pinned.txt`로 환경을 준비한
후 자신의 preflight receipt를 남긴다. 추가 solver 개발은 필요하지 않다.

## 고정 요청과 명령

`REQUESTS_LONGTAIL.json`은 기존 `case_specs('longtail')`를 호출해 생성했다.
L28/L64 각각 T55/T65/T75, 총6개다. 공통 설정은 m0,join39,orders3,
nodes128,rtol2e-11,max_step0.25다.

```bash
.venv/bin/python scripts/phys66_ncp.py --profile longtail \
  --out runs/phys66_longtail --workers 1 --memory-gib 4 --timeout 900 --resume
```

capsule의 `run_preflight.sh`와 `run_longtail.sh`가 위 고정 자원 설정과
BLAS/OpenMP 단일 thread를 적용한다. worker1개, address-space4GiB,
각 case wall900초;6개 worker wall limit 합은5400초다.

resume은 source/code/package versions/Python build/spec fingerprint가 같고
SUCCESS 영수증과 두 payload의 SHA가 유효한 case를 재사용한다. 유효한 성공
영수증이 없는 case만 새 attempt를 생성한다. 실패와 timeout은 원래 attempt에
남긴다. 다른 fingerprint를 과거 성공과 섞지 않는다.

실행자는 `SOURCE_RESULTS.zip`, `SHA256SUMS`, `PREFLIGHT.json`,
`CAMPAIGN_longtail.json`을 반환하면 된다. 과거 PHYS64의20건은 이 profile에
포함되지 않는다. numerical integration/roundoff와 angular 제외 sector의
total error는 별도 의무이며 **HH_R10=OFF**를 유지한다.
