# PHYS78 실제 pilot 그림 검토

31개 완료 case의 161개 저장 epoch(z=20→2)로 10개 PNG·PDF를 생성했고 실제 PNG를 직접 확인했다. 대표 원자종 그림은 P013이다. 그림 작업의 신규 ODE 및 benchmark는 0회다.

## 해석 범위

물질 응력은 collisionless nonbaryonic DM, 복사 응력은 anisotropic free radiation에서 온다. 반응 기체에는 isotropic closure π_gas=0을 적용했다. 21개 isotope/charge slot의 PI+RR exploratory 계산이며 핵반응망 전체 완성이나 관측 적합 결과가 아니다. Li III/IV 및 T/n의 정확한 영점은 숨기거나 floor로 올리지 않았다.

## 표시와 실제 값

등방 초기조건인 P013/P029/P030의 수치잔차는 별도 signed 그림 02b에 모두 표시했다. 주 물리 그림은 이 세 control의 관측 최대값 이하인 sample만 명시적으로 생략한다. 이는 display cutoff이고 수치오차 상한이 아니다. 저장 값은 전혀 바뀌지 않았다.

| 양 | 주그림에 보이는 실제 최소 | 실제 최대 | 생략 sample/4508 |
|---|---:|---:|---:|
| Sigma_F | 6.5127959e-06 | 1.0000000e-01 | 8 |
| Pi_m_F | 4.7357882e-10 | 5.4688651e-04 | 10 |
| Pi_r_F | 3.8423206e-10 | 2.3885550e-03 | 10 |
| Pi_total_F | 8.7657612e-07 | 2.9354416e-03 | 4 |

## 잔차와 취소

각 case의 signed tensor 합 이후 norm 취하기와 저장된 norm의 차이는 아래 JSON에 기록했다. Frobenius는 half-contraction norm의 √2배이며, 모든 그림 footer에 이 차이를 적었다.
저장된 energy identity 최대 절댓값은 2.5144527e-16, isotope 보존 잔차 최대값은 1.7350768e-14다. 이들은 sampled algebraic diagnostics이며 continuum certificate가 아니다.
P024에서 |Π_m^s+Π_r^s|/(|Π_m^s|+|Π_r^s|)는 0.627391–0.965295이다. 같은 trajectory의 signed components를 비교한 값이며 species-off 인과 실험이 아니다.

## Figure Hostile Pass / Residual Pass

축과 legend 겹침, log 범위를 지배하던 등방 잔차, z=2 tick roundoff, zero ion의 오해 가능성을 수정하고 실제 그림으로 재확인했다. 주 응력 그림의 cancellation dip과 원자종 전이 구간은 legend에 가리지 않는다. 원시 NPZ·receipt checksum과 표시 manifest가 데이터 출처를 보존한다.

HH_R10=OFF. Production admission은 발급하지 않는다.
