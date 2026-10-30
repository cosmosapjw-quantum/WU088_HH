# R38 동일 세션 적대적 심사 (distinct author 아님)

## Block-critical claims
1. **전자 PES 최소점 대비 37,170 cm^-1**은 H+HD->D+H2 반응 Q로 사용할 수 없다. 이 반응의 BO 채널 에너지 차이는 분자 H₂와 HD의 (v,J) 핵운동 고유에너지 차이이다. 기존 두 R38 경로 모두 질량 차이를 포함한 이원자 radial 문제만 풀었다. 이를 full 3body scattering 인증으로 승격하면 안 된다.
2. **스펙트럼 energy zero mismatch:** spectral 데이터는 `h2(r)+1`로 계산하므로 absolute E가 FD보다 +1 Hartree 높다. `E_H2 - E_HD`만 비교했다. 절대 에너지 직접 비교는 부정확하다.
3. **문턱 / Arrhenius parameter:** GL2022 Eq.(4)의 열평균 rate에 추가 Maxwell tail을 곱하는 것은 같은 열운동 에너지 suppression을 두 번 세는 오류가 될 수 있다. 이번 자료는 kinetic tail을 출력 확률에 곱하지 않았다. GL 논문의 gamma≈405 K 또한 416 K 단일 채널 threshold의 독립 검증이 아니다.
4. **확률 의미:** 19,200개 branch P는 R37 제한 영역의 첫 화학 종료 사건에만 적용된다. 영역 이탈 후 재진입과 재결합을 포함한 cosmological yield가 아니다.

## Numerical checks
- 190채널 exo/endo 분류 190/190 일치. v1 높은 상태에서는 spectral–FD threshold 절대 차이 최대 0.329 K; 모든 값에 동일 정밀도 보증 불가. R37 1,920개 case의 조건부 Q 시프트는 최대 +0.002204 K, 최소 −0.001545 K.
- 19,200행 70자리 source-only Decimal 검산; 최대 prob-sum 차이 <2e−16; input source byte SHA 기록. New Python unittest 정상/-O 각각 7/7.
- 별도 Fortran native compile and readback; original Fortran warnings against function dummy `vex(100)`/two-element actual arrays remain warnings, code may warrant conservative review; only `vex(1..2)` are used in `funcion`. Do not edit original.

## Residual obligations and smallest productive next action
- Original native 3body isotope-dependent reaction probabilities require Hamiltonian with masses and correct coupled-channel boundary and a scattering S matrix or appropriate independently validated SQM capture method; not furnished by a stand-alone electronic PES evaluator.
- GL–EMAA 50 rate discrepancies: require owner attribution or supplementary raw rate provenance for those rows. No implicit source switch.
- Distinct-author R6 and C9 remain NOT_RUN. This report is same-context adversarial checking only.
