# Codex handoff: R31Y low-rank replay와 원본 producer intake

Repository: cosmosapjw-quantum/WU088_HH
Branch: research/r31y-lowrank-20260929
Stack base: research/r31x-subspace-witness-20260929
Pinned parent: da2742895d36c72934b11d0677b7763637ad3ebf
Parent tree: c7cda62ad6c137ae6369bcb472f7a6708a30ea76

목표는 제공된 R31Y 연구 코드의 경량 재현과, 반복해서 부재를 확인했던 축약 snapshot 밖의 원 producer artifact를 한 번 추적하는 것이다. 원래 Q의 물리적 의미가 해결되었다고 간주하지 않는다. 현재 remote HEAD/tree와 companion PUBLICATION_RECEIPT.json을 확인하고 후속 commit이 있으면 diff를 읽는다. 기존 dirty worktree, source, raw, checkpoint는 보존한다. Main merge, force push, 타 owner PID/cgroup mutation을 하지 않는다.

## 입력 및 실행

THEORY_KO.md, SOURCE_PINS.json, FILE_MANIFEST.json, lowrank.py, test_lowrank.py를 먼저 읽는다. Companion zip의 inputs/EXISTING_METRIC_INPUTS.npz는71481 bytes이며 SHA256은 아래와 같다.

565a9ee6d831f5f9e3e69010270f5319aa3328432950efcfda81cfabf325c079

기존 검증된 NCP 경로에 같은 input이 있으면 SHA 확인 후 재사용한다. 없으면 companion에서 read-only로 복원한다. 입력을 Git source 파일로 대체하거나 synthetic arrays로 채우지 않는다. PY는 확인된 /root/wu088_hh_ncp_work_v2/venv/bin/python 또는 기존 검증된 환경이다. 이번 runtime은 NumPy/SciPy/pytest만 필요하며 SymPy가 없어도 새 dependency 설치를 하지 않는다. Wolfram exact .wl은 이미 실행된 이론 증거이며 NCP에 Wolfram 설치를 요구하지 않는다.

RUN은 mktemp 등으로 새로 만든 절대 경로, SNAPSHOT은 확인된 절대 입력 경로다.

```bash
set -euo pipefail
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
export WU088_R31Y_INPUT="$SNAPSHOT"
export PYTHONPYCACHEPREFIX="$RUN/pycache"
run() {
  local name="$1"; shift
  printf '%q ' "$@" > "$RUN/$name.command"; printf '\n' >> "$RUN/$name.command"
  set +e
  "$@" > "$RUN/$name.log" 2>&1
  local rc=$?
  set -e
  printf '%s\n' "$rc" > "$RUN/$name.exit"
  return "$rc"
}
run COMPILE "$PY" -m py_compile research/r31y_lowrank/lowrank.py research/r31y_lowrank/test_lowrank.py
run TESTS "$PY" -m pytest -q -p no:cacheprovider research/r31y_lowrank/test_lowrank.py --junitxml="$RUN/TESTS.xml"
run REPLAY "$PY" research/r31y_lowrank/lowrank.py --input "$SNAPSHOT" --out "$RUN/POINT_REPLAY.json"
```

실제 collected/pass/fail/error/skip을 기록한다. 이 구현의 sandbox tests는20 PASS였으나 그 수를 맞추어 skip하거나 test를 삭제하지 않는다. 네 mode 비교에는 phase-dependent eigenvector byte identity를 cross-platform equality로 강제하지 말고 입력·코드는 byte identity, 출력은 residual/spectrum semantics를 구분한다.

## 필수 수학·구현 점검

R0=[[0,B],[B†,F]]는 명시적 보조모형이다. 실제 E=R_nn는 비영이며 원 R을 screening/symmetrization하지 않는다. Raw minus auxiliary norm과 whitened remainder를 그대로 보존한다. Exact Hermitian/SPD 가정의 inertia (2,2,45)를 float 원자료의 exact rank라고 보고하지 않는다.

Direct small K G, whitening/QR small matrix, auxiliary full eig, raw full general eig를 구분한다. Raw matrices의 Hermiticity gap, Cholesky reconstruction gap, complex eigenvalue imaginary part를 숨기지 않는다. 작은 floating norm을 certified physical enclosure라고 쓰지 않는다.

Stored Q의 retained25/complement24 sector 분해는 algebraic observation이다. Q의 원 생성 source와 물리적 채널/parity/exchange 해석은 여전히 Q_AUTHORITY_BLOCKED다. H와 dotQ 및 whole-cell contract를 검사하지 않았으므로 동역학적 sector decoupling으로 승격하지 않는다.

## 원 producer intake: 같은 축약 파일 반복검사 금지

현재 R31W/X companion만 다시 읽어서 Q/frame authority를 해결하려 하지 않는다. 기존 repo/native runtime backups 또는 connector folder listing에서 아래 exact 후보들을 한 번 찾고 그 결과를 PRODUCER_INTAKE.json으로 반환한다.

1. R31S_FULL49_z2.npz: 86445 bytes, SHA256 e8ee6796082063f04d7754e6917dafa4fc978371d3f4e0a44d64e990e5f6d8da. R31U manifest의 후보 member는 WU088_HH_R31S_NCP_20260928/evidence/z2/R31S_FULL49_z2.npz였다. 단독 array 발견만으로 Q producer authority가 닫히는 것은 아니다. 이를 생성한 script와 source identity가 필요하다.
2. WU088_HH_C21_TRANSFER_CP4_20260923.zip: SHA256 c10c932a6cdad817982e00920a893733b367827b116d058791bf5aacad517cd9.
3. R31P_OD192_z4_NODE_SEAL.zip: SHA256 1aee5abdf6bfc0993b5a32dc1a8b8f22c19b26c2ec5795064b03bd0ad860d8e2.
4. R31P_JVP192_z4_NODE_SEAL.zip: SHA256 4a57ead0b4a5f6a9462a7f42585b718a74264991ff648dc7b521d62ac1db555a.

이 이름/해시는 R31X authority 보고서의 upstream candidates다. 현재 다운로드/내용 확인된 것으로 읽지 않는다. Local existing paths를 먼저 확인하고 provider 사용 시 정확한 object ID와 size를 얻은 뒤 필요한 원본만 가져온다. Split archive라면 합성 manifest와 member order가 필요하다. Missing source를 새 native 계산으로 복구하지 않는다.

이 루프에서 Google Drive search의 기본 MIME filter는 ZIP을 제외하는 모습이 오류응답에 노출되었다. 따라서 ZIP 이름 검색의 빈 결과를 존재 부정으로 쓰지 말고 알려진 folder listing 또는 정확한 object를 읽는다. 현재 R31S redesign parent에 있는 후속 연구 packages와 original producer archive를 혼동하지 않는다.

Producer가 확보되면 Q 생성 규칙과 j_dotO 정의/단위/endpoint ordering·phase를 실제 source line/member로 연결한다. 저장된 involution의 작은 commutator는 physical authority의 대체물이 아니다. 확보 실패 시 탐색한 경로·provider·범위와 없거나 접근 불가능한 exact field를 기록한다. 새 도구 권한 문제가 아닌 원본 부재를 tool blocker로 오분류하지 않는다.

## 반환·종료와 백업

RETURN.json: reviewed/executed commit+tree, input/hash, Python/NumPy/SciPy/pytest identity, commands/exits/JUnit, 4×4 spectrum, remainder and all numerical gaps, sector spectrum, PRODUCER_INTAKE 상태, source mutation 범위와 unverified를 기록한다.

No new native/H integrals, M3A/M3B/reference preparation, 기존13/33/134 suite 재실행, z1/z0.5/full144, HH trajectory, H-skip, M5, provider/production admission. New lightweight stored linear algebra=true, native_evaluations=0, production_admitted=false, independent_review_admitted=false를 분리한다. BR01/BR02 historical gaps도 유지한다.

정상 재현이면 code를 다시 설계하지 않는다. 추가 오류가 실제 재현되는 경우만 failing test와 최소 patch를 보존한다. Non-force publication과 create-only 이중백업은 허용된다.
Drive parent: 1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM
Dropbox parent: /BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928

두 provider의 실제 ACK/object ID/size와 노출된 checksum을 detached receipt로 기록한다. 충분한 R1/R2 뒤에 중복 raw restore를 반복하지 않는다. 실제 restore 없이는 RESTORE_VERIFIED라고 하지 않는다.

Stop: 새 R31Y replay와 한 번의 targeted producer intake를 반환하면 종료. 원본이 없으면 새 원본 확보가 다음 action이지 같은 replay/authority audit의 반복이 아니다.
