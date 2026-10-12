# PHYS13 독립 판정: PROMOTE_SCOPED

2026-10-12. 판정자: `/root/hh_phys13_decision_review`.

후보 생성과 후보의 검증 설계에 참여하지 않은 독립 판정자로서, 최종
`thermo_v2` 산출물과 최종 이론을 **PROMOTE_SCOPED**로 판정한다.
판정 대상, 입력 hash, 읽은 범위와 상속 전제는 `DECISION.json`에 기록했다.
과학적으로 차단하는 미해결 지적은 없다.

## 판정 대상과 실제 검사

최종 계산 코드 SHA256은
`45c6b076ce4e90b5a00a26c39503bbcbe862f814ba960782248a8737787dfeaa`,
최종 이론 SHA256은
`ec4d3ed67130683f5d1529d6802db67780a5aa7bf514637f4f757670ef88ef8b`다.

후보 모듈을 import하거나 실행하지 않고, 별도로 작성한 Fraction 구간
산술로 원 PHYS09 exact endpoints와 보존 scalar words에서 핵심 결과를
재구성했다. 두 first-stage의 Δe, Δn_e, ΔT, 두 냉각 성분, projected
ΔEgas, χ_eff, 냉각 비중, birth 온도 해석, 억제 비율과 f/fhat bridge의
정확한 끝점이 모두 일치한다. 196개 assertion에는 86개의 십진 외향 표시
검사와 8개의 작은 exact-rational/Jet 사례가 포함된다. 실제 과학 family는
두 개다. 이 수를 196개의 독립 물리 사례로 읽으면 안 된다.

독립 검산 실행은 약 0.039초였고 `INDEPENDENT_ARITHMETIC.json`에 결과와
스크립트 hash를 남겼다. 선택적 CAS import는 설치된 환경에 없어 실패했다.
그 환경 사건과 원 traceback은 별도로 보존하고, 표준 라이브러리의 정확
유리수 4-slot Jet로 해당 검사 부분을 구성했다. 후보 과학 코드·입력에는
변경이 없다.

## 핵심 수학과 수치 판별

1. **온도·전자 규약.** 실제 FT03 source는 저장 nHe와 nH를 각각 constant
   Jet로 올려 나눈 fhat를 사용한다. `f = exact(fHe)`와 fhat는 구별된다.
   `T = C_T w/Pi`와 `ne = nH[x+fhat(y1+2y2)]`의 연결은 원 source와 맞는다.
2. **Root와 유한 응답.** 근의 fixed-point 성질로 얻은
   `gc ± (beta + B r)`는 상속 Y 안에 들어간다. 같은 α와 같은 근 branch를
   유지한 FTC 적용은 단위 λ 경로의 유한 응답을 포함한다.
3. **에너지 상관.** `ell_f U = d(E_g U + E_lambda)`는 원 energy residual의
   정확한 첫 미분이다. 저장 gradient와 λ tail을 유지한다. 새로 계산한
   gas-energy HH 응답은 두 stage에서 엄밀히 음수다. R에서 f/fhat 차이와
   He 항을 보존한 χ_eff 식도 정확하다.
4. **Finite 비중.** 유한 `-Δw/Δe`는 양의 Ue 가중평균으로, 입자 냉각 비중은
   양의 `-U_T` 가중평균으로 local 포함을 상속한다. 단순 무가중 적분이나
   endpoint 성분 분해와 같다고 두지 않는다.
5. **Birth와 mixed 온도.** Vw와 Ve는 양수지만 `Vw/Ve < w/Pi`가 엄밀하므로
   photon birth의 유한 온도 응답은 음수다. 재사용한 양의 mixed-temperature
   포함과 모순되지 않는다. 기존 W_T의 출처는 PHYS09다.
6. **Readout bridge.** `(f-fhat)`를 인수로 보존한 동일 g의 온도 차이와 λ
   미분식이 정확하다. 그 유한 bound가 두 다른 source의 근 차이를 포함하는
   것으로 확대되지 않았다.

| 독립 검산한 포함 | full | first_half |
|---|---:|---:|
| ΔT [K] | [-2.283422272e-5, -7.460984727e-6] | [-1.141949741e-5, -3.731834011e-6] |
| Δe [electron/H] | [1.027763740e-10, 3.128554646e-10] | [5.142175993e-11, 1.565039294e-10] |
| ΔEgas [eV/H] | [-4.224385304e-12, -8.590455955e-13] | [-1.058106258e-12, -2.156864302e-13] |
| χ_eff [eV/electron] | [13.60117523, 13.63954074] | [13.59981015, 13.61901334] |
| 입자 냉각 비중 | [0.3167901824, 0.3198634497] | [0.3171088123, 0.3198927331] |

표는 원 exact 포함보다 바깥쪽인 표시를 사용한다. 원 근의 점 추정,
통계적 신뢰구간 또는 시간 적분오차의 표가 아니다.

## 해소된 지적과 채택 범위

이론 §9에 electron suppression ratio를 새 수치 산출물과 나란히 열거한
표현을 지적했다. 최종본은 실제 계산한 temperature ratios 및 electron
mixed sign과, 식 (29)에서 유도한 electron ratios를 명확히 구별한다.

채택 범위는 각 고정 α에서 PHYS09 whole-box source inclusion, 열린 C²
real-lift, uniform root·응답 포함을 상속하는 두 개의 독립 first stage다.
full과 first_half는 동일 COMMON에서 따로 시작하며 서로 다른 계수 tuple을
쓴다. 실제 carried second_half, 시간·continuum 수렴, native certificate,
full49, 일반 비등방성 scan, 소비자 admission과 우주론적 생략 판정은 이
판정에 들어가지 않는다. 전역 DAG node 완료는 추가하지 않는다.

지정된 새 관측량 후처리의 주요 위험은 해소되었다. 추가 historical suite
재실행은 필요하지 않다.
