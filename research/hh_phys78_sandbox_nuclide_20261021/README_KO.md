# PHYS78 — 샌드박스 LRS 동위원소 pilot

**31개 z=20→2 이력과 1개 별도 정련, 10종 PNG/PDF가 완료되어 포함되어 있다.** 자세한 유도·결과·제약은 [FINAL_REPORT_KO.md](FINAL_REPORT_KO.md), 상태는 [DAG_OVERLAY.json](DAG_OVERLAY.json), 실제 계산 수는 [EXECUTION_LEDGER.json](EXECUTION_LEDGER.json)을 읽는다.

## 실행

Python3.12와 requirements.txt의 패키지를 사용한다. 의존성이 준비된 환경에서는 Rust·별도 컴파일·온라인 반응률 다운로드가 필요 없다. 이 디렉터리에서:

```bash
python source/run_pilot.py --output results/pilot --site local --max-workers 3 --preflight
python source/run_pilot.py --output results/pilot --site local --max-workers 3 --resume
python analysis/check_saved_results.py
python source/plot_pilot.py --input results/pilot --output figures
```

`--resume`는 source/input/config와 저장 payload SHA를 확인하고 같은 완료 identity를 건너뛴다. 실제 확인에서 31 skip, 0 new ODE, 93 case file bytes 불변이었다. 실패 case의 자동 overwrite/retry는 하지 않는다. 완료 계산을 다시 만들기 위해 claims를 삭제하지 않는다.

## 과학 범위

Non-tilted LRS Bianchi I, anisotropic collisionless nonbaryonic matter/free radiation, isotropic reacting H1/D/T/He3/He4/Li6/Li7 gas. 지정 isotope의 q=0..Z 전체21 nuclear/ionic state와 derived electron. Gas thermal/binding energy, electron, gray photons, expansion은 결합되어 있다. **pi_gas=0; 비영 pi_m은 collisionless DM이다.**

활성 rate는13PI+13RR. n/T초기값0, LiIII/IV는18/30/60eV광원에서0이다. 슬롯 보유는 모든 전하 단계의 활성 생성이나 전체19핵반응 완료를 뜻하지 않는다. Molecules/anions, CI/CX, Compton, spectral reactive transport 및 baryonic anisotropic closure는 OPEN이다. gas Tmax약25371K에서 CI생략이 무시 가능하다고 입증하지 않았다.

Signed sigma=diag(-s,-s,2s), pi_A=diag(-p_A,-p_A,2p_A)를 같은 normal frame에서 보존한다. Tensor sum 후 norm; Frobenius=sqrt2×half-contraction. 기존 PR128기준과 HH1231/REI729/HH74control63을 대체하지 않는다. sampled residual과 한 점의 combined refinement는 continuum certificate가 아니다.

## 수치·자원

불변 positive packet 준비, shared moment evaluation, bounded output batch, 정확한 BDF diagonal scaling을 사용한다. Accepted-state clipping은 없다. Invalid Newton predictor는 명시적으로 실패할 수 있으며 무조건 recover하는 보장은 없다. 완료31pilot에서 negative/rejected stage는0이다. 성능배수·benchmark주장은 없다.

이번sandbox실제8CPU/8GiB, 기본3one-threadworkers. NCPprofile상한64CPU/128GiB, 실제headroom·cgroup·affinity·공유lease로 제한한다. 다른process는종료하지않는다. 이미완료한본pilot을NCP에서다시실행할필요없다.

HH_R10=OFF. Production admission NOT_ISSUED. Additive Draft PR133, merge하지않음. 다음 의무는 COLLISIONAL_ATOMIC_AND_THERMAL_CLOSURE이며, hardUVLi활성화는inner-shell/source contract를먼저닫는다.
