# PHYS89 독립 C9 — 실제 결과의 한정 채택

## 판정

**PASS_SCOPED_SOURCE_DIAGNOSTIC_AND_TYPED_FINITE_INTERFACE**를 채택한다. 고정 ENDF MF33 표시 행렬의 정확한 PSD 반례와 finite functional/소비자 bookkeeping 인터페이스의 한정 구현 검증이 완료됐다. 선택 물리 노드와 원 actual atomic-to-bare/physical finite-T supplier는 `PARTIAL_INPUT_DEPENDENCIES`를 유지한다.

- Primary scientific identity: `c688ab6b06ab1e94781645e174cd555423ba49fc15d6b76c31acef3890f2e8b2`.
- 별도 독립 checker identity: `0f946ef3e6d2253091e50f4bdfca708ce9900a93677d0793367510b5ee2111b5`.

검토자는 원 R6와 static 검토를 재사용하고, 실제 primary·실패한 원 reference·별도 repair1·resume의 원 영수증과 payload를 읽었다. 명령/lease/admission/identity/hash를 대조했으며 과학 코드를 다시 실행하지 않았다.

## 실제 source 결과와 정확한 반례

별도 parser는 원154boundaries,11781packed values,23409matrix entries 및 모든 raw token bytes를 정확히 일치시켰다. MF33의153groups를 MF3의153knots/152cells와 혼동하지 않았다. SOURCE_TABLE에 저장된 zero-based group0,10의 블록은

\[
F_{\{0,10\}}=\begin{pmatrix}a&a\\a&a-d\end{pmatrix},\qquad
 a=4.278572\times10^{-4},\quad d=10^{-10}.
\]

따라서 \(\det F_{\{0,10\}}=-ad=-1069643/25000000000000000000<0\)이다. 독립 checker가 원 source를 다시 decode하여 이 exact Fraction minor를 확인했다. 저장된 같은 두 항에 대해 \(w=e_0-e_{10}\)이면

\[
w^T Fw=a+(a-d)-2a=-10^{-10},\qquad
\frac{w^TFw}{w^Tw}=-5\times10^{-11}.
\]

이 직접 대수를 확인했고 최소 eigenvalue에 대한 해당 상계도 따른다. Group0은 sigma support와[1e-5,1.5e-5)eV에서 겹치며, group10은[0.01765,0.06265)eV다. 둘 다 유효 sigma support에 걸치므로 바깥쪽 covariance row만 골라 생긴 반례가 아니다.

원 표시 F를 확률 covariance로 채택하면 이 방향의 분산이 음수여야 하므로 **현재 표시 행렬의 stochastic covariance admission은 DISALLOWED**다. 이 판정은 underlying full-precision covariance, evaluator 전체, 또는 physical model을 배제하지 않는다. 한 번의 binary64 eigensolve 및72개 음수 진단값은 interval spectral-count certificate가 아니다. 채택 근거는 위 exact minor와 quadratic form이다.

F는 projection, jitter, clipping 없이 보존됐다. ULP/반ULP는 nearest-rounding 가정 아래의 형식적 상자이며 실제 formatter나 physical uncertainty를 보증하지 않는다. 원인 상태는 `NOT_ESTABLISHED`다. COMMARA-2.0/2011에서 현재153group 및 nominal evaluation으로의 변환 관계가 미결이라는 원전 조사도 source-input 의무로 유지한다. 이를 다른 provenance라는 이유만으로 추가 오류라고 단정하지 않았다. Strong no-go 성과는 `NOT_CLAIMED`다.

## 구현 및 독립 검증

| 범위 | 실제 결과 |
|---|---|
| Primary | 1회 성공,27/27checks, 그중15guards |
| 원 independent reference | blank ENDF control을 int로 변환하다 exit1; scientific comparisons 전에 실패 |
| 별도 reference repair1 | 1회 PASS_EXACT,154boundaries/11781tokens/23409entries, 모든 exact fixture 값 일치 |
| Float 대 exact fixture | 117개 비교, 기존 abs5e-15+rel5e-13 기준 유지 |
| Primary/eigen 재실행 | 0 |
| 실제 read-only resume | primary와 repair1 각각1회 SKIP,22hash 불변, pycache전후빈집합 |

Manufactured three-group PSD fixture는 LFLᵀ/BFBᵀ, 정규화의 exact finite change와 remainder, 같은 사건의 signed energy/particle-count/caloric 소유권, proper/coordinate clock, reference density, SI 변환을 검사한다. 이는 실제 nuclear thermal group weights나 physical source CI가 아니다. 입사 n,p의 thermal 소유, positive C_V, capture-only temperature contribution이 적용 범위다.

원 reference의 실패와 첫 static 검토가 그 blank-control 경로를 놓친 사실을 보존했다. 별도 repair1은 selector와 별도 identity 결속만 바꾸었고 numerical parser/fixture/comparison/tolerance 함수는 원본과 동일하다. 원7개 freeze와 성공한 primary 전체 bytes가 유지됐으므로 primary 재실행은 필요하지 않았다. P89-R6R-01 및 P89-Cpre-01/02/03과 실제 selector 실패의 한정 복구는 모두 닫혔다. 새 material scoped finding은 없다.

## 자원·실패·예산

실제 bounded child는3개=성공2+보존실패1이다. 합계 child CPU는0.41658999999999996s, launch-inclusive child wall은0.4201385129999835s, coordinator CPU는0.07300099999999998s다. Wrapper 전 metadata launcher의 TypeError1은 wrapper0/child0의 별도 실패다.

두 resume는 metadata-only CPU0.06936s 및 wall0.06991689699498238s로 별도 계상한다. Callback/integral/rewrite0, 새로운 pycache0을 실제 영수증과22개 현재 파일 hash로 확인했다. 모든 scientific child는 원 shared lease·fresh memory와 CPU0/8,1worker/thread,20CPU/45wall 범위를 유지했으며 다른 process 종료는0이다.

Primary/원 reference/별도 repair1/Wolfram 잔여 허용량은 모두0, automatic retry0, budget reset=false다. PHYS88의 불변 원 ledger, PDF shortening 원인NOT_ESTABLISHED와 정확한 bytes 복구, 실패 child 및 all_zero=False를 유지한다. PHYS89 중단 전 Wolfram evaluator1 성공/7zeros 및 context SERVICE_ERROR1은 transcript 근거이며 원 raw bytes가 현재 없다는 한계와 함께 보존한다. 재호출은0이고 symbolic lineage는8calls다. 전체 역사·원격 CPU/금액/전역 잔여예산은null이다.

## 물리·전달 경계와 다음 의무

Actual evaluator mass deck와 invariant-s 대응, electron/target-state validity, current nominal에 결속된 유효 covariance/원 precision, full-support tail의 mass·moment bound, 이름 있는 thermal/fast/radiation consumer 구현과 ACK가 필요하다. REI-L2의 원 beta 범위는 바뀌지 않았으며 capture 확장은PROPOSED_UNIMPLEMENTED, BASS nuclear consumer는NOT_BOUND다.

HH_R10=OFF, production NOT_ISSUED, 전역 물리 완료율null. 새 ODE/적분/benchmark/nuclear activation/fast stopping은 모두0이다. 이 C9는 한정 과학·구현 판정이며 S2/FINAL의 Git 게시, 단계 ACK, 최종 wholeGET·CRC·payloadSHA·Git identity·실제 추출 및 중앙 관측의 완료를 대신하지 않는다. 완료된 identity를 더 검사하거나 재실행하지 말고 실제 전달과 남은 source-input 의무로 이동한다.
