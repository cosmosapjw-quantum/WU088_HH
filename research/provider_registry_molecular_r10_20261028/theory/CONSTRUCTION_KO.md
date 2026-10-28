# R4/C4 구성 선택과 실행 경로

기존 R9는 nominal K의 lag kernel과 aR+bE feedback를 함께 유효하게 다룬다. 이번 원래 HD 식에서는 -w(I-pi1^T)diag(d) 자체를 full generator로 흡수할 수 있다. 전체 fine-state box의 forcing g_r를 그대로 사용하면 bE를 제거할 수 있다. 실제 외부 반응률/consumer 입력 없이도 확인할 수 있는 새로운 수학적 구성이다.

후보 1은 R9 양의 응답의 원인별 분해다. 이 후보는 보수성 진단에 유용하지만 이번에는 후보 2인 full-generator 삼각형 폐쇄를 먼저 완성한다. 후보 2는 생성자 overlap이 약한 sparse K에서 raw 상계가 더 클 수 있다. 이 경우에도 같은 시각의 인증 R9 cap과 교차할 수 있다. Raw 결과의 우열은 실제 실행값으로 판정한다.

## 실행 DAG

Source intake와 backup/literature intake는 독립 native agents가 수행했다. 이론 constructor가 정확한 residual identity, Dobrushin Euler bridge, projected-sink 생성자 및 삼각형 식을 작성했다. 구현 author는 production core와 primary runner를 작성했고, 다른 author는 production import 없이 Decimal160 analytic reference를 작성했다. 환경 중단 후 부모가 실제 남아 있는 파일을 회수했고 새 독립 검토자가 원전·proof·code를 읽은 한 번의 R6/C9 pass를 진행 중이다. 같은 검토가 실제 출력에 이어지며 반복 review tree를 만들지 않는다.

S05에서 proof/contract/core/inputs/runners/Wolfram script와 immutable saved source를 SHA256·bytes로 고정한다. 그 뒤 primary1회→reference1회→결과해석/최종C9 순서다. 각 Python lane은60CPU초/90wall초이고 OS CPU는 subprocess 전체를 측정해 import와 serialization을 포함한다. 실제 attempt 파일은 배타적으로 생성하며 기존 run은 덮어쓰지 않는다. CAS는 새 algebra1회30wall초다. 과거 단위의 예산은0 그대로이며 ODE/native source 계산은 수행하지 않는다.

로컬 Python은 현재 작동한다. Git CLI network는 연결 실패를 보존하고 정상 GitHub connector의 expected-parent/force=false 게시를 사용한다. ZIP은 실제 게시된 source파일과7개 pinned inherited source를 포함하며 전체 Git history가 아니다. Provider ACK·metadata size와 로컬 ZIP CRC/member SHA를 기록한다. FINAL 자체의 receipt는 자기 ZIP 밖 PR150과 종료 메시지에 둔다.
