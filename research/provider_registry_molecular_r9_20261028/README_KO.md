# R9: 인과적 셀별 결합 오차 상계

R8의 저장된 수축 kernel·비교 계수·인증 상계를 재사용하고 각 시간 셀의 결합 부등식을 양의 2×2 역행렬로 닫는다. 새 이론·코드 의무를 등록한 DAG는 **17/34**다. 이론 R1–R10 및 코딩 C1–C10, 각 단계 게시·이중 백업의 실제 근거를 기록한다.

현재 계약은 CONTRACT.json, 진행은 DAG.json/WORKFLOW_RECORD.json, 실제 실행은 EXECUTION_LEDGER.json에서 관리한다. 실제 HD reactive source와 물리 소비자 density/clock 입력은 별도 INPUT_PENDING이다.
