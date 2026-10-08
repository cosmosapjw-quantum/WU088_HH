# F1M 직접 source intake continuation

원 F1M ZIP의 source-lock 누락1개를 원 F1P ZIP의 exact manifest로 결속한다. 전체 과학/소비자 적용 승인은 별개다. 자세한 결과는 WORK_REPORT_KO.md, 직접17개 증거는 evidence/SOURCE_CLOSURE.json이다.

검증은 stdlib archive/hash read-only 경로이며 bundle의 science module을 import/execute하지 않는다. Cache의 원 bytes를 사용한다:

```sh
python3 -B verify_f1m_intake.py --f1m /root/.cache/WU088_HH/sha256/18/6e/186e1169a7265a8b83108dab654f9e40d1817c790d6a3c234ec2c27514fa91e0 --f1p /root/.cache/WU088_HH/sha256/35/e6/35e64c16be7d8fda86f4f2b35a88fdffd0d7721276e92316f4371ae35a14c8d1
WU088_F1M_ZIP=/root/.cache/WU088_HH/sha256/18/6e/186e1169a7265a8b83108dab654f9e40d1817c790d6a3c234ec2c27514fa91e0 WU088_F1P_ZIP=/root/.cache/WU088_HH/sha256/35/e6/35e64c16be7d8fda86f4f2b35a88fdffd0d7721276e92316f4371ae35a14c8d1 python3 -B -m unittest test_intake -v
```

F1M만 주는 경우 예상exit2(SOURCE_CLOSURE_INCOMPLETE)다. 다른 archive bytes는 거절한다. 원ZIP에 빠진 파일을 삽입하거나 upstream verify_delivery.py를 덮어쓰지 않는다. 직접 F1M SOURCE_LOCK의17개만 검사하고 parent의 재귀적 source-lock closure를 주장하지 않는다.

Output ZIP의 input/F1M.zip과 input/F1P.zip은 검증된 원 archive 그대로다. FILE_MANIFEST.json의 파일별 SHA로 payload를 확인한다. Snapshot 이후 실제 Git/current HEAD/backup ACK는 detached DELIVERY_RECEIPT.json에 있으며, receipt 자신의 ACK는 별도 receipt transport log에 있다. Git 인계와 사용자 지정 ChatGPT 대화의 직접 수신을 구분한다.

Canonical HH-F1은 REI-F07를 기다린다. Consumer가 실제 HH domain·owner·constants·adapter·budget receipt를 게시하면 새 exact HEAD에서 이를 읽고 다음 task를 진행한다. 24/289 및 consumed scope는 유지한다.
