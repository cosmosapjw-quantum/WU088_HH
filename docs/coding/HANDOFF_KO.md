# 다음 작업 인계

현재 코드/데이터가 변경되지 않았으면 과거 B160/B192 1440 pair, R31F~R31J 및 이전 과학 full suite를 다시 실행하지 않는다.

1. 원격 게시 상태를 detached receipt와 실제 origin/main으로 확인한다. 성공하지 않은 push를 상속하지 않는다.
2. 원래 runtime을 유지한 채 `bash scripts/benchmark_host.sh` 한 번으로 host 성능 보고를 만든다. CPU topology/quota와 process×thread budget을 먼저 검사한다. outer12×inner4 같은 무허가 oversubscription을 하지 않는다.
3. foreign-component 벤치마크 결과만으로 최적의 전체 H configuration을 선택하지 않는다. H0 비용·queue/ACK 시간까지 포함한 작은 bounded host throughput 비교를 다음 validation으로 고정한다.
4. candidate source/kernel을 production에 넣기 전 science-resolution selected controls -> all94 comparison -> 독립 review를 닫는다. 비용순 scheduler는 scalar kernel을 바꾸지 않지만, 실제 host wave의 새 telemetry를 확인해야 한다.
5. 연구 critical path는 새 z=0,16,32,48,64의 source-bound 독립 dotO와 ionic2 provider다. 현재 반환물의 H0 O/D를 독립 JVP로 표시하지 않는다. 필요한 원본 코드/배열을 회수하거나 해당 계산만 별도 bounded heavy handoff한다.
6. 각 point full49를 닫은 후에만 R31J midpoint/보간/endpoint 규칙으로 진행한다. exact phase-envelope interpolation은 제안이며 기존 preregistration을 바꾸어 사용하지 않는다.

금지: old runtime rm-rf, force-push, threshold relaxation, fast-math, binary64 downgrade, 자의적 작은 항 삭제, waveform/observable 진입, 보고서-only PASS의 raw admission 전이.
