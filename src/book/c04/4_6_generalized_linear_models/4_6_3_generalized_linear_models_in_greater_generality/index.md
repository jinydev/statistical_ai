---
layout: default
title: "index"
---

[< 4.6.2 Poisson Regression On The Bikeshare Data](../4_6_2_poisson_regression_on_the_bikeshare_data/index.html) | [4.7 Lab Logistic Regression Lda Qda And Knn >](../../4_7_lab_logistic_regression_lda_qda_and_knn/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 4.6.3 Generalized Linear Models in Greater Generality

We have now discussed three types of regression models: linear, logistic and Poisson. These approaches share some common characteristics:

1. Each approach uses predictors $X_1, \dots, X_p$ to predict a response $Y$. We assume that, conditional on $X_1, \dots, X_p$, $Y$ belongs to a certain family of distributions. For linear regression, we typically assume that $Y$ follows a Gaussian or normal distribution. For logistic regression, we assume that $Y$ follows a Bernoulli distribution. Finally, for Poisson regression, we assume that $Y$ follows a Poisson distribution.
2. Each approach models the mean of $Y$ as a function of the predictors. In linear regression, the mean of $Y$ takes the form

$$
\text{E}(Y \mid X_1, \dots, X_p) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \quad (4.39)
$$

i.e. it is a linear function of the predictors. For logistic regression, the mean instead takes the form

$$
\text{E}(Y \mid X_1, \dots, X_p) = \frac{e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p}}{1 + e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p}} \quad (4.40)
$$

while for Poisson regression it takes the form

$$
\text{E}(Y \mid X_1, \dots, X_p) = e^{\beta_0 + \beta_1 X_1 + \dots + \beta_p X_p} \quad (4.41)
$$

Equations (4.39)–(4.41) can be expressed using a _link function_, $\eta$, which applies a transformation to $E(Y \mid X_1, \dots, X_p)$ so that the transformed mean is a linear function of the predictors. That is,

$$
\eta(\text{E}(Y \mid X_1, \dots, X_p)) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p \quad (4.42)
$$

The link functions for linear, logistic and Poisson regression are $\eta(\mu) = \mu$, $\eta(\mu) = \log(\mu / (1 - \mu))$, and $\eta(\mu) = \log(\mu)$, respectively.

The Gaussian, Bernoulli and Poisson distributions are all members of a wider class of distributions, known as the _exponential family_. Other well-known members of this family are the _exponential_ distribution, the _Gamma_ distribution, and the _negative binomial_ distribution. In general, we can perform a regression by modeling the response $Y$ as coming from a particular member of the exponential family, and then transforming the mean of the response so that the transformed mean is a linear function of the predictors via (4.42). Any regression approach that follows this very general recipe is known as a _generalized linear model_ (GLM). Thus, linear regression, logistic regression, and Poisson regression are three examples of GLMs. Other examples not covered here include _Gamma regression_ and _negative binomial regression_.

---

## Sub-Chapters


[< 4.6.2 Poisson Regression On The Bikeshare Data](../4_6_2_poisson_regression_on_the_bikeshare_data/index.html) | [4.7 Lab Logistic Regression Lda Qda And Knn >](../../4_7_lab_logistic_regression_lda_qda_and_knn/index.html)
