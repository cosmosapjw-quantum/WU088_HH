# REI의 실제 이동분만 확인한 R13 종료 시점 의존성 기록

`cosmosapjw-quantum/rei_bianchi`의 `research/rei-causal-prefix-consumer-20261027`은 기존 census의 `b77c7b8d45c48a7e4722e733309430d5ba668b0d`에서 `ebf59d21fb7d97a3c6cf01c1af12a7afbc671f7d`로 이동했다. 새 tree는 `a1e4502af1428cb6271034c335aa11c5e5363bd3`다. Root의 별도 seven-ref GET에서 확인된 이 이동분만 조사했으며, 다른 여섯 ref나 전체 저장소 조사를 반복하지 않았다.

이 변경은 **7개 commit, 7개 경로(수정 1, 추가 6)**다. 새 HD reactive array 또는 WU의 이름이 결속된 물리 consumer·density·clock은 이 변경에서 제공되지 않았다. 해당 결론은 조사한 변경 자료에 한정하며, 전역 자료 부재를 주장하지 않는다.

## 실제로 새로 기록된 사항

REI `finite_thermal_endpoint_20261028`의 별도 native reviewer가 두 단계에 걸쳐 기존 C6–C8 증거와 정확 유리수 구현을 검토하고, F1 한 건의 표현식 교정을 확인했다. 새 `REVIEW_RESULT.json`은 **R6 `pass_scoped`, C9 `pass_scoped`**, 해당 unit의 진도를 **13/20 → 15/20**으로 기록한다. 구성은 이론 **6/10**, 코딩 **9/10**이며 남은 단계는 R7–R10과 C10이다. 이는 새 source가 보고한 진도이며, 이 조사에서 REI DAG를 다시 세지 않았다. 같은 기록의 working DAG **33/88**, central 마지막 관측 **28/88**, canonical delta **0**은 유지된다.

유일한 기존 파일 변경은 source-bath 문서의 온도 변환식이다. 별도로 표현된 값을 \(\theta,k,t\)라 두고 \(\rho_\theta=\theta-kt\)를 보존하여

\[
\frac{T_a^E}{t}=\frac{k\,\mathrm{EV}}{k_B^{SI}}+
\frac{\rho_\theta\,\mathrm{EV}}{k_B^{SI}t}
\]

로 교정했다. 짧은 식은 \(\rho_\theta=0\) 또는 반올림 전 모형이라는 전제에서만 성립한다고 명시한다. 실제 base/head 문서 diff는 이 단락과 교정 경위에 한정되고, production code 변경은 없다. Source는 기존 C7의 저장값을 이용한 targeted exact-rational check **1회**, 기존 suite·source replay·CAS·IVP 추가 **0회**를 기록한다. 이 조사는 해당 계산을 재실행하지 않았다.

나머지 여섯 새 경로는 Phase 1/2 심사, F1 종결, 결과 기록과 audit capsule/index다. Capsule은 **61개 payload**를 보존한다. C8 primary의 81 checks와 companion의 158 checks는 한 C8 단계에 대한 서로 다른 기존 증거로 유지되며 합산하여 추가 단계로 세지 않는다. Source의 고정 BASS 과학 pin은 `634c3046ffccc5d00f1ab7588b5834a6eb8053ad`다.

## WU 입력 결속에 미치는 영향

새 심사 결과는 고정된 BASS atomic finite-caloric transaction의 조건부 source-model 진단이다. Literal binding의 NH와 clock도 source의 값이며 실제 WU 수신자 density/clock이 아니다. 새 결과의 물리 경계는 actual REI temperature, native25, physical radii가 `null`, self-consistent thermal feedback은 `false`, L4는 `false`다. 이를 WU 물리 결속으로 올리지 않는다.

따라서 WU의 actual HD array 및 named physical consumer/density/clock은 **`INPUT_PENDING`**, 이 의존성 이동에 의한 WU scientific/physical delta는 **0**이다. 진행한 R13의 고정 계약·코드·실행 결과를 바꿀 이유는 이 변경에서 발견되지 않았다.

## 읽은 범위와 identity

취득 시작은 **2026-10-28 17:34:54 KST**, immutable source 취득 종료는 **17:36:44 KST 이전**이다. Head의 AGENTS 전체, 7개 변경 파일 전체 bytes와 수정 파일의 base bytes를 확보했다. **9개 source snapshot 모두 재계산 Git blob과 서버가 돌려준 blob이 일치**한다. 결과·F1 종결은 전체를 읽었고, 긴 Phase 1/2와 capsule은 판정·F1·물리 범위·payload inventory 및 필요한 literal binding을 읽었다. 61개 내장 과학 payload 전체를 새로 독립 심사했다고 주장하지 않는다.

정확한 경로, Git blob, SHA-256, 읽은 범위는 `SOURCE_IDENTITIES.json`에 있다. `COMPARE_METADATA.json`은 immutable base/head 비교 결과이고, `F1_DOCUMENT_DELTA.diff`는 직접 비교한 변경 단락이다. 소스 원문과 connector 응답은 로컬 조사 기록으로 보존했으며, 이 공개 요약은 필요한 identity와 범위만 담는다.

이 작업의 과학 실행·import·CAS·remote mutation은 모두 **0**이다. 기존 census의 독립 재심사 또는 R11/R12 과학 심사는 수행하지 않았다.
