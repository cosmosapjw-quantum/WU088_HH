from __future__ import annotations
import math, statistics


def candidate_layouts(*, physical_budget:int, logical_budget:int, pairs:int=12) -> list[tuple[int,int,bool]]:
    if min(physical_budget,logical_budget,pairs)<1 or logical_budget<physical_budget:
        raise ValueError('invalid benchmark budgets')
    preferred=[
        (12,1,False),(6,2,False),
        (12,2,True),(6,4,True),(4,6,True),(3,8,True),(2,12,True),
    ]
    out=[]
    for p,t,smt in preferred:
        budget=logical_budget if smt else physical_budget
        if p<=pairs and p*t<=budget:
            out.append((p,t,smt))
    if not out:
        raise ValueError('no full-pair benchmark layouts fit host budget')
    return out


def representative_pairs_from_events(rows:list[dict], *, count:int=12) -> list[tuple[int,int]]:
    if count<1:
        raise ValueError('count must be positive')
    vals=[];seen=set()
    for row in rows:
        if 'ia' not in row or 'ib' not in row or 'wall_seconds' not in row:
            continue
        pair=(int(row['ia']),int(row['ib']));wall=float(row['wall_seconds'])
        if pair in seen or not math.isfinite(wall) or wall<=0:
            continue
        seen.add(pair);vals.append((wall,pair))
    vals.sort(key=lambda x:(x[0],x[1]))
    if len(vals)<count:
        raise ValueError('not enough unique timed pair rows')
    if count==1:
        return [vals[len(vals)//2][1]]
    idx=[]
    for k in range(count):
        i=round(k*(len(vals)-1)/(count-1))
        if idx and i<=idx[-1]:
            i=idx[-1]+1
        idx.append(i)
    return [vals[i][1] for i in idx]


def select_exact_layout(samples:list[dict], *, locality_tie_fraction:float=0.02) -> dict:
    if not 0<=locality_tie_fraction<=0.25:
        raise ValueError('invalid tie fraction')
    grouped={}
    for row in samples:
        key=(int(row['processes']),int(row['kernel_threads']),bool(row.get('use_smt',False)))
        grouped.setdefault(key,[]).append(row)
    candidates=[]
    for key,rows in grouped.items():
        if not all(r.get('numerical_array_exact_equal') is True for r in rows):
            continue
        if not all(r.get('affinity_disjoint') is True for r in rows):
            continue
        walls=[float(r['batch_wall_s']) for r in rows]
        if any(not math.isfinite(x) or x<=0 for x in walls):
            continue
        cross=max(int(r.get('cross_l3_workers',0)) for r in rows)
        candidates.append({
            'processes':key[0],'kernel_threads':key[1],'use_smt':key[2],
            'median_wall_s':statistics.median(walls),
            'cross_l3_workers':cross,'repetitions':len(rows),
            'median_h0_pair_wall_s':statistics.median(float(r.get('median_h0_pair_wall_s',0.0)) for r in rows),
            'median_foreign_pair_wall_s':statistics.median(float(r.get('median_foreign_pair_wall_s',0.0)) for r in rows),
        })
    if not candidates:
        raise ValueError('no exact affinity-valid layout')
    fastest=min(candidates,key=lambda r:(r['median_wall_s'],r['cross_l3_workers'],r['processes'],r['kernel_threads']))
    band=fastest['median_wall_s']*(1+locality_tie_fraction)
    tied=[r for r in candidates if r['median_wall_s']<=band]
    best=min(tied,key=lambda r:(r['cross_l3_workers'],r['median_wall_s'],r['processes'],r['kernel_threads']))
    out=dict(best)
    out['fastest_median_wall_s']=fastest['median_wall_s']
    out['locality_tie_fraction']=locality_tie_fraction
    out['selection_reason']='WITHIN_TIE_BAND_PREFER_L3_LOCALITY' if out['median_wall_s']>fastest['median_wall_s'] and out['cross_l3_workers']<fastest['cross_l3_workers'] else 'FASTEST_MEDIAN_EXACT_CONFIGURATION'
    return out
