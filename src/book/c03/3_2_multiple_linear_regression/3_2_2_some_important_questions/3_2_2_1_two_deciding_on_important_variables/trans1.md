---
layout: default
title: "trans1"
---

[< 3.2.2 Some Important Questions](../trans1.html) | [3.2.2.2 Three Model Fit >](../3_2_2_2_three_model_fit/trans1.html)


> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# Two: Deciding on Important Variables

# 질문 2: 중요한 변수 결정 (Two: Deciding on Important Variables)

As discussed in the previous section, the first step in a multiple regression analysis is to compute the $F$-statistic and to examine the associated $p$-value.

이전 섹션에서 논의했듯이, 다중 회귀 분석의 첫 번째 단계는 $F$-통계량을 계산하고 연관된 $p$-값을 조사하는 것입니다.

If we conclude on the basis of that $p$-value that at least one of the predictors is related to the response, then it is natural to wonder _which_ are the guilty ones!

해당 $p$-값을 토대로 적어도 하나의 예측 변수가 응답과 연관되어 있다고 결론 내린다면 자연스럽게 _어떤_ 변수들이 그 원인(유죄)인지 궁금해질 것입니다!

We could look at the individual $p$-values as in Table 3.4, but as discussed (and as further explored in Chapter 13), if $p$ is large we are likely to make some false discoveries.

표 3.4 에서와 같이 개별 $p$-값들을 살펴볼 수도 있겠지만, 앞서 논의한 대로 (그리고 13장에서 더 깊이 탐구하겠지만) 만약 $p$ 개수가 크다면 우리는 일부 잘못된 발견을 할 가능성이 높습니다.

It is possible that all of the predictors are associated with the response, but it is more often the case that the response is only associated with a subset of the predictors.

모든 예측 변수가 응답 변수와 연관되어 있을 수도 있지만, 응답 변수가 변수들의 부분집합에만 연관되어 있는 경우가 훨씬 더 흔합니다.

The task of determining which predictors are associated with the response, in order to fit a single model involving only those predictors, is referred to as _variable selection_.

해당 예측 변수들만을 포함하는 단일 모델을 적합하기 위해 어느 예측 변수들이 응답 변수와 통계적으로 연관되어 있는지 결정해 내는 임무 과정을 _변수 선택(variable selection)_ 이라고 부릅니다.

The variable selection problem is studied extensively in Chapter 6, and so here we will provide only a brief outline of some classical approaches.

선택 문제의 변수는 6장에서 매우 광범위하게 연구되기 때문에, 여기서는 일부 고전적인 접근법에 대한 간략한 윤곽만을 제공할 것입니다.

Ideally, we would like to perform variable selection by trying out a lot of different models, each containing a different subset of the predictors.

이상적으로 우리는 각각 다른 구성의 예측 변수 부분집합을 포함하는 많은 다양한 모델을 시도함으로써 변수 선택을 수행하고자 합니다.

For instance, if $p = 2$, then we can consider four models: (1) a model containing no variables, (2) a model containing $X_1$ only, (3) a model containing $X_2$ only, and (4) a model containing both $X_1$ and $X_2$.

예를 들어 만약 $p = 2$ 라면, 우리는 다음의 네 가지 모델을 고려할 수 있습니다: (1) 변수를 포함하지 않는 모델, (2) 오직 $X_1$ 만 포함하는 모델, (3) 오직 $X_2$ 만 포함하는 모델, 그리고 (4) $X_1$ 과 $X_2$ 모두를 포함하는 모델입니다.

We can then select the _best_ model out of all of the models that we have considered.

그런 다음 고려한 모든 모델들 중에서 _최고의_ 모델을 선택할 수 있습니다.

How do we determine which model is best?

어떤 모델이 가장 우수한지 어떻게 결정합니까?

Various statistics can be used to judge the quality of a model. These include Mallow's $C_p$, Akaike information criterion (AIC), Bayesian information criterion (BIC), and adjusted $R^2$.

모델의 품질을 판단하는 데 있어 다양한 통계를 사용할 수 있습니다. 여기에는 맬로의 $C_p$ (Mallow's $C_p$), 아카이케 정보 기준(AIC), 베이즈 정보 기준(BIC), 그리고 조정된 결정 계수(adjusted $R^2$) 가 포함됩니다.

These are discussed in more detail in Chapter 6.

이것들은 6장에서 더 구체적으로 다루어집니다.

We can also determine which model is best by plotting various model outputs, such as the residuals, in order to search for patterns.

우리는 패턴을 찾기 위해 잔차(residuals) 같은 다양한 모델 결과물 그래프를 표시함으로써 가장 좋은 모델을 가려낼 수 있습니다.

Unfortunately, there are a total of $2^p$ models that contain subsets of $p$ variables.

불행히도, $p$ 개의 변수의 부분집합을 가지는 모델들은 그 총합이 자그마치 $2^p$ 개입니다.

This means that even for moderate $p$, trying out every possible subset of the predictors is infeasible.

이는 중간 정도의 $p$ 에 대해서조차 예측 변수의 가능한 모든 부분집합을 시도해 보는 것이 실현 불가능함을 의미합니다.

For instance, we saw that if $p = 2$, then there are $2^2 = 4$ models to consider.

가령, 우리가 방금 전 보았듯 만일 $p = 2$ 이면 단지 $2^2 = 4$ 만큼의 모델들만 고려하면 됩니다.

But if $p = 30$, then we must consider $2^{30} = 1,073,741,824$ models! This is not practical.

하지만 만일 $p = 30$ 라면, 우리는 약 $2^{30} = 1,073,741,824$ 개의 셈법을 필히 고려해야만 합니다! 이것은 실용적이지 않습니다.

Therefore, unless $p$ is very small, we cannot consider all $2^p$ models, and instead we need an automated and efficient approach to choose a smaller set of models to consider.

그러므로 $p$ 가 웬만큼 매우 작지 않은 이상 우리는 모든 $2^p$ 종 모델들을 통째로 고려할 수는 없으며, 대신 더 적은 수의 고려 모델군을 선택할 자동화되고 효율적인 접근 방식이 필요합니다.

There are three classical approaches for this task:

이 작업을 수행하기 위한 세 가지의 전통적인 고전 접근법이 존재합니다:

- _Forward selection_. We begin with the _null model_ — a model that contains an intercept but no predictors. We then fit $p$ simple linear regressions and add to the null model the variable that results in the lowest RSS. We then add to that model the variable that results in the lowest RSS for the new two-variable model. This approach is continued until some stopping rule is satisfied.

- _전진 선택(Forward selection)_. 우리는 절편만 포함하고 예측 변수는 전혀 포함하지 않는 모델인 _영 모델(null model)_ 에서 시작합니다. 그런 다음 $p$ 개의 단순 선형 회귀를 적합하고, 가장 낮은 RSS 를 야기하는 변수를 영 모델에 추가합니다. 이어서 새롭게 탄생한 그 모델을 상대로 최저 RSS 를 만족할 두 번째 모델 변수를 추가합니다. 이 접근법은 어떤 정지 규칙을 달성하고 만족할 때까지 계속됩니다.

- _Backward selection_. We start with all variables in the model, and remove the variable with the largest $p$-value — that is, the variable that is the least statistically significant. The new $(p - 1)$-variable model is fit, and the variable with the largest $p$-value is removed. This procedure continues until a stopping rule is reached. For instance, we may stop when all remaining variables have a $p$-value below some threshold.

- _후진 선택(Backward selection)_. 우리는 모델 안에 모든 변수를 전부 집어넣은 풀 상태로 시작하여 가장 큰 $p$-값을 가진 변수 — 즉, 통계적으로 가장 덜 유의미한 변수를 모델에서 제거합니다. $(p - 1)$ 개의 변수를 가진 새로 적합된 모델에서 다시 가장 큰 $p$-값을 뽐내는 변수를 색출해 또 제거합니다. 이 절차는 정지 규칙에 도달할 때까지 끈질기게 계속 나아갑니다. 예를 들어, 남아있는 모든 변수들의 $p$-값이 싹 다 기준 임계값 수위 미만으로 집절될 때 우리는 작업을 멈출 수 있습니다.

- _Mixed selection_. This is a combination of forward and backward selection. We start with no variables in the model, and as with forward selection, we add the variable that provides the best fit. We continue to add variables one-by-one. Of course, as we noted with the `Advertising` example, the $p$-values for variables can become larger as new predictors are added to the model. Hence, if at any point the $p$-value for one of the variables in the model rises above a certain threshold, then we remove that variable from the model. We continue to perform these forward and backward steps until all variables in the model have a sufficiently low $p$-value, and all variables outside the model would have a large $p$-value if added to the model.

- _혼합 선택(Mixed selection)_. 본 제안은 앞서 설명한 전진 방식과 후진 방식 결합체입니다. 모델에 변수가 없는 상태로 출발하여, 전진 선택처럼 최상의 결과를 가져다주는 변수를 차례대로 투입 추가합니다. 이후 다시금 우리는 변수 묶음을 점진적으로 하나씩 누적해 쌓아 나갑니다. 다만 `Advertising` 사례를 기약하며 살펴본 바, 모델 내부에 새로운 성격의 예측 요소가 조금이라도 추가될 때마다 기존 변수들이 할양하는 $p$-값들은 순차적으로 더 커질 수 있습니다. 이런 연유로, 어느 시점에서 모델 안에 있던 한 변수의 당당한 $p$-값이 모종의 특정 임계 수준 위로 치솟아 오른다면, 지체 없이 우린 해당 변수를 도로 모델 밖으로 제거 및 축출해 버립니다. 결국 우리는, 잔여하는 모델 변수 요원 전체가 보장받은 아주 충분히 낮은 값어치의 $p$-값을 온전히 손에 죄다 지니도록, 더불어 추가 여지가 남아 모델 테두리 바깥을 서성이는 변수를 새로 투입 추가할 시 전부 높은 $p$-값 불량 스코어 수위를 발생시키게 될 상태로 수렴 안정될 시기까지, 계속해서 으레 앞뒤 전후 전·후진 단계를 거듭해 오가며 수행합니다.

Backward selection cannot be used if $p > n$, while forward selection can always be used.

전진 선택은 그 어떤 상황에서도 활용 가능하지만, 반면 역방향의 후진 선택법은 $p > n$ 인 열악한 관측 환경의 경우엔 부적합해 사용될 수 없습니다.

Forward selection is a greedy approach, and might include variables early that later become redundant. Mixed selection can remedy this.

동시에 전진 선택 방식은 탐욕적인(greedy) 알고리즘 체제이며 향후 짐만 되는 잉여성 중복 부품으로 전락할 변수를 초기 단계에 미리 덜컥 채용해 포함할 수 있는데, 이런 단점을 혼합 선택법이 직접 보완 조양하여 구제해 낼 수 있습니다.

---

## Sub-Chapters (하위 목차)


[< 3.2.2 Some Important Questions](../trans1.html) | [3.2.2.2 Three Model Fit >](../3_2_2_2_three_model_fit/trans1.html)
