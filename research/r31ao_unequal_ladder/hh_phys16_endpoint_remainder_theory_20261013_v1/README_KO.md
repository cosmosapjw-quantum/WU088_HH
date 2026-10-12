# WU088_HH PHYS16 — 상관 endpoint 결함과 유한 관측량

2026-10-13 KST. `physmath-research-loop` 내장 규약 1.0.0의 THEORY R1–R10을 적용했다. 원 PHYS15의 동일 COMMON 잔차를 실제 보존 source·carry 자료에 적용하고, endpoint Jacobian에서 평균 Jacobian과 공통 adjoint로 가는 2차 remainder를 유도했다.

**현재 과학 판정: `PROMOTE_SCOPED`.** 독립 심사와 root 채택을 완료했다. 동일 COMMON·고정 α·원 C² source 계열 안의 실제 Full–two-half endpoint 포함과 공통 adjoint 결과를 채택한다. R6·R8·R9를 완료로 연결했고, 19쪽 PDF와 실제 Git/Google Drive/Dropbox 저장을 확인했으며 R1–R10을 완료했다. 저장 근거는 `publication/BACKUP_ACK.json`에 있다.

## 현재 결과

기체 차이의 방향은 d=g₂−g_F, 온도는 ΔT=T₂−T_F다. 고정 admissible α마다 동일한 λ,b∈[0,1]을 두 half와 Full에 공유한다. 원 source 계열은 geometric-isotropic, 33개 photon group 및 두 guard, source-aligned C² 계열이다.

| 실제 계산 | 포함 |
|---|---|
| Δx_HII | [4.968073098724, 6.424794326491]×10⁻⁸ |
| Δe, electrons/H | [4.968232944627, 6.425017521665]×10⁻⁸ |
| Δw, eV/H | [−2.378772061685, −1.828215860677]×10⁻⁸ |
| ΔT, endpoint 보정과 교차 후 | [−0.001585967387181453, −0.001210819969055199] K |
| m=2 Neumann 예측의 S-norm 오차 | ≤7.663478331196157×10⁻¹⁶ |
| 같은 Π_F에 대한 온도 remainder | ≤1.710575696736044×10⁻¹² K |

현재 원 자료의 평균 numerator adjoint 부호까지 포함했으므로, b>0에서 birth-redshift sector는 냉각 방향이고 birth backward-Euler sector는 가열 방향이다.

\[
\Delta T_{bR}/b\in[-2.193573619033929,-2.084075101148286]\times10^{-9}\ {\rm K},
\]
\[
\Delta T_{bBE}/b\in[6.795510419222985,7.189758987952319]\times10^{-5}\ {\rm K}.
\]

b=0에서 두 sector는 정확히 0이다. 이는 같은 평균 inverse와 유한 분모를 사용한 잔차 attribution이며, 전체 매개변수 미분은 다음 연구 단위의 대상이다.

## 읽을 파일

| 목적 | 파일 |
|---|---|
| 완전한 유도·원 Hessian 대응·실제 적용 | [theory/ENDPOINT_REMAINDER_THEORY_KO.md](theory/ENDPOINT_REMAINDER_THEORY_KO.md) |
| 주장과 근거 연결 | [theory/ENDPOINT_REMAINDER_CLAIMS.json](theory/ENDPOINT_REMAINDER_CLAIMS.json) |
| 실제 residual과 첫 포함 | [checks/application/run01/results/CORRELATED_DEFECT_RESULTS.json](checks/application/run01/results/CORRELATED_DEFECT_RESULTS.json) |
| endpoint remainder·공통 adjoint·birth 부호 | [checks/endpoint/application01/ENDPOINT_REMAINDER_RESULTS.json](checks/endpoint/application01/ENDPOINT_REMAINDER_RESULTS.json) |
| source 시각 차이와 cooling cone | [evidence/intake/PHYS16_APPLICATION_DERIVATION_KO.md](evidence/intake/PHYS16_APPLICATION_DERIVATION_KO.md), [evidence/intake/SOURCE_COOLING_AUDIT_KO.md](evidence/intake/SOURCE_COOLING_AUDIT_KO.md) |
| SciSpace·Exa 원전 비교 | [literature/LITERATURE_REVIEW_KO.md](literature/LITERATURE_REVIEW_KO.md) |
| Wolfram·xAct 실제 출력 | [checks/wolfram/WOLFRAM_XACT_EXECUTION.json](checks/wolfram/WOLFRAM_XACT_EXECUTION.json) |
| 독립 심사와 최종 과학 채택 | [review/INDEPENDENT_REVIEW.json](review/INDEPENDENT_REVIEW.json), [review/DECISION.json](review/DECISION.json) |
| 현재 DAG와 인계 | [NEXT_DAG.json](NEXT_DAG.json), [HANDOFF_KO.md](HANDOFF_KO.md) |
| 다음 parameter-response 계약 | [contracts/PARAMETER_RESPONSE_CONTRACT.json](contracts/PARAMETER_RESPONSE_CONTRACT.json) |
| THEORY R1–R10 상태 | [state/RESEARCH_STATE.json](state/RESEARCH_STATE.json) |

보고서는 [19쪽 PDF](report/WU088_HH_PHYS16_THEORY_20261013.pdf)와 LaTeX 원고로 완성됐다. 최종 조판 검토는 `report/qa/QA_RESULT.json`, 빌드 지침은 `report/BUILD_KO.md`를 참조한다.

## 실제 검산과 실행 범위

원 고정 C,B,q,S와 signed Hessian을 exact rational 또는 보존된 directed dyadic interval arithmetic으로 사용했다. 원 반응 fit, physical source callback, nonlinear root solve, history replay를 새로 호출한 횟수는 모두 0이다.

Wolfram Language 15.0.1과 xAct xTensor 1.3.0을 실제 사용했다. affine 4D 기체 상태 공간에서 tensor contraction 6개와 scalar 항등식 4개가 정확히 0을 반환했다. 최종 canonicalization은 xPerm의 Wolfram Language group algorithms를 사용했다. 실제 설정 교정·출력·버전·원 archive identity는 위 실행 기록에 보존했다.

원 source 포함 자체의 정칙성·영역·입력 동일성은 PHYS15 및 PHYS14의 채택된 근거를 재사용한다. 현재의 새로운 유도·포함에 대한 독립 심사는 실제 산술 18개 검증군, source 직접 검토, 원고의 부호·가중치·단위·범위를 검토하여 `PROMOTE_SCOPED`로 판정했고, root가 같은 범위에서 채택했다. 채택 기록은 `review/DECISION.json`이며 SHA256은 `610df271576260d01b473c004824ef7179bce475931cfd50c7e017dadfc0bbd3`다. 최종 PDF·전달 확인도 R10에 연결하여 완료했다.

## 실행 환경과 부모 입력

이 패키지는 PHYS15의 보존 입력 폴더를 필요로 한다. 현재 재현 배치는 이 PHYS16 폴더 옆의 `HH_PHYS15_THEORY_20261012_v1`이다. `--parent`에 다른 실제 PHYS15 경로를 지정할 수 있다. 부모는 commit `b4b8019c6f149035c52784aced8e9cd7f3fbb23b`, tree `0a356c941dc7f9c7aacc7245396a9a53fe39dde4`에 대응한다.

Python 3의 표준 라이브러리를 사용한다. 기본 경로의 wrapper는 같은 형제 폴더 배치를 사용한다.

```bash
python3 checks/application/run_application.py reproduction01
```

직접 CLI의 정확한 인자는 다음과 같다. 출력 디렉터리는 새 경로여야 한다.

```bash
python3 src/application/correlated_endpoint_application.py \
  --parent /path/to/HH_PHYS15_THEORY_20261012_v1 \
  --output /path/to/new_application_output

python3 checks/endpoint/read_endpoint_hessian_bounds.py \
  --phys15 /path/to/HH_PHYS15_THEORY_20261012_v1 \
  --output /path/to/new_hessian_readout.json

python3 checks/endpoint/apply_endpoint_remainder.py \
  --phys15 /path/to/HH_PHYS15_THEORY_20261012_v1 \
  --application /path/to/new_application_output/CORRELATED_DEFECT_RESULTS.json \
  --hessian /path/to/new_hessian_readout.json \
  --output /path/to/new_endpoint_remainder_results.json
```

위 명령은 실제 실행 기록에 있는 CLI를 사용한다. 유지된 입력에서는 저장된 결과를 재사용하고, 새로운 입력이나 교정의 영향을 확인할 때 새 이름으로 실행한다. Git에 외부화된 PHYS15 대형 입력을 준비할 때는 부모의 `INPUT_RESTORE.json`과 `src/restore_large_inputs.py`를 따른다.

## 다음 연구

`HH_DEFECT_PARAMETER_RESPONSE`는 같은 global λ,b에 대한 ∂θd와 ∂θΔT를 구한다. 기존 C² source, mixed gas-parameter derivative 및 PHYS09/PHYS14의 U/V carry로 시작할 수 있다. 구체적인 P1–P4 시작식과 성공 기준은 [theory/NEXT_PARAMETER_RESPONSE_PROPOSAL_KO.md](theory/NEXT_PARAMETER_RESPONSE_PROPOSAL_KO.md)에 있다.

원 global DAG bytes와 기존 HH first11 node 값은 보존했다. 새 RUX 완료는 추가하지 않았고, 현재 heavy queue는 비어 있으며 launch=false다.

## 최종 저장과 재개

[PR51](https://github.com/cosmosapjw-quantum/WU088_HH/pull/51)은 PR50 위의 draft 연구 PR이다. 과학 commit은 `23218af77c9872230b47b6e12bde3e7500368c3c`이며, 이후 metadata commit은 실제 backup ACK와 R10 종료를 연결한다. 과학 snapshot은 4,846,184 bytes, SHA256 `148efaf4219b95b9407b145737311c2e603faf1bf003db3188d0a322465b22e3`로 고정했다. Google Drive ID `158GDLZEGouvjhB9WmvS4AscWx-3tUDrL`, Dropbox ID `id:BSpOijBcT10AAAAAAD4RqQ`, rev `65dab6b163c9f0af03d47`에 저장됐고 두 공급자의 실제 크기를 확인했다. 상세 근거는 `publication/BACKUP_ACK.json`을 참조한다.
