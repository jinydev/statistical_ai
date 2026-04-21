---
layout: default
title: "trans1"
---

[< 4.6.1 Linear Regression On The Bikeshare Data](../4_6_1_linear_regression_on_the_bikeshare_data/trans1.html) | [4.6.3 Generalized Linear Models In Greater Generality >](../4_6_3_generalized_linear_models_in_greater_generality/trans1.html)

> 💡 **학습 팁:** 이 페이지는 원문 형식을 최대한 존중한 **직역본**입니다. 내용이 어렵거나 수학적 설명이 딱딱하게 느껴진다면, 더 쉽고 비유적으로 풀어쓴 [🏄‍♂️ Vibe Coding 버전보기](./trans2.html)를 추천합니다!

# 4.6.2 Poisson Regression on the Bikeshare Data
# 4.6.2 Bikeshare 데이터에 대한 포아송 회귀

To overcome the inadequacies of linear regression for analyzing the `Bikeshare` data set, we will make use of an alternative approach, called _Poisson regression_. Before we can talk about Poisson regression, we must first introduce the _Poisson distribution_.
`Bikeshare` 데이터 세트를 분석하기 위한 선형 회귀의 부적절함을 극복하기 위해, 우리는 _포아송 회귀(Poisson regression)_ 라는 대안적 접근법을 사용할 것입니다. 포아송 회귀에 대해 이야기하기 전에 먼저 _포아송 분포(Poisson distribution)_ 를 소개해야 합니다.

Suppose that a random variable $Y$ takes on nonnegative integer values, i.e. $Y \in \{0, 1, 2, \dots\}$. If $Y$ follows the Poisson distribution, then
확률 변수 $Y$ 가 음이 아닌 정수 값을 취한다고 가정합니다, 즉 $Y \in \{0, 1, 2, \dots\}$. 만약 $Y$ 가 포아송 분포를 따른다면, 다음이 성립합니다:

$$
\text{Pr}(Y = k) = \frac{e^{-\lambda} \lambda^k}{k!} \quad \text{for } k = 0, 1, 2, \dots \quad (4.35)
$$

Here, $\lambda > 0$ is the expected value of $Y$, i.e. $E(Y)$. It turns out that $\lambda$ also equals the variance of $Y$, i.e. $\lambda = E(Y) = \text{Var}(Y)$. This means that if $Y$ follows the Poisson distribution, then the larger the mean of $Y$, the larger its variance.
여기서, $\lambda > 0$ 은 $Y$ 의 기댓값, 즉 $E(Y)$ 입니다. $\lambda$ 는 또한 $Y$ 의 분산과 같음이 밝혀졌습니다, 즉 $\lambda = E(Y) = \text{Var}(Y)$ 입니다. 이는 $Y$ 가 포아송 분포를 따른다면, $Y$ 의 평균이 클수록 그 분산도 커짐을 의미합니다.

The Poisson distribution is typically used to model _counts_; this is a natural choice for a number of reasons, including the fact that counts, like the Poisson distribution, take on nonnegative integer values. Rather than modeling the number of bikers, $Y$, as a Poisson distribution with a fixed mean value like $\lambda = 5$, we would like to allow the mean to vary as a function of the covariates. In particular, we consider the following model for the mean $\lambda = E(Y)$:
포아송 분포는 전형적으로 _개수(counts)_ 를 모델링하는 데 사용됩니다; 개수 역씨 포아송 분포와 같이 음이 아닌 정수 값을 취한다는 사실을 포함하여 여러 가지 이유로 이것은 자연스러운 선택입니다. 탑승자 수 $Y$ 를 $\lambda = 5$ 와 같이 고정된 평균 값을 갖는 포아송 분포로 모델링하는 대신, 우리는 평균이 공변량의 함수로서 변하도록 허용하고자 합니다. 특히, 평균 $\lambda = E(Y)$ 에 대해 다음 모델을 고려합니다:

$$
\lambda(X_1, \dots, X_p) = e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p} \quad (4.36)
$$

or equivalently
또는 동등하게

$$
\log(\lambda(X_1, \dots, X_p)) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \quad (4.37)
$$

Here, $\beta_0, \beta_1, \dots, \beta_p$ are parameters to be estimated. Together, (4.35) and (4.36) define the Poisson regression model. Notice that in (4.36), we take the _log_ of $\lambda(X_1, \dots, X_p)$ to be linear in $X_1, \dots, X_p$; this ensures that $\lambda(X_1, \dots, X_p)$ takes on nonnegative values for all values of the covariates.
여기서 $\beta_0, \beta_1, \dots, \beta_p$ 는 추정될 매개변수입니다. (4.35)와 (4.36)은 함께 포아송 회귀 모델을 정의합니다. (4.36)에서 $\lambda(X_1, \dots, X_p)$ 의 _로그(log)_ 가 $X_1, \dots, X_p$ 에 선형이 되도록 취했다는 것에 주목하십시오; 이는 공변량의 모든 값에 대해 $\lambda(X_1, \dots, X_p)$ 가 음이 아닌 값을 취하도록 보장합니다.

To estimate the coefficients $\beta_0, \beta_1, \dots, \beta_p$, we use the same maximum likelihood approach that we adopted for logistic regression in Section 4.3.2. We estimate the coefficients that make the observed data as likely as possible.
계수 $\beta_0, \beta_1, \dots, \beta_p$ 를 추정하기 위해, Section 4.3.2 의 로지스틱 회귀에 채택했던 것과 동일한 최대 우도 접근법(maximum likelihood approach)을 사용합니다. 관측된 데이터를 최대한 그럴듯하게(likely) 만드는 계수를 추정합니다.

We now fit a Poisson regression model to the `Bikeshare` data set. Qualitatively, the results are similar to those from linear regression in Section 4.6.1. We again see that bike usage is highest in the spring and fall and during rush hour, and lowest during the winter and in the early morning hours.
이제 `Bikeshare` 데이터 세트에 포아송 회귀 모델을 피팅합니다. 정성적으로, 그 결과는 Section 4.6.1 의 선형 회귀 결과와 유사합니다. 다시 한 번 자전거 사용량이 봄과 가을, 그리고 출퇴근 시간에 가장 높고, 겨울과 이른 아침 시간에 가장 낮음을 볼 수 있습니다.

Some important distinctions between the Poisson regression model and the linear regression model are as follows:
포아송 회귀 모델과 선형 회귀 모델 간의 몇 가지 중요한 차이점은 다음과 같습니다:

- _Interpretation:_ To interpret the coefficients in the Poisson regression model, we must pay close attention to (4.37), which states that an increase in $X_j$ by one unit is associated with a change in $E(Y) = \lambda$ by a factor of $\exp(\beta_j)$. For example, a change in weather from clear to cloudy skies is associated with a change in mean bike usage by a factor of $\exp(-0.08) = 0.923$, i.e. on average, only 92.3% as many people will use bikes when it is cloudy relative to when it is clear.
- _해석:_ 포아송 회귀 모델의 계수를 해석하려면, $X_j$ 가 한 단위 증가하면 $E(Y) = \lambda$ 가 $\exp(\beta_j)$ 의 비율만큼 변한다고 명시하는 (4.37)에 세심한 주의를 기울여야 합니다. 예를 들어, 날씨가 맑은 하늘에서 흐린 하늘로 변하면 평균 자전거 사용량이 $\exp(-0.08) = 0.923$ 의 인자(factor)로 변하는 것과 연관됩니다. 즉, 평균적으로 날씨가 흐릴 때는 맑을 때 대비 92.3% 의 사람만이 자전거를 사용할 것입니다.
- _Mean-variance relationship:_ As mentioned earlier, under the Poisson model, $\lambda = E(Y) = \text{Var}(Y)$. Thus, by modeling bike usage with a Poisson regression, we implicitly assume that mean bike usage in a given hour equals the variance of bike usage during that hour. Thus, the Poisson regression model is able to handle the mean-variance relationship seen in the `Bikeshare` data in a way that the linear regression model is not.
- _평균-분산 관계:_ 앞서 언급했듯이 포아송 모델 하에서 $\lambda = E(Y) = \text{Var}(Y)$ 입니다. 따라서 자전거 사용량을 포아송 회귀로 모델링함으로써, 우리는 특정한 한 시간의 평균 자전거 사용량이 특정 시간 동안의 자전거 사용량의 분산과 같다고 암묵적으로 가정합니다. 따라서 포아송 회귀 모델은 선형 회귀 모델이 할 수 없는 방식으로 `Bikeshare` 데이터에서 볼 수 있는 평균-분산 관계를 처리할 수 있습니다.
- _nonnegative fitted values:_ There are no negative predictions using the Poisson regression model. This is because the Poisson model itself only allows for nonnegative values.
- _음이 아닌 적합 값:_ 포아송 회귀 모델을 사용하면 음수 예측이 없습니다. 이는 포아송 모델 자체가 음이 아닌 값만 허용하기 때문입니다.

---

## Sub-Chapters

[< 4.6.1 Linear Regression On The Bikeshare Data](../4_6_1_linear_regression_on_the_bikeshare_data/trans1.html) | [4.6.3 Generalized Linear Models In Greater Generality >](../4_6_3_generalized_linear_models_in_greater_generality/trans1.html)
