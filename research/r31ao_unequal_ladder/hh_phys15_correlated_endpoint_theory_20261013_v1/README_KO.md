# WU088_HH PHYS15 — Full–two-half endpoint 결함 이론

**독립 판정: PROMOTE_SCOPED.** 같은 COMMON의 실제 두-half와 Full 사이 차이를 직접 유도하여, 원 source 정규화와 광자 chronology를 보존하는 잔차·관측량 전달 정리를 완성했다.

- `REPORT_KO.md`: 주요 결과와 수행 범위.
- `theory/CORRELATED_ENDPOINT_THEORY_KO.md`: 통합 정리와 증명.
- `theory/PHOTON_DEFECT_THEOREM_KO.md`: 원 격자의 photon sector, 부호, guard 수지.
- `theory/ASSUMPTIONS_AND_BINDINGS_KO.md`: 원 CI·RR·DR 및 HH source의 정규화 연결.
- `theory/FIXED_PRECONDITIONER_BINDING.md`: 기존 C,B,q,S의 정확한 원본 대응.
- `report/WU088_HH_PHYS15_THEORY_20261013.pdf`와 `.tex`: 정식 한국어 보고서.
- `review/DECISION.json`, `review/REVIEW_KO.md`: 독립 검토와 채택 범위.
- `contracts/ENDPOINT_ENCLOSURE_CONTRACT.json`: 다음 실제 수치 포함의 구현 계약.
- `state/RESEARCH_STATE.json`, `NEXT_DAG.json`, `HANDOFF_KO.md`: R1–R10와 다음 재개 지점.

이번 단위는 실제 유도와 정확한 대수 검산을 수행했다. 새로운 physical source·root·history 실행은 0회다. 후속 `HH_CORRELATED_ENDPOINT_ENCLOSURE`에서 검토된 식에 기존 자료를 넣어 실제 r,d,ΔT/e/w/ne 및 photon·sector 구간을 계산한다.

## 작은 검산의 재현

프로젝트 root에서 다음 명령을 사용할 수 있다. 이들은 제조된 대수 예제와 원 leaf의 판별 계산이며 실제 물리 history를 실행하지 않는다.

```bash
python3 checks/check_nonlinear_transfer.py --output /tmp/phys15_nonlinear_check.json
python3 checks/photon/check_photon_defect_identities.py --project inputs/phys14 --output /tmp/phys15_photon_check.json
```

Wolfram의 실제 기호 계산 코드는 `checks/WOLFRAM_ALGEBRA.json`에 있다. 저장된 결과를 검토하는 데 재실행은 필요하지 않다. 원 입력의 bytes·SHA256 및 source provenance는 `inputs/INPUT_MANIFEST.json`과 `evidence/bindings/`에 보존한다.
