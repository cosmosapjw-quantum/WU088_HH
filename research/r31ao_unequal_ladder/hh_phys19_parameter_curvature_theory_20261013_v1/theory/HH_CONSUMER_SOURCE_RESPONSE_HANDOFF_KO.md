# PHYS20 handoff — 실제 소비 구간의 HH 열·전자 source 응답

## 재개점과 완료 목표

PHYS19의 순수 곡률·보간 오차 계산은 끝났으며, 이 handoff 작성 시점의 최종 채택은 독립 심사와 root decision을 기다린다. 해당 identity의 채택 결과를 확인하여 재사용한다. PHYS20의 다음 목표는 **실제 이름과 immutable 입력을 가진 rei_bianchi 구간 하나에서 HH의 절대 온도 변화율과 전자 생성률을 계산하는 것**이다. 기존 HH_DOMAIN_SCREEN와 HH_MATERIALITY를 수행한다. 현재 consumer 입력 결박 상태는 **unverified**다.

완료 결과는 실제 구간의 source/domain 비교, HH source 응답과 다른 source의 기여를 담은 검증된 표, 해당 결론의 유효범위다. 이 파일 작성 중 PHYS20 retrieval·과학 계산·원격 변경은 수행하지 않았다. 간결한 실행 계약은 NEXT_CONSUMER_CONTRACT.json에 있다.

## 1. 첫 targeted retrieval

1. 현재 WU088_HH entry와 채택된 PHYS19 handoff에서 predecessor decision/identity를 읽는다. 기존 provider 계약의 원 위치는 research/r31ao_unequal_ladder/hh_atomic_reuse_plan_20261012_v2/contracts/ 아래 HH_REI_EXPORT_CONTRACT.json, HH_PROCESS_OWNER_ROWS.json, HH_CONSUMER_REQUEST_TEMPLATE.json이다. entry가 가리키는 버전을 사용한다.
2. 연결된 저장소에서 rei_bianchi의 현재 branch/head를 확인하고, 실제 존재하는 CURRENT_DEVELOPMENT_PLAN.json, RESEARCH_STATE.json, HANDOFF 또는 동등 entry가 가리키는 baseline/interval 산출물을 읽는다. **consumer entry가 실제 채택한 구간 하나**를 선택하고 repo·commit/tree·scenario·interval ID를 붙인다. root entry의 포인터를 따라 관련 파일만 회수한다.
3. 그 구간의 gas/photon 입력, source callback/계수, density/clock, geometry/closure, process-owner 자료와 filled consumer request를 결박한다. 이미 실행된 동일 logical case의 원자료를 재사용한다. 확인되지 않은 필드는 그 이름과 필요한 실제 source를 기록한다.

## 2. 최소 consumer 입력

| 묶음 | 실제 필요한 값과 식별자 |
|---|---|
| Identity | repo/head commit·tree, scenario ID, interval ID, source/result object ID 또는 경로·hash, 해당 baseline의 채택 근거 |
| Time·frame | 구간 시작/끝·단위, 표를 평가할 시각 또는 인증 state tube, source derivative의 정의, local collision frame, consumer clock으로의 변환 |
| State·COMMON | \(x=x_{\rm HII}\), \(y=y_{\rm HeII}\), \(z=y_{\rm HeIII}\), \(w\), 입력값/구간과 상관관계; 원 gas/photon COMMON, photon groups/guards, birth·IC·HH switch의 정의 |
| Density·units | physical/comoving 구분, rest-frame \(n_H,n_{He}\)와 단위, 원 stored \(\widehat f=n_{He}^{stored}/n_H\), \(w\)·광자의 H당 정상화, 정확한 energy·\(k_B\) conversion leaves |
| Source·ownership | native source code/version와 계수·fit 범위, HH 반응/channel 및 \(\nu_H\), 동일 입자 pair 계수의 정의, \(\lambda\) switch, thermal/electron/photon 과정별 owner |
| Geometry·closure | background/time-map identity, geometry·tilt/frame, local kinetic/thermal closure, photon remap/absorption operator와 해당 구간 source coverage |
| Question | \(\dot T_{\rm HH}\), \(\dot e_{\rm HH}\)의 signed·absolute 범위. 항 생략 판정까지 요구할 때는 해당 observable의 허용 budget과 transfer를 추가 |

전체 source/fixed-coefficient/COMMON/operator 비교표를 채운다. **Local source admission**은 원 microscopic/thermal closure와 단위·frame·density·상태영역을 근거로 판정한다. **PHYS19 endpoint 결과의 재사용**은 그 결과에 필요한 동일 COMMON·source·geometry·operator family의 일치 또는 증명된 전달을 추가로 요구한다. 서로 다른 기하에서도 local rate를 전달할 수 있는 경우에는 그 local covariance/closure 근거와 clock 변환을 기록한다. 이 두 claim의 범위를 각각 명시한다.

## 3. 계산할 정확한 instantaneous source

원 ideal-mixture thermal readout이 admission된 점 또는 인증된 state tube에서 \(\widehat f\)를 HH 반응에 대해 고정하고
\[
e=x+\widehat f(y+2z),\qquad \Pi=1+\widehat f+e,\qquad
T=\frac{C_Tw}{\Pi},\qquad
C_T=\frac{2\epsilon_{\rm eV}}{3k_B}
\]
를 사용한다. \(\epsilon_{\rm eV}\)와 \(k_B\)는 실제 source의 동일 단위 conversion leaves다. 정의
\[
\ell_e=(1,\widehat f,2\widehat f,0),\qquad e_w^T=(0,0,0,1),
\qquad \dot g_{\rm HH}=\nu_Hq_{\rm HH}
\]
에서, dot을 local collision frame의 physical proper time(초)에 대한 미분으로 정하면
\[
\boxed{\dot T_{\rm HH}
=\frac{C_Te_w^T-T\ell_e}{\Pi}\,\nu_Hq_{\rm HH}},
\qquad
\boxed{\dot e_{\rm HH}=\ell_e\nu_Hq_{\rm HH}},\qquad
\boxed{(\dot n_e)_{\rm HH}=n_H\dot e_{\rm HH}}.
\]
마지막 식은 H nuclei를 보존하는 HH process contribution이다. 전체 \(n_e\) 방정식의 density evolution은 해당 owner가 별도로 제공한다.

원 PHYS15 FT03/LCS source의 구체적인 선택은
\[
\nu_H=(1,0,0,-\chi_H)^T,\qquad
q_{\rm HH}=\lambda n_H(1-x)^2k_{\rm HH}(T).
\]
따라서 이 source가 admission된 경우
\[
\boxed{\dot T_{\rm HH}
=-\frac{C_T\chi_H+T}{\Pi}q_{\rm HH}},\qquad
\boxed{\dot e_{\rm HH}=q_{\rm HH}}.
\]
pair 계수·threshold·switch는 원 source graph의 정의를 사용한다. Independent singlet ion-pair channel에는 그 채널의 실제 \(\nu\), rate 및 electron owner를 적용한다.

**차원 확인:** \(n_H\,[{\rm cm}^{-3}]\), \(k_{\rm HH}\,[{\rm cm^3\,s^{-1}}]\)이면 \(q_{\rm HH}\,[{\rm s^{-1}}]\), \(C_T\,[{\rm K/eV}]\), \(\chi_H\,[{\rm eV}]\)다. \(w\)의 eV/H와 \(\Pi\)의 particles/H 정상화를 함께 사용하면 결과는 K/s, per H/s, \({\rm cm^{-3}s^{-1}}\)다. SI 입력도 같은 차원 검사와 명시된 conversion을 거친다. Source가 \(c^{-1}\partial_t\)를 사용하면 physical per-second 결과를 위한 \(c\)를 복원한다. Consumer clock \(t_c\)에 대해서는 확인된 \(d\tau_{\rm gas}/dt_c\)를 곱하여 변환한다.

## 4. 첫 검증 표와 종료 조건

한 표의 열은 **interval/state identity, clock/frame, \(n_H,\widehat f,T,\lambda,q_{\rm HH}\), signed \(\dot T_{\rm HH}\), \(\dot e_{\rm HH}\), \((\dot n_e)_{\rm HH}\), 단위, source owner, input/coverage 근거**다. 같은 상태에서 계산 가능한 다른 thermal/electron source를 같은 단위로 함께 제시하고 signed total을 보인다. 필요하면 양의 \(\sum_j|\dot T_j|\)를 분모로 HH 절대 기여율을 제시한다. 겹치는 과정은 owner를 대조하여 각 total에 한 번 반영한다.

값·단위·부호·source sum·원 input binding을 독립적으로 검토한다. 실제 consumer 구간의 local source 범위와 지배 입력이 판정되면 이 단위를 닫는다. 입력 결박이 완성되지 않으면 확인된 필드·실제 미확인 필드·다음 최소 retrieval을 기록한다.

## 5. Carry/history의 조건과 독립 lane

Instantaneous 표는 그 state 또는 인증 tube의 local contribution이다. Finite interval 온도·전자 효과를 계산할 때는 실제 state evolution 또는 채택된 source-to-observable response transfer를 결박한다. HH ON/OFF history를 선택하면 기존 HH_MATCHED_HISTORY의 실제 RUX11 baseline, 같은 physical IC/source/closure/geometry, global switch, 연속 gas+photon+guard carry와 매 stage source coverage를 적용한다. BASS의 \(\tau\)/visibility에는 해당 receiver의 실제 결박을 붙인다.

HH_STRICT_NATIVE와 HH_SINGLET은 각각 고유 과학질문과 원 native/microscopic 입력 조건으로 계속 독립 실행 가능하다. 이 다음 목표는 기존 RUX DAG·상태 및 두 lane의 선행조건을 변경하지 않는다. 실행 크기는 회수한 실제 한 구간으로 정하고, 이 handoff의 heavy queue는 비어 있다.


## PHYS19 최종 채택 후 연결

PHYS19는 독립 유도와 실제 Fraction 심사 후 PROMOTE_SCOPED로 채택됐다. 현재 채택 기록은 review/DECISION.json이며, 위 PHYS20 작업의 consumer binding은 계속 unverified / PREPARED_NOT_EXECUTED다.
