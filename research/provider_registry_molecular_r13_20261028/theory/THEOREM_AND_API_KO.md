# R13 정리와 유한 구현 계약

## 증명 대상과 전제

R11 full-A block certificate와 R12의 exact nonaligned clock을 그대로 쓴다. 동일 family/state/clock, 모든 허용 w 경로와 모든 시작시각에 대해 길이 tau에서 zero-mass l1 수축 q, 나머지구간 nonexpansiveness를 전제한다. K/pi/destruction은 고정이며 H=pi*d^T-diag(d), A=K+wH다. forcing은 whole fine/coarse-domain에서 유효한 비음수 piecewise-affine 상계다. 고정 c>=0와 signed d_c를 사용한다.

이 전제 아래 positive overlap 식은 전역 ideal R을 정확히 계산한다. source/translated/initial/observation event 사이의 R은 차수2이하이고, 내부 rational vertex를 추가하면 각 subcell에서 단조인 비음수 quadratic이다. 세 Bernstein2 coefficient는 비음수다. 양의 exponential Bernstein2 weights는 모든 signed d_c에 대해 ideal E endpoint를 주며, dyadic128/Taylor96의 유리수 tail과 directed rounding은 이를 감싼다. Whole-R은 one-sided limit까지 포함한 supremum, whole-E는 별도 constant-majorant로 인증한다.

## Source 함수와 경계

입력 g_r[j]=[r_left,r_right], g_e[j]=[e_left,e_right]는 sourcecell 내부의 affine whole-domain 상계함수를 정의한다. 두 관측 sample을 잇는 interpolation을 자동으로 whole-domain 인증으로 읽지 않는다. 서로 다른 cell의 one-sided endpoint가 달라도 적분의 measure-zero 경계값은 결과에 영향을 주지 않는다.

초기항 q^floor((t-t0)/tau)R0는 블록 경계에서 아래로 점프할 수 있다. 각 cell 오른쪽의 polynomial 값은 왼쪽 극한이다. 실제 endpoint R은 별도로 계산한다. 따라서 whole-cell의 supremum을 endpoint와 one-sided limit 후보의 유한 maximum으로 계산한다. 함수가 실제 maximum을 갖는다고 주장하지 않는다.

## 수치 설계

1. exact rational 입력과 유한 domain을 검사하고 동일 binding/certificate를 연결한다.
2. source/observation/translated/initial event를 exact equality로 합친다.
3. 각 basecell의 양끝과 midpoint를 exact overlap으로 계산한다. midpoint 재구성은 이미 증명된 quadratic의 coefficient 복원이므로 unknown trajectory interpolation이 아니다.
4. 내부 vertex가 있으면 exact rational로 넣는다. 기존 polynomial을 subcell에 제한하여 local coefficient와 nonnegative Bernstein2 coefficient를 얻는다.
5. exp와 세 positive beta-moment를 양수 argument에서 directed Taylor96으로 감싼다. 음수 argument는 reciprocal exp와 index reversal을 쓴다. 모든 곱셈항의 부호를 확인한다.
6. exact R와 outward E endpoint를 저장하고, whole-E는 같은 initial E upper와 constant forcing c*R_sup+max(g_e)로 계산한다.
7. observation point는 정확히 같은 knot만 고른다. observation closed cell은 gap-free refined cell upper의 maximum을 반환한다.

Taylor96은 |d_c|*(T-t0)<=16에서 양의 remainder를 포함한다. 128bit는 rounding grid이며 모든 enclosure 폭이2^-128이하라는 뜻이 아니다. 독립 reference는 Decimal160, 실행전 고정1e-80 relative guard이며 interval reference라는 명칭을 쓰지 않는다. 매우작은argument에서 phi closed form의 cancellation은 별도 직접series로 처리한다.

## 입출력 의미

Raw endpoints_lower/upper는 chosen rational q의 ideal comparison에 대한 enclosure다. Physical error의 lower가 아니다. Whole upper는 닫힌 셀 전체에 대한 상계이며 endpoint연결선은 그 인증이 아니다. 실제physicalsource와consumer결속은 별도INPUT_PENDING이다. R11 savedcap 또는 일반physicalcap을 이 새 affine forcing에 붙이는 API는 발급하지 않는다.

Sourcebits<=256, derivedbits<=16384, source/observation 각각1..64cells, base<=2048, vertexrefined<=4096, fullblocks<=8, overlapwork<=200000을 동시에 만족해야 한다. 최대값의 독립 조합이 모두 수용된다는 주장은 없다. 정확한 선행 work 계산과 reject 위치는 C4/C5의 구현 계약에 기록한다.

Degree0 source는 R12 ideal함수로 환원된다. Exact source/observation refinement는 같은ideal함수를 보존하며 directed rounding 출력의 bitidentity는 요구하지 않는다. Affine forcing과 같은 cell supremum constant forcing의 비교는 양의kernel로 유도하지만, 실제자료에서의엄격개선률이나raw의보편우위로확장하지않는다.
