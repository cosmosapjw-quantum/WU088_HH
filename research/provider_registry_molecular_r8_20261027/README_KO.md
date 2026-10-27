# WU R8 — 인증된 지연 커널과 두 번의 Volterra 상계 개선

**조건부 이론·구현 채택, 과학 DAG 17/32.** R7 입력과 저장 궤적을 유지하며 native9의 최종 R/E 상계를 **48.0844% /48.1532%** 줄였다. 기존30개 노드 객체는 보존했다.

주요 문서는 [연구 보고서](REPORT_KO.md), [복사 가능한 인계](HANDOFF_KO.md), [과학 채택](SCIENTIFIC_ADMISSION.json), [48파일 payload](SCIENTIFIC_PAYLOAD_MANIFEST.json), [최종 수치 요약](results/FINAL_RESULTS_SUMMARY.json), [독립 C9](reviews/C9_FINAL_REVIEW_KO.md)다. 그림은 [NATIVE9_BOUNDS.svg](results/NATIVE9_BOUNDS.svg), 구현은 [volterra_feedback.py](src/volterra_feedback.py)다.

실제 primary237/237PASS, 최초 reference726/727PASS·1FAIL보존, exact scalar24/24PASS이며 열린 실질 지적0이다. Python과학 전체CPU4.320964초, 새ODE0회다. CAS는16zeros·4/6True·2symbolic과 실제경고를 보존한부분확인이다.

현재 S01–S09의 실제 게시·이중 원본ZIP검증을 마쳤고 workflow18/20이다. S10 보고서·handoff의 최종 전달을 처리한다. 완료 상태와 제공자 원본ID는 [게시·백업 색인](delivery/PUBLICATION_INDEX.json) 및 [workflow](WORKFLOW_RECORD.json)를 따른다.

다음 연구는 [NEXT_INPUT_CONTRACT](followup/NEXT_INPUT_CONTRACT.json)의 실제 reactive source 또는 명명된 소비자의 state/pool/density/clock/전체구간box를 결속한다. 물리·중앙delta0, HH_R10OFF, productionNOT_ISSUED, L4false를 유지한다.
