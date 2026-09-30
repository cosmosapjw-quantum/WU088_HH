R31AI의 사전등록된 B192, z=2.5 단일 minimal mixed science node를 아래 scope에 한하여 정확히 한 번 실행하도록 명시적으로 승인한다. 아래 JSON은 예시가 아니라 이번 실행에 대한 실제 승인이다.

```json
{
  "schema": "WU088_R31AI_Z25_MINIMAL_MIXED_AUTHORIZATION_V1",
  "authorize": true,
  "action": "AUTHORIZE_R31AI_Z25_MINIMAL_MIXED_NODE",
  "scope_sha256": "78d960c041536f2baa2160639e5a60878f43f73aadee2e3174ffd5a27d8a68e7",
  "one_shot": true
}
```

research/r31aj_z25_validation/CODEX_HANDOFF_KO.md를 적용하라. 승인 범위는 mixed O 47x2, D_col 47x2, D_row 2x47, independent dotO 47x2이며, H 행렬·neutral47·ionic2·full49·trajectory·다른 z·M3/reference 작업은 승인하지 않는다. 변경 없는 검증된 OD/JVP producer를 사용한다. 기존 fused OD 내부 T/moment intermediates는 source 구현대로 두되 H block을 조립·저장하지 않는다.

출력 접근 전에 scope, 원 prereg/model/manifest/rule 및 producer identity를 확인하고 동일 geometry의 기존 결과나 승인 소비 기록이 있으면 중복 실행하지 말라. 첫 scientific output identity 생성 시 one-shot을 소비한다. 해당 한 node의 OD/JVP 두 단계는 하나의 승인 transaction이며 미완료 시 자동 재실행 대신 partial evidence를 반환하라.

고정된 E_K/E_Dmax Pareto rule을 한 번 적용하고 모든 secondary errors를 보존하라. Reference-error robustness는 별도 부록이다. 실제 reference error bound가 없으면 UNAVAILABLE로 보고하고 1e-10 또는 metric residual을 오차상계로 대입하지 말라. 결과 뒤 retuning·knot insertion·후속 node를 실행하지 말라. 연구 branch에 비강제 게시하고 Drive+Dropbox create-only 백업 후 종료하라. 실제 raw restore 없이 RESTORE_VERIFIED라고 하지 말라.
