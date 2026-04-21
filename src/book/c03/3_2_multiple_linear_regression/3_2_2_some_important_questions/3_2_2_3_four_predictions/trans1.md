---
layout: default
title: "trans1"
---

[< 3.2.2.2 Three Model Fit](../3_2_2_2_three_model_fit/trans1.html) | [3.3 Other Considerations In The Regression Model >](../../../3_3_other_considerations_in_the_regression_model/trans1.html)


> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# Four: Predictions

# 질문 4: 예측 (Four: Predictions)

Once we have fit the multiple regression model, it is straightforward to apply (3.21) in order to predict the response $Y$ on the basis of a set of values for the predictors $X_1, X_2, \dots, X_p$.

다중 회귀 모델을 적합하고 나면, 예측 변수들 $X_1, X_2, \dots, X_p$ 의 일련의 값들을 기반으로 응답 $Y$ 를 예측하기 위해 수식 (3.21) 을 적용하는 것은 간단합니다.

However, there are three sorts of uncertainty associated with this prediction.

그러나 이 예측에는 세 가지 종류의 불확실성이 연관되어 있습니다.

1. The coefficient estimates $\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_p$ are estimates for $\beta_0, \beta_1, \dots, \beta_p$. That is, the _least squares plane_

1. 계수 추정치 $\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_p$ 는 $\beta_0, \beta_1, \dots, \beta_p$ 에 대한 추정치입니다. 즉, 다시 말해 _최소 제곱 평면(least squares plane)_ 인

$$
\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 X_1 + \dots + \hat{\beta}_p X_p
$$

is only an estimate for the _true population regression plane_

은 단지 _참 모집단 회귀 평면(true population regression plane)_ 인 다음에 대한 추정치일 뿐입니다.

$$
f(X) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p
$$

The inaccuracy in the coefficient estimates is related to the _reducible error_ from Chapter 2. We can compute a _confidence interval_ in order to determine how close $\hat{Y}$ will be to $f(X)$.

계수 추정치의 부정확성은 2장의 _축소 가능한 오차(reducible error)_ 와 관련이 있습니다. 우리는 $\hat{Y}$ 가 $f(X)$ 에 얼마나 가까울지 판별하기 위해 _신뢰 구간(confidence interval)_ 을 계산할 수 있습니다.

2. Of course, in practice assuming a linear model for $f(X)$ is almost always an approximation of reality, so there is an additional source of potentially reducible error which we call _model bias_.

2. 물론 실무 현장에서 $f(X)$ 에 대한 선형 모델을 가정하는 것은 거의 항상 현실에 대한 근사치이므로, 우리가 _모델 편향(model bias)_ 이라 부르는 잠재적인 축소 가능 오차의 추가적인 요인이 존재합니다.

So when we use a linear model, we are in fact estimating the best linear approximation to the true surface.

따라서 우리가 선형 모델을 사용할 때, 사실 우리는 진짜 표면에 대한 최선의 선형 근사치를 추정하고 있는 것입니다.

However, here we will ignore this discrepancy, and operate as if the linear model were correct.

하지만 여기서 우리는 이 불일치를 무시하고 선형 모델이 정확한 것처럼 다룰 것입니다.

3. Even if we knew $f(X)$ — that is, even if we knew the true values for $\beta_0, \beta_1, \dots, \beta_p$ — the response value cannot be predicted perfectly because of the random error $\epsilon$ in the model (3.20).

3. 비록 우리가 $f(X)$ 를 안다 해도 — 다시 말해, $\beta_0, \beta_1, \dots, \beta_p$ 의 실제 참값을 안다 해도 — 모델 (3.20) 의 무작위 오차 $\epsilon$ 때문에 응답 값을 완벽하게 예측할 수는 없습니다.

In Chapter 2, we referred to this as the _irreducible error_. How much will $Y$ vary from $\hat{Y}$? We use _prediction intervals_ to answer this question.

2장에서 우리는 이것을 _축소 불가능한 오차(irreducible error)_ 라고 불렀습니다. 응답 $Y$ 가 예측 $\hat{Y}$ 로부터 얼마나 다르게 변동할까요? 우리는 이 질문에 답하기 위해 _예측 구간(prediction intervals)_ 을 사용합니다.

Prediction intervals are always wider than confidence intervals, because they incorporate both the error in the estimate for $f(X)$ (the reducible error) and the uncertainty as to how much an individual point will differ from the population regression plane (the irreducible error).

예측 구간은 항상 신뢰 구간보다 넓은데, 이는 결과적으로 $f(X)$ 추정치의 오차(축소 가능한 오차)와, 개별 지점이 모집단 회귀 평면과 얼마나 다를지에 대한 불확실성(축소 불가능한 오차)을 모두 아우러 포함하기 때문입니다.

We use a _confidence interval_ to quantify the uncertainty surrounding the _average_ `sales` over a large number of cities.

우리는 수많은 도시에 걸친 _평균(average)_ `sales` 를 둘러싼 불확실성을 수량화하기 위해 _신뢰 구간(confidence interval)_ 을 사용합니다.

For example, given that $\$100,000$ is spent on `TV` advertising and $\$20,000$ is spent on `radio` advertising in each city, the $95\%$ confidence interval is $[10,985, 11,528]$.

예를 들어, 각 도시에서 `TV` 광고에 $\$100,000$ 가 지출되고 `radio` 광고에 $\$20,000$ 가 지출된다고 주어질 때 $95\%$ 신뢰 구간은 $[10,985, 11,528]$ 입니다.

We interpret this to mean that $95\%$ of intervals of this form will contain the true value of $f(X)$.[9]

우리는 이것을 이 형태의 구간 중 $95\%$ 가 $f(X)$ 의 참값을 포함할 것이라는 의미로 해석합니다.[9]

> [9] In other words, if we collect a large number of data sets like the `Advertising` data set, and we construct a confidence interval for the average `sales` on the basis of each data set (given $\$100,000$ in `TV` and $\$20,000$ in `radio` advertising), then $95\%$ of these confidence intervals will contain the true value of average `sales`.

> [9] 다시 말해, 만약 우리가 `Advertising` 데이터 세트와 같은 다수의 분량 데이터 세트들을 수집하고, 각각의 데이터 세트에 기초하여 평균 `sales` 에 대한 신뢰 구간을 모형 구축한다면 (`TV` 광고 $\$100,000$ 와 `radio` 광고 $\$20,000$ 가 주어질 때), 이 신뢰 구간의 $95\%$ 는 결국 평균 `sales` 의 참값을 포함할 것입니다.

On the other hand, a _prediction interval_ can be used to quantify the uncertainty surrounding `sales` for a _particular_ city.

한편, 어떤 _특정(particular)_ 도시에 대한 `sales` 범위 주변을 둘러싼 불확실성을 정량 계량화하는 데는 _예측 구간_ 이 사용될 수 있습니다.

Given that $\$100,000$ is spent on `TV` advertising and $\$20,000$ is spent on `radio` advertising in that city the $95\%$ prediction interval is $[7,930, 14,580]$.

그 নির্দিষ্ট 도시에서 `TV` 홍보에 $\$100,000$ 이 소비되고 `radio` 광고에 $\$20,000$ 이 소요된다는 조건에서, $95\%$ 예측 구간은 광활한 $[7,930, 14,580]$ 입니다.

We interpret this to mean that $95\%$ of intervals of this form will contain the true value of $Y$ for this city.

우리는 이를 바탕으로 이 형식을 가진 구간의 $95\%$ 가 이 도시의 참된 $Y$ 값을 포함할 것이라는 의미로 해석합니다.

Note that both intervals are centered at 11,256, but that the prediction interval is substantially wider than the confidence interval, reflecting the increased uncertainty about `sales` for a given city in comparison to the average `sales` over many locations.

주의해 되새길 점은 두 구간 모두 정중앙 한가운데를 11,256 으로 잡고 중심 타점을 공유하지만, 여러 곳의 전반 평균 `sales` 양상과 비교할 때 오직 어느 특화된 도시에 얽힌 `sales` 산출 불확실성이 증가됨을 크게 반영하므로, 결과적으로 예측 구간은 태생적으로 신뢰 구간보다 근본적으로 훨씬 더 두껍고 넓다는 것입니다.

---

## Sub-Chapters (하위 목차)


[< 3.2.2.2 Three Model Fit](../3_2_2_2_three_model_fit/trans1.html) | [3.3 Other Considerations In The Regression Model >](../../../3_3_other_considerations_in_the_regression_model/trans1.html)
