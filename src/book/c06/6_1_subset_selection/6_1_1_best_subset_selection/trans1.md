---
layout: default
title: "trans1"
---

# _6.1.1 Best Subset Selection_ 
# 6.1.1 최적 부분집합 선택 (Best Subset Selection)

To perform _best subset selection_, we fit a separate least squares regression best subset for each possible combination of the $p$ predictors. That is, we fit all $p$ models that contain exactly one predictor, all $\binom{p}{2} = p(p-1)/2$ models that contain exactly two predictors, and so forth. We then look at all of the resulting models, with the goal of identifying the one that is _best_. 
이른바 **'최적 부분집합 선택(best subset selection)'** 방식을 거행 수행(perform) 적용하기 위해, 우리는 $p$ 개의 예측 변수(predictors)들로 구성 조립 편성 짜 맞출 수 있는 모든 발생 가능 조합(every possible combination) 가지수 각각의 케이스마다 상호 독립 분리된 제각각의 별도(separate) 최소 제곱 회귀 모델을 일일이 모두 피팅 적합(fit)해 적용시켜 봅니다. 즉 다시 말해 통역해 보자면, 단 1개의 고립된 예측 변수만을 독단 보유 장착한 도합 $p$ 개의 세트 모델들을 남김없이 피팅 시도해 보고, 나아가 정확히 2개의 예측 변수만을 이면 포함 내포 수반하는 도합 $\binom{p}{2} = p(p-1)/2$ 체급 덩어리 갯수의 모델들을 역시 마찬가지로 죄다 깡그리 묶어 피팅시켜보며, 이와 같은 전개 방식 동일 양상 흐름을 그 너머로 계속 전진 지속(and so forth)해 나간다는 뜻입니다. 그런 후에 후반부에 도달하게 되면(We then), 종단에 산출 귀결 도출되어 파생 생산된 그 무수히 방대한 모든(all of the resulting) 관측 모델 개체군들 위쪽을 전면 조망 확인 주시 점검(look at)하게 되는데, 이 과정의 최종 목적 궁극 조준 과녁(goal)은 이들 경쟁자 무리 중 단연 압도적으로 가장 우수한 **'최고, 최상, 최적(best)'** 의 1등 모델 단 하나를 지목 판별 색출 식별 추출 가늠 판독해 내는(identifying) 데에 집중 조준 맞춰져 있습니다.

The problem of selecting the _best model_ from among the $2^p$ possibilities considered by best subset selection is not trivial. This is usually broken up into two stages, as described in Algorithm 6.1. 
이처럼 무식 무자비한 최적 부분집합 선택(best subset selection) 구도 설계망에 의해 대두 수렴 산출 고려 조명 계산된 도합 $2^p$ 개($2^p$ possibilities)라는 엄청난 극한 거대 숫자 후보군 범위 풀 판도 영토 틈(among) 속에서 그 단 1개의 참된 진성 **'최고 에이스 모델(best model)'** 표본을 감각 발탁 선택 채택(selecting)해 내야만 한다는 당면 퀘스트 이슈 문제(problem)는 여간 결코 쉽지 않으며 결코 시시 사소 만만 가볍 녹록한 사안(not trivial)이 아닙니다. 이 거대 국면 사안(This)은 대체로 십중팔구 통상 대개 보편 주로(usually) 아래 후단 **'알고리즘 6.1 (Algorithm 6.1)'** 에 상세 기입 명기 명료 묘사 서술 적시(described)되어 있는 바와 같이, 크게 양면 두 갈래 단계(two stages)의 순차 파편 구조 공정 국면 절차로 등분 분할 쪼개어 타파(broken up) 분리 타결 처리 진행됩니다.

---

## Sub-Chapters (하위 목차)

### Algorithm 6.1 Best subset selection (알고리즘 6.1 최적 부분집합 선택)
* [문서로 이동하기](./6_1_1_1_algorithm_6.1_best_subset_selection/trans1.html)

모든 K크기의 변수 조합에서 가장 좋은 모델을 기록하고, 최종적으로 Cross-Validation이나 AIC/BIC 평가지표로 모델 1개를 선정하는 절차입니다.
