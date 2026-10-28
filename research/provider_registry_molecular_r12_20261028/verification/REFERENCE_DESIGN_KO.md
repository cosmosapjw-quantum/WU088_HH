# R12 독립 reference — 비정렬 forcing convolution

## 범위와 독립성

이 문서는 `WU_NONALIGNED_CONVOLUTION_R12` 계약의 새 R5/R7 및 C7/C8 의무를 위한 독립 구성이다. production의 overlap loop, interval helper, 선행 Python module을 import하거나 복사하지 않는다. 기존 R11 PRIMARY_RESULTS의 고정 bytes에서 chosen rational q·tau·초기값·계수·binding·닫힌 cap을 읽고 새 비정렬 관측 문제에 필요한 계산만 수행한다. 새 generator/ODE/native/CAS 계산과 닫힌 옛 campaign 재실행은0이다. 실행은 root의 동결·게시 뒤1회 gate에만 허용된다.

적용한 skill_context_used는 `physmath-research-loop 1.3.0`의 SKILL, `references/POLICY_INTEGRATION.md`, `references/SUBAGENT_MODE.md`, THEORY_LOOP R5(실제 유도)/R7(허용된 판별 검증), CODING_LOOP C7(의도한 물리·source history 대응)/C8(수치·재현성)다. 실제 native delegation으로 할당된 constructor이며 추가 child나 review-of-review를 만들지 않는다. 기존 skill1.0으로 닫은 source를 다시 쓰지 않는다.

## 정확한 primitive와 event grid

각 start·전체 family에 유효한 block certificate의 실제 chosen rational `q∈[0,1]`, `tau>0`를 그대로 쓴다. `h(u)=q^floor(u/tau)`, `h(0)=1`, `0^0=1`이다. `x=max(v,0)`, `n=floor(x/tau)`에 대해

\[
J(v)=\int_0^{\max(v,0)}h(u)\,du
=\tau\sum_{k=0}^{n-1}q^k+q^n(x-n\tau).
\]

Reference는 유한합을 직접 구성한다. 따라서 q=0에서는 `J(v)=min(max(v,0),tau)`, q=1에서는 `J(v)=max(v,0)`가 별도 극한 추정 없이 성립한다. source cell `[a_j,a_{j+1}]`의 정확한 forcing 기여는

\[
F_j(t)=g_{r,j}\{J(t-a_j)-J(t-a_{j+1})\}.
\]

이는 production의 양의 overlap 길이 합과 독립인 적분 primitive 표현이다. `F(t)=ΣF_j(t)`, `R(t)=h(t-t0)R0+F(t)`를 Fraction으로 평가한다. source cell 끝점의 measure-zero 중복은 적분을 바꾸지 않는다. 새 forcing의 age0은 항상 h0=1이고 source history를 cell마다 reset하지 않는다.

독립 event 집합은 관측 knot·source knot·초기 block jump `t0+k*tau`·모든 source knot의 양의 shift `a_j+k*tau`·실제 old cap knot의 합집합이다. 정확한 유리수 비교로 [t0,T] 밖을 제거하고 중복을 합친다. event 사이에서 F는 affine이고 h는 일정하다. segment `[l,r]`에서

\[
L=q^{\lfloor(l-t0)/\tau\rfloor}R0+F(l),\quad
V=q^{\lfloor(l-t0)/\tau\rfloor}R0+F(r)
\]

이며 V는 r의 왼쪽 극한이다. `R(r)`는 block jump에서 별도 point value를 갖는다. 닫힌 segment의 정확한 R 상계는 `max(L,V,R(r))`이고, 요청된 닫힌 cell은 gap-free refined segments의 max로 집계한다. source-cell index, old-cap containment 및 point equality를 독립 검색하여 production index metadata도 확인한다.

## Decimal160의 signed scalar 적분

`R(l+u)=L+βu`, `β=(V-L)/Δ`와 상수 ge에 대해

\[
E(l+Δ)=e^{dΔ}E(l)+(cL+g_e)\phi_1(d,Δ)+cβ\phi_2(d,Δ),
\]

\[
\phi_1=(e^{dΔ}-1)/d,\qquad
\phi_2=(e^{dΔ}-1-dΔ)/d^2.
\]

정확히 d=0이면 `phi1=Δ, phi2=Δ²/2`다. 이 식은 Decimal160의 `exp`와 닫힌식으로 평가한다. production의 Taylor96/Bernstein 양의 급수와 계산 경로가 다르다. 양·음 d 및 ±1e-30 control을 포함하며 near-zero cancellation을 이유로 tolerance나 정밀도를 실행 후 바꾸지 않는다.

닫힌 cell E는 동일 initial E에서 R를 위의 정확한 상수 Rmax로 바꾼 scalar 상해를 이용한다. 상수 forcing `B=cRmax+ge`의 해는 `Y(u)=exp(du)E(l)+B phi1(d,u)`이고 도함수는 `exp(du)(dE(l)+B)`이므로 구간에서 단조이다. 따라서 `max(E(l),Y(Δ))`가 전체 닫힌 cell의 충분한 상계다. 이 참고 상계와 출력 whole upper를 비교하며 원래 affine 해의 구간 안 표본 확인이 보조될 경우 diagnostic으로만 표시한다.

Decimal check는 실행 전 고정한 `1e-80*max(1,abs(reference),abs(lower),abs(upper))` guard를 쓴다. Decimal160 결과는 corroboration이며 엄밀한 interval reference를 주장하지 않는다. Fraction F/R/격자/cap/순서 비교에는 수치 guard가 없다. 원래 sample atol2e-12/rtol2e-10과 strict=false 기록은 바꾸지 않고 sample campaign도 다시 실행하지 않는다.

## Cap과 aligned reduction

R11 cap은 SHA-256 `80ed0f8df5c785e47ce737acb8b029485db54b543d57498bf182427093f29b1b`,2,058,347 bytes의 PRIMARY_RESULTS에서만 읽는다. saved case는 동일 initial/source family/state/clock과 원래 exact0..192delta horizon을 유지한다. source gr/ge를 한 cell로 줄이는 경우 모든 원래192개 값의 exact equality를 확인한다.

각 refined segment가 포함되는 old **closed** cell을 독립 확인한다. old point cap은 exact rational point equality일 때만 쓴다. refined cell이 old 경계를 넘거나 old index가 임의로 선택되면 실패다. Rcap은 exact raw whole R와 old whole Rupper의 min으로 독립 구성한다. Ecap은 이 상수 Rcap과 동일 ge를 사용한 단조 비교 recurrence와 실제 point/whole cap의 min으로 구성한 ideal lower target을 비교한다. 이는 외향 upper 구현의 충분한 하한 target이며 실제 물리 오차 lower가 아니다. 별도로 모든 실제 capped 출력이 해당 old point/whole cap보다 크지 않은지 exact Fraction으로 검사한다. 관측 cell이 여러 old cells에 걸치면 그 gap-free cover의 최대 cap과 비교한다.

원래 aligned 관측점에서는 새 primitive F/R가 immutable R11의 저장 interval에도 포함되는지 확인한다. Raw E의 같은 ideal 함수도 양쪽 저장 enclosure에서 확인한다. 외향 연산 횟수나 표기 차이 때문에 무조건 byte/numeric identity를 요구하지 않는다. 비정렬 관측 refinement에서 공통 knot의 ideal F/R/E가 유지되는지 비교한다. old source 코드·행렬지수·ODE·reference runner를 다시 돌리는 절차가 아니다.

## 실행과 보고

runner는 인자 없이 root가 실행한다. `raw/PREEXECUTION_FREEZE.json`의 PASS와 모든 frozen file bytes/SHA를 확인하고, 아직 prefreeze에 존재하지 않은 실제 PRIMARY_RESULTS의 digest를 read-only로 별도 기록한다. 자기 output `raw/REFERENCE_RESULTS.json`이 있으면 덮어쓰지 않고 종료한다. 모든 check/group/component 수는 실제 관측에서 집계하며 예상 총수를 꾸미지 않는다. 정확 비교, Decimal corroboration, source/cap coverage, metadata identity를 분리해 counts와 첫 실패를 저장한다.

완료 판정은 root가 맡는다. reference 자체는 한 번의 finite construction/verification lane이며 source/proof 검토를 반복시키거나 실제 HD 물리 closure·보편적 개선을 주장하지 않는다.
