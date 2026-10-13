# R10 다음 단위 추천 — 실제 소비 구간의 HH 열·전자 source 응답

**선택할 목표:** 기존 HH_DOMAIN_SCREEN–HH_MATERIALITY에 연결하여, 실제 rei_bianchi 소비 계열 한 구간에서 **HH가 만드는 절대 열 변화율(K/s)과 전자 생성률(per H/s)**을 source·영역에 결박해 계산한다. 물리 질문은 “이 구간에서 HH 항의 크기와 부호가 얼마이며, 어떤 상태·source 불확실성이 그 값을 지배하는가?”로 고정한다.

**선택 근거.** PHYS19 SUMMARY의 bilinear remainder는 \(6.145761081776\times10^{-12}\) K, 순수 midpoint 보정 remainder는 \(2.892887673208\times10^{-13}\) K다. 반면 \(F_{00},a_\lambda,a_b\) 포함의 전체 폭은 각각 \(3.75147418127\times10^{-4}\), \(1.958485175184\times10^{-9}\), \(4.08987164059\times10^{-6}\) K다. 현재 response shape의 인증을 완료하고, 실제 source·상태·관측량 결박에 계산을 배정하는 편이 다음 물리 판단에 기여한다. 이 폭들은 현재 포함의 해상도이며, 물리적 불확실성의 고유 하한으로 해석하지 않는다.

## 첫 계산과 완료 결과

1. 실제 소비 request에서 한 구간의 원 gas/photon state와 시간·밀도·온도·source code/version·closure·process owner를 가져온다. 원 NCP07/PHYS14–19의 \(C^2\) source, exact density ratio, HH switch/stoichiometry, 33+2 photon graph, geometry 및 양의 \(\Pi\)를 항목별로 대조한다. 비교가 끝나면 해당 구간에서 재사용되는 source와 새로 필요한 source 범위가 구체화된다.
2. HH source를 \(\dot g_{\rm HH}=\nu_Hq(g)\), 원 readout을 \(T=C_Tw/\Pi\)라 쓰고, 실제 채택된 \(\nu_H\)와 density convention으로
   \[
   \dot T_{\rm HH}
   =\left(\frac{C_T}{\Pi}e_w^{T}-\frac{T}{\Pi}\ell_e\right)\nu_Hq,
   \qquad
   \dot e_{\rm HH}=\ell_e\nu_Hq
   \]
   를 외향 포함한다. 같은 구간의 실제 source에서 HH·electron collision·radiative·팽창 항을 같은 단위로 비교하여 지배 항과 입력 폭을 기록한다. 이 signed local source response는 기존 observable transfer를 바로 사용하는 첫 과학 계산이다.
3. 다음 단위의 완성 결과는 **실제 소비 구간 1개의 HH source 응답표, 전체 thermal/electron source에 대한 기여, 적용 가능한 source-domain 결론**이다. 누적 history가 필요해지는 후속 질문에는 기존 HH_MATCHED_HISTORY의 실제 RUX11/carry 조건을 적용한다. PHYS19는 domain이 일치하는 범위의 two-half–Full defect 제어에 재사용한다.

## 필요한 입력과 준비 상태

| 입력 | 현재 확인한 상태 |
|---|---|
| 원 provider source·COMMON·ray/guard·root/carry·finite readout | NCP07/PHYS14–19 입력과 결과가 회수되어 있다. PHYS15 source bridge가 \(n_H,n_{\rm He}^{stored},f,\Pi\), 초기 상태와 시간 구간의 정확한 연결을 제공한다. |
| actual named consumer request, source/scenario identity, 한 구간의 domain | 회수한 PHYS18 DAG는 WAIT_FOR_NAMED_CONSUMER_INPUT으로 기록한다. 이번 분과는 현재 remote consumer의 존재 여부를 조사하지 않았으므로 상태는 **현재 입력 결박 미확인**이다. 다음 루프 첫 작업은 연결된 실제 소비 자료의 targeted intake다. |
| materiality 질문/기준 | 위 절대 source-response 질문으로 바로 정의할 수 있다. 특정 항 생략 결정을 내릴 때 해당 관측량의 실제 허용 budget을 추가한다. |

**독립 lane의 처리.** HH_STRICT_NATIVE와 HH_SINGLET은 각각 고유 과학질문으로 별도 실행할 수 있다. Native의 원 source/ray/root/carry 조건, singlet의 channel/spin/basis/velocity/impact/energy/tail 조건을 유지한다. 원 microscopic 47+2 basis·complex ETF·Hamiltonian-order 연구는 그 lane의 관측량에 결박한다. 이번 소비 목표에서 native source 평가가 추가로 필요하면 적용되는 좁은 영역만 계산한다. 이번 다음 목표의 실행 준비도는 **provider 계산식과 근거 준비 완료, actual consumer 입력 결박 확인 필요**다.

읽은 근거: PHYS19 checks/application/run01/results/SUMMARY.json; PHYS18 NEXT_DAG.json와 publication_overlay/CURRENT_DEVELOPMENT_PLAN.json 및 docs/coding/IMPLEMENTATION_PLAN.md; PHYS15 ROOT_OVERLAY_FINAL.json와 theory/ASSUMPTIONS_AND_BINDINGS_KO.md; PHYS14 NEXT_DAG.json/HANDOFF_KO.md 및 원 COMMON_INPUT_SCOPE의 값. 코드 변경·추가 원전탐색·source/root 실행은 수행하지 않았다.

