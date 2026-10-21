# 새 대화 handoff: PHYS75 복구와 다음 연구 실행

`$physmath-research-loop`를 사용해 WU088_HH의 PR128 이후를 이어라. 이번 대화는 새로운 물리 캠페인이 아니라, 이전 `PHYS75_RESUME_DELIVERY.zip`(SHA256 `52b329218eef5154e00a58bb27eb30fef9eadc9509f82fc8df5aac937a72305f`)의 publication/backup 실패 복구를 수행한다. 아래 실제 delivery receipt의 status·SHA·provider IDs만 새 완료 상태의 authority로 사용한다.

기준 repo https://github.com/cosmosapjw-quantum/WU088_HH. 2026-10-21의 비교 기준 PR127 HEAD `71e925938387b73958c8881a06ef387e6874fafe`, 이후의 더 새로운 PR128 HEAD 마지막 관측 `92f5ab9dba531ebe05909dcb77d3740d2c68c580`, branch `research/hh-phys75-sector-memory-20261021`. 새로운 작업 시작 전 최신 HEAD와 backup readback을 다시 확인한다. 기존 checkout·working changes를 보존한다.

핵심 과학 authority는 REI PR198 long collisionless (1231 histories), REI PR213 warm 729 histories, WU088 HH PR127 control63, HH PR128 긴 이력의 separate matter/radiation memory 및 pinned finite-L8 state reduction이다. 다른 모델·기간과 출력 표준화를 하지 않고 숫자를 합치지 않는다. PR128 18 focused tests, 3 new pairs/6 small IVPs와 plots는 기존 보고된 범위에서 완료되어 재실행하지 않는다.

이번 архив source의 `code/shear_attribution.py`는 signed same-trajectory conditional integrating factor J_m,J_r를 독립적으로 계산하는 opt-in standalone fallback이다. 원본 데이터를 읽어 제대로 바인딩하지 못하면 결과는 `HISTORY_INPUT_NOT_IDENTIFIED`다. 8 focused algebra/interface tests가 PASS였다는 사실이 729 actual trajectories를 후처리했다고 뜻하지 않는다. PR128의 생산적 분석을 다시 열거나 과거 fallback을 canonical owner로 승격하지 않는다.

수학 계약: frame common, pi_total=pi_m+pi_r tensor before norm, signed half S=sqrt3 s/H, P_X=sqrt3 (8piG/c²)p_X/H², full Frobenius =sqrt2 half; I=e^{3(N-N0)}H/H0, S=S0/I + J_m+J_r, J_X=I^-1 int IP_X dN. Work factor=2SP_X(half), S_F P_X,F(full). 조건부 분해이지 causal species-off 실험이 아니다. Finite-grid remainder/quad error는 continuum certificate가 아니다.

남은 실제 연구: (a) source-pinned explicit schema로 아직 남은 published histories를 비교하거나 (b) PR128 이후 물리적으로 admissible 새 DAG를 선택한다. 새 heavy NCP run이나 benchmark는 이번 복구 의무가 아니며 완료된 15 HH job,76 panels,152 profiles, 63 control, warm729, long1231를 재실행하지 않는다. HH_R10=OFF, Production NOT_ISSUED. 실제 새 작업 때에는 가용 CPU/RAM을 cooperative shared admission, max64CPU/128GiB, reserve16GiB, nested thread1로 채우되 타 사용자/Codex process의 존재만으로 중단하지 않고 외부 process를 건드리지 않는다.

결과마다 DERIVED / NUMERICALLY_CHECKED / IMPLEMENTATION_VERIFIED / REPORTED / BLOCKED를 분리한다. 정확 Git source commit과 tree, 원본 archive SHA, Drive/Dropbox upload ACK와 readback 등급을 확인한 경우만 완료라고 쓴다. main merge/force push 금지. 기존 failure log와 외부 provider 미확인 상태를 보존한다.
