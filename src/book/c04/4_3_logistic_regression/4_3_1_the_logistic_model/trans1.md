---
layout: default
title: "trans1"
---

[< 4.3 Logistic Regression](../trans1.html) | [4.3.2 Estimating The Regression Coefficients >](../4_3_2_estimating_the_regression_coefficients/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 4.3.1 The Logistic Model
# 4.3.1. 로지스틱 모형 (The Logistic Model)

How should we model the relationship between $p(X) = \text{Pr}(Y=1 \mid X)$ and $X$?
우리는 $p(X) = \text{Pr}(Y=1 \mid X)$ 와 $X$ 사이의 관계를 어떻게 모델링해야 할까요?

(For convenience we are using the generic 0/1 coding for the response.)
(편의를 위해 종속 변수에 대해 일반적인 0/1 코딩을 사용한다고 가정합니다.)

In Section 4.2 we considered using a linear regression model to represent these probabilities:
4.2절에서 우리는 이러한 확률들을 나타내기 위해 선형 회귀 모델을 사용하는 것을 고려했었습니다:

$$
p(X) = \beta_0 + \beta_1 X
$$

If we use this approach to predict `default` = `Yes` using `balance`, then we obtain the model shown in the left-hand panel of Figure 4.2.
만약 이 접근법을 사용하여 `balance`로 `default` = `Yes`를 예측한다면, 그림 4.2의 왼쪽 패널에 표시된 모델을 얻게 됩니다.

Here we see the problem with this approach: for balances close to zero we predict a negative probability of default; if we were to predict for very large balances, we would get values bigger than 1.
여기서 우리는 이 접근법의 문제점을 봅니다: 잔고가 0에 가까울 때 파산 확률을 음수로 예측하며; 매우 큰 잔고에 대해 예측할 경우 1보다 큰 값을 얻게 됩니다.

These predictions are not sensible, since of course the true probability of default, regardless of credit card balance, must fall between 0 and 1.
물론 실제 파산 확률은 신용카드 잔고와 무관하게 0과 1 사이에 있어야 하므로, 이러한 예측은 이치에 맞지 않습니다.

This problem is not unique to the credit default data.
이 문제는 신용카드 체납 데이터에만 국한되지 않습니다.

Any time a straight line is fit to a binary response that is coded as 0 or 1, in principle we can always predict $p(X) < 0$ for some values of $X$ and $p(X) > 1$ for others (unless the range of $X$ is limited).
0 또는 1로 코딩된 이진 응답 변수에 직선을 피팅할 때마다, 원칙적으로 ($X$의 범위가 극도로 제한되지 않는 한) 항상 일부 $X$ 값에 대해서는 $p(X) < 0$을, 다른 값들에 대해서는 $p(X) > 1$을 예측할 수 있습니다.

To avoid this problem, we must model $p(X)$ using a function that gives outputs between 0 and 1 for all values of $X$.
이 문제를 피하려면, 모든 $X$ 값에 대해 0과 1 사이의 출력값을 내놓는 함수를 사용하여 $p(X)$를 모델링해야 합니다.

Many functions meet this description.
이러한 조건을 만족하는 함수는 많습니다.

In logistic regression, we use the _logistic function_,
로지스틱 회귀에서는 **로지스틱 함수(logistic function)** 를 사용합니다:

$$
p(X) = \frac{e^{\beta_0 + \beta_1 X}}{1 + e^{\beta_0 + \beta_1 X}} \quad (4.2)
$$

To fit the model (4.2), we use a method called _maximum likelihood_, which we discuss in the next section.
모형 (4.2)을 적합시키기 위해, 우리는 다음 절에서 논의할 **최대 우도(maximum likelihood)** 라는 방법을 사용합니다.

The right-hand panel of Figure 4.2 illustrates the fit of the logistic regression model to the `Default` data.
그림 4.2의 오른쪽 패널은 `Default` 데이터에 대한 로지스틱 회귀 모델의 적합을 보여줍니다.

Notice that for low balances we now predict the probability of default as close to, but never below, zero.
이제 잔고가 낮을 때 체납 확률을 0에 가깝지만 결코 0 미만으로는 예측하지 않음에 주목하십시오.

Likewise, for high balances we predict a default probability close to, but never above, one.
마찬가지로, 높은 잔고에 대해서는 파산 확률을 1에 가깝지만 결코 1을 넘지 않게 예측합니다.

The logistic function will always produce an _S-shaped_ curve of this form, and so regardless of the value of $X$, we will obtain a sensible prediction.
로지스틱 함수는 항상 이런 형태의 **S자 모양(S-shaped)** 곡선을 생성하므로, $X$의 값에 관계없이 우리는 합리적인 예측을 얻을 수 있습니다.

We also see that the logistic model is better able to capture the range of probabilities than is the linear regression model in the left-hand plot.
또한 우리는 왼쪽 그래프의 선형 회귀 모형보다 로지스틱 모형이 확률의 범위를 더 잘 포착함을 볼 수 있습니다.

The average fitted probability in both cases is 0.0333 (averaged over the training data), which is the same as the overall proportion of defaulters in the data set.
두 경우 모두 평균 적합 확률은 0.0333(훈련 데이터에 대한 평균)이며, 이는 데이터셋 내 전체 체납자 비율과 동일합니다.

After a bit of manipulation of (4.2), we find that
수식 (4.2)를 약간 조작해보면, 우리는 다음을 발견합니다:

$$
\frac{p(X)}{1 - p(X)} = e^{\beta_0 + \beta_1 X} \quad (4.3)
$$

The quantity $p(X) / [1 - p(X)]$ is called the _odds_, and can take on any value between 0 and $\infty$.
값 $p(X) / [1 - p(X)]$은 **오즈(odds, 승산)** 라고 불리며, 0과 무한대($\infty$) 사이의 모든 값을 취할 수 있습니다.

Values of the odds close to 0 and $\infty$ indicate very low and very high probabilities of default, respectively.
0과 $\infty$에 가까운 오즈 값은 각각 체납 확률이 매우 낮거나 매우 높음을 나타냅니다.

For example, on average 1 in 5 people with an odds of $1/4$ will default, since $p(X) = 0.2$ implies an odds of $0.2 / (1 - 0.2) = 1/4$.
예를 들어, 오즈가 $1/4$인 그룹에서는 5명 중 평균 1명이 파산합니다. 왜냐하면 $p(X) = 0.2$는 오즈가 $0.2 / 0.8 = 1/4$ 임을 의미하기 때문입니다.

Likewise, on average nine out of every ten people with an odds of 9 will default, since $p(X) = 0.9$ implies an odds of $0.9 / (1 - 0.9) = 9$.
마찬가지로, 오즈가 9인 그룹에서는 10명 중 평균 9명이 파산하게 되는데, 이는 $p(X) = 0.9$가 오즈 $0.9 / 0.1 = 9$ 를 의미하기 때문입니다.

Odds are traditionally used instead of probabilities in horse-racing, since they relate more naturally to the correct betting strategy.
오즈는 올바른 베팅 전략과 더 자연스럽게 연관되기 때문에 경마 등에서 전통적으로 확률 대신 사용되어 왔습니다.

By taking the logarithm of both sides of (4.3), we arrive at
수식 (4.3)의 양변에 로그($\log$)를 취하면 다음 식에 도달합니다:

$$
\log\left( \frac{p(X)}{1 - p(X)} \right) = \beta_0 + \beta_1 X \quad (4.4)
$$

The left-hand side is called the _log odds_ or _logit_.
이 수식의 좌변은 **로그 오즈(log odds)** 또는 **로짓(logit)** 이라고 불립니다.

We see that the logistic regression model (4.2) has a logit that is linear in $X$.
우리는 로지스틱 회귀 모델 (4.2)이 $X$에 대해 선형성을 띠는 로짓 구조를 가짐을 확인할 수 있습니다.

Recall from Chapter 3 that in a linear regression model, $\beta_1$ gives the average change in $Y$ associated with a one-unit increase in $X$.
3장에서 다룬 선형 회귀 모형에서는, $\beta_1$이 $X$의 한단위 증가에 수반되는 $Y$의 평균적인 변화량을 나타냈다는 점을 상기하십시오.

By contrast, in a logistic regression model, increasing $X$ by one unit changes the log odds by $\beta_1$ (4.4).
대조적으로, 로지스틱 회귀 모형에서는 $X$를 한 단위 증가시키면 로그 오즈가 $\beta_1$만큼 변화합니다 (4.4).

Equivalently, it multiplies the odds by $e^{\beta_1}$ (4.3).
동일한 의미로, 이는 오즈 값에 $e^{\beta_1}$을 곱한 것과 같습니다 (4.3).

However, because the relationship between $p(X)$ and $X$ in (4.2) is not a straight line, $\beta_1$ does _not_ correspond to the change in $p(X)$ associated with a one-unit increase in $X$.
그러나 (4.2)에서 $p(X)$와 $X$의 관계가 직선 형태가 아니기 때문에, $\beta_1$은 $X$의 1단위 증가에 따른 $p(X)$의 실제 수치적 변화량에는 부합하지 **않습니다**.

The amount that $p(X)$ changes due to a one-unit change in $X$ depends on the current value of $X$.
$X$의 한 단위 변화로 인해 $p(X)$가 변하는 양은 현재 $X$의 위치(값)에 의존합니다.

But regardless of the value of $X$, if $\beta_1$ is positive then increasing $X$ will be associated with increasing $p(X)$, and if $\beta_1$ is negative then increasing $X$ will be associated with decreasing $p(X)$.
하지만 $X$ 값에 상관없이, 만약 $\beta_1$이 양수라면 $X$의 증가는 $p(X)$의 상승 기조와 무조건 연결되며, $\beta_1$이 음수라면 $X$의 증가는 $p(X)$의 하락 기조와 연결됩니다.

This is the document for this topic.
이것은 이 주제에 대한 문서입니다.

---

## Sub-Chapters

[< 4.3 Logistic Regression](../trans1.html) | [4.3.2 Estimating The Regression Coefficients >](../4_3_2_estimating_the_regression_coefficients/trans1.html)
