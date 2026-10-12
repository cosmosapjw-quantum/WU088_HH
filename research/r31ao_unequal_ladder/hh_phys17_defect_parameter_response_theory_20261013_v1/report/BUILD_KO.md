# PHYS17 보고서 재컴파일

이 폴더의 `WU088_HH_PHYS17_THEORY_20261013.tex`가 주 원고다. 완성 PDF는
19쪽이며 전체 유도, 실제 구간표, 직접 forcing/feedback 분해, 원전 대응,
독립 검토, 다음 mixed-response 시작식을 포함한다.

## 포함된 파일로 빌드

XeLaTeX와 BibTeX가 있는 환경에서 현재 `report/` 디렉터리를 작업
디렉터리로 사용한다. LaTeX source ZIP에서는 `latex/`가 같은 위치다.

```bash
xelatex -interaction=nonstopmode -halt-on-error WU088_HH_PHYS17_THEORY_20261013.tex
bibtex WU088_HH_PHYS17_THEORY_20261013
xelatex -interaction=nonstopmode -halt-on-error WU088_HH_PHYS17_THEORY_20261013.tex
xelatex -interaction=nonstopmode -halt-on-error WU088_HH_PHYS17_THEORY_20261013.tex
```

`fonts/`에는 원 Noto Serif CJK KR에서 현재 전체 TeX에 필요한 글자를
추출한 regular/bold OTF와 OFL 라이선스가 들어 있다. 현재 원고를 그대로
재컴파일할 때는 full font나 Python의 fontTools가 필요하지 않다. 원고에
새 한글을 추가할 때만 전체 원 font로 `prepare_fonts.py --font-source
FULL_FONT_DIRECTORY`를 실행하여 subset을 갱신한다. 본문 mono font는
DejaVu Sans Mono, 수식은 TeX 기본 수학 font를 사용한다.

수치표와 두 패널 그림은 이미 포함되어 있으므로 문서 재컴파일만으로
원 물리 계산을 다시 실행하지 않는다. `build_report_data.py`는 현재
동결된 exact rational 결과에서 표와 유한 변화 envelope 그림을 생성한
원 코드다. 그림은 같은 alpha와 다른 매개변수 고정하의 전역 도함수
구간을 적분한 외측 영역이며, 표본 trajectory나 fitting 곡선이 아니다.

## 실제 완료된 검증

`BUILD_RECORD.json`과 `BUILD_LOG.txt`는 실제 XeLaTeX 결과를 기록한다.
최종 빌드에는 누락 glyph, overfull box, 미해결 참조·인용이 없다. 짧은
증명 문단에서 underfull 경고 하나가 남으며, 실제 페이지에서 텍스트
누락·겹침·여백 이탈 없이 읽히는 것을 확인했다.

`qa/QA_RESULT.json`, `qa/QA_REPORT_KO.md`, `qa/RENDER_MANIFEST.json`은
전체 19쪽 Poppler 렌더와 시각 확인의 기록이다. 첫 전체 렌더에서 1쪽
PNG의 decode 오류가 관측되어 그 페이지만 다시 렌더했고, 최종 PNG
19개 모두 정상 decode를 확인했다. PDF 자체의 페이지·수식·글꼴은
정상이다. SHA-256은 특정 완성본의 identity이며, 날짜 metadata와 TeX
버전 차이 때문에 재컴파일 PDF의 바이트가 달라질 수 있다.
