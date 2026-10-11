# PHYS09 복구 실행 독립 검토

판정: **PASS_SCOPED_RECOVERED_PHYS09_SAVED_SOURCE_PROJECTED_INTERVAL_GATE**. 구현 작성자가 아닌 검토자가 고정 소스와 보존된 실행 증거를 대조했다. 새 compiler/build/gate/consumer/과학 실행 및 설치는 모두 0회다. 요청된 모델 설정은 Astra/xhigh이며, 실제 backend 모델은 독립적으로 확인하지 못했다.

고정 science commit은 `3e409503c40a7899033126a458b1cb06b227978a`, core tree는 `afdef4725df9fdb084038d291343ac371ef96196`다. Manifest 145개 payload, 실행 전후 13개 입력, 원시 로그 8개와 복구한 실제 ELF 바이너리를 확인했다. 바이너리 SHA-256은 `09e05a8fb0a19482d361a8252e075641ab4bcb019d13bd6a1085b68c1257b653`다. 보존된 compiler/build/gate/consumer는 각각 1회, exit 0이며 기록된 한도 안이다.

기존 consumer를 호출하지 않고 표준 라이브러리 Fraction으로 저장된 50개 구간의 **전체 exact-rational 포함**을 독립 확인했다(실패 0). 원 자료에서 TSV 12,594행의 끝점 bits를 다시 대응시켜 모두 일치했다. 모든 33×3 photo Jet와 signed gradient/Hessian, 네 Neumann 항과 가중 tail, mixed forcing의 네 항 및 projected energy의 다섯 항을 보존한다. 실제 출력은 다섯 항 구간합을 포함하며 strict contraction·양의 image margin·비특이 C를 만족한다.

| stage | 실제 projected energy 구간 |
|---|---|
| full | [-6.192852956727528e-16, -2.012354998700859e-16] |
| first_half | [-7.759698274994996e-17, -2.535731601320379e-17] |

두 상계는 음수이며 direct `ell W`는 0 포함을 그대로 유지한다. 결과는 원 source inclusion과 fixed-coefficient C² family 전제 아래 같은 단위 parameter rectangle의 유한 gas-energy 상호작용에 한정된다. first_half는 같은 COMMON에서 시작하는 별도 첫 stage이며 carried second-half가 아니다.

컴파일러 hash는 실제 rustc payload가 아닌 rustup proxy다. 버전은 보존된 `rustc -vV` stdout으로 확인되지만 toolchain payload의 byte 인증은 아니다. HOST 기록에는 x86_64와 affinity만 있고 CPU 모델·성능 benchmark는 없다. Git 반환물의 설명문·identity·validation 세 파일은 원 복구 포장의 동명 파일과 다르므로 전체 포장 byte 동일성을 주장하지 않는다.

이전 검토의 outer exit124는 보존된 closeout의 전송 실패 기록이며 stderr에도 연결 종료가 남아 있다. 과학 실행의 exit 0과 분리한다. 이전 reviewer의 실제 모델과 outer exit를 독립 raw process receipt로 확인했다고 주장하지 않는다.

실제 native root/U/V/W/I는 **null**, native authority는 **false**다. carry, full/two-half defect, time/continuum remainder, full49, production/global admission과 기존 PHYS07 energy/node32 OPEN을 유지한다. 업로드 ACK·원격 byte readback·Git 게시 결과는 별도 영수증의 범위다. 구조화된 근거와 개별 구간 판정은 [DECISION.json](DECISION.json)에 있다.
