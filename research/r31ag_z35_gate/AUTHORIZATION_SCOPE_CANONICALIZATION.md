# R31AG scope canonicalization

Canonical JSON algorithm:

1. UTF-8 JSON.
2. Recursively sort object keys lexicographically.
3. Separators exactly ',' and ':' with no whitespace.
4. Preserve array order.
5. Only finite JSON numbers; NaN/Infinity forbidden.
6. SHA-256 over exact canonical bytes.

Canonical bytes:

```json
{"R31AF_engine_sha256":"ab220248066580fc77af70c412251dbe3ed643a6fadc266cf5c25a7a3a6651a0","R31AF_policy_sha256":"720b221a9e01ab7fc1bbd482b600ea785fed0b8c6b80b5834c576a75c2b70756","R31Z_model_sha256":"4ba03ba2adbdc9533f6472558b33a7edf86959bfc397e5fc8e3e90f8765ba034","comparison_tolerance":1e-10,"decision_rule_sha256":"52b995b2f5516cf586cf1cbcdb681ec521f1b911a7538e3999a11d0f3bd62560","forbidden":["H","neutral47","ionic2","full49","trajectory","other_z","M3_reference","post_result_model_retuning"],"one_shot":true,"post_result":"compare_once_and_stop","preregistration_sha256":"ec4613f5300ec38a488eae75f5c7267a2f1a166c34e45d54bb9fa8b449537447","radial_order":192,"required_outputs_only":["mixed_O_47x2","mixed_D_col_47x2","mixed_D_row_2x47","independent_mixed_dotO_47x2"],"schema":"WU088_R31AF_Z35_MINIMAL_MIXED_SCOPE_V1","selected_time_ta":7.825570336618339,"selected_z_a0":3.5,"selection_sha256":"546026387ecae9952b0397fb0dd26ad0633465739d8bbb82878f0f4c532c545e","six_node_manifest_sha256":"e444e9f1cff7d4cc9425a2f44ff45a6e87199c6bf31ca2b095010364379e7573"}
```

Expected SHA-256:

`f43faaf5746a5fda5cd26593ee69e97c0f2be8239727a62081d49357e3c2a9b4`
