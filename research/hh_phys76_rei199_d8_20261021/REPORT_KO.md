# PHYS76 후속: REI199 D8 저장 표본 접합 분석

## 범위와 상태

이번 additive 보충은 PR130의 별도 후속 작업이다. PR130의 저장 완료 1,231개 `z=4→2` 이력과 PHYS76 계산을 재실행하지 않았다. REI199 B 계열의 L8, 40-state 입력에서 `D8`로 지정된 네 case의 저장 `raw.npz`만 분석했다. 각 case는 `z=2`까지 저장된 153 epoch이며, 관측된 인접 표본의 부호변화 구간을 기록한다. 새 IVP 0회, NCP 0회, benchmark 0회.

owner archive는 `REI_UNIFIED_FINAL_20261021_20261021T111808Z.tar.gz`, 36,855,980 bytes, SHA-256 `7b39d8c8ffa0b61762211295a25d14412de37f6e1a6d163ebf0b93a8337f2251`이다. 분석 시 archive SHA/크기, top-level manifest의 다섯 파일(case별 INPUT/RESULT/ATTEMPT/raw/tail) SHA/크기, 결과의 저장 checks, case/config/grid identity를 검사했다. 스크립트와 결정론적 JSON 결과는 `source/analyze_d8.py`, `D8_RESULT.json`에 있다. 제한 테스트 4/4 통과.

## 부호·프레임 사상

부호 있는 shear는 저장 `s,H`로부터 `Sigma_F,signed = sqrt(6) s/H`로 구성하고 저장 `Sigma_F`와 절댓값을 대조했다. 이는 `sqrt(2)` 배인 full Frobenius scalar이며 PHYS76의 half-contraction과 동일한 양으로 혼동하지 않는다.

물질 `P_m = Pi_F_signed_matter`와 복사 `P_r = Pi_F_signed_gamma + Pi_F_signed_nu`는 같은 정상직교 frame의 서명 있는 별도 기여로 유지했다. 먼저 `P_total = P_m + P_r`를 계산하여 저장 `Pi_F_signed`와 대조한 뒤에만 full Frobenius norm `abs(P_total)`을 저장 `Pi_F`와 대조했다. 부호 있는 성분의 크기를 먼저 합하거나 각 species norm을 합하지 않았다.

## 결과

| REI199 case (`P_m,i`) | 저장 인접 인덱스 | x bracket | a bracket | z (고 z → 저 z) | signed `Sigma_F` endpoints |
|---|---:|---:|---:|---:|---:|
| `-3e-4` | 135–136 | 1.67453403643–1.69049733717 | 0.25410990688–0.25819888975 | 2.93530505076–2.87298334621 | +1.022522174e-6, −2.045413302e-6 |
| `-1e-4` | 141–142 | 1.77031384089–1.78627714163 | 0.27965219830–0.28415219227 | 2.57587033490–2.51924084070 | +7.597778576e-7, −1.892213443e-6 |
| `0` | 144–145 | 1.81820374311–1.83416704386 | 0.29337057893–0.29809132078 | 2.40865809940–2.35467667223 | +8.014231560e-7, −1.669738287e-6 |
| `+1e-4` | 147–148 | 1.86609364534–1.88205694608 | 0.30776191678–0.31271423533 | 2.24926492027–2.19780773315 | +9.145758167e-7, −1.390699766e-6 |

전체 signed 물질/복사 응력, 총 signed 응력, full norm, 고유 elapsed-time endpoint 및 5개 case 파일 해시는 `D8_RESULT.json`에 기록했다.

## 해석 한계와 owner 경계

이는 주어진 저장 격자에서의 엄격한 인접 표본 bracket이다. 연속 ODE의 영점 존재·유일성, 시간 오차, whole-cell source/residual enclosure를 증명하지 않는다. PHYS76 조건부 시간수송의 whole-cell 입력 enclosure와 angular truncation 인증은 계속 OPEN이다. 본 보충 결과만으로 REI199 owner DAG를 변경하거나 production/likelihood admission을 발급하지 않는다.

REI199 live branch에서 관측한 owner HEAD는 `744438f4512c7df1646aad0136ddc435b27200b0`; 그 owner DAG에서 D8은 `ready_not_run`이었다. 이 additive 보충은 D8 분석 산출물이며 owner의 별도 채택/검토가 필요하다. REI213 warm729, HH74 control63 및 REI199의 40/56-state 계열은 다른 데이터 계열이다. REI214/BASS177 exact binary64 cache와 REI215/BASS178 native moment 결과도 고정된 owner/model identity의 후보일 뿐, 이 네 분석에 재사용하거나 대체하지 않았다.

PHYS76의 1,231개 완료 case와 기존 인계 결과는 변경되지 않는다. `HH_R10=OFF`; production admission `NOT_ISSUED`.
