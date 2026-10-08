# WU088_HH FD1 첫 box 진단 준비 반환

상태: READY_FOR_EXACT_DIAGNOSTIC_AUTHORIZATION. HH 평가 0회, 적분 0회, science dispatch 0회. 기존 수락 24/289와 누락 265 unbounded를 유지했다. epsilon_C/R=null, B22=OPEN_UNDETERMINED, scientific/production admission=false다. 최초 HH callback의 nonfinite 원인은 아직 관측하지 않았다.

원격 successor 290d83a8d1ae2f22dcded3e40574a850eda1410a의 START_PROMPT와 지정 상세 prompt를 실제로 읽었다. 상세 prompt 7884 bytes/SHA256 23d414ceba6555eadc5f340279679c318962cf9c60685b8ca59214cc1cc827fa, 검토 ZIP 5255001 bytes/SHA256 4f3673e48c97663101cb8cd644bc7c7e889727baa383d58305c2a4c246485471를 확인했다. 양 provider metadata를 대조하고 Dropbox에서 artifact당 한 번 다운로드했다. 검토 ZIP 165 payload와 CRC/manifest를 검증했다. 원 pilot ZIP은 기존 검증된 local bytes를 재사용했다. 사용자 재업로드와 provider 중복 다운로드는 없었다.

최종 workspace는 /root/WU088_NCP_EXEC_20261003_v2/fd1_prep_20261003_v3다. 원 numeric source, signed ordered107, precision128, frozen input/geometry/margin과 기존 성공 backend/worker/compiler flags를 보존하고 별도 sidecar만 compile/link했다. FLINT3.4.0/GMP/MPFR 및 system-library linkage는 기존 worker와 일치한다. 적분 translation unit은 연결하지 않았고 dynamic symbols에 acb_calc_integrate 참조가 없다. compiler exit0, 경고0이다.

Q272와 Q000의 outer arb dump는 원 failure_samples[0]의 real `-f -1 30000001 -1d`, imag `0 0 0 0`을 그대로 사용한다. 첫 inner box는 고정 FLINT quad_simple 산술로 만들고 원 log_map을 통해 물리 box를 기술했다. 두 geometry description은 field callback이 아니다. 원 margin 1/536870912와 원 signed107 순서를 입력 파싱으로 대조했다. 실제 HH 호출은 없었다.

최종 source에 대해 fresh/stale/duplicate/uncharged recorder, 범위 밖 query와 잘못된 hash, raw/source/binary/logbox/coefficient 및 관측 binding 변경, 누락 승인·중복 campaign 거절 등 18개 고유 검사가 통과했다. 기존 40개 검사나 검토 queue 실험을 새 검사로 세거나 재실행하지 않았다. 최종 live gate는 실제 전용 unit의 memory.max=34359738368, cpu.max=400000 100000, affinity64, 조상 quota/사용량/6GiB 여유, capabilities0, NoNewPrivs1, UID0와 private read-only cgroup view에서 통과했다. UID0 경로를 별도 비root UID 검증으로 부르지 않는다. 미래 unit 전체 wall60초와 query당10초/1024MiB 제한을 proposal에 결속했다. 향후 승인 직전에는 다시 실제 PID·namespace·자원·loader를 검사한다.

FD1 v1의 /proc/1/root 조상 읽기 EACCES와 v2의 /proc/1/ns/mnt capabilities0 EACCES, 초기 성공 sidecar 및 모든 로그는 그대로 보존했다. 최종 v3는 작업 private namespace 안에서 host cgroup view를 read-only bind하고 fresh outside/inside PID·namespace 소속을 대조한다. 시스템 전역 mount·계정·패키지는 변경하지 않았다. 소스가 바뀐 준비 continuation만 새 prefix에서 수행했으며 원 backend/worker 재빌드는 0회다. 현재 검사수에는 이전 준비 검사를 합산하지 않았다.

보호된 기존 파일/링크 73949개에 대해 bytes/SHA/mode/mtime/target 변화가 없었다. 소비된 6셀 registry, RUN_STARTED/EXECUTION_BINDING/raw/RETURN, 원 PREPARED와 실패 backend tree, B22 claim을 보존했다. claim 존재만으로 process/race 원인을 추론하지 않았다. R31AK frozen, z0.75 holdout, B128/B160 consumed, B192 reuse를 유지했다. Bianchi/rei_bianchi 및 다른 원자 repo는 변경하지 않았다.

최종 proposal self SHA256: `4f121182611c1609145728cbddfc5c346fdbbdf9c8424527b25534f282ad37be`
proposal file SHA256: `73993d5f8b642874c521e646847c1f68fa604b4e15e0b641bea5f5e87241c79b`
query scope SHA256: `20ff5d09ea36b1a87489ea80961bb692161ff881fa4075c71637b81afc9cfc51`
sidecar source SHA256: `8850d822137bbe18109457349713682a1e8ae386d8553bb82c7f76630e327056`
sidecar build self SHA256: `a65848adb48217b46499b400dfbce5775a912dfa0045c185b54cd8a35706bb79`

제안 후보는 Q272_cached, Q272_reference, Q000_cached, Q000_reference 각각1회, 총4 field callback, 적분0회, 단일worker이며 자동 retry가 없다. diagnostic registry와 output은 absent다. 이번 준비 요청이나 기존 6셀 승인은 이 후보의 과학 승인이 아니다. 실제 future run/consume/HH 경로는 시험 호출하지 않았다. 다음 최소 조치는 이 exact proposal과 고정4회·예산에 대한 별도 명시적 사용자 승인이다. 이후 결과가 불충분하면 UNRESOLVED로 멈추며 적분·다른 box·coverage를 추가하지 않는다.

같은 research branch의 additive/non-force publication 및 Drive/Dropbox create-only 결과 ZIP/보고서 백업은 별도 DELIVERY_RECEIPT에 실제 ACK/object/metadata와 최종 commit을 기록한다. 출력 검증 tier는 ACK+metadata이며 실제 다운로드 검증이 없는 출력의 RESTORE_VERIFIED는 false다. 입력 Dropbox object의 RESTORE_VERIFIED와 구분한다.
