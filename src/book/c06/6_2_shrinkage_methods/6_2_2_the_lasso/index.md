---
layout: default
title: "index"
---

# _6.2.2 The Lasso_ 

Ridge regression does have one obvious disadvantage. Unlike best subset, forward stepwise, and backward stepwise selection, which will generally select models that involve just a subset of the variables, ridge regression will include all $p$ predictors in the final model. The penalty $\lambda \sum \beta_j^2$ in (6.5) will shrink all of the coefficients towards zero, but it will not set any of them exactly to zero (unless $\lambda = \infty$). This may not be a problem for prediction accuracy, but it can create a challenge in model interpretation in settings in which the number of variables $p$ is quite large. For example, in the `Credit` data set, it appears that the most important variables are `income`, `limit`, `rating`, and `student`. So we might wish to build a model including just these predictors. However, ridge regression will always generate a model involving all ten predictors. Increasing the value of $\lambda$ will tend to reduce the magnitudes of the coefficients, but will not result in exclusion of any of the variables. 

The _lasso_ is a relatively recent alternative to ridge regression that overcomes this disadvantage. The lasso coefficients, $\hat{\beta}_{\lambda}^L$, minimize the quantity

$$
\sum_{i=1}^n \left( y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij} \right)^2 + \lambda \sum_{j=1}^p |\beta_j| = \text{RSS} + \lambda \sum_{j=1}^p |\beta_j| \quad (6.7)
$$

Comparing (6.7) to (6.5), we see that the lasso and ridge regression have similar formulations. The only difference is that the $\beta_j^2$ term in the ridge regression penalty (6.5) has been replaced by $|\beta_j|$ in the lasso penalty (6.7). In statistical parlance, the lasso uses an $\ell_1$ (pronounced “ell 1”) penalty instead of an $\ell_2$ penalty. The $\ell_1$ norm of a coefficient vector $\beta$ is given by $\|\beta\|_1 = \sum |\beta_j|$.

As with ridge regression, the lasso shrinks the coefficient estimates towards zero. However, in the case of the lasso, the $\ell_1$ penalty has the effect of forcing some of the coefficient estimates to be exactly equal to zero when the tuning parameter $\lambda$ is sufficiently large. Hence, much like best subset selection, the lasso performs _variable selection_. As a result, models generated from the lasso are generally much easier to interpret than those produced by ridge regression. We say that the lasso yields _sparse_ models—that is, sparse models that involve only a subset of the variables. As in ridge regression, selecting a good value of $\lambda$ for the lasso is critical; we defer this discussion to Section 6.2.3, where we use cross-validation. 

6.2 Shrinkage Methods 245 

![Figure 6.6](./img/6_6.png)

**FIGURE 6.6.** _The standardized lasso coefficients on the_ `Credit` _data set are shown as a function of $\lambda$ and $\|\hat{\beta}_{\lambda}^L\|_1 / \|\hat{\beta}\|_1$._

As an example, consider the coefficient plots in Figure 6.6, which are generated from applying the lasso to the `Credit` data set. When $\lambda = 0$, then the lasso simply gives the least squares fit, and when $\lambda$ becomes sufficiently large, the lasso gives the null model in which all coefficient estimates equal zero. However, in between these two extremes, the ridge regression and lasso models are quite different from each other. Moving from left to right in the right-hand panel of Figure 6.6, we observe that at first the lasso results in a model that contains only the `rating` predictor. Then `student` and `limit` enter the model almost simultaneously, shortly followed by `income`. Eventually, the remaining variables enter the model. Hence, depending on the value of $\lambda$, the lasso can produce a model involving any number of variables. In contrast, ridge regression will always include all of the variables in the model, although the magnitude of the coefficient estimates will depend on $\lambda$.

Another Formulation for Ridge Regression and the Lasso 

One can show that the lasso and ridge regression coefficient estimates solve the problems

$$
\begin{align*}
\underset{\beta}{\text{minimize}} \sum_{i=1}^n \left( y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij} \right)^2 \quad &\text{subject to} \quad \sum_{j=1}^p |\beta_j| \le s \quad (6.8) \\
\underset{\beta}{\text{minimize}} \sum_{i=1}^n \left( y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij} \right)^2 \quad &\text{subject to} \quad \sum_{j=1}^p \beta_j^2 \le s \quad (6.9)
\end{align*}
$$

respectively. In other words, for every value of $\lambda$, there is some $s$ such that the Equations (6.7) and (6.8) will give the same lasso coefficient estimates. Similarly, for every value of $\lambda$ there is a corresponding $s$ such that Equations (6.5) and (6.9) will give the same ridge regression coefficient estimates. 

246 6. Linear Model Selection and Regularization 

When $p = 2$, then (6.8) indicates that the lasso coefficient estimates have the smallest RSS out of all points that lie within the diamond defined by $|\beta_1| + |\beta_2| \le s$. Similarly, the ridge regression estimates have the smallest RSS out of all points that lie within the circle defined by $\beta_1^2 + \beta_2^2 \le s$.

We can think of (6.8) as follows. When we perform the lasso we are trying to find the set of coefficient estimates that lead to the smallest RSS, subject to the constraint that there is a _budget_ $s$ for how large $\sum_{j=1}^p |\beta_j|$ can be. When $s$ is extremely large, then this budget is not very restrictive, and so the coefficient estimates can be large. In fact, if $s$ is large enough that the least squares solution falls within the budget, then (6.8) will simply yield the least squares solution. In contrast, if $s$ is small, then $\sum_{j=1}^p |\beta_j|$ must be small in order to avoid violating the budget. Similarly, (6.9) indicates that when we perform ridge regression, we seek a set of coefficient estimates such that the RSS is as small as possible, subject to the requirement that $\sum_{j=1}^p \beta_j^2$ not exceed the budget $s$. The formulations (6.8) and (6.9) reveal a close connection between the lasso, ridge regression, and best subset selection. Consider the problem

$$
\underset{\beta}{\text{minimize}} \sum_{i=1}^n \left( y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij} \right)^2 \quad \text{subject to} \quad \sum_{j=1}^p I(\beta_j \ne 0) \le s \quad (6.10)
$$

Here $I(\beta_j \ne 0)$ is an indicator variable: it takes on a value of 1 if $\beta_j \ne 0$, and equals zero otherwise. Then (6.10) amounts to finding a set of coefficient estimates such that RSS is as small as possible, subject to the constraint that no more than $s$ coefficients can be nonzero. The problem (6.10) is equivalent to best subset selection. Unfortunately, solving (6.10) is computationally infeasible when $p$ is large, since it requires considering all $\binom{p}{s}$ models containing $s$ predictors. Therefore, we can interpret ridge regression and the lasso as computationally feasible alternatives to best subset selection that replace the intractable form of the budget in (6.10) with forms that are much easier to solve. Of course, the lasso is much more closely related to best subset selection, since the lasso performs feature selection for $s$ sufficiently small in (6.8), while ridge regression does not. 

---

## Sub-Chapters (하위 목차)

### The Variable Selection Property of the Lasso (라쏘의 변수 선택 특성 메커니즘)
* [문서로 이동하기](./6_2_2_1_the_variable_selection_property_of_the_lasso/)

어떻게 라쏘가 계수를 정확히 0으로 타겟 쳐내주어 희소(Sparse)한 모델을 기하학적으로 생성하는지, 그 수학적 원리를 마름모 궤적으로 시각화하여 관찰합니다.

### Comparing the Lasso and Ridge Regression (라쏘와 릿지 회귀의 구조적 차이 비교)
* [문서로 이동하기](./6_2_2_2_comparing_the_lasso_and_ridge_regression/)

소수의 변수만 반응에 유의미할 땐 라쏘가, 다수 변수들이 전반적으로 미세하게 얽혀 영향을 미칠 땐 릿지가 상대적으로 유리할 가능성이 높다는 구도를 설명합니다.

### A Simple Special Case for Ridge Regression and the Lasso (릿지와 라쏘의 특수한 교안 사례)
* [문서로 이동하기](./6_2_2_3_a_simple_special_case_for_ridge_regression_and_the_lasso/)

변수 행렬 데이터 디자인이 완벽한 상호 직교(Orthogonal) 구조라 가정할 때, 두 기법 방식이 원래 OLS 선형 회귀 계수 추정값을 어떻게 소프트/하드로 깎는지 단순화해 증명합니다.
