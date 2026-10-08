# C0 응용 계약과 HH channel crosswalk

상태: `C0_CROSSWALK_IMPLEMENTATION_VERIFIED__APPLICATION_AUTHORITY_BLOCKED`.

## 실제 산출물

DAG C0의 APPLICATION_CONTRACT.json, HH_CHANNEL_CROSSWALK.json, RELEVANCE_OBLIGATIONS.json과 read-only 검사기를 만들었다. 실제 source file 10개의 bytes/SHA를 고정했고 49-row 순서와 Q49→25의 저장된 binary64 계수를 보존했다. 새 HH 적분·전파·rate 평가는 0이다.

고정 FROZEN_INPUTS.npz의 SHA256은 `8482d2854ab620c58bb1d7a7a45cf88eb71fd75081242263a9ef48927f0a282c`이다. active 단전자 Ritz energy를 기준으로 negative 25, positive-energy L2 pseudostate 22이며 별도 ionic variational trial 2개다. Negative 값은 정확한 hydrogen state를 보증하지 않고 positive population은 flux-normalized ionization rate가 아니다. phase_E를 물리 reaction threshold로 사용하지 않았다. Spin-singlet/고정 평면 block을 unpolarized cross section으로 자동 승격하지 않는다.

종 순서 (HI,HII,Hminus,e_free)의 ion-pair event는 nu=(-2,1,1,0)이다. 핵수와 전하는 보존되고 자유전자 변화는 0이다. Hminus를 버리면 투영된 HI+HII 핵수 변화는 -1, 기존 H/He 전자수 식을 강제하면 전자 +1을 잘못 센다. 따라서 Hminus 상태 또는 보존적인 제거 근사 없이는 이 경로를 receiver에 주입하지 않는다. 이는 negligibility 증명이 아니다.

R1 MICRO-0 및 geometry에 14개 process/family contract owner를 고유하게 부여했다. 실제 rate routine의 exact implementation pin은 회수되지 않았으므로 provider_admitted=false다. HH baseline replacement는 0개다.

R2-T/R3/R4의 실제 후속 결과 문서를 회수했다. 과거 'R2-N 완료 자료 미발견'을 후속 결과 부재로 계승하지 않는다. 다만 corrected G7 원 식과 exact receiver implementation receipt는 여전히 회수되지 않았다. 이들은 reference/auditor 문서이며 global production 상태를 인증하지 않는다. R4의 radiation-chemistry-opacity feedback 및 production replacement는 OPEN이다.

R3/R4의 photon 10–100eV, E^-1.5 SED 및 고정 absorber는 audit fixture이다. 물리 T, 충돌 에너지, 우주론적 redshift, 밀도, 속도분포, SED, tilt, observable 오차 예산은 DOMAIN_CONTRACT_REQUIRED로 남겼다. Fixture 출력 온도를 유효 domain 경계로 쓰지 않는다.

## 검증과 전달

최종 22 tests PASS, skip 0. Channel red→green 8개, 거절 조건 red→green 13개, 유효한 미해결 계약 positive test 1개다. Metadata CLI exit0, physical application 요구 CLI exit3. DB는 기존 31 table/schema/rows를 보존하고 c0_ 6개 table을 더해 37개다. Integrity ok, FK 위반0, 실제 로컬 SQL 복원 논리 해시 일치. 독립 과학 검토·HH 수치 인증·NCP 성능 검증은 아니다.

이 Git 디렉터리는 결과 요약, 검사기와 테스트 소스를 직접 게시한다. 전체 계약 JSON 3개, SOURCE_LOCK.json, frozen input/receiver 문서, 상세 보고서, red/green logs, DB와 SQL dump는 C0_RESULT.json이 해시로 고정한 38-payload ZIP에 있다. 전체 자료를 Git에 풀어서 게시한 것은 아니다. 실행 시 ZIP을 새 빈 디렉터리에 복원한 뒤 그 안의 c0_application_contract_20261002_v1에서 아래 명령을 쓴다. JSON/source 파일이 없는 이 Git 디렉터리만으로 성공했다고 하지 않는다.

```sh
python3 -B -m unittest discover -s tests -v
python3 -B c0_contract.py --validate
python3 -B c0_contract.py --require-application
```
마지막 명령의 기대값은 exit3이다. 잘못된 값을 0으로 대체하거나 application gate를 true로 고쳐 실행하지 않는다.

기존 coverage20/289, missing269 미상계, B22 OPEN, full D/epsilon/production 미완료를 보존한다. C0 bounded metadata deliverables는 완료지만 application acceptance 전체는 미완료다. 다음 독립 노드는 C1_ACTUAL_REPRESENTED_GAPS_AND_MACHINE_PREDICATE_BRIDGE이다. C3 물리율 주입/C5 최종 동결 전에는 남은 C0 전제를 닫아야 한다.
