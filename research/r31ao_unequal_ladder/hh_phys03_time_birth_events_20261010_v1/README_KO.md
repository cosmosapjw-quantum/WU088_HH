# WU088_HH PHYS03

물리 목표: PHYS02의 frozen mixed-response 결과를 시간 의존성, photon birth,
고정 격자 remap과 BE source 순서에 연결하는 이론을 구한다.

먼저 읽을 파일:

- [FINAL_REPORT_KO.md](FINAL_REPORT_KO.md): 핵심 물리 결과와 새 수치
- [FINAL_STATUS_KO.md](FINAL_STATUS_KO.md): 독립 판정과 봉인 상태
- [NOTATION_AND_INTERPRETATION_KO.md](NOTATION_AND_INTERPRETATION_KO.md): 기호와 음의 mixed response의 의미
- [NEXT_HANDOFF_KO.md](NEXT_HANDOFF_KO.md): PHYS04의 구체적인 다음 목표
- [REPRODUCE_KO.md](REPRODUCE_KO.md): 기존 evidence를 보존하는 재현

상세 이론:

- smooth_theory/PHYS03_SMOOTH_THEORY_KO.md: nonautonomous K3/K4, causal birth kernel, 반복 birth+BE
- HYBRID_THEORY_KO.md: 공통 시각 event 혼합 chain rule
- CHRONOLOGY_THEORY_KO.md: 실제 source의 threshold remap 한 column과 free-emission energy
- REMAINDER_TRANSFER_KO.md: finite mixed sign을 옮기는 충분조건

Source·evidence:

- inputs/source_survey: 최신 owner/source 의미와 immutable byte binding
- results/CHRONOLOGY_256.json: Arb256 exact endpoints 및 mpmath 교차검사
- smooth_theory/NONAUTONOMOUS_EXACT_CHECK.json: exact algebra evidence
- logs: root의 최초 new-check stdout/stderr
- independent: candidate author와 분리된 최종 decision review
- MANIFEST.json: 자기 자신을 제외한 전체 file SHA-256

Declared model과 actual runtime의 admission을 구분한다.
Native/IVP/nonlinear BE/NCP/기존 완료 suite를 호출하지 않은 물리 연구 패킷이다.
