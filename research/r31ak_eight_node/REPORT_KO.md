# R31AK: z=2.5 protocol-deviation closeout, eight-node successor, clean holdout design

기준 remote는 commit `a3bf6f0fbb6ab2e0d53a28cb72d403db0e48b925`, tree `0a384e8e12d3f3c5829e8fe0609cb2c223fb7363`이다.

Frozen numerical result는 `PARETO_SUPPORTED_AT_Z25`다. R31AI는 R31Z 대비 E_O 64.80%, E_dotO 76.94%, E_K 59.12%, E_Dmax 61.40% 낮다. 그러나 최초 frozen comparator는 OD identity의 numeric z와 JVP identity의 string z를 raw type으로 비교해 direct arrays를 읽기 전에 실패했고, output 생성 뒤 numeric metadata normalization adapter가 추가되었다. Model, predictions, metrics, tolerance, decision formula는 바뀌지 않았으므로 numerical result는 보존하지만, independent-validation gate는 소급 복원하지 않는다.

Canonical classification:
`NUMERICAL_RESULT_RETAINED__INDEPENDENCE_NOT_ADMITTED__METADATA_ONLY_RECOVERY`.

z=2.5 direct arrays는 successor training으로 사용할 수 있으며 provenance는
`PROTOCOL_DEVIATED_NUMERICAL_COMPARISON_CONSUMED_AS_R31AK_TRAINING`.

[2,3] midpoint residual에서 필요한 local necessary bounds:
- sup ||d4O/dt4|| >= 0.2947800782196966 /t_a^4
- sup ||d2K/dt2|| >= 0.13736267798030663 /t_a^3
- sup ||d4O/dz4|| >= 7.366987778521003 /a0^4
- sup ||d2K/dz2|| >= 0.6866962233874174 /(t_a a0^2).

R31AK는 기존 interpolation family를 바꾸지 않고 z=2.5 knot만 추가한 eight-node local h-refinement다:
`{0,0.5,1,2,2.5,3,3.5,4}`.

다음 clean holdout은 successor-cell midpoint 중 prior direct exposure가 없는 점에서 prediction-only selection한다. z=1.5는 prior OD-only exposure로 제외한다. Provisional candidates:
`{0.25,0.75,2.25,2.75,3.25,3.75}`.

현재 turn의 Dropbox/Drive title search는 이 provisional candidates에 대해 0 result였지만 absence proof로 사용하지 않는다. NCP follow-up에서 CP4 archive/local/provider metadata를 payload access 없이 다시 inventory한다.

Selection:
`S=sqrt(DeltaK_model^2+DeltaDmax_model^2)`, max S, tie -> lower z. S는 design only. Final direct verdict는 prelocked E_K/E_Dmax Pareto다.

z=2.5 protocol bug 재발 방지를 위해 metadata adapter를 output 전 구현했다. JSON number/string z를 Decimal로 canonicalize하고 invalid values를 reject한다. Focused tests 14 PASS, new science node 0.

Reference-error upper bound는 여전히 unavailable이다. z=2.5 margins의 common sensitivity budget 0.06206254082953607/t_a는 actual source-error bound가 아니다.

다음 NCP node는 existing eight-node replay + fresh holdout inventory + prediction-only selection + prereg lock까지만 수행하고 direct holdout을 실행하지 않는다.
