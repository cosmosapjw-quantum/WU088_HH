# WU088_HH R16: 일반 비음수 유리 삼차 forcing의 exact 전처리·동결 R15 연동

**2026-10-28 · 과학 방법론 scoped 결과 · 물리/생산 승격 없음**

## 1. 경계와 종합

R15 FINAL `ec352ac1328d59e7525530f3fc300bcf22f60f33`(DAG 31/46, workflow20/20)을 원천으로 고정했다. 이 대화에서 사용자가 계속 진행하도록 지시한 R16는 원래 4개 Bernstein-B3 계수가 모두 비음수여야 한다는 R15의 좁은 범위를, **다항식 전체가 [0,1]에서 비음수이지만 일부 B3 계수는 음수인 유리 삼차식**으로 확장한다. 기존 R15 검증 302/302·reference302/302·CAS72/72는 재실행하지 않고, 새 R16 전처리와 동결 R15 코어를 정확히 연결했다.

이전 답변에서 확인한 접근 가능한 branch 2,430개와 PR 1,196개를 현재 요청의 입력 조사로 재사용한다. 새 전수조사를 반복하지 않았다. 해당 결과는 비원자적 최신 조사이며 전체 대화 본문 접근을 보장하지 않는다. 새 원전 중 **EMAA HD rovibration dataset DOI 10.17178/emaa_hd_rovibration_805a7aa5**는 H+ 충돌 171개 전이·25개 온도라는 dataset 설명을 제공한다. 원 데이터 bytes/상태·단위/consumer binding을 실제 확보하지 않았으므로 여전히 물리 INPUT_PENDING이다. 원 논문은 González-Lezana·Hily-Blant·Faure, JCP 157 214302 (2022), DOI 10.1063/5.0128598. 관련 전처리 문헌은 Harris–Parrilo arXiv:2309.10675의 cubic 비음수 cone과 Bernstein 양수 cone 구별이다. 이러한 문헌은 방법의 배경이며 R16 자체의 수학 검증을 대신하지 않는다.

## 2. 결과와 적용 범위

[theory/PROOF_KO.md](theory/PROOF_KO.md)는 `p(u)=Σ b_i B_i^3(u)`의 정확한 비음수 판정(끝점과 도함수 실수근의 algebraic sign), 내부 이중 영점의 유리성, exact rational split 후 모든 수용 다항식을 nonnegative Bernstein-B3 piece로 만드는 유한 종료의 수학적 증명을 포함한다. 다만 *임의 입력에 대한 256 깊이·16,384 방문의 성공 보증은 없다*. Resource cap에서 끝나면 `ResourceExceeded`를 반환하고 물리·수학적 불가능 판정으로 바꾸지 않는다.

[src/r16_nonnegative_cubic.py](src/r16_nonnegative_cubic.py)는 Fraction 기반으로 이를 구현한다. 입력 256bit/파생16384bit, 기본 dyadic depth256, row별 node16384, R15 변환 후 원 source cell 최대16으로 제한한다. `g_r,g_e` 양 채널의 실제 split knot 합집합에서 원 함수를 정확한 affine de Casteljau restriction으로 재표현한다. 원 hash를 검사하고 새 whole-forcing canonical hash를 생성하되, 원 native source SHA·state order·clock·full-A family와 flags는 변경하지 않는다.

[src/r16_cli.py](src/r16_cli.py)는 R15 original Git blob `0a95d907790cbf87207deb32c9a9ab1ae24aa3a1`를 검증한 뒤 원본 `validate`/`run_case`를 실제 호출한다. 입력 전제의 참은 새 물리 실험이 아니라 사용자가 공급한 자료·certificate에 의존한다. `source_sha256='ffff...'`를 쓴 산술 시험은 물리 HD 자료가 아니다.

## 3. 실제 실행 근거와 실패 보존

- 이전 대량 SymPy 1,500 사례 실행은 **시간 제한으로 중단**되어 통과로 세지 않았다. 축소된 경계 사례 19개와 결정론적 무작위 220개를 SymPy 독립 기호식/임계점/조각별 항등식으로 검산: **239개 PASS**, 이 중 random 33개 비음수·187개 음성. 입력 타입·source digest·source-cell budget의 음성 테스트도 통과.
- 복원된 R15 FINAL source ZIP **1,643,598바이트**, SHA256 `e8d65ee595b346550d14dbfb9d3876553326c6bd2fc2bee1dd4ab04415aaa246`, ZIP CRC PASS. R15 core Git blob 해시 직접 검산 PASS.
- **실제 R15 원본 연동**: `(t-1/3)^2`의 원 B3 `(+1/9,-1/9,0,+4/9)`를 2개 셀로 분할, R15 `validate+run_case` exit0. `q=1, d_c=0, R0=E0=0, c=1, g_e=0`에서 exact `R(1)=1/9`, `E(1)=1/36`을 바깥쪽 R15 interval이 포함하며 E interval 폭은 `2^-127`이다.
- Wolfram 첫 제출은 변수 치환이 잘못된 **검증 스크립트 오류(8/18)**. 교정된 [theory/WOLFRAM_EXACT_CHECK.wl](theory/WOLFRAM_EXACT_CHECK.wl)은 6개의 독립 rational B3 제어계수 행 × (left/right 제한 항등식, Simpson 적분) = **18/18 exact-zero**, 반환된 nonzero {}. 첫 결과를 삭제하거나 첫 실행부터 18/18이었다고 보고하지 않는다.
- 그림 [figures/R16_B3_SIGNED_PREPROCESSING.svg](figures/R16_B3_SIGNED_PREPROCESSING.svg) (PNG는 local source ZIP에도 수록)을 실제 열어 확인했다. 원본 B3 control 값은 곡선의 표본이 아님을 그림에 표시하며 원본 음수값과 분할된 비음수값을 구분한다.
- 소규모 외부 runtime: Python 3.13.5, Linux 6.18.55, C++ g++14.2 probe 통과. 새 ODE=0. 기존 완료 R15 core의 source 수정·다시 전체 테스트=0.

## 4. 감사와 채택

**Physics/math:** p의 비음수 구간 판정, interior double root의 rational 성질, zero-aware dyadic 종료, 정확한 분할 동일성은 제시한 가정 아래 직접 유도. 서명·단위·IC·BC는 전처리로 바뀌지 않는다. 생산 numeric tolerance를 풀지 않는다.

**Math/code:** independent SymPy algebraic sign/explicit polynomial equality, Wolfram corrected18/18, actual old R15 `validate/run_case`, malformed/hash/bit/depth/source-cell guard, create-only output을 확인했다. `r16_nonnegative_cubic.py`의 출력 생성은 중간 감사에서 atomic `'x'` mode로 교정했다. 이 변경 후 targeted 239개 test는 다시 통과했고 이미 저장된 원 R15 결과는 변경하지 않았다. 동일 세션 자체 감사를 독립 blind subagent라고 부르지 않는다. `native_subagent=NOT_RUN`, fresh-context blind review도 NOT_RUN.

**Adoption:** WU local scoped *theory+code method* 두 노드를 추가하는 과학 판정은 31/46 → 새 OPEN 31/48 → **scoped 채택 33/48**이다. 부모 46개 노드 내용 동일. 중앙/물리 DAG 증분0; actual HD reactive state-to-state array, named physical consumer/density/clock은 INPUT_PENDING, `native_v=UNSPECIFIED`, `MISSING_NOT_ZERO`, `TIQM/SQM DISTINCT`, `HH_R10=OFF`, `production=NOT_ISSUED`, `L4=false`다. R16의 all-rational-cubic 수학적 종료와 fixed resource cap의 수용 범위를 동일시하지 않는다.

## 5. 전달·게시 상태

GitHub Direct CLI는 현재 컨테이너의 DNS 실패. Connector API를 통한 원격 source 게시 시도와 별도 Library 저장을 수행한다. 연결된 Google Drive·Dropbox의 파일 업로드 어댑터는 새 로컬 파일 경로/단순 file_id를 수용하지 않아 직접 ZIP 이중 업로드는 지원되지 않는 것으로 관측됐다. Library 백업은 별도이며 **이것을 Drive·Dropbox 이중백업 완료로 기록하지 않는다**. [WORKFLOW_RECORD.json](WORKFLOW_RECORD.json)에는 R1..R10/C1..C10 각 완료 범위(2/20…20/20), DAG(31/48→33/48), 실제 게시/백업 ACK를 별도로 기록한다. 게시/백업에 실패했다면 code/science 통과와 구분해 `DELIVERY_PENDING`으로 남긴다.

다음 실행 의무는 실제 **GL2022/EMAA native reactive bytes**와 named consumer/state/density/clock를 확인해 새로운 원본·consumer identity로 결속하는 것이다. 자료 확보 없이 polynomial degree를 다시 올리는 메타 확장보다 과학적 효용이 크다. 재개 명령과 신원 정보는 [HANDOFF_KO.md](HANDOFF_KO.md)에 있다.
