R31AL z=0.75 minimal mixed node를 한 번 실행하려면 아래 envelope를 현재 user instruction으로 명시적으로 승인하십시오.
이 파일은 예시이며 실행 승인이 아닙니다. 승인 전에는 science command 0개입니다.

```json
{
  "schema": "WU088_R31AL_Z075_MINIMAL_MIXED_AUTHORIZATION_V1",
  "authorize": true,
  "action": "AUTHORIZE_R31AL_Z075_MINIMAL_MIXED_NODE",
  "scope_sha256": "2f22f11f279b8d7f98efb2a4bff1fbfb79145f7f5010ce5081ca6ebfcc147357",
  "one_shot": true
}
```

승인 범위: z=0.75 a0, B192, tau=z/producer velocity; mixed O/D_col/D_row 및 independent mixed dotO만.
H, neutral47, ionic2, full49, trajectory, 다른 z, M3/reference, 결과 후 수정은 제외됩니다.
