# R9 — 실제 공급자, 상태 합산 이론과 코드의 결속

## 1. 이번에 해결한 문제

R3까지 원래 19개 target의 28개 방향은 primary-source 참조를 갖추었다. 이 참조 완결성과 모든 상태·동위원소·분자·음이온의 실제 물리 계수 완결성은 다른 조건이다. 이번 R4는 연결된 분자 생성·파괴 원자료를 찾아 여섯 provider variant와 77개 원 수치 셀을 채우고, 어떤 상태 집계가 정수 사건과 실제 소멸률을 연결하는지를 유도했다. 출처는 [source packet](sources/MOLECULAR_SOURCE_PACKET.json), 기존 결과의 재사용 경계는 [REUSED_CALCULATIONS](REUSED_CALCULATIONS.json)에 있다.

77개 수치는 발표된 이론 계수의 인쇄값이다. 서로 독립인 77개 실험이나 검증된 77개 runtime rate를 뜻하지 않는다. TIQM/SQM은 같은 사건의 계산 방법 대안이고, Bovino의 ortho/para는 source normalization 확인 전 자동 합산하지 않는다. 정수 수지의 H1/D2/Li7·핵 ground 모델과 source가 실제 명시한 질량수·isomer·전자·진동·회전 상태를 따로 보존한다.

## 2. 구성적 결론

유한 상태 밀도 x>=0, X=sum(x), 비음수 정규화 lift pi, 같은 collider h>=0와 같은 source convention의 상태별 계수 d>=0를 선언한다. L_pi X=pi X는 양수성과 총수를 보존한다. 정확한 소멸 source와 lift source는

\[
J=h d^{\mathsf T}x,\quad J_\pi=h(d^{\mathsf T}\pi)X,\quad
\Delta J=h d^{\mathsf T}(x-\pi X)
\]

이고, 합이0인 잔차에 대한 양·음 질량 분해로

\[
|\Delta J|\le {h(d_{\max}-d_{\min})\over2}\|x-\pi X\|_1
\]

을 얻는다. 고정된 pi와 h>0, 전체 비음수 상태 영역에서 하나의 scalar가 모든 x에 정확하려면 d가 상수여야 하고, 그 조건은 충분하다. h=0 또는 x=pi X인 제한된 상태족의 exactness는 별도다. 일반 P에 대해서는 d가 ker(P)를 소멸시키는 조건이 대응한다. 실제 상태 영역이 제한되면 실현 가능한 fiber 차이를 사용한다. 이는 모든 closure가 불가능하다는 strong no-go가 아니다. [정식 증명](theory/STATE_LIFT_THEORY_KO.md), [13개 claim](theory/CLAIMS.json), [독립 수용](theory/THEORY_ADMISSION.json).

현재 공급자 표는 실제 소비자에 필요한 전체 d,pi,b를 제공하지 않는다. 따라서 위 식은 실제 수치 오차를 가공하는 방법과 필요한 입력을 명확히 하며, 이번에 실제 LiH/HD population의 오차 수치가 얻어졌다는 뜻은 아니다. formation b는 정수 상태 channel의 사건 flux 가중치다. 이를 분수 stoichiometry의 한 사건으로 대체하지 않는다.

## 3. 구현과 근거

[THEORY_CODE_MAP](THEORY_CODE_MAP.json)은 각 claim을 코드, 저장 산출물 및 별도 이론 범위와 대응시킨다. 일반 P의 runtime closure solver나 실제 미지 b의 분기 solver는 구현했다고 주장하지 않는다. 실제 구현은 여섯 source-qualified 사건의 정수 투영, 선언한 유리수 상태의 lift/defect/bound, 원식의 계약된 29개 점 및 잘못된 조합의 차단이다.

변경하지 않은 finite compiler와 R1 adapter를 여섯 새 열에 적용했다. 과거149개 열과 합성249 결과를 재실행하지 않았다. baryon·charge·electron-lepton·동위원소 보존과 물질 총수 변화 [-1,0,0,0,0,0]가 확인됐다. RA의 primary photon1개와 총 cascade/실제 escape 수는 구별하며, 뒤의 두 값과 에너지는 미결정이다. 기존 gamma:escaping 문자열은 외부 수 장부 label이며 transport 증거가 아니다.

구현 검증28/28, 독립8/8군과1138 assertions, 독립 Decimal80 29점이 통과했다. 생산값과 독립 원식 참조의 최대 상대차1.942018822568154e-16는 고정 기준2e-14보다 작다. 이는 원식 구현의 표본 비교다. Wolfram의 유한 행렬36성분과5항등식의 정확한0 및2예제는 일반 증명의 독립 보조 근거이며, 그 자체를 전역 증명으로 쓰지 않는다.

Bennett500K의 table 분모 잔차24.8102185%와 fit 분모 잔차19.8783552%를 모두 유지했다. 원 table4.79e-20과 식의 계수는 독립 원문 대조에서 일치했다. 원문의 상대오차 분모가 미정이므로 논문 오류나 표를 고쳐야 할 근거로 해석하지 않았다. GL2022 두 점의 최대 table 분모 잔차는205K에서1.7802021%다. 이 잔차들은 covariance·물리 불확실성·Q가 아니다.

## 4. 물리 계수 및 전체 registry에 남은 조건

현재 새 provider의 실제 physical rate, nuclear Q, energy partition, 상태 lift 소비자 결속과 활성화는 모두 미승인이다. Bovino2.258eV는 native 추정 에너지이고, GL2022의405K는 fit의 activation parameter다. 둘 중 어느 것도 이번에 승인된 state-resolved Q가 아니다.

다음 실제 변경 입력은 [NEXT_INPUT_CONTRACT](followup/NEXT_INPUT_CONTRACT_KO.md)가 지정한 공급자 state block과 실제 consumer 계약이다. GL2022의 같은 온도에서 source가 허용한 전체 초기 상태의 d_j, 상태 에너지, 이미 포함한 spin 합산 및 실제 x 또는 pi를 결속하는 작은 단위가 구체적이다. aggregate 두 점에서 d_j를 역산하거나 LTE를 임의로 채우지 않는다. 기존 target6 EXFOR 관측량/beam response/covariance와 MeV consumer 조건도 별도로 남는다.

완료 수는 [DAG](DAG.json)와 실제 [WORKFLOW_RECORD](WORKFLOW_RECORD.json)를 따른다. 이 문서는 새로운 중앙 완료나 외부 소비자 ACK를 발급하지 않는다. 최종 code 수용은 독립 C9 판정 후 동일 ADMISSION_CANDIDATE의 scientific_payload를 SCIENTIFIC_ADMISSION으로 채택하는 절차에 따른다.
