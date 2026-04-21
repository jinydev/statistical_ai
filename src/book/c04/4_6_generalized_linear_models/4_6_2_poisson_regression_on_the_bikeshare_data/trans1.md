---
layout: default
title: "trans1"
---

[< 4.6.1 Linear Regression On The Bikeshare Data](../4_6_1_linear_regression_on_the_bikeshare_data/trans1.html) | [4.6.3 Generalized Linear Models In Greater Generality >](../4_6_3_generalized_linear_models_in_greater_generality/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.6.2 Poisson Regression on the Bikeshare Data
# 4.6.2 Bikeshare 데이터에 대한 포아송 회귀

To overcome the inadequacies of linear regression for analyzing the `Bikeshare` data set, we will make use of an alternative approach, called _Poisson regression_.
`Bikeshare` 데이터 세트를 분석하기 위해 선형 회귀가 가지는 부적절함(inadequacies)을 극복하기 위해, 우리는 **포아송 회귀(Poisson regression)**라고 불리는 대안적인 접근법을 사용할 것입니다.

Before we can talk about Poisson regression, we must first introduce the _Poisson distribution_.
포아송 회귀에 대해 논의하기 전에, 우리는 먼저 **포아송 분포(Poisson distribution)**를 도입해야 합니다.

Suppose that a random variable $Y$ takes on nonnegative integer values, i.e. $Y \in \{0, 1, 2, \dots\}$.
어떤 확률 변수 $Y$가 음이 아닌 정수 값들, 즉 $Y \in \{0, 1, 2, \dots\}$ 을 취한다고 가정해 봅시다.

If $Y$ follows the Poisson distribution, then
만약 $Y$가 포아송 분포를 따른다면, 다음 식이 성립합니다.

$$
\text{Pr}(Y = k) = \frac{e^{-\lambda} \lambda^k}{k!} \quad \text{for } k = 0, 1, 2, \dots \quad (4.35)
$$

Here, $\lambda > 0$ is the expected value of $Y$, i.e. $E(Y)$.
여기서 $\lambda > 0$ 은 $Y$의 기댓값, 즉 $E(Y)$입니다.

It turns out that $\lambda$ also equals the variance of $Y$, i.e. $\lambda = E(Y) = \text{Var}(Y)$.
$\lambda$는 $Y$의 분산과도 같다는 것이 밝혀졌습니다. 즉, $\lambda = E(Y) = \text{Var}(Y)$ 입니다.

This means that if $Y$ follows the Poisson distribution, then the larger the mean of $Y$, the larger its variance.
이것은 만약 $Y$가 포아송 분포를 따른다면, $Y$의 평균(mean)이 커질수록 분산(variance) 또한 커진다는 것을 의미합니다.

The Poisson distribution is typically used to model _counts_; this is a natural choice for a number of reasons, including the fact that counts, like the Poisson distribution, take on nonnegative integer values.
포아송 분포는 일반적으로 **개수(counts)**를 모델링하는 데 사용됩니다; 이것은 포아송 분포와 마찬가지로 개수가 음이 아닌 정수 값을 취한다는 사실을 포함하여 여러 가지 이유로 자연스러운 선택입니다.

Rather than modeling the number of bikers, $Y$, as a Poisson distribution with a fixed mean value like $\lambda = 5$, we would like to allow the mean to vary as a function of the covariates.
자전거 이용자의 수 $Y$를 $\lambda = 5$와 같이 고정된 평균값을 가지는 포아송 분포로 모델링하는 대신, 우리는 그 평균이 공변량(covariates)들의 함수로서 변화하도록 허용하고자 합니다.

In particular, we consider the following model for the mean $\lambda = E(Y)$:
특히, 우리는 평균 $\lambda = E(Y)$에 대해 다음과 같은 모델을 고려합니다:

$$
\lambda(X_1, \dots, X_p) = e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p} \quad (4.36)
$$

or equivalently
또는 동등하게

$$
\log(\lambda(X_1, \dots, X_p)) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \quad (4.37)
$$

Here, $\beta_0, \beta_1, \dots, \beta_p$ are parameters to be estimated.
여기서 $\beta_0, \beta_1, \dots, \beta_p$는 추정해야 할 매개 변수들입니다.

Together, (4.35) and (4.36) define the Poisson regression model.
식 (4.35)와 (4.36)은 함께 포아송 회귀 모델을 정의합니다.

Notice that in (4.36), we take the _log_ of $\lambda(X_1, \dots, X_p)$ to be linear in $X_1, \dots, X_p$; this ensures that $\lambda(X_1, \dots, X_p)$ takes on nonnegative values for all values of the covariates.
(4.36) 식에서, 우리가 $\lambda(X_1, \dots, X_p)$의 **로그(log)**를 취하여 $X_1, \dots, X_p$에 대해 선형적이 되도록 한다는 점에 주목하십시오; 이는 공변량들의 모든 값들에 대해서 $\lambda(X_1, \dots, X_p)$가 항상 음이 아닌 값을 취하도록 보장합니다.

To estimate the coefficients $\beta_0, \beta_1, \dots, \beta_p$, we use the same maximum likelihood approach that we adopted for logistic regression in Section 4.3.2.
계수 $\beta_0, \beta_1, \dots, \beta_p$를 추정하기 위해, 우리는 4.3.2 절에서 로지스틱 회귀를 위해 채택했던 것과 동일한 최대 우도 접근법(maximum likelihood)을 사용합니다.

We estimate the coefficients that make the observed data as likely as possible.
우리는 관측된 데이터가 나타날 확률을 가능한 한 최대로 만드는 계수들을 추정합니다.

We now fit a Poisson regression model to the `Bikeshare` data set.
우리는 이제 `Bikeshare` 데이터 세트에 포아송 회귀 모델을 적합시킵니다.

Qualitatively, the results are similar to those from linear regression in Section 4.6.1.
정성적으로(Qualitatively), 그 결과는 4.6.1 절의 선형 회귀에서 얻은 결과와 유사합니다.

We again see that bike usage is highest in the spring and fall and during rush hour, and lowest during the winter and in the early morning hours.
우리는 자전거 이용이 봄과 가을 그리고 출퇴근 시간대에 가장 높고, 겨울과 이른 아침 시간에 가장 낮다는 것을 다시 한번 확인합니다.

Some important distinctions between the Poisson regression model and the linear regression model are as follows:
포아송 회귀 모델과 선형 회귀 모델 간의 몇 가지 중요한 차이점들은 다음과 같습니다:

- _Interpretation:_ To interpret the coefficients in the Poisson regression model, we must pay close attention to (4.37), which states that an increase in $X_j$ by one unit is associated with a change in $E(Y) = \lambda$ by a factor of $\exp(\beta_j)$. For example, a change in weather from clear to cloudy skies is associated with a change in mean bike usage by a factor of $\exp(-0.08) = 0.923$, i.e. on average, only 92.3% as many people will use bikes when it is cloudy relative to when it is clear.
- **해석(Interpretation):** 포아송 회귀 모델에서 계수들을 해석하기 위해, 우리는 (4.37) 식에 주의를 기울여야 하는데, 이 식은 $X_j$의 한 단위 증가가 $\exp(\beta_j)$ 라는 배수 팩터(factor)만큼의 평균 $E(Y) = \lambda$ 변화와 관련되어 있음을 나타냅니다. 예를 들어, 날씨가 맑음에서 흐림으로 변하는 것은 평균 자전거 이용량의 $\exp(-0.08) = 0.923$ 배로의 변화와 관련이 있습니다. 즉, 맑을 때 대비 흐릴 때 평균적으로 집단의 92.3% 만이 자전거를 사용할 것입니다.

- _Mean-variance relationship:_ As mentioned earlier, under the Poisson model, $\lambda = E(Y) = \text{Var}(Y)$. Thus, by modeling bike usage with a Poisson regression, we implicitly assume that mean bike usage in a given hour equals the variance of bike usage during that hour. Thus, the Poisson regression model is able to handle the mean-variance relationship seen in the `Bikeshare` data in a way that the linear regression model is not.
- **평균-분산 관계(Mean-variance relationship):** 앞서 언급했듯이, 포아송 모델 하에서는 $\lambda = E(Y) = \text{Var}(Y)$ 이 성립합니다. 따라서, 자전거 이용량을 포아송 회귀 예측으로 모델링함으로써, 우리는 주어진 시간대의 평균 대여량이 곧 해당 시간대 자전거 사용량의 분산과 동일하다는 것을 암묵적으로 가정하게 됩니다. 그러므로 포아송 회귀 모델은 직선형 통나무인 선형 회귀 모델이 다룰 수 없었던, `Bikeshare` 야생 데이터에서 관찰된 이 평균과 분산 간의 연결 관계를 시스템상으로 다룰 수 있습니다.

- _nonnegative fitted values:_ There are no negative predictions using the Poisson regression model. This is because the Poisson model itself only allows for nonnegative values.
- **음수 아닌 적합값(nonnegative fitted values):** 포아송 회귀 모델을 사용하면 음수 예측의 재앙이 발생하지 않습니다. 이는 포아송 모델 수학 모델링 자체가 본질적으로 음이 아닌 양수값의 정수 반환들만을 조립 허용하기 때문입니다.

---

## Sub-Chapters

[< 4.6.1 Linear Regression On The Bikeshare Data](../4_6_1_linear_regression_on_the_bikeshare_data/trans1.html) | [4.6.3 Generalized Linear Models In Greater Generality >](../4_6_3_generalized_linear_models_in_greater_generality/trans1.html)
