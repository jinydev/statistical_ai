---
layout: default
title: "index"
---

[< 3.2.2.2 Three Model Fit](../3_2_2_2_three_model_fit/index.html) | [3.3 Other Considerations In The Regression Model >](../../../3_3_other_considerations_in_the_regression_model/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# Four: Predictions

Once we have fit the multiple regression model, it is straightforward to apply (3.21) in order to predict the response $Y$ on the basis of a set of values for the predictors $X_1, X_2, \dots, X_p$.

However, there are three sorts of uncertainty associated with this prediction.

1. The coefficient estimates $\hat{\beta}_0, \hat{\beta}_1, \dots, \hat{\beta}_p$ are estimates for $\beta_0, \beta_1, \dots, \beta_p$. That is, the _least squares plane_

$$

\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 X_1 + \dots + \hat{\beta}_p X_p

$$

is only an estimate for the _true population regression plane_

$$

f(X) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p

$$

The inaccuracy in the coefficient estimates is related to the _reducible error_ from Chapter 2. We can compute a _confidence interval_ in order to determine how close $\hat{Y}$ will be to $f(X)$.

2. Of course, in practice assuming a linear model for $f(X)$ is almost always an approximation of reality, so there is an additional source of potentially reducible error which we call _model bias_.

So when we use a linear model, we are in fact estimating the best linear approximation to the true surface.

However, here we will ignore this discrepancy, and operate as if the linear model were correct.

3. Even if we knew $f(X)$ — that is, even if we knew the true values for $\beta_0, \beta_1, \dots, \beta_p$ — the response value cannot be predicted perfectly because of the random error $\epsilon$ in the model (3.20).

In Chapter 2, we referred to this as the _irreducible error_. How much will $Y$ vary from $\hat{Y}$? We use _prediction intervals_ to answer this question.

Prediction intervals are always wider than confidence intervals, because they incorporate both the error in the estimate for $f(X)$ (the reducible error) and the uncertainty as to how much an individual point will differ from the population regression plane (the irreducible error).

We use a _confidence interval_ to quantify the uncertainty surrounding the _average_ `sales` over a large number of cities.

For example, given that $\$100,000$ is spent on `TV` advertising and $\$20,000$ is spent on `radio` advertising in each city, the $95\%$ confidence interval is $[10,985, 11,528]$.

We interpret this to mean that $95\%$ of intervals of this form will contain the true value of $f(X)$.[9]

> [9] In other words, if we collect a large number of data sets like the `Advertising` data set, and we construct a confidence interval for the average `sales` on the basis of each data set (given $\$100,000$ in `TV` and $\$20,000$ in `radio` advertising), then $95\%$ of these confidence intervals will contain the true value of average `sales`.

On the other hand, a _prediction interval_ can be used to quantify the uncertainty surrounding `sales` for a _particular_ city.

Given that $\$100,000$ is spent on `TV` advertising and $\$20,000$ is spent on `radio` advertising in that city the $95\%$ prediction interval is $[7,930, 14,580]$.

We interpret this to mean that $95\%$ of intervals of this form will contain the true value of $Y$ for this city.

Note that both intervals are centered at 11,256, but that the prediction interval is substantially wider than the confidence interval, reflecting the increased uncertainty about `sales` for a given city in comparison to the average `sales` over many locations.

---

## Sub-Chapters


[< 3.2.2.2 Three Model Fit](../3_2_2_2_three_model_fit/index.html) | [3.3 Other Considerations In The Regression Model >](../../../3_3_other_considerations_in_the_regression_model/index.html)
