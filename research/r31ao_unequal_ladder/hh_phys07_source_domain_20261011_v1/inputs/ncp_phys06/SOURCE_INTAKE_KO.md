# PHYS07 최신 NCP source intake

PHYS06 NCP의 새 nonnative 구현 반환을 확인했다. `codex/hh-phys06-ncp-20261011`의 현재 head는 `65a36e255aa6d9911e23a9b5ced18d8a9f507606`, 구현 core는 `927019cff541e8a4a1f0d2c8846f1466d6b70533`다. 기존 연구 PR35의 head `baf23360627bc1c6d10aac5317052f23edafd1b1`과 NCP v2 head `4b9231a0eff113701e7178ad98624233f387dd15`은 그대로다. 새 NCP branch를 head로 지정한 PR 조회 결과는 비어 있다. 이것은 조회 시점의 관측이다.

고정 source 82개, 총 499706 bytes를 선택했다. `SOURCE_INTAKE_MANIFEST.json`에 각 파일의 실제 SHA256, Git blob SHA, 원래 저장소 경로 및 intake 방법이 있다. Manifest SHA256은 `fdecbf0c21d90cae761899d75442b14211f99c56cb45b9f153fe44a36d8ea48b`다. 읽기 전용 Git identity 확인이며 과학 검산 재실행이나 ZIP 복구 반복이 아니다. 기존 local source 9개는 새 tree의 동일 blob/size에 연결하여 재사용했다. 빈 로그는 remote tree가 나타내는 0-byte empty blob를 정확히 물질화했다.

## 채택할 신규 상태

- NCP의 T01–T07은 승인된 source 이식과 조건부 산술·제한 검증·전달 범위에서 완료됐다. ell*G/Jnorm/Psi의 full Jet, S/Q 변환, uniform root/linear 조건부 산술, U/V/W, finite/observable/paired adapter가 추가됐다.
- 새 target 6개는 최초 실행 PASS였고 manufactured fixture의 1회 recheck도 PASS였다. 전체 기록은 build 7회, target 7회다. 최초 두 build 오류 E0624/E0284와 수정, independent review REQUEST_CHANGES 및 같은 finding 수정 closure가 보존됐다.
- 마지막 observable gradient widening 이후에는 target을 다시 실행하지 않았다. 최종 narrow build PASS와 interval monotonicity의 source 검토만 있다. Final binary pin을 앞선 6개 target 실행 binary로 소급하지 않는다.
- 독립 NCP decision은 `APPROVE_SCOPED_IMPLEMENTATION`이다. 조건부 nonnative 구현에만 해당한다. 실제 source callback counters와 native endpoint/conservative/internal-point/root counters는 해당 target에서 0이었다. 별도 계측하지 않은 IVP/heavy/old-suite/receipt-specific counts는 반환 원문처럼 null로 유지한다.
- actual source-wide Gc/A/full mixed partials, C² chart, root/tube, U/V/W, finite I, paired mixed defect, continuous/time remainder는 null/HOLD다. `src/adapter.rs::bind`는 actual source enclosure 부재를 typed `Unresolved`로 보존한다.

## 실제 새 pins와 전달

| 항목 | 값 |
|---|---|
| NCP head tree | `f823df8c95defcaba737139859cd9eeeda4ef133` |
| Implementation core tree | `f156e72d5e58d4c6efa840606af28e43aa014e6f` |
| Full new source SHA256 | `26a7136322696aaf1dd65a13987d437ee8dfd86ed8967e6db1a224d828fb01f6` |
| Candidate source SHA256 | `14b1d1e76f54175069020fb49568f8a3c16571620fd69a532afaed73bb34a207` |
| ABI SHA256 | `149b59c50ceec2a7d6c1beef54490181dd4aeefaa473e356810abd02133f2ea9` |
| Final build binary SHA256 | `36bc9ad2f95d214d1a0b1abe4fd44623c5dd1aea6e1e67cbc3eb28c9bd12363d` |
| NCP ZIP SHA256 | `f4ca1d2169628dfdb4966de27435f8f32d804193dada62468a1611cc6bef12ad` |
| NCP ZIP bytes / entries | 4005923 / 174 |
| NCP archive manifest SHA256 | `31dd9f0aef182e0ccd1d350c44415f2e1e57a2402a279c5b9d5dfce6a2dc36d6` |
| NCP detached receipt SHA256 | `713fc394a425fbd1c207ff4f8f5fbf68eb808a47b07b57d5c425eb1f964c8a19` |
| ZIP Drive ID | `1AcrHu25VfLsxIoeIsRZgyq8wl-8vMP8t` |
| ZIP Dropbox ID | `id:BSpOijBcT10AAAAAAD3_Rw` |
| Receipt Drive ID | `14UA1q4TPeVCHPOyTrrW8vPbLUqXSeLUW` |
| Receipt Dropbox ID | `id:BSpOijBcT10AAAAAAD3_SA` |

NCP가 남긴 고정 delivery 기록은 두 provider의 ZIP 및 receipt를 실제 다시 내려받아 검증했다고 보고한다. PHYS07 intake는 그 원문과 Git identity를 읽었으며 두 archive를 다시 내려받지 않았다. 원래 수행자의 restore evidence와 이번 intake의 identity 확인을 구분한다. 새 worker/live execution을 과거 build PID, binary 또는 provider ACK로 증명하지 않는다.

## 다음 물리 목표에 직접 도움이 되는 결론

기존 v2 대비 native source의 유일한 delta는 `phys04_mixed.rs`의 metadata export 추가다. FT03/HH-rate/transport/rounding 식은 같다. 따라서 다음 연구는 generic validator의 반복 구현 대신 실제 frozen source의 C² gas chart와 X×Theta 전체의 Gc/A/mixed 포함값을 산출하는 쪽이 타당하다.

`phys04_reduced_residual`과 `phys04_prepare_family`는 endpoint/BE point/root/private permit을 호출하지 않는 public source arithmetic 진입점이다. 그 호출 수와 source proof 범위를 새 계약에서 명시할 수 있다. `Phys04ExactPermit`의 private issuer, 실제 endpoint/conservative/root producer와 authorization0 경계는 보존해야 한다.

온도는 stored density ratio fhat를 쓰며 coupled HH gate는 35000–60000 K다. paired temperature guard는 fHe에 ±8 EPSILON 폭을 준 별도 interval을 쓴다. 고정 geometry의 remap/threshold branch를 λ,b에 따른 C² 위반과 혼동하지 않는다. λ,b=0,1과 N=0은 수식의 열린 algebraic extension과 실제 code admissibility를 구분해 다룬다. 상세 source 위치·조건·계산 경계는 `SOURCE_BOUNDARY_AND_CHART_KO.md`에 정리했다.

이 문서는 source 조사·후보 설계 역할의 산출물이다. PHYS07의 독립 최종 판정이 아니며 actual root/physical 값을 새로 채우지 않는다. 이번 intake의 scientific/native execution과 remote mutation은 모두 0이다.
