# S07 · R7/C7 — 실제 독립 reference와 CAS

새 standalone reference를 정확히1회실행했다. 691/691 PASS,51,547 component comparisons,실패0. 구성metadata11,296/exact27,094/coverage8,026/Decimal5,131. Production import/replay0이며J0/J1/J2/analyticroots/phi4독립경로를사용했다. 전체processCPU1.195646초,두과학process합4.420146초(import/serialization포함)이다.

Decimal160은intervalreference가아니다. 실행전고정1e-80relativeguard에서모든비교가PASS지만guard없는strictDecimalcontainment실패는83건이고strict=false로보존한다. 이값은물리saved-sample지표가아니며R10/R11원래readout을변경하지않는다.

새WolframCAS1회에서32/32 exact zero residuals를받았고이번반환warning0이다. Actualsubmitted3,551bytes는frozen script와byte-identical이며추가LF0이다. 이전R11/R13Power::infy/General::messages원인은여전히NOT_ESTABLISHED이며이번call로재진단하지않는다. Symboliccorroboration은fullcode/physicalproof가아니다.

R14primary/reference/CASremaining0/0/0. Workflow14/20,DAG27/44. 이후는saved-output판정/그림,독립C9,채택·전달이며과학재실행은없다.
