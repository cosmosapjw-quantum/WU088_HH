# NCP 접속 및 B192 ABI 근거 조사

현재 복원된 문서에서는 실행 가능한 NCP SSH endpoint, 인증된 세션, 선택된 FLINT/GMP/MPFR build 반환물을 찾지 못했다. 이전 coordinator intake도 `authorized_NCP_endpoint_available=false`라고 명시한다. 초기 intake 시점의 SSH 연결·agent 환경 표지는 모두 없고 PATH에는 `ssh` 프로그램만 있었다. 동시에 진행 중인 새 workspace toolchain/bootstrap 결과는 이 과거 intake와 별도다. 이것은 조사한 자료와 현재 세션의 결과이며 전체 계정이나 실제 NCP 서버 상태의 부재를 주장하지 않는다. 현재 작업 환경의 기록은 quota 8 CPU·8 GiB이며 NCP64 성능 근거로 사용할 수 없다.

과거 64 CPU affinity 생산 환경의 정확한 경로는 `/root/wu088_hh_ncp_work_v2/venv/bin/python`, runtime `/root/WU088_R31AL_Z075_RUNTIME_20260930`다. 이 경로는 접속 주소가 아니다. 과거 `h0.so` 및 JVP `analytic.so` build identity는 있으나 오래된 C++ quadrature kernel이며 새 validated FLINT/Arb backend 증거가 아니다. 기존 handoff의 host 단계를 실행하려면 이미 인증된 실제 NCP 세션이 필요하다. 문서만으로 임의 SSH 명령이나 호스트를 구성하지 않았다.

이번에는 Dropbox의 원 R31AL ZIP 613,510 bytes를 실제로 받아 SHA256 `b3763d40cdc93f1e8d314b79b95a93b7eaf04a1cdcb98308514d5f32c022f874`를 기존 receipt와 대조했다. 381 member 중 OD/JVP 두 원 NPZ와 좁힌 metadata만 읽었다. OD는 12,862 bytes/SHA `7e7b5782cc698a364aeac608620e56c7bfdc64035ffe5dfee501608dae7970df`, JVP는 50,398 bytes/SHA `53569e92875254e897a7e23b55620cca9c5acf9f86124dc0a73198ad41d1df87`로 기존 B192 authority와 일치한다. 13개 NPY의 header, whole-member SHA와 payload SHA를 새로 결박했다. 이는 NCP 실행 없이 확보한 바이트 근거이며 원 science state를 다시 계산하지 않았다.

11개 extended-array member의 7,159개 16-byte candidate component는 x87 canonical-finite와 binary128 finite bit-pattern 검사 모두를 통과했다. 따라서 padding이나 finite 패턴만으로 serializer 형식을 유일하게 정할 수 없다. 별도로 JVP `z.npy`의 10 유효바이트가 고정 literal 3/4의 x87 little-endian offset0 표준 인코딩과 정확히 일치하고 IEEE binary128의 3/4와는 불일치했다. 이는 기록된 `--z 0.75`가 이 member에 저장되었다는 source linkage를 전제로 한 유용한 형식 구별 근거다. 일반 행렬 값을 숫자로 변환하거나 이 관찰을 ABI 승인으로 승격하지 않았다.

G2 원문은 실제 historical representation/layout 증명을 요구하며 wheel 바이트 회수를 독립된 필수 조건으로 정하지 않는다. 과거 RAW_ABI_AUTHORITY의 미확보 wheel/config 항목은 당시 남은 증거 목록이며 원 계약의 유일한 승인 방법으로 해석하지 않는다.

새로 확인한 대체 증거 경로는 `ABI_LAYOUT_EVIDENCE_CHAIN.json`에 정리했다. JVP 원 source SHA는 output IDENTITY와 PRE_OUTPUT_LOCK에 일치하며, `z=LD(z)`와 CD raw/O/dotO를 같은 `save→np.savez_compressed` 호출로 저장한다. producer native guard는 longdouble16bytes/64significand와 complex32bytes를 검사한다. 고정 NumPy2.3.5 source의 complex setter는 real slot0·imag slot1이며, np.savez 경로는 dtype과 C/F 순서를 보존한 raw bytes를 쓴다. OD도 동일한 기록된 Python/NumPy 환경에서 같은 LD/CD aliases 및 serializer를 사용한다. 이 source/log chain과 실제 `z=3/4` anchor를 수용하면 역사적 wheel이 없어도 두 exact archive에 한정한 layout authority의 독립 검토가 가능하다.

따라서 구체적인 남은 단계는 source/log provenance가 해당 두 출력의 producer 실행 근거로 충분한지 독립 심사하는 것이다. 당시 NumPy binary/config snapshot은 더 강한 보강 자료가 될 수 있지만, 이를 유일한 필수 복구물로 단정하지 않는다. 이 문서는 아직 자체 admission을 부여하지 않으며, 독립 검토가 통과하면 per-NPY SHA에 묶인 exact x87 decode를 새 산출물로 수행할 수 있다. 전체 수치 적분·역사적 machine predicate 또는 production admission은 별개의 문제다.

이 조사에서 backend build, 수치 적분, comparator, cloud write, 임의 host probe는 모두 0회다.

## 독립 검토와 실제 exact decode 후속 결과

독립 `B192_BYTE_AND_SOURCE_REVIEW.json`은 두 원 archive에 한정한 source/byte layout 추론을 통과시켰다. 추가로 원 OD의 `O_row=O.conj().T` 94개 대응 pair가 첫 component 유효10바이트 동일·둘째 component x87 sign bit만 반전함을 직접 확인해 real/imag offset16을 보강했다. 이 기록과 각 NPY SHA에 연결한 `HISTORICAL_PRODUCER_LAYOUT_REVIEWED` authority로 immutable exact decoder를 한 번 실행했다.

12개 real/complex NPY, 4,586 logical element를 float cast 없이 exact dyadic으로 저장했다. 정수 `n.npy` 한 개는 원 byte identity만 보존한다. header의 C/F 순서, raw/payload/math 해시, signed zero, padding을 별도 보존했고 z=3/4 및 O/O_row의 94개 exact conjugate-transpose 관계도 통과했다. 20초·프로세스별 1 GiB guard에서 exit0, wall 약0.166초였다. 결과는 `decoded/DECODE_RESULT.json`, scope는 `B192_DECODE_RETURN.json`에 있다.

이는 한정된 historical layout/represented-data intake의 완료이며 raw represented arrays의 exact math를 제공한다. 원 wheel byte fidelity, 적분오차, actual model-gap/eta, historical machine predicate replay, full-D certificate 및 production admission은 이 결과에 포함되지 않는다. 이전 header-only/candidate 문서는 당시 증거 상태로 그대로 보존했다.
