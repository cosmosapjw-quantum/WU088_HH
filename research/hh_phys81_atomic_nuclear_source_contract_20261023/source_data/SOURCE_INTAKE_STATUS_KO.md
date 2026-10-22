# PHYS81 원전 intake 중간 상태

기록 시각: 2026-10-22 UTC. 이 작업은 source acquisition / 원문 전사 / identity 검증만 수행한다. 기존 C22D H1 CI 실행 또는 PHYS80 kernel 검증을 재실행하지 않았다. 새로운 rate 적분·fit·활성 등록·ODE 실행은 0이다.

## 확보된 원전과 판단

| 원전 | 실제 bytes / identity | 확인된 내용 | 아직 열려 있는 사항 |
|---|---|---|---|
| Bell et al. 1983, DOI 10.1063/1.555700 | bell_nist.pdf; 2,419,989 bytes; SHA256 2427d619172a06ccf49e20af3cc0ab44a17e58262902600502786351f52261df | PDF 21/27쪽, printed p.910 Table 5 실제 픽셀에서 H I B1=-0.0186 및 B3=-0.1901. Li I reliability는 ±10%. A/B 단위 10^-13 eV² cm²; 표 confidence67%. | 표 전사 확인은 저온 물리 오차 인증이 아니다. p.894는 threshold 부근 오차가 더 크다고 명시한다. |
| Lennon et al. 1988, DOI 10.1063/1.555809 | lennon_bell1988.pdf; 5,256,441 bytes; SHA256 a45be5d8aa752c67f37746285a3770ad48c9a6210aeeac09ac989a27fd6323a7 | printed p.1325 / PDF42쪽 Sec4 실제 이미지: 수정 대상 C IV, B III, O VI. | 해당 절은 H/He/Li 계수 대체나 H B1 정오표의 근거가 아니다. 전체 학계에 별도 정오표가 없다는 주장은 하지 않는다. |
| CCC He I author archive, 13-Apr-2026 | ccc_e-He_sig.zip; 1,502,872 bytes; SHA256 d68ba39d81c8252043e12f92155c1a9ab73117b55abfd971b98d6a65c6993a85 | 900 members. 실제 README와 TICS.s1S 두 member만 추출. TICS는 one-electron total ionisation, 단위 cm². Ground state table 56 data rows, E=24.4..2000eV, 24.4/24.5eV zero, first positive24.6eV. | README는 해당2026결과 unpublished라고 명시. exact physical threshold, pointwise uncertainty, 별도 redistribution license 미기재. TICS라는 명칭만으로 잔류 He+의 내부상태별 branch를 확정할 수 없다. |
| CCC Li I author CGI, DOI 10.1103/PhysRevA.49.1066 | ccc_li_ground_tics.html; 1,618 bytes; SHA256 ac76cfef7ca94accf4004267323251cfc6c7b6a68bcd0893ef4e634ad2a91ed9 | 2s²S→continuum, cm², 13 rows, E=6..15eV. 최초 σ(6eV)=5.18148e-17cm². | Bell threshold5.39eV..firstsample6eV gap, upper15eV tail가 남는다. 전표본만의 finite contribution과 full Maxwellian rate를 구분해야 한다. |
| Zapesochnyi–Aleksakhin 1969, Sov.Phys.JETP28,41–45 | zapesochnyi_aleksakhin1969.pdf; 708,577 bytes; SHA256 b9932a8413cd8b4f8a7e428a5da536fb8dcd55150c5a63c0747cf960d4742408 | threshold..30eV alkali single-ionization 원실험. 실제 p44표 Li I=5.39eV, apparentlinearinterval3.4eV, slope mantissa0.9×10^-16. | 당시 beam energyspread0.1eV(90%), energyaxis uncertainty0.1–0.2eV, absolute±15%, rms±12%, threshold relative≤3%. 이 증거만으로 훨씬 작은 excess-energy 영역의 정밀도를 인증하지 않는다. 원문 slope 단위 인쇄 glyph는 별도로 보존한다. |
| NIFS-DATA-059, 2000 | nifs_data059.pdf; 2,457,084 bytes; SHA2565721807484723d646fd259edca10269dbe8ac6e2a9bff5023ccbba2d66aa0998 | Author/institute primary report 실제PDF확보. Page3(p2) 원문은 ground He ionization이 실험자료에 기반하며 다른 excited states에는 CCC를 사용한다고 명시. | scanned PDF로 내장 text없음. 식/표에 대한 추가 시각검토 중. |

## Table 5 원전 전사

숫자는 표의 mantissa이며 A와 B의 공통 단위는 10^-13 eV² cm²이다. 빈 셀은 원전에서 빈 셀로 보존한다. 코드의 zero-padding 결정과 구분한다.

| Species | I/eV | A | B1 | B2 | B3 | B4 | B5 | Reliability |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| H I | 13.60 | 0.1845 | -0.0186 | 0.1231 | -0.1901 | 0.9527 | blank | ±7% |
| He I | 24.60 | 0.5720 | -0.3440 | -0.5230 | 3.4450 | -6.8210 | 5.5780 | ±5% |
| He II | 54.42 | 0.1845 | 0.0887 | 0.1315 | 0.3877 | -1.0910 | 1.3541 | ±10% |
| Li I | 5.39 | 0.0854 | -0.0040 | 0.7573 | -0.1779 | blank | blank | ±10% |
| Li II | 75.64 | 0.7220 | -0.1492 | -1.3007 | 1.9443 | blank | blank | ±12% |
| Li III | 122.45 | 0.4000 | blank | blank | blank | blank | blank | ±10% |

Haque2006의 -0.00186은 PHYS80이 기록한 후대 전사이며 이번에는 원본1983픽셀과 일치하지 않음을 확인했다. 원전1983값의 전사 분쟁은 resolved-to-original로 표시할 수 있다. 후대 저자가 의도한 수정인지의 별도 증거는 아직 확보하지 못했다.

## 실제 도구 사용 및 접근 범위

- Exa actual search5회, fetch1회 결과는 PRIMARY_SEARCH_RAW_001.json 및002.json, NIST_CHANNEL_SEARCH_RAW.json 및002.json에 보존했다.
- SciSpace actual search1회, returned10papers; search question, unique IDs, DOI, 제외 사유는 SCISPACE_USAGE_RECEIPT.json. 반환된 다른 시스템의 정오표를 Bell 정오표로 취급하지 않았다.
- Default sandbox의 네트워크 OPERATION_NOT_PERMITTED와 approved public-read 성공을 구분해 PRIMARY_FETCH_ATTEMPT_001..005.json에 기록했다. ADS/AIP403은 별도 기록. 우회 로그인·credential 사용은 없었다.
- 첨부18-literatures.zip7members와19-papers.zip8members를 안전하게 나열했다. 19-papers의8개PDF는 메모리상 첫쪽/metadata만 읽어 GR/CMB 문헌임을 확인했다. blanket extraction 없음. 비공개 대화는 접근·전수확인하지 않았다.
- remote_inventory가 확인한 bass_cr PR96 / ba39fc75521aa18705ec832d789e50dd5c6565bc의 C22D H1-only CI 결과는 이미 완료된 identity로 존중하며 다시 구현하거나 실행하지 않았다.

## 안정 원전 URL

- https://srd.nist.gov/jpcrdreprint/1.555700.pdf
- https://srd.nist.gov/jpcrdreprint/1.555809.pdf
- https://atom.curtin.edu.au/ccc-db/index.html
- https://atom.curtin.edu.au/CCC-DB/He/I/ELECTRON_IMPACT/e-He_sig.zip
- https://atom.curtin.edu.au/cgi-bin/c4nick.in?element=Li&charge=I&process=ELECTRON_IMPACT&low=2s_dSz2szX2YS&upp=tics_TICSzticszTICS&data_type=cross&cs_unit=cm2
- https://jetp.ras.ru/cgi-bin/dn/e_028_01_0041.pdf
- https://nifs-repository.repo.nii.ac.jp/records/2000098
- https://nifs-repository.repo.nii.ac.jp/record/2000098/files/NIFS-DATA-059.pdf

Public accessibility는 논문 전체의 재배포허가와 같지 않다. 이 intake는 원문 identity와 수치자료 provenance를 보존하며, 출판·재배포 license를 새로 주장하지 않는다.

## 최종 추가: finite CI window의 ground-product 에너지 근거

NIST ASD5.12 실제 HTML을 2026-10-22에 확보했다. 수치는 handbook의 과거 반올림값 대신 현재 ASD의 eV 출력에서 직접 읽었다. 아래 합계는 원전 수치의 단순 덧셈이며 모델 실행이 아니다. 상세 provenance/uncertainty/URL/SHA는 NIST_GROUND_PRODUCT_WINDOW_EVIDENCE.json에 보존했다.

| 종 | 중성 ground ionization I | 잔류이온 최저 들뜬준위 ΔE | I+ΔE | 검토하는 finite incident window |
|---|---:|---:|---:|---:|
| He I → He II | 24.587389011eV | 2p²P°1/2, 40.8130309000eV | 약65.400420eV | 24.6–60eV |
| Li I → Li II | 5.391714996eV | 1s2s³S1, 59.020708eV | 약64.412423eV | 6–15eV |

초기 ground-state 중성 원자와 단일 입사 전자의 충돌이라는 조건 아래, 두 창 모두 잔류이온을 들뜨게 만드는 내부 에너지 문턱보다 낮다. 반동은 이 내부 에너지 하한을 낮추지 않는다. 따라서 해당 창에 제한된 단일 이온화 반응의 residual ion ground-state energy map을 닫을 수 있다. 이것은 source window 밖의 Maxwellian 기여, neutral excitation의 열수지, photon-assisted 반응을 닫지 않는다.

He II의 실제 최저 n=2 준위는 2p J=1/2이며 2s보다 조금 낮다. NIST He II 표는 4He, Li II bound-level 표는 7Li를 명시한다. 따라서 이 자료를 He3/Li6에 정확한 동위원소별 입력이라고 부르지 않는다. Li II uncertainty는 ionization limit으로부터의 분리값에 대한 오차라는 원전 주석도 보존했다.

## 최종 추가: NIFS He I 권장 계수 전사

NIFS-DATA-059 Eq9(PDF6쪽, printed p5)와 TableIV(PDF15쪽, printed p14)를 실제 픽셀로 확인했다. ground He I 계수 A1..A6는 [0.5857, -0.4457, +0.7680, -2.521, +3.317, 0]이며 식의 공통 prefactor는 10^-13/(I E)이다. Bell과 같은 식 계열이므로 향후 비교 입력으로 재사용 가능하다. 빠른 OCR이 A3 앞에 잘못 붙인 minus를 이미지에서 바로잡았다. 이 전사는 NIFS059_GROUND_HE_VISUAL_TRANSCRIPT.json에 있으며 활성화·rate평가를 수행하지 않았다. 이 보고서의 ground-state fit은 Shah et al.1988 J.Phys.B21,2756 실험과 CCC89를 기반으로 한다.

문헌조사 범위는 여기서 닫는다. 새 source evidence의 저장·정리와 source-data literal 전사만 수행했고, 신규 수치 rate fit/integration, scientific IVP/ODE, 기존 완료 identity 재실행은 모두0이다. 출판할 때는 작은 수치 전사+attribution+source hash/URL을 사용하며, 원문 PDF 전체의 repository 재배포허가를 주장하지 않는다.

## H1 단회 조회와 최종 standalone 전달물

Root의 추가 요청에 따라 NIST H I levels를 정확히1회 새로 조회했다. 같은 표의 ionization Limit=(13.598434599702)eV, uncertainty=0.000000000012eV, reference HDEL을 확보했다. C22D raw H curve의 첫 에너지13.6058000eV는 그대로 보존한다. NIST chemical I와 numerical source-window boundary를 같은 값으로 바꾸지 않는다.

PHYS81_ATOMIC_CI_SOURCE_REGISTRY.json은 H1/He4/Li7의 branch, chemical I, source identity, 입력 단위, finite window, full-rate uncertainty OPEN을 분리한다. PHYS81_CI_FINITE_WINDOW_LITERAL_DATA.csv에는 H87행/He27행/Li13행의 원 숫자를 전사했다. H 입력 단위 a0²와 He/Li 입력 단위 cm²를 각 행에 명시했고 이 intake에서는 단위 환산을 수행하지 않았다. H의 기존 source SHA가 remote_inventory의 C22D receipt와 일치하는지 확인해 복사·재사용했다. 24.4/24.5eV의 He zero samples를 physical threshold라고 부르지 않으며 finite candidate window는 firstpositive24.6eV에서 시작한다.

전체 원본은 연구 출처 검토용으로 이 intake 경로에 남아 있고, Git 게시용으로는 작은 숫자 전사와 provenance 파일만 선택할 수 있다.
