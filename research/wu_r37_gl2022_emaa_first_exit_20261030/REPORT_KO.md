# WU R37 | 원논문 2편을 사용한 새로운 물리 계산 보고서

## 결과 요약

원본 GL2022 computed SQM H+ + HD -> D+ + H2 700 source cells, EMAA HD-H+ 171×25 original rates 및 EMAA/HITRAN 복사 A 계수로, HD(v=0,J≤4)에서 **첫 화학반응 혹은 첫 원자료-영역 이탈**을 경쟁시키는 상태공간 CTMC를 계산했다. 8개 정확한 원본 온도 ×4 양성자 밀도 ×6 복사 경계 ×2 명시적 핵스핀 정책 ×5 초기 상태로 **1920 사례**를 생성했다. 원본 H2 최종 J0..9 분기는 **19200행**, 출판 논문 Eq5의 신뢰가능 기여량은 **8행**을 별도 파일로 작성했다. 자원 사용은 원본 출처가 제공하는 5×5 killed generator의 확률해석으로 한정한다.

## 대표적인 새로운 물리 결과

Tgas=105 K, proton density=1000 cm^-3, initial HD(v0,J2), GL2022 Eq6-7 product-spin-weighted source:

- z_rad=30, T_rad=84.4905 K: P(chemical first)=**0.9999926345924086**, P(collision exit first)=**4.514809101390478e-6**, P(radiation exit first)=**2.850598489955173e-6**.
- z_rad=300, T_rad=820.3755 K: P(chemical first)=**0.1938681645474435**, P(collision exit first)=**1.2601515523206718e-4**, P(radiation exit first)=**0.8060058202973245**. Radiative exit decomposes into v0 high-J **0.7243692380925736**, vibrational/higher **0.08163658220475084**.
- The high-redshift boundary *parameter* is a prescribed radiation temperature, not an astrophysical gas history. Outside-state return and chemical reactions are not followed.

Source-selected range across all 1920 conditional experiments: chemical-first probability **1.0367998467242782e-6 … 0.9999999999972595**; collision-first exit maximum **0.5630721119877884**; radiation-first exit maximum **0.9999989631917894**. Maximum total first-absorption mass defect **2.0735060368142087e-16**.

## 수치적/이론적 범위

저밀도·저온 입력에서는 M-matrix의 조건수가 매우 커서 단순 float64 inverse 확률 결함이 4.54e-10에 달했다. 모델 계수를 확대/clip하거나 허용오차를 풀지 않고 **65-digit inverse + source-rate outgoing-sum diagonal**으로 직접 재계산해 수지식을 복원했다. Python 12개 표적 테스트는 normal, `python -O` 양쪽에서 통과했고, 별도 first-step jump-chain 역행렬 알고리즘과 Wolfram 정확한 두 상태 항등식도 검산했다. 동일 작성자 자체 검산이며 다른 작성자의 R6/C9는 수행되지 않았다.

## 문헌 확인 및 중요한 blocker

GL2022 JCP 157 214302 (2022) main PDF, Velilla2008 JCP129 084307 main PDF를 직접 읽고 SHA 잠금했다. Velilla의 H3+ 37170 cm^-1 해리 한계는 HD/H2의 동위원소 반응 Q나 threshold가 아니다. 동위원소 동역학 재구성에는 원논문 각주 55에 명시된 **EPAPS E-JCPSA6-129-612834 Fortran source code**, 해당 PES/질량 규약/분자 진동·회전 영점과 화학반응 채널이 실제로 필요하다. 공개 웹에서 원문 Fortran ZIP 바이트를 확보하지 못했으므로 새 연구는 이를 재구성했다고 주장하지 않는다. 또한 EMAA 사용자 업로드 원본의 내부 SHA/형식은 맞지만 EMAA 공식 서버에서 독립 재다운로드 바이트 인증은 아직 완료되지 않았다.

R36 50개 GL vs EMAA numeric mismatch와 16개 EMAA-only pair는 이전 R36에서 이미 원문 대조되었으나, 두 출처의 차이를 출판사/저자 수정으로 확정하지 않았다. 본 R37은 신뢰가능 GL 초기 J0..4 화학반응만 사용하며 15 K `.000(00)`, 2505 K j3,J'7 의심 지수, j5 중복 전사 문제, j7/J8 미확보 반응 경로를 자동 대치하지 않는다.

## 산출물, DAG, 결정

- `results/R37_CHEM_VS_EXIT_1920.csv`: 전체 첫 종료확률과 독립적 이탈경로, 기대 첫 종료시간.
- `results/R37_CHEM_H2_PRODUCT_19200.csv`: H2(v0,J'0..9) 반응경로별 첫 종료확률.
- `results/R37_PAPER_EQ5_PARTIAL_8.csv`: GL2022 Eq5 논문 열평균과 입력한 에너지 convention을 명시한 일부분의 hybrid 비교.
- `results/SUMMARY.json`, `run_r37.py`, `tests/test_r37.py`, `evidence/*`: 코드·원본 SHA·실제 실행 로그·리뷰.

Canonical DAG **34/49** (+0), auxiliary R37 **1/1**. 문서의 20개 연구 단계 기록은 한 과학 계산에 대한 retrospective evidence ledger이지 독립된 실험 20개가 아니다. R6/C9 distinct-author NOT_RUN. Owner ACK/physical Q/native PES source/L4/production 모두 HOLD. PR/백업은 원본을 보호하는 add-only 별도 경로에만 게시한다.
