# PHYS15 이론 보고서 PDF QA

판정: **PASS**. 완성 PDF는 **17쪽**이며 A4, 한국어 11pt XeLaTeX 문서다.

- 파일: `WU088_HH_PHYS15_THEORY_20261013.pdf`
- SHA256: `bb56b101ce91b1323cf558214d58744293e40c085d4a81067720a86613fb7515`
- 작성일: 2026-10-13 KST
- 조판 확정: 2026-10-12T15:36:51.822750+00:00

## 조판과 내용 구성

12개 본문 절과 2개 부록, 번호식 88개, 정리 7개와 명제 2개, 표 5개와 TikZ 의존관계 그림 1개를 확인했다. `kfrac`, `kwH`, `kwHe`의 완전한 반응 인수 분해와 captured threshold 동일성, 일곱 광자 sector, source bridge, 평균 Jacobian과 componentwise bound, finite temperature와 공통 adjoint, guard ledger 및 실제 Full의 성분별 photon secant를 포함한다. 독립 이론 검토의 최종 `PROMOTE_SCOPED` 판정을 반영했다.

## 실제 검토

전체 17개 페이지를 Poppler로 렌더하고 5개 contact sheet에서 페이지별 글리프, 수식, 표, 경계, 번호와 본문 흐름을 확인했다. 8·9·10·11·14·15·17쪽을 원해상도로 추가 확인했다. Remap 경계식, source 반응 계수, 평균 Jacobian과 Neumann 포함, 교정된 photon secant, DAG와 긴 참고 경로 및 hash를 집중해서 보았다.

최종 컴파일의 `Overfull hbox/vbox`, `Missing character`, 미정 reference/citation 및 LaTeX warning은 모두 0이다. PDF 텍스트의 페이지 바깥 span, 본문 가로 여백의 허용 경계를 넘는 span 및 대체 문자도 0이다. 새 full-font subset에서 요청한 source-supported 글리프의 손실은 0이고, font manifest의 TeX SHA가 완성 원고와 모두 같다.

목차 뒤의 읽기 안내를 같은 페이지에 배치하고, 긴 secant 설명을 display 식으로 정리했다. DAG의 네 출력에 각각 차이 기호를 표시했다. PDF 원문과 수학 정리의 내용은 이론 검토에서 승인된 관계를 유지한다.

## 렌더 근거

최종 보관용 표면은 `stable_pages/`의 JPEG 17개와 `stable_contact_*.jpg` 5개다. Poppler 중간 PNG 중 일부가 이 호스트에서 불완전하게 기록되어 해당 페이지만 다시 렌더했고, 최종 세트는 PyMuPDF로 독립 생성하여 atomic write와 fsync 후 저장했다. PDF 자체의 파싱, 텍스트와 페이지 수는 계속 정상이었다. 상세 정보는 `STABLE_RENDER_MANIFEST.json`, `PAGE_BOUNDS.json`, 그리고 상위 `REPORT_QA.json`에 있다.

## 확정 상태

PDF, 여섯 TeX 파일, fonts와 빌드 안내를 확정했다. 보고서 빌드는 연구 source callback, root 또는 history를 새로 실행하지 않았다.
