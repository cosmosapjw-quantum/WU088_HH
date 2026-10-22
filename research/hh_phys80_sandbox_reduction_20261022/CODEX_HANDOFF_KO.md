# Codex handoff — PHYS80 sandbox reduction

## 현재 완료 범위와 identity

Repository: https://github.com/cosmosapjw-quantum/WU088_HH

Branch: research/hh-phys80-sandbox-reduction-20261022

실제 부모 PR134 HEAD: 3304d16db1dc9bf868c185a8eeb6cc9dbc270e50.
부모 과학 commit: 338fb7728e8b41f49551200b1f1ba73c047fb90c.
이 PHYS80 snapshot의 실제 science commit과 최종 HEAD, Draft PR 및 backup
identity는 delivery/POST_PUBLICATION_RECEIPT.json과 최종 PR 본문,
외부 PHYS80_FINAL_DELIVERY_20261022.json으로 확인한다.
아직 없는 최종 hash를 이 파일의 내용에서 추정하지 않는다.

먼저 FINAL_REPORT_KO.md, CONTRACT.json, DAG_OVERLAY.json,
EXECUTION_LEDGER.json, RESEARCH_LOOP_AND_CODE_MAP_KO.md,
verification/independent/ 및 delivery/를 읽는다.

PHYS79의 고정 밀도 neutral CI + D/H DB CX control에 한정한 exact reduction:
22→4(C01),22→1(C02). 원소별 isotope rate 공유, 고정 inventory,
T/neutron 및 higher charge0을 유지한다. QSS나 species-off 실험이 아니다.
He/Li는 초기 중성 isotope 비를 보존하는 affine lift이고, actual potential로
u=u0−b·Δq와 T=u/[(3/2)kB N]를 복원한다.

새 Radau identity:

| 작업 | science identity | nfev | 부모 대비 max scaled error |
| --- | --- | ---: | ---: |
| C01_REDUCED_BASE | 98f621e3a855548a7c8e379c38093815313d8fdb703bfd25fa7eaddaa1f05bdc | 463 | 3.5858783426e-9 |
| C02_REDUCED_BASE | 8647a92cba02fcc2fbcce7a121361c150f4cce36e096412f28476d6bd6126ef3 | 933 | 8.8829681149e-10 |
| C01_REDUCED_REFINED | 639fcf6f214f864b7a23a947d9c7127c0c1195e79333fbeaf903318482926a51 | 1422 | 4.0196554386e-11 |

새 ODE3=성공3/실패0. 재개 시3verified skips/추가ODE0.
부모 PHYS79 ODE3 및 PHYS78 ODE34, HH1231/REI729/HH74control63을 재실행하지 않았다.
독립 review16논리군, 첫15PASS+1fixture실패와 마지막3점 보완을 보존했다.
Maxwellian kernel unittest6개는 별도 집계다.

## 실행 및 재현

핵심 runner는 unit 상대 경로로 읽는다:

    python source/run_reduced.py
    python source/run_reduced.py --execute

두 번째 명령도 완료된 동일 identity에서는 bytes를 확인한 뒤 건너뛴다.
완료된 identity를 새 output 디렉터리로 우회 재실행하지 않는다.
변경된 과학/구현 의무가 있으면 새 plan·source·numerical identity를 먼저 만든다.
실패/partial/orphan identity는 보존하고 자동 replay하지 않는다.
모든 actual ODE는 /tmp/rei-bianchi-cooperative-leases의 자기 lease를 필요로 한다.
worker/thread각1, 다른 process 종료0, NCP0, benchmark0.

Python3.12.14/NumPy2.3.5/SciPy1.17.0. Matplotlib3.10.8.
당시 cgroup quota8CPU/memory8GiB; 실제 실행 때 남은 slot은2/2/3이었다.
오래된 resource 관측을 새로운 lease로 대신하지 않는다.
old nfev와 new nfev는 작업량 비교이며 paired wall-time benchmark가 아니다.

## 다음 physics→coding

선택 DAG: LOW_T_CI_SOURCE_COVERAGE.

1. source/maxwellian/의 출처 판단과 Bell H Table5 B1 전사 충돌을 읽는다.
   원문 PDF bytes 또는 실제 읽을 수 있는 table image로 닫을 의무가 남아 있다.
2. 255–11605K의 threshold 법칙·단면적 오차·isotope threshold와
   chemical ionic potential의 일관성을 유도한다.
3. 현재 generic Bell kernel은 계수를 명시적으로 받아 log-rate와
   incoming-energy moment를 계산한다. 기본 H/He/Li 계수나 물리 admission은 없다.
   순 열손실을 incoming electron energy로 동일시하지 않는다.
4. source/domain/에너지 계약을 닫은 후 새 원자 연산자/consumer adapter를 구현한다.
   새 injection/PI/RR/expansion에는 현재4/1차원 invariant를 자동 확장하지 않는다.

RECOMBINATION_TO_Z20_INITIAL_CHARGE_CONTRACT, He/Li CX state/photon energy,
D PI/RR potential adapter, Li hard-UV inner-shell/branching/spectral contract,
전체 핵반응·분자·Compton·spectral transport는 OPEN이다.
접근 불가 비공개 대화를 전수 조회했다는 주장도 하지 않는다.

같은 normal orthonormal frame에서 signed tensors를 합한 뒤 norm.
Frobenius=sqrt(2)*half-contraction. reacting gas pi=0; pi_m은 collisionless DM.
HH_R10=OFF. Production admission NOT_ISSUED. Draft 유지; main merge 없음.
