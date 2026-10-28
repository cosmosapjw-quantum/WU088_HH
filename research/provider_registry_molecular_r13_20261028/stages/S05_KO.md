# S05 · R5/C5 — 실제 증명·구현과 실행 전 동결

Exact affineoverlap, translatedevent, quadratic/vertex, nonnegativeBernstein2, signedpositiveweights, wholeRsup/wholeEmajorant, exactobservationaggregation을구현했다. 현재24validsyntheticcases와38rejectionguards를작성했다. Wholeforcingcanonicalhash는정확한함수와state/clock에서재계산하며actualFIXTURE_SOURCEbytes는primary에서검증한다. 모든새fixture는ARITHMETIC_CONTROL_PREMISE다.

PROOF_KO.md는directedintegerTaylorinduction까지구현과대응한다. R13-R6-F01 maximum/supremum표현을교정했고원본bytes를보존했다. R13-F02 primaryCLI/overwrite가능성을실행전에고쳤다. 교정전primaryhash는관측했으나그원본bytes는NOT_PRESERVED이며재구성하지않았다. Source의ASTparse는문법확인이고과학검증이아니다.

14개실행의존파일을SHA256으로동결했다. Primary/reference/CAS는아직0/0/0회이며S05게시·백업후각1회만수행한다. workflow10/20,과학DAG25/42. 새과학노드의채택은최종독립검토와실제검증후다.
