---
layout: default
title: "trans2"
---

# _6.1.1 Best Subset Selection_ 
# 6.1.1 최적 부분집합 선택 (Best Subset Selection): 무식하지만 확실한 드림팀 선발전

To perform _best subset selection_, we fit a separate least squares regression best subset for each possible combination of the $p$ predictors. That is, we fit all $p$ models that contain exactly one predictor, all $\binom{p}{2} = p(p-1)/2$ models that contain exactly two predictors, and so forth. We then look at all of the resulting models, with the goal of identifying the one that is _best_. 
이 **'최적 부분집합 선택(Best Subset Selection)'** 이라는 오디션 방식은 굉장히 무식하면서도 확실합니다. 타겟을 맞추기 위해 존재하는 전체 $p$ 명의 참가자(Predictors)들을 가지고 고를 수 있는 세상의 모.든.경.우.의.수(every possible combination) 조 제비뽑기를 다 돌려서, 수천수만 개의 예선 팀(별도의 모델)들을 각각 따로 만들어 전부다 최소 제곱법 피팅 훈련(Fit)을 시켜보는 극단적인 노가다 전법입니다.
좀 더 쉽게 풀어볼까요? 오직 참가자 단 1명으로만 이루어진 팀 모델을 총 $p$ 개 만들어 돌리고, 그다음엔 딱 2명으로만 짝을 지은 콤비 팀 모델 고작 $\binom{p}{2} = p(p-1)/2$ 개 조합을 몽땅 돌리고, 그다음엔 3인조, 4인조... 이런 미친듯한 완전 탐색 무한 스크롤 전개(and so forth)를 끝까지 밀고 나갑니다. 
이렇게 수만 번의 예선을 거치며 탄생한 수많은 결과 모델(resulting models) 무리들을 경기장 스크린에 쭉 띄워두고(Look at), 그 속에서 단 하나의 **'초우주 최강 넘사벽 챔피언 팀(Best)'** 모델을 정확하게 지목 식별 발탁 색출해 내는(Identifying) 것이 이 대장정 오디션의 궁극적 최종 조준 과녁(Goal)입니다.

The problem of selecting the _best model_ from among the $2^p$ possibilities considered by best subset selection is not trivial. This is usually broken up into two stages, as described in Algorithm 6.1. 
수학을 조금 공부했다면 눈치채셨겠지만, 이런 전수조사 노가다 방식에 의해 생성되는 전체 참전자 콤비 파벌의 경우의 수는 자그마치 **$2^p$ 개($2^p$ possibilities)** 라는 은하계 급 극악의 팽창 숫자를 자랑합니다. 이 어마무시한 빅뱅 우주 속에서 감히 **'유일신 챔피언 모델(Best model)'** 하나를 손가락으로 콕 집어 골라내야(Selecting) 하는 이 선발 문제는 여간 골때리고 빡센 사안(Not trivial)이 아닙니다. 참가 변수가 10개 언저리일 때야 상관없지만 조금만 많아져도 연산량이 폭발해 버리죠. 그래서 이 가혹한 선택 궤도는 한방에 결판 내는 게 아니라, 보통 후술 되는 **'알고리즘 6.1 (Algorithm 6.1)'** 에 기재된(Described) 구조처럼 아주 영리한 이중 필터 2단계(Two stages) 검열 관문 절차로 쪼개져서(Broken up) 신중하게 타파 진행됩니다.

---

## Sub-Chapters (하위 목차)

### Algorithm 6.1 Best subset selection (알고리즘 6.1 최적 부분집합 선택)
* [문서로 이동하기](./6_1_1_1_algorithm_6.1_best_subset_selection/trans2.html)

모든 K크기의 변수 조합에서 가장 좋은 모델을 기록하고, 최종적으로 Cross-Validation이나 AIC/BIC 평가지표로 모델 1개를 선정하는 절차입니다.
