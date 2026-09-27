import hashlib
import pytest
from wu088_hh.transport_probe import dropbox_content_hash,local_hashes,compare_hash_sets,select_latest_acked_delta

def test_dropbox_hash_empty_matches_spec_empty_outer_sha(tmp_path):
    p=tmp_path/'x';p.write_bytes(b'')
    assert dropbox_content_hash(p)==hashlib.sha256(b'').hexdigest()

def test_compare_remote_hash_accepts_common_matching_algorithm(tmp_path):
    p=tmp_path/'x';p.write_bytes(b'abc')
    local=local_hashes(p)
    out=compare_hash_sets(local,{'md5':local['MD5']})
    assert out['all_common_match'] is True
    assert out['common_algorithms']==['md5']

def test_compare_remote_hash_rejects_mismatch_or_no_common(tmp_path):
    p=tmp_path/'x';p.write_bytes(b'abc');local=local_hashes(p)
    assert compare_hash_sets(local,{'MD5':'0'*32})['all_common_match'] is False
    assert compare_hash_sets(local,{'CRC32':'abcd'})['any_common'] is False

def test_latest_acked_delta_uses_last_queue_entry_with_ack():
    q=[{'delta_sha256':'a','delta_path':'a.zip'},{'delta_sha256':'b','delta_path':'b.zip'}]
    a=[{'delta_sha256':'a','drive':{},'dropbox':{}}]
    row,ack=select_latest_acked_delta(q,a)
    assert row['delta_sha256']=='a' and ack['delta_sha256']=='a'
    with pytest.raises(ValueError):select_latest_acked_delta(q,[])
