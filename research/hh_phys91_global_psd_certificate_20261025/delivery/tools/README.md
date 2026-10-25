# PHYS91 final downloaded-byte verification

This helper is prepared for root's later use; preparation is not a restore result.
Run only on the file produced by an actual complete provider GET. Root owns the
provider GET and authoritative remote Git identity capture. No network, HEAD,
retry, scientific import, callback, numerical calculation, or nested ZIP opening
is performed here. An upload/metadata ACK cannot establish a GET.

```
python publication/restore_helpers/verify_download.py zip ACTUAL_DOWNLOAD.zip EXPECTATION.json NEW_RECEIPT.json
python publication/restore_helpers/verify_download.py json ACTUAL_MAIN_OR_TERMINAL.json EXPECTATION.json NEW_RECEIPT.json
```

ZIP expectation fields:

- `bytes`, `sha256`: root's expected raw whole ZIP identity.
- `original_config`: path to the exact original final build config.
- `reuse_bindings`: path to the preserved PARENT_REUSE_BINDINGS.json.
- `authoritative_tree`: path to JSON shaped as
  `{"head":"...","tree":"...","files":{"repo/path":"git-blob-sha1"},"source_metadata":{...}}`.
  Root derives this map from the authoritative remote tree response; it must
  include every blob under the unit. Inherited blobs absent from that map are
  bound to preserved inherited Git objects in `reuse_bindings`.
- `frozen_manifest`: path to the saved frozen-eight manifest with `files` mapping
  unit-relative (or full repository) paths to SHA256 strings.
- `extract_parent`: existing writable directory for unique create-only restoration.
- `source_metadata`: root's actual GET source metadata, copied without interpreting
  unknown/null values or claiming provider provenance from an ACK.
- Optional `manifest_checks`: list of `{"keys":["key","nested_key"],"value":...}`
  root-selected exact checks beyond config identity.

JSON expectation fields are `bytes`, `sha256`, `source_metadata`, and `checks`.
For each MAIN/TERMINAL file, root must select exact parsed key paths for head,
tree, and scientific identity, e.g. each `checks` item is
`{"keys":["root_selected_key","head"],"value":"expected head"}`. Lists may
contain integer indices. Missing paths fail. Explicit null expectations remain
null; no normalization or inferred science result is introduced.

ZIP checks cover whole raw bytes/SHA256, all member CRCs, all manifest payload
bytes/SHA256, exact member path set, authoritative unit blob/path identity,
pinned inherited objects, frozen eight, three input identities, and parent
payload identities. Exactly one whole parent ZIP is retained as opaque bytes;
nested restore count is zero. All members, including ARCHIVE_MANIFEST.json and
the parent ZIP, are actually written to a unique new directory and reread for
SHA256 and exact path-set verification. Dynamic member/payload/Git counts are
reported from the actual archive. A failure raises an exception and never emits
a PASS receipt; failed extraction may leave its unique partial directory for
inspection. Receipts are create-only. Use each provider's actual downloaded
bytes independently. The helper cannot itself prove that root's supplied local
path came from a GET, or that supplied tree metadata came from the remote;
root retains those transport/source evidences.

Preparation validation: one finite AST/static pass only. No archive or JSON
transport verification has been run during helper preparation.
