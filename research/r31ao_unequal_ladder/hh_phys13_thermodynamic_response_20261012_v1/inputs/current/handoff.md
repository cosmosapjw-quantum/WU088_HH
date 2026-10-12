# WU088_HH atomic-reuse 후속 작업 인계

대상 repository는 cosmosapjw-quantum/WU088_HH다. 이번 변경은 사용자 첨부 REI Atomic-Reuse successor DAG를 반영한 HH 계획·제공 계약이다. 계획의 실제 commit/PR은 최종 delivery receipt에서 읽는다. 과학 기준점은 PHYS12 commit dcea5dc6545736e6f4afa5acf4b7eabd428485e8, science subtree ff2625c424a9c2e17af99d960fd6fcdda79227f9다.

## 먼저 읽을 것

root AGENTS.md와 CURRENT_DEVELOPMENT_PLAN.json, 이 계획의 DEVELOPMENT_PLAN_KO.md, NEXT_DAG.json, TASK_CARDS.jsonl, review/PLAN_REVIEW.json, HH_RETAINED_RESULTS.json, contracts/HH_REI_EXPORT_CONTRACT.json, contracts/HH_PROCESS_OWNER_ROWS.json을 읽는다. 원 첨부는 inputs/에 보존했다. 원 global DAG의 PROPOSED_NOT_EXECUTED를 실제 PASS로 바꾸지 않는다.

PHYS12 L0–L2와 L3 종료는 기존 완료다. endpoint 산술, 원 source/root/inverse, 과거 PHYS09/11 suite, 저장 그림을 자동 재실행하지 않는다. PHYS12는 same-alpha source/C2 조건 아래 두 별개의 첫 단계에 대한 finite x_HII/w 응답이다. 전체 history·범용 k(T)·HH 생략 증명으로 사용하지 않는다.

## 다음 HH 작업

현재 HH_REUSE는 등록됐고 HH_EXPORT 제공 계약은 준비됐다. 다음은 HH_DOMAIN_SCREEN이다.

1. 기존 공유 산출물에서 실제 소비 요청과 scenario identity가 제공됐는지 한 번 확인한다. 이미 있는 입력을 사용자에게 다시 요청하지 않는다. 원 첨부의 경로 존재만으로 source admission이나 현재 REI PASS를 추론하지 않는다.
2. 실제 소비 요청이 있다면 contracts/HH_CONSUMER_REQUEST_TEMPLATE.json의 consumer commit/scenario/process/observable/domain/units를 결박한다. 소스 식·고정 계수·COMMON·stage/PreBE·변수·단위를 함께 대조한다. 수치 domain box가 겹치는 것만으로 PHYS12 적용을 승인하지 않는다.
3. HH_CONSUMER_ADMISSION.json에 일치, 별도로 증명된 포함, 불일치 또는 미결 필드를 남긴다. 불일치가 있으면 필요한 최소 source/변환/입력 작업 하나를 고른다.
4. 적절한 소비 입력이 없으면 NO_CONSUMER_BOUND와 정확한 미결 필드, 최소 입력 작업을 반환하고 이 경로를 멈춘다. 이를 현재 전체 REI 물리입력 부재의 증거로 기록하지 않는다. 반복 readiness polling을 하지 않는다.
5. 적용성이 확인되고 관측량의 절대 허용오차 또는 명시적인 HH 응답 질문이 정해지면 HH_MATERIALITY로 간다. 작은 mixed I를 HH 총기여로 쓰지 않는다. 상계가 기준을 넘는 것만으로 중요한 효과가 확정됐다고 쓰지 않는다.

## 실제 EoR 비교가 선정되는 경우

RUX14의 HH_MATCHED_HISTORY에는 실제 RUX11 기준 결과, HH process/domain admission과 구체적 효과·불확실성 질문이 필요하다. 물리 history 실행 owner는 rei_bianchi이고 HH는 과정/응답 authority를 제공한다. 이 HH 계획의 작성·게시만으로 외부 repo mutation 또는 history 실행이 발생한 것으로 기록하지 않는다.

O(G,lambda)의 FLRW/BI × OFF/ON 네 경우를 정의하고, 같은 geometry의 ON/OFF에서 source/IC/closure를 유지한다. geometry 간 변경도 사전에 고정한다. 이미 계산된 정확한 조건의 경우를 재사용하고 빠진 경우만 실행한다. 실제 수행한 x_HII,T_g,n_e 및 결박된 BASS tau/visibility만 보고한다. time carry, nuclei/charge/photon/energy 장부와 관측량별 오차를 보존한다.

## 독립 HH 연구와 NCP

HH_STRICT_NATIVE와 HH_SINGLET은 독립 선택 경로다. REI RUX04/RUX07/RUX11을 이들 작업의 선행조건으로 넣지 않는다. 각자의 원 source/basis/native/root/ray/guard/carry 또는 channel/spin/velocity/impact/energy/tail 조건은 유지한다. LCS 자유전자 생성과 H+/H− singlet 생성은 다른 과정이며 후자의 즉시 자유전자 증분은 0이다.

현재 heavy_queue=[]; launch=false; NO_HEAVY_JOB_READY다. 새 과학 job은 배정되지 않았다. NCP_TASKS.json의 경로별 과학 입력·실제 비용·독립 분할 조건을 충족하는 새 작업만 선정한다. 경량 계약·자료 읽기·유도·필요한 작은 산술은 HERE에서 수행한다. 56 workers/112 GiB는 64-core/128-GiB 환경의 정책 상한이며 실측 최적값이 아니다. 시간 carry와 같은 gas에 결합된 photon groups를 독립 작업으로 쪼개지 않는다.

## 반환

RETURN_TEMPLATE.json에 실제 선택 노드, 입력 identity, 소비 적용성, 실행 command/exit/output, 실제 비용, 정확한 미결 필드, 다음 최소 작업, 독립 판정과 claim 범위를 기록한다. template의 null을 성공이나 관측된 0으로 채우지 않는다. 새 과학 수행이 없으면 그 사실을 명시한다.

root/main이나 과거 PHYS12 과학 파일을 덮어쓰지 않는다. 승인된 변경은 새 branch/PR와 독립적인 immutable 결과로 보존한다. Git object/ACK/metadata verification이 충분하면 동일 자료를 반복 다운로드하지 않으며 upload와 실제 restore를 구분한다.
