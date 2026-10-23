# Codex 재개: PHYS84 source adapter, 공유 lease 대기

## 먼저 읽을 실제 근거

1. PR141 최종 본문과 외부 `PHYS84_FINAL_DELIVERY_20261023.json`에서 actual final HEAD, ZIP/JSON IDs와 SHA를 읽는다. S0 또는 S1 단독 checkout을 final로 혼동하지 않는다.
2. repository AGENTS, 본 단원 `FINAL_REPORT_KO.md`, `CONTRACT.json`, `DAG_OVERLAY.json`, `EXECUTION_LEDGER.json`, `STAGE_STATUS.json`, `RESEARCH_LOOP_MAP_KO.md`를 읽는다.
3. `reviews/INDEPENDENT_REVIEW.json`, `reviews/RESOURCE_GATE_REVIEW_KO.md`, `verification/ATTEMPT_01.json`, `implementation/ADMISSION_WAIT_HANDOFF.json`, `delivery/`와 `POST_PUBLICATION_HANDOFF_KO.md`를 읽는다.
4. 중앙 pinned handoff는 rei_bianchi `0f9d9df825be1dac9ca9bdf73cdc2e8908bcba17`, `research/orchestration_longterm_20261023/assembly/HANDOFF_WU088_HH_KO.md`다. 실제 현재 중앙/소유자 refs 및 병렬 변경을 bounded 범위에서 대조한다.

## 완료와 미완료

PHYS83 final `6a2fc5aacb6182a916b9434c316e99e750e8273c`, identity `e09e64848d545d844590c6cc733cc870109d8fa4f3b44bff796afd11c0753d0c`의 132 rate / 324 steady / 732 transient, 71cases/2111assertions, 57science frozen files는 완료 근거다. 이를 재실행하지 않는다. PHYS82 final `ca9d53983459ea08f9992a8a24663e46b7180344`의 CRLF 복구와 이전 완료 identities도 보존한다.

새 PHYS84 계약·유도, Wolfram19zero, v5 code와 독립 정적 검토는 준비되었다. **새 검증 child0, assertion0, 실제 source application0, 결과행0, 실제 resume0.** Attempt01은 pinned shared lease가 available1.054565GiB < reserve1.5+job0.5GiB에서 거부한 exit75다. 이 상태를 numerical failure, PASS 또는 완료 scientific identity로 바꾸지 않는다. Prepared artifact identity `dca969a27fa00a703efb4c9f341efb5e50b45b2d88f5896a66f2c4aeced0a0db`와 source science identity는 구별한다.

## 다음 허용 실행

사용자 authorization은 이어지지만 실제 resource admission은 매번 필요하다. 기존 guard·shared lock·reserve·job을 유지하고 다른 process를 종료하지 않는다. 금전 budget null은0이 아니다. Runtime 버전 차이는 완료 science 자동 재실행 사유가 아니다. 현재 external runtime은 도구 사용량 제한으로 미확인이다.

먼저 code/contract/input pins와 backup을 byte-only 대조하고 실제 자원 조건이 변했는지 확인한다. 변경 없이 동일 미달 상태라면 blind retry하지 않는다. 조건이 충족되고 root가 실행을 열면 단원 디렉터리에서 다음 최초 수치 검증을 수행한다.

```bash
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 \
NUMEXPR_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 BLIS_NUM_THREADS=1 \
PYTHONDONTWRITEBYTECODE=1 \
python source/leased_call.py --kind verification \
  --label source-interface-attempt02 --receipt verification/ATTEMPT_02.json \
  -- python verification/verify_source.py --attempt verification/attempt_02
```

첫 결과와 실패를 그대로 남긴다. Independent Fraction oracle와 guards의 actual raw outcome, lease receipt를 fresh reviewer가 읽기 전에는 source application을 시작하지 않는다. 검증이 통과하면 실제 current descendant에 검증 checkpoint를 expected SHA로 게시·백업하고 다음 한 번을 실행한다.

```bash
mkdir -p results
python source/leased_call.py --kind application \
  --label constructed-source-application01 --receipt results/APPLICATION_ATTEMPT_01.json \
  -- python source/run_source.py --output results/source_application \
  --authorize-new-16row-application
```

위 command에도 동일 thread environment를 적용한다. results 상위 directory를 확인하되 이미 존재하는 output/partial completion은 덮어쓰지 않는다. 성공 후 actual results를 독립 검토하고, 별도 승인한 `--kind resume ... --resume` 한 번으로 bytes 재사용과 callback0을 확인한다. 완전한 command와 예정 경로는 `implementation/ADMISSION_WAIT_HANDOFF.json`에 있다. 마지막 source/application identity와 science freeze를 별도로 생성한 뒤 S2로 기록한다.

## 계속 유지할 의무

REI-L1 explicit states/excitation reservoir/source/domain/clock/radiative owner binding은 OPEN이다. Consumer admission은 새 numeric checks 통과와 별개다. 모든 방출 diagnostic을 두 번 합산하지 않는다. Gas π=0, 별도 DM π_m, same-frame tensor 합 뒤 norm과 Frobenius convention을 유지한다. Li physical uncertainty, CX, D PI/RR, nuclear finite-T joint event moments, z20 initial charge, Li inner-shell 및 full geometry/spectrum 의무는 DAG의 OPEN 상태다. HH_R10=OFF; production NOT_ISSUED.
