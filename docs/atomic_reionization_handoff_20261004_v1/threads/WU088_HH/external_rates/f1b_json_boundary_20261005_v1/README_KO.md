# F1B JSON boundary continuation

원 f1b_20261004_v1을 보존한 별도 후보다. 중복 JSON key와 object 아닌 root만 새로 거절한다. 원 evaluate/direction 수치 코드는 그대로이며 consumer admission은 false다.

```sh
python3 -B -m unittest discover -s tests -p test_json_boundary.py -v
python3 -B src/hh_f03_binding.py --input INPUT.json --output NEW_OUTPUT.json
```

Tests는 원 input/WU088_HH_FAST_F1B_20261004_v1/src를 사용하고 Git에서는 기존 sibling f1b_20261004_v1/src를 사용한다. 두 원 파일 SHA를 확인한 뒤 parity를 검사하므로 Git checkout에서도 실행 가능하다. Cloud output ZIP의 input/F1B.zip은 검증cache와 byte동일하다. Scratch 재현이 필요하면 새 input 디렉터리에 그 원root만 복원한다. 동일source의완료검사는관례적으로반복하지않는다.

Valid input은 원 MODEL_KEYS와7coords,provider 및 optional direction/dt_s다. 중복decodedkey는어느object에서나DUPLICATE_JSON_FIELD로거절된다. top-levelobject가아니면JSON_OBJECT_INPUT_REQUIRED다. 기존 output은덮어쓰지않는다. 원F1Bsource는inputZIP에보존하고diff는evidence/CHANGE.patch에있다.

현재 gate는 SYNC_STATE/TASK_RETURN을 읽는다. Source/read/byte parity와물리적소비자채택을구분한다. HH-F1은REI-F07대기,legacy24/289와consumedscopes는불변이다.
