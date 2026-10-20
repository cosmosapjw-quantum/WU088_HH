# NCP / Codex 실행 handoff

아래 본문을 실제 64코어/128 GiB NCP에서 사용할 수 있다. 게시 이후 확정된
source SHA·metadata HEAD·draft PR은 `publication/REMOTE_PUBLICATION.json`과
외부 `PHYS73_DELIVERY_20261021.json`을 먼저 읽는다. 실제 source SHA를 추측하지 않는다.

```text
WU088_HH PHYS73의 구현 완료 batch를 실행하라.
Repository: https://github.com/cosmosapjw-quantum/WU088_HH
Branch: research/hh-phys73-green-batch-20261021
과학·구현 source commit: dbf42680b9ac91c7841b17b2df8086a6b09cc705 (draft PR125).
확정 parent: PR124 HEAD 9d6d7491f26850918d6316ed466e3df35dace570.
실행 source/metadata HEAD는 PHYS73_DELIVERY_20261021.json과 publication/REMOTE_PUBLICATION.json에서 읽어 pin하라.

먼저 새 GitHub/다른 대화/백업/실제 host 실행 및 같은 request의 진행 process를 대조하라.
이전 세션은 NCP에 제출하지 않았지만 접근하지 못한 실행의 전역 부재를 뜻하지 않는다.
recovery ZIP은 full Git clone이 아니다. 별도 full checkout을 사용하라.

연구 유도·코드 구현은 완료돼 있다. NCP에서는 compiler/작은 환경 수정/실제 실행만 수행하라.
research/hh_phys73_20261021/ncp_delivery/README_KO.md와 requirements-tested.txt를 읽어
실제 interpreter에 의존성을 설치하고 rustc/gfortran을 사용하라.

repo root에서 HH_R10=OFF로 다음을 plan 후 실행하라:
python -u research/hh_phys73_20261021/implementation/ncp_batch.py --out /mnt/data/WU088_HH_PHYS73_BATCH --cpus 64 --memory-gib 128 --wall-seconds 86400 --run

현재 queue는 original-source L64/T44/N257,N513(dps60), PHYS66 longtail6,
validated L64 j37..64의 28개 chain, optional PHYS72 scalar/Fortran host reproduction이다.
source preparation 최대64×1GiB, longtail6×4GiB+validated28×2GiB 동시80GiB,
headroom16GiB 및 실제 cgroup/affinity 제한을 지켜라. BLAS/OpenMP는1thread다.

완료된 PHYS63/69/71/72와 PHYS70 L64 PR123 결과를 유지하라.
PHYS71의 76개 panels와 inherited152 profiles를 재적분하지 마라.
PHYS68 old j0..28 및 PHYS69 j29..36 enclosure는 검증 후 재사용하며 새j37..64만 계산한다.
원래 full-matrix longtail의 solver/precision/gates와 validated D1 1e-45/D2 1e-62 목표를 완화하지 마라.

B27,k7/10,E49/200,eta_C=-10/7,eta=Fy,xi=Fy-phi,HH_R10=OFF를 보존하라.
frozen NPZ SHA f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d.
D3 corrected certificate SHA f75d082e1966dd61a326c37b6ff14e8f330e010341a59a88eb4ca8d4734e6173.
양의 analytic Yukawa angular backend를 사용하고 high-j binary64 Gauss source로 되돌리지 마라.
finite-grid 진단과4.918263356868373e-53 continuum analytic component bound를 구분하라.
u(27)=0 particular를 physical matched xi로 올리지 마라. 원래 boundary trace와 origin은 별도다.

완료된 job은 runner의 hash-bound resume로 재사용하라. 실패 attempt를 지우지 마라.
컴파일·작은 환경 수정은 실제 변경/버전/hash를 남기고 새로운 과학 설계로 바꾸지 마라.
각 단계의 유도/코드/검증/과학 실행/게시/백업/DAG 상태를 따로 보고하라.
마지막 archives/PHYS73_NCP_RETURN_<invocation>.zip와 _ACK.json을 실제 SHA와 함께 반환하라.
Git merge나 외부 메시지 발송은 이 handoff에 포함하지 않는다.
```
