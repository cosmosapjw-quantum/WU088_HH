# WU088_HH R31S: c64-g3 재설계 / 읽기 전용 probe

기준 parent: 5887d2a2239db9f34d5bd5b4840abce420b37f1a. WU088_HH만 변경한다. frozen/reference/vendor/scientific runtime 및 기존 pair/ACK는 바꾸지 않는다.

z2 직접 소스 H order-comparison/full49는 PASS, [0,4] linear interpolation은 FAIL이다. 새 heavy 계산은 0이다. 결과와 실행 trace는 evidence/RESULT.json, 설계와 다음 구현자 계약은 DESIGN_KO.md를 참조한다.

이 커밋의 실행 코드는 read-only probe 및 in-memory durability-credit specification model이다. cloud native bridge, benchmark, persistent executor 및 production promotion은 아직 수행하지 않았다. 상세 후처리 코드/전체 evidence/생성 full49 배열을 포함한 별도 conversation artifact 패키지도 제공한다. 이 Git 커밋은 해당 패키지의 전체 대용이라고 주장하지 않는다.

NCP host에서 저장소 root 기준으로 지금 실행할 것은 probe뿐이다. stdlib만 필요하다.

```bash
REPORT_DIR=$(mktemp -d "$HOME/wu088_ncp_probe.XXXXXX")
python3 research/r31s_ncp/probe/ncp_probe.py \
  --workspace "$HOME" --out "$REPORT_DIR/HOST_PROBE.json"
echo "$REPORT_DIR/HOST_PROBE.json"
```

heavy_execution_allowed=false, selected_configuration=null이 정상이다. PROBE_REQUIRES_CGROUP_INSPECTION은 우회하지 말고 그대로 반환한다. 기존 script에 workers=64를 넣어 실행하지 않는다.

새 tests만 실행할 때 (pytest/NumPy/SymPy가 이미 있는 개발 환경):

```bash
python -m pytest -q research/r31s_ncp/tests
```

29개 새 tests만 검증했다. 과거 scientific full suite 재실행, NCP instance 생성, credential/system 설정 변경, 새 유료 heavy run, 자동 merge를 하지 않는다.
