---
layout: default
title: "index"
---

[< 6 6. Collinearity](../3_3_other_considerations_in_the_regression_model/3_3_3_potential_problems/6_6._collinearity/index.html) | [3.5 Comparison Of Linear Regression With K Nearest Neighbors >](../3_5_comparison_of_linear_regression_with_k_nearest_neighbors/index.html)


> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 3.4 The Marketing Plan

We now briefly return to the seven questions about the `Advertising` data that we set out to answer at the beginning of this chapter.

1. _Is there a relationship between sales and advertising budget?_

This question can be answered by fitting a multiple regression model of `sales` onto `TV`, `radio`, and `newspaper`, as in (3.20), and testing the hypothesis $H_0 : \beta_\text{TV} = \beta_\text{radio} = \beta_\text{newspaper} = 0$.

In Section 3.2.2, we showed that the $F$-statistic can be used to determine whether or not we should reject this null hypothesis.

In this case the $p$-value corresponding to the $F$-statistic in Table 3.6 is very low, indicating clear evidence of a relationship between advertising and sales.

2. _How strong is the relationship?_

We discussed two measures of model accuracy in Section 3.1.3.

First, the RSE estimates the standard deviation of the response from the population regression line.

For the `Advertising` data, the RSE is $1.69$ units while the mean value for the response is $14.022$, indicating a percentage error of roughly $12\%$.

Second, the $R^2$ statistic records the percentage of variability in the response that is explained by the predictors.

The predictors explain almost $90\%$ of the variance in `sales`.

The RSE and $R^2$ statistics are displayed in Table 3.6.

3. _Which media are associated with sales?_

To answer this question, we can examine the $p$-values associated with each predictor's $t$-statistic (Section 3.1.2).

In the multiple linear regression displayed in Table 3.4, the $p$-values for `TV` and `radio` are low, but the $p$-value for `newspaper` is not.

This suggests that only `TV` and `radio` are related to `sales`.

In Chapter 6 we explore this question in greater detail.

4. _How large is the association between each medium and sales?_

We saw in Section 3.1.2 that the standard error of $\hat{\beta}_j$ can be used to construct confidence intervals for $\beta_j$.

For the `Advertising` data, we can use the results in Table 3.4 to compute the $95\%$ confidence intervals for the coefficients in a multiple regression model using all three media budgets as predictors.

The confidence intervals are as follows: $(0.043, 0.049)$ for `TV`, $(0.172, 0.206)$ for `radio`, and $(-0.013, 0.011)$ for `newspaper`.

The confidence intervals for `TV` and `radio` are narrow and far from zero, providing evidence that these media are related to `sales`.

But the interval for `newspaper` includes zero, indicating that the variable is not statistically significant given the values of `TV` and `radio`.

We saw in Section 3.3.3 that collinearity can result in very wide standard errors.

Could collinearity be the reason that the confidence interval associated with `newspaper` is so wide?

The VIF scores are $1.005$, $1.145$, and $1.145$ for `TV`, `radio`, and `newspaper`, suggesting no evidence of collinearity.

In order to assess the association of each medium individually on sales, we can perform three separate simple linear regressions.

Results are shown in Tables 3.1 and 3.3.

There is evidence of an extremely strong association between `TV` and `sales` and between `radio` and `sales`.

There is evidence of a mild association between `newspaper` and `sales`, when the values of `TV` and `radio` are ignored.

5. _How accurately can we predict future sales?_

The response can be predicted using (3.21).

The accuracy associated with this estimate depends on whether we wish to predict an individual response, $Y = f(X) + \epsilon$, or the average response, $f(X)$ (Section 3.2.2).

If the former, we use a prediction interval, and if the latter, we use a confidence interval.

Prediction intervals will always be wider than confidence intervals because they account for the uncertainty associated with $\epsilon$, the irreducible error.

6. _Is the relationship linear?_

In Section 3.3.3, we saw that residual plots can be used in order to identify non-linearity.

If the relationships are linear, then the residual plots should display no pattern.

In the case of the `Advertising` data, we observe a non-linear effect in Figure 3.5, though this effect could also be observed in a residual plot.

In Section 3.3.2, we discussed the inclusion of transformations of the predictors in the linear regression model in order to accommodate non-linear relationships.

7. _Is there synergy among the advertising media?_

The standard linear regression model assumes an additive relationship between the predictors and the response.

An additive model is easy to interpret because the association between each predictor and the response is unrelated to the values of the other predictors.

However, the additive assumption may be unrealistic for certain data sets.

In Section 3.3.2, we showed how to include an interaction term

---

## Sub-Chapters


[< 6 6. Collinearity](../3_3_other_considerations_in_the_regression_model/3_3_3_potential_problems/6_6._collinearity/index.html) | [3.5 Comparison Of Linear Regression With K Nearest Neighbors >](../3_5_comparison_of_linear_regression_with_k_nearest_neighbors/index.html)
