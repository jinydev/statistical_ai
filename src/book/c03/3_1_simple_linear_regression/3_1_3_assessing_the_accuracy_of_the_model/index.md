---
layout: default
title: "index"
---

[< 3.1.2 Assessing the Accuracy of the Coefficient Estimates](../3_1_2_assessing_the_accuracy_of_the_coefficient_estimates/index.html) | [3.2 Multiple Linear Regression >](../../3_2_multiple_linear_regression/index.html)

> 💡 **학습 팁:** 원문 해석이 어렵다면? 한 줄씩 나란히 번역된 [📖 직역본 보기](./trans1.html)를 추천합니다!

# 3.1.3 Assessing the Accuracy of the Model

Once we have rejected the null hypothesis (3.12) in favor of the alternative hypothesis (3.13), it is natural to want to quantify _the extent to which the model fits the data_. The quality of a linear regression fit is typically assessed using two related quantities: the _residual standard error_ (RSE) and the $$R^2$$ statistic.

> $^4$ In Table 3.1, a small $p$-value for the intercept indicates that we can reject the null hypothesis that $\beta_0 = 0$, and a small $p$-value for `TV` indicates that we can reject the null hypothesis that $\beta_1 = 0$. Rejecting the latter null hypothesis allows us to conclude that there is a relationship between `TV` and `sales`. Rejecting the former allows us to conclude that in the absence of `TV` expenditure, `sales` are non-zero.

| Quantity | Value |

| Residual standard error | 3.26 |

| $F$-statistic | 312.1 |

$$

\text{RSE} = \sqrt{\frac{1}{n-2}\text{RSS}} = \sqrt{\frac{1}{n-2}\sum_{i=1}^n(y_i-\hat{y}_i)^2} \quad (3.15)

$$

Note that RSS was defined in Section 3.1.1, and is given by the formula

$$

\text{RSS} = \sum_{i=1}^n (y_i - \hat{y}_i)^2 \quad (3.16)

$$

In the case of the advertising data, we see from the linear regression output in Table 3.2 that the RSE is 3.26. In other words, actual sales in each market deviate from the true regression line by approximately 3,260 units, on average. Another way to think about this is that even if the model were correct and the true values of the unknown coefficients $\beta_0$ and $\beta_1$ were known exactly, any prediction of sales on the basis of TV advertising would still be off by about 3,260 units on average. Of course, whether or not 3,260 units is an acceptable prediction error depends on the problem context. In the advertising data set, the mean value of `sales` over all markets is approximately 14,000 units, and so the percentage error is $3,260 / 14,000 = 23\%$.

The RSE is considered a measure of the _lack of fit_ of the model (3.5) to the data. If the predictions obtained using the model are very close to the true outcome values—that is, if $y_i \approx \hat{y}_i$ for $i = 1, \dots, n$—then (3.15) will be small, and we can conclude that the model fits the data very well. On the other hand, if $\hat{y}_i$ is very far from $y_i$ for one or more observations, then the RSE may be quite large, indicating that the model doesn’t fit the data well.

## $$R^2$$ Statistic

The RSE provides an absolute measure of lack of fit of the model (3.5) to the data. But since it is measured in the units of $Y$, it is not always clear what constitutes a good RSE. The $$R^2$$ statistic provides an alternative measure of fit. It takes the form of a _proportion_—the proportion of variance explained—and so it always takes on a value between 0 and 1, and is independent of the scale of $Y$.

To calculate $$R^2$$, we use the formula

$$

$$

R^2 = \frac{\text{TSS} - \text{RSS}}{\text{TSS}} = 1 - \frac{\text{RSS}}{\text{TSS}} \quad (3.17)

$$

where $\text{TSS} = \sum (y_i - \bar{y})^2$ is the _total sum of squares_, and $\text{RSS}$ is defined in (3.16). $\text{TSS}$ measures the total variance in the response $Y$, and can be thought of as the amount of variability inherent in the response before the regression is performed. In contrast, $\text{RSS}$ measures the amount of variability that is left unexplained after performing the regression. Hence, $\text{TSS} - \text{RSS}$ measures the amount of variability in the response that is explained (or removed) by performing the regression, and R^2 measures the _proportion of variability in $Y$ that can be explained using $X$_. An R^2 statistic that is close to 1 indicates that a large proportion of the variability in the response is explained by the regression. A number near 0 indicates that the regression does not explain much of the variability in the response; this might occur because the linear model is wrong, or the error variance $\sigma^2$ is high, or both. In Table 3.2, the R^2 was 0.61, and so just under two-thirds of the variability in `sales` is explained by a linear regression on `TV`.
The R^2 statistic (3.17) has an interpretational advantage over the RSE (3.15), since unlike the RSE, it always lies between 0 and 1. However, it can still be challenging to determine what is a _good R^2_ value, and in general, this will depend on the application. For instance, in certain problems in physics, we may know that the data truly comes from a linear model with a small residual error. In this case, we would expect to see an R^2 value that is extremely close to 1, and a substantially smaller R^2 value might indicate a serious problem with the experiment in which the data were generated. On the other hand, in typical applications in biology, psychology, marketing, and other domains, the linear model (3.5) is at best an extremely rough approximation to the data, and residual errors due to other unmeasured factors are often very large. In this setting, we would expect only a very small proportion of the variance in the response to be explained by the predictor, and an R^2 value well below 0.1 might be more realistic!
$$

The $$R^2$$ statistic is a measure of the linear relationship between $X$ and $Y$. Recall that _correlation_, defined as

$$

$$

r = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2} \sqrt{\sum_{i=1}^n (y_i - \bar{y})^2}} \quad (3.18)

$$

is also a measure of the linear relationship between $X$ and $Y$.$^5$ This suggests that we might be able to use $r = \text{Cor}(X, Y)$ instead of R^2 in order to assess the fit of the linear model. In fact, it can be shown that in the simple
> $^5$ We note that in fact, the right-hand side of (3.18) is the sample correlation; thus, it would be more correct to write $\widehat{\text{Cor}}(X, Y)$; however, we omit the "hat" for ease of notation.
80 3. Linear Regression
<br>
**Simple regression of `sales` on `radio`**
<br>
| | Coefficient | Std. error | $t$-statistic | $p$-value |
| :--- | :--- | :--- | :--- | :--- |
| `Intercept` | 9.312 | 0.563 | 16.54 | $< 0.0001$ |
| `radio` | 0.203 | 0.020 | 9.92 | $< 0.0001$ |
**Simple regression of `sales` on `newspaper`**
<br>
| | Coefficient | Std. error | $t$-statistic | $p$-value |
| :--- | :--- | :--- | :--- | :--- |
| `Intercept` | 12.351 | 0.621 | 19.88 | $< 0.0001$ |
| `newspaper` | 0.055 | 0.017 | 3.30 | $0.00115$ |
**TABLE 3.3.** _More simple linear regression models for the_ `Advertising` _data. Coefficients of the simple linear regression model for number of units sold on_ Top: _radio advertising budget and_ Bottom: _newspaper advertising budget. A $\$1,000$ _increase in spending on radio advertising is associated with an average increase in sales by around 203 units, while the same increase in spending on newspaper advertising is associated with an average increase in sales by around 55 units. (Note that the_ `sales` _variable is in thousands of units, and the_ `radio` _and_ `newspaper` _variables are in thousands of dollars.)_
linear regression setting, R^2 = $r^2$. In other words, the squared correlation and the R^2 statistic are identical. However, in the next section we will discuss the multiple linear regression problem, in which we use several predictors simultaneously to predict the response. The concept of correlation between the predictors and the response does not extend automatically to this setting, since correlation quantifies the association between a single pair of variables rather than between a larger number of variables. We will see that R^2 fills this role.
---
$$

---

## Sub-Chapters

This is the document for 3.1.3 Assessing the Accuracy of the Model.

[< 3.1.2 Assessing the Accuracy of the Coefficient Estimates](../3_1_2_assessing_the_accuracy_of_the_coefficient_estimates/index.html) | [3.2 Multiple Linear Regression >](../../3_2_multiple_linear_regression/index.html)
