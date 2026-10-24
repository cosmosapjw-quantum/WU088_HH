# PHYS86 bounded Wolfram implementation

Prepared from the Astra-authored CONTRACT.json and full theory note in this unit. Requested implementation model is `gpt-6.1-sol/high`; actual backend identity is `UNOBSERVED`. This directory records preparation and mechanical checks. Scientific verification and Wolfram execution remain NOT_RUN until the controller's explicit GO after independent review and stage backup.

## Two requests and fixed limits

1. `RECOVERY_REQUEST_ARGUMENTS.json`: exactly one call of the preserved PHYS85 repair01 core. The `source/phys85_repair01_core.wl` bytes are exactly the original repaired cloud source prefix before its old output wrapper. Only the output projection changes. No prior complete raw report is claimed or recovered. The two old calls and their exhausted allowance are unchanged. This is a separately authorized first compact complete certificate, with at most one new call.
2. `MOMENTS_REQUEST_ARGUMENTS.json`: exactly one call of the source finite exponential-family moment interface and independent polynomial derivative oracle. Three q points, ten guards and 82 expected assertions. All retained-daughter source composition tests are algebraic identities in independent formal `uC`, `rate`, `cv`, with declared physical domain Cv>0, R>=0 and T>0. No daughter caloric data, positive numeric Cv, physical rate, Bessel numeric table or continuum quadrature is invented.

Each request uses `timeConstraint:60` and an inner 55-second bound, one kernel, no parallel work and no new ODE. No probe, retry, split call or scientific local execution is authorized. A concrete runtime failure returns to Astra with all raw bytes preserved; no automatic repair call follows. The unchanged local reserve1.5GiB+job0.5GiB contract failed upstream, so this preparation uses metadata, source text, hashing, JSON and static delimiter checks only.

## Source and checker paths

`source/reaction_moments.wl` constructs a positive one-particle finite family, applies a nonnegative kernel, computes exact selected moments, and exposes the temperature-source coefficient pair. Positive rational q is restricted to 0<q<1. One-particle energies are positive integers in epsilon0 units. Base weights are positive exact rationals; kernel entries may be zero. A zero kernel returns source0 and explicit UNDEFINED normalized moments. Numeric nonpositive Cv and negative rate are rejected; R=0 returns0 before normalized moment access.

The independent checker in `verification/verify_reaction_moments.wl` differentiates the three frozen partition polynomials directly. It checks 15 selected/partition moment residuals per q, source composition coefficients, and q-dependent kernel correction. The wrong correction control is required to be nonzero. The Bessel checks use the derivative and recurrence identities algebraically. NR checks construct the standard large-z K_nu series coefficients, cancel their common exponential/square-root factor, and take symbolic limits and source reductions.

The PHYS85 compact certificate carries actual ordered 1,017 bits, actual ordered label SHA, actual case/ensemble/guard counts, all 36/6 row residual sums of absolute values, nine ordered distinct channel/fixture energy triples, three channel covariances, the 23 actual ordered guard Failure tags and all original failure labels. `source_data/PHYS85_EXPECTED_ORDER.json` fixes those orders by mechanically transcribing the frozen source loop structure. The two radiation routes have the same selected covariance, so the first route per channel supplies the declared three values.

## Exact transport

`compact_transport.wl` serializes a compact RawJSON payload `p`. Rational values are strings with integer numerator/denominator; integer counts and booleans retain JSON types. The outer envelope contains only `p`, its SHA256 and UTF-8 byte length. SHA and byte count exclude all envelope fields and bind the exact received p string, with no local reserialization required. Official Hash documentation specifies UTF-8 bytes for a string; its HexString output matches ordinary SHA256. Official RawJSON documentation specifies Compact->True to omit line breaks and tabs.

The complete outer JSON must be ASCII. The runtime guard measures the complete envelope after one further RawJSON string escaping, including string quotes, and returns only explicit OUTPUT_TOO_LARGE if it exceeds8,000 bytes. This covers the envelope's escaped Out string representation. No list, assertion, failure, rational or row is truncated. The full evaluator raw response must still be retained even if its formatting/transport fails. No static scientific rational lengths were evaluated locally; the finite runtime measurement is authoritative.

Official references read during preparation:

- https://reference.wolfram.com/language/ref/Hash.html (Details: string UTF-8 bytes; SHA256/HexString)
- https://reference.wolfram.com/language/ref/format/RawJSON.html (Export options and Compact->True examples)

## Mechanical preparation commands

Run from `/workspace/scratch/ebcaaaa20861`:

```bash
python wu_phys86_20261024/tools/prepare_phys86.py
python WU088_HH/research/hh_phys86_juttner_reaction_moments_20261024/implementation/static_verify.py
```

The assembler checks both parent frozen hashes, extracts only the unchanged core, constructs the expected label order, assembles code/request files and writes a minimal freeze manifest. It does not execute Wolfram or numerical/scientific Python. `static_verify.py` checks request/source equality, balanced delimiters/strings/comments, absence of package/parallel/ODE calls and unchanged parent core. It is not a Wolfram parser or a science PASS.

## Exact authorized execution procedure after controller GO

For request A then B, use the Wolfram Language evaluator tool `mcp__codex_apps__wolfram_wolframlanguageevaluator` with the **entire corresponding REQUEST_ARGUMENTS.json object unchanged**. These files are the full exact command arguments. Invoke each at most once; no probe or partial code. Save the sent object as `implementation/attempt_recovery/TOOL_REQUEST_ARGUMENTS.json` or `implementation/attempt_moments/TOOL_REQUEST_ARGUMENTS.json`. Save the entire returned tool object unchanged in the same attempt directory as `RAW_WOLFRAM_RESPONSE.json`, including every content block, structuredContent, warning and isError. Preserve a tool exception separately if no normal object returns. Record actual dispatch/return UTC times and tool identity. Then run only the transport parser:

```bash
python WU088_HH/research/hh_phys86_juttner_reaction_moments_20261024/implementation/parse_response.py recovery WU088_HH/research/hh_phys86_juttner_reaction_moments_20261024/implementation/attempt_recovery
python WU088_HH/research/hh_phys86_juttner_reaction_moments_20261024/implementation/parse_response.py moments WU088_HH/research/hh_phys86_juttner_reaction_moments_20261024/implementation/attempt_moments
```

The parser extracts a complete JSON envelope only, checks exact payload SHA/length and bounded escaping, preserves the complete decoded certificate and exact p bytes, and reports scope counts/bits and zero residual fields. It performs no scientific arithmetic or independent scientific acceptance. Any parse/scope failure is saved in PARSE_AND_SCOPE_RECEIPT.json; it is never silently retried. After these prescribed observations, return raw outcomes and the actual diff to a fresh Astra reviewer. Scientific admission and publication are the controller's decisions.
