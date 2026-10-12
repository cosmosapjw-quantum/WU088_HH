# PHYS14 인계: 실제 두 번째 half 전달 이후

## 먼저 재사용할 결과

`results/advance01/ADVANCE_RESULTS.json`은 같은 COMMON에서 출발한 h=6.25e8 s 두 half의 실제 source-aligned endpoint 계열이다. 과거 HH ON과 원 compensation을 유지하고 미래 λ,b 각각 [0,1]를 두 단계 모두에 공통 적용했다. `review/DECISION.json`의 조건부 scope와 함께 읽는다. 계산 코드는 `src/phys14_advance.py`, 새 실행 기록은 `evidence/advance01/`다.

- 등방 geometry의 정확한 common rho와 normalized weights를 원 ray enclosure 안에 결박했다. 원 독립 coefficient box 전체와 이 geometric subfamily를 구별한다.
- gas4 + photon group33 + 총 guard2의 정확한 39-state closure. 값/U/V/W 156개 slots를 다음 동일 구조 stage에 전달할 수 있다.
- 원 X strict self-map, κ<0.0005392100481791. 새 근 domain, Neumann tail, source-centre/whole-X Taylor 포함과 signed carry를 보존했다.
- 두-half 유한 HH ΔT∈[-1.893684639279e-5,-9.751531029264e-6] K, Δe∈[1.343169300092e-10,2.595287368628e-10] electrons/H.
- 유한 birth ΔT∈[-2.278717930823e-4,-1.931735858256e-4] K, Δw>0 및 Δe>0.
- 유한 mixed temperature interaction∈[1.966322264584e-12,3.448057221983e-12] K; mixed electron response<0.
- 전달 photon-memory의 온도 첫 미분∈[-1.649099651540e-12,-4.924434099674e-13] K. 같은 implicit inverse 아래 gas/direct-HH/memory 분해다.
- 원 격자의 transport-only R(rho)^2−R(rho²) 정리와 실제 COMMON 가중 결과를 확보했다. 광자수·에너지 moment는 정확히0이고 HI-active photon number 차이는 약−8.6806e-9 photons/H다.

## 다음 한 루프의 우선 질문

**같은 COMMON와 geometric coefficients를 공유하는 기존 Full과 실제 two-half의 T/e/w endpoint 결함을 상관관계를 보존하여 포함한다.**

1. PHYS11 Full carry와 PHYS14 두-half carry의 같은 coefficient/geometric family를 결박한다. 원 Full endpoint와 PHYS14의 nH/nHe/atomic leaves는 같다. PHYS13의 독립 첫-half를 여러 번 더해 이력을 만들지 않는다.
2. 같은 입력을 유지한 defect residual, root difference equation 또는 Taylor-difference를 구성한다. 두 넓은 root intervals의 독립 차이만으로 결함을 판정하지 않는다. 이전 단계의 gas/photon correlation이 필요한 항목을 명시한다.
3. remap splitting, 중간 absorption, endpoint source timing과 birth chronology의 기여를 같은 관측량에 전달한다. 기존 closed-form spectral stencil은 그대로 재사용한다.
4. 필요한 경우 현재 source-centre/whole-X inclusion과 새 작은 root box의 부족한 부분만 추가한다. 새 source evaluation이 필요하다는 실제 domain/evidence가 생기기 전에는 기존 atomic kernel을 반복하지 않는다.
5. 새 결함의 부호/크기/불확실성을 같은 계열에서 판정한다. 시간분할 두 점의 비교와 전역 수렴 차수, source model adequacy, 소비자 EoR materiality를 각각 귀속한다.

이번 PHYS14는 위 다음 결함 비교를 실행하지 않았다. `NEXT_DAG.json`에는 해당 유도 작업을 구체적 후속 node로 두었다. 외부 REI DAG와 기존 아홉 HH nodes를 그대로 보존했다. HH_SINGLET와 HH_STRICT_NATIVE는 각 원자료·권한 요구를 유지하는 독립 경로다.

## 실행·복구·출처

전체 백업 snapshot은 원 입력45개를 모두 포함한다. Git snapshot은 기존31개 blob과 새 작은9개를 포함하고, 큰5개는 `INPUT_RESTORE.json`의 pinned NCP07 ZIP에서 복구한다. ZIP archive size/SHA256와 exact member를 모두 검사하는 복구 명령은 다음과 같다.

```bash
python3 src/restore_large_inputs.py --archive /absolute/path/WU088_HH_PHYS07_NCP_LOCAL_20261011_v1.zip
```

과학 계산은 이미 통과했다. 재현이 구체적으로 필요할 때만 새 attempt 이름으로 실행한다.

```bash
python3 src/run_bounded.py --attempt requested_reproduction01
```

이 명령은 기존 성공 결과를 덮어쓰지 않고, 실행 전 code/contract/input-manifest identity와 실행 후 CPU/RSS/exit를 기록한다. 원 atomic source/native root callback과 NCP job은 이번에 0이었다. 추가 복구 검증과 analytic oracle는 과학 history case 수에 더하지 않는다.

보고서는 `report/WU088_HH_PHYS14_20261012.tex`와 PDF, 상세 유도는 `theory/THEORY_CANDIDATE_KO.md`, 원 조건은 `SCIENTIFIC_CONTRACT.md`다. 결과 상태 원본의 `CANDIDATE_COMPUTED`는 계산 당시 상태로 남기고 최종 채택은 별도 `review/DECISION.json`에 결박한다.
