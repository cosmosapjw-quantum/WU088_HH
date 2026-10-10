# PHYS06 NCP source intake

## 결론과 범위

고정 NCP head는 **4b9231a0eff113701e7178ad98624233f387dd15**이고 core 구현 commit **892eca446ce23815d103f162dbd71c198a1e6198**의 후손이다. 중간 commit은 34a3ba25c5df882bd284b41ec5d3b0d41e6682eb, head tree는 10a19c64b17352095ce7874284fb12cc5b8b0e54다. source identity를 현재 Git 원문에서 확인했으며 과학적 타당성 또는 native 권한의 증거로 사용하지 않는다.

이번 intake는 read-only source 확인, 기존 검증 기록의 범위 확인, 원 COMMON seed 필드 추출, 고정 원자 cross-section 식의 점별 산술 전사다. native endpoint, conservative BE point, certificate 내부 point, root producer, IVP, 기존 과학 suite 실행은 모두 0이다. 이 intake 실행자는 후보의 최종 decision reviewer가 아니다.

## 새 handoff에서 반복하지 않을 완료 항목

| 항목 | 닫힌 범위 | 직접 근거 |
|---|---|---|
| detached PHYS04 receipt | v2에서 입력 receipt 및 ZIP/publication identity 회수 완료 | RETURN_KO.md, NCP_RETURN.json |
| same-execution receipt | private SameEndpointReturn 소비; λ/b·clock·source·preBE·parent·strict root image·history 검사, carry와 원 root box 분리, 추가 endpoint/point/root 0인 합성 경로 | candidate/src/phys04_receipt.rs, evidence/v2_amplitude_receipts_fixed.stdout |
| 원 COMMON seed | 원 ON byte decode/encode 및 물리 stock·guard·compensation·과거 HH history 보존; 미래 increment ledger 분리; four corners 동일 초기 physical payload | src/family.rs, tests/targeted.rs, evidence/v2_targeted.stdout |
| source-ordered transport | 고정 8/8/16, redshift/hat → endpoint birth → grouping → coupled residual; signed gas/photon/guard U,V,W 유지 | candidate/src/phys04_transport.rs |
| 실제 FT03/LCS 도함수 | ft03_interval_rhs 및 hh_rate_jet에 다변량 chain rule 적용; 전체 gas Hessian, photon N/D quotient Hessian, old U,V,W, λ 혼합항 | candidate/src/phys04_mixed.rs |
| tangent 산술 | 실제 source centre Jacobian의 고정 C, C rhs+(I−CA) box strict inclusion 및 weighted contraction | phys04_mixed_at_box, phys04_linear_image |
| v2 제한 검증 | receipt 4 + targeted 4 PASS 기록, offline/locked build PASS 기록; 과거 189-slot Decimal100 diagnostic oracle 재사용 | evidence/INDEPENDENT_DECISION_V2.json, 기존 stdout, NCP_RETURN.json.validation |

구현 검증 상태는 기존 NCP 실행 기록에 근거한 **inherited implementation-verified 범위**다. 이 intake가 build/test/oracle를 다시 수행한 것은 아니다. 원 189-slot oracle는 source 식·상수·cross-section을 공유하는 독립 Decimal 차분 계산이며 rigorous FD truncation/remainder 증거가 아니다.

## 남은 실제 연결

1. CommonFamily → trusted amplitude producer adapter가 없다. accepted_half1_amplitude_producer 내부에는 λ/b endpoint 경로가 있지만 private Phys04ExactPermit의 issuer는 없다.
2. 기존 hh_stage_root_amplitude_inner는 scalar λ의 point solve와 Krawczyk root enclosure다. λ,b rectangle 전체의 root/tangent tube가 아니다.
3. src/certificate.rs::export_derivatives는 clock/density/source/b-rectangle seal 이후 호출자가 공급한 gas 및 tangent box에서 산술을 계산한다. NativePointCertificate와 NativeFamilyTube에는 constructor가 없고 request_native_family_certificate는 항상 거절한다. native_root_certified=false다.
4. 실제 full/half1/half2 four-corner 반환값, actual U,V,W, \(D_h\), \(I_h\), HH/mixed scheme defects는 null이다. 독립 continuous source-law target과 time remainder도 없다.
5. authorization=null, budget=0이다. 1 macro / 4 corners / 12 endpoints 제안은 권한이 아니다. 과거 identity-only lease도 미래 실행의 live identity가 아니다.

다음 NCP 작업은 완료한 기반에서 CommonFamily adapter와 PHYS06 uniform theorem의 source-bound interval exporter, 실제 premise 생성 경로를 이어야 한다. sealed 원 owner snapshot과 기존 ON history를 보존하고 native 실행 허용과 수학적 충분조건 충족을 각각 판단한다. λ=0을 원 archived ON→OFF byte retag로 구현하지 않는다.

## Energy 좌표의 직접 source 결합

source의 matter energy
\[
e=w+\chi_{\rm H}x+
f_{\rm He}\chi_{\rm HeI}y_1+
f_{\rm He}(\chi_{\rm HeI}+\chi_{\rm HeII})y_2
\]
는 기존 coupled_primary::energy에서 escape와 photon energy를 제외한 값이다. 기존 energy 함수 전체는 \(e+e_{\rm escape}+\sum_jE_jP_j\)를 계산한다.

HHeModel::controlled_fixture의 threshold literal [13.598_434_599_702,24.587_389_011,54.417_76]는 coupled_primary::CHI와 같으며 Ft03Model::controlled가 바꾸지 않는다. AtomicProvider의 fit cutoff [13.60,24.59,54.42] eV는 별도다. HI 13.60 eV를 binding energy 13.598434599702 eV로 대체하지 않는다.

FT03 event ledger에서 CI thermal loss \(-\chi_a\,{\rm CI}_a\)는 binding gain과 상쇄된다. RR escaped energy는 binding+kinetic, DR escaped energy는 HeI binding+DR energy다. 다만 source의 density leaf를 유지하면 nonphoto 성분에는 작은 정규화 보정이 필요하다. model(stage)는 \(n_{\rm He}=\mathrm{fl}(n_{\rm H}f_{\rm stage})\)를 저장하고 FT03 interval 식은 \(\tilde f=\mathrm{exact}(n_{\rm He})/\mathrm{exact}(n_{\rm H})\)를 사용한다. energy ledger 및 photo 식은 \(f_{\rm stage}\)를 사용하므로 정확한 관계는
\[
s_{f_{\rm stage}}F_{\rm np}=-L_{\rm escape}-2H_{\rm mean}w
+\delta f\left[\chi_{\rm HeI}F^{(0)}_{y_1}+(\chi_{\rm HeI}+\chi_{\rm HeII})F^{(0)}_{y_2}\right],
\]
\[
\delta f=f_{\rm stage}-\tilde f,\qquad
L_{\rm escape}=\frac{{\tt rhs.escaped\_energy\_rate}}{n_{\rm H}\,{\tt eV\_erg}}.
\]
여기서 \(F^{(0)}\)는 photo를 제거한 FT03 chemical RHS다. 원 archived t0 입력의 정확한 density leaf로 계산하면 \(\delta f=3.9213377261891804541504\ldots\times10^{-18}>0\)이다. 제안 half/full 시각의 진단 density에서도 각각 \(7.32582781528316\ldots\times10^{-18}\), \(3.80578358513024\ldots\times10^{-19}\)로 0이 아니다. SOURCE_DENSITY_LEAF_CORRECTION.json에 정확 유리수와 직접 source 결합을 보존했다.

최초 intake의 무보정 등식은 이 차이를 놓쳐 이론/대수 수준에서 정정했다. 최초 보고서는 SOURCE_INTAKE_PRE_DENSITY_CORRECTION_KO.md에 남겼다. source를 임의로 renormalize하지 않았고 원 input JSON의 바이트도 바꾸지 않았다. 위 관계는 source 식의 직접 대수적 결합이며 새 native trajectory 검증이 아니다. HH의 direct contribution \(q(1,0,0,-\chi_{\rm H})\)에는 \(sH=0\)이 정확히 성립한다. 상태 변화에 따른 간접 HH 영향까지 0이라는 뜻은 아니다.

직접 근거는 candidate/src/hhe_events.rs L61–77, ft03_controlled.rs L112–169, coupled_primary.rs L216–294, hh_primary_extension.rs L49–80이다. 33-node grid는 10–20 eV이므로 HeI/HeII cross-section은 모두 0이다. 고정 stock \(N_j\)와 \(d>0\)의 energy-row photo curvature는 HI 한 방향에만 있다. active \(N_j>0\)가 존재하면 이 부분 Hessian은 rank 1이다. 일반 3-species 이론과 이 snapshot 특수화를 구분한다.

## 원 COMMON seed에서 얻은 입력

ARCHIVED_COMMON_SEED_POINT_INPUT.json은 원 seed byte를 hh_checkpoint_encode/decode 저장 layout에 따라 읽은 결과다. 새 extractor는 원 native decoder를 실행하지 않고 Python struct로 필드를 추출한다. SHA-256, Git blob SHA, FNV checksum, 총 읽은 byte 수, packet energy의 고정 node bit 일치, gas/photon point의 저장 box 포함을 확인했다. 기존 native decode/encode roundtrip 증거는 v2 targeted 기록에 있다.

| 양 | 원 snapshot 또는 명시한 source 산술 |
|---|---:|
| time | \(1.6\times10^{11}\) s |
| \(x_{\rm HII}\) | 0.9131385026926517 |
| \(x_{\rm HeII}\) | 0.300035085528747 |
| \(x_{\rm HeIII}\) | 0.5999927594007611 |
| \(w\) | 13.565646600651332 eV/H |
| \(f_{\rm He}\) | 0.083 |
| source \(\mathbf H\) | \((10^{-14},10^{-14},10^{-14})\ {\rm s}^{-1}\) |
| source 식에서 계산한 \(n_{\rm H}(t_0)\) | \(9.952115015900972\times10^{-5}\ {\rm cm}^{-3}\) |
| source 식에서 계산한 \(T\) | 49489.0775133998 K |

단위 상수, source/birth 상수, HH fit constants는 checkpoint identity words에서 직접 읽었다. 제안된 macro \(1.25\times10^9\) s와 half \(6.25\times10^8\) s는 NCP_RETURN의 미래 계약 값이며 새 실행 결과가 아니다.

33개 group의 원 stored primary packets와 128방향 photon의 정확 유리수 합을 별도로 보존했다. 두 표현 사이 최대 point 차이는 \(5.421010862427522\times10^{-20}\ {\rm H}^{-1}\)이므로 동일 byte가 아니다. 이 값들은 archived old state이며 다음 endpoint remap/birth를 거친 preBE state가 아니다.

cross-section 표는 고정 provider 식과 binary64 상수를 Python math로 전사한 점별 진단값이다. 99번 scalar formula call을 기록했으며 NCP Rust/libm bit identity를 새로 인증하지 않는다. HI는 13.6 eV에서 \(6.346296358990503\times10^{-18}\ {\rm cm}^{2}\), 13.7 eV에서 \(6.22255406204696\times10^{-18}\ {\rm cm}^{2}\)다. source coefficient diagnostic에는 사용할 수 있으나 native root 또는 uniform enclosure의 대체물은 아니다.

## 파일과 고정 범위

SOURCE_INTAKE_MANIFEST.json은 원문 34개 각각의 repo path, Git blob SHA, SHA-256, byte size, 고정 raw URL, snapshot 경로와 read_scope를 담는다. 파일 전체를 회수했더라도 전부 의미 검토했다고 표시하지 않는다. SOURCE_INTAKE_SUMMARY.json은 완료/미완료 및 call-counter, package 포함 목록을 기계가 읽을 수 있게 보존한다. COMMIT_IDENTITY.json은 core→전달 commit→head 관계다. 새 extractor와 입력 JSON은 원 repo source와 구분한 derived artifact다.

source intake는 여기서 freeze한다. PHYS06의 새 archived-energy diagnostic은 별도 실행 기록을 사용하며 이 원문 회수 또는 이전 oracle의 재실행으로 세지 않는다.
