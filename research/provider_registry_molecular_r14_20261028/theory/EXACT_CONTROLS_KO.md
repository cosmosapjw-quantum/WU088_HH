# R14 exact controls와 판별 의무

상태: 수동 exact derivation; 실제 실행 결과가 아니다. 기본값은 \(t_0=0,\tau=1,c=1,d_c=0,R_0=E_0=0,g_e=0\)이다. 아래 수치는 조건부 arithmetic fixtures이며 HD physical gain이 아니다.

## 1. Quadratic 적분과 더 느슨한 bounds

\(q=1,\ T=1,\ g_r(s)=s^2\)이면
\[
R(t)=t^3/3,\quad E(t)=t^4/12,\quad R(1)=1/3,\quad E(1)=1/12.
\]
같은 domain에서 \(s^2\le s\le1\). Affine \(g_r=s\) 비교는 \(R(1)=1/2,E(1)=1/6\), constant \(g_r=1\) 비교는 \(R(1)=1,E(1)=1/2\)다. Ideal relative reduction은 constant 대비 R \(2/3\), E \(5/6\), affine 대비 R \(1/3\), E \(1/2\)다. Rounded outputs나 physical data 개선과 혼동하지 않는다. 분모 0인 비율은 null이다.

## 2. Signed middle coefficient를 갖는 nonnegative source

\(g_r(s)=(s-1/4)^2\), source Bernstein triplet \((1/16,-3/16,9/16)\), \(q=1,T=1\). Vertex \(1/4\)의 source split을 거친다.
\[
R(1)=7/48,\qquad E(1)=1/32.
\]
원래 구간의 cumulative cubic Bernstein coefficients \((0,1/48,-1/24,7/48)\)는 signed이므로 monotone cubic에 R13 positivity lemma를 자동 적용하는 구현은 이 사례로 판별된다. 선택한 Simpson construction은 effective source pieces에서 positive cubic을 만든다.

## 3. 서로 다른 두 source vertices의 union

2번의 \(g_r\)와 \(g_e(s)=(s-3/4)^2\)를 함께 사용한다. Source vertices \(1/4,3/4\)의 union은 세 effective pieces를 만든다.
\[
R(1)=7/48,\qquad E(1)=1/32+7/48=17/96.
\]
같은 원래 source cell 안에서 gr/ge 각각의 vertex를 반영해야 한다.

## 4. 하나의 irrational interior maximum

\(q=0\), \(g_r=s^2\) on \([0,1]\), \(g_r=1/2\) on \([1,2]\). \(x=t-1\in[0,1]\)에서
\[
R(1+x)=1/3+x/2-x^3/3.
\]
Critical \(x=1/\sqrt2\), whole supremum \(1/3+\sqrt2/6\), \(R(1)=1/3,R(2)=1/2,E(2)=7/12\).
Cubic Bernstein coefficients \((1/3,1/2,2/3,1/2)\), \(M_B=1/2\), hence certified rootbox whole-gap \(\le2^{-97}\).
Optional critical scalar value: \(E(1+1/\sqrt2)=3/16+\sqrt2/6\).

## 5. 한 base cell 안의 두 irrational critical roots

\(q=0\), first source \(g_r(s)=1+2s\) on \([0,1]\), second \(g_r(1+x)=9/8+x+x^2\) on \([1,2]\). 각각 source Bernstein coefficients는 \((1,2,3)\), \((9/8,13/8,25/8)\). 둘 다 monotone이며 source vertex preprocessing이 \([1,2]\)을 나누지 않는다.
\[
R(1+x)=2+x/8-x^2/2+x^3/3,\qquad
R'=x^2-x+1/8.
\]
Critical roots는 \((1-1/\sqrt2)/2\), \((1+1/\sqrt2)/2\). 각각 local maximum \((95+\sqrt2)/48\), minimum \((95-\sqrt2)/48\)이다. 전체 \([1,2]\) maximum도 앞의 값이다.
\[
R(1)=2,\quad R(2)=47/24,\quad E(1)=5/6,\quad E(2)=45/16.
\]
Cubic coefficients \((2,49/24,23/12,47/24)\), derivative coefficients \((1/8,-3/8,1/8)\), \(M_B=3/8\). 두 root branches는 derivative vertex \(1/2\)로 분리한다. Rootbox gap은 \(\le(3/8)2^{-96}\), 최대 bisections 192회다.

## 6. 별도의 irrational root 형태

Root 제안 golden control: \(q=0,\ g_r=s^2\) on \([0,1]\), \(g_r=2-s\) on \([1,2]\).
\[
R(1+x)=1/3+x-x^2/2-x^3/3.
\]
Critical \(x=(\sqrt5-1)/2\), whole supremum \((5\sqrt5-3)/12\), \(E(2)=2/3\). \(\sqrt2\) fixtures와 다른 quadratic discriminant를 사용한다.

## 7. Initial downward jump와 unattained supremum

\(q=0,R_0=1,g_r=s^2\) on \([0,1]\).
\[
R(t)=1+t^3/3\quad(0\le t<1),\quad R(1)=1/3,
\]
\[
R(1^-)=\sup_{[0,1]}R=4/3,\qquad E(1)=13/12.
\]
Supremum lower witness가 left limit일 수 있다. Actual endpoint와 left limit를 동일시하면 실패해야 한다.

## 8. Global memory와 fresh forcing

\(q=1/2,g_r=s^2,T=5/4\)에서
\[
R(t)=t^3/3-(t-1)_+^3/6,\quad
E(t)=t^4/12-(t-1)_+^4/24
\]
이므로 \(R(5/4)=83/128,E(5/4)=1249/6144\).
같은 case에서 \(q=0\)이면 \(R(5/4)=31/48,E(5/4)=13/64\).
\(q=0\)을 모든 forcing contribution 0으로 처리하거나 observation/source boundary에서 memory를 reset하면 이 항등식에 맞지 않는다.

## 9. 별도 guard와 reduction controls

- Exact rational critical root, endpoint root, double derivative root, constant derivative, constant polynomial, degree-two/one/zero reductions.
- Endpoints는 비음수지만 interior가 음수인 triplet \((1,-2,1)\)는 midpoint 값 \(-1/2\)이므로 reject.
- Nonnegative isolated-zero polynomial은 accept. Coincident gr/ge vertices는 exact deduplicate.
- Source/observation refinements는 같은 ideal function을 유지한다. Rounded bitidentity는 별도 주장이다.
- Signed positive/negative \(d_c\), near-zero \(d_c\), \(|d_c|(T-t_0)=16\), shifted rational \(t_0\), nonaligned observations, discontinuous source values.
- 원래 source hash/state/clock 불일치, domain limits, derived-bit guard, max effective 48, near-boundary / near-coalescent roots.
- Degree-zero source는 R12 ideal comparison, degree-one source는 R13 ideal comparison으로 reduce한다. Accepted older harness를 다시 실행할 필요 없이 새 구현 내 algebraic controls로 검증한다.

