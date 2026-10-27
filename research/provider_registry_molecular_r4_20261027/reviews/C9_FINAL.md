# R4 C9 독립 최종검토

**최종 판정: 출처·조건부 이론·6개 정수 반응열·고정 29점의 원식 구현에 한정하여 승인한다. final_freeze=true이며 남은 blocking finding은 0건이다.** S08의 실제 최종 그림, 13개 이론–코드 대응표 및 구체적인 admission 후보를 읽어 기존 수치 검토와 일치함을 확인했다. 물리 rate·Q·consumer 결속과 활성화는 승인 범위에 포함되지 않는다.

검토자 /root/authority_survey는 공급자 원행 및 생산 코드의 작성자가 아니다. 검토자는 독립 검사기를 작성했고, root가 S07에서 이를 한 번 실행한 실제 결과와 영수증을 읽었다. C9에서 생산 코드, 검사기, 기존 249 검사, 원식, compiler, Wolfram을 실행하지 않았다. 정확한 파일 해시는 동반 JSON에 기록한다.

## 1. 실제 완료된 근거

| 근거 | 실제 결과 | 승인되는 범위 |
|---|---:|---|
| primary01 | 첫 실행 exit 0, 신규 6열, 원식 29점 | 동결된 출처를 읽고 완결된 7개 payload와 마지막 COMPLETE marker를 생성 |
| implementation01 | 28/28 | typed guards, method·spin 구분, 부분 출력·실행 실패의 기록 |
| independent01 | 8/8군, 1,138 assertions | 출처 77셀 보존, 6열의 독립 보존량·소유권 검토, 29점 Decimal80 기준값 |
| 독립 이론검토 | 13/13 조건부 명제 승인 | 명시된 유한 상태와 cone/lift 가정 안의 증명 |
| 신규 Wolfram 1회 | 행렬 36개 원소·스칼라 5개 항등식이 정확히 0 | 선언된 행렬과 예제; 일반 정리의 독립 증명은 별도 근거 |

최대 이진 64비트–Decimal80 상대차는 \(1.942018822568154\times10^{-16}\)이다. 사전에 고정한 원식 구현 기준 \(2\times10^{-14}\)를 충족한다. 기준은 원식의 구현 오차에 적용되며, 논문 표에 대한 fit 잔차나 물리적 정확도에 전용하지 않는다. 기준점은 Bennett의 27개 native 온도와 González-Lezana 2022의 두 native 비교 온도다.

독립 검사기의 실제 결과 SHA256은 **ac42d76bcb5471b32c4b635bb20998256181bc3227ed39855e889c505790bf56**이고, 실제 실행 영수증은 **da60c926e415806c22bbeac32a5736021caf84ce762c22795fbc546706f95ebb**다. 결과 파일의 PASS를 실행 계획으로 추정하지 않았다.

## 2. 출처와 반응열의 해석

6개의 공급자 variant와 77개의 native rate 셀, 14개의 상태 식별자, 7개의 coarse material family, 6개의 정수 반응열이 존재한다. 14개 상태 식별자는 새로 결속된 14개 물리 population을 뜻하지 않는다. H1·D2·Li7 및 핵 ground 상태의 모델 지정은 출처의 미지정 isotope·state 정보와 구분된다.

소유권은 5개 그룹이다. Honvault의 TIQM과 SQM은 동일한 물리 event를 설명하는 방법 대안으로서 합산하지 않는다. Bovino의 ortho·para 분기는 구별하되 unresolved spin normalization을 임의로 닫지 않는다. Bennett의 준결합 생존 가중 aggregate와 GL2022의 회전 열적 평균 및 제품 spin 가중은 각 출처의 의미를 유지한다. 반대 방향의 coarse 열만으로 상세평형이나 공통 상태 ensemble을 도출하지 않는다.

RA의 즉시 방출 primary photon 수는 1이며 다른 5열의 해당 primary 수는 0이다. **총 cascade photon 수, escaped photon 수, escaped energy는 6열 모두 null**이다. legacy adapter의 gamma:escaping 명칭은 수 bookkeeping이고 광자 수송이나 escape fraction을 승인하지 않는다. 6열의 energy는 null이며 UNQUALIFIED:ENERGY가 유지된다.

기존 R1/R2/R3의 149개 열과 합성 249 검사는 재사용했다. 신규 6개 열의 보존량 확인을 실제 rate·핵 Q·heat·runtime consumer 승인으로 확대하지 않는다.

77셀의 원문 대조는 이전 출처 검토의 고정 packet 및 명시적인 재구성 영수증을 재사용한다. 이번 독립 검사는 packet과 공개 숫자 derivative 사이의 77셀 무결성을 확인했다. 소실된 원 검토 파일을 복구했다고 주장하거나 원 논문 77셀을 다시 추출하지 않았다.

## 3. Fit 잔차의 두 분모

다음 수치는 저장된 29개 독립 기준값에서 읽었으며 추가 fit 계산은 하지 않았다.

\[
r_{\rm table}=\frac{k_{\rm fit}-k_{\rm table}}{k_{\rm table}},
\qquad
r_{\rm fit}=\frac{k_{\rm fit}-k_{\rm table}}{k_{\rm fit}}.
\]

| 출처와 온도 | 최대 절댓값: table 분모 | 최대 절댓값: fit 분모 |
|---|---:|---:|
| Bennett, 500 K | 24.810218511972806% | 19.87835516015286% |
| GL2022, 205 K | 1.78020210900424% | 1.812467697174358% |

Bennett 500 K의 native 표 값은 \(4.79\times10^{-20}\ {\rm cm^3\,s^{-1}}\), Decimal80 원식 값은 약 \(5.9784094667234974\times10^{-20}\ {\rm cm^3\,s^{-1}}\)이다. 이 한 원행, scale, 인쇄 식 계수는 원문 이미지와 다시 대조되어 일치했다. 해당 원문의 오차 설명에는 분모가 명시되지 않았다. 따라서 서로 다른 분모의 잔차를 기록하고 **논문 모순, 물리 불확실성 또는 source 값을 수정할 근거로 판단하지 않는다.** GL2022의 두 기준점에서는 signed 잔차가 음수이므로 표는 절댓값임을 명시한다.

## 4. 구현 보완과 실행 비용

첫 primary 실행 전에 지적된 세 가지 문제는 닫혔다. 기존 registry 파일이 하나라도 있으면 출처 load나 compiler 호출 전에 중단한다. 명령 누락은 attempt 생성 전에 거부하고, 실행 파일 부재 등 launch 오류는 실제 자원 사용과 함께 영수증에 남긴다. 모든 열의 총 cascade yield는 null로 유지한다. 최종 provider catalog 상대 경로에는 R4 leaf root라는 기준도 명시되었다.

부분 출력과 launch 오류의 실제 음성 대조는 저장된 implementation01의 28개 control에 포함되어 있다. missing-executable 영수증은 의도된 격리 검증이며 실패한 과학 계산으로 세지 않는다. C9에서는 이 검증을 반복하지 않았다.

| 실행 | child CPU s | wall s |
|---|---:|---:|
| primary01 | 0.126174 | 0.166922210003 |
| implementation01 | 0.336198 | 0.368270241001 |
| independent01 | 0.269399 | 0.272747768999 |
| plot01 | 3.423240 | 3.429062019000 |
| plot02 | 2.669490 | 2.699556759002 |

이 다섯 child의 실제 CPU 합계는 6.824501 s다. 두 plot은 저장된 점을 표시했고 새 원식 평가는 0이다. 첫 그림의 실제 exit 0과 가려진 점에 대한 visual QA를 보존했으며, 두 번째 그림은 layout만 수정했다. 이 값은 개별 child의 실제 RUSAGE_CHILDREN 변화량이다. coordinator 실행 구간 CPU는 영수증에 별도 기록되어 있으며 네트워크·도구·준비·과거 실행 및 Wolfram kernel CPU의 미측정 비용은 0으로 처리하지 않는다. 기존 PHYS91의 primary/reference/Wolfram 잔여 0은 유지되며 과거 예산의 이월이나 리셋은 없다.

## 5. 이론과 물리 admission의 경계

조건부 상태 lift, 정확 defect 식, half-spread L1 bound와 full-cone 가정 아래의 scalar closure 기준은 독립 이론검토 13개 명제의 범위에서 받아들인다. 상태별 \(d\), population, \(\pi\), 형성 분기 \(b\)가 native source와 실제 consumer에 결속되었다고 주장하지 않는다. \(b\)의 가중 결과는 사건·채널 평균이며 한 정수 event에 fractional product를 넣는 해석은 허용하지 않는다.

물리 rate, chemical/nuclear Q, heat 분배, 실제 상태 closure bound, consumer ACK, 활성화는 승인되지 않았다. HH_R10은 OFF, production은 NOT_ISSUED, L4 ready는 false다. 새로운 강한 no-go나 신규성 주장은 없다.

## 6. S08의 최종 그림과 13개 이론–코드 대응

선택된 source_fit_diagnostics_v2.png를 실제로 열어 네 panel의 native/formula marker, signed 잔차, 두 분모의 legend, 500 K peak, 두 HD 기준점, footer를 확인했다. 원식 데이터와 독립 결과는 이전에 고정한 해시를 유지한다. 그림은 29개 저장 점만 표시하며 새 fit, 보간, 외삽이나 물리 불확실성 bound를 도입하지 않는다. C9에서는 그림을 재생성하지 않았다.

LiH 온도 축은 log, HD 온도 축은 linear이고 **두 coefficient 축은 모두 log**다. 잔차의 세로축은 linear percent다. 최초 S08 그림 검토서가 HD coefficient 축을 linear라고 적은 한 문장을 발견했으며 검토자가 정정했다. 수정된 JSON SHA256은 **59ad289c8d4b3ef3f5439992ceda9a41c0fc2ed01589e7eac3d2f85291ba23f8**이다. 정정 영수증 **721b2e9eb5520bbe65dd6ef6102b43aef801c637a1ebd2246ba50fc20026e43c**에 기존 게시본의 hash·commit·ZIP을 보존했다. 그림, code, data, 과학 판정은 바꾸지 않았다.

THEORY_CODE_MAP.json의 13개 claim과 실제 함수·저장 결과·독립 근거를 대조했다. C03의 reference derivative는 이론의 의무이며 새 IVP 구현으로 표시되지 않는다. C07의 constant-d 또는 zero-h 판정에는 full-cone/fixed-lift 해석이 붙어 있다. C08의 일반 \(P\) closure와 C09의 실제 형성 분기 \(b\)는 **조건부 이론**으로 기록되며 일반 물리 solver나 state-resolved runtime 구현을 주장하지 않는다.

## 7. 구체적인 admission 후보의 승인

검토한 ADMISSION_CANDIDATE.json SHA256은 **ffc85ee587938a0e280912c61e21060a3396dddf17e9b2c792f844cac4c512ce**이고 THEORY_CODE_MAP.json은 **f7246cd8ec695ceb4c98de92fbba7d0ed45c11fa0dfe506735d7a633d3eb97ca**다. 후보의 scientific_payload를 그대로 최종 SCIENTIFIC_ADMISSION에 복사하고 이 C9 파일의 해시를 payload 밖에 결속하는 채택을 승인한다. 후보 전체의 해시와 별도로 정렬된 UTF-8 compact JSON payload의 SHA256 **34765b943cce5a67d49a622f76c0cf9aeceb635c8cd6a3cf58b5cebb8e3c5fde**도 동반 JSON에 기록했다.

후보는 native theoretical coefficient 6 variants/77셀, 13개 조건부 명제, 6개 정수 candidate, 29 native node 원식 구현만 승인한다. inherited 19 target/28 source-reference 방향과 이전 149열은 유지한다. 지표나 문서 통과를 물리적 registry 완성으로 합치지 않는다.

현재 실제 S08 DAG는 **8/24**다. root가 이 승인 후보를 실제 채택하면 WU_MOLECULAR_SOURCE_OPERATOR_CODE_R4의 한정된 계약을 닫아 **9/24**로 기록할 근거가 된다. 원 20노드의 strict complete 5와 implementation-only 2의 구별은 유지된다. 중앙 새 return ACK는 null이고 foreign owner의 노드는 수정하지 않았다.

## 8. 게시·백업 및 실행 경계

최종 검토에서 읽은 로컬 HEAD와 S09 preflight의 WU HEAD는 **3b0f1748edeae1dd49c6557ef0d443d54ef1ea6a**다. S09 preflight의 실제 관측 시각은 2026-10-27 06:30:51.856 UTC이며 AGENTS의 기존 해시는 유지된다.

S08은 expected parent **ffed56b979b2ddc7cd278579f884e1a5a2067b69**, non-force로 게시되었다. source ZIP은 1,051,234 B, SHA256 **0694b2be1c8503190700d0d9e40cf4c54761142c0b4d7233560a7dbe5c4c5be4**이며 실제 업로드 ACK는 Dropbox **id:BSpOijBcT10AAAAAAEDApA**, Drive **1-Jm4oWDVZ_buW5Lupkn-EFz4Z6Hloi2w**다. Dropbox의 첫 FETCH_FAILED는 별도 영수증에 남아 있고 동일한 불변 ZIP의 재업로드가 성공했다. 과학 계산이나 archive를 다시 만들지 않았다.

후속 checkpoint의 expected parent는 현재 S08 HEAD이며 force=false다. 이 C9는 아직 발생하지 않은 S09/S10 게시나 최종 전체 소스 ZIP의 양쪽 byte readback을 완료했다고 선언하지 않는다. source snapshot, checkpoint 업로드 ACK와 후속 delivery metadata commit은 구분한다.

본 최종 C9에서 신규 원식 평가, compiler 호출, 독립 검사 재실행, Wolfram 호출, plot 재생성, cloud 다운로드는 모두 0이다. 수행한 일은 실제 파일·그림·영수증 읽기, 해시 결속, 한 문장의 검토 metadata 정정 확인 및 이 두 검토 파일 작성이다.
