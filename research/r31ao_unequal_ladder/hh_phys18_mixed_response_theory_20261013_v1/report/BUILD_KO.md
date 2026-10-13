# PHYS18 LaTeX/PDF 재현

## 동결 산출물

주 파일은 `WU088_HH_PHYS18_THEORY_20261013.tex`, 최종 PDF는 같은 basename의
PDF이며 21쪽이다. 상세 시각 검사와 최종 SHA256은 `qa/QA_RESULT.json`에 있다.
원 수치 결과의 표와 그림, 전체 62개 번호식을 담은 LaTeX, 참고문헌과 CJK
font subset을 함께 제공한다. 데이터 출처는 `DATA_AND_FIGURE_PROVENANCE.json`,
원 수식 전사 identity는 `THEORY_TRANSCRIPTION.json`을 따른다.

## 이미 제공한 LaTeX 묶음 컴파일

LaTeX source ZIP의 `latex/` 디렉터리에서 다음 순서로 실행한다.

```bash
xelatex -interaction=nonstopmode -halt-on-error WU088_HH_PHYS18_THEORY_20261013.tex
bibtex WU088_HH_PHYS18_THEORY_20261013
xelatex -interaction=nonstopmode -halt-on-error WU088_HH_PHYS18_THEORY_20261013.tex
xelatex -interaction=nonstopmode -halt-on-error WU088_HH_PHYS18_THEORY_20261013.tex
```

XeLaTeX/TeX Live, BibTeX, fontspec·amsmath·mathrsfs·graphicx 등 preamble의
패키지가 필요하다. 이미 포함된 font subset으로 컴파일할 때 전체 CJK font를
다시 받거나 prepare_fonts.py를 실행할 필요는 없다. 준비 환경은 XeTeX
2022/xdvipdfmx(20220710), Python3.12.14이다.

글자를 추가해 font subset을 다시 만들 때는 NotoSerifCJKkr의 원 regular/bold
OTF와 OFL.txt가 있는 디렉터리를 `prepare_fonts.py --font-source ORIGINAL_FONT_DIR`로
명시한다. 이 스크립트는 .tex/.bib/.bbl의 글자를 함께 모은다. 폰트 출처/라이선스와
exact SHA는 `FONT_SUBSET_MANIFEST.json` 및 `fonts/OFL.txt`에 있다.

표·그림을 다시 생성할 때는 현재 core의 frozen run02/readout01을 그대로 두고
`python3 build_report_data.py`를 실행한다. 보고서 컴파일과 그림 생성은 원
physical source, root solve 또는 history를 실행하지 않는다.

## 실제 빌드와 교정

첫 빌드는 mathscr의 패키지가 누락돼 종료됐다. `mathrsfs`를 추가했고 원 preamble과
실패 로그를 `build_attempt01/`에 보존했다. 뒤이어 XeLaTeX/BibTeX/XeLaTeX2회가
성공했다. 후속 편집에서 새 한글 글자의 font subset과 François의 precomposed
문자를 적용하여 missing glyph를 제거했다.

마지막 layout 준비 중 font-source 필수 인자를 생략한 helper 호출이 exit2로
끝났으며 `BUILD_LAYOUT_FINAL.json`에 기록했다. 원 font 디렉터리를 명시한
`BUILD_LAYOUT_RETRY.json`의 재실행으로 해결했다. 이 호출은 과학 계산을 수행하지 않는다.
최종 고립 문단 편집 뒤 XeLaTeX2회와 21쪽 렌더가 완료됐고 모든 로그 진단은 없다.
`BUILD_ORPHAN_FIX.json` 및 최종 `BUILD_LOG.txt`가 마지막 실행을 나타낸다.

PDF를 byte-identical하게 재생성하는 데는 생성 시각 등 엔진 metadata도 같아야 한다.
제공 PDF의 exact identity와 원 TeX/데이터 identity를 따로 보존했다.
