# PHYS13: 같은 소스 계열의 유한 온도·전자 응답과 냉각 분해

## 목적과 범위

사용자의 2026-10-12 다음 WU088_HH 연구 루프 실행 요청에 따라, PHYS12의 선택된 미래 HH ON/OFF 응답을 실제 source 온도와 전자 수로 변환한다. 원 동기는 HH가 같은 암시적 단계의 가스에 주는 절대 효과와 그 물리적 원인을 구분하는 것이다. PHYS09의 기존 혼합 온도 구간과 source energy Jet를 재사용한다. PHYS13의 새 산출물은 유한 ΔT, Δ(n_e/n_H), Δn_e, 두 냉각 기여, energy-projected effective energy per extra electron, 상대적인 birth 보정, 그리고 f/fhat readout 차이의 상관된 응답 상계다.

## 고정 입력과 보호할 의미

- 프로젝트: cosmosapjw-quantum/WU088_HH. 읽은 최신 계획 commit 76bba5e3a59234f46fa7dcfc6dcdcb125c813e57; PHYS12 science dcea5dc6545736e6f4afa5acf4b7eabd428485e8.
- 각 stage에서 허용된 동일 고정 계수 tuple α를 (λ,b)∈[0,1]² 전체에 유지한다. C² real-lift/source-inclusion과 uniform root enclosure는 PHYS09의 상속 전제다.
- g=(x_HII,y_HeII,y_HeIII,w[eV/H]). fhat=exact(nHe_stored)/exact(nH), C_T=2 exact(ev_erg)/(3 exact(kb_erg_k)), p=1+fhat+x+fhat(y1+2y2), T=C_T w/p. Source와 photo energy weight의 f=exact(fHe)와 fhat를 합치지 않는다.
- 실제 Full d=1.25e9 s, first_half d=6.25e8 s는 같은 COMMON에서 따로 시작한다. 과거 HH ON/광자/compensation은 유지된다. λ=0은 선택된 미래 HH source를 끄며 b=0은 선택된 미래 photon birth를 끈다.
- 원 U,V,W/source energy Jet/exact endpoints와 scalar bits를 재사용한다. 원 source, basis, closure, compensation, precision/tolerance를 바꾸지 않는다. 초기 box 밖의 수치 해·새 ray carry·history를 구성하지 않는다.

## 계산과 완료 기준

1. 실제 source 온도식과 보존 leaf bits를 연결한다. 첫 단계 C² branch 및 exact endpoint 출처를 남긴다.
2. 기존 Banach self-map 자료 β+|K|r로 root value box를 포함하고, 새 source 호출 없이 유한 관측량 응답을 exact Fraction 산술로 계산한다.
3. U_e>0 및 U_T<0가 포함으로 판정되면 finite Δe>0, ΔT<0를 보고한다. 성립하지 않으면 수치 구간을 그대로 보고한다. 부호를 만들기 위한 clipping은 금지한다.
4. ℓ_f U=d(ℰ_g U+ℰ_λ)를 사용하여 thermal/electron 상관을 보존한 χ_eff=-U_w/U_e와 두 냉각 기여의 비중을 계산한다. 각 분모의 strict positivity와 source identity를 확인한다.
5. PHYS09의 positive temperature mixed interval은 재사용 결과로 표시한다. 이를 새 ΔT와 결합한 유한 birth 억제 비율은 새 결과다.
6. source-aligned fhat readout과 stage-f readout 사이의 λ-response 차이는 같은 g(λ,b) 위의 상관된 차이식으로 감싼다. source 자체를 f로 바꾸는 실험으로 읽지 않는다.
7. exact rational analytic cases와 독립 유도/판정으로 주요 위험을 확인한다. 같은 입력의 과거 full suite는 재실행하지 않는다.

## 예산·승인·종료

경량 Python 표준 라이브러리 후처리. 각 과학 실행 wall/CPU 45초, 주소공간 384 MiB, 파일당 32 MiB. 실패는 원 로그와 함께 보존하고 같은 범위에서 근거 있는 수정을 한다. 새로운 native/source/root call, NCP heavy job, 예약 실행은 없다. 가용 입력·유도·실행·보고서·별도 branch/PR 및 기존 승인된 Drive/Dropbox 이중백업은 연속 수행한다. main merge와 외부 메시지는 수행하지 않는다.

후보 생성·계산에 관여하지 않은 독립 reviewer가 scoped PROMOTE/HOLD를 판정한다. 필수 판별 위험이 해소되면 추가 검산을 멈춘다. 실제 consumer는 이번 타겟 조사에서 결박되지 않았다. 이 독립 provider 관측량 연구가 외부 소비 admission, RUX14 또는 전체 REI 완료를 뜻하지 않는다.
