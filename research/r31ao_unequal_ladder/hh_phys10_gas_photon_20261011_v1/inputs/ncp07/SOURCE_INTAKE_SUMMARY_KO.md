# PHYS08 intake — 새 PHYS07 NCP 반환과 다음 물리 의무

## 판정과 출처

PHYS07 NCP 반환이 새로 존재한다. 현재 읽은 NCP branch는 `codex/hh-phys07-ncp-20261011`, head는 `4d5c18b8a6d348e2de42b5e12dc0fd4d753add7b`, head tree는 `5f418eda6613d0e69bf5404a43d7598a60f54ded`다. 과학 core는 `dfa574ce2c302ff2dce38d0e487903d57f1db977`, core tree는 `fbca3981915bcc9d34659ec5c776a6989ebac9c2`이며 부모는 이전 NCP06 head `65a36e255aa6d9911e23a9b5ced18d8a9f507606`이다. [PR #37](https://github.com/cosmosapjw-quantum/WU088_HH/pull/37)은 open이고 merge되지 않았다. Core는 2026-10-11 04:31:22 UTC, delivery commit은 04:37:02 UTC다. 연구 PHYS07 [PR #36](https://github.com/cosmosapjw-quantum/WU088_HH/pull/36)의 head `e9272a1ffe0bd012e4e34718b7b2576bfd26772e`는 읽은 시점에 그대로다.

이번 intake는 새 source/evidence의 선별 읽기와 byte identity 검증이다. 과학 실행, source/provider/native 호출, build, test, 원격 mutation은 모두 수행하지 않았다. NCP 최초 실행과 독립 판정은 보존된 원본으로 수신했으며, 이 intake가 그 과학 실행이나 독립 심사를 다시 수행했다는 뜻은 아니다.

`raw/`에 선별 원본 81개, 2,596,971 bytes를 저장했다. 모든 파일은 authoritative Git tree의 blob SHA1과 size에 일치한다. 원 NCP package manifest에 포함된 선별 69개는 기록된 SHA256과 size에도 일치한다. 전체 195개 payload 및 대형 binary/geometry trace를 새로 내려받지는 않았다. 파일별 출처·Git blob·SHA256·size와 적용 범위는 `SOURCE_INTAKE_MANIFEST.json`, 구조화 결과는 `SOURCE_INTAKE_SUMMARY.json`에 있다.

## 새로 완료된 NCP 의무

공개 `phys04_prepare_family`와 `phys04_reduced_residual`을 같은 입력·PreBE 객체에 결박하는 source producer가 구현됐다. Whole gas X × whole Theta와 gas center × whole Theta의 export를 stage마다 한 번씩 보존한다. Native scalar leaves, signed 7-slot Jet, Hessian, stored input, geometry trace와 각종 byte pins가 함께 저장됐다.

실제 두 first target은 다음과 같다.

| Target | 시간 폭 | Exit | Elapsed | RSS |
|---|---:|---:|---:|---:|
| `phys07_sourcebox_full_first` | 1.25e9 s | 0 | 2.087629672999924 s | 44,040,192 bytes |
| `phys07_sourcebox_first_half_first` | 6.25e8 s | 0 | 2.1109214340000335 s | 44,040,192 bytes |

두 target은 같은 실행 binary SHA256 `8dfd6eaf24c827cdd199fc7e07b4e44335d9876413503022c4352ccfc8549416`을 before/after에 기록했고, source 변경·source 실패·재실행은 없다. Build는 한 번, 12.874553323999976 s에 exit 0이었다. 실제 합계는 PreBE 2, reduced residual 4, FT03 4, HH 4, provider channels 396, uniform root arithmetic 2다. 구분된 native endpoint/point/internal-point/root counter는 0이지만, 계측하지 않은 IVP/heavy/old-suite/certificate-producer 등의 필드는 `null`이다. 금지 또는 ceiling 0을 관측값 0으로 바꾸지 않는다.

조건부 uniform 산술은 full `q.hi=1.1736830563768177e-4`, first-half `q.hi=5.8538714993538125e-5`이고 strict image margin은 모든 성분에서 양수다. 이 결과는 고정 coefficient 실수 source의 수학적 조건부 산술이다. Native solver/root certificate 또는 실제 U/V/W/I를 발행한 결과가 아니다. First-half는 동일 COMMON에서 시작하는 첫 반단계이며 두 번째 carried half가 아니다.

독립 판정 `review/DECISION.json`은 **APPROVE**다. 범위는 source producer, 보존된 source export, fixed-coefficient real-source C²와 conditional uniform arithmetic이다. Reviewer는 후보·이론·테스트 비생성자였고 scientific execution/build/test/provider/ref replay가 모두 0이었다. 177개 동결 파일의 크기·SHA256과 source aggregate를 검토했다. Scope 밖으로는 native authority/root/U/V/W/I, finite energy sign, carried second-half, paired defect, time/continuum remainder, physical adequacy, full49 및 production이 남아 있다.

## 새 blocker의 정확한 내용

두 `SOURCE_DIRECTIONAL_WITNESS.json`은 OPEN이다. 기존 witness는 각 nonzero interval birth derivative와 각 `physical_incoming.hi>0` 노드에 대해 `a_heat*p<w`를 요구한다. Node 32는 E=20 eV이고 다음 raw interval을 가진다.

- Physical incoming value: `[0,128*min_subnormal]`, endpoint bits `0000000000000000`와 `0000000000000080`.
- Birth derivative M: `[-128*min_subnormal,+128*min_subnormal]`, endpoint bits `8000000000000080`와 `0000000000000080`.
- `a_heat*p`: `[13.475359183281284,13.69928594098373]` eV/H.
- Gas thermal w: 약 `[13,14]` eV/H.

따라서 node 32에 대한 충분조건은 닫히지 않는다. 이 OPEN은 원 과학 데이터에 남겨야 한다. Tail 삭제, epsilon threshold, clipping, support screening으로 바꾸면 다른 데이터와 다른 증명이 된다. 저장된 negative AD projections와 closed formula의 overlap만으로 두 계산의 동일성도 증명되지 않는다.

동시에 모든 source birth와 전체 photon stock이 서로 다른 객체라는 점이 중요하다. `P_M`은 incoming의 b derivative를 사용한 birth 방향 source이고, `P_N`은 기존 stock 및 현재 birth를 모두 포함한 실제 photo source다. 현재 witness가 하나의 `support` 변수로 두 충분조건을 함께 검사하므로, 전체 stock node의 좁은 냉각 실패가 birth-only 설명까지 OPEN으로 만든다. 이 사실 자체가 native source의 부호 반전을 뜻하지 않는다.

## 생산적인 다음 물리 연구

전체 photo source와 birth-direction source 각각에 대해

\[
B(v)=p\,v_w-w\left(v_x+\hat f v_{y_1}+2\hat f v_{y_2}\right),\qquad
DT[v]=C\,B(v)/p^2
\]

를 사용하면, 모든 노드가 따로 냉각해야 한다는 충분조건을 제거할 수 있다. `P_N`에는 저장된 `SOURCE_BOX_COMPONENTS.json`의 33×3 rates를, `P_M`에는 같은 source에서 보존한 b derivatives를 사용한다. 모든 signed tail을 유지한 채 합계의 포함값을 직접 판정해야 한다. 이 weighted 조건은 기존 node 32 OPEN을 숨기지 않고 더 넓은 수학적 충분조건을 새로 제공한다.

그 다음 HH source `H=q(1,0,0,-CHI_H)`의 방향미분을 실제 source graph로 연결하면 된다. Source 수준의 상호 억제, finite birth amount와 source-rate의 관계, 전체 stock 및 birth 방향의 온도 부호를 구별해야 한다. 유한 implicit interaction으로 확대하려면 saved whole-domain export와 uniform existence/regularity를 다시 같은 family에 명확하게 결박하는 논증이 필요하다. Native authority 필드는 별개로 유지한다.

Root 요청에 따라 두 stage의 `SOURCE_BOX_COMPONENTS.json`도 추가 복구했다. 각 파일은 554,961 및 554,945 bytes이며 모든 rate value/gradient/Hessian이 들어 있다. 추가 source 평가가 필요하지 않다. Root가 정한 새 bounded artifact-arithmetic 계약 아래 사용할 수 있다. PHYS07의 두 source target 예산은 소진됐고 그대로 보존된다.

## 별도로 가능한 structural birth 명제

현재 source를 읽으면 underlying fixed-coefficient real family에서 future birth derivative의 구조적 support는 `{24}`라는 명제를 세울 수 있다.

1. `src/family.rs`의 `CommonFamily::initialize`는 입력 gas/photon/guard를 `Jet::constant`로 만들어 future b derivatives를 0으로 시작한다.
2. `candidate/src/phys04_transport.rs`의 remap, fixed geometry, source weights는 b에 의존하지 않는다.
3. `source_n=b*constant(fl(dt*SOURCE))`를 구성하고, born은 `out[d*n+3*spectral_subdivisions]`, 즉 node 24에만 더한다.
4. Grouping은 128방향의 합이다. 실수 식의 정확한 derivative support와, 모든 덧셈에서 nextafter를 적용하는 interval implementation의 포함폭은 서로 다른 개념이다.

이는 원 numerical array를 수정할 근거로 쓰지 않는다. Source-derived sidecar 명제로 독립적으로 검토할 수 있고, 특히 전체 physical stock의 node32 tail을 제거하는 근거와 혼동하면 안 된다. Current source identities는 다음과 같다.

| Source | SHA256 | Git blob SHA1 |
|---|---|---|
| `src/family.rs` | `52fc20bb0fb51d93d6c3d72860f8356f978ecea49708f1e7af58a32b08887cd9` | `1062366e6321b89cde0e592472353500f865a380` |
| `candidate/src/phys04_transport.rs` | `aa7b7ebc83ce1c191fdfbf7039f2a1810caff22ec0744d9802f53832770f6b97` | `ed4b24ae41bf1657b59a299ddbdeae9c8c14f389` |
| `candidate/src/interval_math.rs` | `e4639a4386feee536dbe7e7ffb1260f26fa00697b6b05477083c182ddf03de18` | `c33a2c91ec5be0a3d9e97c26098f6ba2cb7b5f5e` |
| `candidate/src/hh_primary_extension.rs` | `f47d910abb096f96b829e3392fdfbf55d079ba2fbb09a45416c97c76a4f4a647` | `3e8042094d95dc2f5d37d41204cab2576b82c1d6` |
| `src/sourcebox.rs` | `d771968e9c12c0cce5a9e3ec5fa7311d0040ac63d1f4f4a6f54f048972f674ae` | `7a6c6f7e357726b8a5f04fd8e7cac1cd11823f7f` |

원 파일은 `https://github.com/cosmosapjw-quantum/WU088_HH/blob/4d5c18b8a6d348e2de42b5e12dc0fd4d753add7b/research/r31ao_unequal_ladder/ncp_phys07_local_20261011_v1/` 아래에 있다.

## 전달 상태와 한계

원 NCP archive는 `WU088_HH_PHYS07_NCP_LOCAL_20261011_v1.zip`, 5,644,521 bytes, SHA256 `4ea6b7dbbc714493ac85f944a65a353a1ee75abf5742c3e7ce65a7df56cc3465`, MANIFEST SHA256 `720b32730fba9f759d52b5b6f3e222553e673c18710087177ee2a656e58d49ca`다. Drive ID는 `1NsBdq3WAvNWVOmS7Yfpcib99nDKVrZ6H`, Dropbox ID는 `id:BSpOijBcT10AAAAAAD4FPg`다.

원 `RESTORE_VERIFICATION.json`에는 두 provider에서 실제 다운로드한 archive bytes/SHA, ZIP CRC 및 195개 payload를 확인했다고 기록돼 있다. 이번 intake가 새 restore를 한 것은 아니다. NCP individual Dropbox START upload에는 FETCH_FAILED가 있었고, 정확한 전달 파일들을 51,883-byte delivery bundle에 담아 두 provider에 업로드한 최종 영수증이 있다. Archive restore와 이 delivery bundle의 ACK, 각 개별 파일의 ACK를 구별한다.

Repository `AGENTS.md`는 확보했다. `research/`, `research/r31ao_unequal_ladder/`, 새 NCP package 안에는 중간 `AGENTS.md`가 없다. Repo 지침의 필수 read 목록은 구조화 summary에 기록했다. 기존 과학 성공을 포맷·반복 검증만으로 연장하지 않고, 위 weighted source 명제와 다음 실행 가능한 소비자를 만드는 것을 PHYS08의 실제 진전으로 권고한다.

## AGENTS 필수 baseline 읽기 완료

같은 pinned NCP head에서 `raw/repo/README_KO.md`, `raw/repo/docs/research/RESULTS_KO.md`, `raw/repo/docs/coding/IMPLEMENTATION_PLAN.md`, `raw/repo/evidence/FINAL_VERIFICATION.json`을 추가로 복구하고 전체 내용을 읽었다. 네 파일 모두 authoritative Git blob·size와 일치한다. 이 문서들은 inherited R31K-B source-bound scattering/component lane의 역사와 실행 제한을 설명한다. Frozen source 보존, 기존 완료 anchor 재실행 금지, 독립 dotO/full49 gate, numerical equivalence와 production admission 분리가 현재 작업과 일관된다. 문서의 benchmark/pytest/scheduler 예시 명령은 실행하지 않았다. Legacy 결과를 PHYS07/08 물리 source 결과에 대입하지 않는다.

필수 baseline 읽기 전의 manifest·JSON summary·한국어 summary 원본은 `prior_to_required_baseline_reads/`에 bytes 그대로 보존했다. 기존 raw source와 READ_RECOVERY_LOG.json은 변경하지 않았다. 최종 원본 선택은 81개, 2,596,971 bytes이며 원 NCP manifest 대상은 그대로 69개다. 과학/native/provider/build/test/원격 mutation은 모두 0을 유지한다.
