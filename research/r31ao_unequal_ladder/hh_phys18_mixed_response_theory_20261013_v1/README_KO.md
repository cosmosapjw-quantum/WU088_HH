# WU088_HH PHYS18 — HH·birth 혼합 응답

## 현재 결과

독립 심사와 root 채택은 **PROMOTE_SCOPED**다. 같은 COMMON, 고정 admissible α,
전역 λ,b∈[0,1]², 원 source-aligned geometric-isotropic C² family에서
F=ΔT=T₂−T_F의 보통 혼합 편미분을 계산했다.

**F_{λb}와 네 모서리 interaction I는 모두
[−2.668505746423, −2.118796636045]×10⁻¹² K에 포함된다.**
0보다 작은 상한은 양의 면적 부분사각형의 음의 interaction, strict submodularity와
두 marginal의 감소를 보장한다. 축 위 실제 함수를 유지하면

F = F(λ,0)+F(0,b)−F(0,0)−2.393651191234×10⁻¹² λb + R,
|R| ≤ 2.748545551890×10⁻¹³ λb K.

이 교차 오차는 축의 미계산 비선형성까지 직선화한 오차가 아니다.
첫 반응 F_λ<0, F_b>0는 고정된 PHYS17 결과로 유지된다.

## 구성과 실제 검산

`theory/MIXED_RESPONSE_THEOREM_KO.md`의 62개 번호식은 직접·상관 mixed implicit 식,
HI 유리식 공간차, HH·He density bridge, 일곱 photon sector, 35개 photon/guard
mixed jet와 양의 입자수 분모를 가진 유한 온도 quotient를 구성한다.
원 C,B,q,S와 signed C² Hessian 구간을 사용한다.

주 application run02와 readout01의 exact 결과는 동결했다. 주 계산 wall은
0.967359201 s, readout은 0.114272613 s였다. 독립 Fraction/Cramer 계산은
22/22 PASS, 별도 photon polynomial convolution 980/980 포함을 얻었다.
실제 Wolfram 15.0.1 + xTensor 1.3.0 실행에서 tensor 7개와 scalar/matrix 성분
14개 차이가 정확히 0이다. xPerm의 Wolfram Language backend를 사용했다.
새 source callback, nonlinear physical root solve, history replay는 모두 0회다.

가장 큰 음의 기여는 stage −hDq₂[s_b]ν_H와 endpoint −H_{gλ}(g_F)d_b에서 나온다.
명시적으로 분리한 다섯 HH gradient 항, 광자 일곱 항은 같은 Full inverse와
온도 covector를 거친다. 온도 geometry는 유한 quotient에 별도로 더해진다.
HeII mixed gas 성분의 포함은 0을 포함하며 그 부호를 새로 판정하지 않았다.

## 읽기 순서

1. `report/WU088_HH_PHYS18_THEORY_20261013.pdf`와 LaTeX 원고.
2. `theory/MIXED_RESPONSE_THEOREM_KO.md`, 수치 corollary와 claims JSON.
3. `checks/application/APPLICATION_KO.md`, run02/readout01의 원 수치·자원 기록.
4. `review/INDEPENDENT_REVIEW.json`, `review/DECISION.json`.
5. `HANDOFF_KO.md`, `NEXT_DAG.json`, `contracts/CURVATURE_CONTRACT.json`.

## 다음 연구 단위

**HH_DEFECT_PARAMETER_CURVATURE**: 두 pure curvature F_{λλ},F_{bb}를 실제 포함하고
전체 bilinear 보간의 signed/absolute 오차를 K로 구한다. C1–C20을 유도했고
23개 입력 파일과 실제 read field를 검토했다. 첫 half의 선형 inverse 준비는
C₁=I, S₁=(1,1,1,27/2), q₁<0.0005396<1로 완료했다.
두 순수 곡률의 수치 application은 **not_run**이다.

앞선 13개 HH DAG 노드 값과 원 global REI DAG bytes는 보존했다.
새 global RUX 완료는 없고 heavy_queue=[], launch=false다.
원 native/microscopic 경로의 조건은 별도 범위로 유지한다.

## 재현과 기록

`DEPENDENCIES.json`의 PHYS17 최종 archive와 그 안의 PHYS16/15를 형제 core로
복원한다. 원 성공 출력 디렉터리는 유지하고 새 출력 경로로 재현한다.
일부 추가 균형 contraction, true-Full photon endpoint readout, finite Neumann
tail은 유도로 채택됐으며 모든 추가 경로를 수치 실행했다고 세지 않는다.
첫 guard schema 오류와 독립 checker 표현 오류는 원 source·로그와 함께 보존했다.
실제 Git·백업 응답은 `publication/BACKUP_ACK.json` 및 최종 별도 delivery receipt로
결박한다. 이미 채택한 과학 파일을 저장 상태 때문에 재계산하지 않는다.
