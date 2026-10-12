# PHYS15 이론 보고서 빌드

완성본은 `WU088_HH_PHYS15_THEORY_20261013.pdf`이며 한국어 LaTeX 원문은 같은 이름의 `.tex`에서 시작한다. 본문과 부록은 `sections_1_6.tex`, `sections_7_12.tex`, `appendix.tex`로 나뉜다. 현재 독립 판정은 `review_status.tex`, 실제 표적 검산은 `checks_status.tex`에 결박되어 있다.

이 폴더에서 다음 명령을 두 번 실행하면 목차와 상호참조가 안정화된다.

```bash
xelatex -interaction=nonstopmode -halt-on-error WU088_HH_PHYS15_THEORY_20261013.tex
xelatex -interaction=nonstopmode -halt-on-error WU088_HH_PHYS15_THEORY_20261013.tex
```

XeLaTeX, amsmath/mathtools, TikZ, hyperref 및 본문에서 로드하는 표준 TeX Live 패키지가 필요하다. 한국어 Noto Serif CJK regular/bold subset은 `fonts/`에 함께 제공되며 원 OFL을 포함한다. 기존 PHYS14 font subset을 그대로 복사하지 않고 full Noto source에서 이번 TeX 전체 문자를 수집하여 생성했다. `FONT_SUBSET_MANIFEST.json`은 사용한 full font SHA256과 subset 및 원고 대응을 기록한다.

`prepare_fonts.py --font-source /absolute/path/to/full/fonts`는 본문에 새 문자를 추가할 때 subset을 재생성한다. 제공된 완성 원문을 그대로 컴파일할 때는 추가 font 준비가 필요하지 않다.

PDF 시각 검토 기록은 `qa/QA_REPORT_KO.md`, 기계 가독 기록은 `qa/QA_RESULT.json`이다. 최종 17개 페이지와 전체 contact sheet를 확인했으며 원해상도 검토 페이지를 별도로 기록했다. `render_qa.py`는 Poppler 전체 페이지 렌더와 자동 bounds 검사를 재현한다. 보관할 최종 JPEG 렌더는 `qa/stable_pages/` 및 `qa/stable_contact_*.jpg`다.

과학적 결론, 원 source 및 검산 입력은 상위 PHYS15 연구 묶음의 `theory/`, `checks/`, `evidence/`, `review/`에 있다. 이 보고서의 빌드는 연구 source callback이나 root/history 계산을 호출하지 않는다.
