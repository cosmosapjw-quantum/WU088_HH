# R31T read-only delta verification probe

The durable z=2 traces show that compute-wave scheduling is already about 97.5% efficient for the current 2x12 layout, while remote delta transactions/readback contribute more wall time than compute at B192.

This probe does not change the durability policy and performs no remote mutation. It selects one already-ACKed delta from an existing completed H state, queries provider-side size/hash metadata with rclone, and compares any common strong hash against local bytes.

If both providers expose a matching checksum plus size, a later separately-approved optimization can consider:

- routine 12-pair delta: dual upload + provider checksum/size verification;
- final H basis-state seal: retain full dual raw readback.

That would follow the selective-readback distinction between upload verification and restore verification. It is not enabled by this branch.

Example on the completed z=2 B192 state:

```bash
python scripts/probe_delta_remote_metadata.py \
  --folder "$RUNTIME/completion/mixed_h/wide_hybrid12/B192_g80_sunit_z4000000000000000" \
  --out "$WORK/r31t_delta_metadata_probe_z2_B192.json"
```

No output from this probe is sufficient by itself to alter ACK semantics.
