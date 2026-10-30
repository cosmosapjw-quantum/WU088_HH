# R37 추가 물리 분석: 방사선 이탈과 화학 반응의 첫 종료 경쟁

입력: 변경하지 않은 R37 원본 `results/R37_CHEM_VS_EXIT_1920.csv` (SHA256 `83f4678316df964faf32d2dcf8a168261059deced1669414fd54bb3e2f1650cd`). `analyze_dominance.py`가 원본 바이트 해시를 확인한 뒤 **보간 없이** 1,920개 기록만 집계한다.

R37은 `HD(v=0,J=0..4)`의 문서화된 source graph를 최초로 떠나거나 첫 화학반응을 할 확률에 대한 계산이다. `P_radiative_exit_first > P_H2_before_first_exit`는 첫 종료 원인들의 상대적 우세를 의미할 뿐, 우주론적 HD 소멸 수율 또는 H2 생성률의 우세 조건이 아니다.

각 복사 경계마다 8 Tgas ×4 고정 양성자 밀도 ×5 초기 J = **160개의 조건**이 있다. GL2022 식 (6)-(7)에 따른 핵스핀 가중 모델은 `OFF/0/10/30`에서 0/160, `100`에서 80/160, `300`에서 113/160 사례에서 복사 이탈이 화학반응보다 크다. 비가중 대조 모형은 각각 0/160, 80/160, 101/160이다. 이 수치는 그리드 점들의 분율이며 임의의 천체환경 사전분포에 대한 확률이 아니다.

대표 예 (원본 그리드): Tgas=105 K, n(H+)=1000 cm^-3, J=2, weighted에서 `z=30`: (Pchem,Prad)=(0.9999926345924086,2.850598489955173e-6); `z=300`: (0.1938681645474435,0.8060058202973245). 두 값은 경계 온도 변화에 조건부이고, 시간 진화하는 우주론적 redshift가 아니다. 허용된 source-graph 외부에 대한 물리 정보가 없으므로 'global root'나 연속 z 유일성을 주장하지 않는다.

출처: González-Lezana, Hily-Blant, Faure, *J. Chem. Phys.* 157, 214302 (2022), DOI 10.1063/5.0128598, Eq.(1)-(7). Velilla et al., *J. Chem. Phys.* 129, 084307 (2008), DOI 10.1063/1.2973629, Eq.(7)-(13), EPAPS source E-JCPSA6-129-612834 *미확보*. 두 원논문 PDF는 R37 원본 ZIP에 SHA 잠금한 비공개 원본으로만 보존하고 공개 GitHub에 게시하지 않는다.

**진척 계약**: canonical 34/49 변동 없음; R37 auxiliary 1/1 scoped; R6/C9 서로 다른 저자 검증 NOT_RUN; PES_NATIVE_THRESHOLD=NULL; PHYSICAL_Q=NULL; OWNER_ACK=NOT_OBTAINED; L4=false; PRODUCTION=NOT_ISSUED.
