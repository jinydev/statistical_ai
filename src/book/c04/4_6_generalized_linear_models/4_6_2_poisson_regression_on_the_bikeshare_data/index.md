---
layout: default
title: "index"
---

[< 4.6.1 Linear Regression On The Bikeshare Data](../4_6_1_linear_regression_on_the_bikeshare_data/index.html) | [4.6.3 Generalized Linear Models In Greater Generality >](../4_6_3_generalized_linear_models_in_greater_generality/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 4.6.2 Poisson Regression on the Bikeshare Data

To overcome the inadequacies of linear regression for analyzing the `Bikeshare` data set, we will make use of an alternative approach, called _Poisson regression_. Before we can talk about Poisson regression, we must first introduce the _Poisson distribution_.

Suppose that a random variable $Y$ takes on nonnegative integer values, i.e. $Y \in \{0, 1, 2, \dots\}$. If $Y$ follows the Poisson distribution, then

$$
\text{Pr}(Y = k) = \frac{e^{-\lambda} \lambda^k}{k!} \quad \text{for } k = 0, 1, 2, \dots \quad (4.35)
$$

Here, $\lambda > 0$ is the expected value of $Y$, i.e. $E(Y)$. It turns out that $\lambda$ also equals the variance of $Y$, i.e. $\lambda = E(Y) = \text{Var}(Y)$. This means that if $Y$ follows the Poisson distribution, then the larger the mean of $Y$, the larger its variance.

The Poisson distribution is typically used to model _counts_; this is a natural choice for a number of reasons, including the fact that counts, like the Poisson distribution, take on nonnegative integer values. Rather than modeling the number of bikers, $Y$, as a Poisson distribution with a fixed mean value like $\lambda = 5$, we would like to allow the mean to vary as a function of the covariates. In particular, we consider the following model for the mean $\lambda = E(Y)$:

$$
\lambda(X_1, \dots, X_p) = e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p} \quad (4.36)
$$

or equivalently

$$
\log(\lambda(X_1, \dots, X_p)) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \quad (4.37)
$$

Here, $\beta_0, \beta_1, \dots, \beta_p$ are parameters to be estimated. Together, (4.35) and (4.36) define the Poisson regression model. Notice that in (4.36), we take the _log_ of $\lambda(X_1, \dots, X_p)$ to be linear in $X_1, \dots, X_p$; this ensures that $\lambda(X_1, \dots, X_p)$ takes on nonnegative values for all values of the covariates.

To estimate the coefficients $\beta_0, \beta_1, \dots, \beta_p$, we use the same maximum likelihood approach that we adopted for logistic regression in Section 4.3.2. We estimate the coefficients that make the observed data as likely as possible.

We now fit a Poisson regression model to the `Bikeshare` data set. Qualitatively, the results are similar to those from linear regression in Section 4.6.1. We again see that bike usage is highest in the spring and fall and during rush hour, and lowest during the winter and in the early morning hours.

Some important distinctions between the Poisson regression model and the linear regression model are as follows:
- _Interpretation:_ To interpret the coefficients in the Poisson regression model, we must pay close attention to (4.37), which states that an increase in $X_j$ by one unit is associated with a change in $E(Y) = \lambda$ by a factor of $\exp(\beta_j)$. For example, a change in weather from clear to cloudy skies is associated with a change in mean bike usage by a factor of $\exp(-0.08) = 0.923$, i.e. on average, only 92.3% as many people will use bikes when it is cloudy relative to when it is clear.
- _Mean-variance relationship:_ As mentioned earlier, under the Poisson model, $\lambda = E(Y) = \text{Var}(Y)$. Thus, by modeling bike usage with a Poisson regression, we implicitly assume that mean bike usage in a given hour equals the variance of bike usage during that hour. Thus, the Poisson regression model is able to handle the mean-variance relationship seen in the `Bikeshare` data in a way that the linear regression model is not.
- _nonnegative fitted values:_ There are no negative predictions using the Poisson regression model. This is because the Poisson model itself only allows for nonnegative values.

---

## Sub-Chapters


[< 4.6.1 Linear Regression On The Bikeshare Data](../4_6_1_linear_regression_on_the_bikeshare_data/index.html) | [4.6.3 Generalized Linear Models In Greater Generality >](../4_6_3_generalized_linear_models_in_greater_generality/index.html)
