# WU R33 실행 보고서 | 원본 HD/H⁺ SQM 화학 × CMB radiative exchange

**신규 과학:** GL2022 원문에서 인증된 350개 reactive rate + 70개 downward inelastic rate와 REC161 A, REC164 Sung 네 선 중심을 사용하여, 외부 CMB 복사장에 노출된 5준위 HD에서 첫 제한적 화학반응까지의 CMB 흡수·유도방출·자발방출과 H₂ 제품 분기 및 회전 에너지 수지를 동시에 계산함. 원본 rate/Einstein A/Sung 데이터는 변경하지 않았음.

- **1,470개** 물리 상태 (7 ×2 ×3 ×5 ×7), **5,880개** line photon expectation, **14,700개** H₂ 최종생성물 확률, **735개** 공통 실제 n(H⁺) spin policy 비교, **210개** z-CMB zero-crossing 탐색으로부터 163개의 0≤z≤300 근.
- \(T_g=105\,\mathrm K\), 초기 J=2, n(H⁺)=3954.4181821071797 cm⁻³, `Eq6-7_spin_effective`: radiation OFF \(E_{rad}=+2.5806029252187536\times10^{-21}\,\mathrm J\); z=100 CMB \(E_{rad}=-1.0246306136451205\times10^{-20}\,\mathrm J\); z=300 CMB \(E_{rad}=-2.5658596373780328\times10^{-20}\,\mathrm J\). Signed photon bath transfer reverses under an *externally prescribed* hotter radiation bath.
- 위 조건의 0점은 \(z_r=38.19417624108174\), \(T_r=106.82372734506828\,\mathrm K\), 잔차 약 \(-2.2762162406727386\times10^{-35}\,\mathrm J\). 이것은 cosmological redshift trajectory나 실제 스펙트럼 왜곡 검출이 아니라, 고정 bath 모델의 조건부 판별량이다.
- 1,470개 물리 에너지 수지 최대 절댓값 잔차 \(3.4832248603566023\times10^{-34}\,\mathrm J\); first-radiation/first-reaction 확률 정규화 최대 절댓값 편차 \(3.597122599785477\times10^{-14}\).
- CMB OFF에서는 R30 원본 210개 사례의 광자 수·기대 반응시간·선 에너지 및 2100개 H₂ 제품 확률과 일치 (Python actual test PASS). `raw_SQM` 과 spin effective를 분리하며 후자는 외부 원전의 계통오차를 뜻하지 않는다.

**이론 판정:** `derived`, `numerically_checked`, `source_qualified_scoped`. 실험 자체 검증이나 독립 작성자 R6/C9는 아님. 소스와 식: THEORY_KO.md, source SHA, src/cmb5.py, results/*.csv, tests/. 임의의 molecular formation/thermal history, fixed-density에서 실제 우주 밀도 의미, 역반응, chemistry Q, radiation transport, full-A, production은 포함되지 않음. 공식 EMAA 171×25 원본 바이트와 Velilla2008 native PES Fortran, isotope-specific threshold, REC/CR owner ACK는 미확보.

**정본 DAG: 34/49 그대로.** R33 auxiliary: 1/1 scoped. 단계 증거 R1–R10/C1–C10 총 20개는 실제 연구를 R/C로 사후 분류하는 별도 기록이며, 서로 다른 20번의 독립 실행이 아니다. R6/C9 distinct-author NOT_RUN, native subagent NOT_EXPOSED. 단계별 업로드/게시·검산의 실제 영수증은 `evidence/`에 별도 기록한다. parent PR #171 immutable, main 및 타 저장소 변경 금지.
