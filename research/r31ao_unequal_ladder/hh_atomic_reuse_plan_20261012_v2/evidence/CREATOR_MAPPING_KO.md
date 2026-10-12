# WU088_HH와 첨부 RUX DAG의 매핑 분석

## 판정

첨부 4개 파일과 실제 PHYS12 `DECISION.json`, 상태·DAG·source contract를 읽었다. 이 분석은 계획 매핑이며 새 물리 계산, 원본 변경, 원격 mutation을 수행하지 않았다. PHYS12의 로컬 판정은 `PROMOTE_SCOPED`다. parent가 전달한 실제 repo pin은 `dcea5dc6545736e6f4afa5acf4b7eabd428485e8`이며, 이 하위 분석에서는 해당 원격 pin을 다시 조회하지 않았다. 입력별 byte size와 SHA256은 `DAG_MAPPING.json`에 남겼다.

재편의 핵심은 WU088_HH를 **HH 소스·응답 제공자 및 독립 미시 반응 연구**로 유지하고, REI의 실제 EoR 이력과 연결되는 작업만 RUX14에 매핑하는 것이다. 첨부 DAG의 모든 RUX 노드는 계획상 `PROPOSED_NOT_EXECUTED`이므로, 현재 HH 문서에서 이들의 외부 완료 상태를 새로 발명할 수 없다.

## 원문과 현재 결과를 연결하는 결정

1. **기존 결과 재사용:** 첨부 S14는 PHYS11와 observable-first 계획을 가리킨다. 현재 PHYS12는 그 계획의 L0–L2를 이미 수행하고 L3에서 종료했다. 첨부 원본은 보존하고 `S14_PHYS12` 후속 증거 항목으로 최신 결과를 추가한다. 동일 endpoint 산술, 기존 source/native 계산 또는 독립 검토를 재실행하지 않는다.
2. **REI 선행조건 분리:** RUX04–RUX11·RUX16에 HH strict certificate, full49, 미시 singlet 연구 완결을 선행조건으로 추가하지 않는다. 첫 REI baseline은 HH OFF 또는 명시적으로 선택한 검증 범위의 effective closure로 구성할 수 있다. 그 선택은 소비자의 owner registry와 물리 모델 기록에 남겨야 한다.
3. **RUX14의 준비와 실행 분리:** HH 생산자 계약과 기존 local sensitivity 자료는 지금 준비할 수 있다. 실제 `HH_EFFECT_ON_EOR.json`은 외부 RUX11 결과와 채널의 관측량 관련성·적용영역 판정이 있을 때 수행한다. PHYS12 완료로 RUX14 전체를 PASS 처리하지 않는다.
4. **대형 계산 정책의 범위:** 첨부 JSON `execution_policy.no_new_heavy_until`에 RUX04·RUX07이 범위 표기 없이 들어 있다. 이를 모든 HH 대형 계산에 복사하면 독립 singlet lane에도 EoR 시나리오·결합 interval 선행조건이 생긴다. 이 두 조건은 REI 소비용 우주론 이력 작업에 적용하고, 독립 미시 연구에는 기존 원자 source/basis/raw input, channel/spin/velocity/impact/energy/tail 의무 및 실제 비용·독립 분할 gate를 적용한다.

이 결정은 첨부 원문 §§3.1–3.2의 “HH는 첫 EoR history 필수조건이 아니며 독립적 연구 가치를 유지한다”는 의도를 보존한다. 원문 자체가 독립 연구를 폐기하라고 요구하지 않는다.

## Global–local 매핑

| Global 노드 | HH에서 제공할 부분 | 완료 처리 범위 |
|---|---|---|
| RUX00 | PHYS12 source/result/decision pin, 재실행 금지 항목 | HH 증거만; 7-repo inventory 완료가 아님 |
| RUX01 | 보존된 PHYS12 표와 그림을 별도 HH diagnostic으로 제공 | F08/SYNC03 결과 재사용과 구분 |
| RUX02 | HH 소비에 필요한 물리 입력·domain 항목 | 실제 REI input admission은 외부 owner |
| RUX03 | HH OFF·LCS·singlet 별도의 owner/stoichiometry/energy/domain rows | 전체 H/He opacity registry를 대체하지 않음 |
| RUX04–11 | 실제 채택된 consumer scenario/history가 필요할 때 참조 | HH가 선행 blocker가 되지 않음 |
| RUX14 | 보존된 local sensitivity + HH producer export + 조건부 EoR 비교 | PHYS12는 local sensitivity 하위 의무만 충족 |
| RUX16 | HH 범위·출처·오차 정보를 소비자에게 제공 | physical/continuum/production 판정은 별도 |

## 제안하는 HH local DAG

| 노드 | 의존성 | 바로 만들거나 기다릴 산출물 | 성공·중단 기준 |
|---|---|---|---|
| `HH_REUSE` | 기존 PHYS12 | `HH_RETAINED_RESULTS.json` | 정확한 원본과 독립 판정 연결; science rerun 없음 |
| `HH_EXPORT` | HH_REUSE | `HH_REI_EXPORT_CONTRACT.json`, `HH_OWNER_ROWS.json` | effective LCS와 미시 singlet 구분; units·switch·COMMON·source family 명시 |
| `HH_DOMAIN_SCREEN` | HH_EXPORT + 실제 consumer request | `HH_CONSUMER_ADMISSION.json` | 소비 계열이 원래 고정 source family와 일치/포함되는지 확인; domain box 수치만 맞는 것으로 충분하지 않음 |
| `HH_MATERIALITY` | HH_DOMAIN_SCREEN + 선언된 관측량·허용오차 | `HH_MATERIALITY_DECISION.json` | 절대 HH 기여를 관측량 tolerance와 같은 단위·범위에서 비교; 국소와 전 이력 판정 분리 |
| `HH_MATCHED_HISTORY` | HH_MATERIALITY의 필요 판정 + 실제 RUX11 | `HH_EFFECT_ON_EOR.json` | 같은 IC·source·closure·geometry·solver를 유지하고 지정 HH 채널만 ON/OFF; 실제 필요한 경우 한 번 비교 |
| `HH_STRICT_NATIVE` | 기존 strict DAG | 선택된 native certificate 결과 | PHYS11 고유 의무 유지; REI baseline이나 이미 채택된 LCS 결과의 선행조건이 아님 |
| `HH_SINGLET` | 고유 원자 입력·물리 목표 | 지정한 원래 microscopic observable | 독립 연구로 유지; RUX04·RUX07·RUX11을 요구하지 않음 |

`HH_DOMAIN_SCREEN`은 준비 작업이므로 RUX11 전에도 진행할 수 있다. 실제 RUX14 EoR 결과의 원문 의존성은 유지한다. 이번 요청이 계획 재편인 만큼, 위 신규 science 노드를 실행 완료로 표시해서는 안 된다.

## PHYS12가 이미 해결한 내용과 해결하지 않은 내용

이미 채택된 결과는 각기 COMMON에서 출발하는 두 **서로 다른 첫 단계**에서, 각 단계의 한 고정 계수 묶음 α를 유지한 미래 LCS HH ON/OFF 유한 차이다. λ와 b_amp는 [0,1]이고, b_amp=0에도 기존 광자는 남는다. 상속한 열린 C²/source inclusion 및 균일 U 포함에서 FTC로 절대 x_HII와 열에너지 w 응답을 얻었다. full과 first_half 모두 Δx>0, Δw<0이며 기존 혼합 응답 I는 별도 재사용했다.

이 결과로 다음을 제공할 수 있다.

- 검증 범위를 유지한 `delta_x_HII` 및 `delta_w_thermal_eV_per_H`의 정확 포함.
- 해당 고정 계열의 HH–미래 광자 생성 혼합 효과와 절대 효과의 구분.
- export 소비 시 지켜야 할 정의, units, 원 source identity와 조건.

현재 결과로 제공할 수 없는 것은 다음이다.

- 임의의 T·밀도·redshift를 입력받는 일반 `k_HH(T)` 표.
- PHYS12의 Δx/dt를 그대로 쓴 순간 반응률, 두 first-stage 결과를 누적한 EoR 이력.
- 임의의 비등방성에서의 부호·크기: 저장된 Hubble triplet은 [1e-14,1e-14,1e-14] s^-1다.
- w의 부호만으로 추정한 온도 차이: 입자수 계수 변화가 필요하다.
- 작은 혼합 I 또는 작은 국소 Δx만으로 정한 우주론적 HH 생략 가능성.
- 실제 native root/U/V/W/I, carried second_half, 시간·연속체 오차, 전역 보존, full49 또는 production의 새로운 인증.

consumer process ID, scenario identity, 실제 source/history, 관측량·허용오차는 아직 이 분석에서 새로 제공되지 않았다. 이들은 `null`로 남기며 0 또는 물리적 효과 없음으로 해석하지 않는다. 외부 입력이 새로 주어지기 전까지 재귀적 blocker 감사나 임의 HH 정밀화를 시작할 이유는 없다.

## HH 소스 계약의 물리적 최소항목

LCS source는 q = n_H,proper (1−x_HII)^2 k_LCS(T)와 H=q(1,0,0,−χ_H)를 유지한다. q는 proper second당 정규화된 H 분율 소스이고, w는 H핵당 열에너지 eV다. 원 LCS 정의에 새 pair-counting 1/2를 삽입하지 않는다. 별도 microscopic singlet H+ / H− 사건을 직접 자유전자 생성 LCS 사건으로 대체하지 않는다.

소비자 계약에는 반드시 원 source lock·COMMON·고정 α의 identity, stage duration, switch 범위, source/opacity owner, stoichiometry, threshold energy, energy-bookkeeping 역할을 연결한다. PHYS12 reference X가 x_HII∈[0.90,0.93], y_HeII∈[0.29,0.31], y_HeIII∈[0.59,0.61], w∈[13,14] eV/H에 있다는 것만으로 다른 실제 EoR state의 적용성을 증명할 수 없다. source equation과 나머지 고정 계수도 맞아야 한다.

baseline HH OFF 여부와 제외한 사건도 owner row에 기록하면, precision 연구가 끝나지 않았다는 이유로 첫 EoR을 막지 않으면서 이후 채널을 켤 때 중복 수지를 방지할 수 있다.

## NCP 선택 조건

현재 queue=[]와 launch=false를 유지한다. 이 재편 자체는 대형 계산의 실행 명령이 아니다. 기존 NCP 정책의 선택 조건은 두 경로 중 하나다.

- **REI 소비용 HH:** 지정된 관측량 민감도/오차 예산이 추가 HH 계산을 요구하고, RUX04·RUX07에 해당하는 실제 물리 입력·결합이 유효하며, 실제 RUX14 history 단계라면 RUX11 및 matched-history 계약도 충족할 것.
- **독립 HH microscopic:** 구체적 원자 반응 관측량과 고유 source/basis/channel/domain gate가 충족될 것. REI의 물리 입력이 이 연구의 필요 입력이 아니라면 RUX04·RUX07·RUX11은 요구하지 않는다.

두 경로 모두 named unfinished task, immutable inputs, 실행기와 계약의 일치, 타당한 기존 pilot 재사용 또는 필요한 최소 pilot, wall/CPU/RSS/overhead, 독립 분할·checkpoint/resume이 필요하다. 하나의 이력 내부 time carry와 공통 gas에 결합된 photon groups는 임의 독립 task로 쪼개지 않는다. 이전 56 worker/112 GiB는 상한이며 실제 가용 자원·개별 RSS·I/O·미완료 독립 task 수로 축소해야 한다.

## 분석 종료

계획 매핑에 필요한 구분을 모두 도출했다. 재편에서 새로 해야 할 것은 HH 결과의 producer export와 소비/독립 lane별 조건을 기계 판독 가능하게 보존하는 것이다. global 과학 노드 완료 추정, native/원자율 재실행, 새 consumer tolerance 조작은 필요하지 않다. 이 분석에서는 원본 bytes 보존 및 읽은 source identity 기록 외에 과학 실행을 수행하지 않았다.
