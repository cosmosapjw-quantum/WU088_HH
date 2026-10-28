# 다음 변경 입력 계약 — GL2022 HD state block

기계 판독 권위는 NEXT_INPUT_CONTRACT.json이다. 이 문서는 R9_SYNTHESIS_KO.md가 참조하던 후속 계약을 실제 파일로 채운다.

## 문제와 원자료

\[
\mathrm H^++\mathrm{HD}(v=0,j)\longrightarrow
\mathrm D^++\mathrm H_2(v'=0,j')
\]
의 상태별 source를 소비자의 HD 상태 분포에 연결한다. 출처는 González-Lezana, Hily-Blant & Faure, J. Chem. Phys. 157, 214302 (2022), [DOI 10.1063/5.0128598](https://doi.org/10.1063/5.0128598), 식 (5)–(7)과 III.A다.

- [현재 다시 읽은 publisher HTML](https://aipp.silverchair-cdn.com/article-minimal/2842276)
- [원 supplement locator](https://aipp.silverchair-cdn.com/jcp/article-supplement/2842276/zip/214302_1_epaps/)
- [HAL record](https://hal.science/hal-04285297v1), 본문 PDF 214302_1_online.pdf
- [EMAA HD spectroscopy/excitation candidate](https://emaa.osug.fr/details/HD)

반응 (1)의 source support는 초기 j=0..8, 최종 j'=0..9이며 v=v'=0이다. 전체 계산 온도 범위는 5–3000 K이고 원 temperature grid는 아직 확보하지 않았다. 본문은 supplementary material의 수치 존재를 명시하지만 이번 도구 조회에서는 배열이 반환되지 않았다. 과거 HTTP403을 현재 상태로 상속하지 않는다. HAL 현재 metadata는 본문 PDF만 반환했고 EMAA는 우선 반응 (2)의 excitation 자료다.

## 확보할 최소 입력

| 필드 | 필요한 내용 |
|---|---|
| Source identity | 원 파일 bytes/SHA256, DOI, table/file/header, 공개 범위 |
| State rates | 같은 T의 k_jj' 또는 정확한 source convention의 d_j, 단위 cm3/s |
| Spin convention | raw 또는 이미 weighted인지; statistical factor의 중복 적용 여부 |
| Energies | HD E_0j, 단위·zero·isotope; Q가 필요하면 H2와 공통 chemical reference 추가 |
| Support | 실제 초기·최종 상태 범위, 누락 state/tail의 처리 |
| Population | 소비자 x_j 또는 명시적으로 채택한 pi_j |
| Consumer | kinetic T, H+ 밀도 h, proper-time 또는 변환, reference density, number/energy owner |

Source가 raw rates를 주는 경우에만
\[
d_j={1\over4}\sum_{j'\ {\rm even}}k_{0j,0j'}
+{3\over4}\sum_{j'\ {\rm odd}}k_{0j,0j'}
\]
로 집계한다. 이미 가중된 공급자 값에는 같은 인자를 다시 곱하지 않는다. Source의 thermal ensemble을 명시적으로 선택한 경우
\[
\pi_j=\frac{(2j+1)\exp[-E_{0j}/(k_BT)]}
{\sum_{r=0}^{8}(2r+1)\exp[-E_{0r}/(k_BT)]}.
\]
실제 비평형 소비자의 x를 이 분포로 대체하는 결정은 별도다.

## 계산식과 코드 연결

입력을 결속한 뒤 기존 molecular_operator.destruction_defect의 조건부 연산에 새 벡터만 전달한다.
\[
J=h\,d^\mathsf Tx,\quad
J_\pi=h(d^\mathsf T\pi)X,\quad
|\Delta J|\le {h\over2}(d_{\max}-d_{\min})\|x-\pi X\|_1.
\]
HD,H+,H2,D+ 순서의 밀도 source는 (-J,-J,+J,+J)다. 사건 source를 n_ref로 나누면 s^-1이 되지만, reference가 시간에 따라 변하는 population fraction 방정식에는 추가로 -f dot(n_ref)/n_ref 항이 필요하다. 서로 다른 reactant의 반응이므로 동일입자 조합 인자 1/2를 추가하지 않는다.

수지와 단위, 비음수성과 정규화, h=0/상수 d/x=piX 극한 및 새 source literal을 검증한다. Source의 초기·최종 상태 범위가 유한하면 그 범위의 number-source로 판정하고, 누락 상태 효과는 별도 근거가 있을 때 결합한다. k_B를 유지한다.

실제 d/pi/x를 채우는 qualification adapter는 아직 구현·실행하지 않았다. 기존 원식 evaluator의 29 native-node 승인은 그대로이며 새 T로 자동 확장하지 않는다. 현재 코드의 physical_source_binding=false는 새 계약 수용 전에 변경하지 않는다.

## 수용과 중단

새 수치 원본, spin 규약 및 consumer 입력을 확보하면 그 입력에 대해서만 bounded 실행 계약을 작성한다. 원값·식·정수 사건·물리 source·열 Q·광자·activation을 별도로 판정한다. 원배열을 얻지 못했거나 규약·consumer가 미결이면 INPUT_DEPENDENCY로 기록하고 확보된 파일과 출처를 보존한다. 두 aggregate 값에서 9성분 d_j를 역산하지 않으며, 405 K fit 파라미터를 chemical Q로 사용하지 않는다.

이후 실행의 예산은 아직 배정하지 않았다. 기존 PHYS91 잔여0과 미상 global 예산을 유지하며 완료된 R1–R4 과학을 재실행하지 않는다. 이 계약 작성은 새 DAG 노드 완료나 중앙 ACK가 아니다.
