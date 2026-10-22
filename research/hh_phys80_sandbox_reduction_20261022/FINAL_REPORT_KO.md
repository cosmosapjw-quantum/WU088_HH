# PHYS80 최종 과학 보고서 — 고정 inventory의 정확한 환원과 sandbox 실행

## 1. 판정과 현재 단계

PHYS79의 고립된 neutral CI + D/H ground-state CX 부분계에서 **21종 abundance와 열에너지의 22상태 방정식을 C01에서는 4상태, C02에서는 1상태로 정확히 환원**했다. 열에너지는 보존량에서 복원하고, 온도 의존성을 포함한 analytic Jacobian으로 Radau를 실행했다. 새 algorithm identity 세 개는 모두 완료했으며, 저장된 PHYS79 궤적과의 scaled-state 차이 및 새 baseline–refinement 차이가 사전 기준 \(10^{-6}\) 아래다. 완료된 PHYS78/79 및 HH1231/REI729/HH74control63 identity 재적분은 0이다.

동시에 저온 CI를 위한 일반 Maxwellian 적분 kernel을 구현·검증했다. 이 결과는 명시적으로 주어진 단면적 함수의 수치 적분을 다룬다. H/He/Li의 실제 저온 CI 계수, isotope threshold, 오차 및 에너지 결합을 승인한 결과는 아니다. 전체 COLLISIONAL_ATOMIC_AND_THERMAL_CLOSURE는 계속 OPEN이다. [실행 원장](EXECUTION_LEDGER.json), [과학 실행](verification/SCIENCE_STDOUT.json), [물리→코드 계약](theory/PHYSICS_TO_CODE_GATE_KO.md)이 각 판정의 범위를 고정한다.

| 단계 | 이 문서가 근거를 확인한 상태 |
| --- | --- |
| 유도 | 고정 inventory, 지정 CI/CX 부분계의 exact reduction 및 Jacobian COMPLETE_SCOPED |
| 코드 | 환원 연산자, strict guard, identity 보존 runner, 일반 Maxwellian kernel COMPLETE_SCOPED |
| 구현 검증 | 독립 유한 검토 PASS_SCOPED; 최초 차분 fixture 실패와 제한된 후속 점검을 함께 보존 |
| 과학 실행 | 새 isolated ODE 3 = control 2 + 별도 refinement 1; 성공 3, 실패 0 |
| 재개 검증 | 완료 identity 3개 바이트 검증 후 skip; 새 ODE 0 |
| 그림 | 3종 PNG/PDF 생성; 실제 PNG 3개 시각 검토 PASS_SCOPED |
| 게시 | Draft PR136 science snapshot 게시 및 원격 135개 파일 검증 PASS; 최종 metadata HEAD는 외부 전달 JSON에 결합 |
| 백업 | S0 checkpoint의 Drive upload ACK 및 Dropbox upload/size ACK 확인; 최종 ZIP의 full-byte/CRC/payload 판정은 외부 final-delivery JSON에 기록 |
| production | HH_R10=OFF; production admission NOT_ISSUED |

## 2. 시작 identity, 새 근거와 접근 범위

부모는 [Draft PR134](https://github.com/cosmosapjw-quantum/WU088_HH/pull/134)의 실제 HEAD \(3304d16db1dc9bf868c185a8eeb6cc9dbc270e50\)이다. PHYS79 science commit \(338fb7728e8b41f49551200b1f1ba73c047fb90c\)의 결과와 부모 source를 byte-pinned 입력으로 재사용했다. 게시용 branch research/hh-phys80-sandbox-reduction-20261022는 게시 전 관측에서도 그 부모 HEAD에 있었다. 새 science commit은 `fd18c59796175191bdd5f9b7ab2981d5e92836fd`이며 [Draft PR136](https://github.com/cosmosapjw-quantum/WU088_HH/pull/136)으로 게시했다. 원격 parent/tree와 135개 Git blob SHA1·size를 확인했고 변경은 모두 새 unit 경로의 추가였다. S0 checkpoint의 provider ID는 [게시 영수증](delivery/POST_PUBLICATION_RECEIPT.json)에 있다. 최종 metadata HEAD와 최종 ZIP identity는 자기참조를 피하기 위해 외부 `PHYS80_FINAL_DELIVERY_20261022.json`과 PR 본문에 연결한다.

초기 증분 intake는 WU의 최근 PR, 지정 sibling PR/branch와 전달 기록을 대조했다. PHYS79 로컬 ZIP 및 외부 delivery JSON의 전체 bytes identity를 확인했고, 이전 양 provider의 전체 bytes/CRC/166 payload SHA 검증은 **재사용 근거**로 분류했다. 이 단계에서 remote ZIP을 다시 내려받았다고 주장하지 않는다. 이전 51 repo/142 branch catalog 전체를 재실행하거나 접근 불가능한 비공개 대화를 전수 조사하지 않았다. [증분 inventory](inventory/INCREMENTAL_INVENTORY_KO.md), [복구 근거의 재사용](inventory/PARENT_RESTORE_EVIDENCE_REUSE.json)을 따른다.

14:40–14:41 UTC의 [게시 전 갱신](inventory/PREPUBLICATION_REFRESH_KO.md)은 부모 ref가 그대로임을 확인했다. REI221에는 별도의 conditional local sandbox science commit \(569f784e78676123513b7390001d317eb62d6372\)가 생겼고, REC120은 기존 8개 THERM01 이력에 전달 복구 자료가 추가됐다. REI의 독립 abundance·주어진 event/energy 입력과 REC의 열 이력은 각각의 계약에 속한다. 그 실행을 PHYS80의 세 ODE에 더하지 않으며, 저온 CI나 고정 inventory 환원에 새 물리 승인을 부여하지 않는다. HE86 ref는 그대로였다. sibling 백업에 대한 upload/size ACK와 full download 검증의 차이도 원문대로 유지한다.

15:04–15:05 UTC에 추가로 확인한 [HH PR135](https://github.com/cosmosapjw-quantum/WU088_HH/pull/135)의 HEAD `6c3b12554288893d5d7e221d77be943324285ceb`와 REI222 HEAD `074933f73743ed10ff98a10db49d1b72696ead4f`는 별도의 D PI/RR event-energy component를 제공한다. 추가 파일 9/9 Git blob identity와 생산자 receipt의 source 3/3 SHA256이 일치했다. 공급된 PI/RR event와 에너지를 thermal/binding/radiation 및 particle-count 온도 항으로 매핑하는 부분은 재사용하고, source-qualified D threshold/rate/RR capture-energy moments와 결합 control은 OPEN으로 유지한다. 생산자 72 event+8 invalid/domain+27 temperature+1 exact cycle 검증을 재실행하거나 PHYS80 수에 합산하지 않았다. [늦은 sibling 판단](delivery/LATE_HH135_REI222_ASSESSMENT_KO.md)과 [원문 identity 영수증](delivery/LATE_HH135_REI222_SCOPE_RECEIPT.json)이 이 S1 metadata 갱신의 근거다. 고정된 124개 PHYS80 과학 payload는 바꾸지 않았다.

## 3. 무엇을 정확히 환원했는가

본 제어계는 고정 proper density, 팽창 없음, PI/RR·thermal bath 없음, neutral CI rows(0,1,3) 및 D/H CX만을 가진다. T isotope와 neutron의 inventory는 0이고 HeIII, LiIII/IV도 0이다. 원소 내 동위원소가 같은 CI kinetic fit을 쓴다는 부모 모델 가정을 유지한다. 일반 재결합·핵반응·주입을 허용한 21종 네트워크 전체에 이 차원을 적용하지 않는다.

\(H,D,B,L\)을 각각 H1, D, He3+He4, Li6+Li7의 보존 abundance라 하고

\[
Q=Y_{\rm HII}+Y_{\rm DII},\quad v=Y_{\rm DII},\quad
h=\frac{Y_{\rm He3II}+Y_{\rm He4II}}{B},\quad
\ell=\frac{Y_{\rm Li6II}+Y_{\rm Li7II}}{L}
\]

로 둔다. 그러면 \(Y_{\rm HII}=Q-v\), \(Y_{\rm HI}=H-Q+v\), \(Y_{\rm DII}=v\), \(Y_{\rm DI}=D-v\)이다. He/Li의 중성 isotope abundance들은 같은 선형 소멸률을 따르므로 초기 중성 isotope 비율이 보존된다. 구현은 초기 상태를 기준으로 한 affine lift를 사용한다. 따라서 실제 저장 IC의 반올림을 보존하면서, 서로 다른 초기 isotope ion fraction도 표현한다. 같은 초기 ion fraction은 그 특수한 경우다.

전자와 총 열입자 수는

\[
x_e=Q+Bh+L\ell,\qquad N=H+D+B+L+x_e
\]

이다. 열에너지 \(u\)의 단위는 eV/H이고, 전체 \(E=u+\epsilon\cdot Y\)가 보존된다. 큰 \(E\)에서 binding을 매번 빼는 대신 다음 anchor를 사용한다.

\[
u=u_0-I_H(Q-Q_0)-\delta_{\rm eff}(v-v_0)
 -I_{\rm He}B(h-h_0)-I_{\rm Li}L(\ell-\ell_0),\qquad
T=\frac{u}{(3/2)k_BN}.
\]

여기서 \(I_H=13.6\), \(I_{\rm He}=24.59\), \(I_{\rm Li}=5.392\) eV는 실제 부모 ionic potential의 차이다. CI rate fit의 He 24.6/Li 5.4 eV threshold와 혼동하지 않는다. \(\delta_{\rm eff}=\epsilon_{\rm DII}-\epsilon_{\rm HII}=0.0037054533027216507\) eV는 저장 potential의 실제 뺄셈이며, 선언한 \(43k_B\)와 약 \(7.76\times10^{-16}\) eV의 반올림 차이가 있다. rate의 detailed-balance exponent는 부모의 43 K 그대로다. 이 구분은 PHYS79의 유한정밀도 동역학과 비교하기 위해 필요하다.

공통 \(n_H\)와 proper time에서 정확한 네 식은

\[
\begin{aligned}
\dot Q&=n_Hk_Hx_e(H+D-Q),\\
\dot v&=n_H\{k_Hx_e(D-v)+k_f(D-v)(Q-v)-k_rv(H-Q+v)\},\\
\dot h&=n_Hk_{\rm He}x_e(1-h),\\
\dot\ell&=n_Hk_{\rm Li}x_e(1-\ell).
\end{aligned}
\]

CX는 Q를 보존하므로 첫 식에서 상쇄된다. CI가 없는 C02에서는 Q,h,\(\ell\)이 모두 고정되어 v만 남는다. 모든 higher charge 0은 이 활성 반응 집합의 불변 부분공간이다.

Jacobian은 \(J=n_H(M+w\otimes\nabla T)\)로, 고정 T 반응 미분과 모든 rate의 온도 의존성을 합한다. \(C_V=3k_B/2\), \(b=(I_H,\delta_{\rm eff},I_{\rm He}B,I_{\rm Li}L)\), \(a=(1,0,B,L)\)일 때

\[
\nabla T=-\frac{b+C_VTa}{C_VN}.
\]

실제 solver 좌표는 \(z=(Q/(H+D),v/D,h,\ell)\), 시간은 부모의 \(\theta=n_Hk_{\rm ref}t\)다. 따라서 대각 scaling과 time scaling을 Jacobian에도 동일하게 적용한다. 원 식, 전체 Jacobian, lift 증명, source-domain 조건은 [상세 유도](theory/EXACT_REDUCTION_AND_JACOBIAN_KO.md)와 [계산 계약](theory/COMPUTATIONAL_CONTRACT.json)에 있다.

C02는 \(T(v)=T_0-\delta_{\rm eff}(v-v_0)/(C_VN)\)를 이용해 닫힌 에너지 scalar 연산자를 갖는다. 물리 구간에서
\(G(v)=e^{-43/T(v)}(D-v)(Q-v)-v(H-Q+v)\)는 엄격히 감소하므로 평형은 유일하고 그 방향으로 접근한다. 유한 시간 끝점을 정확한 평형으로 취급하지 않는다. QSS나 강제 평형을 대입하지 않았고, splitting의 비가환 오차를 없다고 가정하지 않았다. 향후 QSS에는 lag와 느린 변수 결합에 대한 별도 오차 한계가 필요하다.

## 4. 사전에 고정한 실행 계약

C01은 \(T_0=25370.66308424773\) K, \(n_H=10^{-3}\ {\rm cm^{-3}}\), HII/H=0.1, D의 초기 ground-state DB 비율, 나머지 존재 isotope의 singly ion fraction 0.01에서 시작한다. C02는 \(T_0=300\) K, \(n_H=1\ {\rm cm^{-3}}\), HII/H=0.5, **DII/D=\(10^{-6}\)**, 다른 존재 isotope는 중성이다. 물리 시간 범위와 161개 저장 시각은 부모 control과 동일하다.

[REDUCTION_PLAN](inputs/REDUCTION_PLAN.json)은 새 실행 전에 Radau, analytic Jacobian, solver-controlled max step, baseline rtol=\(2\times10^{-8}\)/scaled atol=\(2\times10^{-11}\), refinement \(2\times10^{-10}\)/\(2\times10^{-13}\)을 고정했다. Newton RHS/Jacobian trial부터 strict nonnegative state와 source-domain guard를 유지했고, clipping·projection·signed trial extension은 사용하지 않았다. C01 활성 neutral CI의 하한 \(k_BT=1\) eV와 D/H CX fit의 2.7–200000 K 조건을 확인한다. 모든 accepted endpoint 및 161 dense samples를 검증하지만 전체 interpolant의 연속 인증은 아니다.

사전 gate는 부모 궤적 및 새 refinement scaled-state 차이 \(10^{-6}\), isotope 상대 오차 \(10^{-10}\), total energy 상대 오차 \(2\times10^{-10}\), C02 extent-temperature 절대 오차 \(10^{-9}\) K와 평형 거리/D \(10^{-6}\)이다. worker 1/thread 1, 실제 shared lease 아래 순차 실행했으며 다른 process 종료는 0이다. create-only claim, 매 solve 직전 호출 marker, 실패·부분 결과의 자동 replay 차단을 유지한다. 완료 receipt와 NPZ bytes를 확인하면 동일한 execute 명령도 skip하며 별도 resume 옵션을 요구하지 않는다.

## 5. 실제 과학 실행 결과

| 새 실행 | 차원 | 새 Radau nfev | 저장된 부모 DOP853 nfev | 부모 대비 최대 scaled-state 차이 | 새 solve wall s |
| --- | ---: | ---: | ---: | ---: | ---: |
| C01_REDUCED_BASE | 4 | 463 | 15557 | \(3.5858783426\times10^{-9}\) | 2.844910 |
| C02_REDUCED_BASE | 1 | 933 | 2909 | \(8.8829681149\times10^{-10}\) | 0.772949 |
| C01_REDUCED_REFINED | 4 | 1422 | 60773 | \(4.0196554386\times10^{-11}\) | 2.625782 |

이 표는 [실제 새 영수증](verification/SCIENCE_STDOUT.json)과 저장된 부모 영수증의 계산량을 나란히 표시한다. 부모 solver는 다시 실행하지 않았다. 두 알고리즘의 실행 시점과 host 부하는 같지 않으므로, paired wall-time benchmark나 보편적 가속 배수를 주장하지 않는다.

새 C01 baseline–refinement의 최대 scaled-state 차이는 \(3.5481474703\times10^{-9}\)다. C01 온도는 약 25370.663084→24461.949998 K, C02는 300→299.999793080427 K로 변했다. C02의 전자 abundance 변화는 관측상 0, closed-energy extent 온도 차이는 \(5.6843418861\times10^{-14}\) K, 최종 평형 거리/D는 \(3.6705103993\times10^{-9}\)다. 평형 비교에는 저장된 PHYS79 scalar equilibrium oracle를 재사용했으며, 이번 PHYS80의 새 root solve는 0이다.

세 결과의 isotope 상대 오차 최대는 \(1.8375257965\times10^{-16}\), 저장 total-energy 상대 오차 최대는 \(2.2204460493\times10^{-16}\), 최소 종 abundance는 0이다. accepted mesh는 각각 66/134/203점이며 모두 온도 domain, positivity, thermal energy gate를 통과했다. runner의 isotope 정량 gate는 161개 저장점에 적용했다. 후속 독립 저장결과 감사는 accepted mesh 403개 점(초기점 포함, 실제 step 400개)과 dense sample 483개를 한 번 후처리했고, isotope 상대 오차 최대 2.2204460493e−16와 absent isotope 0을 확인했다. 이는 ODE·RHS·rate 재평가가 없는 별도 근거다. [감사 영수증](verification/independent/postflight_audit_001.json)을 참조한다. 열에너지를 first integral에서 복원하므로 작은 energy residual 자체는 독립 정확도 증거가 아니다. 별도 full-event 연산자와의 접선 비교, 다른 solver의 저장 궤적과의 비교를 함께 사용한다.

science identity는 C01 base 98f621e3a855548a7c8e379c38093815313d8fdb703bfd25fa7eaddaa1f05bdc, C02 base 8647a92cba02fcc2fbcce7a121361c150f4cce36e096412f28476d6bd6126ef3, C01 refined 639fcf6f214f864b7a23a947d9c7127c0c1195e79333fbeaf903318482926a51이다. [재개 영수증](verification/RESUME_STDOUT.json)은 이 세 identity를 모두 SKIP_COMPLETE_VERIFIED로 기록하며 새 ODE는 0이다.

계획의 2026-10-22T06:45:09.601278+00:00와 실행 영수증의 14:38 UTC는 원래 timestamp대로 보존한다. 그 사이를 연속 연산 시간으로 해석하지 않는다. 실제 command wall은 약 23.754 s이고 위 표는 각 solve timer다. 샘플 일치와 한 번의 정련은 continuum certificate가 아니다.

## 6. 검증 회계와 그림

Wolfram은 context 1회 후 evaluator 3회 중 algebra 성공 2회와 syntax failure 1회를 보존했다. 성공한 계산은 21종 lift, 전자/입자/에너지 chain, 4×4 Jacobian, scalar 및 rate 미분의 symbolic residual 0을 확인한다. 실패 영수증을 성공 호출로 바꾸지 않았다.

[독립 코드 검토](verification/independent/REVIEW_KO.md)는 16개 **논리 점검군** 중 최초 15 PASS와 차분 fixture 실패 1개를 기록했다. Li6 초기 ion fraction 0의 경계를 중앙차분이 넘어서 strict guard가 올바르게 거부한 사례다. 생산 코드를 완화하지 않고 도달하지 못했던 마지막 3점만 내부점에서 보완했다. 완료된 Jacobian 9점 재검증은 0이고, 합계 12점/39열이 사전 gate를 통과했다. 별도로 full-event 접선 13점의 최대 정규화 오차는 \(3.8179583055\times10^{-16}\), rate derivative 23점의 최대 상대 오차는 \(1.3290252565\times10^{-9}\)였다. 거부 경로와 identity/cache fixture도 같은 검토에 포함되며 별도 test suite 수로 더하지 않는다.

일반 Maxwellian kernel의 **고유 unittest method 6개 PASS**는 위 16개 점검군과 별도다. 순수 A 단면적 witness 9개에서 32/64차 적분 profile 18개를 analytic E1 oracle과 비교했다. 이 kernel 검증의 ODE 실행은 0이다. [kernel 영수증](source/maxwellian/BELL_KERNEL_VERIFY_RECEIPT.json)을 보존한다.

[F01 궤적 비교](figures/F01_saved_trajectory_comparison.png), [F02 오차·계산량](figures/F02_accuracy_and_work.png), [F03 Maxwellian 수치 계약](figures/F03_maxwellian_numeric_contract.png)은 저장된 결과만 읽어 만들었다. F03은 \(I=10\) eV, \(A=4\times10^{-14}\ {\rm eV^2cm^2}\), B 없음의 합성 witness다. 3종의 PDF도 함께 제공한다. [렌더 영수증](verification/FIGURE_RENDER.json)의 당시 visual_QA=PENDING은 보존했고, 이후 [실제 PNG 시각 검토](verification/FIGURE_VISUAL_QA.json)가 PASS_SCOPED를 기록했다. PDF는 같은 그림의 export이며 독립 raster 검토를 주장하지 않는다.

## 7. 일반 저온 Maxwellian kernel의 성과와 남은 물리

\(\theta=k_BT\)를 eV로 쓰면, 주어진 electron-impact 단면적에 대한 rate는

\[
k(T)=C\theta^{-3/2}\int_I^\infty E\sigma(E)e^{-E/\theta}\,dE
\]

이다. Bell 형식은 \(x=(E-I)/\theta\)로 변수 변환하여 Boltzmann suppression을 log-rate로 보존하고, Gauss–Laguerre 적분으로 number 및 입사 에너지 moment를 계산한다. finite log-rate와 floating underflow를 구별하고, 평가된 음의 단면적은 clipping 없이 거부한다. 순수 A 항은 E1 함수의 별도 oracle을 갖는다. [상세 유도](source/maxwellian/MAXWELLIAN_DERIVATION.md)와 [구현](source/maxwellian/bell_kernel.py)에 단위·normalization·tail 조건을 명시했다.

그러나 [Bell 원문](https://srd.nist.gov/jpcrdreprint/1.555700.pdf)의 H Table 5 B1 추출값과 후대 전사 사이의 자릿수 차이는 해결되지 않았다. threshold 바로 위 단면적의 형태·정규화·오차, He/Li 계수, isotope 에너지 일관성도 더 닫아야 한다. species 계수를 내장 기본값으로 등록하거나 이 kernel을 기존 궤적에 활성화하지 않았다. 32/64차 일치는 엄밀 quadrature certificate가 아니고, 유한 적분점에서의 positivity는 전체 에너지 구간 증명이 아니다. 유한 상한 tail bound에는 실제 단면적 envelope가 필요하다. [출처 판단](source/maxwellian/LOW_T_SOURCE_ASSESSMENT.md)과 [조회 영수증](source/maxwellian/SEARCH_RECEIPTS.json)에 Exa/SciSpace 및 primary-source evidence의 범위를 남겼다.

CI의 입사 전자 에너지 moment는 shared thermal pool의 net cooling과 동일하지 않다. 충돌 후 전자들도 thermal pool에 남으므로 화학 potential defect와 에너지 보유·방출을 따로 회계해야 한다. 이 일반 kernel은 새 cooling adapter를 공급하지 않는다.

## 8. 다음 DAG와 재개 조건

다음 physics→coding 노드는 LOW_T_CI_SOURCE_COVERAGE의 구체적 species/threshold/uncertainty 계약이다. 이를 닫은 뒤 기존 CI 연산자의 에너지 potential과 결합한다. He/Li의 state-resolved CX와 radiative photon-energy moment, RECOMBINATION_TO_Z20_INITIAL_CHARGE_CONTRACT, Li hard-UV inner-shell/branching/spectral-energy 계약은 계속 OPEN이다. D PI/RR energy adapter는 HH135의 보존적 event-energy/C99 component를 재사용하는 PARTIAL 상태다. D의 threshold-consistent rate와 matched RR capture-energy moment, photon retention/escape 결합 및 새 coupled control은 여전히 OPEN이다. 전체 핵반응·분자·excitation/free-free/Compton·spectral transport의 완성을 주장하지 않는다.

T/neutron의 양의 주입이나 새 반응을 넣으면 보존 inventory와 invariant manifold부터 다시 유도해야 한다. 현재 4/1차원 변수를 자동 재사용하지 않는다. 새 물리 조건을 선택할 때 이미 완료된 symbolic/finite/ODE identity는 근거로 재사용하고, 변경된 의존성만 점검한다. S0 science의 실제 descendant commit·Draft PR·원격 payload와 checkpoint 저장 ACK는 확인했다. S1 metadata commit은 과학 124개 payload를 유지하며, 최종 HEAD/ZIP/provider full-byte·CRC·payload 검증은 외부 final-delivery JSON으로 마감한다. [Codex handoff](CODEX_HANDOFF_KO.md), [다음-thread 시작문](NEXT_THREAD_HANDOFF_KO.md), [게시·전달 연결](POST_PUBLICATION_HANDOFF_KO.md)에서 같은 외부 identity를 조회하도록 명시했다.

상위 non-tilted LRS Bianchi I 계약, 같은 normal orthonormal frame에서 signed matter/radiation tensor를 먼저 합한 뒤 norm을 취하는 규칙, Frobenius=\(\sqrt2\)×half-contraction을 유지한다. reacting gas의 \(\pi=0\), 비영 \(\pi_m\)은 collisionless DM이다. 이번 고립 parcel의 수치 결과가 새 우주론적 stress closure를 제공하지 않는다.

## 정책 적용 부록

사용자가 이번 turn에 선택한 embedded physmath workflow 1.0.0과 physics·coding 양 트랙의 명시적 실행 지시를 적용했다. cloud 1.3의 기본 R10 정지와 과거 AGENTS의 PHYS71 우선순위는 현재 허가된 작업을 막는 규칙으로 승격하지 않았고, 과거 지침 파일·실행 근거도 고치지 않았다. 연구 단계 R10과 별도 기능 flag HH_R10을 구분한다. 정확한 R1–R10/C1–C10 단계명과 증거 연결은 [20단계 근거표](RESEARCH_LOOP_AND_CODE_MAP_KO.md)에 있다. 강한 no-go 정리를 주장하지 않는다. HH_R10=OFF, production admission NOT_ISSUED를 유지한다.
