# PHYS80 증분 intake — PHYS79 최종 전달 이후

## 결론과 관측 범위

이 intake는 **읽기 전용 provenance 조사**다. PHYS79 최종 HEAD `3304d16db1dc9bf868c185a8eeb6cc9dbc270e50`과 로컬 최종 ZIP/외부 JSON의 전체-byte SHA256이 일치했다. 기존 두 provider 전체복원 증거를 그대로 재사용했으며 원격 ZIP/JSON을 다시 받지 않았다. 기존 과학 실행·테스트·ODE·NCP·benchmark 재실행은 모두 0이다.

시간 기준은 2026-10-22 03:25:00 UTC, 현재 관측은 06:34–06:41 UTC이다. PHYS79 PR134의 최종 본문 갱신은 03:25:37 UTC로 기준분과 겹치지만 내용과 HEAD가 이미 알려진 최종 전달이다. “이번에 새로 읽은 결과”, “이전 intake에서 바뀐 ref”, “기준시각 뒤 게시된 결과”를 구별한다. PR 갱신시각을 과학 실행시각으로 간주하지 않는다.

조사는 WU 최신 12 PR, 지정 sibling 5개 repo의 최신 5 PR씩, 기존 6개 sibling PR, 관련 9개 exact branch ref, WU `research/hh-phys8*` ref prefix, 새로 발견한 관련 handoff에 한정했다. 이전 51개 repo/142개 branch catalog를 재조사하지 않았다. 접근할 수 없는 비공개 대화는 **UNAVAILABLE**이며 전수 확인하지 않았다. 전체 branch에 중복 작업이 없다는 주장도 하지 않는다. 실제 API URL·관측시각·응답 범위는 [REMOTE_OBSERVATIONS.json](REMOTE_OBSERVATIONS.json), 고정 handoff 텍스트와 SHA256은 [PINNED_HANDOFF_MANIFEST.json](PINNED_HANDOFF_MANIFEST.json)에 있다.

## Actual refs

| 단위 | 현재 exact head | 기존 intake와 관계 |
|---|---|---|
| WU PR134 | `3304d16db1dc9bf868c185a8eeb6cc9dbc270e50` | 동일한 PHYS79 최종 전달 |
| REI PR220 | `8be7533cc97b3302bf42608699d6e8313ed6af8a` | 동일 |
| REI PR219 | `6a12f3865d9ea427c1391c41caed8bb7cb7ec00d` | 이전 `2c6aa0a14102cbe296a596b759f159a9f3d96b99`에서 진행. 현재 commit 03:23:54 UTC로 cutoff 이전 |
| REC PR119 | `ad93fa1c71f8a2b2a0b19836be3c7b739b11b0c7` | 동일 |
| CR PR96 | `a5e12c5f3e6d323e211d65fefad34060ec07eff0` | 동일 |
| HE PR85 | `16a424b7290f484c57e97c8ed74f81e6d2043782` | 이전 `88f9957d219f71b458b3bcaf41ccdde60538379f`에서 복원 metadata 추가. 02:32:29 UTC로 cutoff 이전 |
| bass PR180 | `574c3af93810122af0a7977e00e34195e5251a09` | 동일 |
| REI PR221 | `c1714f82ea7de15fee230a1a995365970ee6dc02` | 새로 관측한 C2 mapping 결과, 06:33:10 UTC 게시 |
| REC PR120 | `d562d03415e37488cd4b5444488c77555260e0fb` | 새로 관측한 THERM01 실행 handoff, PR 갱신 06:33:56 UTC |
| HE PR86 | `bb1259b21c7b83b0376a5f7fcbb0c6321918ec90` | 새로 관측한 HE33 moment foundation. PR 갱신 03:17:14 UTC로 cutoff 이전 |

WU 최신 목록에는 새 PHYS80 PR이 없었으며 `research/hh-phys8*` matching-ref 결과도 비어 있었다. 이는 지정 prefix/목록에 대한 06:35 UTC 관측이다.

## 관련 새 결과와 재사용 경계

### REI221: C1 본문보다 actual C2 handoff가 앞서 있다

[고정 C2 RESUME](https://github.com/cosmosapjw-quantum/rei_bianchi/blob/c1714f82ea7de15fee230a1a995365970ee6dc02/research/rei_coupled_isotope_mapping_20261022/RESUME.md)는 C2 formula/data/code mapping의 **214 finite checks PASS, 1 diagnostic, cosmological IVP 0**를 기록한다. 실제 진단시각은 `evidence/EXECUTION.json`의 **03:22:50 UTC**로 cutoff 이전이고, 결과를 보존한 head commit은 이후인 06:33:10 UTC다. 현재 PR 본문과 기존 C1 경로 RESUME의 “C2 READY,191 checks”는 이전 lane snapshot이므로 최신 상태로 사용하지 않는다.

다음 C3의 의무는 charge-resolved event/energy interface, 정확한 zero/tiny stock 처리, off-grid rates, beta 한 owner, RR alpha/derivative/energy moment 일치, 전자와 핵의 입자수 변화에 따른 heat capacity이다. **고정 compact33 isotope lift는 positive n/T injection을 담을 수 없고 geometry reduction과 별개**다. PHYS80의 고정 inventory·제한 reaction set에서 22→4를 유도하는 것은 별도 조건부 작업으로 가능하나, nuclear injection이나 source-dependent isotope 비동일성을 추가할 때 그 quotient를 자동 재사용해서는 안 된다. 이번 intake는 그 exactness를 증명하거나 실행하지 않았다.

### PR219 provider lane: 복구 실패는 역사 기록이며 현재 scalar 범위는 완료

같은 REI221 head에 보존된 [bootstrap handoff](https://github.com/cosmosapjw-quantum/rei_bianchi/blob/c1714f82ea7de15fee230a1a995365970ee6dc02/research/rei_bootstrap_energy_providers_20261022/CODEX_HANDOFF_PROMPT.md)는 payload `61e08967832363b611a8e5ba4167ba7b06c06b6b`와 metadata `6a12f386...`의 scoped delivery 완료를 기록한다. 기존 오류와 수정 전 테스트는 이전 identity에 남고, 수정된 bootstrap 5 affected tests가 따로 기록된다. full fresh83와 프로젝트 Rust build는 NOT_RUN이다.

공개 scalar provider 범위는 **100–10000 K**다. 6채널 RR의 derivative-of-fit moment와 3개 ground-target DR fit의 수치 검증은 후보 재사용 근거다. RR derivative의 경험적 오차, DR thermal moment/cascade/energy closure, validated CI/CX, isotope spectroscopy 또는 coupled production 완료를 의미하지 않는다. Badnell donor Li RR와 VF scalar adapter는 서로 다른 모델이며, Badnell의 온도의존 b(T) 미분에는 b-dot이 필요하다. registry에도 LOW_T CI는 missing, Voronov Tmin은 1/1/3/1/4/5 eV다.

### REC120: PR 본문의 Stage A 문구보다 actual handoff가 앞서 있다

[고정 CODEX_HANDOFF](https://github.com/cosmosapjw-quantum/rec_bianchi/blob/d562d03415e37488cd4b5444488c77555260e0fb/research/rec_rei_thermal_yield_20261022/CODEX_HANDOFF.md)는 **THERM01 8 완료 이력 = 6 nominal + 1 tight34 + 1 full63**, 각 193 저장 epoch, z20→2를 기록한다. 과학 checkpoint는 `f68f6e8391f115f36da2766bc8eb20724d1c673f`다. 최대 정규화 energy residual은 **2.935629461677083e-6**, gate 3e-6에 대한 여유는 약 **2.1457%**다. 이 값들은 해당 unit의 기록을 읽은 결과이며 이번 intake가 재계산한 검증값이 아니다. PR 갱신 뒤 새로 관측했으나 실행 자체가 cutoff 뒤였다고 단정하지 않는다.

source-scope clarification은 5–60 eV에서 Li I direct 1s photoionization 가지가 threshold 아래라는 말과, **50–60 eV core excitation/autoionizing resonance 생략**을 구별한다. 후자의 누락량을 0으로 증명하지 않았다. RR fit derivative cooling의 경험적 정확도, UV 자체진화, 전체 열/핵반응 범위는 열려 있다. THERM01을 PHYS80의 CI/CX 원자료나 새로운 source closure로 간주하지 않는다.

### HE32/HE33: 상태수 축소와 물리 closure를 구별한다

HE85 head의 추가는 이전 artifact 복원·saved render reuse 기록이며 신규 IVP가 아니다. HE33 [NEXT_THREAD_HANDOFF](https://github.com/cosmosapjw-quantum/BASS_HE/blob/bb1259b21c7b83b0376a5f7fcbb0c6321918ec90/research/he33_baryon_moment_foundation_20261022/NEXT_THREAD_HANDOFF.md)는 prescribed nu_pi를 쓰는 균질 비상대론적 LRS baryon moment foundation, V8/Wolfram **17 groups PASS, cosmological IVP 0**를 기록한다. science pin은 `1d7dab57becc5829f0282b88a7516360ccad718a`다. 그 세션의 Node CLI NOT_RUN은 이 세션 runtime 부재를 뜻하지 않는다. 반응 가스와 collisionless DM의 stress는 분리해야 한다. PHYS79의 reacting gas pi=0 범위에 HE33 moment closure를 자동 도입하지 않는다.

## 로컬 부모 identity와 가용 자원

| 대상 | 전체 bytes | SHA256 |
|---|---:|---|
| PHYS79 최종 ZIP | 2,557,522 | `513a7d37478b5b055b7b2cd97f752b6d992522d0fc3f45135ffbae831cb183e6` |
| PHYS79 외부 final-delivery JSON | 10,549 | `7fae6fa4b5ee871fd7e6f2968b163b48a5d22398599cbbf93b436b95fc9ad9c0` |

현재 로컬 전체-file hash 일치와 과거 양쪽 provider full-byte/CRC/166-payload 검증은 서로 다른 증거다. 이전 원격 복원 원문 receipt는 [PARENT_RESTORE_EVIDENCE_REUSE.json](PARENT_RESTORE_EVIDENCE_REUSE.json)에 출처/hash와 함께 보존했다. 이번에는 원격 provider metadata나 원격 파일 bytes를 재확인했다고 주장하지 않는다.

06:34:41 UTC 관측에서 Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, Matplotlib 3.10.8이다. 표시 CPU/affinity는 9이나 cgroup quota `800000/100000`로 **8 CPU**, memory.max는 **8 GiB**다. 당시 memory.current는 799,444,992 bytes였다. shared lease directory에는 0-byte `leases.lock`만 보였고 active lease 기록은 없었다. 이 시점 관측은 이후 실행 lease를 대신하지 않는다. 다른 process 종료나 자원 재설정은 하지 않았다.

## 첨부 프로토콜의 적용 범위

04/05/07/08 전문을 읽고 각각 size·line count·SHA256 및 적용/비적용 항목을 [ATTACHMENT_RELEVANCE.json](ATTACHMENT_RELEVANCE.json)에 기록했다. 04/05의 contract→유도→구현→독립 audit 순서, 08의 units/normalization/과학 주장 점검 뒤 07의 clipping/legibility 보정은 PHYS80에 유용하다. CMB gauge/LoS/C_l/CAMB/CLASS 고유 작업은 이 고립 화학 reduction에 적용하지 않는다. Rust archive를 추출하거나 build하지 않았다.

새 numerical comparison이 허용될 경우 source-domain과 고정 isotope inventory 조건을 먼저 고정하고, proper-time 단위와 22→4 상태수 감소를 명시해야 한다. 상태수 감소는 측정 speedup이 아니며, sampled residual과 refinement는 continuum certificate가 아니다. 이번 조사 자체는 PHYS80 유도·코드·검증·과학 실행·게시·backup 완료 상태를 부여하지 않는다.
