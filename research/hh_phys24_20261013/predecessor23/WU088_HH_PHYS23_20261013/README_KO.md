# WU088_HH PHYS23: rate uncertainty와 유한 수신 응답

노출량 정규화 정리와 실제 rate-expression ensemble을 결합하고 고정 BASS finite segment로 전달했다. 대표 결과는 report/REPORT_KO.pdf, 정확한 유리수는 results/PHYS23_RESULT.json에 있다.

- 전자수와 냉각의 sign을 누적 HH 사건수 Q에 대해 보존: ell.V=0.03426165460392323.
- 약110.327배의 다섯 prescription hull: ΔT ∈ [-6.41018e-11,-5.55162e-13]K, Δe ∈ [7.57301e-18,9.09507e-16]perH, finite Δτ ∈ [4.48234e-25,5.38326e-23].
- 동일 gas4/photon2904, proper time0..1e11s, source/IC/geometry/closure의 exact-real 명목 모델.
- 물리적 k coverage와 실제 omission budget은 별도 입력이며, numerical receiver tolerance와 구분했다.

실행: Python202checks PASS; Wolfram50digit rate intervals; exact4x4 resolvent; xAct3 tensor +7 scalar residuals zero. 같은 assistant의 별도 계산 경로다. 새 ODE/native receiver/원자 fit/HPC0회.

재현: python checks/compute_envelope.py. mpmath가 필요하다. 원형 CAS 식은 wolfram/ 아래에 있으며 xAct는 공식 archive hash를 확인한 뒤 로드한다. 로컬 Python은 이미 기록된 CAS interval을 받아 대수적 폐쇄와 독립 고정밀 수치 대조를 한다. 보고서: cd report && xelatex -interaction=nonstopmode -halt-on-error REPORT_KO.tex (두 번).

receiver/CONTRACT_EXTRACT.json은 읽은 connector 계약의 선택 필드 전사본이며 원 full-byte 사본이 아니다. 원 source URL/revision/blob을 유지한다. inputs/PHYS22 ZIP은 원본을 그대로 보존한다.

채택 상태: DECISION.json. 다음: HANDOFF_KO.md. 원격 게시/백업은 이번 루프에서 미수행.
