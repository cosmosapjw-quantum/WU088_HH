# PHYS81 다음 스레드 / Codex 인계

## 실행 완료 identity

Repository: https://github.com/cosmosapjw-quantum/WU088_HH
Draft PR137: https://github.com/cosmosapjw-quantum/WU088_HH/pull/137
Branch: research/hh-phys81-atomic-nuclear-source-contract-20261023
실제 부모 PHYS80 final HEAD: 951182dd59bbb59dba454bbaab78ad56d029355a
S1 code/verification commit: a27bc238eaafb06dbde5f96b5b4f896d2bc5c811
S2 과학 commit: 5745e61be8c8e676c42d48543c8126bc20e717f8
S2 root tree: 42e7f75591467e7ad219c9549c14954bcd1b5895

최종 metadata HEAD와 final ZIP/JSON의 provider IDs 및 SHA256는 **PR137 최종 본문과 외부 PHYS81_FINAL_DELIVERY_20261023.json**에서 읽어 actual refs와 대조한다. 이 Git 파일에 자기 자신의 미래 commit/hash를 미리 넣지 않는다. S0/S1/S2 ZIP은 checkpoint ACK 범위이고 최종 ZIP의 전체 remote-byte/CRC/payloadSHA restore 증거는 외부 영수증으로 마감한다.

필수 읽기: FINAL_REPORT_KO.md, DAG_OVERLAY.json, EXECUTION_LEDGER.json, CONTRACT.json, RESEARCH_LOOP_MAP_KO.md, POST_PUBLICATION_HANDOFF_KO.md, delivery/SCIENCE_PAYLOAD_MANIFEST.json, delivery/FINAL_REFERENCE_DELTA.json, 외부 final-delivery JSON.

## 완료 / 재실행 금지

- PHYS81 새 ODE3=완료3+실패0. 기본/정련3-state Radau, 독립 raw7 DOP853.
- 기본/정련 max state3.266791559486393e-10, raw7/정련7.286526937377857e-11; 사전gate1e-7 PASS.
- 실제 resume3verifiedskips/0ODE.
- 원자15logicalgroups PASS, 핵663assertions(15kinematicinputs/45partitions 등)PASS.
- 27finite profiles+27newBell64+27Bell-windowintegrals 완료.3종PNG/PDF.
- Science88files entriesSHA256: b351b1fcce1274ea023ff9a3d333b3da50e05b13468481ce8aafd040273d34f9.
- PHYS78/79/80, HH1231/REI729/HH74control63, C22D/C22E, REI localflows, REC124/125, HE34/35 및 새HE36/ANGULAR01의 완료identity를 다시 실행하지 않는다.
- NCP0, benchmark0, 새cosmologicalODE0, 다른process종료0. HH_R10=OFF. Production admission NOT_ISSUED.

## 현재 물리 계약

Non-tilted LRS Bianchi I 부모; 같은 normal orthonormal frame의 signed matter/radiation tensor를 합한 후 norm. Frobenius=sqrt(2)*half-contraction. reacting gas pi=0, collisionlessDM pi_m 별도.

새 대조계는 고정밀도 H1/He4/Li7 finite CI-only common-T/stationary-target operator다. H13.6058–968.61,He24.6–60,Li6–15eV; 구간밖0은모델정의다. T범위255–50000K는수치operator범위이며fullphysicalrate인정이아니다. Li7chemical I=5.39172060034581eV(43487.15940(18)cm^-1 원전), sourceaxis는유지.

7→3은정확한연속좌표환원이고QSS가아니다. 새T0=25370.66308424773K,nref=1e-3cm^-3,tend=1e14s,최종T=25266.558216164776K. 에너지첫적분의잔차는독립정확도증명이아니며원래7상태/정련비교는sampled근거다. Radau3 nfev386/1156, DOP8537 nfev89: speedupbenchmark로해석하지않는다.

핵3coldCOMcapture는photon/recoil과explicitζ저장소합0을검증했다. ζ는thermalpopulation/fastparticlecount를지정하지않는다. Nuclear rate/finiteT/normal-framephoton/stopping은OPEN이다.

## 최신 donor delta와 다음 순서

마지막boundedrefresh는2026-10-22 23:30–23:32UTC다. REI221 최신73c5e00cac26b4efc782446975bd6b6762555997, REC125 최신b28b387fecd6cc71fddb98e95f336eba5f8a647f는metadata-only이동이다.

새REC127 ANGULAR01:5185c396b7e07076565ca2f5044a5ccd193e6ee1.405rows완료,0cosmologicalIVP. Q는escape-probabilityPSTF이고photonstress가아니다. Resolved-linepopulation/Einstein/degeneracy 및number/energyinjection은OPEN이다.
새HE89 HE36:6403055c3d574ec0bd1ece80147f9711315902e7.129finiteHtemperature rows/6Cartesiancontrols/7bridgegroups/0newIVP;5pairedbatchingtrials는기존별도benchmark다. All-thermal21state/common-bulkcentraltensor조건의bridge를재사용하고unresolveddEfast/thermal-numberownership을해결하기전PHYS81ζ를자동연결하지않는다. Gaspi0유지.

1. 실제현재refs와외부최종backupidentity를읽고변한의존성만대조한다. 접근불가비공개대화전수확인주장을하지않는다.
2. LOW_T_CI_SOURCE_COVERAGE: Li7threshold→6eV source와uncertainty를먼저닫는다. Bell비교에서255Kwindowfraction4.255644038244163e-11은모델의존진단이다.
3. Bound-boundCE/radiativecooling 및He/LiCX의state/photon/energy계약을원전으로닫고새sourceidentity만구현한다.
4. 핵finite-T 사건 평균,thermal/fastparticlecount와energyownership을닫아HE36의기존bridge에연결한다. Nuclear rates/stopping은그후다.
5. D_PI_RR_MATCHED_SOURCE_MOMENTS, RECOMBINATION_TO_Z20_INITIAL_CHARGE_CONTRACT, LI_HARD_UV_INNER_SHELL_SPECTRAL_CONTRACT, FULL_GEOMETRY_SPECTRAL_BACKREACTION은유지한다.

## 실행 운용

Shared lease protocol:/tmp/rei-bianchi-cooperative-leases. worker1/thread1,0.5GiB요청 및headroom확인. source/leased_call.py를사용하고다른process를종료하지않는다. 새수치작업의contract/sourcehash/identity를먼저고정한다. 기존main실행명령을그대로재실행하지않는다. 폐쇄된결과는manifest/영수증으로재사용한다.

현재과학source의경로는unit상대적이며runtime은Python3.12.14,NumPy2.3.5,SciPy1.17.0이다. 다른runtime의resume는identity불일치를거부한다. Nuclear 독립검증script는실제로실행했던원본absolutefixture경로를보존했으며해당fixturebytes는verification/nuclear/inputs에포함했다. 그완료test를자동재실행하지않는다. 새로운audit이필요하면fixture경로변경을새verificationidentity로명시한다.

각단계의유도/구현/검증/과학실행/게시/백업/DAG상태를분리한다. 전체목표에는고정분모가없어임의%를쓰지않는다. 실제remote후손additiveDraftPR,두handoff와finaldelivery영수증으로마감한다.

Runtime 업데이트만으로 완료된 과학 실험을 반복하지 않는다. 새 물리 의존성 또는 명시적인 새 수치 검증 질문이 있을 때만 별도 계획을 세운다.
