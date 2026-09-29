# R31Y: mixed block의 4차원 결함 모형과 Q의 대수적 보공간

기준 parent는 da2742895d36c72934b11d0677b7763637ad3ebf, tree c7cda62ad6c137ae6369bcb472f7a6708a30ea76이다. R31X NCP의 13 PASS, Q_AUTHORITY_BLOCKED, MIXED_FRAME_AUTHORITY_BLOCKED를 읽고 이어받았다. 기존 source, raw arrays, tolerance, provider와 production gate는 변경하지 않는다.

## 정의와 전제

동일 시각, 고정 좌표에서 i hbar O dotc=(H-i hbar D)c, H=H†, O>0라 두고 R=dotO_actual-D-D†로 정의한다. N=c†Oc이면 dotN=c†Rc이다. 시간은 t_a=hbar/E_h, O는 무차원, R,D 및 generalized eigenvalue는 1/t_a 단위다. 여기의 47+2 partition은 저장된 index partition이며 새로운 물리적 채널 라벨을 부여하지 않는다.

R을 [[E,B],[B†,F]]로 쓰자. B는 p×m, p=47,m=2다. 먼저 E=0인 명시적 보조모형 R0만 연구한다. 실제 저장된 E를 0이라고 선언하거나 원 R을 교체하지 않는다. 이하 Hermitian 정리는 exact Hermitian R0,F 및 exact SPD O를 전제로 한다. 실제 부동소수점 계산에는 별도 잔차를 기록한다.

## 1. 원래 Q 없이 얻는 2m차원 압축

B가 full column rank이면 thin QR B=Ub Tb에서 Ub†Ub=I_m이고 Tb는 가역이다. 다음을 정의한다.

    Z = diag(Ub,I_m),
    K = [[0,Tb],[Tb†,F]],
    R0 = Z K Z†.

Z는 무차원인 (p+m)×2m 행렬이고 K는 inverse-time 단위다. O=L L†의 Cholesky와 L^-1 Z=U T의 thin QR를 쓰면

    L^-1 R0 L^-† = U M U†,   M=T K T†,   U†U=I_(2m).

따라서 (R0,O)의 비영 generalized spectrum 전체가 Hermitian 2m×2m M의 spectrum이다. 이 차원은 관측된 큰 고유값 몇 개를 임의 선택해서 정하는 값이 아니라 mixed block의 full column rank에서 나온다.

동일 결과의 독립 계산 경로는 G=Z†O^-1 Z, small=K G다. AB와 BA의 비영 spectrum 일치로 det(lambda O-R0)=det(O) lambda^(p-m) det(lambda I_(2m)-K G)이다. K G v=lambda v이면 x=O^-1 Z v가 ambient generalized eigenvector다. 이 경로에는 가역 O면 충분하며, 수치 코드에서는 Hermitian triangle을 강제로 대입하지 않는 general eig를 사용한다. Hermitian QR 경로와의 차이를 따로 기록한다.

문헌 배경은 Nakatsukasa, The low-rank eigenvalue problem, arXiv:1905.11490v1이다. 본 연구의 block factorization과 단위 규약은 위와 같이 직접 유도했다. 저랭크 eigensolve가 가능하다는 것과 expensive O/B/F를 저비용으로 새로 생성할 수 있다는 것은 다르다. 실제 host speedup이나 source 계산 생략은 주장하지 않는다.

## 2. 왜 네 mode가 두 양수와 두 음수인가

S1=diag((Tb†)^-1,I), S2=[[I,-F/2],[0,I]]이면

    (S1 S2)† K (S1 S2) = [[0,I],[I,0]].

오른쪽은 각각 m개 +1,-1을 가진다. 따라서 congruence로 inertia가 보존되고, R0 및 SPD metric generalized pencil의 inertia는 (m,m,p-m)이다. 현재 p=47,m=2이면 (2,2,45)다. F는 비영이고 다른 블록과 commute하지 않아도 된다.

B의 rank가 m보다 작으면 이 가역 congruence는 사용할 수 없다. 코드도 수치 rank-deficient B를 거절하며 그 경우에 (2,2,45)를 출력하지 않는다. 실제 R에는 E가 작지만 비영이므로 45개 exact zero는 원자료에 대한 결론이 아니다.

## 3. 원자료의 비영 remainder를 남기는 법

Exact Hermitian 전제에서 Delta=R-R0=[[E,0],[0,0]]라 하면

    epsilon = ||L^-1 Delta L^-†||_2,
    |lambda_i(R,O)-lambda_i(R0,O)| <= epsilon,
    |eta(R,O)-eta(R0,O)| <= epsilon.

R0의 spectrum에는 p-m개 zero를 함께 넣어 정렬한다. 이는 표준 Hermitian perturbation 결과를 같은 whitening frame에 적용한 조건부 정리다. Float로 계산한 epsilon이 그 자체로 certified upper bound는 아니다.

실제 HH snapshot은 binary64 진단에서 O Hermiticity gap 약1.126e-14, R gap 약1.362e-14다. 이를 숨기지 않는다. 원 O/R을 symmetrize하지 않았고 general eig로 전체 entries를 사용했다. Cholesky 경로의 실제 입력 재구성 gap도 약1.041e-14로 보존한다. 따라서 이번 값들은 exact theorem을 지원하는 represented-matrix diagnostics이며 physical-source/interval enclosure가 아니다.

## 4. Q의 대수적 sector와 물리적 authority는 다르다

Q†Q=I인 exact 전제에서 P=QQ†, J=2P-I는 Hermitian involution이다. 만약 [O,J]=[R,J]=0이면 Q와 Euclidean orthonormal 보공간 Qminus를 합친 basis에서 두 matrix가 동시에 block diagonal이다. 따라서 전체 generalized spectrum은 두 sector spectrum의 합집합이다.

이 명제는 Q를 물리적 parity/exchange operator에서 유도했다고 말하지 않는다. 저장된 Q의 수치 column structure로 정의한 대수적 involution을 검사할 뿐이다. R31X의 Q producer/channel meaning/valid-z authority는 계속 미확정이다. H나 dotQ의 동역학적 계약을 검사한 것도 아니므로 propagation decoupling은 주장할 수 없다.

## 실제 저장자료 결과

입력71481 bytes, SHA256 565a9ee6d831f5f9e3e69010270f5319aa3328432950efcfda81cfabf325c079. 원 extended-precision 파일을 보존하고 기존 R31W/X와 같은 complex128 hybrid 진단을 구성했다.

B의 singular values는 0.3649304141812513,0.10269718532148013 /t_a다. 4×4 K G의 실수부는 다음과 같다.

    -0.4831184527967173
    -0.11540262422575771
    +0.17743965987509844
    +0.6007169417167525

최대 허수부는 약5.00e-16 /t_a. 원49×49 general eig의 큰 네 mode와 최대 차이는1.163e-15 /t_a, 보조모형 full eig와는4.013e-16 /t_a, whitening/QR 경로와는4.910e-16 /t_a다. Lowrank factorization gap은9.457e-17 /t_a이며 raw-minus-auxiliary norm은1.0284145759849785e-14 /t_a다. Whitened remainder norm은1.142235373960423e-14 /t_a로 계산되었다. 이 작은 값을 근거 없이 source error로 해석하지 않는다.

Q의25차원 sector에는 -0.48311845279671656,+0.6007169417167526 /t_a가, 보공간24차원에는 -0.11540262422575782,+0.17743965987509824 /t_a가 있다. Nonzero 표시는 진단용1e-12 /t_a 기준이다. O와 R의 sector cross-block norms는 각각3.008e-16,8.546e-17이고 [O,J],[R,J] norms는2.535e-16,1.600e-16이다. Sector spectrum 합집합과 full raw spectrum의 최대 차이는3.239e-15 /t_a다.

따라서 이 point에서 Q가 extremal pair를 잡고 interior pair를 놓친다는 현상은 단순한 numerical rank 우연보다 강하게 설명된다. 두 sector가 현재 pencil에 대해 거의 분리되어 있으며 Q sector에 실제로 더 큰 절댓값의 pair가 존재한다. 하지만 physical symmetry와 z 구간 전체의 sector 보존은 여전히 증명하지 않았다.

## 도구·실행과 남은 gate

SciSpace에서 저랭크 generalized eigenvalue/inertia 문헌을 검색했고 arXiv:1905.11490v1 원전 metadata를 대조했다. Wolfram은 이번에는 실제 작동했다. Exact small-matrix congruence, rank4, characteristic-polynomial identity를 확인했으며 이전 실패를 이번 성공으로 소급 변경하지 않는다. 원 HH float matrices를 exact Wolfram 입력으로 승격하지 않았다.

새 focused20 tests, compile, stored replay 결과는 evidence와 RESULT.json에 있다. Full repository/native scientific suite는 범위 밖이다. NCP R31Y replay는 미수행이며 기존 NCP13/33/134와 합산하지 않는다.

다음 단계는 새로운 R31Y의 경량 검산과 원 producer artifact의 정확한 위치/내용을 확보하는 것이다. 같은 축약 snapshot에서 Q/frame authority를 다시 찾는 반복은 중단한다. 구체적인 acquisition target은 CODEX_HANDOFF_KO.md와 SOURCE_PINS.json에 있다. Q/frame/full-cell authority, source enclosure, physical transition error, independent reviewer admission, production 및 H-skip gate를 이 결과가 열지 않는다.
