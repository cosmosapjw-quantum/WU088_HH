# WU088_HH PHYS24

단면적의 Maxwellian positive-bin map, exact endpoint Lipschitz envelope와 nested refinement를 유도하고, PHYS23의 고정 P01 관측량 경계에 연결했다. Kernel을 실제 계산하여 near-threshold 데이터 확보 우선순위를 정했다.

- report/REPORT_KO.pdf:9쪽 이론 보고서와 완전한 증명.
- results/PHYS24_RESULT.json:상수,정확한weight/관측량계수,계산된witness와입력범위.
- results/KERNEL_BIN_TABLE.csv:CM/lab bins와outward weight.
- checks/FINAL_VALIDATION.json:62개 Python검사와실제CAS검증기록.
- CROSS_REPO_REUSE.json:5개관련repo의실제읽은revision과재사용방식.
- SOURCE_REGISTRY.json:원전검색과회수범위, NASA near-threshold benchmark후보.
- NEXT_INPUT_CONTRACT.json, HANDOFF_KO.md:실제물리envelope/budget입력과다음실행.

실제 Wolfram+xAct가 실행되었다. 서로다른 검산경로는 같은assistant가 작성했으며 외부독립심사는 미수행이다. 이번신규원격mutation은없다.
