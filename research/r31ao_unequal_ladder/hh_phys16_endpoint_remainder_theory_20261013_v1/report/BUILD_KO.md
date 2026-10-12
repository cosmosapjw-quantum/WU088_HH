# LaTeX 재컴파일

이 폴더에는 19쪽 보고서의 LaTeX 원고, 필요한 Noto Serif CJK KR subset 폰트와 OFL, 벡터 그림이 들어 있다. XeLaTeX 및 통상적인 TeX Live 패키지로 컴파일한다.

```bash
xelatex -interaction=nonstopmode -halt-on-error WU088_HH_PHYS16_THEORY_20261013.tex
xelatex -interaction=nonstopmode -halt-on-error WU088_HH_PHYS16_THEORY_20261013.tex
```

기본 빌드는 포함된 subset 폰트를 그대로 사용한다. 새 한글 문자를 원고에 추가할 경우 전체 원본 폰트를 `prepare_fonts.py --font-source /path/to/full/fonts`에 제공하여 subset을 갱신한다. 폰트 원본·subset hash와 glyph coverage는 폰트 생성 기록을 참조한다. 그림의 원 구간은 `FIGURE_PROVENANCE.json` 및 frozen endpoint 결과에 연결된다. PDF QA 결과는 `qa/QA_RESULT.json`에 보존했다.
