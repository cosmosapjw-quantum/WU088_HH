# PHYS10 비생성자 독립 검토

**최종 판정: PROMOTE_SCOPED. Blocking finding은 없다.** 같은 고정 source coefficient 계열과 PHYS09의 조건부 C² implicit family를 전제로, 잔존 광자의 양의 유한 혼합 에너지, 작은 gas+photon 잔여 포함 및 같은 family의 보상 비율을 채택한다. Total의 정확한 0이나 부호, native root/권한 및 시간·carry·전역 보존은 채택하지 않는다.

검토자: `/root/phys10_intake`, `reviewer_was_creator=false`. 이 검토자는 앞서 최신 NCP08/09의 읽기 전용 intake만 작성했다. PHYS10 유도·과학 코드·semantic tests·실행기 변경·새 과학 실행·보고서·routing/handoff를 작성하지 않았다. 이 독립성은 새 PHYS10 과학 후보에 적용되며, 본인이 작성한 intake 자체를 별도 독립 생성물로 포장하지 않는다. Host developer label은 GPT-6 Astra Pro이고 canonical router의 exact Pro alias는 미해결이다. 기존 Astra v4의 model-independent workflow를 적용했으며 실제 backend identity attestation이나 모델 전환을 주장하지 않는다.

## 1. Frozen identity와 실제 실행 증거

Frozen manifest SHA256은 `d3de0ab17b390a13b193d1d2ff66da4e5282eda126b376fd9c921c7908486a7b`다. **185개 파일, 5,997,841 bytes가 모두 일치**했다. 실행의 19개 before/after binding, 최초 snapshot 4개, raw log 2개의 크기·SHA256도 현재 frozen 파일과 일치한다. SUMMARY.json과 원 stdout은 byte-identical이며 stderr는 0 bytes다.

원 `ledger_first` receipt는 2026-10-11 08:44:01.943572–08:44:02.669802 UTC, elapsed **0.7208253940043505 s**, 최대 RSS **23,924 KiB**, exit 0, timeout false를 기록한다. Wrapper에는 wall/CPU 45 s, address-space 384 MiB, 각 파일 16 MiB 한도가 있다. 실제 Python 버전은 기록된 3.12.14다.

기록된 첫 과학 시도는 1회이며 수정 재시도는 없다. **35 assertions와 7 semantic cases**를 구별해 확인했다. 검토자는 candidate·source·compiler·gate·consumer를 실행하거나 import하지 않았고, 완료 PHYS09 inverse와 gas-energy proof도 재계산하지 않았다.

## 2. 수학과 원 source의 연결

원 `PrimaryPacket.per_h`, `photons()`, `photo_rates()`와 group→packet 전달은 N의 단위가 photons/H임을 뒷받침한다. 원 `phys04_reduced_residual`의 denominator와 rate는 동일한

\[
\kappa_{ja}=c n_H L_a\sigma_{ja},\quad
D_j=1+d\sum_a\kappa_{ja},\quad R_{ja}=\kappa_{ja}N_j
\]

를 사용한다. 따라서 \(d\sum_aR_{ja}=N_j^{in}-N_j\)가 underlying real source의 정확한 대수 항등식이다. Photon energy에는 n_H를 추가로 곱하거나 나누지 않는다. Incoming은 원 captured `fl(dt*SOURCE)` amount와 고정 ray weights에 대해 b-affine이며, 같은 COMMON와 geometry를 고정한 이 첫 단계 family에서 gas와 λ에 독립이다.

전체 observable chain rule

\[
\mathscr L[J]=J_gW+J_{gg}[U,V]+J_{g\lambda}V+J_{gb}U+J_{\lambda b}
\]

는 직접 미분으로 확인된다. Code의 gas indices 0–3, λ slot 4와 b slot 5, 두 explicit parameter cross terms 및 full 4×4 Hessian contraction이 이에 대응한다. Photon은 \(-d\mathscr L[\sum E_jR_{ja}]\)로 계산된다.

Nonphoto clone은 실제 source에서 HH·photo·expansion을 추가하기 전에 만들어진다. 동일 χ_H의 HH 반응은 ℓH=0이고, 모든 captured heat를 유지하면

\[
\epsilon_{ja}=\operatorname{exact}(heat_{ja})+
\operatorname{exact}(\chi_a)-\operatorname{exact}(E_j),\qquad
B=\ell F^{np}-2H_{mean}w+\sum_{ja}\epsilon_{ja}R_{ja}.
\]

따라서 \(W_e+W_\gamma=d\mathscr L[B]\)다. Stage f와 stored density ratio의 차이는 nonphoto의 직접 ℓ projection에 포함되므로 별도 Jnorm을 다시 더하지 않는다. Expansion도 한 번만 들어간다.

## 3. Saved output의 독립적인 정합성 확인

Candidate를 호출하지 않는 표준 라이브러리 JSON/struct/Fraction 읽기 검사로 다음을 확인했다.

- 저장된 exact interval **280개**의 분자·분모, 순서, strict/zero-containing 부호와 바깥 binary64 표시가 일치한다.
- 각 stage의 photon/total 다섯 term 구간합은 저장된 전체 구간과 exact endpoint로 일치한다.
- Direct gas+photon sum을 보존하며, source부터 투영한 total 포함은 그 안에 있다.
- Source-part별 합은 early total을 포함한다. 개별 interval 분해를 더한 끝점이 early projection과 같아야 한다는 잘못된 조건은 두지 않는다.
- 저장된 epsilon **198개**를 원 captured energy/threshold/heat bits에서 exact rational로 대조했다. 각 stage에서 **19개**가 비영이며 모두 absorber index 2다. 값은 ±2⁻⁴⁸ 또는 ±2⁻⁴⁹ eV다.
- Gas exact interval은 원 PHYS09 결과와 일치하며 denominator의 엄격한 음의 margin을 유지한다.
- Ratio의 두 표현에 대한 교집합과 eta 정의가 exact endpoint 수준에서 일치한다. Creator claim의 6개 artifact evidence identity도 모두 맞는다.

| 양 | Full | 같은 COMMON first_half |
|---|---:|---:|
| Iγ, eV/H | [2.0147819024003132e−16, 6.190685965150866e−16] | [2.5372573637033666e−17, 7.758341579441771e−17] |
| I_e+Iγ, eV/H | [−3.1314477547412323e−19, 2.4467453520579934e−19] | [−1.9605021839988345e−20, 1.5319948343632613e−20] |
| Iγ/(−I_e) | [0.9984438889973375, 1.0012158616912215] | [0.9992268494887321, 1.0006041628512914] |
| η upper | 0.0015561110026624584 | 0.0007731505112678191 |

Source inclusion과 같은 fixed-alpha C² branch 아래에서 단위 사각형 FTC가 uniform derivative 구간을 같은 finite interaction에 연결한다. 유한 A=−I_e>0, T=I_e+Iγ에 대해 Iγ/A=1+T/A이므로 ratio 포함도 정당하다. Pointwise ratio의 적분을 finite ratio로 바꾸는 오류는 없다. Photon identity 교집합은 이번 수치에서 원 photon interval을 줄이지 않았다는 보고도 그대로 맞는다.

Expansion contribution은 엄격히 음수다. Nonphoto와 total, captured ε의 mixed contribution은 0을 포함한다. 19개의 비영 coefficient가 실제 Ψ contraction의 비영성을 증명하지 않는다. Underflow 이하 rational tail의 바깥 표현인 ±2⁻¹⁰⁷⁴를 실제 exact endpoint나 정확한 0으로 바꾸지 않았다.

## 4. 검증 범위와 observer correction

이번 검토 중 첫 generic JSON visitor가 semantic case 안의 `exact` 키를 직접 interval object로 오인하여 TypeError로 종료했다. `exact`와 함께 `lo_bits/hi_bits`가 있는 실제 serialization object만 방문하도록 제한한 두 번째 read-only 검사에서 위 결과를 얻었다. 최초 traceback은 DECISION.json에 보존했다. 이것은 reviewer의 출력 검사 코드 오류이며, 과학 후보의 첫 실패나 과학 재실행으로 기록하지 않는다. Candidate bytes는 변경하지 않았다.

독립 계산으로 source Jet 전체를 다시 생성·contraction한 검증은 수행하지 않았다. 실제 프로그램·원 실행·저장 값과 정리의 연결을 검토하고, 이미 계산된 포함의 serialization·항별 합·finite identity 정합성을 확인한 범위다. 기존 PHYS09의 source/C² 전제나 uniform root proof를 새 형식 증명으로 승격하지 않는다.

## 5. NCP handoff 판정

PHYS08/09의 실제 완료 반환은 재사용으로 유지된다. NCP_TASKS와 NEXT_DAG는 `heavy_queue=[]`, `launch=false`, NCP 경량 재실행 목록도 빈 상태이며 활성 과학 budget이 0이다. Handoff가 이전 pending Rust 지시를 최신 완료 증거로 해소하는 점은 현재 사용자 실행 분담에 맞는다.

새 heavy campaign을 만들어 64코어를 채우지 않는 판단을 채택한다. 600 s, 8 independent families, 최대 56 single-thread workers/112 GiB는 명시된 미래 운영 정책이며 물리적 필수 scan 크기나 측정된 speedup이 아니다. 실제 normalized history·joint carry·next-stage source coverage·필요한 native-family binding·유한 unfinished task set과 representative cost를 확보하기 전에는 heavy launch를 하지 않는다. Energy group별 독립 gas solve와 시간 조각의 무조건 독립 분할도 제외돼 있다.

## 6. 최종 claim ceiling

P10-01/02의 source identity, P10-03의 양의 uniform/finite photon interaction, P10-04의 같은 family ratio, P10-06의 제한된 source-part 결과를 **PROMOTE_SCOPED**로 채택한다. P10-05에서는 enclosing interval만 채택하고 total sign/exact zero는 unresolved로 유지한다.

Actual native root/U/V/W/I는 null, native authority=false다. Carried second_half, paired full/two-half defect, time/continuum remainder, full49/production 및 global transport/guard/escape/redshift conservation은 OPEN이다. PHYS07 analytic reference energy와 NCP07 node32 per-node predicate도 기존 OPEN을 유지한다. 두 duration으로 시간 수렴 차수나 절대 에너지 변환 효율을 주장하지 않는다.

이 판정은 frozen 연구 후보에 대한 최종 독립 결정이다. RESEARCH_STATE.json의 `COMPLETE_HERE_PENDING_FINAL_INDEPENDENT_DECISION` 및 이론 creator-status는 이 결정 이전에 작성한 시간순 snapshot이다. 그 파일의 independent_decision 포인터가 이 최종 PROMOTE_SCOPED 결정으로 연결되므로 frozen 후보를 수정할 필요가 없다.

게시 commit, archive, Drive/Dropbox object와 실제 ACK는 아직 이 검토 대상의 완료 사실이 아니며 detached receipt에서 별도로 확정해야 한다. 과학 계산을 다시 실행하지 않고 패키징을 진행해도 된다.

