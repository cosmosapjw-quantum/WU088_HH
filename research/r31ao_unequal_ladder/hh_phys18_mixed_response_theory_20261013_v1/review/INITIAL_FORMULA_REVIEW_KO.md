# PHYS18 초기 식의 독립 검토

검토자: `/root/hh_phys18_mixed_review`. 대상은 PHYS17에서 고정한 `NEXT_MIXED_RESPONSE_PROPOSAL_KO.md`의 M1–M16과 `MIXED_RESPONSE_CONTRACT.json`이다. 새 코드·수치 결과가 나오기 전의 식 검토이며 최종 채택 상태는 별도 독립 심사에 기록한다.

## Mixed implicit forcing와 작은 차이

고정 α에서 (λ,b)를 각각 한 번 미분하면 JFWF=−B_F다. JyW+B_y=rλb와 Jy=JF+L를 대입하여

\[
J_FW_d=r_{\lambda b}-LW-(\mathcal B_y-\mathcal B_F).
\]

Hessian 부분은

\[
H_{gg,y}[U,V]-H_{gg,F}[U_F,V_F]
=\Delta H_{gg}[U,V]+H_{gg,F}[d_\lambda,V]+H_{gg,F}[U_F,d_b].
\]

같은 분해를 HgλV와 HgbU에 적용하면 M4의 모든 부호가 나온다. U/V를 바꿔 쓴 동치 분해도 가능하지만 한 식 안에서 선택을 섞지 않는다. Hλb=0은 두 전역 매개변수가 서로 독립이라는 사실만으로 충분하지 않으며, 원 gas-fixed source의 λ-affine·birth-linear 구조와 실제 Hessian[4][5]에서 확인해야 한다.

## HI 유리식

H의 photon 항은 −νQ(1−D⁻¹)이고 D=1+ℓ(1−x)다. Full incoming은 Q=RFZ₀+2bJ이므로 x에 두 번 미분하면 Hxx,ph=2νQℓ²D⁻³, x와 b를 미분하면 Hxb=2νJℓD⁻²다. DF=Dy+ℓdx를 대입하고 분모 차를 정리하면 M5와 M6의 양의 계수 및 dx 인자가 정확히 나온다. 여기서 ℓ=2ha2는 Full duration을 포함하고, 별도의 factor 2는 Full birth injection에서 온다.

## Stage 잔차

r_g=h(B₁(g₁)−B₂(g₂))의 혼합 미분은 M8이다. Bk=Fk+λqkνH−2Hkwew이므로 Bk의 explicit λ derivative는 qkνH이고 혼합 미분에는 Dqk Vk만 한 번 생긴다. M10은 U=U₁+sλ, V=V₁+sb를 대입한 bilinear identity다. M9와 M11은 gradient 값의 선분 차에만 Hessian을 사용하므로 C²에서 닫힌다. B₁,gg−B₂,gg는 실제 각 stage endpoint의 범위 차로 계산할 수 있다.

## 유한 온도

N=FP와 N=CT dw−T₂de를 각각 혼합 미분하면 M14가 나온다. PF,λb=le(W−Wd)를 마지막 항에 대입하면 Wd의 covector는 CTew−(T₂−F)le=CTew−TFle가 되므로 M15와 일치한다. M16은 T₂Π₂=CTw₂의 정확한 혼합 미분이다. 분모 ΠF,Π₂의 positivity는 원 root hull에 결박해야 한다. λ,b는 무차원이므로 출력 단위는 K/(unit λ unit b)다.

## 검토할 수치 의무

원 35 photon/guard mixed Jets와 W₁,W₂,WF가 ordinary partial λb라는 slot 의미, exact-float scalar 해석, 공통 C,B,q,S, 모든 외측 포함의 유효성과 교집합, final temperature 계수 및 I의 전역 양화가 새 application 심사 대상이다. 원 C² Hessian 범위만으로 Hessian-Lipschitz modulus를 부여하지 않는다. 식 M1–M16의 초기 검토에는 현재 blocking finding이 없다.
