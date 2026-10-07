# HH-TH05: 엄격한 이온화 순서와 양의 광학기억

판정: STRICT_HH_IONIZATION_ORDER_AND_POSITIVE_OPTICAL_MEMORY_ENCLOSED.

TH04의 공통 first-exit 영역과 부호 없는 차이 상계를 계승해, 동일 exact-real thermal FT03+LCS/S0-derived 모형에서 각 0<lambda<=1 대 OFF의 HII 분율 순서를 증명했다. 0<t<=8e11s, |epsilon|<=.01에 h_lambda(t)>h_OFF(t)이며, 종료시각에는 6.200e-9*lambda<Delta h<2.874e-7*lambda다. 온도 및 He 역피드백은 생략하지 않고 기존 상계로 제한했다.

광자군의 동일 birth/characteristic과 HI-only 흡수를 사용하면 S_j=int a_j Delta h>0이고 생존광자는 증가, 누적 photo 흡수는 감소한다. 양의 birth와 양의 활성 생애를 갖는 경우에 엄격한 부호를 붙인다. 순간 photo rate, terminal kink, 온도, 작은 Bianchi-FLRW 이중차이의 부호는 별도다. 전체 thermal 계가 cooperative라는 가정이나 임의 lambda쌍의 단조성 주장은 없다.

읽기: THEOREMS_KO.md, RESULT_SUMMARY.json, NEXT_HANDOFF_KO.md. Git은 검색용 별도 요약이다. 전체 증명, 실행 가능한 proof script 2개, 정확한 predecessor certificate와 산술 helper, 새 유리수 결과, 원 성공 로그와 메타데이터 오류의 재현은 ZIP에 있다. Git 요약과 ZIP 상세본이 동일 bytes라는 주장은 없다.

- ZIP: WU088_HH_TH05_SIGNED_RESPONSE_MEMORY_20261007_v1.zip
- bytes: 63729; entries29; manifest payloads28
- SHA256: a49d45a9ee044acb5173054e2a6dabfbafc563bfb46933250b37cd61d54d558e
- Drive: 1mmghc4xQpko3Wz6G09hSGSq2OdNB5XDJ, parent1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM
- Dropbox: id:BSpOijBcT10AAAAAADzhWg
- Dropbox path: /BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/WU088_HH_TH05_SIGNED_RESPONSE_MEMORY_20261007_v1.zip
- 두 provider create-only 완료, ID/name/path/size 확인. R1이며 새 출력 full remote restore=false.

ZIP 루트 HH_TH05_20261007_v1에서 새 출력 경로로 python -B research/verify_signed.py --output NEW/SIGNED.json 및 python -B research/verify_independent.py --certificate NEW/SIGNED.json --output NEW/INDEPENDENT.json을 실행한다. 원 TH04/TH03 proof는 재실행하지 않는다. Input SHA mismatch와 기존 output은 거절한다.

최종 core38+별도55=93 checks, 별도55에 symbolic7 포함. 각 script1회, exit0/stderr0. 두 검산은 같은 작성자의 별도 구현이며 독립 agent 심사나 형식증명은 아니다. Metadata 생성에서 __pycache__를 파일로 읽은 오류는 재현·보존 후 is_file 필터로 고쳤다. 과학 코드·결과·허용오차는 변경하지 않았다. Native/Rust/rate/IVP/BE/geometry root/actual adjoint/old suite 모두0.

HH input adc1ca8c4a0d3b6a719675796661d162e179398f, REI a0001ca14644fc9fd2fbe52f8cfcae3edbedd110을 게시 전에 다시 읽었고 동일했다. 새 IGM thermal provider는 HH 제외/별도 Grackle kinetic fit이며 기존 FT03와 혼동하지 않는다. HH ACTIVE/canonical S0 OFF control, physical/production HOLD 및 legacy24/289·265unbounded·epsilon_C/Rnull·B22OPEN·consumed scopes 유지.
