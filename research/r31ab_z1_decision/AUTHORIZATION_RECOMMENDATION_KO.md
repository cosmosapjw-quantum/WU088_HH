# R31AB authorization recommendation closeout

기준 remote는 `2ebdd94325b54125d95578860fd16042c3fea514`, tree `892e702b3460070c61887b85a9fd3a373da43a9c`이다. R31AB NCP preflight는 focused 3/3 PASS, compile/replay exit 0, prereg/model/rule hashes unchanged, science-node count 0으로 종료했고 `Z1_EXECUTION_STATUS=AWAITING_EXPLICIT_AUTHORIZATION`을 유지했다.

## 연구 판정

과학적 권고는

`RECOMMEND_AUTHORIZE_MINIMAL_Z1_MIXED_NODE`

이다.

이 권고는 어느 interpolation model이 더 낫다고 예측하는 것이 아니다. z=1 direct truth를 읽기 전에 이미 frozen된 R31Z global과 R31AA local의 primary prediction separation이 충분히 커서, 단 한 번의 최소 direct node가 높은 판별력을 갖는다는 뜻이다.

z=1에서 두 frozen model의 차이는

- `||ΔK_model||_2 = 0.2165779475378074 / t_a`
- `ΔDmax_model = 0.21927766897126583 / t_a`
- `||ΔO_model||_2 = 0.12604400117383283`
- `||ΔdotO_model||_2 = 0.009480380748858165 / t_a`.

어떤 direct truth X에 대해서도 triangle inequality

[
||G-L|| le ||G-X||+||L-X||
]

가 성립하므로 적어도 한 모델은 반드시

[
E_K ge 0.1082889737689037/t_a,
]

[
E_{D,max}ge0.10963883448563291/t_a
]

의 오차를 갖는다. Preregistered comparison tolerance (10^{-10})에 비해 primary separation은 약 (2.17	imes10^9), (2.19	imes10^9) 배다.

따라서 z=1은 현재 두 frozen candidate를 구별하는 목적에는 매우 높은 information value를 갖는다. 이 결론은 source-error probability model이나 어느 candidate의 승률을 가정하지 않는다.

## provenance / validation 의미

z=3은 R31Z에게는 withheld point였지만 R31AA form은 z=3 failure를 본 뒤 설계되었다. 따라서 z=3은 R31AA의 tuning/post-hoc evidence이며 independent confirmation으로 재사용하지 않는다.

z=1 preregistration은 z=1 direct output access 전에 model source, metrics, tolerance, Pareto rule을 hash-lock했다. Parent CP4 inventory에서 equivalent z=1 mixed direct node는 발견되지 않았다. 이 조건이 실행 전까지 유지될 때만 z=1을 R31AA의 첫 independent validation으로 취급한다.

문헌적으로도 exploratory/tuning sample과 holdout validation을 분리하고, expensive validation에서 model response를 강하게 구별하거나 QoI에 relevant한 point를 선택하는 것이 합리적이라는 방법론적 배경이 있다. 이 문헌은 WU088_HH의 수치 정확성을 대신 증명하지 않는다.

## 승인 범위

승인할 경우 정확히 한 node만 실행한다.

- z = 1.0 a0
- tau = 2.2358772390338113 t_a
- B192
- mixed O 47x2
- mixed D_col 47x2
- mixed D_row 2x47
- independent mixed dotO 47x2

금지:

- H
- neutral47
- ionic2
- full49
- trajectory
- 다른 z node
- M3/reference preparation
- model retuning before comparison

z=1 direct output을 읽은 직후 preregistered `E_K`, `E_Dmax` Pareto rule로 한 번만 판정하고 종료한다.

## 실행 권한

이 파일은 권고다. 실행 권한 자체는 여전히 false다.

`execution_authorized=false`

상위 지시에서 exact token

`AUTHORIZE_Z1_MINIMAL_MIXED_NODE`

이 확인될 때만 science node를 실행한다. Token이 없으면 preflight/return만 수행한다.

## claim ceiling

z=1 한 점의 결과는 다음을 자동 승인하지 않는다.

- interval-wide accuracy
- transition-amplitude/error bound
- HH trajectory
- full-cell admission
- H-skip
- production
- complete-HH invariant-sector physical adequacy

Fixed Q는 represented-model definition으로 확립되어 `dotQ=0`이지만 complete HH dynamics에서의 physical invariance는 별도 gate다.
