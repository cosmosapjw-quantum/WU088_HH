# R31AE authorization scope canonicalization

Hash algorithm: SHA-256.

Canonical bytes are UTF-8 encoding of JSON after:
1. recursively sorting object keys lexicographically,
2. using JSON separators ',' and ':' with no whitespace,
3. preserving array order,
4. standard JSON true/false/null and finite JSON numbers,
5. forbidding NaN and Infinity.

Canonical JSON bytes for AUTHORIZATION_SCOPE.json are exactly:

```json
{"R31AD_model_sha256":"ab220248066580fc77af70c412251dbe3ed643a6fadc266cf5c25a7a3a6651a0","R31Z_model_sha256":"4ba03ba2adbdc9533f6472558b33a7edf86959bfc397e5fc8e3e90f8765ba034","comparison_tolerance":1e-10,"five_node_manifest_sha256":"05f4068dffad51080942c466e19943a73c508b004d3d46f3b9a2b69a58cefc49","forbidden":["H","neutral47","ionic2","full49","trajectory","other_z","M3_reference","post_result_model_retuning"],"one_shot":true,"post_result":"compare_once_and_stop","preregistration_sha256":"a111005296954c303563be6aaab10379d22694c544576fb1869a37938ab9247d","radial_order":192,"required_outputs_only":["mixed_O_47x2","mixed_D_col_47x2","mixed_D_row_2x47","independent_mixed_dotO_47x2"],"schema":"WU088_R31AD_Z05_MINIMAL_MIXED_SCOPE_V1","selected_time_ta":1.1179386195169057,"selected_z_a0":0.5,"selection_rule_sha256":"835c0a53719849652557737ef61d343c58222d847cf6d1b2ee6fb4831fb656dc","selection_sha256":"2761664a75d7609c7ac0b1df4daf36a50e01d82a80b28a42885a22c5042a800b"}
```

Expected SHA-256:

`f9872cb045fef146987829620c669fb99f2417a787d74cde26dfee107153a567`
