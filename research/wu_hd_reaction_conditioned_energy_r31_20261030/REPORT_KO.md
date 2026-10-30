# WU R31 | 실제 출처 기반 HD 화학반응 전 에너지 분배 데이터

2026-10-30 KST. **새 물리적 결과**: R30 고정 온도·고정 n(H+) 5준위 HD absorbing source model의 충돌 가열·냉각 기여, 광자 복사, 반응 직전 HD 내부 회전 에너지를 원본 GL2022 계산률과 Sung2022 measured fitted rotational centers로 정량 분해했다. 새로운 관측자료/원본 PES 단면적은 생성하거나 확보했다고 주장하지 않는다.

## 수치 결과 (105 K, 초기 J2, n(H+)=3954.4181821071797 cm^-3, Eq6–7 spin-effective)

- 원래 HD 내부 에너지: `5.3051876415004004e-21 J`.
- 양성자 열저장고에 전달하는 signed heat: `-8.507972699776604e-22 J` (열저장고에서 HD로 순 에너지 공급).
- 반응 전 photon energy `2.580602925218754e-21 J`.
- 반응 직전 HD 내부 회전 에너지 `3.575381986259306e-21 J`.
- 보존 residual `+7.52316384526264e-37 J`.
- 기대 하향/상향 H+충돌 건수: `19.944239322083135` / `20.21929312527658`.
- 초기 J0에서는 \(B=-(R+F)\): 예 `-5.823835429184337e-21 J` bath gain; photon `2.4600708316649924e-21 J`, terminal `3.3637645975193524e-21 J`.

**동일 밀도 정책 비교** (105 K, 초기 J2, 동일 n(H+) = 3954.4181821071797 cm^-3): raw SQM \(B=+7.483131835456486\times10^{-22}\) J, spin-effective \(B=-8.507972699776604\times10^{-22}\) J. 순 bath energy 방향이 반대로 바뀌는 *조건부 산란 branch policy 효과*다. R29/R30에서 같은 `n/ncrit`은 두 정책의 실제 밀도가 달라 정책 효과만을 격리하지 못했으며, 이 문제를 35 source-T×J paired cases로 직접 교정했다. 불확실성 신뢰구간이나 원 실험 결과가 아니다.

## 실제 생성 파일

| 파일 | 독립 물리 행 수 | 의미 |
|---|---:|---|
| results/R31_ROTATIONAL_ENERGY_210.csv | 210 | initial, signed bath gain B, photon R, terminal HD F, balance residual |
| results/R31_COLLISION_ENERGY_2100.csv | 2,100 | j→i original down/derived up, expected collisions & energy heat |
| results/R31_TERMINAL_STATE_1050.csv | 1,050 | 5 HD final rotational states at the restricted reaction event |
| results/R31_PHOTON_ENERGY_840.csv | 840 | four spontaneous HD line energies and expected counts |
| results/R31_POLICY_FIXED_DENSITY_35.csv | 35 | policy-only paired differences at matched n(H+) |
| results/R31_MATCHED_DENSITY_HEAT_105K.png | figure | signed collisional heat across initial HD J |
| results/INDEPENDENT_MP75.json | 630 comparisons | independent high precision algorithm, same author |

## 실행 결과

Python 16/16 normal, 16/16 `-O`, Python compileall PASS; 210/210 energy residuals, 35/35 fixed-n density difference balance, same-author mpmath75 210×3 =630 energy metrics; symbolic Wolfram 2 initial states `{True,True}`. 출처 ZIP SHA와 nested R29 identity checked. R30 source ZIP byte-preserved unchanged, R29 and original GL2022 data never edited.

## DAG / 권한 상태

중앙 WU DAG **34/49 불변**, R31 신규 물리 보조단위 **1/1 SCOPED**로 신설. 다른 WU R29 1/1 및 R30 1/1 별도 소유. R6/C9 별도 작성자 검증은 **NOT_RUN**, native subagent NOT_EXPOSED. `PES_NATIVE_THRESHOLD=NULL`, `PHYSICAL_Q=NULL`, `OWNER_ACK=NOT_OBTAINED`, `HH_R10=OFF`, `FULL_A=NULL`, `L4=false`, `PRODUCTION=NOT_ISSUED`. CR/REC나 main은 변경하지 않음. 다음 원전 확보: EMAA HD/H+ numeric RADEX ASCII (171×25), Velilla2008 Fortran 및 native σ(E), CDMS2011 v2 raw original fit/covariance, 실제 원 소유자 ACK.