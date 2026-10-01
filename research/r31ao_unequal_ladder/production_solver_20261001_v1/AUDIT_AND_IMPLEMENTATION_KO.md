# WU088_HH 원 연구 단계 재점검과 수치 solver 연결부

**원 G0–G9 연구 작업은 전부 완료되지 않았다.** 이번에는 Drive·Dropbox의 관련 DB 계보와 원 사용자 프롬프트를 다시 대조했고, 실제로 빠져 있던 수치 연결부를 구현했다. 실행 가능한 정확 유리수 부품은 실행했지만, 전체 HH production solver나 실제 최종 D 인증이 완성됐다고 주장하지 않는다.

기준 프롬프트는 원 attachment 31,861 bytes, SHA-256 `70071962a6b3dc3cfc0c01034c0d1b6f57711833957510a77b0bb6c4e453969e`다. 과거 G0 SSOT에 기록된 입력 hash와 일치한다. 보고서의 재구성 문장이나 최신 coordinator 요약을 원 지시로 대신하지 않았다. 기준 원격 HEAD는 `72ff754814c24e6993092944f5159d400129ae23`이며, 회수된 기존 파일 576개의 Git blob이 해당 tree와 모두 일치했다.

## 데이터베이스 재조사

Dropbox canonical 폴더 123개, dossier 직접 항목 2,316개, 추가 WU088 폴더 11개·476개 descendant를 각 pagination 종료까지 확인했다. Drive canonical 폴더는 122개이며 발견한 WU088 폴더 12개를 조회했다. Drive 전역 document 검색은 100+31개로 종료됐으나, 검색이 일부 알려진 archive를 누락하고 상위 folder listing은 1,000개 cap이다. 따라서 이 조사를 모든 계정의 모든 하위 파일에 대한 전수 조사로 표현하지 않는다.

| DB 계보 | 실제 내용 확인 | 확인된 내용과 한계 |
|---|---|---|
| v1 acquisition | 완료 | sources 67, assets 60; integrity 정상, FK 위반 0 |
| v2 acquisition | 미완료 | `aff168…c1c6` manifest identity 확인. Drive 전송 403, 대형 archive 복원 502로 SQLite bytes 미검사 |
| 부분 재구축 연구 DB | 완료 | sources 4, blockers 5; theorems/code_modules/tests/artifacts와 관계 테이블은 0행 |
| v3 acquisition | 완료 | canonical sources 68, historical records 79, acquired files 66; integrity 정상, FK 위반 0 |
| 원 Deep Research DB | 미복구 | 보고된 원 ZIP hash `ab875d…48a9`의 원본 bytes를 조사 범위에서 찾지 못함 |

검사한 SQLite는 모두 읽기 전후 hash가 같았다. v1의 source ID 67개와 asset ID 60개는 v3에 모두 보존됐고, 공유 asset의 hash 변경은 없었다. 따라서 v3는 유용한 문헌·코드 수집 DB다. 다만 문헌 수집 성공을 원 연구 DB의 모든 정리·모듈·시험 entity 복구나 solver 인증으로 읽을 수 없다. 반대로 원 entity 행의 미복구가 이후 저장소의 T1–T5 증명문서 부재를 뜻하지도 않는다.

R10의 이름에 “production”이 들어가는 보고서도 본문은 당시 **HOLD**였다. 제한된 radial component와 168행 O/D runstore 재사용이 기록됐으며, runstore의 실제 underlying DB schema는 작은 보고서·receipt만으로 확인되지 않았다. 이 역사적 결과를 최신 전체 HH 인증으로 승격하지 않았다. BASS_HE 자료도 별도 물리 모형으로 구분했다.

이번 `current_audit.sqlite`는 원 프롬프트의 10단계·15개 완료 조건·6개 blocker를 현재 source/evidence와 연결하는 **새 감사 DB**다. 잃어버린 원 DB를 복구한 파일로 표시하지 않는다. 정제한 provider 목록과 원 DB의 검증 상태를 함께 보존하고 SQL dump로 재생성할 수 있다.

## 원 연구 단계의 현재 상태

| 단계 | 현재 확인한 것 | 아직 필요한 것 |
|---|---|---|
| G0 intake | 원 프롬프트, 양쪽 provider, DB 3종 실내용 및 계보 대조 | v2 실내용·원 DB 복구 한계는 명시적으로 남음 |
| G1 theorem | T1–T5의 source-specific 증명·검토 문서와 실행 witness | 실제 backend·domain·feasibility 전제 충족; 일반 T1/T2/T4 fallback 제어기는 별도 미구현 |
| G2 decoder | exact NPY decoder, binary64 Frozen107 adapter와 원본 입력 복원 | historical B192 longdouble/complex producer ABI admission과 실제 decode |
| G3 Gram/gap | exact Gram·outward radical 부품 및 새 T5 연결 검증 | 실제 raw/model의 represented gap |
| G4 callback | native Acb callback, source-bound primitive worker 후보 | 고정 backend의 실제 컴파일·링크·callback 검증 |
| G5 endpoint | 2592 task 계획, signed donor 절댓값 합, 정확한 tail evaluator; 실제 입력의 제한된 component 실행 | 모든 필요한 primitive의 충분한 cutoff·최종 오차 예산 |
| G6 interior | whole-outer-box Petras worker와 exact endpoint serializer 후보 | 실제 accepted interior 구간, 폭·시간·메모리 측정 |
| G7 full D | 기존 source-prescribed assembly와 새 연결부 | 2592개 실제 full-domain 구간, 실제 최종 D_col/D_row balls |
| G8 decision | T5 sharp C/R/K 오차와 frozen real Pareto 조합기 실행 | 실제 ε·gap 및 실제 최종 판정; historical machine replay 권위는 별도 |
| G9 review | 독립 component 코드·수학 검토 | 완성된 실제 certificate에 대한 독립 과학 판정 검토 |

전체 15개 완료 조건의 개별 상태는 `audit/STAGE_AUDIT.json`에 있다. 특히 실제 D balls, ε_C/R, represented model gaps, interior feasibility가 아직 없으므로 “모든 연구 단계 완료”나 “source accuracy bound 확보”로 상태를 바꿀 수 없다.

## 이번에 구현한 실행 연결부

`composition/`은 47×2 및 2×47 exact complex 행렬과 최종 entry disks를 받아 T5의 centered spectral residual을 계산한다. K의 중심 상쇄와 각 모델에 독립 저장된 K를 보존한다. 직접 continuous-target gap과 represented-gap ±2ε를 교차시키고, 원 strict/weak Pareto 경계를 유지한다. synthetic 예시에서는 ε_C=ε_R=1/1000, ε_K=0을 얻었다. 이는 실제 HH ε가 아니다.

`endpoint_tasks/`는 원 NPZ를 재검증한 뒤 2592개 source-bound task를 만든다. 각 primitive에서 107개 저장 donor 항의 기여를 빠짐없이 합하고, 같은 k의 field majorant와 같은 (i,j)의 density 경계를 재사용한다. 정확한 0만 생략하며 floating screening은 없다. resource cap 초과는 INCONCLUSIVE이고 기존 완료 결과는 identity를 확인해 재사용한다.

`native_driver/`는 실제 Frozen107 initializer, canonical geometry, whole-parameter-box nested Petras를 연결한다. 성공한 Arb 구간은 integer mantissa와 binary exponent로 내보내며 decimal/binary64 반올림으로 certificate 데이터를 전달하지 않는다. precision·평가 횟수·벽시계·메모리·기존 output 재실행을 제한한다. 현재 C++ worker는 **native 미컴파일·미실행 후보**다. Python 경계 시험은 그 상태를 바꾸지 않는다.

`primitive_join/`은 endpoint와 native 결과를 결합해 2592개 coverage를 검증하고, native assembly initializer 및 exact final rectangle→disk importer를 제공한다. 최종 assembly의 자동 host build/run wrapper는 외부 단계로 남는다. 새 Python·정확 산술 component 시험은 composition 21개, endpoint 17개, native wrapper 11개, join 10개로 합계 59개가 통과했다. 반복 실행이나 독립 부등식 probe를 이 숫자에 중복 합산하지 않았다. endpoint radius는 compact rectangle에 한 번만 더해야 하며, 이후 rectangle→disk에서는 모서리 거리를 outward 계산해야 한다. 전 primitive의 source/window/backend identity와 완전성을 확인해도 임의 JSON의 self-hash가 과학적 증명이나 실제 native 실행 증거가 되지는 않는다.

실제 Frozen107 원본 NPZ는 5,681 bytes, SHA-256 `8482d2854ab620c58bb1d7a7a45cf88eb71fd75081242263a9ef48927f0a282c`로 복원했다. `runtime/`에 실제 endpoint-only 실행 scope, task 결과와 요약을 보존한다. 첫 coarse window `[1/4,4]^2`의 primitive 0은 107개 항, engine call 39회, component 약 0.127초로 끝났지만 tail 상계는 약 `7.41e17`이었다. 이 값은 정규화 전 단일 primitive의 보수적 bound이며 결정에 유용한 최종 ε가 아니다. 그 뒤 3개 cutoff의 첫 시도는 유리수 표현 제한으로 실패했다. 상향 dyadic 압축으로 이를 고친 뒤 3개가 계산됐지만, 고정 panel의 J_t 상계가 큰 T에 비례해 불필요하게 커지는 현상을 발견했다. J_t를 전체 양의 축 질량 상계 W_t와 비교해 min(J_t,W_t)를 사용하도록 개선했다. 이는 같은 내부 영역에 대한 두 유효 상계 중 작은 값을 택하므로 포함 관계를 보존한다. 최종 3개 시도는 모두 끝났고, W3=[1/256,2^192]^2에서 계산된 단일 primitive endpoint 상계 B는 **2^-21 ≤ B < 2^-20**이었다. 이 넓은 내부 영역을 실제로 적분한 결과는 아니다. 전체 실제 endpoint 시도는 10회(조건부 bound 7회, 보존된 실패 3회), native 적분은 0회다. 실패와 두 개선 단계의 원 코드·plan·receipt를 모두 보존했다.

## NCP 실행과 성능

현재 작업 환경은 CPU quota 8, 메모리 8GiB다. 요청한 64코어·128GB NCP의 연결된 실행 환경이 아니다. GCC는 있으나 고정 FLINT/GMP/MPFR 개발 환경, gfortran, MPI가 없고 m4·pkg-config도 없어 여기서 native build 성공을 주장할 수 없다. 시스템 library 이름이 보인다고 고정 backend provenance를 대신하지 않았다.

우선 NCP에서 고정 backend의 build/link identity와 native analytic tests를 검증한 뒤, 같은 입력·같은 cutoff의 한 primitive를 받아들일 수 있는지 측정해야 한다. 그 결과로 precision/cutoff를 정하고 독립 primitive를 병렬 실행한다. 각 worker 안의 Arb 연산은 한 thread로 시작하고, 실제 CPU affinity·quota·메모리로 동시 작업 수를 제한한다. 기존 Fortran/OpenMPI dispatcher 후보와 연결할 수 있지만 실제 MPI 컴파일·64코어 속도 향상은 아직 측정되지 않았다. exact 연산을 binary64 SIMD로 바꾸는 최적화는 적용하지 않았다.

다음 실제 인증 순서는 pinned backend 검증 → 한 primitive의 achieved-radius/cost pilot → 전체 primitive coverage → native final assembly와 exact export → admitted raw/model decode → T5 composition → 독립 최종 판정이다. 최신 사용자 요청은 이 구현·실행을 진행하라는 권한으로 기록했다. 오래된 `execution_authorized=false`를 다시 허락받아야 하는 이유로 재사용하지 않는다. 지금 남은 핵심 제약은 실행환경과 아직 없는 실제 수치 증거다.

전체 scattering production은 선택한 z=3/4 D 인증보다 넓다. 새 위치의 독립 dotO/ionic provider, full49, propagation 및 관측량 gate는 해당 증거로 별도 검증해야 한다. 이 delivery는 기존 B128/B160 완료 상태나 frozen model을 바꾸지 않고 같은 branch에 추가된다.

게시·백업의 실제 성공 여부와 새 commit/package identity는 detached delivery receipt에 기록한다. 업로드 후 metadata ACK와 전체 원격 restore 검증도 구분한다.
