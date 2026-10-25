# PHYS90 독립 C9 최종 검토

## 판정과 결속

**`PASS_SCOPED_CONDITIONAL_COVARIANCE_CELL_AND_CONSUMER_ENVELOPE`**.

유한 자식 `COVARIANCE_FORMATTING_CELL_AND_MATCHED_CONSUMER_ENVELOPE`의 동결 이론·코드, 새 exact pair 결과, 별도 reference, 제조된 공통 소비자 fixture와 실제 readonly resume를 수용한다. 선택 부모 `NUCLEAR_BARE_KERNEL_SOURCE_AND_CONSUMER_CONTRACT`는 `PARTIAL_INPUT_DEPENDENCIES`다.

| 결속 대상 | 실제 identity |
|---|---|
| Scientific identity | `a7107870ad5a66e3bb602115f1068ca7366444b42c539e1a6b4b83da2037513a` |
| Frozen execution HEAD | `298aebe3889011d8a7f48a454cf18d1a98c8f54c` |
| Frozen execution tree | `e67be32177ec3d64d91b8ad695f0a7fa0676ef4d` |
| Contract SHA-256 | `45d7b94544cf801619aa723c79be35c05e3ca2b023e2e94e8985f4c20758a20c` |
| Primary manifest SHA-256 | `af271a4891d0875949f58899022c6d57b3a32e97af2beecce1a4351b303718b0` |
| Reference manifest SHA-256 | `c88111f4d600f076c94d1a1c1cb841b4f8cce3cfd7390a04c617adcfc0ad4c44` |

검토자는 앞선 독립 R6와 preexec 정적 검토를 재사용하고, 실제 산출물·실행·resume 원문과 PNG를 읽었다. 별도 metadata-only SHA 대조에서 frozen7/7, cached inputs2/2, 과학 payload7/7가 일치했으며 canonical binding의 SHA가 기록된 scientific identity와 같다. 이 검사는 `C9_IDENTITY_READBACK.json`에 있다. Scientific module import, callback 또는 과학 재실행은0이다.

## 새 exact 결과

153 singleton,11628 unordered pair에 대해 t=0에서는 singleton 실패0·pair 실패74, t=1에서는 singleton과 pair 실패 모두0이다. 모든 t=1 pair의 통과는 실제153차원 closed box의 전체 PSD 존재를 결정하지 않는다. 원 출력의 `at_t1_full_PSD_compatibility=UNRESOLVED`, `t1_witness=null`, `full_PSD_threshold=UNRESOLVED`는 이 범위와 일치한다.

Pairwise feasibility threshold는 다음 exact 구간으로 결속됐다.

\[
t_{\rm pair}\in\left(
\frac{34406736621}{68719476736},
\frac{550507785937}{1099511627776}
\right],\qquad
\text{width}=2^{-40}.
\]

하단에서는 zero-based pair(10,16)가 실패한다. 해당 cell에서 가능한 최대 determinant는

\[
-\frac{23113}{549755813888000000000000000000}<0.
\]

상단은 모든 singleton·pair를 통과한다. 따라서 lo는 전체 PSD가 가능해질 반경의 엄격한 하계이고, hi는 pairwise threshold의 상계다. 전체 PSD threshold의 상계나 실제 covariance 수정량을 계산했다고 해석하지 않는다.

기존0,10 block에서 새로 계산한 최소 pair radius `8557144/17114287`는 R6의 새 symbolic 식과 일치한다. 기존 sparse probe 중심 `−1/10^10`와 `1069643/2500000000`는 `REUSED_PARENT_EXACT_VALUE`로 표시됐다. 새 계산은 각 방향의 formatting-cell support이며, 부모 exact witness를 새 발견으로 세지 않는다. 새 t=0 결과74는 전체 pair 집계이고 기존 PHYS89의 negative eigenvalue 진단72와 다른 객체다.

## 독립성·보존·경계 검증

Reference는 production kernel을 import하지 않는 별도 per-pair integer/Fraction 구현으로42개 저장 checkpoint 각각의11628pair와153singleton을 비교했다. 전체 t=0/1 실패 목록, 최종 bracket·witness, 새0,10 radius식, 제조8vertices와9support entries가 exact 일치했다. 결과는 `PASS_EXACT_INDEPENDENT_REFERENCE`다.

제조2×2 fixture는 shared off-diagonal cancellation으로 support2를 얻고, 개별 variance maxima12/12와 joint maximum20을 구별했다. 같은 source C의3-row map에서 보존된 q에 대해 Kq=0가 모든8vertices에서 확인됐다. 독립 covariance mutation 및 공동으로 불가능한 marginal maxima를 거부했다. 제조3×3 fixture는 pair 전체 통과와 global upper quadratic−21/10을 동시에 확인해 pair/global claim 구분을 검증했다. 이 fixture의 결과를 actual consumer owner 승인으로 올리지 않는다.

15개 guard가 모두 true다. Preexec finding `P90-C9-01`의 radius1 classification 교정은 동결 전 완료됐고 실제 출력의 all-pass branch도 정확하다. R6의 네 정의·범위 정밀화 사항과 C9 preexec의 단일 finding에 남은 blocking 항목은 없다.

Wolfram 원 입력과 원 응답도 읽었다. 이번 새 식의 evaluator 응답은 scalar residual9개가0, `all_zero=true`, positive-off branch=true다. 이전 PHYS88의 all_zero=false 이력과 다른 호출이며 그 이력을 바꾸지 않는다.

## 실행·실패·재개

첫 wrapper attempt는 PID namespace와 procfs namespace가 달라 자기 lease를 live로 읽지 못했다. 원 receipt의 child_invocations=0이며 scientific allowance를 소비하지 않았다. `PID_NAMESPACE_DIAGNOSTIC_0/1.json`은 기본 실행의 local PID와 `/proc/self` PID가 다르고 host PID 경계에서는 일치함을 직접 보여 준다. 원 frozen wrapper·vendor SHA·lease API와 경로를 유지한 host-PID 실행이 사용됐으며 os proxy, gate 수정 또는 peer 종료가 없었다. 최초 WAIT summary는 `execution/WAIT_EXECUTION_SUMMARY.json`에 보존되고 새 summary는 이후 성공 영수증을 연결한다.

| 실제 실행 | 결과 | child CPU s | launch wall s |
|---|---|---:|---:|
| Primary wrapper attempt1 | WAIT, child0 | 0 | scientific child 없음 |
| Primary actual child1, attempt2 | exit0 | 2.515446 | 2.517889031005325 |
| Independent reference child1 | exit0 | 0.398554 | 0.39987449599721003 |

과학 child 합계는2개 성공, CPU `2.9139999999999997`s, wall `2.917763527002535`s다. 실제 receipt의 수치 표기를 보존한다. Wrapper coordinator CPU 합계 `0.07425899999999999`s는 별도다. 두 성공 직전 own live lease1개, peer 관측0, fresh memory reserve+job 통과, coordinatorCPU8와 childCPU0 강제 경로를 확인했다. 종료 후 own lease가 해제됐다.

Primary와 reference를 각각 한 번 실제 `--resume`했다. 둘 다 `SKIP_COMPLETE_READ_ONLY`, scientific imports0/callbacks0/writes0이다. Before/after9files,98,380bytes의 크기와 SHA가 같으며 두 snapshot JSON의 원bytes SHA도 같다. Resume CPU합계0.063894s, wall합계0.06465108200791292s는 과학 child 비용과 분리한다. 추가 scientific replay와 automatic retry는0, 소진된 과거 allowance는0, budget reset=false다.

## 그림과 산출물

실제 PNG를 시각적으로 읽었다. 축과 라벨은 읽을 수 있고 t=0의74실패에서 t≈0.5 부근의 판정 전환, t=1의0실패를 보여 준다. 제목이 checkpoint 그림임을 밝히고 전체 PSD 인증과의 구분을 표기한다. Step segment는42개 exact checkpoint 사이를 잇는 표시용 연결선이며 각 구간의 전체 실패 개수가 일정하다는 continuum certificate로 읽지 않는다. 정량적 threshold는 원 exact bracket으로 판단한다.

PNG는51,634bytes/SHA `1d1fb66b705f5f4c5262d5b6567ecd8840e7d6e49944a1fa20efa7ede94cae14`, PDF는16,603bytes/SHA `531fa51c7df274b44616f1384e30cefa887869e598d89555785d032c035b26a5`다. 두 파일 모두 같은 단일 primary 안에서 생성돼 manifest와 resume에 결속됐다. PNG만 시각 검사했고 PDF는 바이트 identity를 확인했다. 이 검토에서 그림을 다시 생성하지 않았다.

## 수용 범위와 남은 의무

이번 finite child의 이론·구현·정확한 유한 결과를 수용한다. 실제 formatter의 nearest-rounding 보증, actual full153 PSD candidate 또는 separator, current nominal과 원 precision source의 결속, nuclear mass/electron/target state·differential kernel·tail, named thermal/fast/radiation consumer 구현·ACK는 부모 의무로 남는다. 원 표시 행렬의 결함 원인 `NOT_ESTABLISHED`는 유지한다.

새 ENDF decode0/eigh0/old callback0/integral0/ODE0/benchmark0/nuclear activation0/fast stopping0이다. HH_R10=OFF, production=NOT_ISSUED, global physical completion=null이다. 전체 역사·원격 CPU·금액·잔여 global budget 미관측량은null이다. Final Git publication과 dual-provider wholeGET/CRC/payloadSHA/Git identity/actual extraction은 별도 delivery 영수증으로 완료해야 하며 이 C9 판정으로 그 미래 작업을 완료 처리하지 않는다.
