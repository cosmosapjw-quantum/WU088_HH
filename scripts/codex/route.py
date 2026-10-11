#!/usr/bin/env python3
"""Resolve an explicit task route; do not guess an unavailable alias."""
import argparse, json, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]

def resolve(task, cache, failures=0):
    policy = json.loads((ROOT / '.codex/ROUTING.json').read_text())
    if failures >= policy['escalation']['distinct_failed_attempts']:
        task = 'blocker'
    route = dict(policy['routes'][task])
    model = next((m for m in cache['models'] if m['slug'] == route['model']), None)
    if model is None:
        raise ValueError('requested model unavailable; no silent substitution: '+route['model'])
    efforts = {r['effort'] for r in model['supported_reasoning_levels']}
    if route['effort'] not in efforts:
        raise ValueError('requested effort unavailable: '+route['effort'])
    return route

def main():
    p = argparse.ArgumentParser()
    p.add_argument('task', choices=['routine','code','orchestrator','worker','explorer','review','research','blocker'])
    p.add_argument('--failed-attempts', type=int, default=0, help='distinct documented attempts, not automatic retry count')
    p.add_argument('--run', action='store_true')
    p.add_argument('--cwd', default=str(ROOT))
    p.add_argument('prompt', nargs='?')
    a = p.parse_args()
    route = resolve(a.task, json.loads(pathlib.Path('/root/.codex/models_cache.json').read_text()), a.failed_attempts)
    command = ['codex','--profile',route['profile'],'--model',route['model'],
               '-c','model_reasoning_effort='+json.dumps(route['effort']),'-C',a.cwd]
    if a.prompt: command.append(a.prompt)
    if a.run:
        sys.exit(subprocess.call(command))
    print(json.dumps({'requested':route,'command':command,'availability_basis':'local cached catalog; response admission not tested','live_parent_model_changed':False}))

if __name__ == '__main__': main()
