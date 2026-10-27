# R4 R2/C2 원자료 독립 검토 — 유실 후 복원 기록

## 이 파일의 성격

이 문서는 **이미 완료해 보고한 검토의 기록을 대화에서 복원한 receipt**다. 유실된 `SOURCE_REVIEW.json`이나 `SOURCE_REVIEW.md`의 정확한 원래 바이트가 아니다. 77개 셀의 재검토 또는 새 과학 판정을 수행하지 않았다.

부모 에이전트가 알린 보존 checkpoint는 S01 commit `94ba73928d2e2055cf07ad8801f7e83ccb827818`이다. 현존하는 `next_loop_20261027/S01_PUBLICATION.json`은 이 commit과 contract review의 게시를 기록하지만, 그 뒤 작성된 source review 두 파일은 포함하지 않는다. 이 복원에서는 원격 HEAD를 별도로 갱신하지 않았다.

원래 검토 파일의 기대 SHA256은 다음과 같다. **이 값들을 현재 복원 파일의 SHA로 사용하면 안 된다.**

| 유실 파일 | 완료 당시 보고한 SHA256 |
|---|---|
| `SOURCE_REVIEW.json` | `9bb3405fd8b859d3155afe56d50387c22bce32d0d5a4ab0422ba14692944471d` |
| `SOURCE_REVIEW.md` | `a7e540cb2c26ea9dbdb9c38ead954e11c80c13624b44e714b466d0631eadc4e8` |

복원 시각은 `2026-10-27T05:55:44Z`이다. 원래 검토 파일 작성 시각의 정확한 값은 현재 기록에 없어 `null`로 둔다.

## 원래 완료 보고의 범위

원래 검토 대상 packet은 `MOLECULAR_SOURCE_PACKET.json`, SHA256 `40e2fbd73d451c0c8116b4ca9bd4db4d2e43e4cdf8967988a2fea551f99ce35e`였다. 당시 보고한 판정은 **`ACCEPT_SCOPED_NATIVE_SOURCE_ROWS_AND_SEMANTICS`**이고, 숫자·열·scale·unit 불일치는 0이었다. 아래 수는 그 완료 보고를 재기록한 것이며 이번 복원의 새 검토 수가 아니다.

| 원자료 | Provider variants | 당시 직접 대조한 rate cells |
|---|---:|---:|
| Bennett 2003 Table 3 | 1 | 27 |
| Bovino 2009 Table 1, ortho/para | 2 | 28 |
| Honvault 2013 correction Table 1, TIQM/SQM | 2 | 20 |
| Gonzalez-Lezana 2022 두 SQM 수치 | 1 | 2 |
| 합계 | 6 | 77 |

검토자는 source packet 작성자와 구별되며, 당시에도 source 작성자 parser를 import하거나 실행하지 않았다. LiH 원 PDF 표·식의 시각 대조, correction의 회수된 primary DOI fulltext, publisher HTML의 직접 읽기를 근거로 삼았다. 원 논문의 동역학 계산 자체를 재현하거나 검증한 판정은 아니었다.

## 완료 보고에 남은 핵심 의미 경계

**Bennett 2003.** 원자료는 [출판사 원문의 ADS 보관 PDF](https://articles.adsabs.harvard.edu/pdf/2003MNRAS.341..361B), DOI `10.1046/j.1365-8711.2003.06422.x`였다. Table 3의 scale `10^-20 cm³ s^-1`와 27개 수치를 대조했다. 전자 대칭 계수 `p=1/4`는 이미 공급자 계수에 포함되어 있어 재곱셈하지 않는다. 원자료의 `7LiH` 지정과 수소 질량수의 별도 미명시를 구별했다. Bound/quasi-bound 최종 상태의 집계는 단일 `v=0,j=0` 생성물 지정이 아니며, 후속 cascade의 광자 수·에너지를 고정하지 않는다. Fit residual은 물리적 covariance 또는 일반적인 불확실성 상계가 아니다.

**Bovino 2009.** [arXiv:0911.1281v1](https://arxiv.org/abs/0911.1281v1)의 Table 1에서 14개 온도의 ortho/para 두 열, 총 28개 수치를 대조했다. Total `J=0`은 초기 분자 회전수 `j=0`과 같다고 취급하지 않았다. 초기 상태 및 집계의 핵스핀 가중치 조건은 열린 상태로 유지했다. 원문의 fit `b` 단위 문제를 자동 수정하지 않았다. 별도 Table 3의 `1.92e-09`는 시각 확인했지만 주요 77개 셀에서 격리했으며, 지수를 고치거나 branch fraction으로 해석하지 않았다. source exothermicity도 상태별 Q 또는 핵 Q로 승인하지 않았다.

**Honvault 2013 correction.** [Primary DOI `10.1021/jp4113377`](https://doi.org/10.1021/jp4113377)에서 Exa를 통해 직접 회수된 correction fulltext representation의 20개 셀을 대조했다. 원 ACS PDF는 확보되지 않았으므로 **원본 PDF SHA는 `null`**이다. 회수 representation SHA는 `08943ae9d984636a11d7a4fe65d559afba709b0578c52a814e01893705e63c7e`였다. 수정 표의 순서 `T, SQM, TIQM`, scale `10^-9 cm³ molecule^-1 s^-1`, 초기 `H2(v=0,j=0)`를 보존했다. SQM/TIQM은 대안이며 더하지 않는다. 원 PDF 바이트를 검증했다는 주장은 포함하지 않았다.

**Gonzalez-Lezana 2022.** [Publisher HTML](https://aipp.silverchair-cdn.com/article-minimal/2842276), DOI `10.1063/5.0128598`에서 205 K의 `1.21e-10`과 295 K의 `2.21e-10 cm³ s^-1`를 SQM 수치로 확인했다. 인접 EQM·실험값과 구별했고, 회전 상태 평균과 기존 `1/4`, `3/4` 가중치의 의미를 유지했다. `gamma=405 K`는 fit activation parameter이며 상태별 Q 또는 핵 Q가 아니다. 접근되지 않은 supplement를 읽었거나 추가 표를 확보했다고 하지 않았다.

원래 acceptance는 수치·단위·상태 의미의 보존에 한정된다. 새 theorem, evaluator, physical rate, Q, energy closure, consumer, 상태 population 결속, runtime activation은 승인하지 않았다. 이 receipt 역시 그 범위를 확장하지 않는다.

## 복구를 위해 실제 수행한 작업과 한계

지정 scratch 및 `/tmp`에서 정확한 review 파일명들을 검색했고, 가능한 세션 저장 키들을 조회했다. 원래 파일은 발견되지 않았고 해당 저장 키들도 값을 반환하지 않았다. `/tmp/codex-daemon-0`은 접근 거부가 있었으므로 그 내부의 존재 여부에 대해서는 주장하지 않는다. 전체 저장 키를 열거할 수 있는 API는 사용하지 않았다.

당시 시각 대조에 사용한 `r4_source_review_bennett_p2.png`, `r4_source_review_bennett_p6.png`, `r4_source_review_bovino_p14.png`, `r4_source_review_bovino_p16.png`의 경로는 `/tmp`에 남아 있었다. 이번에는 이미지를 다시 읽어 셀을 재검토하지 않았다. S01 복원 진행 중 로컬 `WU088_HH`는 git repository가 아닌 상태였고, git 변경을 시도하지 않았다.

현재 문맥에는 원래 apply-patch 본문의 정확한 직렬화가 없으므로 기대 SHA가 일치하는 원본 바이트를 재생성할 수 없다. 원래 완료 메시지, final 보고, 입력 및 출력 SHA와 의미 경계를 근거로 이 문서와 동명의 JSON receipt를 새 파일명으로 작성했다. JSON에는 보존된 source별 입력 SHA, 원래 완료 보고의 그룹별 수, 복구 검색 범위 및 한계를 구조화했다.

이번 복원의 새 native-cell 검토, fit/rate 평가, compiler 실행, 기존 science suite 재실행, Wolfram 호출, source 다운로드는 모두 0이다. 작업은 기존 기록 읽기와 복원 metadata 작성·해시에 한정된다.

## 복원 자료를 사용할 때의 조건

원래 검토 판정의 대상은 위에 명시한 packet SHA `40e2fbd7…99ce35e`다. 이번에는 복원된 source packet의 동일성을 검증하지 않았다. 다른 SHA의 packet을 이 기록만으로 자동 승인하면 안 된다. 단순히 물리 결과를 재계산할 필요는 없지만, 내용이 변경되었다면 변경된 입력에 해당하는 검토 범위를 별도로 명시해야 한다.

원래 두 review 파일이 나중에 발견되면 기대 SHA와 비교한 뒤 원본으로 보존하고, 이 복원 이력도 유지한다. 이 receipt 자체의 해시는 새로 산출하며, 원래 두 review SHA와 구별한다.
