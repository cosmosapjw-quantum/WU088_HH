# PHYS78 단계별 상태

| 단계 | 유도·코드·검증·과학 실행 | 게시 | 백업 | 다음 DAG |
|---|---|---|---|---|
| S0 조사·최적화 | 6 repos/1060 refs; 구조적 최적화 계약 | PR133 `9a9f5c16ddf3c9fe98bfbcae6ee1f0cf1ae5ea15`; 19 blobs readback | Drive/Dropbox 업로드 ACK; 전체 restore 미실행 | 보존적인 gray physics |
| S1 물리·코딩 | 21-state PI+RR, 33-state coupled IVP; 최초 baseline; 실패2건 보존 | `81f414482803bafce969059bffce8d462f71dd57`; 88 blobs readback | 두 provider 전체 ZIP·88 payload restore PASS | P013 재사용, 남은30 새 case |
| S2 결과·그림 | pilot31, 고유정련1, 35light tests, 그림10종 완료 | `b001e69668b2d2c2557b51830f5f732164b56ce0`; 369 blobs readback PASS | 두 provider 전체 ZIP·369 payload restore PASS | COLLISIONAL_ATOMIC_AND_THERMAL_CLOSURE |
| S3 전달 | 과학 계산 추가0; 게시·backup receipts 및 handoff | 이 additive metadata closeout; actual HEAD는 외부 receipt | S2 증거 포함; 최종 metadata archive는 외부 receipt로 확인 | 다음 physics→coding |

총 ODE34=초기실패2+pilot완료31+고유정련1. 완료재실행0, NCP0, benchmark0. 과학 source identity와 source/result commit, 최종 metadata HEAD를 구별한다. 최종 HEAD와 전체 backup SHA는 외부 `PHYS78_FINAL_DELIVERY_20261021.json`에 기록한다.

범위는 exploratory finite gray PI+RR isotropic reacting gas와 anisotropic collisionless DM/free radiation이다. 전체19핵반응·reactive gas anisotropy·CI/CX·hardUV Li·continuum certificate와 FULL_NATIVE_COLD_EOR는 OPEN. HH_R10=OFF, production NOT_ISSUED.
