# WU molecular R11 — 지정 7개 ref의 실제 변경과 HD 입력 확인

## 결론과 관찰 범위

2026-10-28 **12:04:08 KST**에 R10 종료 조사에 지정된 같은 7개 ref를 실제 GitHub GET으로 확인했다. **3개 이동, 4개 불변, HEAD GET 오류 0**이다. 변경된 immutable source 10개와 CR PR112 최종 본문 1개를 읽었으며, 저장 완료 시각은 **12:06:12 KST**다. Immutable 10개 파일은 모두 변경 비교 응답의 Git blob SHA와 실제 바이트가 일치한다. PR 본문은 조회 시점의 mutable 관찰이다.

이번 범위에서 새 실제 HD reactive array 또는 WU에 결속된 물리 consumer/state/density/clock의 전달은 관찰되지 않았다. 따라서 저장된 WU R7–R10 입력·증명을 재사용하며 별도 full-A 유한 블록 연구를 진행할 수 있다. 이 판정은 모든 저장소·대화·백업에 대한 전역 자료 부재가 아니다. 기존 51 repo/2375 heads census와 전체 첨부·백업 조사는 재실행하지 않았다.

## 동일한 7개 ref 비교

| 저장소 / branch | R10 종료 SHA | 이번 SHA | 변화 |
|---|---|---|---|
| rec_bianchi / research/rec-h5-defect-bridge-independent-20261028 | 6fdf2cca545d9b44d0666bc22a3233a675e5ad03 | 6fdf2cca545d9b44d0666bc22a3233a675e5ad03 | 불변 |
| rei_bianchi / research/orchestration-sandbox-20261022 | 22a99cb9b1691274e74c122d54521be4f2f51ba5 | 3d8bcdb79a7062459adaad9be6d7fe951f86a17a | 이동 |
| rei_bianchi / research/rei-causal-prefix-consumer-20261027 | e77bc7ec48ae2aee8ded573e66ac0a1060017c54 | 66878795aa14f79b32be0cd532c31b3a4a036985 | 이동 |
| bass / research/bass-b3h-restart-cocycle-20261028 | f834101d3292f304681349db5d435c6f0c6b559e | f834101d3292f304681349db5d435c6f0c6b559e | 불변 |
| vigilode / research/production-solver-closure-20261027 | 7eb2dd0ffda39afb2871d76700a720986ff09fe0 | 7eb2dd0ffda39afb2871d76700a720986ff09fe0 | 불변 |
| bass_cr / research/cr-he-event-union-20261028 | e91a0d19b13a0b3254c194e7a4863b845c271874 | 729cb95164697d8122b0a85ae6e403b57392e724 | 이동 |
| BASS_HE / research/he-azimuth09-20261028 | 307fee38cb65b957deea84c3308f59e972049362 | 307fee38cb65b957deea84c3308f59e972049362 | 불변 |

## 바뀐 과학·전달 의존성

### REI central

Central branch는 HE-HARMONIC10의 조건부 second-harmonic reference 관찰과 CR event-union의 실제 scoped owner return을 추가했다. Central completed/total은 원문 권위에 따라 **28/88**, CR count effect 0이다. WU 관련 node status는 이번 diff에서 바뀌지 않았다. HE 원문에는 25 methods/26 evaluations, 최초 24 PASS+1 FAIL과 별도 targeted 1 PASS, Wolfram 117 zero residuals/14 True 및 2 precision warnings가 함께 보존돼 있다. 이를 WU 수치 근거나 물리 binding으로 이식하지 않는다.

근거: [CR actual return](https://github.com/cosmosapjw-quantum/rei_bianchi/blob/3d8bcdb79a7062459adaad9be6d7fe951f86a17a/research/orchestration_expansion_20261025/returns/CR_HE_EVENT_UNION_20261028.json), [central status](https://github.com/cosmosapjw-quantum/rei_bianchi/blob/3d8bcdb79a7062459adaad9be6d7fe951f86a17a/research/orchestration_expansion_20261025/status/CURRENT_STATUS.json).

### REI finite thermal

R10 조사 당시 9/20에서 **10/20**으로 진행했다. Source literal binding과 `finite_thermal.py`, 테스트 원문, guarded runner를 작성했고, C5 상태는 **AUTHORED_NOT_EXECUTION_VERIFIED**다. 테스트 실행·module import·syntax/AST/compile·CAS·actual-source evaluation·IVP·plot은 모두 0으로 기록돼 있다. 별도 distinct-author R6/C9도 미완이다.

Source-caloric 식 `N=Na+dN, U=cv*Na*Ta+Q+W, T=U/(cv*N)`을 구현했으며 JSON number via binary64, hex dyadic, saved MP-decimal의 출처를 구별했다. 물리 temperature/native25/nb/radii는 null이고 full_state_update=false, L4_ready=false다. 이는 actual WU HD consumer의 공급이 아니다. C5 source capsule 63,289 bytes와 두 provider ACK·크기 확인이 기록돼 있으며 원본 byte 재다운로드는 NOT_RUN이다.

근거: [C5 handoff](https://github.com/cosmosapjw-quantum/rei_bianchi/blob/66878795aa14f79b32be0cd532c31b3a4a036985/research/rei_expanded_event_consumer/finite_thermal_endpoint_20261028/HANDOFF_C5_20261028.md), [source literal binding](https://github.com/cosmosapjw-quantum/rei_bianchi/blob/66878795aa14f79b32be0cd532c31b3a4a036985/research/rei_expanded_event_consumer/finite_thermal_endpoint_20261028/inputs/SOURCE_BATH_LITERAL_BINDING_20261028.json).

### CR He event union

R10의 당시 관찰인 수행14/20·dual-backup13/20은 역사적 기록으로 보존한다. 이번 실제 source/PR/central return에서는 **20/20** 및 stage dual R2 20개를 확인했다. Scientific S=`406783036c26e71f3b85568adcfb5e163b012ab1`, documents D=`729cb95164697d8122b0a85ae6e403b57392e724`, central M=`3d8bcdb79a7062459adaad9be6d7fe951f86a17a`다.

Scoped decision은 PASS_SCOPED_EVENT_UNION, open blockers 0, child1/1이다. Primary39/39+9,603 atomwise, controls42/42, independent3,696/3,696, graph81, CAS12groups/16zeros가 실제 결과로 보고됐다. 같은 상태의 finite atomic family에서 `0<=C<=min(N/2,N-max_i n_i)`와 once-only source correction을 구현·검증한 결과다. 저장된 N, Cmax 등 값은 조건부 H1/He4 100K, nb=8750/47에 속한다.

**actual exclusive measure, actual Ccross, outside partner response, actual projectile donor work, actual EOS/T, absolute proper volume, full-source physical native25는 여전히 null**이다. 명명된 `consume_event_union`의 범위를 WU의 physical binding으로 승격하지 않는다. Canonical SOURCE 및 CLOSEOUT 양 provider actual original full GET SHA/CRC R3 PASS는 해당 owner 원문/PR가 보고한 완료 근거이며, 이번 intake가 원본 ZIP을 다시 다운로드한 것은 아니다.

근거: [scientific summary](https://github.com/cosmosapjw-quantum/bass_cr/blob/729cb95164697d8122b0a85ae6e403b57392e724/research/cr_he_event_union_20261028/SCIENTIFIC_SUMMARY.json), [C9](https://github.com/cosmosapjw-quantum/bass_cr/blob/729cb95164697d8122b0a85ae6e403b57392e724/research/cr_he_event_union_20261028/review/C09_FINAL.json), [PR112 actual closeout](https://github.com/cosmosapjw-quantum/bass_cr/pull/112).

## SciSpace·Exa의 실제 HD 자료 조사

SciSpace 자연어 질문 1회는 10개 논문을 반환했지만 정확한 GL2022 항목은 반환하지 않았다. Lepers–Guillon–Honvault의 2019 TIQM 연구는 관련 원전 locator로 식별했고, 다른 반응계와 HD+ electron 논문은 현재 reactive input으로 채택하지 않았다.

Exa 검색 2회와 primary publisher article fetch 1회를 수행했다. [González-Lezana–Hily-Blant–Faure, JCP157,214302(2022)](https://doi.org/10.1063/5.0128598)의 III.A/III.B 및 supplementary/data-availability 설명을 읽었다. 원문은 reactive channel의 SQM numerical rates를 supplement에 둔다고 명시한다. EMAA 안내는 별도 nonreactive channel에 해당한다. 이번 반환 내용에는 actual reactive state-to-state array bytes가 없었다. TIQM/SQM 구별과 native v=UNSPECIFIED, MISSING_NOT_ZERO 상태를 유지한다.

추가 primary locator 확인을 위한 web system1 3 queries와 AIP/HAL 2 open은 수행했다. Publisher open은 접근 불가 CDN redirect로 SERVICE_ERROR, HAL은 URL 접근 불가로 SERVICE_ERROR였다. 이 접근 결과는 supplement 자료의 부재를 증명하지 않는다. **Actual reactive arrays retrieved=0**이며 다음 물리 입력 계약을 그대로 유지한다. 세부 검색 metadata는 HD_SOURCE_LOCATOR_RESEARCH.json에 있다.

## 재사용·재개 결정

불변 4 refs는 이전 근거를 재사용한다. 새로운 외부 정책·예산·owner의 중단 규칙은 WU 규칙으로 이관하지 않는다. 기존 WU R10 source와 실행은 재실행하지 않았고, physical/central delta0, HH_R10=OFF, production=NOT_ISSUED, L4=false를 유지한다. 남은 과학 입력이 공급되면 exact source family/state/clock/density/whole-domain binding을 먼저 처리한다.

