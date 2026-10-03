# C3B: conditional observable to rate reference

Status: conditional theory and reference implementation verified; actual HH physical inputs/rates unavailable. Frozen107/CP1 singlet model and original Q/phases/ETF remain unchanged. No new HH integration, matrix evaluation, trajectory, order, geometry or NCP run.

## New result
For normalized u_dot=Gu, G†=-G, 0<=A=A†<=I,

p_dot=u†Ju, J=A_dot+[A,G].

If beta_T=integral_T^infinity ||J||dt is finite, p_infinity exists and |p_infinity-p(T)|<=beta_T. A commuting diagonal Coulomb phase cancels here even if the full state has no pointwise limit. Actual HH off-diagonal/effect tails are not supplied.

Normalized preparation/state errors delta_in,delta_num and effect error eta give the sufficient bound 2delta_in+2delta_num+eta+beta_T, separately from arithmetic evaluation. Neither a D-array gap nor a D enclosure is automatically a state-error certificate.

## Measures and missingness
With explicit impact-azimuth averaging, x=b² gives sigma/pi=integral dx Pbar(sqrt(x),g). Only bounds valid over entire disjoint cells are accepted; point samples, overlap, duplicate and mismatched identities are rejected. No impact tail or missing cell implies full=null, not zero. The inner (t,u) endpoint does not cover propagation time, impact plane or relative-energy tails.

For a normalized local relative law, k=integral d³g F_rel(g)|g|sigma(g,g_hat). Maxwell specialization additionally requires isotropy, zero relative drift and isotropic/averaged sigma. With theta=mu*k_B*(Ta/ma+Tb/mb), S(x)=sigma(theta*x)/pi,

k=sqrt(8*pi*theta/mu)*integral dx x*exp(-x)*S(x).

Whole-bin weights are (1+a)exp(-a)-(1+b)exp(-b). ImpactTail stores an integral tail; EnergyTail stores a pointwise sigma/pi envelope. Their C++ types differ and cannot be implicitly interchanged.

The explicit speed laws (weights2/3,1/3;speeds1,5) and mono3 have equal second moments9 but mean speeds7/3 and3. Even constant sigma yields different rates. Bianchi homogeneity or a temperature alone is not a Maxwell closure.

## Counting and physics boundary
Nonzero spin weights require their sector data. Singlet-only does not define unpolarized rates. Same-population unordered events use n²k/2; distinct-population cross events use na*nb*k. Stoichiometry is applied afterwards. The ion-pair event creates Hplus and Hminus, not a free electron.

Closed-collision threshold clipping is rejected in prescribed-trajectory context. Actual threshold, heat, work, source domain/UQ and the baseline14 definitions remain unbound. request_physical_rate always throws SourceUnavailable; an absent provider does not prove negligible HH physics.

## Reproduction
The standalone ZIP contains50 unique tests (8 recorded red/green,31 native regression,1 manufactured integration,10 source/contract),4 additional long-double diagnostic integrations and31 UBSan repeats. The Git subset has all40 native cases and4 diagnostics; the10 source-lock tests need the ZIP.

The unchanged headers are in ../c3a_channel_contract_20261003_v1/closure. From this directory, in a fresh build directory:

```sh
BUILD=$(mktemp -d /tmp/c3b.XXXXXXXX)
for name in red_green reference_tests fixture_driver; do
  g++ -std=c++20 -O1 -fno-fast-math -Wall -Wextra -Werror -pedantic \
    -I../c3a_channel_contract_20261003_v1/closure tests/$name.cpp -o "$BUILD/$name" || exit
  if [ "$name" = fixture_driver ]; then
    "$BUILD/$name" "$BUILD/MANUFACTURED_PIPELINE.json" || exit
  else
    "$BUILD/$name" || exit
  fi
done
```

Exact rational references use installed Boost1.83; tested compiler GCC14.2.0. Current-host binaries are evidence, not portable-binary certification. Actual HH rates are not the synthetic fixture's SI numbers.

67-table DB preserves the61-table predecessor. Source26 locked; exact report/test/DB/package identities and provider ACKs are in DELIVERY_INDEX and detached receipt. Local SQL restore is separate from remote restore.

Next: C4A_LOCAL_SOURCE_OPERATOR_WITH_EXPLICIT_HMINUS_AND_ENERGY_LEDGER. Build conservative local species/electron/thermal source composition with synthetic providers only. Preserve explicit Hminus, energy ownership and missing baseline/domain inputs. Actual20/289 accepted,269 unbounded,epsilon_C/R=null,B22 open,scientific/production/review false. Full C3/C4 physical admission and C5 freeze remain open.

Primary external comparators: Stenrup et al.,arXiv0902.1900 and Walker et al.,arXiv1406.5750, abstracts only. No numerical data/model import. Detailed independent derivations and provenance are in the full THEORY_KO.md in the ZIP.
