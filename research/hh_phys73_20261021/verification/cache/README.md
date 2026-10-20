# Analytic source, Coulomb cache, and native integration evidence

All files listed by COPY_RECEIPT.json are byte-identical copies of their original sandbox evidence. The cache check uses only l=0,1, radial 3 -> 5 nested sample nodes on [27,28], and mpmath dps40. It performs sample preparation without a scientific panel/profile integration.

CACHE_CHECK_RECEIPT.json records 14 passing checks, 40 actual F/G scalar evaluations across the initial, cached refined, and independent uncached sample preparations, identical cached/uncached N5 binary packets, zero-evaluation completed-preparation resume, and rejection of changed cache payloads or incompatible bindings. Cache hit counts include within-call reuse of B, even when persistent caching is disabled.

integrated/INTEGRATED_PIPELINE_RECEIPT.json records one native sweep and one native dense action on the already prepared N5 packet, followed by production original_source.summarize. It performs zero additional Coulomb evaluations and zero panel/profile integrations. Both outputs pass the independent finite-packet action check and have exactly zero sampled Dirichlet boundary. Dense/sweep difference is a floating-point comparison on this fixed packet; continuum, quadrature, angular/radial tail, and roundoff certificates are not inferred.

INTEGRATED_CACHE_CHECK_EXECUTED.py preserves the exact executed driver, including its original sandbox paths. The original preparation JSON/cache bindings and original logs have not been rewritten after copying.
