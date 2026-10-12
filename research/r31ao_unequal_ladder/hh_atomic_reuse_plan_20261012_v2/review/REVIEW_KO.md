# HH Atomic-Reuse v2 독립 계획 검토

## 판정

**APPROVE_PLAN_SCOPED.** 사용자 첨부 REI DAG를 WU088_HH의 현재 PHYS12 기준에 연결한 계획·제공 계약의 재편을 채택할 수 있다. blocking finding과 필수 수정 요구는 없다. 이 판정은 새 PHYS13, 원자율·native runtime·소비자 EoR 이력 또는 production의 과학적 승격이 아니다.

검토자는 `/root/replan_remote_intake`다. 앞선 역할은 실제 HH GitHub 상태의 read-only 관측과 원래 기준 파일의 identity 확인이었다. 후보 계획·계약 작성과 후보 validator 설계에 참여하지 않았다. frozen candidate를 받은 뒤 원문을 직접 읽고 판정했으며 후보 47개 파일을 수정하지 않았다.

## 검토 대상과 실제 확인

`review/CANDIDATE_FREEZE.json`의 SHA256은 `5ce98cb56433919f64fbcd334a954c8f53dc76131580525209708ee356e97c1b`다. 처음과 검토 종료 시점 모두 47/47 파일의 크기·SHA256이 일치했다. 전체 목록은 `REVIEWED_FILE_HASHES.json`에 있다.

첨부4개 사본은 실제 upload 원본과 byte가 같았다. 원 global 17노드의 ID·title·owner·dependencies·status는 대응표와 일치한다. PHYS12와 과거 root에서 복사한 baseline8개 및 intake evidence3개도 원본과 일치한다. PHYS12 subtree `ff2625c424a9c2e17af99d960fd6fcdda79227f9`와 정확 결과 blob `13c946c63912e3a082f8c2d21c75d055d7874125`는 앞서 확보한 실제 remote tree에 결박된다. 이는 `INDEPENDENT_REFERENCE_READBACK.json`에 보존했다.

후보의 기존 구조 검사 1회/29항목 PASS 기록을 읽었지만, 그것만으로 의미를 판정하지 않았다. 아래 결론은 실제 계획 본문·source 계약·local/global DAG·작업 카드·root·handoff 및 상속한 근거를 직접 대조한 결과다. 후보 validator를 import하거나 다시 실행하지 않았다. source/native/PHYS12/이력 계산과 과거 full suite 재실행은 모두 0회다.

## 의미 검토

1. **권위와 재사용.** 원 첨부는 proposed snapshot이고 현재 HH 과학 기준은 실제 PR46/PHYS12다. S14의 역사적 pointer를 덮어쓰지 않고 S14_PHYS12로 이후 결과를 연결한다. N2의 과거 HOLD에서 오늘의 외부 입력 부재를 추론하지 않는다. 저장된 자료는 보존·재사용되며 새 계산으로 표현되지 않는다.

2. **RUX14 의존성.** 제공 계약과 구체적 입력이 있는 적용성·관측량 준비는 RUX11 전에 가능하다. 실제 EoR HH ON/OFF 이력에는 `external_dependencies=[RUX11]` 및 실제 baseline 증거가 요구된다. 준비 완료를 global RUX14 완료로 바꾸는 경로가 없다. RUX00–16 원 상태와 전제는 보존된다.

3. **독립 HH 연구.** strict-native와 microscopic singlet은 고유 source/native 또는 atomic/channel 입력 의무를 유지한다. REI RUX04/RUX07/RUX11을 이들 고유 연구의 선행조건으로 추가하지 않았고, 이들 완료를 REI baseline의 선행조건으로도 만들지 않았다.

4. **Source-family 적용성.** PHYS12의 같은 α, COMMON과 기존 광자, real-lift와 상속 source/C² 전제, 각각의 stage/PreBE 및 root branch 조건을 유지한다. 좌표 box가 겹치는 것만으로 다른 history에 포함을 수출할 수 없다는 제한이 명시돼 있다. 두 첫 단계는 누적 이력이나 k(T) 표로 사용되지 않는다.

5. **사건·단위·스위치.** LCS에서는 net HI −1, HII +1, 자유전자 +1이고 singlet H+/H−에서는 HI −2, HII +1, H− +1, 즉시 자유전자 0이다. 후자의 rate·threshold는 새로 만들어 넣지 않았다. q의 proper fraction/s와 w의 thermal eV/H, 원 pair-counting convention, threshold의 한 번 집계가 유지된다. λ=0과 b_amp=0의 미래 소스 의미도 보존된다.

6. **관측량 판정.** 절대 HH 기여, Bianchi–FLRW 차이, 그 차이에 대한 HH 기여를 구분한다. 유효한 상계가 허용오차 이하인 경우에만 scoped omission을 지지하고, 절대효과 하계가 허용오차를 넘을 때만 materiality를 확정한다. 상계가 큰 경우 자체는 중요도 확정이 아니다. 작은 mixed I나 HH 기여를 분모로 한 ratio를 전체 EoR 생략 오차로 쓰지 않는다. consumer threshold가 null인 현재에는 생략 판정이 없다.

7. **계산과 NCP.** 네 geometry/switch 경우는 논리적 비교이며 네 번의 새 실행 명령이 아니다. 동일 조건 저장 이력을 재사용하고 빠진 경우만 계산하도록 했다. 실제 비용·고정 입력·실행 manifest·안전한 독립 분할이 있을 때 NCP를 선택한다. RUX04/RUX07/RUX11은 REI 소비 경로에 적용되며 독립 native/singlet에는 고유 전제가 적용된다. 시간 carry와 공통 gas에 결합된 photon groups를 임의로 병렬 task로 나누지 않는다. 56worker/112GiB는 정책 상한이고 실측 최적값이 아니다.

8. **현재 진입점.** root의 plan/state·문서, local DAG·task card, handoff가 PHYS12 유지·조건부 DOMAIN_SCREEN·빈 NCP queue를 같은 의미로 지시한다. 과거 native 지침은 역사적 범위로 보존돼 자동 benchmark의 새 지시가 되지 않는다. 미결 필드 한 번 확인 후 정확한 최소 작업을 반환하도록 하여 반복 readiness 감사가 default가 되지 않는다.

## 판정의 한계와 종료

제공 계약은 준비됐지만 실제 소비자 runtime이 결박된 것은 아니다. 전체 EoR의 HH 효과, 임의 source에 대한 k(T), native root/U/V/W/I, carried second_half, 시간·연속체 나머지, global/production은 이 검토로 채택되지 않는다. 원 PHYS12 `PROMOTE_SCOPED`는 원 전제하에 그대로 보존된 과학 증거다.

게시·백업·원격 복원은 이 검토의 범위 밖이다. frozen 이후의 실제 commit/PR와 provider ACK는 별도 delivery receipt에서만 확정한다. raw request/response의 경로 맥락은 `evidence/README.md`가 전체 패키지의 `remote_intake/`로 설명한다.

요청된 계획 재편의 의미 검토는 완료됐다. 이 판정을 위해 추가 과학 계산이나 재감사를 수행할 필요는 없다.
