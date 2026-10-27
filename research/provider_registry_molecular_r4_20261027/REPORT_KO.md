# WU088_HH molecular R4 — R10/C10 재개 보고서

## 현재 결과와 전달 상태

2026-10-27 재개 시 GitHub의 실제 연구 HEAD는 f949c21cca6e2534b725241068bd6c6e06158495, tree는 92b79d59129f9545785da0b56e39da3b1a4df261였다. 연구 브랜치는 research/provider-registry-20261025, 기존 draft는 PR150이다. main은 이 연구 계열의 현재 권위가 아니다.

R4의 source·조건부 이론·정수 사건·원식 표본 구현은 독립 검토 후 이미 채택됐다. 이번에는 그 과학 결과를 재실행하지 않고 마지막 인계 내용을 작성하고 S09 전달 근거를 회수했다. 로컬 DAG는 **9/24**, 이론·코딩 워크플로의 완전히 종료된 단계는 **18/20**이다. R10/C10의 문서 내용은 준비됐으며, 계약된 최종 S10 전체 ZIP과 양 provider 실제 바이트 readback이 남아 있으므로 전달 완료를 20/20으로 올리지 않는다.

권위는 SCIENTIFIC_ADMISSION.json, reviews/C9_FINAL.json, DAG.json, WORKFLOW_RECORD.json이다. 원래 과학 payload의 canonical SHA256은 다음과 같으며 이번 재개에서 다시 일치했다.

    34765b943cce5a67d49a622f76c0cf9aeceb635c8cd6a3cf58b5cebb8e3c5fde

이 보고서와 인계서의 실제 게시 identity는 후속 delivery/R10_PUBLICATION.json에 결속한다. 그 영수증이 생기기 전에는 이 문서의 존재를 미래 게시·백업 ACK로 해석하지 않는다.

## 재사용한 과학적 성과

| 항목 | 범위와 근거 |
|---|---|
| 실제 분자 공급자 | LiH 방사결합·파괴와 HD 생성·파괴의 6 source variants, 원 수치 77 cells |
| 정수 사건 연산자 | 새 6열; 기존 R1/R2 149열과 합성249검사를 재사용 |
| 상태 집계 이론 | 명시한 전제 아래 13/13 claims 독립 수용 |
| 구현 | 기존 receipt의 28/28 checks |
| 독립 수치 비교 | 기존 8/8 groups, 1138 assertions, Decimal80 29 native nodes |
| 수치 범위 | 원식 구현 최대 상대차 1.942018822568154e-16, 고정 한계 2e-14 |
| 기호 보조검산 | 이전 R4의 실제 1회 Wolfram: 행렬36성분·5 scalar identities의0과2예제 |
| 물리 소비자 | state population, source normalization, energy owner와 실제 consumer ACK 미결속 |

77 cells는 발표된 이론 계수의 인쇄값이다. TIQM/SQM은 계산 방법 대안이고 Bovino ortho/para의 source-normalization 조건은 별도로 남는다. 직접 생성 광자 수, 총 cascade 광자 수와 실제 escape 수를 구분한다. RA의 primary photon1개는 나머지 광자·열 에너지의 값을 결정하지 않는다.

## 상태별 계수를 집계량에 연결하는 식

같은 proper-time convention과 source normalization을 사용하는 유한 상태 밀도 \(x_j\ge0\), collider 밀도 \(h\ge0\), 소멸 계수 \(d_j\ge0\), 고정된 비음수 정규화 lift \(\pi_j\)를 둔다.

\[
X=\sum_jx_j,\qquad \sum_j\pi_j=1,\qquad
J=h\sum_jd_jx_j,\qquad J_\pi=h\left(\sum_jd_j\pi_j\right)X .
\]

따라서 \(r=x-\pi X\)는 \(\sum_jr_j=0\)을 만족하고
\[
\Delta J=J-J_\pi=h\,d^\mathsf Tr.
\]
\(d_c=(d_{\max}+d_{\min})/2\)를 빼도 \(d_c\sum r_j=0\)이므로
\[
|\Delta J|
=h|(d-d_c\mathbf1)^\mathsf Tr|
\le {h\over2}(d_{\max}-d_{\min})\|r\|_1 .
\]

각 밀도가 cm\(^{-3}\), \(d_j\)가 cm\(^3\) s\(^{-1}\)이면 \(J,\Delta J\)와 우변은 cm\(^{-3}\) s\(^{-1}\)이다. \(h=0\), 일정한 \(d_j\), 또는 \(x=\pi X\)에서는 오차가0이다. 고정 \(\pi\)·\(h>0\)와 전체 비음수 상태 영역에서 하나의 scalar 계수가 모든 \(x\)에 정확한 필요충분조건은 \(d_j\)가 모두 같은 것이다. 이를 확인하려면 단일 상태에 질량 \(X\)를 놓은 \(x=Xe_j\)를 각각 대입하면 된다. 제한된 상태족에서의 정확성과 일반 사영 \(P\)의 조건은 기존 theory/STATE_LIFT_THEORY_KO.md의 범위를 따른다.

이는 이번 재개에서 새로운 물리적 \(d,\pi,x\)를 채웠다는 뜻이 아니다. 현재 구현 molecular_operator.destruction_defect는 선언된 유리수 입력에 대한 정확한 조건부 연산이며 physical_source_binding=false를 유지한다.

## 원식 구현 오차와 source-fit 잔차

Bennett2003의 500 K 인쇄값은 4.79e-20 cm3/s이며, 같은 원식의 저장된 Decimal80 값은 약 5.9784094667234974e-20 cm3/s다. 이를 table 값으로 나눈 잔차는24.8102185%, fit 값으로 나누면19.8783552%다. 두 분모를 함께 보존한다. 원문의 상대오차 분모가 특정되지 않아 이 사실만으로 논문 오류를 판정하거나 원표를 수정하지 않았다.

GL2022의 두 native 비교점에서는 table 분모 잔차 절댓값의 최대가205 K에서1.7802021%다. 이 source-fit 잔차와 binary64 구현 상대차는 서로 다른 값이다. 전자는 covariance, 물리적 신뢰구간, Q 또는 energy-partition uncertainty로 채택되지 않았다. 이번 재개는 이 수치들을 저장 결과에서 재사용했으며 새로운 fit evaluation은0이다.

## 이번에 직접 확인한 보존 근거

S01–S09 모두 Dropbox와 Drive의 현재 객체가 존재하며 각 쌍의 이름과 크기가 일치했다. S09의 원 upload ACK 파일은 기존 Git tree에서 찾지 못했으므로 새로운 회수 영수증을 작성했다. 과거 ACK 원문을 복원했다고 주장하지 않는다.

S09 원본을 Drive의 raw-file 반환으로 읽었다.

- 파일: WU_MOLECULAR_R4_S09_20261027_f949c21cca6e.zip
- 크기: 1,092,150 bytes
- SHA256: 84e7f59613b26add26c3d8ce4ff64cc49db99782e644345065cdff7c6d9f19ac
- ZIP CRC:145/145 members
- Manifest payload의 bytes/SHA256:144/144
- 각 payload의 Git blob SHA1 재계산:144/144
- 현재 pinned Git tree의 경로·size·blob SHA 대응:144/144
- source commit/tree와 SCIENTIFIC_ADMISSION canonical payload의 일치 확인

검증은 현재 제공된 JavaScript 실행 기능에서 메모리 안의 원 바이트에 수행했다. SHA256·SHA1의 empty/abc와 CRC32의123456789 알려진 검산값을 먼저 확인했다. 파일시스템에 압축을 풀지는 않았다. Dropbox S09는 현재 metadata까지 확인했으며 이번에 Dropbox 원본 전체 GET을 수행한 것은 아니다. 상세 결과는 delivery/S09_RECOVERED_READBACK.json과 재현 가능한 검증 핵심 코드에 있다.

## 현재 실행환경과 미완료 전달

이번 턴의 python3 실행 probe, c++ 호출 및 task-local 파일 쓰기는 모두 실행 서비스의 "No usable execution environment is available" 응답으로 시작되지 않았다. 분류는 각각 SERVICE_ERROR이며 Python package 부재나 compiler 부재로 판정하지 않는다. 연결 기기 inventory에는 online device가0개였고 그 기기에서 실행을 시작하지 않았다.

GitHub와 provider 읽기 및 메모리 검증은 가능해 이 보고서, 실제 다음 입력 계약, 인계서와 영수증을 준비·게시한다. 새 S10 ZIP을 로컬에서 생성하거나 업로드했다고 주장하지 않는다. 남은 작업은 기존 package_checkpoint.py의 --full 실행, create-only Dropbox/Drive 저장, 두 실제 원본의 바이트·member 비교다. 후속 턴은 런타임을 새로 probe하고 이 관측을 상속하지 않는다. 권한·정책 차단이나 사용자 재승인 요청이 아니다.

## 다음 물리 입력

구체적인 다음 단위는 González-Lezana, Hily-Blant & Faure (2022), DOI10.1063/5.0128598의 **HD+H+ destruction state block**이다. 원문 식(5)–(7)과 supplementary-material 안내를 현재 다시 읽었다. 원 논문은 HD(v=0,j=0..8)에서 H2(v'=0,j'=0..9)로의 state-to-state 계수와5–3000 K 범위를 기술한다. 이번 retrieval에서 원 numerical supplement의 배열은 취득되지 않았다. 이는 자료 부재 판정이 아니다.

동일 온도의 원 \(k_{0j,0j'}\) 또는 이미 source-qualified된 \(d_j\), 초기 상태 에너지, spin weighting, support/tail와 실제 소비자 \(x\) 또는 명시한 \(\pi\)가 필요하다. EMAA의 HD excitation 자료는 별도 반응(2)이며 destruction 반응(1)의 자동 대체물로 쓰지 않는다. 상세한 원자료 경로와 입력/출력·수용·중단 조건을 followup/NEXT_INPUT_CONTRACT.json 및 .md에 작성했다.

원 target6 EXFOR의 identical-D normalization·beam response·covariance·MeV photon consumer와 PHYS91의 B1/consumer 의무는 별개로 유지한다. 과거 PHYS91 primary/reference/Wolfram remaining은 모두0, global history/remaining은null이다. 새 scientific execution0, compiler call0, IVP0, Q evaluation0이며 기존 실행 비용 장부를 바꾸지 않는다. HH_R10=OFF, production=NOT_ISSUED, L4_ready=false와 중앙 completion delta0을 유지한다.
