---
layout: default
title: "trans1"
---

[< 4.3.1 The Logistic Model](../4_3_1_the_logistic_model/trans1.html) | [4.3.3 Making Predictions >](../4_3_3_making_predictions/trans1.html)

> 💡 **학습 팁:** 통계 수식과 용어가 낯설고 어렵다면? 아주 쉽게 풀어쓴 [📖 쉬운 해설(의역본) 보기](./trans2.html)를 추천합니다!

# 4.3.2 Estimating the Regression Coefficients
# 4.3.2. 회귀 계수 추정 (Estimating the Regression Coefficients)

The coefficients $\beta_0$ and $\beta_1$ in (4.2) are unknown, and must be estimated based on the available training data.
식 (4.2) 안에 있는 계수 $\beta_0$와 $\beta_1$은 미지수이며, 가용한 훈련 데이터를 바탕으로 추정되어야 합니다.

In Chapter 3, we used the least squares approach to estimate the unknown linear regression coefficients.
3장에서 우리는 미지의 선형 회귀 계수를 추정하기 위해 최소 제곱법을 사용했습니다.

Although we could use (non-linear) least squares to fit the model (4.4), the more general method of _maximum likelihood_ is preferred, since it has better statistical properties.
비록 우리가 모형 (4.4)를 적합하기 위해 (비선형) 최소 제곱법을 사용할 수도 있겠지만, 통계적 성질이 더 우수한 보다 일반적인 방식인 **최대 우도법(maximum likelihood)** 이 선호됩니다.

The basic intuition behind using maximum likelihood to fit a logistic regression model is as follows: we seek estimates for $\beta_0$ and $\beta_1$ such that the predicted probability $\hat{p}(x_i)$ of default for each individual, using (4.2), corresponds as closely as possible to the individual's observed default status.
로지스틱 회귀 모델을 적합하기 위해 최대 우도법을 사용하는 기본 직관은 다음과 같습니다: 우리는 식 (4.2)를 사용하여 계산된 각 개인의 파산 예측 확률 $\hat{p}(x_i)$가 해당 개인의 실제 관측된 파산 상태와 가능한 가장 밀접하게 일치하도록 하는 $\beta_0$ 및 $\beta_1$의 추정치를 찾습니다.

In other words, we try to find $\hat{\beta}_0$ and $\hat{\beta}_1$ such that plugging these estimates into the model for $p(X)$, given in (4.2), yields a number close to one for all individuals who defaulted, and a number close to zero for all individuals who did not.
다시 말해, 우리는 식 (4.2)로 주어진 $p(X)$ 모델에 추정치들을 대입했을 때 파산한 모든 개인에 대해서는 1에 가까운 수치를, 파산하지 않은 모든 개인에 대해서는 0에 가까운 수치를 산출하게 만드는 $\hat{\beta}_0$와 $\hat{\beta}_1$을 찾으려 시도합니다.

This intuition can be formalized using a mathematical equation called a _likelihood function_:
이러한 직관은 **우도 함수(likelihood function)** 라고 불리는 수학 방정식을 사용하여 공식화될 수 있습니다:

$$
\ell(\beta_0, \beta_1) = \prod_{i: y_i=1} p(x_i) \prod_{i^{\prime}: y_{i^{\prime}}=0} (1 - p(x_{i^{\prime}})) \quad (4.5)
$$

The estimates $\hat{\beta}_0$ and $\hat{\beta}_1$ are chosen to _maximize_ this likelihood function.
추정치 $\hat{\beta}_0$ 및 $\hat{\beta}_1$은 이 우도 함수를 **최대화(maximize)** 하도록 선택됩니다.

Maximum likelihood is a very general approach that is used to fit many of the non-linear models that we examine throughout this book.
최대 우도 기법은 이 책 전반에서 살펴보는 다수의 비선형 모델을 적합시키는 데 사용되는 매우 일반적인 접근법입니다.

In the linear regression setting, the least squares approach is in fact a special case of maximum likelihood.
선형 회귀 설정에서 최소 제곱법은 사실 최대 우도법의 특수한 경우입니다.

The mathematical details of maximum likelihood are beyond the scope of this book.
최대 우도법의 수학적 세부 사항은 이 책의 범위를 벗어납니다.

However, in general, logistic regression and other models can be easily fit using statistical software such as `R` or `Python`, and so we do not need to concern ourselves with the details of the maximum likelihood fitting procedure.
그러나 일반적으로 로지스틱 회귀와 여타 모형들은 `R`이나 `Python`같은 통계 소프트웨어를 사용하여 쉽게 적합시킬 수 있으므로, 최대 우도 적합 절차의 세부사항에 대해 스스로를 너무 염려할 필요는 없습니다.

Table 4.1 shows the coefficient estimates and related information that result from fitting a logistic regression model on the `Default` data in order to predict the probability of `default = Yes` using `balance` .
표 4.1은 `balance`를 사용하여 `default = Yes`일 확률을 예측하기 위해 `Default` 데이터에 로지스틱 회귀 모델을 적합시킨 결과 도출된 계수 추정치와 관련 정보를 보여줍니다.

We see that $\hat{\beta}_1 = 0.0055$; this indicates that an increase in `balance` is associated with an increase in the probability of `default`.
우리는 $\hat{\beta}_1 = 0.0055$임을 볼 수 있으며; 이는 `balance`의 증가가 `default` 확률의 증가와 연관되어 있음을 나타냅니다.

To be precise, a one-unit increase in `balance` is associated with an increase in the log odds of `default` by 0.0055 units.
정확히 말하자면, `balance`의 1 단위 증가는 `default`의 로그 오즈 값이 0.0055 단위 증가하는 것과 연관됩니다.

Many aspects of the logistic regression output shown in Table 4.1 are similar to the linear regression output of Chapter 3.
표 4.1에 표시된 로지스틱 회귀 분석 결과의 많은 측면이 3장의 선형 회귀 분석 결과와 유사합니다.

For example, we can measure the accuracy of the coefficient estimates by computing their standard errors.
예를 들어, 계수 추정치의 표준 오차를 계산함으로써 그 정확도를 측정할 수 있습니다.

The _z_-statistic in Table 4.1 plays the same role as the _t_-statistic in the linear regression output.
표 4.1의 **z-통계량(z-statistic)** 은 선형 회귀 결과의 *t*-통계량과 동일한 역할을 수행합니다.

For instance, the _z_-statistic associated with $\beta_1$ is equal to $\hat{\beta}_1 / \text{SE}(\hat{\beta}_1)$, and so a large (absolute) value of the _z_-statistic indicates evidence against the null hypothesis $H_0 : \beta_1 = 0$.
예를 들어, $\beta_1$과 관련된 z-통계량은 $\hat{\beta}_1 / \text{SE}(\hat{\beta}_1)$와 같으며, 따라서 z-통계량의 (절댓값이) 크다는 것은 귀무 가설 $H_0 : \beta_1 = 0$에 반대되는 증거를 나타냅니다.

This null hypothesis implies that the probability of `default` does not depend on `balance` .
이 귀무 가설은 `default` 확률이 `balance`에 의존하지 않음을 의미합니다.

Since the _p_-value associated with `balance` in Table 4.1 is tiny, we can reject $H_0$.
표 4.1에서 `balance`와 연관된 *p*-값이 매우 작기 때문에 우리는 귀무가설 $H_0$를 기각할 수 있습니다.

In other words, we conclude that there is indeed an association between `balance` and probability of `default`.
다시 말해서, 우리는 진정으로 `balance`와 `default` 확률 사이에 연관성이 결론지어 존재한다고 판단합니다.

The estimated intercept in Table 4.1 is typically not of interest; its main purpose is to adjust the average fitted probabilities to the proportion of ones in the data (in this case, the overall default rate).
표 4.1에서 추정된 절편은 일반적으로 주요 관심 대상이 아닙니다; 그 주된 목적은 평균 적합 확률을 데이터 내 값이 1인 비율(이 경우 전체 파산율)에 맞추어 조정하는 것입니다.

This is the document for this topic.
이것은 이 주제에 대한 문서입니다.

---

## Sub-Chapters

[< 4.3.1 The Logistic Model](../4_3_1_the_logistic_model/trans1.html) | [4.3.3 Making Predictions >](../4_3_3_making_predictions/trans1.html)
