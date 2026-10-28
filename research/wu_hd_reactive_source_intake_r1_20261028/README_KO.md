# WU088_HH source-backed R1 checkpoint (not physical admission)
기존 REI H–Li 고정 인계에서 요청한 WU 담당 후속 노드 `WU_HD_REACTIVE_STATE_SOURCE_NEXT`의 다음 **R1 연구 위치·입력 계약**을 완료했다. 정본 H–Li PR151은 별도 브랜치로 보존하고, R16 PR150의 20/20·33/48은 재계산하지 않았다.

## 원전의 두 채널과 선택
González-Lezana et al., JCP157 214302 (2022), DOI10.1063/5.0128598은 (1) H⁺+HD→D⁺+H₂ **반응성 교환**과 (2) H⁺+HD→H⁺+HD **비탄성 여기/탈여기**를 구분한다. (1)의 상태별 수치가 보충자료에 명시돼 있지만 원본 ZIP 다운로드가 실패했다. 현재 **실제 수치값·파일 SHA·원전 행·정확한 가용 온도 노드가 없다**. 선정한 후속 단일 셀은 HD(v0,j2)→H₂(v′0,j′1), SQM; 아직 수치 인용/물리 수용 전제는 충족되지 않는다.
보충자료 원 URL: https://aipp.silverchair-cdn.com/jcp/article-supplement/2842276/zip/214302_1_epaps/ .

Lepers et al. TIQM(2019, arxiv:1902.01759)와 2020 erratum DOI10.1093/mnras/staa3146의 H₂ ortho–para 열평균 가중치(짝수 j′ 1/4, 홀수 j′ 3/4)는 별도 방법과 열평균에 귀속된다. GL2022 native SQM 상태별 자료에 자동 곱하지 않는다. EMAA HD-H⁺ 171 전이는 non-reactive HD internal rovibration이므로 이 reactive 노드의 자료로 대신할 수 없다.

## 정확한 원자·전하 장부
종 순서 (H⁺,HD,D⁺,H₂)에서 S=(-1,-1,+1,+1); 핵종 H1=(1,1,0,2), D=(0,1,1,0), 전하=(1,0,1,0)의 S와 내적은 모두 정확히0. 단위는 1cm³s⁻¹=10⁻⁶m³s⁻¹. Cross section m²/Å²는 thermal rate m³s⁻¹와 혼용 금지. WU는 microscopic Q, REC/HE/CR은 각 전파·열/에너지 소유권 구분.

## 실제 도구·실행
7개 파일의 전체 소스팩은 Drive [ZIP](https://drive.google.com/file/d/1yP1hNY4sNGXbNdMhSJdcNV4JGP31QshR/view)에 있으며 원본 GET SHA256 일치, CRC 7/7, ZIP 15413 bytes, SHA256 `282617f8b4e369c5e515db9348a8fa799acedaa69d5a629b75f504a42d27686d`; ChatGPT Library 사본도 생성됐다. 내용: 독립 standalone preflight code, 15개 pytest, 세부 R1 계약·ledger·보고서·handoff·manifest. 실제 `python3 -m pytest -q` 15/15 PASS, 처음 예상값 Decimal 정밀도 오류는 테스트만 교정; `python3 -m py_compile` PASS. Wolfram stoichiometric residual (0,0,0), spin fractions 1/4+3/4=1.
**모든 preflight 성공은 NONAUTHORITATIVE이고 production은 admitted=False만 반환한다.** Native source row independent review NOT_RUN; native subagent NOT_RUN; 이 단계의 R1 기획/계약만 완료, **요청 과학 노드와 C5/C9 완료 아님**.

## 물리 및 DAG 중단
WU R16 33/48, REI canonical 28/88, 신규 채택 0. H–Li 26 nuclear ground+5 nuclear levels, 102 formal charges, 621 MISSING/null+93 N/A는 카탈로그 표현이며 실제 rate coverage가 아니다. Native source+named REC/CR consumer/density/clock가 오기 전에는 신규 primary/reference/ODE 예산을 열지 않는다. 과거 한도 초기화 및 old R16·NCP·fresh83 반복 금지.

다음 실행: 보충 ZIP 실제 원본 bytes/sha 확보 → 정확히 한 native numeric row 원문 대조 → v/j/method/T/unit/support 및 spin 처리 동결 → named consumer commit/entrypoint, density/clock, full-A/whole-forcing qualifier 연결 → 새로운 유한 cumulative science budget 동결 → R2/C2 진행 및 독립 검토.
