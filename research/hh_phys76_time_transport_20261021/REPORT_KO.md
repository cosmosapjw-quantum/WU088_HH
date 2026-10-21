# PHYS76 — signed sector transport와 z=20→2 preliminary pilot

## 결과와 범위

PHYS75의 실제 미완료 DAG에서 **CONTINUUM_TIME_ANGULAR_CERTIFICATE의 시간 응답 부분**을 선택했다. 전체 cell enclosure가 주어졌을 때 유효한 signed 선형 응답 구간 정리를 유도하고 구현했다. 이와 별도로, 원래 1,231개 long collisionless 이력의 z=4 종단상태에서 **새 z=4→2 구간만** 이어서 사용자가 요청한 z=20→2 예비 시간진화 및 parameter-sweep 그림을 완성했다.

이번 단위의 실제 과학 실행은 **신규 tail ODE 1,231회, 실패 0, 기존 z=20→4 재실행 0, NCP 작업 0, benchmark 0**이다. 완료된 65개 원래 표본에 tail의 중복 시작점을 제외한 32개를 붙여 case당 97개, 총 119,407개 표시 상태를 얻었다. 적분 자체는 원래 8상태 owner와 DOP853 허용오차를 유지했다. 분석·그림 단계는 저장 데이터만 읽었다.

이 결과는 **non-tilted, reflection-even LRS Bianchi I의 유한 L8 collisionless pilot**이다. 물질은 원래 massive Vlasov 성분 및 등방 dust, 복사는 원래 photon/massless-neutrino 성분을 따른다. 따뜻한 C15 H/He/UV, full cold EoR coupling, 일반 non-LRS tensor 문제와 구분한다. 초기 다른 sector의 anisotropic stress가 0인 slice에서도 해당 species의 배경과 동역학은 남아 있다.

현재 결과의 과학적 수용은 **PRELIMINARY_SAMPLED_SAME_TRAJECTORY_DIAGNOSTIC**이다. HH_R10=OFF, production admission=NOT_ISSUED다. 연구 절차의 R10 종료와 프로젝트의 HH_R10 admission은 서로 다른 상태다.

## 1. 출처와 최신 결과 대조

| 역할 | 고정 identity |
|---|---|
| 과학 기준 WU088_HH PR128 | 92f5ab9dba531ebe05909dcb77d3740d2c68c580 |
| 보충 게시 WU088_HH PR129 / 이번 branch의 remote 조상 | b76fd4b5d0dfe4850ebde66a8a10f78402d36c00 |
| REI198 게시 HEAD | 8bd35af5f11c7ea5945b656be1c013d1c1933498 |
| REI198 long archive SHA256 | 2c1433a92ae68c328436852b2842c9b7c51d30b9ff84a22fe2dffbd04ee4246d |
| 1,231 종단상태 index SHA256 | 62f5d96fd323b1ed60c61f4b51e35ab80eb3498d2800c6c04addc1e5e2483115 |
| 이번 실제 실행 runner SHA256 | 959952f9d347bcc515410ef90b3b8dc4b36388ad4bfd2acc2bac356fafd6d97b |

PR128/129의 실제 HEAD, PHYS75_FINAL_DELIVERY_20261021.json, POST_PUBLICATION_HANDOFF_KO.md, DAG_OVERLAY.json 및 관련 백업의 metadata/원본을 대조했다. HH의 기존 138개 branch ref와 최근 PR 기록을 열거했고 관련 DAG·보고서·입력 소스를 선택해 읽었다. 제공된 프로젝트 자료도 관련 프로토콜을 판별했다. 모든 branch의 모든 파일을 읽었다는 뜻은 아니며, 비공개 대화 검색은 현재 도구에서 unavailable이었다. 이를 포함한 조사 범위와 실패는 evidence/INVENTORY.json 및 FINAL_REMOTE_IDENTITY_CHECK.json에 남긴다.

PR129 standalone shear_attribution.py는 explicit source mapping을 요구하는 보충 도구로 보존했다. 이번 endpoint 비교는 **PR128의 stress_memory.py**를 직접 기준으로 사용한다. PR128에서 언급한 별도 FULL 과학 archive는 조사 범위에서 찾지 못했으며, 이 전달 공백을 지우지 않았다. 대신 원래 REI198 archive 37,945,383 bytes의 실제 바이트를 확보하고 5,747개 payload와 manifest를 대조하여 1,231개 원시 상태·component 진단을 복원했다.

동시 작업에서 REI PR214/BASS177의 ACCEL01 exact binary64 (x,b) cache 및 pending-only executor를 확인했다. 최종 재조회에서는 REI PR215/BASS178의 ACCEL02 native massive-moment/C++ 선택 경로와 REI PR199의 별도 40/56상태 z=20→2 unified pilot도 발견했다. 이들은 이번 실행 뒤의 최신 대조표에 포함한다. 같은 vendor 파일이 있어도 state, wrapper, closure, 초기 parameter축, 시간 표본 identity가 다르면 이력을 합치지 않는다. 이번 완료한 8상태 owner를 새 warm/native owner로 소급 교체하지 않았다. 정확한 최신 HEAD·경로·재사용 조건은 FINAL_REMOTE_IDENTITY_CHECK.json을 따른다.

## 2. 물리 정의와 차원

같은 정규직교 normal frame에서
\[
\sigma_{\hat a\hat b}=\operatorname{diag}(-s,-s,2s),\qquad
\pi^{(A)}_{\hat a\hat b}=\operatorname{diag}(-p_A,-p_A,2p_A),\quad A=m,r.
\]
고유시간 \(H,s\)는 s\(^{-1}\), \(p_A\)는 J m\(^{-3}\)이며 \(K=8\pi G/c^2\)다. 따라서
\[
\dot s+3Hs=K(p_m+p_r)
\]
의 모든 항은 s\(^{-2}\)다. 에너지밀도 convention에서 \(Kp\)를 사용하며 \(8\pi G/c^4\)를 고유시간 방정식에 그대로 대입하지 않는다.

Signed half-contraction 좌표와 full Frobenius 관측량은
\[
S=\sqrt3\,s/H,\qquad P_A=\sqrt3 Kp_A/H^2,
\]
\[
\Sigma_F=\sqrt2|S|,\qquad
\Pi_{A,F}=\sqrt2|P_A|,\qquad
\Pi_{\mathrm{total},F}=\sqrt2|P_m+P_r|.
\]
즉 \(\sqrt{T_{ab}T^{ab}/2}\)를 쓰는 기존 half convention과 \(\sqrt{T_{ab}T^{ab}}\) 사이에는 \(\sqrt2\) 차이가 있다. 그림·endpoint CSV는 F를 명시하고 입력의 signed half 좌표도 보존한다. Total은 signed tensor를 먼저 합한 후 norm을 취한다.

\(x=\ln(a/a_i)\), \(H>0\)라 두면
\[
S'+\alpha S=P_m+P_r,\quad
\alpha=3+H'/H=2-q_{\rm dec},\quad
q_{\rm dec}=-1-H'/H.
\]
실제 저장 상태의 이름 q는 \(s/H_{\rm ref}\)이며 감속 parameter \(q_{\rm dec}\)와 다르다.

\[
I(x)=e^{3(x-x_i)}H(x)/H_i,\qquad
S(x)=\frac{S_i}{I(x)}+J_m(x)+J_r(x),
\]
\[
J_A(x)=I(x)^{-1}\int_{x_i}^{x}I(u)P_A(u)\,du.
\]
이 식은 하나의 실제 coupled trajectory에서 H와 두 source를 고정한 조건부 기여 분석이다. Species-off 실험은 H와 source 자체를 바꾸므로 이 분해만으로 그 인과 효과를 판정할 수 없다.

## 3. 채택한 경량화와 vectorization

PR128 endpoint composite Simpson과 맞으면서 모든 저장 node의 기여를 한 번에 얻도록 source/cumulative_memory.py를 작성했다. Local propagator
\[
T_{ij}=\exp[3(x_i-x_j)+\log H_i-\log H_j]
\]
를 사용하므로 매우 큰 전역 integrating factor 배열을 만들지 않는다. 균일한 홀수 node grid에서, 짝수 k는
\[
J_k=T_{k-2,k}J_{k-2}
+\frac h3(T_{k-2,k}P_{k-2}+4T_{k-1,k}P_{k-1}+P_k),
\]
홀수 k는
\[
J_k=T_{k-1,k}J_{k-1}
+\frac h{12}(5T_{k-1,k}P_{k-1}+8P_k-T_{k+1,k}P_{k+1})
\]
로 계산한다. Case 및 sector축은 NumPy로 함께 처리하고 시간축만 선형 순회한다. K개 case, N개 저장 node에서 필요한 산술은 O(KN)이다. 각 prefix를 독립 적분하는 가상 O(KN²) 구현과 복잡도를 비교할 수 있지만, 원래 PR128 endpoint 코드가 O(KN²)였다는 주장은 하지 않는다.

홀수 node는 다음 저장점을 사용하고 음의 가중치를 포함한다. 따라서 offline 누적 진단이며 causal online solver나 positivity-preserving quadrature가 아니다. SciPy 1.17 cumulative_simpson의 quadratic interpolation 정의와 직접 대조하고 endpoint에서 PR128을 확인했다.

새 tail에는 검증된 원래 8상태 owner를 그대로 재사용했다. 원래 phase-space populations를 새로 크게 적분하거나 다른 closure로 줄이지 않았다. 다른 세션의 exact cache/native moment 최적화는 코드·식·입력 identity가 맞는 범위에서 후속 재사용하도록 기록했다. 성능 benchmark를 실행하지 않았으므로 몇 배 가속이나 최적 worker 수를 주장하지 않는다. 자세한 채택·보류 결정은 OPTIMIZATION_REUSE_KO.md에 있다.

## 4. 실제 미완료 의무를 진전시킨 구간 정리

한 cell 폭 h>0에서 \(\alpha\in[\alpha_-,\alpha_+]\), \(P_A\in[p_{A,-},p_{A,+}]\)가 **cell 전체에 대해 인증**되고 시작 \(J_A\) enclosure가 주어졌다고 하자. 다음을 정의한다.
\[
\Phi(a,h)=\int_0^h e^{-au}du=
\begin{cases}(1-e^{-ah})/a,&a\ne0,\\h,&a=0,\end{cases}
\]
\[
\mathcal G=[e^{-\alpha_+h},e^{-\alpha_-h}],\qquad
\mathcal R=[\Phi(\alpha_+,h),\Phi(\alpha_-,h)].
\]
양의 Green kernel과 signed source의 가중평균으로
\[
\mathcal J_{A,n+1}=
\mathcal G\mathcal J_{A,n}+
\mathcal R[p_{A,-},p_{A,+}]
\]
가 실제 \(J_A(x_{n+1})\)를 포함한다. \(\alpha>0\)는 필요하지 않다. Initial memory에도 같은 \(\mathcal G\)를 적용한다. 계수의 상관을 잃어 범위가 넓어질 수 있으나 포함관계는 유지된다.

source/interval_transport.py는 Decimal의 directed arithmetic, correctly rounded exp의 인접 표현가능 endpoint 및 작은 인자에 대한 명시적 series tail bound로 이 재귀를 구현했다. Underflow/subnormal/overflow는 허용 범위 밖으로 처리한다. Witness 문자열은 provenance를 보존할 뿐 그 내용을 인증하지 않으므로 출력은 항상 conditional_on_input_enclosures, input_witnesses_verified=false다.

실제 저장 표본만으로 whole-cell 입력 enclosure는 나오지 않는다. Coupled Einstein–Boltzmann residual과 angular truncation bound를 공급하는 단계는 남아 있다. 따라서 부모 CONTINUUM_TIME_ANGULAR_CERTIFICATE는 OPEN으로 유지하고, 이번에는 그 하위 transport 정리·구현만 완료했다. 이 결과는 기존 variation of constants와 interval arithmetic의 구체적 적용이며 새로운 no-go나 문헌 신규성을 주장하지 않는다.

## 5. 신규 z=4→2 계산과 이어 붙이기

모든 case의 원래 \(x_*=\ln(4.2)\), 8상태
\[
(\tau=H_{\rm ref}t,b,q=s/H_{\rm ref},E_0,E_2,E_4,E_6,E_8)
\]
와 case별 matter amplitude를 그대로 읽었다. \(a_{\rm ref}=1/21\), \(H_{\rm ref}\), owner 파일 7개와 archive manifest를 고정했다. 원래 종료 설정은 이전 run의 xmax였고 RHS 자체의 물리 domain 경계가 아니므로, source 점검과 정량적인 chart/positivity guard 후 새 구간 \([x_*,\ln7]\)만 적분했다. initial()과 원래 solve()는 호출하지 않았다.

새 구간은 원래와 같은 DOP853, rtol=3e-11, atol=3e-13, 시작점 포함 33저장점이다. 최초 독립 점검에서 sampled brightness의 한 열 GEMV와 batch GEMM 사이 최대 1.11e-16의 마지막 비트 차이가 확인됐다. 기존 상태를 33열로 반복하여 동일한 원래 batch 연산 형상으로 restart 진단을 비교하도록 고쳤다. 시간 진행 없이 모든 1,231개 restart가 정확히 일치했으며, 허용오차를 완화하거나 저장 값을 덮어쓰지 않았다. 최초 실패 검토도 보존했다.

기존 65점 grid와 새 33점 grid는 각각 균일하지만 spacing이 다르다. 결합한 97점을 uniform Simpson에 넣지 않고 각 segment의 누적 응답을 별도로 구한다.
\[
D=T D_*,\qquad J_A=T J_{A,*}+j_A^{\rm tail},
\]
\[
r_{\rm combined}=r_{\rm tail,local}+T\,r_{\rm old,*}.
\]
따라서 기존 endpoint 오차를 새 initial memory에 흡수해 숨기지 않는다.

## 6. Parameter sweep와 preliminary 결과

Nominal 초기축은 원본 metadata로 복원했다. 모멘트 진단의 binary64 마지막 비트 차이를 서로 다른 물리 parameter로 세지 않았다.

| Lane | Case | 초기 signed half 축 |
|---|---:|---|
| Radiation slice | 625 | S0 25점, -0.004…0.004; Pr0 25점, -0.001…0.001; Pm0=0 |
| Matter slice | 600 | 같은 S0 25점; Pm0 24개 비영점, -0.0004…0.0004; Pr0=0 |
| Opposing mixed | 6 | S0=(-0.004,0,0.004); Pm0=±0.0004, Pr0=-Pm0 |

Matter의 zero initial-stress 축은 기존 radiation grid의 공통 zero-stress 축과 중복되므로 새 case로 계산하지 않았다. Figure04는 600개 lane의 비영점 grid를 그대로 표시하고 빠진 열을 임의 interpolation하지 않는다. Mixed 6개는 독립 3차원 Cartesian sweep이 아니다.

대표 mixed_s+0_m+1은 초기 \((S_0,P_{m,0},P_{r,0})=(0,+4e-4,-4e-4)\)다.

| 양 | z=20 | z=4 | z=2 |
|---|---:|---:|---:|
| Signed sqrt(2)S | 0 | -6.94101837e-5 | -5.93215462e-5 |
| Signed sqrt(2)Pm | +5.65685425e-4 | +3.22009447e-5 | +1.09304830e-5 |
| Signed sqrt(2)Pr | -5.65685425e-4 | -1.32987371e-4 | -7.51340430e-5 |
| Pi_total,F | approximately 0 | 1.00786426e-4 | 6.42035600e-5 |

z=2에서 initial memory는 0, matter memory는 +3.69770520e-5, radiation memory는 -9.62985969e-5다. 합계는 관측 signed shear와 1.26e-12 이내에서 맞는다. 두 stress가 처음 상쇄되었더라도 정규화와 sector 동역학이 다르므로 상쇄는 유지되지 않는다. 순간 상쇄율
\[
1-|P_m+P_r|/(|P_m|+|P_r|)
\]
은 약 1에서 0.25400670으로 변했다. 표본상 Sigma_F 최대는 6.95839e-5, z=4.34791893에서 나타난다. 이는 저장 표본 최대값이며 연속시간 극값의 인증이 아니다.

z=2의 Sigma_F 최대는 radiation lane 5.30426953e-4, matter lane 3.26570907e-4, mixed lane 3.49118398e-4다. 이 범위는 각 lane의 서로 다른 초기 parameter 집합에 대한 결과다. 동일 initial amplitude의 species-off 효능 순위로 해석하지 않는다.

그림은 figures/z20_z2의 01 separate stress time, 02 signed memory time, 03 signed endpoint slices, 04 full sweep heatmaps의 PNG와 PDF다. ENDPOINTS.csv에는 모든 case의 signed 값, norm, memory, closure residual이 있고 TIME_PACKET.npz에는 모든 97점 곡선이 있다.

## 7. 검증과 정확도 범위

Focused tests의 최종 서로 다른 테스트 수는 41개다: cumulative 13, interval 11, continuation fake-solver 10, saved-analysis 7. Manufactured pipeline와 독립 검토를 별도 근거로 남겼다. 동일 identity에 대한 반복 test를 새로운 검증 수로 세지 않았다. Saved-analysis 7개 test 이후에는 경계 비교 의미를 바로잡은 docstring 한 줄만 바뀌었다. 역패치 SHA256과 docstring 제외 AST의 동일성으로 최종 source에 대한 실행상 동등성을 확인했고, 최종 native-loader 독립 검토도 별도로 남겼다. 최종 hash로 7개 test를 새로 실행했다는 주장은 하지 않는다.

| 검토 | 실제 결과 |
|---|---:|
| 기존 PR128 endpoint 대비 최대 차이, signed half | 1.92988e-17 |
| 결합 z=2 endpoint closure residual 최대, F | 5.10760e-12 |
| tail local z=2 residual 최대, F | 1.05124e-12 |
| z=2까지 전파된 기존 residual 최대, F | 4.68611e-12 |
| 전체 저장 node closure residual 최대, F | 3.10755e-10 |
| stitch residual 항등식 결손 최대, F | 4.88201e-19 |
| Algebraic Einstein constraint 상대 오차 최대 | 4.30219e-16 |
| Radiation E0 work 적분의 sampled residual 최대 | 5.38666e-14 |

각 최대값은 서로 다른 case에 있을 수 있어 최대값들을 직접 더하는 등식은 성립하지 않는다. 이 값들은 saved-trajectory·floating-point·sampled-quadrature consistency의 지표다. 전역 ODE 오차나 continuum certificate로 승격하지 않는다.

독립 검토에서 새 tail 40,623점의 H>0, E0>0, sampled angular brightness>0, elapsed proper time 증가, |b| 범위, sector tensor와 Frobenius normalization, signed tensor합을 확인했다. 최소 sampled brightness=0.52158669, 최대 |b|=0.00171211이었다. 각도·시간 표본 사이 positivity를 이 검사로 인증하지 않는다. Evidence에는 원래 실패 fixture, 구현 수정 및 final scoped pass를 모두 보존한다.

## 8. 자원 공유와 실행 회계

HH74의 변경하지 않은 resources.LeasePool을 재사용했다. NCP 모드는 CPU upper cap64, RAM upper cap128GiB, reserve16GiB, 작업당 예약0.25GiB, BLAS/OpenMP thread1, 실제 affinity/cgroup/busy/available memory를 적용한다. 공유 lease 경로는 /tmp/rei-bianchi-cooperative-leases다. 같은 프로토콜을 쓰지 않는 다른 세션도 있을 수 있으므로 실제 busy/memory를 보수적으로 함께 고려한다. 남은 capacity만 admit하며 다른 process를 signal하거나 종료하지 않는다.

이번 실제 host는 visible9CPU, 약9.5GiB였고 local worker ceiling2, reserve2GiB로 계산했다. NCP 접속 경로의 Desktop Commander가 월간 사용량 한도로 요청을 거부하여 SSH 명령 자체가 실행되지 않았다. 이 한도는 전체 연구를 중지하는 이유로 사용하지 않았다. 작은 신규 tail만 로컬 자원으로 완료했다.

실제 전체 wall115.2286s, case CPU 합50.1820s, case wall 합54.5003s를 receipt에 기록했다. 검증·스케줄러·I/O를 포함한 전체 wall과 개별 case 시간 합은 다르다. 이 값은 비용 회계이며 가속배수 또는 benchmark 비교가 아니다. 이번 1,231개 tail의 pending은 0이므로 현재 NCP에 같은 queue를 다시 실행할 이유가 없다.

## 9. 게시·백업·DAG

실제 remote PR129 HEAD의 descendant branch research/hh-phys76-time-transport-20261021에 additive Draft PR130을 게시했다. 원래 source나 PR128/129 자료를 바꾸지 않고 새 PHYS76 subtree만 추가한다. S0 계약, S1 이론·구현, S2 과학 결과·그림, S3 최종 영수증을 구분한다. 각 R/C 단계와 근거·checkpoint의 대응은 RESEARCH_LOOP.json에, 게시와 저장의 실제 provider 응답은 delivery/에 기록한다.

기존 PHYS75 보충 ZIP의 Dropbox 실패는 이번에 별도 복구했다. 원래 Drive ZIP과 새 Dropbox 재다운로드가 952,307 bytes 및 SHA256 33cf1a493a3c5b54eea9871255606e658c0625eda8578872ec29b9d2075521c9로 정확히 일치한다. PR129의 과거 BLOCKED 기록을 고치지 않고 PHYS75_DROPBOX_RECOVERY.json을 추가했다. 이는 별도 PR128 FULL archive 전달 공백의 해결을 뜻하지 않는다.

최종 파일의 content identity와 remote commit, Drive/Dropbox ACK는 PHYS76_FINAL_DELIVERY_20261021.json을 기준으로 한다. Git에는 source·유도·검증·요약·그림 및 결과 index를 게시하고, case별 raw histories와 원본 upstream archive는 완전한 재개 packet에 보존한다. 자신의 SHA를 자신 내부에 넣는 순환을 피하기 위해 science commit과 후속 delivery metadata HEAD를 구분한다.

DAG에서 완료한 하위 노드는 all-node Simpson, 조건부 시간 response proof/implementation, 저장 종단상태 continuation, z20→2 preliminary plots, scoped verification이다. 다음 실제 의무는 whole-cell source/residual enclosure, angular truncation, full native cold EoR, non-LRS, HH matched xi/rate이며 각각 OPEN이다. 최신 REI199의 별도 D8 saved-history sign-reversal 분석과 ACCEL02 native moments는 해당 owner branch에서 재사용 검토한다. 완료한 sweep를 반복하는 작업을 다음 단계로 잡지 않는다.

## 참고와 재개

- PR128 과학 기준: https://github.com/cosmosapjw-quantum/WU088_HH/pull/128
- PR129 보충 기준: https://github.com/cosmosapjw-quantum/WU088_HH/pull/129
- 이번 Draft PR130: https://github.com/cosmosapjw-quantum/WU088_HH/pull/130
- SciPy1.17 cumulative Simpson: https://docs.scipy.org/doc/scipy-1.17.0/reference/generated/scipy.integrate.cumulative_simpson.html
- Python3.12 Decimal: https://docs.python.org/3.12/library/decimal.html
- Niesen–Wright, phi functions: https://arxiv.org/abs/0907.4631

Exa와 SciSpace는 문헌 후보를 탐색했고 채택 근거는 원 논문·공식 문서와 직접 유도다. Wolfram은 scalar phi·normalization 항등식 대조에 사용했으며, undefined-symbol/중간 zero-division 경고도 원문으로 남겼다. Symbolic residual0을 interval witness의 인증으로 사용하지 않는다.

복사 가능한 Codex 및 다음 대화 handoff는 각각 CODEX_HANDOFF_KO.md와 NEXT_THREAD_HANDOFF_KO.md에 있다. source/CONTINUATION_RUNNER_KO.md의 신규 run 명령은 원래 실행 기록이며, 이미 완료한 queue에 그대로 재실행하는 지시가 아니다.
