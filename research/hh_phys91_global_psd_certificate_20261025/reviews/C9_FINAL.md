# PHYS91 C9 최종 독립 검토

**판정: PASS_SCOPED_EXACT_GLOBAL_PSD_DISTANCE_B1_UNRESOLVED. C9 COMPLETE_SCOPED.**

Primary1, independent reference1, 실제 metadata-only resume 각1회 및 원 PNG/PDF를 같은 C9 pass에서 확인했다. Blocking finding0, 열린 finding0, 코드 repair0이다. 실행 전 C9_PREEXEC의 원본은 유지한다. 이 판정은 전체153행렬의 조건부 PSD distance enclosure를 채택하며, B1의 PSD 존재 또는 부재는 여전히 **OPEN**이다.

## 1. 실제 결과와 정확한 해석

F/H와8개 frozen files의 scientific identity는 **4b7e3ce80c6a96373e4f0f214d63c12738d2ab5f71b9f83bc01cfbaf5bb5c376**이다. 실제 실행 S1 HEAD는 c9eaf283c227157067d27cecd672033d795bbe68, tree4e2bd383ce1afecb0bf7669f70bd02340ca11629다. R6에서 검토한 CONTRACT/theory와 모든 frozen source SHA는 그대로다.

인증된 전역 거리 구간은 양 끝을 포함하여

```
[606934757065126340229833497971012560 /
 1044859134592536248071098889705557947,

 1210812737265140594067745 /
 1208925819614629174706176]
```

이다. 새 lower는 exact PSD dual에서 얻은 closed endpoint다. PHYS90의 별도 strict lower34406736621/68719476736도 그대로 유지하며, 그 pair upper를 전체 PSD upper로 사용하지 않았다. 실제로 beta<1<alpha이므로 alpha<=1 또는 beta>1의 어느 admission 조건도 성립하지 않는다.

4096changed-candidate projections와16exact checkpoints는 사전 동결된 두2048회 stage의 정상 종료다. 이는 bounded search의 허용된 unresolved 결과이며 algorithm error, B1 존재/부재 증명 또는 물리적 no-go로 분류하지 않는다. 유효한 전체 거리 enclosure를 얻은 성과와 남은 B1 질문을 분리한다.

선택 dual은 checkpoint4의88열 factor, primal은 checkpoint13의65열 factor이고 maximal entry-error witness는 zero-based(22,74)다. 결과의 원 rank 필드는 factor 열 개수를 기록한다. Quantized Gram의 정확한 선형대수 rank나 padding을 더한 최종 C의 rank를 별도로 계산한 값은 아니다. 이 **비차단 표현 문제는 여기서 의미를 명확히 하여 닫았으며**, 원 코드와 결과 bytes를 고치거나 새 계산을 하지 않는다.

## 2. 독립 reference와 수용 근거

독립 reference는 PASS_EXACT_SELECTED_CERTIFICATES로 종료했다. Kernel/primary import0, candidate generation0, eigensolve0이며 standard-library integer/Fraction 경로로 선택된 두 인증서를 검증했다.

- 선택 primal: 모든11781upper entries, exact padding·alpha·witness·inclusive endpoint.
- 선택 dual: 전체 Gram을 먼저 합한 뒤의 signed trace와 absolute support, exact beta와 strict B1 기준.
- 합성 구간: inherited lower의 openness, exact contradiction 부재와 최종 B1_UNRESOLVED.
- 모든16checkpoints: 실제 원문 SHA·metadata·저장 scalar min/max 선택의 결속.
- 독립20boolean fixtures PASS 및 forest16sign cases. 모든 rank-one에 대한 명제는 재사용한 이론의 forest proof에 근거한다.

선택하지 않은 모든 checkpoint factor를 독립 재계산했다는 주장은 하지 않는다. Primary가 각 checkpoint를 exact 검증했고 reference가 최종 선택된 두 endpoint를 독립 검증한 범위다. Reviewer는 factor나 scientific fixture를 다시 실행하지 않았다.

## 3. 실제 자원 및 resume

| 실행 | 횟수 / exit | CPU seconds | Wall seconds | 고정 cap |
|---|---|---:|---:|---|
| Primary | 1 / 0 | 13.679209 | 13.693714398999873 | CPU60 / wall90 |
| Reference | 1 / 0 | 0.571149 | 0.5727001010000095 | CPU30 / wall45 |

Scientific child 합계CPU14.250358s, wall14.266414499999883s다. 두 wrapper coordinator의 CPU0.05050599999999999s는 별도다. Original shared lease, CPU0/8, one worker/thread, fresh reserve1.5GiB+job0.5GiB, 두 own lease 해제, retry0와 다른 process 종료0을 실제 receipts에서 확인했다.

Primary/reference resume는 각각 실제1회, exit0, SKIP_COMPLETE_READ_ONLY, scientific imports/callbacks/writes 각각0이다. 전후25개 payload/manifest, 총9110118bytes의 SHA와 size가 모두 같다. 이 metadata 비용CPU0.091248s/wall0.09206515599998966s는 scientific child 비용과 분리한다.

두 새 scientific allowance는 모두 소진됐고 reset=false다. 이전 완료 allowance도0이며 관측하지 않은 전체 역사·remote 비용과 잔여 global budget은 null을 유지한다.

## 4. 원 그림 열람

원 PNG와 PDF의1page를 실제 시각적으로 확인했다. PDF는518.4×302.4points,17897bytes이며 임시 PNG로 한 번 렌더링해 열람했다. 제목·축·16checkpoints·두 bound 곡선·B1 범례가 완전하게 보이고 clipping·누락·읽기 어려운 glyph가 없다.

원 PNG67161bytes의 SHA는 ba2a1ef466af73aaa53aa2ace835ce703b954f069f3220fa56e083fb7dc1175d, 원 PDF의 SHA는9f04af1270d0662b9b5e42ac8d02db3e948cde3d6ffba912c4ea776886fc5c4e다. 열람 후 primary manifest의 원 SHA와 일치했다. Plot 재생성·수정은0이다. 그림은 decimal overview이며1에 가까워 보인다는 인상으로 B1을 판정하지 않는다.

## 5. 물리적 한계와 다음 전이

이 결과는 conditional halfULP closed cell에 대한 수학적 인증이다. 실제 formatter guarantee, physical CI, source covariance 채택·repair, actual nuclear kernel/mass/target-state/tail/consumer ACK를 발급하지 않는다. Parent PARTIAL_INPUT_DEPENDENCIES, source cause NOT_ESTABLISHED, HH_R10 OFF, production NOT_ISSUED, global physical completion null이 유지된다.

**Root가 이 scope로 scientific admission과 S2 게시를 진행할 수 있다.** 추가 과학 실행, projection, reference 재실행, resume 반복이나 그림 생성은 요구하지 않는다. 남은 작업은 승인된 보고·배송·인계다. Reviewer의 실행은 원문 읽기, metadata SHA, 원 PDF 읽기 전용 렌더링1회와 이 검토문 작성에 한정됐다.
