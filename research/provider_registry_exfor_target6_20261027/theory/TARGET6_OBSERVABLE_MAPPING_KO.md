# Target 6: EXFOR 공급자 관측량과 저장 사건 열의 사상

## 1. 이번에 닫는 입력 의무

원 target 6은 `⁴He + γ ↔ D + D`이며 정방향은 `TARGET19:06:target_forward`다. R2는 이 방향의 정수 수 사영을 이미 승인했지만 직접 수치 공급자 참조를 확보하지 못했다. 이번 입력은 공식 IAEA EXFOR export의 `(2-HE-4(G,D)1-H-2,,SIG)` 및 `DA` 표다. 공급자의 핵종 표기가 이 반응의 핵 채널을 직접 식별한다. 따라서 **수치 자료가 존재하는가**라는 입력 의무를 실제 원행으로 닫을 수 있다. 이것만으로 소비자의 사건 빈도를 확정하지는 않는다.

공급자 pin은 `IAEA-NDS/exfor_master@939a14d7bba1ddce51975cb5e8711ce96b3b0871`이다. 원 `ENTRY`, parent/subentry `BIB`, `COMMON`, DATA 헤더·단위·고정폭 cell·행 위치가 `sources/exfor/PROVIDER_ROWS.json`에 연결되어 있다. 원 entry SHA256과 Git blob SHA1을 보존했다. 저자 제공 수치와 논문의 TABLE 전사는 직접 입력으로 삼고, CURVE 출처는 원문만 보존한다. 행 수와 물리적으로 독립적인 실험 수는 다른 수량이다. 특히 M0475002와 M0475003은 같은 실험의 미분·적분 관측량이다.

## 2. 관측량은 공급자가 정의한 형태로 유지한다

| Subentry | 자료 | 입사 에너지 표기 | 단위 | 이번 연결 |
|---|---|---|---|---|
| M0011002 | SIG 14행, Arkatov 등 1978 저자 제공 | EN 26–65 MeV의 14개 표지 | MICRO-B | 원 표의 각도·이차 에너지 적분 단면적 |
| M0475002 | DA 12행, Arends 등 1976 Table 1 | EN 213/258/330 MeV, 각 에너지에 ANG-CM 46/61/73/87도 | NB/SR | CM 미분 단면적 |
| M0475003 | SIG 6행, 같은 논문 Table 2 | EN 201–359 MeV의 6개 표지 | NB | 원 표가 제공한 적분 단면적 |
| M0826002 | SIG 4행, Arkatov 등 1972 Table 1 | EN-MIN/MAX, 총 범위 30–75 MeV | MICRO-B | 입사 에너지 bin으로 보고된 SIG |

[LEXFOR 2025/05](https://nds.iaea.org/nrdc/nrdc_doc/iaea-nds-0208-202505.pdf) C.1, C.8, D.13에 따라 EN은 별도 `-CM` 표지가 없으므로 lab 관례, ANG-CM/DATA-CM은 CM이다. SIG는 이차 에너지와 방출 각도에 대해 적분된 면적 단위 관측량이고, DA는 `dσ/dΩ`다. 입사 에너지에 대해 적분한 `∫σdE`는 INT와 면적×에너지 단위를 갖는다. **M0826002에 EN-MIN/MAX가 있다는 사실은 그 SIG를 INT로 바꾸지 않는다.** 이 값의 실제 빔 응답·bin 가중치는 이번 entry에서 정해지지 않았다.

단위의 차원 사상은 `1 MICRO-B = 10⁻³⁴ m²`, `1 NB = 10⁻³⁷ m²`, `1 MeV = 10⁶ eV`다. 이번 데이터에는 이를 적용하지 않고 원 문자열을 유지한다. 에너지 표지 사이의 보간, 범위 밖 외삽, 네 TABLE 공급자의 결합·재정규화는 수행하지 않는다. 특히 46–87도의 네 각도 값을 4π배하거나 반구 대칭을 가정해 total SIG를 새로 만들지 않는다. M0475003은 M0475002에서 이번에 계산한 값이 아니라 별도로 공급된 표다.

M0011003은 `EP,SIG`, COMMON `POLAR=2`이다. LEXFOR M.12의 electric multipolarity 정의에 따른 **E2 성분**이며, 빔 편극도가 2라는 뜻이 아니다. 7행을 보조 자료에 보존하고 main 36행이나 전체 SIG에 가산하지 않는다.

## 3. 정수 사건 열의 재사용과 동일 입자 계수

R2가 저장한 `TARGET19_PHOTONUCLEAR:06`의 material 수 변화는

\[
\Delta N_{{}^4\mathrm{He}}=-1,\qquad \Delta N_D=+2.
\]

조건을 갖춘 사건 flux가 나중에 `R = n_He4 Γ`로 정의되면 물질 source는 `(-1,+2)R`, 흡수 광자 수는 `-R`다. 공급자 SIG가 이 사건 단면적이라는 연결이 확정되어야 `Γ`의 실제 광자 스펙트럼 적분을 정의할 수 있다. 이번에는 `R`, `Γ` 어느 것도 계산하지 않았다. proper-time 및 reference-nucleus convention은 저장된 R2 열의 조건을 그대로 상속한다.

bare ground 수 사영에서는 baryon 변화가 `-4+2×2=0`, 전하 변화가 `-2+2×1=0`, electron-lepton 변화가 0이다. 이 산술 관계는 이미 승인된 열에 들어 있으며 새 compiler 호출 없이 행과 원 출력 SHA를 참조한다. 원 실험 target의 전자·이온 상태가 bare ground 모델과 같다는 결론은 여기서 나오지 않는다.

광핵 정방향의 초기 입자는 He4와 photon으로 서로 다르다. 최종 D 두 개를 이유로 이 사건 flux에 초기 동일쌍 계수 `1/2`를 붙이지 않는다. 역방향 D+D의 unordered pair convention은 별도 공급자와 소비자 규약에 속하며 이번에 생성하지 않는다. 또한 DA가 이 exclusive 두-D 채널의 완전한 D 입자 수율로 정의될 경우 `∫dσ_D = 2σ_event`이다. 이미 final-state 중복을 처리한 event 관측량에 다시 계수를 적용하면 오류가 된다. 선택 entry만으로 full/half-sphere와 particle/event 규약을 결속하지 못하므로, **원 값을 재정규화하지 않고 그 의무를 남긴다.**

## 4. 불확실성과 상태의 의미

네 main 표는 모두 ERR-S를 제공한다. 해당 숫자와 단위를 그대로 연결하고 통계오차로 읽는다. 이는 총오차·신뢰구간·확률분포·공분산을 제공했다는 뜻이 아니다. M0826 parent의 `(ERR-SYS,,5.)`는 입사 감마 beam intensity에 대한 **5% 이하의 상한**이다. 이를 정확한 Gaussian 표준편차 5%로 바꾸거나 ERR-S와 제곱합하지 않는다. 다른 계통오차의 부재는 0이 아니며, 신뢰확률·공분산·합성오차는 null이다. 같은 실험의 미분·적분 표를 독립 관측으로 곱하지 않는다.

source 표기는 He4 및 D의 동위원소와 exclusive nuclear channel을 식별한다. 이온 전하, 전자 상태, 세부 핵 상태/isomer와 소비자 bare 상태의 일치, beam response 및 event normalization은 미결속이다. branch fraction은 null로 남기며 exclusive channel 표기를 전체 photoabsorption branching ratio 1로 해석하지 않는다. 핵 Q, 원자–bare 질량 변환, 질량·결합 에너지 공분산 및 에너지 침적은 이번 단위의 계산 대상이 아니다. Q 값·오차·질량 규약은 null, Q admission은 false다. 기존 약반응의 spectator electron·딸 상태·neutrino 규약은 R1/R2 근거를 그대로 보존한다.

## 5. 다음 물리 연결의 필요 입력

선택한 실험의 원 논문 또는 공급자 보완으로 incident-energy response, angular acceptance/integration, 동일 D 정규화를 먼저 확인한다. 각 가용 데이터셋의 계통오차·공분산과 상호관계도 함께 기록한다. 그다음 실제 소비자의 isotope/ionic/nuclear/electronic 상태, MeV photon spectrum, 좌표·시계·밀도·process owner가 source와 맞는지 결속한다. 낮은 원자 광이온화 에너지 범위의 기존 REC 입력을 이 핵 반응의 MeV photon 소비자로 대입하지 않는다.

이것은 다음 물리 계약을 만드는 구성적 경로이며 새 no-go 정리가 아니다. 이번 판정의 상한은 **4개 실제 TABLE 공급자·36개 원 수치 행과 기존 target6 정수 열의 참조 연결**이다. 모든 rate/Q/state-branch-domain/energy/consumer admission, activation은 false다. 원19 ID·28방향의 primary-source 참조는 완비되지만, 전체 확장 종·상태·분자·음이온 과정의 모든 물리 승인이 완료됐다는 주장은 하지 않는다.
