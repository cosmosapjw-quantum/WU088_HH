# PHYS18 종료와 PHYS19 재개 계약

## 확정한 연구 위치

PHYS18 HH_DEFECT_MIXED_RESPONSE는 PROMOTE_SCOPED다. 정리 8개와 corollary 4개,
62개 번호식, 주 수치 application과 finite readout, 독립 22/22 검산 및
실제 Wolfram+xAct 검산이 연결됐다. 핵심 interval은
F_{λb}, I∈[−2.668505746423,−2.118796636045]×10⁻¹² K다.
원 C² 같은-family 전체 사각형에서의 포함이며 네 점을 새로 풀거나 차분한 값이 아니다.

## 다음에 실제 진행할 일

`contracts/CURVATURE_CONTRACT.json`을 읽고 HH_DEFECT_PARAMETER_CURVATURE를 실행한다.
원 첫 half/Full U,V와 carried second-half U,V를 재사용한다. C1–C20 순서대로
각 θ∈{λ,b}의 K_{k,θ}=g_{k,θθ}, 첫 half photon pure jet와 둘째 stage incoming
pure jet를 구성한다. carried 둘째 half에서는 Q_{2,θθ}와 교차 product의 인수 2를
빠뜨리지 않는다. Full·첫 half의 fixed-gas H_{θθ}=0과 carried incoming 곡률은 구분한다.

첫 half C₁=I와 S₁=(1,1,1,27/2)의 exact q₁은
5095881330588929517/9444732965739290427392 < 0.0005396 < 1이다.
원 Full C,B,q,S, PHYS14 second-half L_hFg와 scales도 준비돼 있다.
이 선형 준비를 다시 같은 이유로 실행할 필요는 없으며, 새 pure RHS와 inverse
포함 및 finite quotient를 실제 계산하는 의무가 남아 있다.

direct·correlated·endpoint difference pure 포함을 교차한 뒤 F_{λλ},F_{bb}의
수치 구간과 부호 또는 남는 dominant width를 기록한다. 그 크기 상계 M_{λλ},M_{bb}로
|F−L_bilin F| ≤ M_{λλ}λ(1−λ)/2 + M_{bb}b(1−b)/2 ≤ (M_{λλ}+M_{bb})/8을
실제 K 단위 수치로 닫는다. 현재 mixed 부호와 anchored correction은 재사용 입력이다.
다음 단위는 순수 응답 application **not_run**, ready 상태로 시작한다.

## 지켜야 할 전제와 경계

같은 COMMON, 하나의 전역 λ,b, 고정 admissible α, 원 33 photon+2 guard,
기체 좌표와 exact stored native leaf/온도 정규화를 유지한다. 원 signed Hessian
범위만으로 C² 유도가 닫혔다. 제시되지 않은 C³ 또는 Hessian Lipschitz 상수를
가정하지 않는다. 모든 식의 도함수는 보통 편미분이며 Taylor 1/2 계수와 구분한다.

이번의 strict negative mixed ΔT는 HeII mixed 성분의 부호, pure 곡률,
연속 방정식의 exact solution error, native/microscopic 실행 권한을 뜻하지 않는다.
원 global DAG의 상태와 첫 13개 HH 노드 값은 보존했다.
heavy_queue=[], launch=false이며 새 global RUX 완료를 기록하지 않는다.

## 재현 경로와 실패 보존

`DEPENDENCIES.json`에 PHYS17 최종 bundle과 중첩 PHYS16/15 archive 크기·SHA256,
복원 prefix, 실제 source/carry 필요 필드를 적었다. 조상 metadata는 별도 staging에
보관하여 현재 receipt를 덮어쓰지 않는다. 주 application과 독립 verifier의
원 command/환경/자원 기록은 각 PRE_RUN·RUN 파일에 있다.
원 successful result bytes를 수정하거나 성공 디렉터리에 재실행하지 않는다.

production run01은 guard의 숫자 index 접근에서 실패했고 원 named field로 고쳤다.
독립 checker의 첫 prior singleton 가정과 successor metadata 객체 비교 오류는
checker만 교정했다. 원 실패 파일을 보존했고 생산식·수치 결과는 바뀌지 않았다.
Wolfram의 미지정 함수 HH18/B18 진단은 일반 C² 함수 항등식의 형식 미분에 관한
관찰된 진단으로 보존했다. 모든 지정한 항등식은 정확히 0이었다.

## 출판과 종료

PHYS17 PR52 head ba5f2693c5c1222b2635d87f33ed4e47eba519ae에 additive branch/draft PR를
쌓는다. main merge는 수행하지 않는다. 현재 단위의 과학 commit, 실제 Drive/Dropbox
ACK와 크기 대조를 받은 뒤 R10과 저장 metadata만 닫는다. 최종 head와 전달 파일은
별도 DELIVERY_RECEIPT.json을 따른다. upload ACK와 restore verification은 다른 기록이다.
