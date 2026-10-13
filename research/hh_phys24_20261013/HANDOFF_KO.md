# PHYS24 완료와 PHYS25 재개

## 현재 결과

고정 warm P01의 PHYS22/23 finite-response/exposure 계수를 재사용하여 전체 single-ionization event 단면적 σev에서 network k=<σev vrel>/2로 가는 양의 Maxwellian kernel을 만들었다. 실제 σ 자료의 event convention을 먼저 읽어 변환하며, 기존 LCS 등의 k에 추가1/2를 넣지 않는다. 에너지축은 CM이고 equal-mass lab 에너지는2E다.

9개 bin의 연속 온도 영역상 외향 weight는 results/KERNEL_BIN_TABLE.csv에 있다. 같은 absolute σ-error에 대한 weight의92.50624%가 χ..2χ CM에,99.93503%가χ..50eV CM에 놓인다. 실제 사건 비율은 σ(E)를 곱한 뒤 계산한다.

BASS_HE THEORY13의 endpoint cone을 Maxwellian energy weight로 확장했다. 정확한 compatible 점값과 정당화된 L에 대해 σ-=max(0,max_i(si-L|E-Ei|)), σ+=min_i(si+L|E-Ei|)의 적분은 admissible 비음수 L-Lipschitz 집합의 실제 inf/sup다. 새 점 추가에 따라 nestedness가 성립한다. [14,18]eV의 제조된 witness에서중점하나를추가하여폭을1.988536배줄였다. 이를 실제 산란 데이터로 기록하지 않는다.

## 재사용 위치

DECISION.json, results/PHYS24_RESULT.json, CROSS_REPO_REUSE.json, NEXT_INPUT_CONTRACT.json을 읽는다. Local PHYS23 archive와 별도 posted PR56은 bytes 및 rate표가 다르다. 공통 PHYS22 majorant identity와 exposure 계수만 연결했으며 local 완전한 coefficient 입력으로 계산했다. HE recoil 수치상계와 CR cold electron-donor 수치는 다른 physical family라 전이하지 않았다.

## 다음 단위

PHYS25_NEAR_THRESHOLD_CHANNEL_CALIBRATION. 같은 H(1s)+H(1s)->H+ + H+e_free 사건에 대해 CM χ..2χ의 표본/pointwise bounds 또는 교정된 모델과 오차를 우선 확보한다. Sheldon1965 NASA-TN-D-3134는 같은 채널의 threshold..twice-threshold benchmark 후보이며 원문 그림과 수식은 아직 실행용으로 전사하지 않았다. 해당 H-H 결과의 uncertainty와 다른 He-He/Ar-Ar 비교의 factor-two를 분리한다.

고에너지 연결과 tail을 명시하고, rate 상계를 기존 observable 계수에 곱한다. 실제 온도/전자/Thomson 할당예산을 받으면 Kallow=min(B_T/C_T,B_e/C_e,B_tau/C_tau,Ktube)에 대입한다. 예산을 수치 reference tolerance로 바꾸지 않는다. Shape/slopes 없이도 pointwise-bin 상계 경로는 유효하므로 강제 매끄러움 가정을 추가하지 않는다.

완료된 nominal source, ODE, tangent, 비교행렬과 가중치 캠페인은 다시 돌리지 않는다. 새 입력이 바꾸는 bin/정규화/온도 범위만 재평가한다. 코드·보고서의 결과는 같은 assistant의 독립 산술/CAS 경로 검증이며 외부심사 없음. 이번 신규 원격 게시/업로드 없음.
