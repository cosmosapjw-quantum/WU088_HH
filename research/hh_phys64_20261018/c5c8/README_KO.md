# PHYS64 C5-C8: 차수별 Born 응답과 NCP 실행 준비

## 기준과 보호 범위
백업을 먼저 확인했다. 확인한 WU Dropbox/Google Drive 경로의 최신 결과는 PHYS63이었고 새 NCP 결과는 없었다. PHYS63 최신 Git는 653db0dfaa57f04d7c0a93017c60a5902bdb319e. R5 PR111/0218ef1de8d36d0562b09b075aad0ad6f3055970를 계승한다. 실제 모델은 기존 원자단위 h=-Delta/2-1/r-(1+1/d)e^-2d, d=|x-0.7 zhat|, k=.7. 원래 eta=Fy, xi=Fy-phi와 입력 NPZ SHA256 f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d를 보존한다. 이번 수치 객체는 유한 m-block angular Galerkin, r27..T이며 T 바깥 screen은 0이다.

## 실제로 추가한 계산
Delta=sum epsilon^n Yn, epsilon=3e-23에서 Y1,Y2,Y3를 각자의 자연 크기로 직접 적분한다. Y2를 total-Born 차분으로 추출하지 않는다. 원래 비중심 potential의 각도 Gram은 매 RHS에서 평가하며, 포함된 모든 중간 ell의 행렬 곱을 유지한다. 세 번째 소스 Y1Y2+Y2Y1의 비가환 순서를 보존한다.

L28,m0,T39에서 계산된 물리적 기여(단위 a0^-1):
D1=(2.766042246013503e-24 +4.500676730156273e-25 i)
D2=(7.017743633174654e-48 +3.200163222384794e-48 i)
D3=(2.143001354846671e-71 +1.718651496404267e-71 i).
이는 유한 절단 Taylor 계수의 수치값이다. 전체 nonlinear remainder 또는 무한 angular DtN의 인증된 포함구간이 아니다. D1+D2를 f64로 더하면 D2가 사라지지만 두 항을 분리 저장하면 각각 계산 가능하다.

두 번째 기여는 L21->28에서 상대 0.0795663만큼 바뀐다. 반면 L28->32는 8.38e-14, L28의 angular128->192/rtol2e-11->2e-12/maxstep.25->.125 변화는 2.08e-13이다. 작은 self-difference는 절단오차 상계가 아니다. 원래 first Born에서 보이지 않던 중간 angular 채널의 중요성을 확인한 진단이다.

서로 다른 radial GL 적분으로 Yn 소스를 다시 적분했을 때 Y1/Y2/Y3 상대 잔차는 약1.21e-12/3.10e-12/1.21e-11. 이 검사는 ODE dense Coulomb 경로를 공유하므로 완전히 독립적인 special-function 검증으로 표시하지 않는다. 기존 mpmath first-Born 기준, signed-m 대칭, source-tamper 및 비가환 음성 제어도 별도 검사했다.

비물리적 strength1e20, ell0/1,r27..33에서는 직접 U,U' 방정식과 차수별 부분합을 비교했다. 1/2/3차 오차 약1.24e-7/2.93e-11/8.09e-15, 전류 잔차5.66e-16이다. 이는 비선형 코드 제어이며 원래 strength1의 numerical error certificate가 아니다.

## 구현 및 실제 실행
- src/wu088_hh/phys64_born_hierarchy.py: 완전한 1..5차 행렬 hierarchy, 별도 계수 적분 검증 및 JSON 요약.
- src/wu088_hh/phys64_campaign.py와 scripts/phys64_ncp.py: 직접 실행, 케이스별 OS 프로세스, timeout, 낮은 우선순위, 메모리 ceiling, atomic 결과, 입력/코드/환경/결과 SHA 기반 resume, 결과 패키징.
- scripts/phys64_born_hierarchy.py: 8개 원래 물리적 case와 별도 증폭 검산 생성기.
- 선택 회귀: 이전 PHYS63 24개+R5 12개+신규 solver22개+runner8개=66/66 PASS, exit0. 전체 과거 저장소 test suite를 실행한 것은 아니다.
- 실제 sandbox 프로세스 2개 완료; 같은 실행의 resume에서 2개 재사용, 추가 계산0. NCP는 아직 실행하지 않았다.
- 원본 solver나 생산 owner를 수정하지 않았다. 새 코드를 native Git 파일로 전부 게시한다. 압축 packet만으로 코드를 대신하지 않는다.

## NCP에서 그대로 실행
Python 실행 경로다. 새 Rust 포트나 solver 구현을 NCP에 맡기지 않는다. 필요한 Python 버전은 3.11 이상이며 tested package versions는 requirements-tested.txt에 있다. 기존 환경이 다르면 격리 venv를 쓰고 실행 버전을 기록한다.

```bash
python3 scripts/phys64_ncp.py --preflight-only --out research/hh_phys64_20261018/ncp_run
python3 scripts/phys64_ncp.py --profile smoke --workers 2 --resume --out research/hh_phys64_20261018/ncp_run
python3 scripts/phys64_ncp.py --profile extended --workers 4 --memory-gib 4 --timeout 180 --resume --out research/hh_phys64_20261018/ncp_run
```

extended는18개: m0,L21/28/40/64,T35/39/43, m1/2,L28/40,T39, L28 refinement192/256점이다. 기본 총4 worker/각4GiB VM/BLAS1 thread. 이미 실행 중인 다른 연구를 종료하거나 설정을 바꾸지 않는다. 실패 attempt도 보존하며 output별 로그와 종료 코드를 남긴다. 네트워크 연결/SSH key 검사는 하지 않는다. 현재 호스트가 승인된 NCP이면 직접 실행한다.

성공 후 CAMPAIGN.json, cases/*/SUCCESS.json, 각 attempt의 RESULT.json/COEFFICIENTS.npz를 확인한다. 실행기는 SOURCE_RESULTS.zip와 SHA256SUMS를 자동 생성하고 내부 바이트를 검증한다. 클라우드 게시 권한을 가정하지 않으므로 cloud_backup=NOT_ATTEMPTED_BY_RUNNER이며 실제 Git/Dropbox/Drive 게시 및 복원은 승인된 기존 도구로 이어서 수행한다.

## 다음 과학 의무
질적 full real-axis LAP/Poisson/DtN은 PHYS63에서 확보한 상태로 유지한다. PHYS64의 명시적 continuum 나머지 상계는 ell0/1 유한반경 투영에만 적용한다. 고차 P20-Q21의 유용한 정량 상수, radial/angular tail, floating interval error, interior matching/original driven xi 및 sigma(E),k_HH(T)는 여전히 미완료다. HH_R10=OFF. native_subagents=NOT_RUN.
