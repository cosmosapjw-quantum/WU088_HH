# PHYS72 재개 기준

이 회차는 원래 exterior 문제의 실제 outgoing Coulomb Green 가중 상한,
original screen norm, lambda=1 수렴 및 4차 이상 Born remainder를 닫았다.
`REPORT_KO.md`, `CONTRACT.json`, `NEXT_DAG.json`과 최종 외부
`PHYS72_DELIVERY_20261020.json`을 먼저 읽는다. Git 최종 HEAD와 provider
ACK는 외부 DELIVERY 및 `publication/` 기록으로 확인한다.

## 고정 결과

- `q=553311/10^26=5.53311e-21 < 1`.
- `(21,20),m0`의 order>=4 upper `<1.50654e-80 a0^-1`.
- 같은 PHYS71 D3 중심은 `(Z1-Z0)-exactD1-exactD2`를 radius
  `<7.271949342749e-79 a0^-1`로 포함한다.
- 정확한 결정은 `implementation/bounds.py`의 Fraction을 사용한다.
  native output은 rounded cross-check다.

## 재사용해야 하는 완료 근거

PHYS63 존재, PHYS69 D2, PHYS71 R1–R10/C1–C10과 D3는 완료다.
PHYS71 frozen M/PENDING은 외부 DELIVERY가 이미 닫았다. 기존 76 패널 및
152 profile의 재적분과 완료 게시를 재시작하지 않는다. 새 proof의 무한-j
상한은 shifted multiplier로 얻었고, H_C의 growing C_j도 그대로 남아 있다.
finite-L Gamma64를 무한-j 상수로 바꾸지 않는다.

`FROZEN_U_SUBSET.npz` SHA:
`f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`.
Corrected D3 certificate SHA:
`f75d082e1966dd61a326c37b6ff14e8f330e010341a59a88eb4ca8d4734e6173`.

## NCP

`ncp_delivery/README_KO.md`에는 준비된 exact Python 및 Fortran 실행 명령이
있다. 이론·코드는 여기서 완성했고 기본 Fortran compile/run도 실제 성공했다.
NCP는 선택적 재현의 compile, 작은 환경 경로 조정, 실행·회수만 수행하면 된다.
새 physical campaign은 이 결과의 승인 조건이 아니다. 실제 NCP 제출 수는 0.

## 다음 과학 의무

새 exterior inverse를 활용해 원래 source-driven `xi`와 interior/origin,
incoming-adjoint matching을 별도 범위로 연구한다. `eta=Fy`, `xi=Fy-phi`,
`eta_C=-10/7`을 구분하고 원래 Hamiltonian, B27,k7/10,E49/200을 유지한다.
`sigma(E)`와 `k_HH(T)`로의 전이는 그 의무가 닫힌 뒤에 수행한다.
`HH_R10=OFF`.

VigilODE PR77/78은 reflecting-grid 모형이다. residual inverse 구조를
재사용할 때에도 `theory/THEOREM_AND_MODEL_MAP.md`의 실제 HH 대응을 먼저
적용한다. 충분조건 실패는 strong no-go가 아니다.

## 복원 범위

SOURCE_AND_EVIDENCE와 RECOVERY ZIP은 source/evidence capsule이다.
전체 Git clone으로 취급하지 않는다. Git history가 필요하면 실제 branch를
clone/fetch하고 외부 DELIVERY의 최종 HEAD와 대조한다. 이 전달물에는 Git
bundle이나 additive patch를 포함하지 않는다. 증거 capsule의 명시된 subtree만
복원해도 새 exact scalar certificate와 포함원은 재현할 수 있다.

121-file science source commit은 `f26fa5a6e9fcb4428d6467cb762c852fa49daa6f`,
science tree는 `b22ac13ca38d5bdbf1aa96cecc74e04c7f9e2e02`다. 후속 metadata
commit과 외부 DELIVERY는 게시·백업·clean restore 결과 및 실행 안내만 닫는다.
Science capsule과 최종 metadata HEAD의 identity를 서로 바꾸어 사용하지 않는다.
원래 checkout 경로가 사라진 뒤 pinned remote blob과 대조하여 121개 파일을
복원했으며, 원인 미확인 및 native binary 부재도 publication 기록에 명시했다.
