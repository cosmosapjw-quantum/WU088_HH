# WU088_HH PHYS10 — 기체·잔존 광자의 유한 혼합 에너지 수지

## 결과와 근거 상태

**같은 고정 소스 계열에서 HH와 미래 광자 birth의 결합은 기체 에너지의 가산 예측을 낮추고, 잔존 광자 에너지의 가산 예측을 높인다. 두 유한 혼합량의 크기는 Full에서 0.156%, first_half에서 0.078% 이내로 보상된다.** 기체와 광자의 합에 대한 포함 구간은 0을 포함하므로 그 합의 부호나 정확한 0을 채택하지 않는다.

근거 상태는 derived / numerically checked / implementation-verified (새 Python rational postprocessor)이며, 원 NCP07 source inclusion과 C² chart 및 PHYS09의 같은 root-family 증거를 상속한다. 최종 독립 scoped 채택은 `review/DECISION.json`을 따른다. 이번 결과를 actual native root 또는 전체 수송 계의 에너지 보존으로 승격하지 않는다.

## 1. 실제 최신 상태와 이번 질문

NCP08 PR41 head `5288fd50148755f5ed37391e3dcb612d8d51f130`와 NCP09 PR42 head `e6a72c3df5803b5b23f9a38918dad6a1eba7e1f7`에서 실제 완료 반환을 확인했다. NCP09의 50/50 exact-oracle 전체 포함과 12,594개 원 endpoint 대응은 기존 비생성 검토를 재사용한다. 이번 intake는 35개 작은 text 파일의 실제 Git blob/크기와 기존 입력 23개의 전후 binding을 확인했다. 완료 compiler/gate/consumer를 다시 실행하지 않았다.

PHYS09는 gas finite interaction I_e<0를 얻었다. PHYS10은 이 음의 gas interaction이 같은 흡수 단계의 잔존 광자 에너지와 어떤 수지를 이루는지 새로 계산한다. U,V,W와 gas interval을 다시 풀지 않고 저장된 정확 구간을 입력으로 삼는다.

이 논의에서 HH는 이미 고정한 source의 세기 lambda이고, b는 미래 광자 birth의 세기다. 과거 COMMON history는 모든 corner에서 동일하게 유지한다. 기존 2전자 frozen107 atomic-pair wave는 별도 계산 lane으로 남긴다.

## 2. 정의·단위·고정 계열

g=(x_HII,y_HeII,y_HeIII,w), w의 단위는 eV/H다. theta=(lambda,b)는 [0,1]^2다. full의 d=1.25e9 s, first_half의 d=6.25e8 s이며 둘 다 동일 COMMON에서 시작하는 독립 first-stage다. First_half가 완료된 full 또는 다른 half를 이어받는다는 가정을 넣지 않았다.

각 admitted coefficient tuple alpha를 rectangle 전체에서 고정한다. Corner마다 다른 interval coefficient를 택하지 않는다. 이 underlying real-source family는 captured leaves를 실수로 올린 source이며, 반올림된 실행 프로그램을 C²라고 가정하지 않는다.

원 photon packet은 photons/H이며 E_j는 eV다. 따라서 e_gamma=sum_j E_j N_j는 eV/H다. kappa_ja=c*n_H*l_a*sigma_ja의 단위는 s^-1, R_ja=kappa_ja*N_j의 단위는 H당 초당 반응 수다. e_gamma에 n_H를 추가로 나누지 않는다. 기체 에너지는 e=ell*g, ell=(chi_H,f*chi_HeI,f*(chi_HeI+chi_HeII),1)이다. Stage f와 stored n_He/n_H의 차이를 유지하며 nonphoto의 직접 ell projection에 이미 들어 있는 Jnorm을 중복 추가하지 않는다.

기체 또는 광자 관측량 Q의 유한 혼합량은 I_Q=Q(1,1)-Q(1,0)-Q(0,1)+Q(0,0)이다. 이는 두 작용의 가산 예측에 대한 departure이며 절대 energy gain 또는 흡수 효율과 다르다.

## 3. 광자 제거 항등식과 총 수지

실제 `phys04_reduced_residual`에서

\[
N_j=\frac{\bar N_j+bM_j}{D_j},\qquad
D_j=1+d\sum_a\kappa_{ja}(g)>0,\qquad R_{ja}=\kappa_{ja}N_j.
\]

따라서 모든 같은 source 계열에서

\[
d\sum_aR_{ja}=N_j^{in}-N_j.
\]

PreBE 뒤의 N_j^{in}은 b에 affine이고 lambda와 gas에 독립이다. 혼합 미분에서 incoming 항은 정확히 사라진다. 저장 `photons`에 full photon Jets가 있다고 가정하지 않는다. 실제 존재하는 모든 33×3 rate full Jets를 위 항등식으로 소비한다.

U=g_lambda, V=g_b, W=g_lambdab에 대해

\[
\mathscr L[J]=J_gW+J_{gg}[U,V]+J_{g\lambda}V+J_{gb}U+J_{\lambda b}.
\]

에너지 weighted absorption A=sum_(j,a) E_j R_ja를 쓰면

\[
W_\gamma=-d\mathscr L[A].
\]

원 captured heat를 node energy로 바꾸지 않고 epsilon_ja=exact(heat_ja)+exact(chi_a)-exact(E_j)를 계산한다. Psi=sum epsilon_ja R_ja를 두면 PHYS09의 동일 chi_H HH 상쇄와 광자 항등식에서

\[
B=\ell F^{np}-2H_{mean}w+\Psi,\qquad
\boxed{W_e+W_\gamma=d\mathscr L[B].}
\]

W_e와 W_gamma를 서로 독립인 interval로 합치는 것보다 B를 먼저 구성한 뒤 다섯 chain-rule 항을 계산하면 dependency loss가 작다. 두 표현의 구간을 모두 보존한다. Source 식에 lambda 관련 미분이 정확히 없는 부분에서도 저장된 signed numerical tail은 합산에서 제외하지 않았다.

같은 C² root branch 위의 단위 사각형 FTC로 I_Q=int_0^1 int_0^1 W_Q db dlambda가 성립한다. 따라서 위 uniform mixed 구간이 각각의 유한 interaction도 포함한다. 네 corner root의 직접 계산이나 작은 두 차이의 뺄셈을 실행하지 않았다.

## 4. 실제 새 포함 결과

아래 값은 exact rational endpoint를 binary64로 바깥쪽 표시한 것이다. 완전한 분자/분모는 `results/ledger_first/LEDGER_RESULTS.json`에 있다.

| 양 | full | 같은 COMMON first_half |
|---|---:|---:|
| I_e, eV/H (PHYS09 재사용) | [-6.1928529567274838e-16, -2.0123549987008769e-16] | [-7.7596982749949402e-17, -2.5357316013204017e-17] |
| I_gamma, eV/H | [2.0147819024003132e-16, 6.1906859651508663e-16] | [2.5372573637033666e-17, 7.7583415794417712e-17] |
| I_e+I_gamma 직접 구간 합, eV/H | [-4.1780710543271699e-16, 4.1783309664499889e-16] | [-5.2224409112915727e-17, 5.2226099781213692e-17] |
| 먼저 합친 source의 I_e+I_gamma, eV/H | [-3.1314477547412323e-19, 2.4467453520579934e-19] | [-1.9605021839988345e-20, 1.5319948343632613e-20] |
| I_gamma/(-I_e) | [9.9844388899733749e-01, 1.0012158616912215e+00] | [9.9922684948873208e-01, 1.0006041628512914e+00] |

I_gamma는 두 stage 모두 엄격히 양수다. I_e+I_gamma는 두 stage 모두 ZERO_CONTAINING이다. Exact zero나 상쇄 후 잔여 부호가 증명됐다고 쓰지 않는다.

같은 계열에 대해 I_gamma/(-I_e)=1+(I_e+I_gamma)/(-I_e)이므로, 음의 gas margin을 사용하는 bound는

\[
\left|\frac{I_\gamma}{-I_e}-1\right|
\le \eta=\frac{\max|[I_e+I_\gamma]|}{-[I_e]_{hi}}.
\]

Full eta≤0.0015561110026624584, first_half eta≤0.0007731505112678191이다. 이는 각각 0.15561110026624584%, 0.07731505112678191%다. 이 비율은 source-family mixed ledger의 잔여 크기 상계이며 계산 오차 추정, 신뢰수준 또는 시간 이산화 수렴률이 아니다.

## 5. 남는 에너지 항의 해석

| B의 분해에 대응하는 유한 interaction, eV/H | full | first_half |
|---|---:|---:|
| Nonphoto | [-2.7874174115845231e-19, 2.7907756952147026e-19] | [-1.7451970205780317e-20, 1.7472999977840642e-20] |
| Expansion | [-3.4403034315670928e-20, -1.0578055231115218e-20] | [-2.1530516342080285e-21, -6.6257658924165930e-22] |
| Captured heat correction Psi | [-4.9406564584124654e-324, 4.9406564584124654e-324] | [-4.9406564584124654e-324, 4.9406564584124654e-324] |

개별 분해의 interval 상·하한을 더한 값은 먼저 합친 B의 interval보다 넓을 수 있다. 이 표는 source별 기여의 포함이며 모든 극값이 같은 상태에서 동시에 달성된다는 뜻이 아니다.

99개 epsilon 중 19개는 exact rational로 0이 아니고 모두 HeII absorber 열에 있다. 그러나 이것만으로 실제 Psi 또는 그 유한 mixed interaction이 0이 아니라고 결론내릴 수 없다. Psi mixed interval은 0을 포함한다. 표시된 ±5e-324는 정확한 유리수 구간을 바깥쪽 최소 subnormal로 표시한 값이며, 원 데이터나 합산을 0으로 clip한 결과가 아니다.

기체의 음의 혼합량과 잔존 광자의 양의 혼합량이 거의 서로 보상된다는 해석은 이 local absorption stage에서 성립한다. HH가 neutral substrate를 줄이는 같은 source 방향과 정합한다. 이 e_gamma는 PreBE 이후 남는 광자량이며, escape/guard/redshift 전체 ledger를 모두 더한 우주론적 총에너지가 아니다. Nonphoto 원자 과정과 expansion이 남고 Psi는 captured source representation correction이다. Gas+photon exact global conservation이나 새로운 physical energy injection을 주장하지 않는다.

## 6. 실제 실행·재현성·실패 보존

새 실행은 `ledger_first` 한 번이며 exit0, elapsed 0.7208253940043505 s, 최대 RSS 23924 KiB다. 45s wall/CPU,384MiB address-space,각 output16MiB 예산 안에서 끝났고 19개 binding이 전후 동일하다. 최초 실패·수정 재실행은 없으며 stderr는 비어 있다.

35개 assertion과 7개 의미 사례를 구분한다. 사례는 광자 제거의 exact number identity, 닫힌식 finite photon FTC, 다섯 항 모두 비영인 observable chain rule, 비영 heat capture defect, signed subnormal, early projection의 dependency 보존, 잘못된 exact/divisor/intersection/tangent 입력 거절이다. 각 stage에서 99 rate+4 nonphoto full Jets의 5,871개 원 value/gradient/Hessian interval을 소비했다.

PHYS09 exact U/V/W를 입력으로 재사용했고 inverse/Banach/root를 재계산하지 않았다. Source callback, native endpoint/root, IVP, 과거 suite, 새로운 compiler/build는 모두 0이다. 새 Python 함수는 기존 exact interval primitive와 원 source Jets를 공유하므로 독립적인 원 물리 모델 재검증이라고 부르지 않는다. 실제 비생성 검토가 유도·source binding·구간 표현·실행 증거를 확인한다.

## 7. NCP64코어·128GiB 분담

현재 완료된 NCP08 build/gate/consumer는 각각 1.421573/0.004197/0.667820초였고 NCP09는 0.766846/0.062807/0.083373초였다. 이 숫자는 원 실행 호스트의 관측값이며 64코어 성능 시험이 아니다. 이번 PHYS10 새 계산도 여기서 1초 이내에 끝났다. 따라서 `NCP_TASKS.json`의 active heavy_queue는 비어 있고 launch=false다.

현재 33×128 photon 구조와 공통 4D gas solve를 복제하거나 시간 구간을 독립 shard로 잘라 코어를 채우지 않는다. 실제 긴 campaign이 준비되면 독립된 물리 family의 전체 history를 worker별로 배정하고 그 family 내부 carry는 순차로 유지한다. 64코어·128GiB는 실제 가용 CPU/memory 관측으로 제한할 자원 상한이며 속도비 보장이 아니다.

다음 연구 의무는 joint gas/photon/guard/ledger 및 U,V,W carry, 실제 다음 stage source coverage, normalized history/source/closure와 native-family 연결이다. 이 입력과 독립 task 집합, 첫 미완료 대표 task의 실제 비용이 준비될 때 새 중량 계약을 연다. 완료 실행을 성능 측정 명목으로 반복하지 않는다. `EXECUTION_ROUTING_KO.md`, `NEXT_DAG.json`, handoff에 이 순서를 구체화했다.

## 8. Claim ceiling

Native actual root/U/V/W/I는 null이고 native_authority=false다. 이번 photon observable도 수학적 source-family 결과다. Carried second_half, full/two-half paired defect, time/continuum remainder, full49/production은 OPEN이다. 과거 PHYS07 reference energy와 NCP07 node32 per-node OPEN을 소급 수정하지 않는다. PHYS08 minsubnormal_signed의 binary64 unresolved도 보존한다.

실제 Git commit/tree와 양쪽 backup ACK·metadata는 별도 START/receipt/index로 기록한다. Local archive bytes 검증, remote upload 확인, remote download restore를 구별한다. 압축본에는 본 연구와 입력·코드·이전 완료 증거가 들어가며 별도 사용자 첨부가 필요 없다.
