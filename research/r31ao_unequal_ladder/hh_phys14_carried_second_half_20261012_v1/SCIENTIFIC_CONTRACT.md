# PHYS14 — 등방 배경에서의 공동 carry와 두 번째 half 단계

## 목적과 완료 기준

PHYS13의 첫 단계 온도·전자 응답을 실제 두 번째 half implicit 단계로 전달한다. 기존 PHYS11의 joint chain rule, PHYS09의 U/V/W, PHYS13의 root image를 재사용하고, 현재 등방 배경의 정확한 group closure와 새 incoming photon/source를 구성한다. 종료 조건은 (1) 원 ray/guard payload의 identity 확보, (2) 등방 geometric subfamily와 원 source 포함의 연결, (3) 새 단계의 root self-map/contraction 및 일차·혼합 응답의 검증된 포함, (4) 온도·전자 관측량 및 원 격자의 spectral remap 분할 효과, (5) 독립 판정·실제 실행 증거·DAG·보고서·게시·이중백업이다. 새로운 근 포함이 실패하면 첫 실패를 보존하고 같은 모델 안에서 필요한 계산을 수정한다.

## 고정한 물리·수학

- 출발 시각 t0=1.6e11 s, h1=h2=6.25e8 s, Hubble triplet의 세 captured binary64 값은 1e-14 /s로 같다. 종료 시각은 기존 Full의 t0+1.25e9 s다.
- 같은 COMMON과 과거 HH ON·primal compensation을 유지한다. 전역 미래 파라미터 lambda,b 각각 [0,1]는 두 단계 모두에 적용한다.
- 첫 단계는 PHYS09/11/13의 같은 고정 계수 계열에서 재사용한다. 원 등방 geometry에 대해 r=exp(-exact(H)*exact(h))와 정규화 source weights의 합=1을 사용하는 geometric subfamily를 선택하고, 원 exported enclosures와의 포함 관계를 기록한다. 원 독립 ray-coefficient enclosure 전체와 이 선택을 구별한다.
- 좌표 g=(x_HII,y_HeII,y_HeIII,w), w [eV/H], photon group N [photons/H], guard number/energy [photons/H,eV/H]. metric (-,+,+,+); c,k_B,epsilon_eV의 captured leaves를 유지한다.
- 두 번째 stage의 nH/nHe/fHe/Hmean, energy/sigma/heat/kB/eV leaves는 기존 Full의 endpoint와 동일하다. nonphoto와 q의 whole-X 및 centre source Jets를 재사용하고, dt와 photon incoming은 새 half 값을 사용한다.
- 원 33 energy nodes 및 piecewise linear hat remap을 유지한다. H active sigma만 17개, helium photo sigma는 전부 정확한 0인지 실제 bits로 확인한다.
- source-aligned T=C_T*w/(1+fhat+e), fhat=exact(nHe_stored)/exact(nH), e=x+fhat*(y1+2*y2). stage f와 fhat는 구별한다.

## 계산형과 수치 계약

원 정확한 유리수 및 binary64 bit endpoints를 읽는다. 새 구간 연산은 Python Fraction에서 계산한 뒤 256 significant binary bits의 dyadic endpoints로 바깥쪽 반올림한다. 지수 범위는 제한하지 않아 저장된 작은 signed tails를 포함한다. 이 반올림 자체의 포함과 부호·zero divisor·혼합 quotient를 작은 독립 유리수 사례로 검사한다. 변경된 source physical coefficients, baseline tolerances 또는 native precision은 없다.

등방 transport와 guard 합은 선형 map으로 값/U/V/W 각각에 작용한다. 다음 absorption은 K_j=a_j(1-x)/(1+h*a_j(1-x)), a_j=c*nH*sigma_j, Fphoto=sum K_j*N_j를 사용한다. 기존 nonphoto/q full-X 도함수와 source centre를 이용한 Taylor 포함을 교차해 root image를 계산한다. Root self-map은 원 X 안에서, contraction은 component-scaled infinity norm으로 판정한다. 새 U,V,W는 4x4 Neumann series와 명시적 tail로 포함하고 유한 반응은 동일 계열의 FTC로 전달한다.

## 검증과 실행 예산

- 실제 과학 구성: 이어진 half+half 한 history family. 재사용된 두 별도 첫 stage는 새 실행 수에 더하지 않는다.
- 필요한 검증: 원 입력 identity, 공통 r의 원 ray interval 포함, branch-stable remap/number-energy identities, scalar closed-form implicit sensitivity 및 mixed carry oracle, directed interval rounding, root image/margins/contraction, linear tail, T/e signs.
- Owner 경량 실행 예산: 한 실행 wall/CPU 90 s, address space 768 MiB, 파일당 32 MiB. 수정이 필요한 경우 근거가 바뀐 관련 실행만 수행하고 원 실행을 보존한다. Heavy/native kernel, 기존 과학 suite 재실행, NCP launch는 계획하지 않는다.
- 기존 PHYS09/11 source derivative inclusion과 첫 stage C2/root premise는 상속한다. 새 stage root/derivative 포함은 이번 계산의 별도 증거로 남긴다. 실행 비용·과학 정확도·native authority·전역 적용은 각각 기록한다.

## 권한·근거·판정

현재 사용자의 다음 연구 루프 지시와 2026-09-28의 기존 Git/Drive/Dropbox 읽기·쓰기·다운로드·업로드 승인을 따른다. additive 연구 브랜치/PR과 create-only 이중백업으로 전달한다. 원 native/reference·basis·prior successful artifacts를 유지한다. 최종 PROMOTE 판정은 후보 생성·검증 설계에 관여하지 않은 독립 reviewer에게 맡긴다.

