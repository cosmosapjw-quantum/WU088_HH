# PHYS80 — sandbox exact reduction와 Maxwellian 계산 계약

고정 PHYS79 isolated control의 21종 abundance와 thermal energy를
보존량으로 4개(CI+DCX) 또는 1개(DCX only) 상태로 환원한다.
같은 물리 입력에 새 algorithm identity를 부여한 Radau 실행 3개가 완료되었다.
full cosmological chemistry, 저온 CI source activation, production을 승인하지 않는다.

먼저 FINAL_REPORT_KO.md, CONTRACT.json, DAG_OVERLAY.json,
EXECUTION_LEDGER.json과 delivery/를 읽는다. 모든 부모 입력은 vendor/와
inputs/phys79_cases/에 byte-pinned되어 있어 이전 전체 repository가 없어도
이 단위의 계산 코드를 읽고 결과를 검증할 수 있다.

## 실행 계약

Python3.12.14, NumPy2.3.5, SciPy1.17.0에서 실행했다.
Python/NumPy/SciPy 버전은 ODE science identity에 포함된다.
그림에는 별도 figure 환경의 Matplotlib3.10.8을 사용했다.

현재 디렉터리에서:

    python source/run_reduced.py

위 명령은 계획 및 기존 identity를 검사한다. 다음 명령도 저장된 완료
identity에서는 receipt와 NPZ SHA256을 확인하고 SKIP_COMPLETE_VERIFIED로 끝난다.

    python source/run_reduced.py --execute

다른 출력 디렉터리를 주어 완료된 세 계산을 다시 돌리지 않는다.
변경된 의무가 있을 때 코드/physics/numerics/source identity를 명시하고
새 실행 계획을 세운다. incomplete/failed/orphan identity는 자동 재시도하지 않는다.
공유 lease가 없으면 WAITING_NO_LEASE로 실행하지 않는다.
다른 process를 종료하거나 resource limit을 변경하지 않는다.

source/maxwellian/bell_kernel.py는 명시적으로 주어진 I,A,B 계수만 받는
별도 수학 prototype이다. source_label은 출처 문자열이며 물리 admission이 아니다.
H/He/Li rate table의 기본값, isotope mapping, CI cooling adapter는 등록하지 않았다.
같은 디렉터리의 검증 스크립트와 완료 receipt를 함께 보존했다.

verification/independent/의 스크립트는 원 실행의 절대 경로와 create-only
fixture를 보존한 역사 증거다. source/run_reduced.py와 vendor/ 경로는 unit
위치를 기준으로 해소한다. 원 독립 검증을 그대로 재실행할 필요는 없다.

그림은 저장 결과만 사용한다. PNG/PDF 3쌍과 각 SHA는
verification/FIGURE_RENDER.json, PNG 시각 검토는
verification/FIGURE_VISUAL_QA.json에 있다.
새 renderer 환경에는 MPLCONFIGDIR를 쓰기 가능한 별도 /tmp 경로로 지정할 수 있다.

## 핵심 범위

- 고정 proper density, expansion=0, PI=RR=0, neutral CI와 D/H DB CX만 포함한다.
- T isotope/neutron과 모든 higher charge의 0이 현재 반응계에서 불변이다.
- isotope별 중성 비율을 고정한 affine lift로 저장 IC의 차이를 보존한다.
- reacting gas pi=0; 원 cosmology의 pi_m은 collisionless DM이다.
- signed matter/radiation tensor는 같은 normal orthonormal frame에서 합한 뒤 norm한다.
  Frobenius는 sqrt(2)×half-contraction이다. 이 단위는 tensor 규약을 바꾸지 않는다.
- first-integral energy residual과 sampled refinement는 continuum certificate가 아니다.
- 역사 nfev 비교는 작업량 근거다. 현재와 과거 wall-time의 paired benchmark는 수행하지 않았다.

HH_R10=OFF. Production admission NOT_ISSUED.

## 게시와 최종 전달

[Draft PR136](https://github.com/cosmosapjw-quantum/WU088_HH/pull/136)의 science commit은 `fd18c59796175191bdd5f9b7ab2981d5e92836fd`이다.
S0의 원격 135개 Git blob identity/size와 additive parent를 확인했다.
[게시 영수증](delivery/POST_PUBLICATION_RECEIPT.json)은 S0 checkpoint의 양 provider 저장 ACK도 기록한다.
최종 metadata HEAD와 최종 ZIP의 전체 bytes/CRC/payload SHA 검증은
외부 `PHYS80_FINAL_DELIVERY_20261022.json` 및 PR 본문에서 확인한다.
늦게 확인한 [HH135/REI222의 D 에너지 component](delivery/LATE_HH135_REI222_ASSESSMENT_KO.md)는
전달 DAG에서 부분 성과로 재사용하며 PHYS80 science payload나 실행 수를 바꾸지 않는다.
