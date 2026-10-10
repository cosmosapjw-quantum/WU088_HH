# WU088_HH R31S: c64-g3 재설계 / NCP + Codex handoff

기준 scientific parent: `5887d2a2239db9f34d5bd5b4840abce420b37f1a`.
R31S redesign parent commit: `5250f17ffe5ca587125169385e97fe9df668c18a`.
WU088_HH만 변경한다. frozen/reference/vendor/scientific runtime 및 기존 pair/ACK는 바꾸지 않는다.

z=2 직접 소스 H order-comparison/full49는 PASS, [0,4] linear interpolation은 FAIL이다.
다음 scientific depth-first direct node는 z=1이지만 **cloud host/build/execution admission 전에는 실행하지 않는다**.
결과와 실행 trace는 `evidence/RESULT.json`, 설계와 claim gate는 `DESIGN_KO.md`를 참조한다.

## NCP M0 현재 상태

사용자가 c64-g3 host에서 read-only probe를 실제 실행했고 다음 top-level 결과를 반환했다.

- repository HEAD: `5250f17ffe5ca587125169385e97fe9df668c18a`
- probe status: `PROBED_NOT_BENCHMARKED`
- planning CPU budget: `64`
- heavy execution allowed: `false`
- host-local report: `/root/wu088_ncp_probe.djNQYK/HOST_PROBE.json`

이 정보는 **사용자 제공 terminal output에 의해 확인된 M0 summary**다.
현재 repository에는 full `HOST_PROBE.json` bytes/SHA가 아직 ingest되지 않았으므로 CPU model, SMT/NUMA/L3, cgroup details, compiler ABI 등은 이 summary만으로 추정하지 않는다.
Codex가 가장 먼저 host-local report를 읽고 SHA-256 및 key facts를 반환해야 한다.

## Codex 역할

Codex는 이번부터 **NCP host-local 구현·빌드·bounded benchmark 담당자**다.
ChatGPT/R31S claim gate는 scientific authority, provenance, stop condition을 유지한다.

Codex handoff SSOT:

- `CODEX_HANDOFF_PROMPT.md`
- `DESIGN_KO.md`
- `evidence/RESULT.json`
- `evidence/NCP_M0_USER_REPORTED.json`

Codex는 새 branch `codex/r31s-ncp-m1-m2`를 현재
`r31s-ncp-c64g3-redesign` HEAD에서 만들고 작업한다.
force-push, merge, z=1 execution, full 144-pair scientific node, M3 production-shaped run,
production async durability promotion은 금지한다.

현재 승인된 범위는:

1. M0 full probe ingest/identity close
2. M1 fresh NCP work root/venv/read-only source+reference/fresh build namespace
3. M2 same-host reference/candidate build 및 bounded representative equivalence/tuning probes
4. test/evidence/commit/push + return handoff
5. **STOP for ChatGPT review before M3/M4/M5**

## read-only probe 재실행

필요하면 다음처럼 새 report를 create-only로 만든다.

```bash
REPORT_DIR=$(mktemp -d "$HOME/wu088_ncp_probe.XXXXXX")
python3 research/r31s_ncp/probe/ncp_probe.py \
  --workspace "$HOME" --out "$REPORT_DIR/HOST_PROBE.json"
echo "$REPORT_DIR/HOST_PROBE.json"
```

`heavy_execution_allowed=false`, `selected_configuration=null`은 M0에서 정상이다.
`PROBE_REQUIRES_CGROUP_INSPECTION`이 나오면 우회하지 말고 STOP한다.

새 R31S tests만 실행할 때:

```bash
python -m pytest -q research/r31s_ncp/tests
```

현재 게시된 R31S verification은 29 PASS이며 target c64-g3 throughput/native bridge/real-provider
fault recovery/production admission을 의미하지 않는다.
