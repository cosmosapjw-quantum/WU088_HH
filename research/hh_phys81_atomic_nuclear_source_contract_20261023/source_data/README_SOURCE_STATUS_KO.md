# 현재 활성 입력과 역사 intake의 구분

현재 계산은 ADMITTED_FINITE_CI_REGISTRY.json(v2, SHA256 2415d357c318f1ff1307239f4f39c8009e6a7005b140c3ec67b492f631097641)과 immutable literal CSV를 사용한다. 초기 PHYS81_ATOMIC_CI_SOURCE_REGISTRY.json 및 SOURCE_INTAKE_STATUS_KO.md는 자료를 처음 확보했을 때의 기록이다. 초기 generic Li I chemical value의 isotope 귀속은 NEUTRAL_ISOTOPE_PROVENANCE.md와 verification/LI7_SOURCE_CORRECTION.json에서 교정했다. 원래 기록은 삭제하지 않았다.

활성 Li7 chemical defect는 Bushaw2007 43487.15940(18)cm^-1의 exact-SI 변환5.39172060034581eV다. 이 수정으로 source energy knots가 이동하지 않는다. He+ 최저 excited residual은2p1/2이며 internal threshold65.400419911eV, 활성 He4 upper60eV다.

Finite operator의 수학·구현 검증 및 고정 대조계 실행이 완료됐으며 full physical rate admission은 발행하지 않았다. 특히 Li7 chemical threshold→6eV 결측 구간, He author-data의 unpublished accuracy, high-energy tails와 isotope-resolved kinetics는 열린 입력 의무다.
