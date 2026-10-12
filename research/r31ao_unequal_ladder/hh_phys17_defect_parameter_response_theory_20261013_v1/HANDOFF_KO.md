# WU088_HH PHYS17 종료·재개

## 채택된 현재 위치

PHYS17의 독립 판정은 **PROMOTE_SCOPED**다. 기준 문서는
`review/INDEPENDENT_REVIEW.json`이며 SHA-256은
`6a9218a5aa13458813301614293e8c5a47b8619fc19c7cd1b6ddc2a7df08d17e`다.
같은 COMMON, 고정 admissible α, 같은 전역 λ,b∈[0,1]²와 원 C² 계열을
유지한다. 다음 설명은 이 범위를 따른다.

채택된 주 응답은 `∂λΔT∈[−1.009599125635e−8,−8.137506081166e−9] K`,
`∂bΔT∈[6.776348385589e−5,7.185335549648e−5] K`다. C² helium closure,
source 시간차 미분, 공통 stage increment, photon 일곱 항, P2 상관 전달과
P4 유한 온도식이 실제 적용에 연결되었다. 직접 forcing/상태 feedback과
유한 Neumann 오차도 채택된 동일 입력을 사용한다.

`theory/PARAMETER_COROLLARIES.json`은 다음을 함께 보존한다.

- 각 매개변수 축의 유한 단조 변화 포함.
- 등결함 곡선의 기울기 `db/dλ∈[0.0001132515805968976,0.0001489886688502190]`.
- 같은 α의 단위 직사각형에서 전체 변화 폭의 포함.
- 네 모서리 mixed contrast의 사전 포함 `|I|≤1.958485175177039e−9 K`.

원 `run02`, `forcing01`, `neumann02`, symbolic 결과와 독립 심사는 그대로
재사용한다. 원 candidate 상태 필드와 초기 실패 기록도 유지한다.

## 원자료 복원

PHYS17과 다음 두 parent 디렉터리가 같은 작업 디렉터리 아래에 오도록
배치한다.

```text
HH_PHYS17_THEORY_20261013_v1
HH_PHYS16_THEORY_20261013_v1
HH_PHYS15_THEORY_20261012_v1
```

부모 archive는
`WU088_HH_PHYS16_THEORY_20261013_RESEARCH_BUNDLE.zip`이다.
크기 **4,851,253 bytes**, SHA-256
`5899d8fac1db04536c83847b651fa3c982c72d944d5420627057dade404ceb6e`를
확인했다. 원 현지 경로는
`/workspace/scratch/b826cbaab54f/phys16_deliverables/WU088_HH_PHYS16_THEORY_20261013_RESEARCH_BUNDLE.zip`이다.
이 archive 내부의 실제 경로는 다음과 같다.

1. `HH_PHYS16_THEORY_20261013_v1/`: PHYS16 자체 결과.
2. `dependencies/WU088_HH_PHYS15_THEORY_20261013_FULL_SNAPSHOT.zip`:
   크기 **3,783,150 bytes**, SHA-256
   `3e9df6e688e8b707e50c188866e84bc7c95491e6a7bae116d6bbfc97a9e87ffe`.
3. 내부 PHYS15 ZIP의 `HH_PHYS15_THEORY_20261012_v1/INPUT_RESTORE.json`:
   3,514 bytes, SHA-256
   `e6cd1fce7e7af2352d2ab5fa6daf5686fc64671ee974e0abf39baa5be0d0e5f8`.

새 빈 작업 디렉터리에 PHYS16 ZIP을 풀고, 이어 위 `dependencies/`의
PHYS15 ZIP을 같은 위치에 풀면 두 parent 디렉터리가 생긴다. 실제 내부
목록에서 PHYS09 `PROJECTED_RESULTS.json`, PHYS11 `CARRY_RESULTS.json`,
PHYS14 `ADVANCE_RESULTS.json`과 `INPUT_RESTORE.json`이 지정한 다섯 대형
입력을 모두 확인했다. 이 전체 스냅샷을 사용하면 추가 원자물리 실행이나
대형 입력의 별도 복원은 필요하지 않다.

대형 입력을 생략한 Git 사본에서 시작할 때는 PHYS15의
`INPUT_RESTORE.json`이 지정한 원 `WU088_HH_PHYS07_NCP_LOCAL_20261011_v1.zip`
및 `src/restore_large_inputs.py`를 사용한다. 해당 스크립트의 실제 CLI는
`--archive PATH --destination-root PHYS15_ROOT`다. Archive와 선택 member의
크기·SHA를 먼저 검사하고, 누락된 다섯 파일만 생성하며 다른 기존 내용은
교체하지 않는다. 원 archive의 공급자 식별자도 `INPUT_RESTORE.json`에
있다. 이는 입력 복원이며 source·history 실행이 아니다.

## 실제 실행 명령과 재현

아래 명령은 각 성공 `PRE_RUN.json`의 배열에서 그대로 추출한 역사적
실행 명령이다. `RUN_RECORD.json`의 명령과 같고 각 exit code는 0이다.
`--output` 디렉터리가 이미 있으면 프로그램이 중단하도록 설계되어 있으므로
보존된 원 실행 폴더에 다시 실행하지 않는다. 별도 재현이 필요하면 복원한
parent 경로와 **새 output 디렉터리만** 지정한다. 후속 postprocess는 동결된
원 run02 파일을 읽으므로 해당 원 파일은 유지한다.

```bash
python3 /workspace/scratch/b826cbaab54f/HH_PHYS17_THEORY_20261013_v1/src/parameter_response_application.py --parent15 /workspace/scratch/b826cbaab54f/HH_PHYS15_THEORY_20261012_v1 --parent16 /workspace/scratch/b826cbaab54f/HH_PHYS16_THEORY_20261013_v1 --output /workspace/scratch/b826cbaab54f/HH_PHYS17_THEORY_20261013_v1/checks/application/run02/results

python3 /workspace/scratch/b826cbaab54f/HH_PHYS17_THEORY_20261013_v1/src/forcing_feedback_decomposition.py --parent15 /workspace/scratch/b826cbaab54f/HH_PHYS15_THEORY_20261012_v1 --parent16 /workspace/scratch/b826cbaab54f/HH_PHYS16_THEORY_20261013_v1 --output /workspace/scratch/b826cbaab54f/HH_PHYS17_THEORY_20261013_v1/checks/application/forcing01/results

python3 /workspace/scratch/b826cbaab54f/HH_PHYS17_THEORY_20261013_v1/src/derivative_neumann_readout.py --parent15 /workspace/scratch/b826cbaab54f/HH_PHYS15_THEORY_20261012_v1 --parent16 /workspace/scratch/b826cbaab54f/HH_PHYS16_THEORY_20261013_v1 --output /workspace/scratch/b826cbaab54f/HH_PHYS17_THEORY_20261013_v1/checks/application/neumann02/results
```

각 source와 결과의 SHA-256은 `DEPENDENCIES.json`, 각 `*_FREEZE.json` 및
결과의 `input_identities`에 연결돼 있다. PDF와 LaTeX 재컴파일 지침은
`report/BUILD_KO.md`를 따른다. 현재 연구의 공개·전달 identity는 동봉된
detached delivery receipt를 참조한다.

## 다음 실제 연구: HH_DEFECT_MIXED_RESPONSE

다음 대상은 `Wd=∂λb(g2−gF)`와 `Fλb=∂λbΔT`의 실제 포함 및 네 모서리
contrast I의 방향이다. `NEXT_DAG.json`과
`theory/NEXT_MIXED_RESPONSE_PROPOSAL_KO.md`의 M1–M16에서 시작한다.

1. 기존 PHYS09 first-half/Full과 PHYS14 actual second-half의 U,V,W,
   PHYS11/14 photon mixed carry를 원 identity와 parameter slot에 결박한다.
2. C² mixed implicit 식 M3와 상관식 M4, stage 식 M8–M13을 실제 포함한다.
   원 PHYS17의 `dλ,db,sλ,sb`와 density derivative closure를 재사용한다.
3. 동일 `C,B,q,S`, `J_F`와 양의 `Π_F`로 M15의 온도 혼합 응답에 전달한다.
4. 실제 `Fλb,I` 구간과 부호 여유를 출력하고 기존 `|I|` 포함과 비교한다.
   폭을 지배하는 source/photon/정규화 항을 실제 출력으로 특정한다.

이 다음 application은 `not_run`이다. 첫 계산은 현재 저장된 C² signed
enclosure와 mixed carry의 경량 구간 연산으로 시작한다. `heavy_queue=[]`,
`launch=false`를 유지하고 새로운 입력·실행 요구는 실제 판별 결과에
연결한다.
