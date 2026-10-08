# HH-F1M: Maxwell 호환성 및 입사 에너지 모멘트

Fastest lane, 동일 research/r31ao-unequal-order-ladder-20260930 branch를 유지한다. 이 폴더에는 전체16개 unit test와 실행 가능한 stdlib reference가 있다. 전체 유도·6개 경량 quadrature·17개 고정 source·실패로그·현재/역사 Git 동기화 ledger는 아래 ZIP이 기준이다. 원자 단면적 provider/새 physical domain/consumer history를 구현하거나 승인하지 않았다.

## 직접 유도한 결과

Nonrelativistic zero-drift Maxwell, fixed initial/final states, temperature-independent nonnegative sigma_eff에서
k=C*(kB*T)^(-3/2)*integral E*sigma_eff(E)*exp[-E/(kBT)]dE,
C=sqrt(8/(pi*mu)). 양의 integrand 대소관계로 T^(3/2)*k(T)는 T에 대해 비감소해야 한다.
원 k57을 바꾸지 않은3000/3001K outward 계산은 W1/W2=약3.8384872637913716e15의 엄격한 감소다. 따라서 원 floor+analytic 전체를 한 고정 양의 Maxwell kernel로 해석할 수 없다. 전체 Grackle solver 오류나 floor 삭제 승인이라는 뜻은 아니다. cutoff를 피한 analytic branch는 이 반례로 부정되지 않는다.

Exact analytic fit k=A_SI*t^p*exp(-B/t), t=T/(1K), E*=kB*(1K), E0=B*E*, a=p+3/2에 대해
E*sigma_eff(E)=A_SI*E*^(-p)*(E-E0)^(a-1)/(C*Gamma(a)), E>E0
를 구성하면 gamma 적분으로 같은 fit를 얻는다. 이는 형식적 analytic continuation이며 experimental sigma reconstruction이 아니다. 그 사건가중 입사 에너지는 mean=E0+a*kBT, variance=a*(kBT)^2다. a_LCS=27/10, a_KS=3. Fit E0와 consumer binding chi를 동일시하지 않는다.

HH ionization에서 입사 에너지 전체는 outgoing kinetic energy로도 남는다. 공통 thermal bath의 ground-state isolated ionization closure이면 thermal=-chi*R, binding=+chi*R이며 mean incoming energy 전체를 cooling으로 빼면 안 된다. outgoing electron distribution은 total rate에서 결정되지 않는다. R=k_net*n_HI^2(no extra half)를 보존하며 unordered pair sigma는 별도 factor convention이다.

## 실제 관측과 현재 의존성

시작 HH026d8b3는 이전 F1P 뒤 Codex sync checkpoint이며 보존했다. REI64bc3aa FT03은 HH를 controlled model에서 제외한 capture/thermal 연구다. 게시 직전 재조회에서 REI5f3bfe2로 이동했고 runtime_inputs/rei_model_lock.json(git blob c9e3243b4babf51bc3405145995a74ef52fa7ea1)이 새로 생겼다. REI-F00의 SYNTHETIC_HHE_3GROUP 계약이고 HH=0, physical_admitted=false, scientific_admission=HOLD다. 과거404를 현재파일부재로 쓰지 않는다. 지정 science_scenario_v1.json은 새head에서도404다. REI-F07의 실제 HH domain/owner/constant/budget/seam 결속은 여전히 대기한다.

## Cloud-first 회수

- name: WU088_HH_FAST_F1M_DELIVERY_20261004_v1.zip
- bytes: 84346
- SHA256: 186e1169a7265a8b83108dab654f9e40d1817c790d6a3c234ec2c27514fa91e0
- Drive ID: 1pQX_6wuLl2O_8HukojqR6KnsMHu5fthc
- Dropbox ID: id:BSpOijBcT10AAAAAADx_Cw
- Drive parent:1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM
- Dropbox folder:/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/

cache 또는 인증된 provider 한 곳에서만 bytes를 회수하고 사용자 재업로드를 요구하지 않는다. 54payload/CRC는 로컬 검증했고 remote restore는 별도다. FINAL_VERIFICATION/REPO_SYNC/REPORT/THEORY/HANDOFF를 읽는다.

이 Git 폴더에서 재현이 실제로 필요할 때만:
```sh
python3 -B -m unittest discover -s tests -v
python3 -B src/hh_moment_compatibility.py --mode moments --provider LCS91 --T 10000 --out /tmp/hh_f1m_NEW.json
```
검사는16개이며 과거suite를 더하지 않는다. 90자리 독립 quadrature는 ZIP의 measure.py와mpmath1.3.0을 사용했고6개를 수행했다. Working digits는 physical accuracy가 아니다.

다음 canonical action=REI-F07. 이후 실제 HH-F1 결속->HH-F2 consumer seam->REI-F09 유일pairedhistory->HH-F3/F4를 따른다. generic 보조함수·고정시료 반복으로 gate를 우회하지 않는다. 원24/289,265unbounded,epsilon null,B22OPEN,FD1/FD2소비와원DB를보존한다. NCP legacy/HHfield/Bianchi/rei_bianchi mutation0이다.

매loop 시작, 게시직전, 종료에 실제 GitHEAD/parent/tree를 확인한다. 동시 변경은 새parent로 add-only 보존하고 stale tree로 덮어쓰지 않는다. 이 정책은 active chat checkpoint 동기화이며 background/webhook monitoring을 뜻하지 않는다. samebranch nonforce와기존목적지 create-only백업,ACK/metadata와restore/과학validation을구분한다.

수학 비교출처:NIST DLMF5.9.1 및1.14(iii); source-specific application/증명과 실패전제는 ZIP THEORY_KO.md.
