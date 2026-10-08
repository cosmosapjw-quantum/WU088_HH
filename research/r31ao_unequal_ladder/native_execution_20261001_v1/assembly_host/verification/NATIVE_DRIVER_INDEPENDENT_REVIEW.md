# Independent native-driver / interior-design review

Verdict: **no blocking finding in the reviewed exact design and Python/source boundary.** Overall native solver validation is **PARTIAL**: this review neither compiled nor executed FLINT/C++ and does not establish native cached/baseline numerical equality, successful compact integration, complete 2,592-primitive coverage, full-D enclosure or production admission.

The review used the code-verification workflow, read-only source inspection, fresh targeted existing tests and an independent exact-rational domain check. No owner files or tests were changed. Active backend build directories/logs were not inspected.

## Exact reviewed identity

| File / identity | SHA-256 |
|---|---|
| native_driver/driver.py | `3e34137e1abb3a216075c27b966c773ad97010b2cfa0eef53c9a32ebe7948689` |
| native_driver/primitive_worker.cpp | `4437413c49d106b55705eb3aee680c9f184d82872cfad8256a9f9f76a832526c` |
| native_driver/dependency_pins.json | `8f53cd061ec3064932898034c1f841a44d3c5ca5de6ccf8a0f07eba2e1921f8e` |
| native driver source identity | `3cc606b5842cbc65225d6f21adf20b2e7cadac5859fda60c389ecbae48e2c372` |
| interior_design/planner.py | `bbd36560cf845bdfc91e7341eb53f0c9c8181eaaf589726407812fce05628c3b` |
| interior_design/test_planner.py | `174c4d1c77e634789331030410b206f1024b828755d362adbf75394d5a45045e` |

Paths above are relative to `native_execution_20261001_v1/`. The baseline comparison was the unchanged `production_solver_20261001_v1/native_driver` plus the pinned original callback/assembly/Petras and cached-callback sources.

## Requirements and evidence

| Requirement / risk | Evidence and result |
|---|---|
| Real-domain positivity guard must not reject a valid large upper endpoint merely because sigma is small | Exact formula inspection; native/Python margin expressions agree; fresh regression and independent large-T counterexample PASS |
| Smaller margin must not bypass complex-domain branch guards | Callback still checks entire complex balls for t,u,A,B,sigma; padded complex-product lower bound derived below; no observed ball acceptance claimed |
| Cached callback must keep the full outer box and original arithmetic | Source inspection shows adapter copy retains contract/parameter/term pointers, assigns full `outer_box`, and calls pinned cached callback; no midpoint substitution |
| Cache build must not double-link or silently replace baseline | Explicit baseline/cached flags and source lists, source pins and manifest revalidation; fresh build-configuration boundary tests PASS |
| Tiling must exactly cover its declared window and add endpoint uncertainty once | Exact contiguous dyadic axes and area-additivity checks PASS; full W3 axis has 200 intervals per axis, 40,000 Cartesian tiles; `execute_full_grid=false` |
| Diagnostic pilot must not become full-window evidence | Separate CENTRAL/TINY_CENTRAL window plans are input/parameter bound, have distinct plan/task identities and are explicitly compact diagnostics; no endpoint result is generated |
| Source / bounds / output must fail closed | Fresh strict JSON, radius, resource, source, create-only and promotion-refusal tests PASS; source identity is distinct from old worker |

## Margin and padded-domain reasoning

For exact positive a,b and a positive real compact rectangle, sigma is decreasing in each real variable:

`sigma(t,u) = (1/(a+t) + 1/(b+u))/2 >= sigma_min = (1/(a+T_t) + 1/(b+T_u))/2 > 0`.

The new effective native margin is

`m = min(1, l_t, l_u, sigma_min) / 2^20`.

This follows from taking the new endpoint/sigma minimum and then retaining the existing default Contract margin when smaller. The Python helper is the same exact expression. This changes a positivity guard, not the requested quadrature radius, precision or scientific target. For the independent synthetic case a=1/512, b=3/512, lower endpoints 1/256 and upper endpoints 2^192, the former margin 2^-28 exceeds sigma_min; the new margin equals sigma_min/2^20 and is strictly positive. Increasing arithmetic precision would not fix the old positive-margin rejection.

For a padded complex axis with real part x in [a+l-p,a+T+p] and imaginary magnitude at most p, `Re(1/(a+t))=x/(x^2+y^2)`. The smallest value at fixed x occurs at |y|=p. The derivative of `x/(x^2+p^2)` has numerator `p^2-x^2`, so it has at most an interior maximum and its minimum on a positive interval occurs at an endpoint. Taking the smaller endpoint value is therefore a valid lower bound; averaging the two axis bounds gives a positive sigma bound.

The planner chooses p no larger than l/4 and (T-l)/4, so the padded rectangle remains strictly inside Re(t)>0. Its recorded margin comparison is exact rational arithmetic. Fresh independent exact-complex samples checked 48 synthetic domains and 3,024 points, including upper endpoints 2^192 and very narrow pilot windows; all satisfy the reported sigma lower bound and worker margin. These samples corroborate the analytic argument; they do not replace it. Actual computed Arb balls still have to pass their original whole-ball guards, and over-wide balls may be refused.

## Cache and compilation boundary

The cached kernel includes the immutable baseline callback translation unit exactly once. Its helper results are invocation-local and indexed by the exact polynomial degree, with unchanged parameters, working precision and complex input balls. The original coefficient multiplication tree and term/sum order remain in place. The new bridge copies only the slice adapter and retains the full outer parameter box. Baseline and cached compilation are explicit modes; mode flags and source lists are included in the build manifest and checked before execution. No speedup, native array equality or complete integrand range acceptance follows from these source facts.

## Fresh commands and limits

Exactly one targeted pass was run after the owner’s final source-freeze notification:

- In `native_driver/`: `python -B -m unittest -v test_driver` — exit 0, **16 tests PASS**.
- In `interior_design/`: `python -B -m unittest -v test_planner` — exit 0, **5 tests PASS**.
- Independent exact Fraction sampling of padded products and the legacy-margin counterexample — exit 0, **48 domains / 3,024 samples PASS**.

Logs: `NATIVE_DRIVER_TEST_LOG.txt`, `INTERIOR_DESIGN_TEST_LOG.txt`; machine-readable exact-check identities and counts: `NATIVE_DRIVER_EXACT_REVIEW_CHECKS.json`. The source hashes observed during these checks match the frozen hashes above.

Generation-time domain-plan driver identity is a historical snapshot, as documented by the owner’s separate `DOMAIN_BINDING_UPDATE.json`. A final run must use the final source/build identity and the appropriate baseline/cached manifest; the snapshot is not silently rewritten. Full-grid scheduling, all-tile radius acceptance, native cached/baseline comparison and independent scientific decision review remain separate execution gates. This review requests no additional broad audit loop.
