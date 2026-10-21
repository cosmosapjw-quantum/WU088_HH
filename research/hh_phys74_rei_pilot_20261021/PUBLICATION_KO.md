# PHYS74: REI Sigma–Pi pilot용 source-pinned HH-side 기여

## 실제 결과와 범위

과학 source: `56db9f2db0746bf571665ef7ac8e216a9df8c3d8`.
실제 parent: PR126 `367db1f18ed9e6ad5cd680e3dbd2a37ecdb0f049`.
원 solver: rei_bianchi PR147 `3b85dedce84d37b3e165da00685a8a984950aafe`.

2026-10-21 sandbox에서 새 63개 non-tilted LRS Bianchi I control histories를 실제 계산했다. zbar20→4,81samples/history,5103samples,nfev7998,peak4workers. Original CanonicalFVSpecies Einstein–gamma/nu hierarchy 및 massive canonical-momentum Vlasov가 authority다. H/He chemistry·ionizing source·electron Thomson coupling은 이 대조군에 없다. generic Bianchi I 전체 또는 full reionization pilot이 아니다. HH_R10=OFF.

초기 signed Sigma magnitudes 0,0.0005,0.001,0.002,0.004와 signed Pi magnitudes 0,0.00025,0.0005,0.001의 양/음 부호를 사용하고 zero duplicates를 제거하여9×7=63case다. Fixed massive fraction0.1,A_m0=0,m/Tref30,ell8,radial24/angular12/Gauss3,원 DOP853 rtol3e-11/atol3e-13를 유지했다. 완료63case resume는63재사용/새실행0이다.

|실측 진단|값|
|---|---:|
|initial coordinate max abs error|1.734723475976807e-18|
|massless N0 number error|0|
|algebraic H constraint relative|2.220446049250313e-16|
|minimum massive cell number|1.491026203638869e-30|
|maximum final Sigma_F|6.996285214159669e-4|
|maximum final Pi_F|2.4053697160612432e-4|
|signed final shear reversals|12|

H constraint는 algebraically computed H의 일관성이지 독립 continuum certificate가 아니다. 모든 수치는 이번 finite control grid에 한정한다. 상세 benchmark0, 측정 speedup 주장없음, NCP launch0, 완료된 HH historical job/panel/profile 재실행0.

## 물리 사상과 유도

공통 normal orthonormal frame, signature(-,+,+,+),
`ds²=-c²dt²+a²exp(-2b)(dx²+dy²)+a²exp(4b)dz²`, `H=dot a/a`, `s=dot b`다.

`σ=diag(-s,-s,2s)`, `π=diag(-p,-p,2p)`, `p=sum_species pi_s`, `pi_s=(P_parallel-P_perp)/3`이므로

- `σ:σ=6s²`, `π:π=6p²`, `σ:π=6sp`.
- `Σ_F=sqrt(6)|s|/H`, `Π_F=(8πG/c²)sqrt(6)|p|/H²`.
- H와sigma는 proper-time s^-1, 압력은J/m³다. `κ_t=8πG/c²=c²κ_E`, `κ_E=8πG/c⁴`, `H_geom=H/c`를 쓰면 기하학적 정의와 동치다.
- Legacy half-contraction norm은 각 full norm보다sqrt2 작다. 다른 thread의norm이틀렸다고자동판정하지말고명시변환한다.
- DeltaP를 반환하는owner는pi_s=DeltaP/3로 변환해야한다. 종별signedtensors를먼저더한뒤norm을취한다.

부호좌표 `S=sqrt(6)s/H`, `P=κ_t sqrt(6)p/H²`를 유지하면 work=`κ_t σ:π/H³=SP=ΣΠcos(theta)`다. 한norm이0이면alignment는정의되지않는다. 일반STF tensor에는Cauchy–Schwarz가적용되며tensor_adapter.py가벡터화된3×3diagnostics를지원한다. Evolution은여전히LRS다.

원shear식 `dot s=-3Hs+κ_t p`, `N=ln(a/a_ref)`에서 `dS/dN=-(3+dot H/H²)S+P`다. 따라서magnitude만으로는부호반전과응력상쇄를구별하지못한다.

초기조건은`H_actual²=Href²+s0²`이므로` s0/Href=S0/sqrt(6-S0²)`다. `|S0|<sqrt6`에서원입력`Sigma_half=|S0|/sqrt2`,orientation=signS0로정확히보낸다. Gamma/nu의공통P2coefficient k에대해`p_rad0=rho_crit Omega_r a_ref^-4 k/15`이며실제massivequadrature의p_m0를포함해
`k=[P0 H_actual²/(sqrt6 κ_t)-p_m0]/[rho_crit Omega_r/(15a_ref⁴)]`
를선택한다. |k|≤0.5를검사하고clipping하지않는다. 초기angularbrightness`1+kP2≥0.5`다. 이것은fixedspeciescomposition의한2Dslice이며모든stressdistribution의유일한역복원이아니다.

## 구현과 최소 확인

`bridge.py`는원constructor의불변Legendre연산자·canonicalmomentumpacket을worker당1회준비하고read-only공유한다. 초기상태·caseparameters·nfev는독립이다. 원class methods를변경하거나monkeypatch하지않는다. 같은equations,solver,tolerances,quadrature다. 온도표·nativeintegrator교체·tolerance완화는하지않았다.

`tensor_adapter.py`는종별signedSTF합산후fullnorm/work/alignment를vectorize한다. `lrs_tensors`는stress_representation='pi_s'또는'delta_p'의명시입력을요구한다. 5103저장sample에서scalar대비maxabs차이는Sigma0,Pi4.336808689942018e-19,work1.6940658945086007e-21이다. 통합재실행없음.

실제uniquechecks는8bridge+4resource+2tensor=14다. Original/cached constructor의RHS와17nodehistory가bit-identical이었다. Bridge suite가두번실행되어작은paritytrajectories는총4개이며테스트수를중복합산하지않는다. Wolfram은contractions6s²,6p²,6sp와ICinverse residual0을확인했다. Native independent subagent는NOT_RUN이며동일실행자의자체검토를독립review로부르지않는다.

최초scaffold importfailure는behavioralTDDred가아니다. 최초figurePermissionError는새figures폴더권한만수정했고과학data/source는변경하지않았다. 실패와성공로그모두FULLarchive에보존했다.

## 64CPU/128GiB 공유 실행

`resources.py`는Linuxaffinity/cgroupancestorCPU·memory,MemAvailable과sampledbusyCPU,공동lease를새admission마다확인한다. Defaultceilings64CPU/128GiB,reserve16GiB,case1GiB,BLAS/OpenMP1. 다른Codex/process이름은veto가아니고foreignsignal은없다. 동일output의중복만lock으로막는다. Zero-capacity에서는새admission을queue하고기존작업은계속한다. 명시wait가끝나면pending을보존한다.

Sharedlease는같은directory를쓰는cooperatinglaunchers의advisory예약이며non-cooperatingfutureload까지보장하는OS격리가아니다. NCP64speedup은측정하지않았다. 현재63case를NCP이식명목으로재실행하지마라.

## 조사와 재사용

이번intake에서REI253/HH135branchnames를paginate하고관련7repos의최신PR·선택source·backup·대화를대조했다. 모든branch의모든파일을전수재감사했다는뜻은아니다. PR126후속원문은PHYS73raw인수를이미닫았고이번에도원ZIP/ACK및4681payload를읽기전용검증했다.15jobs재실행0.

RUN19/BRPERF01의preparedcoefficient/pool,CR89exactepochreuse,BASSS12rayfusion은같은owner계약아래재사용후보다. 이번실제실행에는PR147owner만사용했다. VigilODEreflecting-grid상수나경계를이식하지않았다. HE/REC/V14/age의완료결과와기존HOLD를유지한다.

다른대화의625/81case완료와C15coupled512rows는보고로확인했지만이PHYS74에서원시case를입수하지않았다.63과합산하거나독립확증이라고부르지않는다. 특히half/fullnorm과DeltaP/pi_s를변환한뒤source·frame·IC·closure를대조해야한다. 다음우선작업은기존결합owner결과수집·정규화·중복제거·그림통합이지추가collisionlesssweep이아니다.

## 원전과 실제 이식 범위

Python concurrent.futures https://docs.python.org/3/library/concurrent.futures.html
NumPy read-only sharing https://numpy.org/doc/stable/reference/thread_safety.html
Linux cgroup v2 https://docs.kernel.org/admin-guide/cgroup-v2.html
Lee–Nungesser–Tod arXiv:1911.04937 https://arxiv.org/abs/1911.04937 는masslesssmall-anisotropy문헌배경이며이massive+Lambda finitegrid의continuum증명을대신하지않는다.

## FULL recovery 및 단계 기록

파일: `PHYS74_REI_PILOT_FULL_20261021.zip`,1453025bytes.
SHA256 `8119cc2457a53252dec9c54e3e84871e6b45e9de4030418c5f9ae05ab424cdca`.
115manifestpayloads/116ZIPmembers,fullGitclone아님.
Drive: https://drive.google.com/file/d/14aMjaIIalmHheWsMFAtuQ4Tvsx0RBMT5/view
Dropbox: `/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/PHYS74_REI_PILOT_FULL_20261021.zip`, id:BSpOijBcT10AAAAAAD_fUA.
Drive재다운로드전체바이트및115payload검증완료. Dropbox완료응답·크기·contenthash일치이며raw재다운로드검증으로승격하지않는다.

Archive의package에는11source,원donor8files,63rawhistories,3PNG,CSV,THEORY_KO.md,REPORT_KO.md,REUSE_SURVEY.json,STAGE_LEDGER.json,NEXT_DAG.json,CODEX_HANDOFF.md,NEW_THREAD_HANDOFF.md와실제logs가있다. 단계별유도/코드/검증/실행/게시/백업/DAG를분리한다. 중간단계는로컬checkpoint이며최종cloudbackup을단계마다소급한기록은없다. 최종Gitmetadata와providerACK는외부DELIVERY/ACK에서확정한다.

## Codex 최소 인계

1. FULLarchive를새task-owned디렉터리에복원하고SHA/manifest를대조한다. 완료63cases를새NCPcampaign으로재시작하지않는다.
2. 저장결과그림만재생성: `cd package; python plot_pilot.py --out results/control63 --figures figures_from_saved`.
3. REIC15/currentcoupledowner에서기존raw를가져와`tensor_adapter.lrs_tensors`와`tensor_norms`를사용한다. 실제pressure표현과단위를먼저고정한다.
4. 기존625/81/63case의입력identity·원방정식·closure·norm을대조하고중복제거한다. Missing/다른physics결과를0으로채우지않는다.
5. 실제새coupledcase가필요할때만그owner의준비된runner로가용자원을공유한다. 다른session존재때문에전면중지하거나foreignjob을종료하지않는다. 원budget/tolerance를임의변경하지않는다.
6. 실제source·input·raw·preliminaryplot·DAG·backup영수증을반환한다. 상세benchmark,HH활성화,forcepush,mainmerge는포함하지않는다.

## 다음 대화 최소 인계

PHYS74branch/source와외부DELIVERY/FULL/ACK를읽고그후의새대화·PR·backup부터대조한다. PHYS73rawintake는COMPLETE이며15job/76panel/152profile은재실행하지않는다. PHYS74의63case는collisionlessLRScontrol이고fullHHe/UVpilot이아니다. 다음은다른thread의실제coupled결과를정규화·중복제거하여같은Sigma/Pi정의로표시하는작업이다. 원solverPR147과source56db9f2를보존하고최신HEADdescendantadditivedraft로만변경한다. Native runtime상태는매turn실제probe로확인한다. HH_R10=OFF.
