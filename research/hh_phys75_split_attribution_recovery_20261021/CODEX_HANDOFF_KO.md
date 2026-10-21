# Codex / NCP handoff: WU088_HH PHYS75 archival supplement

## 반드시 먼저 확인

1. 현 시점 GitHub WU088_HH PR128 `research/hh-phys75-sector-memory-20261021` 최신 HEAD를 읽고, PR127 HEAD의 descendant인지 검사한다. 마지막 관측 PR128 HEAD는 `92f5ab9dba531ebe05909dcb77d3740d2c68c580`. 과거 실패한 local `git fetch`를 성공했다고 소급하지 않는다. 병행 작업의 새 원격 commit이 있다면 실제 HEAD를 따르되 사용자 기존 branch/checkout을 reset/clean/force하지 않는다.
2. GitHub/Drive/Dropbox에 이번 별도 PHYS75 supplementary recovery/receipt가 이미 있는지 실제 이름과 해시로 확인한다. 동일 object는 중복 업로드하지 않는다. 새 additive archive는 user-provided historical `PHYS75_RESUME_DELIVERY.zip`의 bytes와 최신 handoff 자료를 포함한다. ZIP은 full clone이 아니다.
3. PR128 source `research/hh_phys75_sector_memory_20261021/source/stress_memory.py`, `analyze.py`, REPORT_KO.md, owner lock과, repo REI PR198/PR213을 읽는다. PR128은 이미 long1231/80015 기억 분석을 실제 수행했으므로 다시 계산하지 않는다. 기존 auxiliary `source/code/shear_attribution.py`는 explicit map이 있는 별도 standalone fallback이며 PR128 output·오차 인증을 대체하지 않는다.

## 동일 trajectory 물리 계약

(-,+,+,+), non-tilted LRS Bianchi I. sigma=diag(-s,-s,2s), pi_X=diag(-p_X,-p_X,2p_X), p_X=(P_parallel,X-P_perp,X)/3. 물질·복사의 성분 부호와 frame을 유지한 채 tensor를 더하고 전체 norm을 취한다. Signed half S=sqrt(3)s/H, P_X=sqrt(3)(8piG/c^2)p_X/H^2; full Frobenius는 sqrt2 배. Work K(sigma:pi_X)/H^3=2SP_X (half) 또는 S_F P_X,F (full). I=exp(3(N-N0))H/H0, J_X=I^-1∫IP_XdN, S=S0/I+J_m+J_r. 이는 고정 trajectory 조건부 분해이며 species를 끈 counterfactual 해가 아니다. Grid/quadrature defect는 continuum bound가 아니다.

## 새로운 작업을 실행할 때만

원래 producer에서 actual time/H/signed component columns·norm 및 SHA를 확인하고 source/ code/shear_attribution.py에 explicit JSON mapping을 전달한다. 잘못된 column 의미를 추론으로 채우지 않는다. 분석용 결과는 create-only 경로에 저장하고 case IDs+input bytes SHA, code SHA, exact command/exit, output hashes를 남긴다. 원래 PR128의 cached Simpson 결과와 비교할 경우 동일히 유효한 시간격자와 일치하는 norm를 사용한다. 새로운 ODE 또는 성능 벤치마크가 필요하지 않다면 돌리지 않는다.

## NCP/공유 서버

SSH 접근이 허용되고 필요할 경우에만 `ssh -i /home/cosmosapjw/.ssh/ncp_key root@49.50.142.2 -p 22`. 실제 연결은 그 당시 확인한다. 다른 Codex 세션은 자동 거부 사유가 아니다. 실제 affinity/cgroup CPU quota·memory.available·existing owned leases를 기준으로 가용 자원에 새 승인 작업만 채우고, 타 프로세스를 종료하거나 signal하지 않는다. max64 CPU/128GiB, minimum 16GiB reserve, BLAS/OpenMP=1. 단순 후처리는 1 worker로 충분. 기존 시간/예산 cap은 재설정하지 않는다.

## 인계와 gate

PHYS73 15 완료, PHYS71 76 panel+152 profiles, HH74 control63, REI198 long1231, REI213 warm729, PR128 6 small IVPs는 이미 완료; 재실행 0. HH_R10=OFF. Full cold EoR, general non-LRS, continuum/observational certification, HH physically matched xi/rates는 여전히 OPEN. DAG와 실행/게시/백업을 독립 상태로 기록. Postprocessing only에서는 production/likelihood admission 발급 금지. 원격 publication(실제 commit/tree/branch/PR)·provider ACK·full byte readback을 각각 따로 기록한다.
