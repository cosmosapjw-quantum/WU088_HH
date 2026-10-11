"""Read immutable native and reference exports; no source callbacks or libm."""
from pathlib import Path
from fractions import Fraction
import hashlib, json, struct

P = Path(__file__).resolve().parents[1]
REF = P.parent / 'hh_phys07_source_domain_20261011_v1'
def load(p): return json.loads(p.read_text())
def exact_ref(i):
    return tuple(Fraction(int(i[k]['numerator']), int(i[k]['denominator'])) for k in ('lo','hi'))
def from_bits(b): return struct.unpack('>d', bytes.fromhex(b))[0]
def exact_native(i):
    values = tuple(from_bits(i[k+'_bits']) for k in ('lo','hi'))
    assert values == (i['lo'], i['hi']), 'JSON float/word mismatch'
    return tuple(Fraction(x) for x in values)
def relation(native, ref, name):
    n = exact_native(native); r = exact_ref(ref)
    return dict(field=name, exact_endpoint_equal=n==r, native_contains_entire_reference=n[0]<=r[0] and r[1]<=n[1],
                reference_contains_entire_native=r[0]<=n[0] and n[1]<=r[1], overlap=max(n[0],r[0])<=min(n[1],r[1]),
                semantic_equivalence_established=False)
def leaf(bits, ref, name):
    r=exact_ref(ref); n=Fraction(from_bits(bits))
    assert r[0]==r[1], 'reference leaf must be one exact scalar'
    return dict(field=name,native_bits=bits, reference_exact_numerator=str(r[0].numerator),
                reference_exact_denominator=str(r[0].denominator), bit_identity=n==r[0])
def jet_rows(n,r,name):
    rows=[relation(n['value'],r['value'],name+'.value')]
    for i in range(len(r['gradient'])):
        rows.append(relation(n['gradient'][i],r['gradient'][i],name+f'.gradient[{i}]'))
        for j in range(len(r['hessian'][i])):
            rows.append(relation(n['signed_hessian'][i][j],r['hessian'][i][j],name+f'.hessian[{i}][{j}]'))
    return rows

result=dict(schema='PHYS07_NATIVE_REFERENCE_COMPARISON_V1',reference_replayed=False,source_callbacks=0,
            native_equivalence_status='OPEN_DIFFERENT_INPUT_AND_COEFFICIENT_SCOPES',
            interpretation='Comparisons of numeric enclosures alone do not establish same real family or scientific equivalence.', stages=[])
for stage in ('full','first_half'):
    p=P/'results'/stage
    if not (p/'SOURCE_BOX.json').exists():
        result['stages'].append(dict(stage=stage,status='NOT_AVAILABLE_SOURCE_FAILED')); continue
    native=load(p/'SOURCE_BOX.json'); r=load(REF/'results'/stage/'source_box.json'); f=load(REF/'results'/stage/'family.json')
    leaves=[leaf(native[k],f['stage'][v],v) for k,v in [('nH_bits','n_h_cm3'),('nHe_stored_bits','stored_n_he_cm3'),('fHe_bits','f_he'),('Hmean_bits','h_mean_per_s')]]
    for i,b in enumerate(native['energy_bits']):
        leaves.append(dict(field=f'energy[{i}]',native_bits=b,bit_identity=Fraction(from_bits(b))==Fraction(f['energies_ev'][i])))
    for i, row in enumerate(native['sigma_bits']):
        for j,b in enumerate(row):leaves.append(leaf(b,f['sigma_cm2'][i][j],f'sigma[{i}][{j}]'))
    comparisons=[]
    for i,n in enumerate(native['G']):comparisons+=jet_rows(n,r['residual'][i],f'G[{i}]')
    comparisons+=jet_rows(native['q'],r['HH_events_per_H_s'],'q')
    for i,n in enumerate(native['D']):comparisons.append(relation(n,r['photon_denominators'][i],f'D[{i}]'))
    for i,n in enumerate(native['photons']):comparisons.append(relation(n,r['outgoing_photon_values_per_H'][i],f'photon[{i}]'))
    pre=load(p/'PREBE.json')
    for i,n in enumerate(pre['groups']):
        comparisons.append(relation(n['gradient'][5],f['B_per_H'][i],f'M_dN_db[{i}]'))
    old=load(p/'COMMON_INPUT_SCOPE.json')
    point_checks=[exact_native(n['value'])[0]<=Fraction(v)<=exact_native(n['value'])[1] for n,v in zip(old['old_gas'],old['archived_point'])]
    summary=dict(stage=stage, leaf_count=len(leaves),bit_identical=sum(e['bit_identity'] for e in leaves),
                 leaf_mismatches=[e for e in leaves if not e['bit_identity']],interval_comparisons=len(comparisons),
                 native_contains_entire_reference=sum(e['native_contains_entire_reference'] for e in comparisons),
                 overlap_only=sum(e['overlap'] and not e['native_contains_entire_reference'] for e in comparisons),
                 disjoint=sum(not e['overlap'] for e in comparisons),archived_gas_point_inside_stored_box=point_checks)
    result['stages'].append(dict(status='STORED_EXPORT_COMPARISON_ONLY',summary=summary, scalar_leaf_bit_equalities=leaves,
        interval_relations=comparisons, scopes=['native: stored COMMON gas/photon/guard interval coefficients, captured native direction and libm widened transport',
        'reference: archived gas point, exact direction-stock sums, isotropic analytic real remap, correctly rounded scalar reference leaves'],
        reference_root_W_I_transferred_to_native=False))
out=P/'evidence/REFERENCE_COMPARISON.json'
assert not out.exists(), 'Preserve initial comparison'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps([s.get('summary',s) for s in result['stages']],indent=2))
