---
layout: default
title: "index"
---

[< 4.3.1 The Logistic Model](../4_3_1_the_logistic_model/index.html) | [4.3.3 Making Predictions >](../4_3_3_making_predictions/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 4.3.2 Estimating the Regression Coefficients

The coefficients $\beta_0$ and $\beta_1$ in (4.2) are unknown, and must be estimated based on the available training data. In Chapter 3, we used the least squares approach to estimate the unknown linear regression coefficients. Although we could use (non-linear) least squares to fit the model (4.4), the more general method of _maximum likelihood_ is preferred, since it has better statistical properties. The basic intuition behind using maximum likelihood to fit a logistic regression model is as follows: we seek estimates for $\beta_0$ and $\beta_1$ such that the predicted probability $\hat{p}(x_i)$ of default for each individual, using (4.2), corresponds as closely as possible to the individual's observed default status. In other words, we try to find $\hat{\beta}_0$ and $\hat{\beta}_1$ such that plugging these estimates into the model for $p(X)$, given in (4.2), yields a number close to one for all individuals who defaulted, and a number close to zero for all individuals who did not. This intuition can be formalized using a mathematical equation called a _likelihood function_:

$$
\ell(\beta_0, \beta_1) = \prod_{i: y_i=1} p(x_i) \prod_{i^{\prime}: y_{i^{\prime}}=0} (1 - p(x_{i^{\prime}})) \quad (4.5)
$$

The estimates $\hat{\beta}_0$ and $\hat{\beta}_1$ are chosen to _maximize_ this likelihood function. Maximum likelihood is a very general approach that is used to fit many of the non-linear models that we examine throughout this book. In the linear regression setting, the least squares approach is in fact a special case of maximum likelihood. The mathematical details of maximum likelihood are beyond the scope of this book. However, in general, logistic regression and other models can be easily fit using statistical software such as `R` or `Python`, and so we do not need to concern ourselves with the details of the maximum likelihood fitting procedure.

Table 4.1 shows the coefficient estimates and related information that result from fitting a logistic regression model on the `Default` data in order to predict the probability of `default = Yes` using `balance` . We see that $\hat{\beta}_1 = 0.0055$; this indicates that an increase in `balance` is associated with an increase in the probability of `default`. To be precise, a one-unit increase in `balance` is associated with an increase in the log odds of `default` by 0.0055 units.

Many aspects of the logistic regression output shown in Table 4.1 are similar to the linear regression output of Chapter 3. For example, we can measure the accuracy of the coefficient estimates by computing their standard errors. The _z_-statistic in Table 4.1 plays the same role as the _t_-statistic in the linear regression output. For instance, the _z_-statistic associated with $\beta_1$ is equal to $\hat{\beta}_1 / \text{SE}(\hat{\beta}_1)$, and so a large (absolute) value of the _z_-statistic indicates evidence against the null hypothesis $H_0 : \beta_1 = 0$. This null hypothesis implies that the probability of `default` does not depend on `balance` . Since the _p_-value associated with `balance` in Table 4.1 is tiny, we can reject $H_0$. In other words, we conclude that there is indeed an association between `balance` and probability of `default`. The estimated intercept in Table 4.1 is typically not of interest; its main purpose is to adjust the average fitted probabilities to the proportion of ones in the data (in this case, the overall default rate).

---

## Sub-Chapters


[< 4.3.1 The Logistic Model](../4_3_1_the_logistic_model/index.html) | [4.3.3 Making Predictions >](../4_3_3_making_predictions/index.html)
