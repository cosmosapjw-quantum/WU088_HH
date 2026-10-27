# R4 R1/C1 독립 계약 검토

**판정: `PASS_SCOPED_CONTRACT_CHECKPOINT`. R1/C1 checkpoint 게시를 막는 결함은 발견하지 않았다.** 검토 대상은 새 분자 공급자 연구의 범위·baseline·예산·승인 상한이다. 아직 생성되지 않은 원자료 추출, 정리 증명, evaluator의 정확성 또는 R6/C9 완료를 승인하는 판정은 아니다.

검토자 `/root/molecule_sources`는 이번 molecular 원자료 packet·계약·이론·evaluator의 작성자가 아니다. 실제 계약과 관련 파일을 읽고 기존 재사용 파일의 SHA-256 일치를 확인했다. 과학 계산, compiler 호출, source parser 실행, 기존 검증 재실행 및 Wolfram 호출은 모두 없었다.

## 검토한 입력

| 입력 | SHA-256 |
|---|---|
| `CONTRACT.json` | `6a40c43c04aa4506281f2021a6879e76e94d560ea3cc8af3c7cdfeffb15eb8bc` |
| `POLICY_OVERRIDE.json` | `4b1e3be4444a078d588f16cdf4b624683ae0f50c54efca86b4dd0ad15182eb6e` |
| `REUSED_CALCULATIONS.json` | `92abcec183e7a3da21a4a1cd59d25b421129cccde164ca53cfe7fe8782dba051` |
| `authority/AGENTS_PARENT.md` | `a65f18d2bc33fab94796374b9852ccad1543e02d25c65b6d36ed3269041c8c33` |

최신 로컬 HEAD는 `bfdeed676617c8b75ed81ac5e79e800fa69f83db`이고, 독립 authority 조사자의 2026-10-27 03:37:53 UTC remote 관찰도 같은 HEAD였다. 현재 네 병렬 agent 역할, R3 실제 Dropbox/Drive byte readback, R4의 최신 cloud metadata를 확인했다. 재사용 명세의 compiler·adapter·R1/R2/R3 admission·R3 DAG·백업 receipt 일곱 파일 해시가 모두 실제 파일과 일치한다. 이는 식별자 검토이며 기존 과학 검증을 다시 실행한 결과가 아니다.

## 판정 근거

### 1. 이전 예산과 새 연구 단위가 분리되어 있다

PHYS91의 primary/reference/Wolfram 잔여량은 모두 0으로 보존되고, 역사적 global CPU·금전·remaining은 null이다. 새 계약은 최대 여섯 새 column, source-fit 평가 표본 29개, 한 번의 symbolic request와 경량 child 상한을 별도로 둔다. 이를 PHYS91 잔여량 회복이나 global budget reset으로 해석하지 않는다. 새 적분·physical Q 예산은 0이며, 비용 미측정 항목을 0으로 쓰지 않고 최초 실패를 보존한다. 이 명세는 현재 요청에 따른 새 단위의 범위로 타당하다. 실제 limiter와 실행 receipt는 후속 구현 단계에서 확인한다.

### 2. 여섯 공급자와 77개 값은 아직 계획 수다

계약의 `anticipated_provider_variants=6`, `anticipated_native_rate_cells=77`은 예상 수로 명시되어 있다. 이번 검토는 이를 원자료에서 독립 확인한 수로 승격하지 않는다. 여섯 variants는 여섯 독립 실험이나 여섯 개의 source-quorum 투표를 뜻하지 않는다. TIQM/SQM은 동일 반응의 계산 방법 대안이고, Bovino의 ortho/para 항목은 원 논문의 channel·spin 의미를 확인해야 한다. 이 구분을 실제 manifest에서 고정하는 것은 R2/C2의 입수 의무다.

### 3. 원 식의 구현 승인과 실제 rate 사용 승인이 구분된다

계약은 source-convention fit 평가를 허용 가능한 구현 성과로 두면서 물리 rate·Q·energy partition·state-lift consumer·activation을 승인하지 않는다. 이 상한은 실험값뿐 아니라 아직 consumer에 결속되지 않은 이론 계수에도 적용한다. 논문의 fit residual, printed rounding, 이론 모델 오차, 관측 오차 및 covariance는 다른 양이다. 이들 사이에 임의 변환을 하거나 residual을 새 physical uncertainty로 삼을 근거는 계약에 없다.

### 4. 동위원소·상태·spin의 미해결 부분을 다룰 수 있는 계약이다

positive state lift, 명시된 population 아래의 defect bound, unknown-state binding 거부가 deliverable로 잡혀 있다. 이 방향은 적절하다. 다만 실제 source의 isotope resolution과 registry가 선언하는 동위원소는 별도 필드여야 한다. LiH 또는 HD라는 aggregate 이름으로 원자의 electronic state, 분자의 rovibrational population, product-state sum, ortho/para 비율을 정할 수 없다. LTE·statistical spin weights·detailed balance·Q를 기본값으로 추가하지 않는다. 이러한 source-to-model 연결은 실제 식과 원문을 대상으로 후속 검토한다.

### 5. Source quorum과 불일치는 후속 입수 단계에 남아 있다

계약은 Bennett2003, Bovino2009, Honvault2013 correction, Gonzalez-Lezana2022를 지정하며 independent review를 요구한다. R1/C1 계획으로는 충분히 구체적이다. 실제 source quorum의 성립은 각 원문의 byte identity, 표·식 locator, native domain/units, correction의 선후관계와 별도 검토자가 확인한 원 행을 요구한다. 이번 계약 검토가 그 입수·검증을 대신하지 않는다.

Bovino Table 3 partial 값과 Table 1 total의 차이는 principal 값과 분리해 보존한다는 계약이 적절하다. 이 차이를 조용히 수정하거나 principal total을 대체하거나 새 물리 uncertainty band로 해석하면 안 된다. 공개 packet에는 원문 접근 권리와 전체 PDF 재배포 권리를 구분해야 한다.

### 6. 게시와 연구 완료의 뜻이 보존된다

사용자가 지정한 physmath 1.0.0 전체 R/C 루프가 우선하며 `POLICY_OVERRIDE.json`은 scheduling만 바꾼다. 자동 additive 게시와 Dropbox/Drive 백업은 이미 명시적으로 승인되어 있으므로 이 검토 때문에 다시 확인을 받을 필요가 없다. PR150에 expected-SHA non-force checkpoint를 기록하고 실제 성공 receipt를 남기는 계약은 타당하다. main merge는 포함되지 않는다.

R4의 20개 workflow stage 진행률은 이전 WU DAG 20개 노드의 완료 수와 다른 축이다. 독립 authority가 고정한 기존 분류는 **strict scoped COMPLETE 5/20, implementation-only PASS 2/20 별도**다. 5개 안에도 source recovery와 declared integer 결과가 포함되므로 이를 5개의 physical consumer 완료로 말할 수 없다. source·science·delivery·중앙 DAG 상태를 각각 유지한다.

## 다음 검토에 전달할 의무

- R2/C2: 실제 source packet을 freeze하고 각 원문·correction·표의 해시/locator 및 실제 행 수를 고정한다.
- R3/C2: source isotope/state 사실과 registry 선언을 분리하며 spin/method 선택 및 product-state 합의 의미를 적는다.
- R3/C3: TIQM/SQM 대안의 중복 소유를 막고, ortho/para의 channel 의미가 확인되기 전 임의 합산·가중을 하지 않는다.
- R5/C5: 원 fit의 계수·식·native T support·단위를 정확히 구현하고 physical binding 거부와 source-only 평가를 구분한다.
- R6/C9: 실제 동결된 정리와 코드를 대상으로 새로운 독립 검토를 수행한다. 이 문서는 그 판정을 미리 제공하지 않는다.

검토 결과와 추적 의무의 기계 판독본은 같은 디렉터리의 `CONTRACT_REVIEW.json`에 있다. 원 계약 파일은 수정하지 않았다.
