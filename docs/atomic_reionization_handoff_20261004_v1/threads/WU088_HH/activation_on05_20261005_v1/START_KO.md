# HH-ON05A: matched ON/OFF 시간격자 비교

판정: `MATCHED_TWO_GRID_HH_CONTRAST_MEASURED__ANISOTROPIC_MODULATION_UNRESOLVED`.

이번 단위는 ON04에서 빠진 fine-grid OFF 두 이력만 계산한 HH-ON05A다. HH 연구는 ACTIVE이며 새 승인 대기로 돌아가지 않는다. 기존 ON04 이력 6개를 재사용했고 새 ON/KS 실행이나 solver 변경은 없다. HH-ON05 전체의 event-aware 단계는 아직 미구현인 ON05B로 남는다.

## 새 결과

D_g(h)=xHII_LCS,g(h)-xHII_OFF,g(h), h=1e10s, fine h/2=5e9s, t_end=8e11s다. 두 기하의 원 S0 입력, 32개 각도 노드, 기존 endpoint birth와 고정 midpoint source를 유지했다. 전체 S0 horizon의 8%이며 연속체 실험이 아니다.

| 기하 | coarse D | fine D | fine-coarse | abs변화/abs fine |
|---|---:|---:|---:|---:|
| FLRW | 8.058612666062004e-8 | 8.070283652461541e-8 | 1.1670986399536787e-10 | 0.1446168053% |
| Bianchi-I | 8.062401801733898e-8 | 8.070342083499327e-8 | 7.940281765428381e-11 | 0.0983884163% |

ON 단독의 큰 fine-coarse 변화와 OFF의 변화가 대부분 상쇄된다. 그러나 위 비율은 두 격자의 변화량이지 참해 오차 상계나 0.15% 정확도 인증이 아니다. 같은 해상도의 ON/OFF는 source/birth가 일치하지만 해상도를 바꾸면 birth quadrature도 달라지므로 여러 이산화 효과가 섞인다.

HH 효과의 비등방 변조 A(h)=D_Bianchi(h)-D_FLRW(h)는 coarse3.789135671894428e-11, fine5.843103778602199e-13으로 coarse/fine=64.8479954398632다. A는 전체 geometry contrast가 아니라 HH contribution의 double difference다. 온도 변조는 -1.461492502130568e-6K에서 -3.4058757591992617e-8K로 바뀌며 비는42.91091647083957이다. 따라서 전체 HH shift의 두 격자 근접성과 그 미소 비등방 변조의 수렴 미확인을 구분한다. 물리적 비등방 HH 신호를 발견했다거나 HH 전체가 numerical noise라고 결론내리지 않는다.

## 실행과 검사

새 native2회, compile1회, acceptedmacro320/child640/BEconstituent960, 모두exit0. 원 scientific Rust23path/hash와 compiler bytes가 fineLCS와 같다. 원 실행기의 HH-ON04 task 문자열은 보존하고 외부 실행영수증을 ON05A로 결속했다. coarse와 fine source_digest 차이는 unused test source2개 때문이며 실제 컴파일 과학 소스의 변경이 아니다.

새 OFF 출력에만 원 independent checker를 각각 실행해11548assertions/24selectedBEroots 통과. 최대root차2.632359905836515e-16, same-endpoint event상대차7.5636064657257e-15, exact누적energy절대잔차1.5127447929103928e-14<1e-12, 전자+photon결손1.1749893672350207e-15<1e-12, localmax5.045724459984413e-5<2e-4다. shared sigma가 원자율 독립 인증은 아니다.

4쌍의 기존/새 ON-OFF 이력을 읽어960개 accepted record pair에서 time,nH,H,광자energy,sigma,source/birth가 동일함을15928assertions로 검사했다. gas와 photon count 결과를 같게 강제하지 않는다. exact dyadic 차이652identity검사와 analysis unit9개가 통과했다. 최초 잘못된 stub의6failure/3error를 보존하고, shape-correct stub에서9assertion RED 뒤9GREEN, 최종9PASS다. 전체 pipeline을 TDD라고 하지 않는다. 마지막 검증은 source/결과/Decimal대조/구문/시험70checks였고 native/root는 재실행하지 않았다.

## 다음과 S0 경계

canonical S0는 OFF 보존, 실제 fixed-energy F08 point+interval/Jet2/root/event/model/checkpoint binding은 미연결이다. source-derived cohort research dispatcher를 F08 생산 실행기로 재명명하지 않는다. 전체 HH-ON1e13s, 새 연속 ODE, 각도정밀화, event-aligned history는 미실행이다. ON05B는 기존 nominal birth time/energy/direction/weight를 먼저 고정하고 양쪽 기하의 두 HI 문턱 crossing을 공통 격자에 삽입한다. 새 internal event boundary에 photon을 추가 생성하면 source quadrature까지 바뀌므로 금지한다. 문턱13.6/13.598434599702eV와 below-threshold count+energy retention은 그대로다. NEXT_EVENT_GRID_CONTRACT를 따른다.

원자 suite/NCP/HHprimitive/fullF08F09/독립 reviewer실행0. Legacy24/289,265unbounded,epsilon_C/R=null,B22OPEN과 consumed scopes 보존. physical/production/continuum admission=false.

## 재현과 백업

전체 새 raw gzip출력, exact 비교곡선, 원source cache, 실행기/checker, 입력/argv/exit/실패, 상세보고서는 `WU088_HH_ON05_MATCHED_CONTRAST_20261005_v1.zip`에 있다. 44445145bytes,147entries/146payloads, SHA256 `bcebb4011f0bbe13bf69fd616865eb2eaacaf1438615802656bb370dc189e22d`. Drive ID `1mUUEUg76EXBMCVADxWc2mTZFC0GkqYBY`, Dropbox ID `id:BSpOijBcT10AAAAAADzGlQ`. 기존 두 provider 목적지에 create-only 완료, ID/name/size 확인한 R1이며 새 output fullrestore=false다.

Git analysis core와9tests, NEXT_EVENT_GRID_CONTRACT, S0_SWITCH_DECISION은 ZIP과 byte동일하다. 이 START/요약은 상세보고서와 byte동일하지 않다. Git폴더는 전체 native 독립재현 패키지가 아니며 REPRODUCE_KO와 원 ON04 ZIP 입력을 함께 읽는다. 원ON04 scientific evidence는 재실행하지 않고 지정 hash로 재사용한다.

HH parent1a91c16141ad9d81076835df8fbbaa529180dfa4, REI8629a63059597d4fdd01be0f4e3c8b120a7766d0는 게시 전에도 같았다. 같은 HH branch non-force append, PR33와 REI반환 PR83. 댓글 게시와 소비자 채택은 별개다.
